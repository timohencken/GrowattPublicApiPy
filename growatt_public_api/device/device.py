from datetime import date
from typing import Optional, Union, List

import truststore

from pydantic_models.device import (
    DeviceList,
    DataloggerList,
    DeviceTypeInfo,
    DataloggerValidation,
    DeviceEnergyDay,
    DeviceDatalogger,
    DeviceCreateDate,
    DeviceAdd,
    DataloggerAdd,
    DataloggerDelete,
)

truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


class Device:
    """
    https://www.showdoc.com.cn/262556420217021/11038523729597006
    TODO: Maybe refactor to distinguish Datalogger and Inverter?
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def datalogger_add(
        self,
        user_id: int,
        plant_id: int,
        datalogger_sn: str,
    ) -> DataloggerAdd:
        """
        3.1 Add collector
        Add the interface of the collector
        https://www.showdoc.com.cn/262556420217021/6117939786619819

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: power station ID is empty or collector serial number error
        * 10003: collector already exists
        * 10004: power station does not exist
        * 10005: user does not exist
        * 10006: user ID is empty

        Args:
            user_id (int): User ID ("c_user_id" as returned in register()), e.g. 74
            plant_id (int): Power Station ID
            datalogger_sn (str): Datalogger serial number

        Returns:
            DataloggerAdd
            {   'data': None,
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/datalogger/add",
            data={
                "plant_id": plant_id,
                "sn": datalogger_sn,
                "c_user_id": user_id,
            },
        )

        return DataloggerAdd.model_validate(response)

    def datalogger_delete(
        self,
        plant_id: int,
        datalogger_sn: str,
    ) -> DataloggerDelete:
        """
        3.2 Delete collector
        Delete the interface of the collector
        https://www.showdoc.com.cn/262556420217021/6117952419029888


        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: power station ID is empty or the collector serial number is wrong
        * 10003: power station does not exist
        * 10004: collector does not exist

        Args:
            plant_id (int): Power Station ID
            datalogger_sn (str): Datalogger serial number

        Returns:
            DataloggerDelete
            {   'data': None,
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/datalogger/delete",
            data={
                "plant_id": plant_id,
                "sn": datalogger_sn,
            },
        )

        return DataloggerDelete.model_validate(response)

    def list(
        self,
        plant_id: int,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> DeviceList:
        """
        3.3 Obtain a power station equipment list
        Interface to get a list of power station equipment
        https://www.showdoc.com.cn/262556420217021/6117958613377445

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: power station ID is empty
        * 10003: power station does not exist

        Note:
            returned "device_type" mappings:
             1: inverter (including MAX)
             2: storage
             3: other (datalogger, smart meter, environmental sensor, ...)
             4: max (single MAX)
             5: sph
             6: spa
             7: min
             8: pcs
             9: hps
            10: pbd
            11: groboost

        Args:
            plant_id (int): Power Station ID
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            DeviceList
            e.g.
            {
                "data": {
                    "count": 3,
                    "devices": [
                        {
                            "device_sn": "ZT00100001",
                            "last_update_time": "2018-12-13 11:03:52",
                            "model": "A0B0D0T0PFU1M3S4",
                            "lost": True,
                            "status": 0,
                            "manufacturer": "Growatt",
                            "device_id": 116,
                            "datalogger_sn": "CRAZT00001",
                            "type": 1
                        },
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
        """

        response = self.session.get(
            endpoint="device/list",
            params={
                "plant_id": plant_id,
                "page": page,
                "perpage": limit,
            },
        )

        return DeviceList.model_validate(response)

    def datalogger_list(
        self,
        plant_id: int,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> DataloggerList:
        """
        3.4 Get a list of power station collectors
        The interface to obtain the collector list of a certain power station
        https://www.showdoc.com.cn/262556420217021/6117971175828060

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: power station ID is empty
        * 10003: power station does not exist

        Args:
            plant_id (int): Power Station ID
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            DataloggerList
            e.g.
            {
                "data": {
                    "peak_power_actual": {
                        "treeID": "PLANT_24765",
                        "flatPeriodPrice": 0,
                        "longitudeText": "null°null′null″",
                        "storage_eChargeToday": 0,
                        "storage_BattoryPercentage": 0,
                        "dataLogList": [],
                        "designCompany": "API interface testing manufacturer",
                        "timezoneText": "GMT+8",
                        "defaultPlant": False,
                        "peakPeriodPrice": 0,
                        "formulaCoal": 0.4000000059604645,
                        "storage_eDisChargeToday": 0,
                        "city": "Shenzhen",
                        "nominalPower": 20000,
                        "unitMap": None,
                        "timezone": 8,
                        "level": 1,
                        "formulaMoneyUnitId": "rmb",
                        "currentPacTxt": "0",
                        "panelTemp": 0,
                        "fixedPowerPrice": 0,
                        "imgPath": "css/img/plant.gif",
                        "storage_TotalToGrid": 0,
                        "moneyUnitText": "￥",
                        "locationImgName": "1.png",
                        "prToday": "0",
                        "energyMonth": 0,
                        "deviceCount": 0,
                        "plantName": "API interface test plant",
                        "plantImgName": "2.png",
                        "eToday": 0,
                        "etodaySo2Text": "0",
                        "country": "China",
                        "emonthMoneyText": "0",
                        "longitude_d": "",
                        "longitude_f": "",
                        "formulaMoney": 1.2000000476837158,
                        "userAccount": "API interface test",
                        "mapLat": "",
                        "longitude_m": "",
                        "createDateText": "2018-12-12",
                        "formulaSo2": 0.800000011920929,
                        "valleyPeriodPrice": 0,
                        "mapLng": "",
                        "energyYear": 0,
                        "treeName": "API interface test power station",
                        "plant_lat": "22.6",
                        "onLineEnvCount": 0,
                        "etodayCo2Text": "0",
                        "latitudeText": "null°null′null″",
                        "etotalSo2Text": "0",
                        "children": [],
                        "hasDeviceOnLine": 0,
                        "id": 24765,
                        "etodayCoalText": "0",
                        "etodayMoney": 0,
                        "createDate": {"time": 1544544000000, "minutes": 0, "seconds": 0, "hours": 0, "month": 11, "year": 118, "timezoneOffset": -480, "day": 3, "date": 12 },
                        "prMonth": "0",
                        "mapCity": "",
                        "etotalMoney": 0,
                        "envTemp": 0,
                        "storage_TodayToGrid": 0,
                        "alias": "",
                        "etotalCo2Text": "0",
                        "emonthCo2Text": "0",
                        "eTotal": 0,
                        "etotalMoneyText": "0",
                        "formulaCo2": 0.6000000238418579,
                        "irradiance": 0,
                        "emonthSo2Text": "0",
                        "hasStorage": 0,
                        "windAngle": 0,
                        "etotalCoalText": "0",
                        "windSpeed": 0,
                        "emonthCoalText": "0",
                        "parentID": "",
                        "EYearMoneyText": "0",
                        "etodayMoneyText": "0",
                        "plant_lng": "113.9",
                        "pairViewUserAccount": "",
                        "latitude_m": "",
                        "userBean": None,
                        "storage_TotalToUser": 0,
                        "storage_TodayToUser": 0,
                        "isShare": False,
                        "currentPac": 0,
                        "latitude_d": "",
                        "latitude_f": ""
                    },
                    "count": 1,
                    "dataloggers": [
                        {
                            "last_update_time": {"time": 1544670394000, "minutes": 6, "seconds": 34, "hours": 11, "month": 11, "timezoneOffset": -480, "year": 118, "day": 4, "date": 13},
                            "model": "ShineWifiBox",
                            "sn": "CRAZT00001",
                            "lost": True,
                            "manufacturer": "Growatt",
                            "type": 0
                        }
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
        """

        response = self.session.get(
            endpoint="device/datalogger/list",
            params={
                "plant_id": plant_id,
                "page": page,
                "perpage": limit,
            },
        )

        return DataloggerList.model_validate(response)

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

    def datalogger_validate(
        self,
        datalogger_sn: str,
        validation_code: Union[int, str],
    ) -> DataloggerValidation:
        """
        3.6 Check whether the collector SN and check code
        Interface to detect whether the collector SN and check code are qualified
        https://www.showdoc.com.cn/262556420217021/6118001776634753

        Note:
            Only applicable to devices with device type 3 (other/datalogger) returned by device.list()

        Specific error codes:
        * 10001: the collector serial number is empty or the length is incorrect
        * 10002: the collector serial number does not match the check code
        * 10003: the collector already exists and has been added

        Args:
            datalogger_sn (str): Datalogger serial number
            validation_code (Union[int, str]): Verification Code

        Returns:
            DataloggerValidationResult

        """

        response = self.session.post(
            endpoint="device/datalogger/validate",
            data={
                "datalogSn": datalogger_sn,
                "valiCode": validation_code,
            },
        )

        return DataloggerValidation.model_validate(response)

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
            Only applicable to devices with device type 3 (other/datalogger) returned by device.list()

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
        # TODO device_? or inverter_?

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

    def add(
        self,
        plant_id: int,
        device_sn: str,
        user_id: int,
    ) -> DeviceAdd:
        """
        Assign inverter to user account.
        If possible, please use device.datalogger_add() instead.

        Add device associated account interface
        The terminal account relationship associated with the device SN is used when the collector SN is not known,
         but the device SN is known, but there is a certain delay.
        The association relationship is not necessarily real-time, only when the device is online.
        It will be associated in real time.
        If the device is not online, it will be associated after the device is online.
        https://www.showdoc.com.cn/262556420217021/9462221142197198

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error

        Args:
            plant_id (int): Power Station ID
            device_sn (str): Inverter serial number
            user_id (int): User ID

        Returns:
            DeviceAdd
            e.g.
            {
                "error_code": 0,
                "error_msg": ""
            }
        """
        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/sn/add",
            data={
                "plant_id": plant_id,
                "sn": device_sn,
                "c_user_id": user_id,
            },
        )

        return DeviceAdd.model_validate(response)
