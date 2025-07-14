from datetime import date
from typing import Optional, Union, List
from loguru import logger
from ..growatt_types import DeviceType
from ..pydantic_models import PlantInfo
from ..pydantic_models.api_v4 import DeviceListV4
from ..pydantic_models.device import (
    DeviceTypeInfo,
    DeviceEnergyDay,
    DeviceDatalogger,
    DeviceCreateDate,
)
from ..plant.plant import Plant
from ..session.growatt_api_session import GrowattApiSession


class Device:
    """
    https://www.showdoc.com.cn/262556420217021/11038523729597006
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def get_device_type(  # noqa: C901 'Device.get_device_type' is too complex (12)
        self,
        device_sn: str,
    ) -> Optional[DeviceType]:
        """
        convenience method to get device type by device_sn

        will use following endpoints to retrieve device type
        * device.type_info()
        * device.list()
        * plant.list_devices() (via device.get_plant())

        Args:
            device_sn (str): Device serial number

        Returns:
            DeviceType
            e.g. DeviceType.MIN
        """

        # 1. get device type via v1 API device/check/sn
        device_type_info = self.type_info(device_sn=device_sn)
        if device_type_info.result == 1:
            device_type = DeviceType.from_device_type_info(device_type=device_type_info.device_type)
            if device_type and device_type != DeviceType.OTHER:
                return DeviceType.from_device_type_info(device_type=device_type_info.device_type)
            else:
                logger.warning(
                    f"Unknown device type {device_type_info.device_type} = {device_type} for device {device_sn} (v1 type_info). Trying fallback methods..."
                )
        else:
            logger.warning(f"Error {device_type_info.result} querying v1 type_info. Trying fallback methods...")

        # 2. get device type via v4 API device.list()
        _page = 0
        while _page < 20:
            _page += 1
            device_list = self.list(page=_page)
            if device_list.error_code != 0:
                logger.warning(
                    f"Error {device_list.error_code}: '{device_list.error_msg}' querying v4 device list. Trying fallback methods..."
                )
                break
            device_types = {x.device_sn: x.device_type for x in device_list.data.data}
            if device_sn in device_types:
                device_type_raw = device_types[device_sn]
                device_type = DeviceType.from_device_list(device_types[device_sn])
                if device_type and device_type != DeviceType.OTHER:
                    return device_type
                else:
                    logger.warning(
                        f"Unknown device type {device_type_raw} = {device_type} for device {device_sn} (v4 list). Trying fallback methods..."
                    )
                    break
            if device_list.data.last_pager:
                logger.warning(f"Device {device_sn} not found in v4 device list. Trying fallback methods...")
                break  # reached last page (without match)

        # 3. get device type via v1 API plant.list_devices()
        # get plant for device
        plant_info = self.get_plant(device_sn=device_sn)
        if plant_info.error_code != 0:
            logger.warning(
                f"Error {plant_info.error_code}: '{plant_info.error_msg}' querying v1 plant info. No further fallbacks available."
            )
            return None
        plant_id = plant_info.data.plant.plant_id
        # get devices for plant
        api_plant = Plant(session=self.session)
        plant_devices = api_plant.list_devices(
            plant_id=plant_id, limit=100
        )  # no paging as plant with >100 devices are rare
        if plant_devices.error_code != 0:
            logger.warning(
                f"Error {plant_devices.error_code}: '{plant_devices.error_msg}' querying v1 plant devices. No further fallbacks available."
            )
            return None
        device_types = {x.device_sn: x.type for x in plant_devices.data.devices}
        device_type_raw = device_types.get(device_sn)
        if not device_type_raw:
            logger.warning(
                f"Unknown device type {device_type_raw} for device {device_sn} (v1 plant device). No further fallbacks available."
            )
            return None
        device_type = DeviceType.from_plant_list_devices(device_type=device_type_raw)
        if device_type and device_type != DeviceType.OTHER:
            return device_type
        else:
            logger.warning(
                f"Unknown device type {device_type_raw} = {device_type} for device {device_sn} (v1 plant device). No further fallbacks available."
            )
            return None

    def list(
        self,
        page: Optional[int] = None,
    ) -> DeviceListV4:
        """
        Device List
        Retrieve the list of devices associated with the distributor, installer, and terminal account of the secret token.
        The devices obtained through this interface are the only ones allowed to fetch data from.
        Devices not on the list are not permitted to retrieve data.
        https://www.showdoc.com.cn/2540838290984246/11292915113214428

        Returned "device_type" values are: (according to https://www.showdoc.com.cn/2540838290984246/11292914311318022 and https://www.showdoc.com.cn/p/b42ee029e131c68c4dbfdd89285c0ec1)
        * inv
        * storage
        * max
        * sph
        * spa
        * min
        * wit
        * sph-s
        * noah

        Rate limit(s):
        * Fetch frequency is limited to once every 5 seconds.

        Args:
            page (Optional[int]): Page number, default 1 (1~n)

        Returns:
            DeviceList
            {   'data': {   'count': 7,
                            'data': [   {'create_date': datetime.datetime(2021, 6, 29, 12, 2, 46), 'datalogger_sn': None, 'device_sn': 'HPJ0BF20FU', 'device_type': 'max'},
                                        {'create_date': datetime.datetime(2024, 11, 30, 17, 37, 26), 'datalogger_sn': 'QMN000BZP0000000', 'device_sn': 'BZP0000000', 'device_type': 'min'}
                                        {'create_date': datetime.datetime(2017, 1, 18, 14, 9, 53), 'datalogger_sn': None, 'device_sn': 'PR34211399', 'device_type': 'inv'}],
                            'last_pager': True,
                            'not_pager': False,
                            'other': None,
                            'page_size': 100,
                            'pages': 1,
                            'start_count': 0},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        response = self.session.post(
            endpoint="new-api/queryDeviceList",
            params={"page": page},
        )

        return DeviceListV4.model_validate(response)

    def type_info(
        self,
        device_sn: str,
    ) -> DeviceTypeInfo:
        """
        3.5 Query device type according to SN
        Query the interface of the device type according to SN
        https://www.showdoc.com.cn/262556420217021/6117996523846727

        Returned "obj":
        1 = Inverter
        2 = Energy storage machine
        3 = collector
        4 = other

        Returned "device_type":
        16 = Inverter
        17 = SPH
        18 = MAX
        19 = SPA
        22 = MIN
        81 = PCS
        82 = HPS
        83 = PBD
        96 = Storage
        218 = WIT
        260 = SPH-S

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Args:
            device_sn (str): Device serial number of datalogger / inverter / ...

        Returns:
            DeviceTypeInfo
            e.g. (inverter)
            {
                "device_type":22,
                "dtc": 5203,
                "have_meter": False,
                "in_system": True,
                "model": 'NEO 800M-X',
                "msg": 'inverter',
                "normal_power": 800,
                "obj": 1,
                "result": 1,
            }
            e.g. (datalogger)
            {
                "device_type": 0,
                "dtc": 0,
                "have_meter": False,
                "in_system": False,
                "model": 'ShineWeFi',
                "msg": 'datalog',
                "normal_power": 0,
                "obj": 3,
                "result": 1,
            }
        """

        response = self.session.get(
            endpoint="device/check/sn",
            params={
                "dataloggerSn": device_sn,
            },
        )

        return DeviceTypeInfo.model_validate(response)

    def energy_day(
        self,
        device_sn: str,
        date_: Optional[date] = None,
    ) -> DeviceEnergyDay:
        """
        3.41 Obtaining the historical power generation of
        An interface to get the historical power generation of the device on a certain day
        https://www.showdoc.com.cn/262556420217021/6118030327488881

        Note:
            Only applicable to devices with device type 3 (other/datalogger) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10005: inverter not existing

        Args:
            device_sn (str): Inverter serial number
            date_ (Optional[date]): Date to query data for - defaults to today

        Returns:
            DeviceEnergyDay
            e.g.
            {
                "data": 168.89999389648438,
                "error_code": 0,
                "error_msg": None,
                "datalogger_sn": 'KHD1850045',
                "device_sn": 'NOD1851006'
            }
        """

        date_ = date_ or date.today()

        response = self.session.get(
            endpoint="device/inverter/day_energy",
            params={
                "device_sn": device_sn,
                "date": date_.strftime("%Y-%m-%d"),
            },
        )

        return DeviceEnergyDay.model_validate(response)

    def get_datalogger(
        self,
        device_sn: str,
    ) -> DeviceDatalogger:
        """
        3.43 Query collector based on SN
        Query collector according to SN
        https://www.showdoc.com.cn/262556420217021/6118045304653161

        Specific error codes:
        * 10003: the device SN is empty
        * 10005: the device does not exist

        Args:
            device_sn (str): Inverter serial number

        Returns:
            DeviceDatalogger
            e.g.
            {
                'data': {
                    'datalogSN': 'QMN0000000000000'
                },
                'error_code': 0,
                'error_msg': None
            }
        """

        response = self.session.post(
            endpoint="device/sn_datalog",
            data={
                "device_sn": device_sn,
            },
        )

        return DeviceDatalogger.model_validate(response)

    def create_date(
        self,
        device_sn: Union[str, List[str]],
        page: Optional[int] = None,
    ) -> DeviceCreateDate:
        """
        Get device creation dates in batches (from October
        https://www.showdoc.com.cn/262556420217021/9462219631565222

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error

        Args:
            device_sn (str): Inverter serial number or list of (multiple) inverter serial numbers (max 100)
            page (Optional[int]): page number, default 1, max 2

        Returns:
            DeviceCreateDate
            e.g.
            {
                'data': {
                    'BZP0000000': {
                        'createTime': '2024-11-30 17:37:00',
                        'datalogSn': 'QMN000BZP0000000',
                        'deviceName': 'MIN',
                        'deviceSn': 'BZP0000000',
                        'deviceType': 'CLOVE',
                        'lastUpdateTime': '2025-02-24 23:03:00',
                        'tableName': ''
                    }
                },
                'error_code': 0,
                'error_msg': ''
            }
        """
        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/all/create_date",
            data={
                "pageNum": page or 1,
                "devices": device_sn,
            },
        )

        return DeviceCreateDate.model_validate(response)

    def get_plant(self, device_sn: str) -> PlantInfo:
        """
        Retrieve plant data (similar to list() by device_id (e.g. inverter id))

        2.10 Get the plant information of a device
        Obtain an interface for the plant information of a device
        https://www.showdoc.com.cn/262556420217021/1494064780850155

        Rate limit(s):
        * Get the frequency once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Account does not exist
        * 10003: Device serial number is empty
        * 10004: Device type is empty
        * 10005: Device does not exist

        Args:
            device_sn (str): Device serial number (non-collector serial number)

        Returns:
            PlantInfo
            {   'data': {   'plant': {   'city': 'Shenzhen',
                                         'country': 'China',
                                         'create_date': datetime.date(2018, 12, 12),
                                         'current_power': None,
                                         'image_url': '2.png',
                                         'installer': 'API interface test vendor',
                                         'latitude': 22.6,
                                         'latitude_d': None,
                                         'latitude_f': None,
                                         'locale': None,
                                         'longitude': 113.9,
                                         'name': 'API interface test power station',
                                         'operator': 'API interface test vendor',
                                         'peak_power': 20.0,
                                         'plant_id': 24765,
                                         'status': 4,
                                         'total_energy': 15.699999809265137,
                                         'user_id': 33}},
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="plant/sn_plant",
            data={
                "device_sn": device_sn,
            },
        )

        return PlantInfo.model_validate(response)
