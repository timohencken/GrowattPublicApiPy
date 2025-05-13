from datetime import date
from typing import Optional, Union, List

import truststore

from pydantic_models import PlantInfo
from pydantic_models.device import (
    DeviceTypeInfo,
    DeviceEnergyDay,
    DeviceDatalogger,
    DeviceCreateDate,
)

truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


class Device:
    """
    https://www.showdoc.com.cn/262556420217021/11038523729597006
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

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
        83 = PDB
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
