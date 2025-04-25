from datetime import date, timedelta
from typing import Optional, Union, List

import truststore

from pydantic_models.inverter import (
    InverterSettingWrite,
    InverterDetails,
    InverterEnergyOverview,
    InverterEnergyHistory,
    InverterAlarms,
    InverterEnergyOverviewMultiple,
    InverterSettingRead,
    InverterEnergyOverviewMultipleItem,
)

truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


class Inverter:
    """
    https://www.showdoc.com.cn/262556420217021/6118532122241417
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
    ) -> InverterSettingRead:
        """
        Inverter parameter setting
        Interface for inverter parameter setting
        https://www.showdoc.com.cn/262556420217021/6118532122241417

        Note:
            Only applicable to devices with device type 1 (inverter) returned by device.list()

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
            device_sn (str): Inverter serial number
            parameter_id (Optional[str]): parameter ID - specify either parameter_id ort start/end_address
            start_address (Optional[int]): register address to start reading from - specify either parameter_id ort start/end_address
            end_address (Optional[int]): register address to stop reading at

        Returns:
            InverterSettingRead
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
            endpoint="readInverterParam",
            data={
                "device_sn": device_sn,
                "paramId": parameter_id,
                "startAddr": start_address,
                "endAddr": end_address,
            },
        )

        inv_setting_response = InverterSettingRead.model_validate(response)
        if inv_setting_response.error_code == 10002:
            inv_setting_response.error_msg += " (or type != 1 - check with device.list())"

        return inv_setting_response

    def setting_write(
        self,
        device_sn: str,
        parameter_id: str,
        parameter_value_1: Union[str, int],
        parameter_value_2: Optional[Union[str, int]] = None,
    ) -> InverterSettingWrite:
        """
        Inverter parameter setting
        Interface for inverter parameter setting
        https://www.showdoc.com.cn/262556420217021/6118532122241417

        Note:
            Only applicable to devices with device type 1 (inverter) returned by device.list()

        This method allows to set
        * predefined settings (see table below)
        * any register value (see table below for most relevant settings, google for "Growatt Inverter Modbus RTU Protocol V1.20" for more)

        Predefined settings
        ========================+===========================+=======================+===================+====================================================================
        description             | parameter_id              | parameter_value_1     | parameter_value_2 | comment
        ========================+===========================+=======================+===================+====================================================================
        Set the inverter on/off | pv_on_off                 |    "0000"             |                   | 0 = Turn off and not automatically connect to the grid next time
                                |                           | or "0001"             |                   | 1 = Turn on and automatically connect to the grid next time
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Set whether to          | pv_pf_cmd_memory_state    |    "0"                |                   | 0 = off
          store PF commands     |                           | or "1"                |                   | 1 = on
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Set active power        | pv_active_p_rate          | "0" ~ "100"           |                   | unit: %
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Set reactive power      | pv_reactive_p_rate        | "0" ~ "100"           |    "over"         | unit: %, "over" = capacitive
                                |                           |                       | or "under"        |         "under" = inductive
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Set PF value            | pv_power_factor           |    "-0.8" ~ "-1"      |                   |
                                |                           | or  "0.8" ~  "1"      |                   |
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Set the inverter time   | pf_sys_year               | YYYY-MM-DD hh:mm:ss   |                   |
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Set the upper limit     | pv_grid_voltage_high      | e.g. "240.7"          |                   | float, at most one decimal digit
         of mains voltage       |                           |                       |                   |
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------

        Register settings
        ========================+===========================+=======================+===================+====================================================================
        description             | parameter_id              | parameter_value_1     | parameter_value_2 | comment
        ========================+===========================+=======================+===================+====================================================================
        Lower limit of          | set_any_reg               | "19"                  | "185" ~ "285"     | The register setting of engineering mode needs to
          mains voltage         |                           |                       |                   |  enter 10 times the value, such as 221.5V, enter 2215
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Upper limit of          | set_any_reg               | "20"                  | "185" ~ "285"     | The register setting of engineering mode needs to
          mains voltage         |                           |                       |                   |  enter 10 times the value, such as 221.5V, enter 2215
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Lower limit of          | set_any_reg               | "21"                  | "40" ~ "65"       | The register setting of engineering mode needs to
          mains frequency       |                           |                       |                   |  enter 10 times the value, such as 50.15Hz, enter 5015
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Upper limit of          | set_any_reg               | "22"                  | "40" ~ "65"       | The register setting of engineering mode needs to
          mains frequency       |                           |                       |                   |  enter 10 times the value, such as 50.15Hz, enter 5015
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Inverter                | set_any_reg               | "30"                  | "1" ~ "250"       |
          communication address |                           |                       |                   |
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Set the inverter on/off | set_any_reg               | "0"                   | "0" / "257"       | 0 = off, 257 = on
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        Set active power        | pv_active_p_rate          | "3"                   | "0" ~ "100"       | unit: %, Percentage of rated power
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------
        google for "Growatt Inverter Modbus RTU Protocol V1.20" for more
        ------------------------+---------------------------+-----------------------+-------------------+--------------------------------------------------------------------


        Specific error codes:
        * 10001: system error
        * 10002: inverter server error
        * 10003: inverter offline
        * 10004: collector serial number is empty
        * 10005: collector offline
        * 10006: set The parameter type does not exist
        * 10007: the parameter value is empty
        * 10008: the parameter value is not in the range
        * 10009: the date and time format is wrong
        * 10012: inverter unknown / not existing or device type != 1

        Args:
            device_sn (str): Inverter serial number
            parameter_id (str): parameter ID - pass "set_any_reg" to write register address
            parameter_value_1 (Union[str, int]): parameter value 1
            parameter_value_2 (Optional[Union[str, int]]): parameter value 2

        Returns:
            InverterSetting
            e.g. (success)
            {
                "data": "",
                "error_code": 0,
                "error_msg": ""
            }
        """
        if parameter_value_2 is None:
            parameter_value_2 = ""

        # parameter values must be string
        parameter_value_1 = str(parameter_value_1)
        parameter_value_2 = str(parameter_value_2)

        response = self.session.post(
            endpoint="inverterSet",
            data={
                "device_sn": device_sn,
                "paramId": parameter_id,
                "command_1": parameter_value_1,
                "command_2": parameter_value_2,
            },
        )

        inv_setting_response = InverterSettingWrite.model_validate(response)
        if inv_setting_response.error_code == 10012:
            inv_setting_response.error_msg += " (or type != 1 - check with device.list())"

        return inv_setting_response

    def details(
        self,
        device_sn: str,
    ) -> InverterDetails:
        """
        Get basic information about the inverter
        Interface to get basic information of inverter
        https://www.showdoc.com.cn/262556420217021/6118559963559236

        Note:
            Only applicable to devices with device type 1 (inverter) returned by device.list()

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Args:
            device_sn (str): Inverter serial number

        Returns:
            InverterDetails
            e.g.
            {'data': {'address': 1,
                      'alias': 'SASF819012',
                      'big_device': False,
                      'children': [],
                      'create_date': None,
                      'datalogger_sn': 'WLC082100F',
                      'e_today': 0.0,
                      'e_total': 0.0,
                      'energy_day': 0.0,
                      'energy_day_map': {},
                      'energy_month': 0.0,
                      'energy_month_text': '0',
                      'fw_version': 'TI1.0',
                      'group_id': 0,
                      'id': 1,
                      'img_path': './css/img/status_gray.gif',
                      'inner_version': 'TIAA10090402',
                      'inverter_info_status_css': 'vsts_table_ash',
                      'ipm_temperature': 0.0,
                      'last_update_time': {'date': 20,
                                           'day': 5,
                                           'hours': 10,
                                           'minutes': 29,
                                           'month': 11,
                                           'seconds': 22,
                                           'time': 1734661762000,
                                           'timezone_offset': -480,
                                           'year': 124},
                      'last_update_time_text': datetime.datetime(2024, 12, 20, 10, 29, 22),
                      'level': 4,
                      'load_text': '0%',
                      'location': None,
                      'lost': True,
                      'model': 0,
                      'model_text': 'A0B0D0T0P0U0M0S0',
                      'nominal_power': 80000,
                      'parent_id': 'LIST_WLC082100F_0',
                      'plant_id': 0,
                      'plant_name': None,
                      'power': 0.0,
                      'power_max': None,
                      'power_max_text': None,
                      'power_max_time': None,
                      'record': None,
                      'rf_stick': None,
                      'serial_num': 'SASF819012',
                      'status': -1,
                      'status_text': 'inverter.status.lost',
                      'tcp_server_ip': '47.107.154.111',
                      'temperature': 0.0,
                      'tree_id': 'SASF819012',
                      'tree_name': 'SASF819012',
                      'update_exist': False,
                      'updating': False,
                      'user_id': 0,
                      'user_name': None},
             'datalogger_sn': 'WLC082100F',
             'device_sn': 'SASF819012',
             'error_code': 0,
             'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/inverter/inv_data_info",
            params={
                "device_sn": device_sn,
            },
        )

        return InverterDetails.model_validate(response)

    def energy(
        self,
        device_sn: str,
    ) -> InverterEnergyOverview:
        """
        Get the latest real-time data of the inverter
        https://www.showdoc.com.cn/262556420217021/6118571427302257

        Note:
            Only applicable to devices with device type 1 (inverter) returned by device.list()

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Args:
            device_sn (str): Inverter serial number

        Returns:
            InverterEnergyOverview
            e.g.
            {'data': {'again': False,
                      'apf_status': 0,
                      'big_device': False,
                      'compharir': 0.0,
                      'compharis': 0.0,
                      'compharit': 0.0,
                      'compqr': 0.0,
                      'compqs': 0.0,
                      'compqt': 0.0,
                      'ctharir': 0.0,
                      'ctharis': 0.0,
                      'ctharit': 0.0,
                      'ctir': 0.0,
                      'ctis': 0.0,
                      'ctit': 0.0,
                      'ctqr': 0.0,
                      'ctqs': 0.0,
                      'ctqt': 0.0,
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
                      'debug1': '0，0，0，250，32806，0，2671，5400',
                      'debug2': '0，0，0，0，0，8000，0，0',
                      'derating_mode': 0,
                      'dw_string_warning_value1': 0,
                      'e_rac_today': 0.0,
                      'e_rac_total': 0.0,
                      'epv1_today': 0.0,
                      'epv1_total': 102709.5,
                      'epv2_today': 0.0,
                      'epv2_total': 108261.0,
                      'epv3_today': 0.0,
                      'epv3_total': 100415.0,
                      'epv4_today': 0.0,
                      'epv4_total': 97070.5,
                      'epv5_today': 0.0,
                      'epv5_total': 103908.1,
                      'epv6_today': 0.0,
                      'epv6_total': 102971.9,
                      'epv7_today': 0.0,
                      'epv7_total': 0.0,
                      'epv8_today': 0.0,
                      'epv8_total': 0.0,
                      'epv_total': 615336.0,
                      'fac': 50.02000045776367,
                      'fault_code1': 0,
                      'fault_code2': 0,
                      'fault_type': 0,
                      'fault_value': 0,
                      'gfci': 1,
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
                      'inverter_id': 'SASF819012',
                      'ipm_temperature': 0.0,
                      'ipv1': 0.0,
                      'ipv2': 0.0,
                      'ipv3': 0.0,
                      'ipv4': 0.0,
                      'ipv5': 0.0,
                      'ipv6': 0.0,
                      'ipv7': 0.0,
                      'ipv8': 0.0,
                      'n_bus_voltage': 143.10000610351562,
                      'op_fullwatt': 0.0,
                      'p_bus_voltage': 140.90000915527344,
                      'pac': 0.0,
                      'pacr': 0.0,
                      'pacs': 0.0,
                      'pact': 0.0,
                      'pf': 1.0,
                      'pid_bus': 0.0,
                      'pid_fault_code': 0,
                      'pid_status': 0,
                      'power_today': 0.0,
                      'power_total': 303642.5,
                      'ppv': 0.0,
                      'ppv1': 0.0,
                      'ppv2': 0.0,
                      'ppv3': 0.0,
                      'ppv4': 0.0,
                      'ppv5': 0.0,
                      'ppv6': 0.0,
                      'ppv7': 0.0,
                      'ppv8': 0.0,
                      'pv_iso': 242.0,
                      'r_dci': 0.0,
                      'rac': 0.0,
                      'real_op_percent': 0.0,
                      's_dci': 0.0,
                      'status': 0,
                      'status_text': 'Waiting',
                      'str_break': 0.0,
                      'str_fault': 0.0,
                      'str_unblance': 0.0,
                      'str_unmatch': 0.0,
                      't_dci': 0.0,
                      'temperature': 23.200000762939453,
                      'temperature2': 25.399999618530273,
                      'temperature3': 25.600000381469727,
                      'temperature4': 0.0,
                      'temperature5': 14.40000057220459,
                      'time': datetime.datetime(2024, 12, 20, 10, 29, 21),
                      'time_calendar': {'first_day_of_week': 1,
                                        'gregorian_change': {'date': 15,
                                                             'day': 5,
                                                             'hours': 8,
                                                             'minutes': 0,
                                                             'month': 9,
                                                             'seconds': 0,
                                                             'time': -12219292800000,
                                                             'timezone_offset': -480,
                                                             'year': -318},
                                        'lenient': True,
                                        'minimal_days_in_first_week': 1,
                                        'time': {'date': 20,
                                                 'day': 5,
                                                 'hours': 10,
                                                 'minutes': 29,
                                                 'month': 11,
                                                 'seconds': 21,
                                                 'time': 1734661761948,
                                                 'timezone_offset': -480,
                                                 'year': 124},
                                        'time_in_millis': 1734661761948,
                                        'time_zone': {'dirty': False,
                                                      'display_name': '中国标准时间',
                                                      'dst_savings': 0,
                                                      'id': 'Asia/Shanghai',
                                                      'last_rule_instance': None,
                                                      'raw_offset': 28800000},
                                        'week_date_supported': True,
                                        'week_year': 2024,
                                        'weeks_in_week_year': 52},
                      'time_total': 10568.921736111111,
                      'time_total_text': '10568.9',
                      'v_pid_pvape': 0.0,
                      'v_pid_pvbpe': 0.0,
                      'v_pid_pvcpe': 0.0,
                      'v_pid_pvdpe': 0.0,
                      'v_pid_pvepe': 0.0,
                      'v_pid_pvfpe': 0.0,
                      'v_pid_pvgpe': 0.0,
                      'v_pid_pvhpe': 0.0,
                      'v_string1': 264.70001220703125,
                      'v_string10': 149.60000610351562,
                      'v_string11': 149.5,
                      'v_string12': 149.5,
                      'v_string13': 0.0,
                      'v_string14': 0.0,
                      'v_string15': 0.0,
                      'v_string16': 0.0,
                      'v_string2': 264.70001220703125,
                      'v_string3': 259.6000061035156,
                      'v_string4': 259.6000061035156,
                      'v_string5': 219.0,
                      'v_string6': 219.0,
                      'v_string7': 156.90000915527344,
                      'v_string8': 156.90000915527344,
                      'v_string9': 149.60000610351562,
                      'vac_rs': 415.8999938964844,
                      'vac_st': 413.3999938964844,
                      'vac_tr': 412.6000061035156,
                      'vacr': 236.5,
                      'vacs': 244.5,
                      'vact': 239.3000030517578,
                      'vpv1': 265.20001220703125,
                      'vpv2': 260.0,
                      'vpv3': 220.0,
                      'vpv4': 157.10000610351562,
                      'vpv5': 149.8000030517578,
                      'vpv6': 149.60000610351562,
                      'vpv7': 0.0,
                      'vpv8': 0.0,
                      'w_pid_fault_value': 0,
                      'w_string_status_value': 0,
                      'warn_bit': 0,
                      'warn_code': 0,
                      'warning_value1': 0,
                      'warning_value2': 0,
                      'warning_value3': 0},
             'datalogger_sn': 'WLC082100F',
             'device_sn': 'SASF819012',
             'error_code': 0,
             'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/inverter/last_new_data",
            params={
                "device_sn": device_sn,
            },
        )

        return InverterEnergyOverview.model_validate(response)

    def energy_multiple(
        self,
        device_sn: Union[str, List[str]],
        page: Optional[int] = None,
    ) -> InverterEnergyOverviewMultiple:
        """
        Get the latest real-time data of inverters in batc
        Interface to obtain the latest real-time data of inverters in batches
        https://www.showdoc.com.cn/262556420217021/6119373063246256

        Note:
            Only applicable to devices with device type 1 (inverter) returned by device.list()

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)
            page (Optional[int]): page number, default 1, max 2

        Returns:
            InverterEnergyOverviewMultiple
            e.g.
            {'data': [{'data': {'again': False,
                                'apf_status': 0,
                                'big_device': False,
                                'compharir': 0.0,
                                'compharis': 0.0,
                                'compharit': 0.0,
                                'compqr': 0.0,
                                'compqs': 0.0,
                                'compqt': 0.0,
                                'ctharir': 0.0,
                                'ctharis': 0.0,
                                'ctharit': 0.0,
                                'ctir': 0.0,
                                'ctis': 0.0,
                                'ctit': 0.0,
                                'ctqr': 0.0,
                                'ctqs': 0.0,
                                'ctqt': 0.0,
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
                                'debug1': '0，0，0，250，32806，0，2671，5400',
                                'debug2': '0，0，0，0，0，8000，0，0',
                                'derating_mode': 0,
                                'dw_string_warning_value1': 0,
                                'e_rac_today': 0.0,
                                'e_rac_total': 0.0,
                                'epv1_today': 0.0,
                                'epv1_total': 102709.5,
                                'epv2_today': 0.0,
                                'epv2_total': 108261.0,
                                'epv3_today': 0.0,
                                'epv3_total': 100415.0,
                                'epv4_today': 0.0,
                                'epv4_total': 97070.5,
                                'epv5_today': 0.0,
                                'epv5_total': 103908.1,
                                'epv6_today': 0.0,
                                'epv6_total': 102971.9,
                                'epv7_today': 0.0,
                                'epv7_total': 0.0,
                                'epv8_today': 0.0,
                                'epv8_total': 0.0,
                                'epv_total': 615336.0,
                                'fac': 50.02000045776367,
                                'fault_code1': 0,
                                'fault_code2': 0,
                                'fault_type': 0,
                                'fault_value': 0,
                                'gfci': 1,
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
                                'inverter_id': 'SASF819012',
                                'ipm_temperature': 0.0,
                                'ipv1': 0.0,
                                'ipv2': 0.0,
                                'ipv3': 0.0,
                                'ipv4': 0.0,
                                'ipv5': 0.0,
                                'ipv6': 0.0,
                                'ipv7': 0.0,
                                'ipv8': 0.0,
                                'n_bus_voltage': 143.10000610351562,
                                'op_fullwatt': 0.0,
                                'p_bus_voltage': 140.90000915527344,
                                'pac': 0.0,
                                'pacr': 0.0,
                                'pacs': 0.0,
                                'pact': 0.0,
                                'pf': 1.0,
                                'pid_bus': 0.0,
                                'pid_fault_code': 0,
                                'pid_status': 0,
                                'power_today': 0.0,
                                'power_total': 303642.5,
                                'ppv': 0.0,
                                'ppv1': 0.0,
                                'ppv2': 0.0,
                                'ppv3': 0.0,
                                'ppv4': 0.0,
                                'ppv5': 0.0,
                                'ppv6': 0.0,
                                'ppv7': 0.0,
                                'ppv8': 0.0,
                                'pv_iso': 242.0,
                                'r_dci': 0.0,
                                'rac': 0.0,
                                'real_op_percent': 0.0,
                                's_dci': 0.0,
                                'status': 0,
                                'status_text': 'Waiting',
                                'str_break': 0.0,
                                'str_fault': 0.0,
                                'str_unblance': 0.0,
                                'str_unmatch': 0.0,
                                't_dci': 0.0,
                                'temperature': 23.200000762939453,
                                'temperature2': 25.399999618530273,
                                'temperature3': 25.600000381469727,
                                'temperature4': 0.0,
                                'temperature5': 14.40000057220459,
                                'time': datetime.datetime(2024, 12, 20, 10, 29, 21),
                                'time_calendar': {'first_day_of_week': 1,
                                                  'gregorian_change': {'date': 15,
                                                                       'day': 5,
                                                                       'hours': 8,
                                                                       'minutes': 0,
                                                                       'month': 9,
                                                                       'seconds': 0,
                                                                       'time': -12219292800000,
                                                                       'timezone_offset': -480,
                                                                       'year': -318},
                                                  'lenient': True,
                                                  'minimal_days_in_first_week': 1,
                                                  'time': {'date': 20,
                                                           'day': 5,
                                                           'hours': 10,
                                                           'minutes': 29,
                                                           'month': 11,
                                                           'seconds': 21,
                                                           'time': 1734661761948,
                                                           'timezone_offset': -480,
                                                           'year': 124},
                                                  'time_in_millis': 1734661761948,
                                                  'time_zone': {'dirty': False,
                                                                'display_name': '中国标准时间',
                                                                'dst_savings': 0,
                                                                'id': 'Asia/Shanghai',
                                                                'last_rule_instance': None,
                                                                'raw_offset': 28800000},
                                                  'week_date_supported': True,
                                                  'week_year': 2024,
                                                  'weeks_in_week_year': 52},
                                'time_total': 10568.921736111111,
                                'time_total_text': '10568.9',
                                'v_pid_pvape': 0.0,
                                'v_pid_pvbpe': 0.0,
                                'v_pid_pvcpe': 0.0,
                                'v_pid_pvdpe': 0.0,
                                'v_pid_pvepe': 0.0,
                                'v_pid_pvfpe': 0.0,
                                'v_pid_pvgpe': 0.0,
                                'v_pid_pvhpe': 0.0,
                                'v_string1': 264.70001220703125,
                                'v_string10': 149.60000610351562,
                                'v_string11': 149.5,
                                'v_string12': 149.5,
                                'v_string13': 0.0,
                                'v_string14': 0.0,
                                'v_string15': 0.0,
                                'v_string16': 0.0,
                                'v_string2': 264.70001220703125,
                                'v_string3': 259.6000061035156,
                                'v_string4': 259.6000061035156,
                                'v_string5': 219.0,
                                'v_string6': 219.0,
                                'v_string7': 156.90000915527344,
                                'v_string8': 156.90000915527344,
                                'v_string9': 149.60000610351562,
                                'vac_rs': 415.8999938964844,
                                'vac_st': 413.3999938964844,
                                'vac_tr': 412.6000061035156,
                                'vacr': 236.5,
                                'vacs': 244.5,
                                'vact': 239.3000030517578,
                                'vpv1': 265.20001220703125,
                                'vpv2': 260.0,
                                'vpv3': 220.0,
                                'vpv4': 157.10000610351562,
                                'vpv5': 149.8000030517578,
                                'vpv6': 149.60000610351562,
                                'vpv7': 0.0,
                                'vpv8': 0.0,
                                'w_pid_fault_value': 0,
                                'w_string_status_value': 0,
                                'warn_bit': 0,
                                'warn_code': 0,
                                'warning_value1': 0,
                                'warning_value2': 0,
                                'warning_value3': 0},
                       'datalogger_sn': 'WLC082100F',
                       'device_sn': 'SASF819012'}],
             'error_code': 0,
             'error_msg': None,
             'page_num': 1}
        """

        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/inverter/invs_data",
            data={
                "inverters": device_sn,
                "pageNum": page or 1,
            },
        )

        # Unfortunately, the original response cannot be parsed by pydantic as the inverter_sn is used as key
        # To fix this, resulting data is restructured
        devices = [
            InverterEnergyOverviewMultipleItem(
                device_sn=inverter_sn,
                datalogger_sn=response.get("data", {}).get(inverter_sn, {}).get("dataloggerSn", None),
                data=response.get("data", {}).get(inverter_sn, {}).get(inverter_sn, None),
            )
            for inverter_sn in response.get("inverters", [])
        ]
        response.pop("inverters", None)
        response["data"] = devices

        return InverterEnergyOverviewMultiple.model_validate(response)

    def energy_history(
        self,
        device_sn: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> InverterEnergyHistory:
        """
        Obtain historical data of an inverter
        Interface to obtain historical data of a certain inverter
        https://www.showdoc.com.cn/262556420217021/6118823163304569

        Note:
            Only applicable to devices with device type 1 (inverter) returned by device.list()

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10004: date interval exceeds seven days

        Args:
            device_sn (str): Inverter serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            InverterEnergyHistory
            e.g.
            {
                "data": {
                    "datas": [
                        {
                            "fac": 50,
                            "iac1": 12,
                            "iac2": 12,
                            "iac3": 12
                            "ipv1": 0,
                            "ipv2": 0,
                            "ipv3": 0,
                            "power": 8912.400390625,
                            "power_factor": -1,
                            "temperature": 75,
                            "time": "2018-12-13 11:03:52",
                            "today_energy": "7.6",
                            "total_energy": "7.6",
                            "vac1": 220,
                            "vac2": 220,
                            "vac3": 220,
                            "vpv1": 248,
                            "vpv2": 0,
                            "vpv3": 0,
                        }
                    ],
                    "device_sn": "ZT00100001",
                    "next_page_start_id": 21,
                    "datalogger_sn": "CRAZT00001"
                },
                "error_code": 0,
                "error_msg": ""
            }
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

        response = self.session.get(
            endpoint="device/inverter/data",
            params={
                "device_sn": device_sn,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return InverterEnergyHistory.model_validate(response)

    def alarms(
        self,
        device_sn: str,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> InverterAlarms:
        """
        Obtain historical data of an inverter
        Interface to obtain historical data of a certain inverter
        https://www.showdoc.com.cn/262556420217021/6118823163304569

        Note:
            Only applicable to devices with device type 1 (inverter) returned by device.list()

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error

        Args:
            device_sn (str): Inverter serial number
            date_ (Optional[date]): Date - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            InverterAlarms
            e.g.
            {
                "data": {
                    "sn": "LCB1714075",
                    "count": 161,
                    "alarms": [
                        {
                            "alarm_code": 25,
                            "status": 1,
                            "end_time": "2019-03-09 09:55:55.0",
                            "start_time": "2019-03-09 09:55:55.0",
                            "alarm_message": "No utility."
                        }
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
        """

        if date_ is None:
            date_ = date.today()

        response = self.session.get(
            endpoint="device/inverter/alarm",
            params={
                "device_sn": device_sn,
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return InverterAlarms.model_validate(response)
