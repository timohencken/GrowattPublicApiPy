from typing import Union, Optional
from ..pydantic_models import EnvSensorList, SmartMeterList
from ..pydantic_models.device import (
    DataloggerValidation,
)
from ..session.growatt_api_session import GrowattApiSession


class Datalogger:
    """
    https://www.showdoc.com.cn/262556420217021/11038523729597006
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def validate(
        self,
        datalogger_sn: str,
        validation_code: Union[int, str],
    ) -> DataloggerValidation:
        """
        3.6 Check whether the collector SN and check code
        Interface to detect whether the collector SN and check code are qualified
        https://www.showdoc.com.cn/262556420217021/6118001776634753

        Note:
            Only applicable to devices with device type 3 (other/datalogger) returned by plant.list_devices()

        Specific error codes:
        * 10001: the collector serial number is empty or the length is incorrect
        * 10002: the collector serial number does not match the check code
        * 10003: the collector already exists and has been added

        Args:
            datalogger_sn (str): Datalogger serial number
            validation_code (Union[int, str]): Verification Code

        Returns:
            DataloggerValidation

        """

        response = self.session.post(
            endpoint="device/datalogger/validate",
            data={
                "datalogSn": datalogger_sn,
                "valiCode": validation_code,
            },
        )

        return DataloggerValidation.model_validate(response)

    def list_env_sensors(
        self,
        datalogger_sn: str,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> EnvSensorList:
        """
        Get the list of environmental detectors according...
        According to the collector SN to obtain the interface of the environmental detector list
        https://www.showdoc.com.cn/262556420217021/6131376900470247

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Collector SN error
        * 10003: Collector does not exist

        Note:
            returned "device_type" mappings:
            48: environmental tester
        Note:
            returned "address" will be required for other API calls in this class

        Args:
            datalogger_sn (str): Datalogger serial number
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            EnvSensorList
            {   'data': {   'count': 1,
                            'datalogger_sn': 'CRAZT00001',
                            'envs': [   {   'address': 2,
                                            'datalogger_sn': 'CRAZT00001',
                                            'device_name': 'ENV_DEVICE',
                                            'device_type': '48',
                                            'last_update_time': datetime.datetime(2019, 1, 9, 10, 38, 11),
                                            'lost': False}]},
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/env/env_list",
            params={
                "datalog_sn": datalogger_sn,
                "page": page,
                "perpage": limit,
            },
        )

        return EnvSensorList.model_validate(response)

    def list_smart_meters(
        self,
        datalogger_sn: str,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> SmartMeterList:
        """
        Obtain the list of smart meters according to the c
        Get the interface of smart meter list according to the collector SN
        https://www.showdoc.com.cn/262556420217021/6131333103798986

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Collector SN error
        * 10003: Collector does not exist

        Note:
            returned "device_type" mappings:
            64: smart meter
            66: SDM one-way meter
            67: SDM three-way meter
            70: CHNT one-way meter
            71: CHNT three-way meter
        Note:
            returned "address" will be required for other API calls in this class

        Args:
            datalogger_sn (str): Datalogger serial number
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            SmartMeterList
            {   'data': {   'count': 1,
                            'datalogger_sn': 'CRAZT00001',
                            'meters': [   {   'address': 1,
                                              'datalogger_sn': 'CRAZT00001',
                                              'device_name': 'AMMETER',
                                              'device_type': '64',
                                              'last_update_time': datetime.datetime(2019, 1, 9, 10, 33, 6),
                                              'lost': False}]},
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/ammeter/meter_list",
            params={
                "datalog_sn": datalogger_sn,
                "page": page,
                "perpage": limit,
            },
        )

        return SmartMeterList.model_validate(response)
