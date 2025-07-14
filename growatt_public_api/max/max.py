from datetime import date, timedelta
from typing import Optional, Union, List
from ..api_v4.api_v4 import ApiV4
from ..growatt_types import DeviceType
from ..pydantic_models.api_v4 import (
    MaxDetailsV4,
    MaxEnergyV4,
    MaxEnergyHistoryV4,
    MaxEnergyHistoryMultipleV4,
    SettingWriteV4,
)
from ..pydantic_models.max import (
    MaxSettingRead,
    MaxSettingWrite,
    MaxDetails,
    MaxEnergyOverview,
    MaxEnergyHistory,
    MaxAlarms,
    MaxEnergyOverviewMultiple,
    MaxEnergyOverviewMultipleItem,
)
from ..session.growatt_api_session import GrowattApiSession


class Max:
    """
    endpoints for MAX inverters
    https://www.showdoc.com.cn/262556420217021/6120369315865619
    """

    session: GrowattApiSession
    _api_v4: ApiV4
    device_sn: Optional[str] = None

    def __init__(self, session: GrowattApiSession, device_sn: Optional[str] = None) -> None:
        self.session = session
        self._api_v4 = ApiV4(session)
        self.device_sn = device_sn

    def _device_sn(self, device_sn: Optional[Union[str, List[str]]]) -> Union[str, List[str]]:
        """
        Use device_sn explicitly provided, fallback to the one from the instance
        """
        device_sn = device_sn or self.device_sn
        if device_sn is None:
            raise AttributeError("device_sn must be provided")
        return device_sn

    def setting_read(
        self,
        device_sn: Optional[str] = None,
        parameter_id: Optional[str] = None,
        start_address: Optional[int] = None,
        end_address: Optional[int] = None,
    ) -> MaxSettingRead:
        """
        Read Max setting parameter interface
        https://www.showdoc.com.cn/262556420217021/6127601154776404

        Note:
            Only applicable to devices with device type 4 (max) returned by plant.list_devices()

        This method allows to read
        * predefined settings
          * pass parameter_id, do not pass start_address or end_address
        * any register value
          * pass start_address and end_address, do not pass parameter_id
        see setting_write() for more details

        Specific error codes:
        * 10001: Reading failed
        * 10002: Device does not exist
        * 10003: Device offline
        * 10004: Collector serial number is empty
        * 10005: Collector offline
        * 10006: Collector type does not support reading Get function
        * 10007: The collector version does not support the reading function
        * 10008: The collector connects to the server error, please restart and try again
        * 10009: The read setting parameter type does not exist

        Args:
            device_sn (str): MAX SN
            parameter_id (Optional[str]): parameter ID - specify either parameter_id ort start/end_address
            start_address (Optional[int]): register address to start reading from - specify either parameter_id ort start/end_address
            end_address (Optional[int]): register address to stop reading at

        Returns:
            MaxSettingRead
            e.g.
            {
                "data": "0",
                "error_code": 0,
                "error_msg": ""
            }
        """

        if parameter_id is None and start_address is None:
            raise ValueError("specify either parameter_id or start_address/end_address")
        elif parameter_id is not None and start_address is not None:
            raise ValueError("specify either parameter_id or start_address/end_address - not both.")
        elif parameter_id is not None:
            # named parameter
            start_address = 0
            end_address = 0
        else:
            # using register-number mode
            parameter_id = "set_any_reg"
            if start_address is None:
                start_address = end_address
            if end_address is None:
                end_address = start_address

        response = self.session.post(
            endpoint="readMaxParam",
            data={
                "device_sn": self._device_sn(device_sn),
                "paramId": parameter_id,
                "startAddr": start_address,
                "endAddr": end_address,
            },
        )

        return MaxSettingRead.model_validate(response)

    # noinspection PyUnusedLocal
    def setting_write(
        self,
        parameter_id: str,
        parameter_value_1: Union[str, int],
        parameter_value_2: Optional[Union[str, int]] = None,
        parameter_value_3: Optional[Union[str, int]] = None,
        parameter_value_4: Optional[Union[str, int]] = None,
        parameter_value_5: Optional[Union[str, int]] = None,
        parameter_value_6: Optional[Union[str, int]] = None,
        parameter_value_7: Optional[Union[str, int]] = None,
        parameter_value_8: Optional[Union[str, int]] = None,
        parameter_value_9: Optional[Union[str, int]] = None,
        parameter_value_10: Optional[Union[str, int]] = None,
        parameter_value_11: Optional[Union[str, int]] = None,
        parameter_value_12: Optional[Union[str, int]] = None,
        parameter_value_13: Optional[Union[str, int]] = None,
        parameter_value_14: Optional[Union[str, int]] = None,
        parameter_value_15: Optional[Union[str, int]] = None,
        parameter_value_16: Optional[Union[str, int]] = None,
        parameter_value_17: Optional[Union[str, int]] = None,
        parameter_value_18: Optional[Union[str, int]] = None,
        parameter_value_19: Optional[Union[str, int]] = None,
        device_sn: Optional[str] = None,
    ) -> MaxSettingWrite:
        """
        Max parameter setting interface
        Max parameter setting interface interface
        https://www.showdoc.com.cn/262556420217021/6127597452472600

        Note:
            Only applicable to devices with device type 4 (max) returned by plant.list_devices()

        This method allows to set
        * predefined settings (see table below)
        * any register value (see table below for most relevant settings, google for "Growatt Inverter Modbus RTU Protocol V1.20" for more)

        Predefined settings
        ========================+=======================================+===========================+============================================================================
        description             | parameter_id                          | parameter_value_[n]       | comment
        ========================+=======================================+===========================+============================================================================
        Set switch machine      | max_cmd_on_off                        | [1]: 0000 or 0001         | 0000 = off, 0001 = on
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set active power        | pv_active_p_rate                      | [1]: 0 ~ 100              | [1]: percentage
                                |                                       | [2]: 0 or 1               | [2]: 0 = no memory, 1 = memory
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set PF value            | pv_power_factor                       | [1]: -0.8 ~ -1            |
                                |                                       |    or 0.8 ~  1            |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------

        Register settings
        =================
        google for "Growatt Inverter Modbus RTU Protocol V1.20" for more

        Specific error codes:
        * 10001: system error
        * 10002: Min server error
        * 10003: Min offline
        * 10004: Min serial number is empty
        * 10005: collector offline
        * 10006: setting parameter type does not exist
        * 10007: The parameter value is empty
        * 10008: The parameter value is not within the range
        * 10009: The date and time format is wrong
        * 10012: Min does not exist
        * 10013: The end time cannot be less than the start time

        Args:
            device_sn (str): energy storage machine SN
            parameter_id (str): parameter ID - pass "set_any_reg" to write register address
            parameter_value_1 (Union[str, int]): parameter value 1
            parameter_value_2 (Optional[Union[str, int]]): parameter value 2
            parameter_value_3 (Optional[Union[str, int]]): parameter value 3
            parameter_value_4 (Optional[Union[str, int]]): parameter value 4
            parameter_value_5 (Optional[Union[str, int]]): parameter value 5
            parameter_value_6 (Optional[Union[str, int]]): parameter value 6
            parameter_value_7 (Optional[Union[str, int]]): parameter value 7
            parameter_value_8 (Optional[Union[str, int]]): parameter value 8
            parameter_value_9 (Optional[Union[str, int]]): parameter value 9
            parameter_value_10 (Optional[Union[str, int]]): parameter value 10
            parameter_value_11 (Optional[Union[str, int]]): parameter value 11
            parameter_value_12 (Optional[Union[str, int]]): parameter value 12
            parameter_value_13 (Optional[Union[str, int]]): parameter value 13
            parameter_value_14 (Optional[Union[str, int]]): parameter value 14
            parameter_value_15 (Optional[Union[str, int]]): parameter value 15
            parameter_value_16 (Optional[Union[str, int]]): parameter value 16
            parameter_value_17 (Optional[Union[str, int]]): parameter value 17
            parameter_value_18 (Optional[Union[str, int]]): parameter value 18
            parameter_value_19 (Optional[Union[str, int]]): parameter value 19

        Returns:
            MinSettingWrite
            e.g. (success)
            {
                "data": "",
                "error_code": 0,
                "error_msg": ""
            }
        """

        # put parameters to a dict to make handling easier
        parameters = {}
        for i in range(1, 20):
            parameters[i] = eval(f"parameter_value_{i}")

        if parameter_id == "set_any_reg":
            assert parameters[1] is not None, "register address must be provided"
            assert parameters[2] is not None, "new value must be provided"
            for i in range(3, 20):
                assert parameters[i] is None, f"parameter {i} must not be used for set_any_reg"
        else:
            assert parameters[1] is not None, "new value must be provided"

        # API docs: if there is no value, pass empty string ""
        for i in range(2, 20):
            if parameters[i] is None:
                parameters[i] = ""

        # parameter values must be string
        for i in range(1, 20):
            parameters[i] = str(parameters[i])

        response = self.session.post(
            endpoint="maxSet",
            data={
                "max_sn": self._device_sn(device_sn),
                "type": parameter_id,
                **{f"param{i}": parameters[i] for i in range(1, 20)},
            },
        )

        return MaxSettingWrite.model_validate(response)

    def setting_write_on_off(
        self,
        power_on: bool,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the power on and off using "new-api" endpoint
        Turn device on/off
        https://www.showdoc.com.cn/2540838290984246/11330750679726415

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            power_on (bool): True = Power On, False = Power Off

        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}
        """

        return self._api_v4.setting_write_on_off(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.MAX,
            power_on=power_on,
        )

    def setting_write_active_power(
        self,
        active_power_percent: int,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the active power using "new-api" endpoint
        Set the active power percentage of the device based on the device type and SN of the device.
        https://www.showdoc.com.cn/2540838290984246/11330751643769012

        Note:
        * most devices can be configured to 0 ~ 100 %
        * NOAH devices can be configured to 0 ~ 800 W

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            active_power_percent (int): Percentage of active power, range 0-100

        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_active_power(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.MAX,
            active_power=active_power_percent,
        )

    def details(
        self,
        device_sn: Optional[str] = None,
    ) -> MaxDetails:
        """
        Get basic Max information
        Interface to get basic information of Max
        https://www.showdoc.com.cn/262556420217021/6120369315865619

        Note:
            Only applicable to devices with device type 4 (max) returned by plant.list_devices()

        Args:
            device_sn (str): Max device SN

        Returns:
            MaxDetails
            {   'data': {   'address': 1,
                            'alias': 'TLMAX00B01',
                            'big_device': False,
                            'children': [],
                            'communication_version': 'ti1.-12288',
                            'datalogger_sn': 'SATA818009',
                            'e_today': 0.0,
                            'e_total': 0.0,
                            'energy_month': 0.0,
                            'fw_version': 'TI1.0',
                            'group_id': -1,
                            'id': 0,
                            'img_path': './css/img/status_gray.gif',
                            'inner_version': 'tiaaxxxxxx01',
                            'last_update_time': {'date': 11, 'day': 5, 'hours': 10, 'minutes': 49, 'month': 0, 'seconds': 36, 'time': 1547174976000, 'timezone_offset': -480, 'year': 119},
                            'last_update_time_text': datetime.datetime(2019, 1, 11, 10, 49, 36),
                            'level': 6,
                            'location': None,
                            'lost': False,
                            'model': 6182500000,
                            'model_text': 'A0B0D0T0PFU1M8S1',
                            'parent_id': 'LIST_SATA818009_3',
                            'plant_id': 0,
                            'plantname': None,
                            'port_name': 'ShinePano-SATA818009',
                            'power': 0.0,
                            'record': None,
                            'serial_num': 'TLMAX00B01',
                            'status': 3,
                            'status_text': 'max.status.error',
                            'tcp_server_ip': '127.0.0.1',
                            'tree_id': 'TLMAX00B01',
                            'tree_name': 'TLMAX00B01',
                            'updating': False,
                            'user_name': None},
                'datalogger_sn': 'SATA818009',
                'device_sn': 'TLMAX00B01',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/max/max_data_info",
            params={
                "device_sn": self._device_sn(device_sn),
            },
        )

        return MaxDetails.model_validate(response)

    def details_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> MaxDetailsV4:
        """
        Batch device information using "new-api" endpoint
        Retrieve basic information of devices in bulk based on device SN.
        https://www.showdoc.com.cn/2540838290984246/11292915673945114

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            MaxDetailsV4
            e.g.
            {   'data': {   'max': [   {   'active_rate': 0.0,
                                           'address': 1,
                                           'alias': 'HPJ0BF20FU',
                                           'backflow_default_power': 0.0,
                                           'big_device': False,
                                           'children': None,
                                           'communication_version': 'ZBab-0002',
                                           'datalogger_sn': 'BLE4BEQ0BW',
                                           'device_type': 1,
                                           'dtc': 5001,
                                           'e_today': 0.0,
                                           'e_total': 0.0,
                                           'energy_day': 0.0,
                                           'energy_day_map': {},
                                           'energy_month': 0.0,
                                           'energy_month_text': '0',
                                           'export_limit': 0.0,
                                           'export_limit_power_rate': 0.0,
                                           'fac_high': 0.0,
                                           'fac_low': 0.0,
                                           'frequency_high_limit': 0.0,
                                           'frequency_low_limit': 0.0,
                                           'fw_version': 'TJ1.0',
                                           'group_id': -1,
                                           'id': 0,
                                           'img_path': './css/img/status_gray.gif',
                                           'inner_version': 'TJAA08020002',
                                           'last_update_time': 1716534733000,
                                           'last_update_time_text': datetime.datetime(2024, 5, 24, 15, 12, 13),
                                           'lcd_language': 0,
                                           'level': 6,
                                           'location': None,
                                           'lost': False,
                                           'max_set_bean': None,
                                           'model': 720575940631003386,
                                           'model_text': 'S0AB00D00T00P0FU01M00FA',
                                           'normal_power': 25000.0,
                                           'on_off': False,
                                           'parent_id': 'LIST_BLE4BEQ0BW_3',
                                           'pf': 0.0,
                                           'pf_model': 0,
                                           'pflinep1_lp': 0.0,
                                           'pflinep1_pf': 0.0,
                                           'pflinep2_lp': 0.0,
                                           'pflinep2_pf': 0.0,
                                           'pflinep3_lp': 0.0,
                                           'pflinep3_pf': 0.0,
                                           'pflinep4_lp': 0.0,
                                           'pflinep4_pf': 0.0,
                                           'plant_id': 0,
                                           'plant_name': None,
                                           'port_name': 'ShinePano - BLE4BEQ0BW',
                                           'power': 0.0,
                                           'power_max': None,
                                           'power_max_text': None,
                                           'power_max_time': None,
                                           'pv_pf_cmd_memory_state': 0,
                                           'reactive_rate': 0.0,
                                           'record': None,
                                           'serial_num': 'HPJ0BF20FU',
                                           'status': 1,
                                           'status_text': 'max.status.normal',
                                           'str_num': 0,
                                           'sys_time': None,
                                           'tcp_server_ip': '47.119.22.101',
                                           'timezone': 8.0,
                                           'tree_id': 'HPJ0BF20FU',
                                           'tree_name': 'HPJ0BF20FU',
                                           'updating': False,
                                           'user_name': None,
                                           'vac_high': 0.0,
                                           'vac_low': 0.0,
                                           'voltage_high_limit': 0.0,
                                           'voltage_low_limit': 0.0}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.details(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.MAX,
        )

    def energy(
        self,
        device_sn: Optional[str] = None,
    ) -> MaxEnergyOverview:
        """
        Get the latest real-time data from Max
        Interface to get the latest real-time data of Max
        https://www.showdoc.com.cn/262556420217021/6127572916461964

        Note:
            Only applicable to devices with device type 4 (max) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: Max does not exist
        * 10003: device SN error

        Args:
            device_sn (str): Max serial number

        Returns:
            MaxEnergyOverview
            e.g.
            {   'data': {   'address': 0,
                            'again': False,
                            'alias': None,
                            'apf_status': 0.0,
                            'apf_status_text': 'None',
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 11, 'day': 5, 'hours': 10, 'minutes': 49, 'month': 0, 'seconds': 36, 'time': 1547174976000, 'timezone_offset': -480, 'year': 119},
                                            'time_in_millis': 1547174976000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2019,
                                            'weeks_in_week_year': 52},
                            'comp_har_ir': 0,
                            'comp_har_is': 0,
                            'comp_har_it': 0,
                            'comp_qr': 0,
                            'comp_qs': 0,
                            'comp_qt': 0,
                            'ct_har_ir': 0,
                            'ct_har_is': 0,
                            'ct_har_it': 0,
                            'ct_ir': 0,
                            'ct_is': 0,
                            'ct_it': 0,
                            'ct_qr': 0,
                            'ct_qs': 0,
                            'ct_qt': 0,
                            'current_string1': 0.0,
                            'current_string10': 0.0,
                            'current_string11': 0.0,
                            'current_string12': 0.0,
                            'current_string13': 0.0,
                            'current_string14': 0.0,
                            'current_string15': 0.0,
                            'current_string16': 0.0,
                            'current_string2': 0.0,
                            'current_string3': 0.0,
                            'current_string4': 0.0,
                            'current_string5': 0.0,
                            'current_string6': 0.0,
                            'current_string7': 0.0,
                            'current_string8': 0.0,
                            'current_string9': 0.0,
                            'datalogger_sn': None,
                            'day': None,
                            'debug1': '0, 0, 0, 0, 0, 0, 0, 0',
                            'debug2': '0, 0, 0, 0, 0, 0, 0, 0',
                            'derating_mode': 0,
                            'e_rac_today': 0.0,
                            'e_rac_total': 0.0,
                            'eac_today': 0.0,
                            'eac_total': 0.0,
                            'epv1_today': 0.0,
                            'epv1_total': 0.0,
                            'epv2_today': 0.0,
                            'epv2_total': 0.0,
                            'epv3_today': 0.0,
                            'epv3_total': 0.0,
                            'epv4_today': 0.0,
                            'epv4_total': 0.0,
                            'epv5_today': 0.0,
                            'epv5_total': 0.0,
                            'epv6_today': 0.0,
                            'epv6_total': 0.0,
                            'epv7_today': 0.0,
                            'epv7_total': 0.0,
                            'epv8_today': 0.0,
                            'epv8_total': 0.0,
                            'epv_total': 0.0,
                            'fac': 0.0,
                            'fault_code1': 2,
                            'fault_code2': 0,
                            'fault_type': 2,
                            'fault_value': 3,
                            'gfci': 0.0,
                            'i_pid_pvape': 0.0,
                            'i_pid_pvbpe': 0.0,
                            'i_pid_pvcpe': 0.0,
                            'i_pid_pvdpe': 0.0,
                            'i_pid_pvepe': 0.0,
                            'i_pid_pvfpe': 0.0,
                            'i_pid_pvgpe': 0.0,
                            'i_pid_pvhpe': 0.0,
                            'iacr': 0.0,
                            'iacs': 0.0,
                            'iact': 0.0,
                            'id': 0,
                            'ipm_temperature': 0.0,
                            'ipv1': 0.0,
                            'ipv2': 0.0,
                            'ipv3': 0.0,
                            'ipv4': 0.0,
                            'ipv5': 0.0,
                            'ipv6': 0.0,
                            'ipv7': 0.0,
                            'ipv8': 0.0,
                            'lost': True,
                            'max_bean': None,
                            'n_bus_voltage': 0.0,
                            'op_fullwatt': 0.0,
                            'operating_mode': None,
                            'p_bus_voltage': 0.0,
                            'pac': 0.0,
                            'pacr': 0.0,
                            'pacs': 0.0,
                            'pact': 0.0,
                            'pf': -1.0,
                            'pid_bus': 0,
                            'pid_fault_code': 0,
                            'pid_status_text': 'Lost',
                            'power_today': 0.0,
                            'power_total': 0.0,
                            'ppv': 0.0,
                            'ppv1': 0.0,
                            'ppv2': 0.0,
                            'ppv3': 0.0,
                            'ppv4': 0.0,
                            'pv_iso': 0.0,
                            'r_dci': 0.0,
                            'rac': 0.0,
                            'real_op_percent': 0.0,
                            's_dci': 0.0,
                            'serial_num': 'TLMAX00B01',
                            'status': 3,
                            'status_text': 'Fault',
                            'strUnblance': 0,
                            'str_Break': 0,
                            'str_Fault': 0,
                            'str_unmatch': 0,
                            'temperature': 0.0,
                            'temperature2': 0.0,
                            'temperature3': 0.0,
                            'temperature4': 0.0,
                            'temperature5': 25.899999618530273,
                            'time': datetime.datetime(2019, 1, 11, 10, 49, 36),
                            'time_total': 0.0,
                            'v_pid_pvape': 0.0,
                            'v_pid_pvbpe': 0.0,
                            'v_pid_pvcpe': 0.0,
                            'v_pid_pvdpe': 0.0,
                            'v_pid_pvepe': 0.0,
                            'v_pid_pvfpe': 0.0,
                            'v_pid_pvgpe': 0.0,
                            'v_pid_pvhpe': 0.0,
                            'vac_rs': 0.0,
                            'vac_st': 0.0,
                            'vac_tr': 0.0,
                            'vacr': 0.0,
                            'vacs': 0.0,
                            'vact': 0.0,
                            'vpv1': 0.0,
                            'vpv2': 0.0,
                            'vpv3': 0.0,
                            'vpv4': 0.0,
                            'vpv5': 0.0,
                            'vpv6': 0.0,
                            'vpv7': 0.0,
                            'vpv8': 0.0,
                            'w_pid_fault_value': 0,
                            'w_string_status_value': 0,
                            'warn_bit': 0,
                            'warn_code': 0,
                            'warn_code1': None,
                            'warning_value1': 0,
                            'warning_value2': 0,
                            'warning_value3': 0,
                            'with_time': False},
                'datalogger_sn': 'SATA818009',
                'device_sn': 'TLMAX00B01',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/max/max_last_data",
            data={
                "max_sn": self._device_sn(device_sn),
            },
        )

        return MaxEnergyOverview.model_validate(response)

    def energy_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> MaxEnergyV4:
        """
        Batch equipment data information using "new-api" endpoint
        Retrieve the last detailed data for multiple devices based on their SN and device type.
        https://www.showdoc.com.cn/2540838290984246/11292915898375566

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            MaxEnergyV4
            e.g.
            {   'data': {   'max': [   {   'address': 0,
                                           'afci_pv1': 0,
                                           'afci_pv2': 0,
                                           'afci_status': 0,
                                           'again': False,
                                           'alias': None,
                                           'apf_status': 0.0,
                                           'apf_status_text': None,
                                           'calendar': 1714113885020,
                                           'comp_har_ir': 0.0,
                                           'comp_har_is': 0.0,
                                           'comp_har_it': 0.0,
                                           'comp_qr': 0.0,
                                           'comp_qs': 0.0,
                                           'comp_qt': 0.0,
                                           'ct_har_ir': 0.0,
                                           'ct_har_is': 0.0,
                                           'ct_har_it': 0.0,
                                           'ct_ir': 0.0,
                                           'ct_is': 0.0,
                                           'ct_it': 0.0,
                                           'ct_qr': 0.0,
                                           'ct_qs': 0.0,
                                           'ct_qt': 0.0,
                                           'current_string1': 0.0,
                                           'current_string10': 0.0,
                                           'current_string11': 0.0,
                                           'current_string12': 0.0,
                                           'current_string13': 0.0,
                                           'current_string14': 0.0,
                                           'current_string15': 0.0,
                                           'current_string16': 0.0,
                                           'current_string17': 0.0,
                                           'current_string18': 0.0,
                                           'current_string19': 0.0,
                                           'current_string2': 0.0,
                                           'current_string21': 0.0,
                                           'current_string22': 0.0,
                                           'current_string23': 0.0,
                                           'current_string24': 0.0,
                                           'current_string25': 0.0,
                                           'current_string26': 0.0,
                                           'current_string27': 0.0,
                                           'current_string28': 0.0,
                                           'current_string29': 0.0,
                                           'current_string3': 0.0,
                                           'current_string30': 0.0,
                                           'current_string31': 0.0,
                                           'current_string32': 0.0,
                                           'current_string4': 0.0,
                                           'current_string5': 0.0,
                                           'current_string6': 0.0,
                                           'current_string7': 0.0,
                                           'current_string8': 0.0,
                                           'current_string9': 0.0,
                                           'datalogger_sn': 'BLE4BL40GS',
                                           'day': None,
                                           'debug1': '0，0，0，30200，7，55，0，8200',
                                           'debug2': '0，24，3，20，24，4，26，0',
                                           'debug3': '0，0，0，0，0，0，0，0',
                                           'derating_mode': 7,
                                           'device_sn': 'QXHLD7F0C9',
                                           'dw_string_warning_value1': 0,
                                           'e_rac_today': 0.0,
                                           'e_rac_total': 0.0,
                                           'eac_today': 0.0,
                                           'eac_total': 225.9,
                                           'epv10_today': 0.0,
                                           'epv10_total': 0.0,
                                           'epv11_today': 0.0,
                                           'epv11_total': 0.0,
                                           'epv12_today': 0.0,
                                           'epv12_total': 0.0,
                                           'epv13_today': 0.0,
                                           'epv13_total': 0.0,
                                           'epv14_today': 0.0,
                                           'epv14_total': 0.0,
                                           'epv15_today': 0.0,
                                           'epv15_total': 0.0,
                                           'epv16_today': 0.0,
                                           'epv16_total': 0.0,
                                           'epv1_today': 0.0,
                                           'epv1_total': 140.3,
                                           'epv2_today': 0.0,
                                           'epv2_total': 83.6,
                                           'epv3_today': 0.0,
                                           'epv3_total': 0.0,
                                           'epv4_today': 0.0,
                                           'epv4_total': 0.0,
                                           'epv5_today': 0.0,
                                           'epv5_total': 0.0,
                                           'epv6_today': 0.0,
                                           'epv6_total': 0.0,
                                           'epv7_today': 0.0,
                                           'epv7_total': 0.0,
                                           'epv8_today': 0.0,
                                           'epv8_total': 0.0,
                                           'epv9_today': 0.0,
                                           'epv9_total': 0.0,
                                           'epv_total': 223.9,
                                           'fac': 46.0,
                                           'fault_code1': 0,
                                           'fault_code2': 0,
                                           'fault_type': 302,
                                           'fault_value': 0,
                                           'gfci': 2.0,
                                           'i_pid_pvape': 0.0,
                                           'i_pid_pvbpe': 0.0,
                                           'i_pid_pvcpe': 0.0,
                                           'i_pid_pvdpe': 0.0,
                                           'i_pid_pvepe': 0.0,
                                           'i_pid_pvfpe': 0.0,
                                           'i_pid_pvgpe': 0.0,
                                           'i_pid_pvhpe': 0.0,
                                           'i_pid_pvpe10': 0.0,
                                           'i_pid_pvpe11': 0.0,
                                           'i_pid_pvpe12': 0.0,
                                           'i_pid_pvpe13': 0.0,
                                           'i_pid_pvpe14': 0.0,
                                           'i_pid_pvpe15': 0.0,
                                           'i_pid_pvpe16': 0.0,
                                           'i_pid_pvpe9': 0.0,
                                           'iacr': 0.0,
                                           'iacs': 0.0,
                                           'iact': 0.0,
                                           'id': 0,
                                           'ipm_temperature': 0.0,
                                           'ipv1': 0.0,
                                           'ipv10': 0.0,
                                           'ipv11': 0.0,
                                           'ipv12': 0.0,
                                           'ipv13': 0.0,
                                           'ipv14': 0.0,
                                           'ipv15': 0.0,
                                           'ipv16': 0.0,
                                           'ipv2': 0.0,
                                           'ipv3': 0.0,
                                           'ipv4': 0.0,
                                           'ipv5': 0.0,
                                           'ipv6': 0.0,
                                           'ipv7': 0.0,
                                           'ipv8': 0.0,
                                           'ipv9': 0.0,
                                           'lost': True,
                                           'max_bean': None,
                                           'n_bus_voltage': 292.9,
                                           'op_fullwatt': 555.5,
                                           'p_bus_voltage': 300.4,
                                           'pac': 0.0,
                                           'pacr': 0.0,
                                           'pacs': 0.0,
                                           'pact': 0.0,
                                           'pf': 1.0,
                                           'pid_bus': 0.0,
                                           'pid_fault_code': 0,
                                           'pid_status': 0,
                                           'pid_status_text': 'Lost',
                                           'power_today': 0.0,
                                           'power_total': 0.0,
                                           'ppv': 0.0,
                                           'ppv1': 0.0,
                                           'ppv10': 0.0,
                                           'ppv11': 0.0,
                                           'ppv12': 0.0,
                                           'ppv13': 0.0,
                                           'ppv14': 0.0,
                                           'ppv15': 0.0,
                                           'ppv16': 0.0,
                                           'ppv2': 0.0,
                                           'ppv3': 0.0,
                                           'ppv4': 0.0,
                                           'ppv5': 0.0,
                                           'ppv6': 0.0,
                                           'ppv7': 0.0,
                                           'ppv8': 0.0,
                                           'ppv9': 0.0,
                                           'pv_iso': 0.0,
                                           'r_dci': 0.0,
                                           'rac': 0.0,
                                           'react_power': 0.0,
                                           'react_power_max': 0.0,
                                           'react_power_total': 0.0,
                                           'real_op_percent': 0.0,
                                           's_dci': 0.0,
                                           'status': 3,
                                           'status_text': 'Fault',
                                           'str_break': 0,
                                           'str_fault': 0,
                                           'str_unbalance': 0,
                                           'str_unmatch': 0,
                                           't_dci': 0.0,
                                           'temperature': 55.100002,
                                           'temperature2': 25.7,
                                           'temperature3': 25.7,
                                           'temperature4': 0.0,
                                           'temperature5': 0.0,
                                           'time': datetime.datetime(2024, 4, 26, 14, 44, 45),
                                           'time_calendar': 1714113885020,
                                           'time_total': 808233.0,
                                           'v_pid_pvape': 0.0,
                                           'v_pid_pvbpe': 0.0,
                                           'v_pid_pvcpe': 0.0,
                                           'v_pid_pvdpe': 0.0,
                                           'v_pid_pvepe': 0.0,
                                           'v_pid_pvfpe': 0.0,
                                           'v_pid_pvgpe': 0.0,
                                           'v_pid_pvhpe': 0.0,
                                           'v_pid_pvpe10': 0.0,
                                           'v_pid_pvpe11': 0.0,
                                           'v_pid_pvpe12': 0.0,
                                           'v_pid_pvpe13': 0.0,
                                           'v_pid_pvpe14': 0.0,
                                           'v_pid_pvpe15': 0.0,
                                           'v_pid_pvpe16': 0.0,
                                           'v_pid_pvpe9': 0.0,
                                           'v_string1': 0.0,
                                           'v_string10': 0.0,
                                           'v_string11': 0.0,
                                           'v_string12': 0.0,
                                           'v_string13': 0.0,
                                           'v_string14': 0.0,
                                           'v_string15': 0.0,
                                           'v_string16': 0.0,
                                           'v_string17': 0.0,
                                           'v_string18': 0.0,
                                           'v_string19': 0.0,
                                           'v_string2': 0.0,
                                           'v_string20': 0.0,
                                           'v_string21': 0.0,
                                           'v_string22': 0.0,
                                           'v_string23': 0.0,
                                           'v_string24': 0.0,
                                           'v_string25': 0.0,
                                           'v_string26': 0.0,
                                           'v_string27': 0.0,
                                           'v_string28': 0.0,
                                           'v_string29': 0.0,
                                           'v_string3': 0.0,
                                           'v_string30': 0.0,
                                           'v_string31': 0.0,
                                           'v_string32': 0.0,
                                           'v_string4': 0.0,
                                           'v_string5': 0.0,
                                           'v_string6': 0.0,
                                           'v_string7': 0.0,
                                           'v_string8': 0.0,
                                           'v_string9': 0.0,
                                           'vac_rs': 0.3,
                                           'vac_st': 2.5,
                                           'vac_tr': 2.3,
                                           'vacr': 0.7,
                                           'vacs': 0.90000004,
                                           'vact': 1.6,
                                           'vpv1': 599.8,
                                           'vpv10': 0.0,
                                           'vpv11': 0.0,
                                           'vpv12': 0.0,
                                           'vpv13': 0.0,
                                           'vpv14': 0.0,
                                           'vpv15': 0.0,
                                           'vpv16': 0.0,
                                           'vpv2': 292.7,
                                           'vpv3': 0.0,
                                           'vpv4': 0.0,
                                           'vpv5': 0.0,
                                           'vpv6': 0.0,
                                           'vpv7': 0.0,
                                           'vpv8': 0.0,
                                           'vpv9': 0.0,
                                           'w_pid_fault_value': 0,
                                           'w_string_status_value': 0,
                                           'warn_bit': 0,
                                           'warn_code': 0,
                                           'warning_value1': 0,
                                           'warning_value2': 0,
                                           'warning_value3': 0,
                                           'with_time': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy(device_sn=self._device_sn(device_sn), device_type=DeviceType.MAX)

    def energy_multiple(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        page: Optional[int] = None,
    ) -> MaxEnergyOverviewMultiple:
        """
        Get the latest real-time data of max in batches
        Interface to obtain the latest real-time data of inverters in batches
        https://www.showdoc.com.cn/262556420217021/6127606661600864

        Note:
            Only applicable to devices with device type 4 (max) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10004: date interval exceeds seven days
        * 10005: Max does not exist

        Args:
            device_sn (Union[str, List[str]]): MAX serial number or list of (multiple) MAX serial numbers (max 100)
            page (Optional[int]): page number, default 1, max 2

        Returns:
            MaxEnergyOverviewMultiple
            {   'data': [   {   'data': {   'address': None,
                                            'again': False,
                                            'alias': None,
                                            'apf_status': None,
                                            'apf_status_text': None,
                                            'calendar': {   'first_day_of_week': 1,
                                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                            'lenient': True,
                                                            'minimal_days_in_first_week': 1,
                                                            'time': {'date': 8, 'day': 5, 'hours': 9, 'minutes': 4, 'month': 0, 'seconds': 59, 'time': 1610067899000, 'timezone_offset': -480, 'year': 121},
                                                            'time_in_millis': 1610067899000,
                                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                            'week_date_supported': True,
                                                            'week_year': 2021,
                                                            'weeks_in_week_year': 52},
                                            'comp_har_ir': 0,
                                            'comp_har_is': 0,
                                            'comp_har_it': 0,
                                            'comp_qr': 0,
                                            'comp_qs': 0,
                                            'comp_qt': 0,
                                            'ct_har_ir': 0,
                                            'ct_har_is': 0,
                                            'ct_har_it': 0,
                                            'ct_ir': 0,
                                            'ct_is': 0,
                                            'ct_it': 0,
                                            'ct_qr': 0,
                                            'ct_qs': 0,
                                            'ct_qt': 0,
                                            'current_string1': 0.0,
                                            'current_string10': 0.20000000298023224,
                                            'current_string11': 0.0,
                                            'current_string12': 0.20000000298023224,
                                            'current_string13': 0.0,
                                            'current_string14': 0.20000000298023224,
                                            'current_string15': 0.0,
                                            'current_string16': 0.0,
                                            'current_string2': 0.30000001192092896,
                                            'current_string3': 0.0,
                                            'current_string4': 0.20000000298023224,
                                            'current_string5': 0.0,
                                            'current_string6': 0.10000000149011612,
                                            'current_string7': 0.0,
                                            'current_string8': 0.20000000298023224,
                                            'current_string9': 0.0,
                                            'datalogger_sn': None,
                                            'day': None,
                                            'debug1': '0, 0, 0, 250, 32998, 0, 5650, 6799',
                                            'debug2': '0, 0, 0, 0, 0, 8000, 18870, 8439',
                                            'derating_mode': None,
                                            'dw_string_warning_value1': 0,
                                            'e_rac_today': 0.0,
                                            'e_rac_total': 0.0,
                                            'eac_today': 0.1,
                                            'eac_total': 43617.8,
                                            'epv1_today': 0.0,
                                            'epv1_total': 12129.7,
                                            'epv2_today': 0.0,
                                            'epv2_total': 12277.9,
                                            'epv3_today': 0.0,
                                            'epv3_total': None,
                                            'epv4_today': None,
                                            'epv4_total': 12116.8,
                                            'epv5_today': 0.0,
                                            'epv5_total': 12287.5,
                                            'epv6_today': 0.0,
                                            'epv6_total': 12320.6,
                                            'epv7_today': 0.0,
                                            'epv7_total': 12678.7,
                                            'epv8_today': None,
                                            'epv8_total': 0.0,
                                            'epv_total': 86631.8,
                                            'fac': 49.97999954223633,
                                            'fault_code1': 0,
                                            'fault_code2': 0,
                                            'fault_type': 0,
                                            'fault_value': 0,
                                            'gfci': None,
                                            'i_pid_pvape': 0.0,
                                            'i_pid_pvbpe': 0.0,
                                            'i_pid_pvcpe': 0.0,
                                            'i_pid_pvdpe': 0.0,
                                            'i_pid_pvepe': 0.0,
                                            'i_pid_pvfpe': 0.0,
                                            'i_pid_pvgpe': 0.0,
                                            'i_pid_pvhpe': 0.0,
                                            'iacr': None,
                                            'iacs': None,
                                            'iact': None,
                                            'id': None,
                                            'ipm_temperature': 0.0,
                                            'ipv1': 0.20000000298023224,
                                            'ipv2': 0.20000000298023224,
                                            'ipv3': 0.10000000149011612,
                                            'ipv4': 0.10000000149011612,
                                            'ipv5': 0.10000000149011612,
                                            'ipv6': 0.10000000149011612,
                                            'ipv7': 0.20000000298023224,
                                            'ipv8': 0.0,
                                            'lost': None,
                                            'max_bean': None,
                                            'n_bus_voltage': 339.5,
                                            'op_fullwatt': None,
                                            'p_bus_voltage': None,
                                            'pac': 755.3,
                                            'pacr': None,
                                            'pacs': None,
                                            'pact': None,
                                            'pf': 1.0,
                                            'pid_bus': 0,
                                            'pid_fault_code': 0,
                                            'pid_status': None,
                                            'pid_status_text': 'Lost',
                                            'power_today': 0.0,
                                            'power_total': 0.0,
                                            'ppv': 601.7,
                                            'ppv1': None,
                                            'ppv2': None,
                                            'ppv3': None,
                                            'ppv4': None,
                                            'ppv5': None,
                                            'ppv6': 63.5,
                                            'ppv7': 115.5,
                                            'ppv8': 0.0,
                                            'pv_iso': 107.0,
                                            'r_dci': 47.70000076293945,
                                            'rac': 0.0,
                                            'real_op_percent': 0.0,
                                            's_dci': 60.29999923706055,
                                            'serial_num': 'GQF0A13002',
                                            'status': None,
                                            'status_text': None,
                                            'str_Break': 0,
                                            'str_Fault': None,
                                            'str_unbalance': None,
                                            'str_unmatch': 0,
                                            't_dci': 121.80000305175781,
                                            'temperature': 13.600000381469727,
                                            'temperature2': 14.100000381469727,
                                            'temperature3': 13.600000381469727,
                                            'temperature4': None,
                                            'temperature5': None,
                                            'time': datetime.datetime(2021, 1, 8, 9, 4, 59),
                                            'time_total': 1540931.6,
                                            'v_pid_pvape': 0.0,
                                            'v_pid_pvbpe': 0.0,
                                            'v_pid_pvcpe': 0.0,
                                            'v_pid_pvdpe': 0.0,
                                            'v_pid_pvepe': 0.0,
                                            'v_pid_pvfpe': 0.0,
                                            'v_pid_pvgpe': 0.0,
                                            'v_pid_pvhpe': 0.0,
                                            'v_string1': None,
                                            'v_string10': 639.2999877929688,
                                            'v_string11': 637.4000244140625,
                                            'v_string12': 637.4000244140625,
                                            'v_string13': 581.5,
                                            'v_string14': 581.5,
                                            'v_string15': 0.0,
                                            'v_string16': 0.0,
                                            'v_string2': None,
                                            'v_string3': None,
                                            'v_string4': None,
                                            'v_string5': None,
                                            'v_string6': None,
                                            'v_string7': None,
                                            'v_string8': None,
                                            'v_string9': None,
                                            'vac_rs': None,
                                            'vac_st': 404.1000061035156,
                                            'vac_tr': 405.70001220703125,
                                            'vacr': 233.60000610351562,
                                            'vacs': 232.8000030517578,
                                            'vact': 233.89999389648438,
                                            'vpv1': 574.0,
                                            'vpv2': 580.0999755859375,
                                            'vpv3': 628.9000244140625,
                                            'vpv4': 647.0999755859375,
                                            'vpv5': 644.0999755859375,
                                            'vpv6': 635.7999877929688,
                                            'vpv7': 577.5999755859375,
                                            'vpv8': 0.0,
                                            'w_pid_fault_value': 0,
                                            'w_string_status_value': 0,
                                            'warn_bit': 0,
                                            'warn_code': 0,
                                            'warning_value1': 0,
                                            'warning_value2': 0,
                                            'warning_value3': 0,
                                            'with_time': False},
                                'datalogger_sn': 'AKE092600C',
                                'device_sn': 'GQF0A13002'},
                            {'data': None, 'datalogger_sn': None, 'device_sn': 'GQF0A1300C'}],
                'error_code': 0,
                'error_msg': None,
                'page_num': 1}
        """

        device_sn = self._device_sn(device_sn)
        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/max/maxs_data",
            data={
                "maxs": device_sn,
                "pageNum": page or 1,
            },
        )

        # Unfortunately, the original response cannot be parsed by pydantic as the inverter_sn is used as key
        # To fix this, resulting data is restructured
        devices = [
            MaxEnergyOverviewMultipleItem(
                device_sn=inverter_sn,
                datalogger_sn=response.get("data", {}).get(inverter_sn, {}).get("dataloggerSn", None),
                data=response.get("data", {}).get(inverter_sn, {}).get(inverter_sn, None),
            )
            for inverter_sn in response.get("maxs", [])
        ]
        response.pop("maxs", None)
        response["data"] = devices

        return MaxEnergyOverviewMultiple.model_validate(response)

    def energy_history(
        self,
        device_sn: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> MaxEnergyHistory:
        """
        Get historical data of a Max
        Interface to get historical data of a certain Max
        https://www.showdoc.com.cn/262556420217021/6127583793839931

        Note:
            Only applicable to devices with device type 4 (max) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10004: date interval exceeds seven days
        * 10005: Max does not exist

        Args:
            device_sn (str): Inverter serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            MaxEnergyHistory
            e.g.
            {   'data': {   'count': 29,
                            'datalogger_sn': 'SATA818009',
                            'datas': [   {   'address': 0,
                                             'again': False,
                                             'alias': '',
                                             'apfStatus': 0,
                                             'apfStatusText': 'None',
                                             'calendar': {   'firstDayOfWeek': 1,
                                                             'gregorianChange': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezoneOffset': -480, 'year': -318},
                                                             'lenient': True,
                                                             'minimalDaysInFirstWeek': 1,
                                                             'time': {'date': 11, 'day': 5, 'hours': 10, 'minutes': 49, 'month': 0, 'seconds': 36, 'time': 1547174976000, 'timezoneOffset': -480, 'year': 119},
                                                             'timeInMillis': 1547174976000,
                                                             'timeZone': {'DSTSavings': 0, 'ID': 'Asia/Shanghai', 'dirty': False, 'displayName': 'China Standard Time', 'lastRuleInstance': None, 'rawOffset': 28800000},
                                                             'weekDateSupported': True,
                                                             'weekYear': 2019,
                                                             'weeksInWeekYear': 52},
                                             'compharir': 0,
                                             'compharis': 0,
                                             'compharit': 0,
                                             'compqr': 0,
                                             'compqs': 0,
                                             'compqt': 0,
                                             'ctharir': 0,
                                             'ctharis': 0,
                                             'ctharit': 0,
                                             'ctir': 0,
                                             'ctis': 0,
                                             'ctit': 0,
                                             'ctqr': 0,
                                             'ctqs': 0,
                                             'ctqt': 0,
                                             'currentString1': 0,
                                             'currentString10': 0,
                                             'currentString11': 0,
                                             'currentString12': 0,
                                             'currentString13': 0,
                                             'currentString14': 0,
                                             'currentString15': 0,
                                             'currentString16': 0,
                                             'currentString2': 0,
                                             'currentString3': 0,
                                             'currentString4': 0,
                                             'currentString5': 0,
                                             'currentString6': 0,
                                             'currentString7': 0,
                                             'currentString8': 0,
                                             'currentString9': 0,
                                             'dataLogSn': '',
                                             'day': '',
                                             'debug1': '0, 0, 0, 0, 0, 0, 0, 0',
                                             'debug2': '0, 0, 0, 0, 0, 0, 0, 0',
                                             'deratingMode': 0,
                                             'dwStringWarningValue1': 0,
                                             'eRacToday': 0,
                                             'eRacTotal': 0,
                                             'eacToday': 0,
                                             'eacTotal': 0,
                                             'epv1Today': 0,
                                             'epv1Total': 0,
                                             'epv2Today': 0,
                                             'epv2Total': 0,
                                             'epv3Today': 0,
                                             'epv3Total': 0,
                                             'epv4Today': 0,
                                             'epv4Total': 0,
                                             'epv5Today': 0,
                                             'epv5Total': 0,
                                             'epv6Today': 0,
                                             'epv6Total': 0,
                                             'epv7Today': 0,
                                             'epv7Total': 0,
                                             'epv8Today': 0,
                                             'epv8Total': 0,
                                             'epvTotal': 0,
                                             'fac': 0,
                                             'faultCode1': 2,
                                             'faultCode2': 0,
                                             'faultType': 2,
                                             'faultValue': 3,
                                             'gfci': 0,
                                             'iPidPvape': 0,
                                             'iPidPvbpe': 0,
                                             'iPidPvcpe': 0,
                                             'iPidPvdpe': 0,
                                             'iPidPvepe': 0,
                                             'iPidPvfpe': 0,
                                             'iPidPvgpe': 0,
                                             'iPidPvhpe': 0,
                                             'iacr': 0,
                                             'iacs': 0,
                                             'iact': 0,
                                             'id': 0,
                                             'ipmTemperature': 0,
                                             'ipv1': 0,
                                             'ipv2': 0,
                                             'ipv3': 0,
                                             'ipv4': 0,
                                             'ipv5': 0,
                                             'ipv6': 0,
                                             'ipv7': 0,
                                             'ipv8': 0,
                                             'lost': True,
                                             'maxBean': None,
                                             'nBusVoltage': 0,
                                             'opFullwatt': 0,
                                             'pBusVoltage': 0,
                                             'pac': 0,
                                             'pacr': 0,
                                             'pacs': 0,
                                             'pact': 0,
                                             'pf': -1,
                                             'pidBus': 0,
                                             'pidFaultCode': 0,
                                             'pidStatus': 0,
                                             'pidStatusText': 'Lost',
                                             'powerToday': 0,
                                             'powerTotal': 0,
                                             'ppv': 0,
                                             'ppv1': 0,
                                             'ppv2': 0,
                                             'ppv3': 0,
                                             'ppv4': 0,
                                             'ppv5': 0,
                                             'ppv6': 0,
                                             'ppv7': 0,
                                             'ppv8': 0,
                                             'pvIso': 0,
                                             'rDci': 0,
                                             'rac': 0,
                                             'realOPPercent': 0,
                                             'sDci': 0,
                                             'serialNum': 'TLMAX00B01',
                                             'status': 3,
                                             'statusText': 'Fault',
                                             'strBreak': 0,
                                             'strFault': 0,
                                             'strUnblance': 0,
                                             'strUnmatch': 0,
                                             'tDci': 0,
                                             'temperature': 0,
                                             'temperature2': 0,
                                             'temperature3': 0,
                                             'temperature4': 0,
                                             'temperature5': 25.899999618530273,
                                             'time': '2019-01-11 10:49:36',
                                             'timeTotal': 0,
                                             'vPidPvape': 0,
                                             'vPidPvbpe': 0,
                                             'vPidPvcpe': 0,
                                             'vPidPvdpe': 0,
                                             'vPidPvepe': 0,
                                             'vPidPvfpe': 0,
                                             'vPidPvgpe': 0,
                                             'vPidPvhpe': 0,
                                             'vString1': 0,
                                             'vString10': 0,
                                             'vString11': 0,
                                             'vString12': 0,
                                             'vString13': 0,
                                             'vString14': 0,
                                             'vString15': 0,
                                             'vString16': 0,
                                             'vString2': 0,
                                             'vString3': 0,
                                             'vString4': 0,
                                             'vString5': 0,
                                             'vString6': 0,
                                             'vString7': 0,
                                             'vString8': 0,
                                             'vString9': 0,
                                             'vacRs': 0,
                                             'vacSt': 0,
                                             'vacTr': 0,
                                             'vacr': 0,
                                             'vacs': 0,
                                             'vact': 0,
                                             'vpv1': 0,
                                             'vpv2': 0,
                                             'vpv3': 0,
                                             'vpv4': 0,
                                             'vpv5': 0,
                                             'vpv6': 0,
                                             'vpv7': 0,
                                             'vpv8': 0,
                                             'wPIDFaultValue': 0,
                                             'wStringStatusValue': 0,
                                             'warnBit': 0,
                                             'warnCode': 0,
                                             'warningValue1': 0,
                                             'warningValue2': 0,
                                             'warningValue3': 0,
                                             'withTime': False}],
                            'max_sn': 'TLMAX00B01',
                            'next_page_start_id': 21},
                'error_code': 0,
                'error_msg': ''}
        """

        if start_date is None and end_date is None:
            start_date = date.today()
            end_date = date.today()
        elif start_date is None:
            start_date = end_date
        elif end_date is None:
            end_date = start_date

        # check interval validity
        if end_date - start_date >= timedelta(days=7):
            raise ValueError("date interval must not exceed 7 days")

        response = self.session.post(
            endpoint="device/max/max_data",
            data={
                "max_sn": self._device_sn(device_sn),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return MaxEnergyHistory.model_validate(response)

    def energy_history_v4(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
    ) -> MaxEnergyHistoryV4:
        """
        One day data using "new-api" endpoint
        Retrieves all detailed data for a specific device on a particular day based on the device SN, device type, and date.
        https://www.showdoc.com.cn/2540838290984246/11292916022305414

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (str): Device unique serial number (SN)
            date_ (Optional[date]): Start Date - defaults to today

        Returns:
            MaxEnergyHistoryV4
            e.g.
            {   'data': {   'datas': [   {
                                             <see energy_v4() for attributes>
                                         }],
                            'have_next': False,
                            'start': 0},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy_history(
            device_sn=self._device_sn(device_sn), device_type=DeviceType.MAX, date_=date_
        )

    def energy_history_multiple_v4(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        date_: Optional[date] = None,
    ) -> MaxEnergyHistoryMultipleV4:
        """
        One day data using "new-api" endpoint
        Retrieves all detailed data for a specific device on a particular day based on the device SN, device type, and date.
        https://www.showdoc.com.cn/2540838290984246/11292916022305414

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)
            date_ (Optional[date]): Start Date - defaults to today

        Returns:
            MaxEnergyHistoryMultipleV4
            e.g.
            {   'data': {   'NHB691514F': [   {
                                                  <see energy_v4() for attributes>
                                              }]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

        """

        return self._api_v4.energy_history_multiple(
            device_sn=self._device_sn(device_sn), device_type=DeviceType.MAX, date_=date_
        )

    def alarms(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> MaxAlarms:
        """
        Get the alarm data of a Max
        Interface to get alarm data of a certain Max
        https://www.showdoc.com.cn/262556420217021/6127591022121148

        Note:
            Only applicable to devices with device type 4 (max) returned by plant.list_devices()

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10005: Max does not exist

        Args:
            device_sn (str): Max device serial number
            date_ (Optional[date]): Date - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            MaxAlarms
            e.g.
            {
                'data': {
                    'alarms': [
                        {
                            'alarm_code': 2,
                            'alarm_message': 'undown error',
                            'end_time': datetime.datetime(2018, 12, 17, 14, 5, 54),
                            'start_time': datetime.datetime(2018, 12, 17, 14, 5, 54),
                            'status': 1
                        }
                    ],
                    'count': 1,
                    'device_sn': 'TLMAX00B01'
                },
                'error_code': 0,
                'error_msg': None
            }
        """

        if date_ is None:
            date_ = date.today()

        response = self.session.post(
            endpoint="device/max/alarm_data",
            data={
                "max_sn": self._device_sn(device_sn),
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return MaxAlarms.model_validate(response)
