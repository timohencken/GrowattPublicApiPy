from datetime import date, timedelta
from typing import Optional, Union, List

import truststore

from pydantic_models.max import (
    MaxSettingRead,
    MaxSettingWrite,
    MaxDetails,
    MaxEnergyOverview,
    MaxEnergyHistory,
    MaxAlarms,
    MaxEnergyOverviewMultiple,
    MaxEnergyOverviewMultipleItem,
)

truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


class Max:
    """
    endpoints for MAX inverters
    https://www.showdoc.com.cn/262556420217021/6120369315865619
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def setting_read(
        self,
        device_sn: str,
        parameter_id: Optional[str] = None,
        start_address: Optional[int] = None,
        end_address: Optional[int] = None,
    ) -> MaxSettingRead:
        """
        Read Max setting parameter interface
        https://www.showdoc.com.cn/262556420217021/6127601154776404

        Note:
            Only applicable to devices with device type 4 (max) returned by device.list()

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
            raise ValueError(
                "specify either parameter_id or start_address/end_address - not both."
            )
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
                "device_sn": device_sn,
                "paramId": parameter_id,
                "startAddr": start_address,
                "endAddr": end_address,
            },
        )

        return MaxSettingRead.model_validate(response)

    # noinspection PyUnusedLocal
    def setting_write(
        self,
        device_sn: str,
        parameter_id: str,
        parameter_value_1: str,
        parameter_value_2: Optional[str] = None,
        parameter_value_3: Optional[str] = None,
        parameter_value_4: Optional[str] = None,
        parameter_value_5: Optional[str] = None,
        parameter_value_6: Optional[str] = None,
        parameter_value_7: Optional[str] = None,
        parameter_value_8: Optional[str] = None,
        parameter_value_9: Optional[str] = None,
        parameter_value_10: Optional[str] = None,
        parameter_value_11: Optional[str] = None,
        parameter_value_12: Optional[str] = None,
        parameter_value_13: Optional[str] = None,
        parameter_value_14: Optional[str] = None,
        parameter_value_15: Optional[str] = None,
        parameter_value_16: Optional[str] = None,
        parameter_value_17: Optional[str] = None,
        parameter_value_18: Optional[str] = None,
        parameter_value_19: Optional[str] = None,
    ) -> MaxSettingWrite:
        """
        Max parameter setting interface
        Max parameter setting interface interface
        https://www.showdoc.com.cn/262556420217021/6127597452472600

        Note:
            Only applicable to devices with device type 4 (max) returned by device.list()

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
            parameter_value_1 (str): parameter value 1
            parameter_value_2 (Optional[str]): parameter value 2
            parameter_value_3 (Optional[str]): parameter value 3
            parameter_value_4 (Optional[str]): parameter value 4
            parameter_value_5 (Optional[str]): parameter value 5
            parameter_value_6 (Optional[str]): parameter value 6
            parameter_value_7 (Optional[str]): parameter value 7
            parameter_value_8 (Optional[str]): parameter value 8
            parameter_value_9 (Optional[str]): parameter value 9
            parameter_value_10 (Optional[str]): parameter value 10
            parameter_value_11 (Optional[str]): parameter value 11
            parameter_value_12 (Optional[str]): parameter value 12
            parameter_value_13 (Optional[str]): parameter value 13
            parameter_value_14 (Optional[str]): parameter value 14
            parameter_value_15 (Optional[str]): parameter value 15
            parameter_value_16 (Optional[str]): parameter value 16
            parameter_value_17 (Optional[str]): parameter value 17
            parameter_value_18 (Optional[str]): parameter value 18
            parameter_value_19 (Optional[str]): parameter value 19

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
                assert (
                    parameters[i] is None
                ), f"parameter {i} must not be used for set_any_reg"
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
            endpoint="tlxSet",
            data={
                "tlx_sn": device_sn,
                "type": parameter_id,
                **{f"param{i}": parameters[i] for i in range(1, 20)},
            },
        )

        return MaxSettingWrite.model_validate(response)

    def details(
        self,
        device_sn: str,
    ) -> MaxDetails:
        """
        Get basic Max information
        Interface to get basic information of Max
        https://www.showdoc.com.cn/262556420217021/6120369315865619

        Note:
            Only applicable to devices with device type 4 (max) returned by device.list()

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
                "device_sn": device_sn,
            },
        )

        return MaxDetails.model_validate(response)

    def energy(
        self,
        device_sn: str,
    ) -> MaxEnergyOverview:
        """
        Get the latest real-time data from Max
        Interface to get the latest real-time data of Max
        https://www.showdoc.com.cn/262556420217021/6127572916461964

        Note:
            Only applicable to devices with device type 4 (max) returned by device.list()

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
                "max_sn": device_sn,
            },
        )

        return MaxEnergyOverview.model_validate(response)

    def energy_multiple(
        self,
        device_sn: Union[str, List[str]],
        page: Optional[int] = None,
    ) -> MaxEnergyOverviewMultiple:
        """
        Get the latest real-time data of max in batches
        Interface to obtain the latest real-time data of inverters in batches
        https://www.showdoc.com.cn/262556420217021/6127606661600864

        Note:
            Only applicable to devices with device type 4 (max) returned by device.list()

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
                datalogger_sn=response.get("data", {})
                .get(inverter_sn, {})
                .get("dataloggerSn", None),
                data=response.get("data", {})
                .get(inverter_sn, {})
                .get(inverter_sn, None),
            )
            for inverter_sn in response.get("maxs", [])
        ]
        response.pop("maxs", None)
        response["data"] = devices

        return MaxEnergyOverviewMultiple.model_validate(response)

    def energy_history(
        self,
        device_sn: str,
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
            Only applicable to devices with device type 4 (max) returned by device.list()

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
        if end_date - start_date > timedelta(days=7):
            raise ValueError("date interval must not exceed 7 days")

        response = self.session.post(
            endpoint="device/max/max_data",
            data={
                "max_sn": device_sn,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return MaxEnergyHistory.model_validate(response)

    def alarms(
        self,
        device_sn: str,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> MaxAlarms:
        """
        Get the alarm data of a Max
        Interface to get alarm data of a certain Max
        https://www.showdoc.com.cn/262556420217021/6127591022121148

        Note:
            Only applicable to devices with device type 4 (max) returned by device.list()

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
                "max_sn": device_sn,
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return MaxAlarms.model_validate(response)
