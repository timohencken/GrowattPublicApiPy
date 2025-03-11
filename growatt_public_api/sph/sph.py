from datetime import date, timedelta
from typing import Optional, Union, List

import truststore

from pydantic_models.sph import (
    SphSettingRead,
    SphSettingWrite,
    SphDetails,
    SphEnergyOverview,
    SphEnergyHistory,
    SphAlarms,
    SphEnergyOverviewMultiple,
    SphEnergyOverviewMultipleItem,
)

truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


class Sph:
    """
    endpoints for SPH/MIX inverters
    https://www.showdoc.com.cn/262556420217021/6129761750718760

    Note:
        Only applicable to devices with device type 5 (sph) returned by device.list()
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
    ) -> SphSettingRead:
        """
        Read SPH setting parameter interface
        Read Mix setting parameter interface
        https://www.showdoc.com.cn/262556420217021/6129766954561259

        Note:
            Only applicable to devices with device type 5 (sph) returned by device.list()

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
            device_sn (str): SPH/MIN SN
            parameter_id (Optional[str]): parameter ID - specify either parameter_id ort start/end_address
            start_address (Optional[int]): register address to start reading from - specify either parameter_id ort start/end_address
            end_address (Optional[int]): register address to stop reading at

        Returns:
            SphSettingRead
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
            endpoint="readMixParam",
            data={
                "device_sn": device_sn,
                "paramId": parameter_id,
                "startAddr": start_address,
                "endAddr": end_address,
            },
        )

        return SphSettingRead.model_validate(response)

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
    ) -> SphSettingWrite:
        """
        SPH parameter settings
        Interface for Mix parameter setting
        https://www.showdoc.com.cn/262556420217021/6129761750718760

        Note:
            Only applicable to devices with device type 5 (sph) returned by device.list()

        This method allows to set
        * predefined settings (see table below)
        * any register value (see table below for most relevant settings, google for "Growatt Inverter Modbus RTU Protocol V1.20" for more)

        Predefined settings
        ========================+=======================================+===========================+============================================================================
        description             | parameter_id                          | parameter_value_[n]       | comment
        ========================+=======================================+===========================+============================================================================
        Grid priority           | mix_ac_discharge_time_period          | [ 1]: 0 ~ 100             | [ 1]: discharge power
                                |                                       | [ 2]: 0 ~ 100             | [ 2]: discharge stop SOC
                                |                                       | [ 3]: 0 ~ 23              | [ 3]: hour
                                |                                       | [ 4]: 0 ~ 59              | [ 4]: minute
                                |                                       | [ 5]: 0 ~ 23              | [ 5]: hour
                                |                                       | [ 6]: 0 ~ 59              | [ 6]: minute
                                |                                       | [ 7]: 0  or 1             | [ 7]: 0 = disable, 1 = enable
                                |                                       | [ 8]: 0 ~ 23              | [ 8]: hour
                                |                                       | [ 9]: 0 ~ 59              | [ 9]: minute
                                |                                       | [10]: 0 ~ 23              | [10]: hour
                                |                                       | [11]: 0 ~ 59              | [11]: minute
                                |                                       | [12]: 0  or 1             | [12]: 0 = disable, 1 = enable
                                |                                       | [13]: 0 ~ 23              | [13]: hour
                                |                                       | [14]: 0 ~ 59              | [14]: minute
                                |                                       | [15]: 0 ~ 23              | [15]: hour
                                |                                       | [16]: 0 ~ 59              | [16]: minute
                                |                                       | [17]: 0  or 1             | [17]: 0 = disable, 1 = enable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Battery priority        | mix_ac_charge_time_period             | [ 1]: 0 ~ 100             | [ 1]: charging power
                                |                                       | [ 2]: 0 ~ 100             | [ 2]: charge stop SOC
                                |                                       | [ 3]: 0  or 1             | [ 3]: mains - 0 = disable, 1 = enable
                                |                                       | [ 4]: 0 ~ 23              | [ 4]: hour
                                |                                       | [ 5]: 0 ~ 59              | [ 5]: minute
                                |                                       | [ 6]: 0 ~ 23              | [ 6]: hour
                                |                                       | [ 7]: 0 ~ 59              | [ 7]: minute
                                |                                       | [ 8]: 0  or 1             | [ 8]: 0 = disable, 1 = enable
                                |                                       | [ 9]: 0 ~ 23              | [ 9]: hour
                                |                                       | [10]: 0 ~ 59              | [10]: minute
                                |                                       | [11]: 0 ~ 23              | [11]: hour
                                |                                       | [12]: 0 ~ 59              | [12]: minute
                                |                                       | [13]: 0  or 1             | [13]: 0 = disable, 1 = enable
                                |                                       | [14]: 0 ~ 23              | [14]: hour
                                |                                       | [15]: 0 ~ 59              | [15]: minute
                                |                                       | [16]: 0 ~ 23              | [16]: hour
                                |                                       | [17]: 0 ~ 59              | [17]: minute
                                |                                       | [18]: 0  or 1             | [18]: 0 = disable, 1 = enable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow           | backflow_setting                      | [1]: 0 or 1               | [1]: 0 = off, 1 = on
                                |                                       | [2]: 0 ~ 100              | [2]: anti-reverse flow power percentage
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Power on and off        | pv_on_off                             | [1]: 0000 or 0001         | 0000 = off, 0001 = on
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set time                | pf_sys_year                           | [1]: "00:00" ~ "23:59"    | HH:MM
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Upper limit             | pv_grid_voltage_high                  | [1]: e.g. 270             | V
         of mains voltage       |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Lower limit             | pv_grid_voltage_low                   | [1]: e.g. 180             | V
         of mains voltage       |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Off-grid                | mix_off_grid_enable                   | [1]: 0 or 1               | 0 = disabled, 1 = enable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Off-grid frequency      | mix_ac_discharge_frequency            | [1]: 0 or 1               | 0 = 50Hz, 1 = 60Hz
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Off-grid voltage        | mix_ac_discharge_voltage              | [1]: 0 or 1 or 2          | 0 = 230V, 1 = 208V, 2 = 240V
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Whether to store the    | pv_pf_cmd_memory_state                | [1]: 0 or 1               | 0 = off, 1 = on
         following PF commands  |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Active power            | pv_active_p_rate                      | [1]: 0 ~ 100              |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Reactive power          | pv_reactive_p_rate                    | [1]: 0 ~ 100              |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        PF value                | pv_power_factor                       | [1]: -0.8 ~ -1            |
                                |                                       |   or  0.8 ~  1            |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Discharge stop SOC      | mix_load_flast_value_multi            | [1]: 0 ~ 100              |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        LoadFirst three-phase   | mix_load_first_control                | [1]: 0 or 1               | 0 = three-phase sum, 1 = single phase
         independent output     |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Single-phase            | mix_single_export                     | [1]: 0 or 1               | 0 = off, 1 = on
         anti-reverse flow      |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------

        Register settings
        =================
        google for "Growatt Inverter Modbus RTU Protocol V1.20" for more

        Specific error codes:
        * 10001: system error
        * 10002: server error of the mixed storage integrated machine
        * 10003: mixed storage integrated machine offline
        * 10004: mixed storage integrated machine serial number is empty
        * 10005: collector offline
        * 10006: Setting parameter type does not exist
        * 10007: Parameter value is empty
        * 10008: Parameter value is out of range
        * 10009: Date and time format is wrong
        * 10012: Hybrid storage integrated machine does not exist
        * 10013: End time cannot be less than start time

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
        parameters = {i: eval(f"parameter_value_{i}") for i in range(1, 19)}

        if parameter_id == "set_any_reg":
            assert parameters[1] is not None, "register address must be provided"
            assert parameters[2] is not None, "new value must be provided"
            for i in range(3, 19):
                assert (
                    parameters[i] is None
                ), f"parameter {i} must not be used for set_any_reg"
        else:
            assert parameters[1] is not None, "new value must be provided"

        # API docs: if there is no value, pass empty string ""
        for i in range(2, 19):
            if parameters[i] is None:
                parameters[i] = ""

        # parameter values must be string
        for i in range(1, 19):
            parameters[i] = str(parameters[i])

        response = self.session.post(
            endpoint="mixSet",
            data={
                "mix_sn": device_sn,
                "type": parameter_id,
                **{f"param{i}": parameters[i] for i in range(1, 19)},
            },
        )

        return SphSettingWrite.model_validate(response)

    def details(
        self,
        device_sn: str,
    ) -> SphDetails:
        """
        Get basic information of SPH
        Interface to get basic information of Mix
        https://www.showdoc.com.cn/262556420217021/6129763571291058

        Note:
            Only applicable to devices with device type 5 (sph) returned by device.list()

        Args:
            device_sn (str): Mix device SN

        Returns:
            SphDetails
            e.g.
            {   'data': {   'ac_charge_enable': True,
                            'activeRate': 50,
                            'address': 1,
                            'alias': 'SARN744005',
                            'backflow_setting': None,
                            'bat_aging_test_step': 0,
                            'bat_first_switch1': 0,
                            'bat_first_switch2': 0,
                            'bat_first_switch3': 0,
                            'bat_parallel_num': 0,
                            'bat_series_num': 0,
                            'bat_temp_lower_limit_c': 110.0,
                            'bat_temp_lower_limit_d': 110.0,
                            'bat_temp_upper_limit_c': 60.0,
                            'bat_temp_upper_limit_d': 70.0,
                            'battery_type': 1,
                            'baudrate': 0,
                            'bct_adjust': 0,
                            'bct_mode': 0,
                            'buck_ups_fun_en': True,
                            'buck_ups_volt_set': 0.0,
                            'cc_current': 0.0,
                            'charge_power_command': 100,
                            'charge_time1': None,
                            'charge_time2': None,
                            'charge_time3': None,
                            'children': [],
                            'com_address': 1,
                            'communication_version': None,
                            'country_selected': 0,
                            'cv_voltage': 0,
                            'datalogger_sn': 'BQC0733010',
                            'device_type': 0,
                            'discharge_power_command': 100,
                            'discharge_time1': None,
                            'discharge_time2': None,
                            'discharge_time3': None,
                            'dtc': 3501,
                            'energy_day': 0.0,
                            'energy_day_map': {},
                            'energy_month': 0.0,
                            'energy_month_text': '0',
                            'eps_freq_set': 1,
                            'eps_fun_en': True,
                            'eps_volt_set': 1,
                            'export_limit': 0,
                            'export_limit_power_rate': 0,
                            'failsafe': 0,
                            'float_charge_current_limit': 600,
                            'forced_charge_stop_switch1': True,
                            'forced_charge_stop_switch2': True,
                            'forced_charge_stop_switch3': True,
                            'forced_charge_time_start1': datetime.time(18, 0),
                            'forced_charge_time_start2': datetime.time(21, 30),
                            'forced_charge_time_start3': datetime.time(3, 0),
                            'forced_charge_time_stop1': datetime.time(19, 30),
                            'forced_charge_time_stop2': datetime.time(23, 0),
                            'forced_charge_time_stop3': datetime.time(4, 30),
                            'forced_discharge_stop_switch1': True,
                            'forced_discharge_stop_switch2': True,
                            'forced_discharge_stop_switch3': True,
                            'forced_discharge_time_start1': datetime.time(0, 0),
                            'forced_discharge_time_start2': datetime.time(0, 0),
                            'forced_discharge_time_start3': datetime.time(0, 0),
                            'forced_discharge_time_stop1': datetime.time(0, 0),
                            'forced_discharge_time_stop2': datetime.time(0, 0),
                            'forced_discharge_time_stop3': datetime.time(0, 0),
                            'fw_version': 'RA1.0',
                            'grid_first_switch1': False,
                            'grid_first_switch2': False,
                            'grid_first_switch3': False,
                            'group_id': -1,
                            'id': 0,
                            'img_path': './css/img/status_green.gif',
                            'inner_version': 'raaa040505',
                            'last_update_time': {'date': 5, 'day': 2, 'hours': 14, 'minutes': 43, 'month': 2, 'seconds': 57, 'time': 1551768237000, 'timezone_offset': -480, 'year': 119},
                            'last_update_time_text': datetime.datetime(2019, 3, 5, 14, 43, 57),
                            'lcd_language': 1,
                            'level': 4,
                            'location': 'null',
                            'lost': False,
                            'lv_voltage': 0,
                            'manufacturer': 'New Energy ',
                            'mix_ac_discharge_frequency': None,
                            'mix_ac_discharge_voltage': None,
                            'mix_off_grid_enable': None,
                            'modbus_version': 305,
                            'model': 1683928000000,
                            'model_text': 'A0B1D0T0PFU2M7S0',
                            'on_off': False,
                            'p_charge': 0,
                            'p_discharge': 0,
                            'parent_id': 'LIST_BQC0733010_96',
                            'pf_sys_year': None,
                            'plant_id': 0,
                            'plant_name': None,
                            'pmax': 0,
                            'port_name': 'port_name',
                            'power_factor': 0.0,
                            'power_max': None,
                            'power_max_text': None,
                            'power_max_time': None,
                            'priority_choose': 0,
                            'pv_active_p_rate': None,
                            'pv_grid_voltage_high': None,
                            'pv_grid_voltage_low': None,
                            'pv_on_off': None,
                            'pv_pf_cmd_memory_state': True,
                            'pv_pf_cmd_memory_state_mix': True,
                            'pv_power_factor': None,
                            'pv_reactive_p_rate': None,
                            'pv_reactive_p_rate_two': None,
                            'reactive_rate': 100,
                            'record': None,
                            'serial_num': 'SARN744005',
                            'status': 5,
                            'status_text': 'mix.status.normal',
                            'sys_time': datetime.datetime(2019, 3, 5, 10, 37, 29),
                            'tcp_server_ip': '192.168.3.35',
                            'tree_id': 'ST_SARN744005',
                            'tree_name': 'SARN744005',
                            'under_excited': 0,
                            'updating': False,
                            'user_name': None,
                            'usp_freq_set': 0,
                            'vbat_start_for_charge': 58.0,
                            'vbat_start_for_discharge': 48.0,
                            'vbat_stop_for_charge': 5.75,
                            'vbat_stop_for_discharge': 4.699999809265137,
                            'vbat_warn_clr': 5.0,
                            'vbat_warning': 480.0,
                            'vnormal': 360.0,
                            'voltage_high_limit': 263.0,
                            'voltage_low_limit': 186.0,
                            'wcharge_soc_low_limit1': 100,
                            'wcharge_soc_low_limit2': 100,
                            'wdis_charge_soc_low_limit1': 100,
                            'wdis_charge_soc_low_limit2': 5},
                'datalogger_sn': 'BQC0733010',
                'device_sn': 'SARN744005',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/mix/mix_data_info",
            params={
                "device_sn": device_sn,
            },
        )

        return SphDetails.model_validate(response)

    def energy(
        self,
        device_sn: str,
    ) -> SphEnergyOverview:
        """
        Get the latest real-time data of SPH
        Interface to get the latest real-time data of Mix
        https://www.showdoc.com.cn/262556420217021/6129764434976910

        Note:
            Only applicable to devices with device type 5 (sph) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: Mix does not exist
        * 10003: device SN error

        Args:
            device_sn (str): SPH/MIX serial number

        Returns:
            SphEnergyOverview
            e.g.
            {   'data': {   'ac_charge_energy_today': 0.0,
                            'ac_charge_energy_total': 0.0,
                            'ac_charge_power': 0.0,
                            'address': 0,
                            'again': False,
                            'alias': None,
                            'battery_temperature': 0.0,
                            'battery_type': 0,
                            'bms_battery_curr': 0.0,
                            'bms_battery_temp': 28.0,
                            'bms_battery_volt': 56.7400016784668,
                            'bms_cell10_volt': 3.549999952316284,
                            'bms_cell11_volt': 3.549999952316284,
                            'bms_cell12_volt': 3.549999952316284,
                            'bms_cell13_volt': 3.5490000247955322,
                            'bms_cell14_volt': 3.5490000247955322,
                            'bms_cell15_volt': 3.5490000247955322,
                            'bms_cell16_volt': 3.549999952316284,
                            'bms_cell1_volt': 3.5480000972747803,
                            'bms_cell2_volt': 3.5480000972747803,
                            'bms_cell3_volt': 3.549999952316284,
                            'bms_cell4_volt': 3.549999952316284,
                            'bms_cell5_volt': 3.549999952316284,
                            'bms_cell6_volt': 3.5510001182556152,
                            'bms_cell7_volt': 3.549999952316284,
                            'bms_cell8_volt': 3.549999952316284,
                            'bms_cell9_volt': 3.513000011444092,
                            'bms_constant_volt': 56.79999923706055,
                            'bms_cycle_cnt': 1331,
                            'bms_delta_volt': 38.0,
                            'bms_error': 0,
                            'bms_error_old': 0,
                            'bms_fw': 257,
                            'bms_gauge_fcc': 100.0,
                            'bms_gauge_rm': 49.9900016784668,
                            'bms_info': 257,
                            'bms_max_curr': 100.0,
                            'bms_max_dischg_curr': 0.0,
                            'bms_mcu_version': 512,
                            'bms_pack_info': 257,
                            'bms_soc': 100,
                            'bms_soh': 47,
                            'bms_status': 361,
                            'bms_status_old': 361,
                            'bms_using_cap': 5000,
                            'bms_warn_info': 0,
                            'bms_warn_info_old': 0,
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 5, 'day': 2, 'hours': 14, 'minutes': 35, 'month': 2, 'seconds': 43, 'time': 1551767743000, 'timezone_offset': -480, 'year': 119},
                                            'time_in_millis': 1551767743000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2019,
                                            'weeks_in_week_year': 52},
                            'datalogger_sn': None,
                            'day': None,
                            'day_map': None,
                            'e_to_grid_today': 0.3,
                            'e_to_grid_total': 2293.0,
                            'e_to_user_today': 0.0,
                            'e_to_user_total': 11991.1,
                            'eac_today': 0.0,
                            'eac_total': 2015.9,
                            'echarge1_today': 0.2,
                            'echarge1_total': 6113.2,
                            'edischarge1_today': 0.4,
                            'edischarge1_total': 5540.6,
                            'elocal_load_today': 0.0,
                            'elocal_load_total': 26980.8,
                            'eps_vac2': 0.0,
                            'eps_vac3': 0.0,
                            'epv1_today': 0.5,
                            'epv1_total': 2352.3,
                            'epv2_today': 0.0,
                            'epv2_total': 0.0,
                            'epv_total': 2352.3,
                            'error_code': 0,
                            'error_text': 'Unknown',
                            'fac': 50.060001373291016,
                            'fault_bit_code': 0,
                            'fault_code': 0,
                            'lost': True,
                            'mix_bean': None,
                            'pac': 0.0,
                            'pac1': 0.0,
                            'pac2': 0.0,
                            'pac3': 0.0,
                            'pac_to_grid_r': 38.6,
                            'pac_to_grid_total': 38.6,
                            'pac_to_user_r': 0.0,
                            'pac_to_user_total': 0.0,
                            'pcharge1': 0.0,
                            'pdischarge1': 16.5,
                            'plocal_load_r': 0.0,
                            'plocal_load_total': 0.0,
                            'ppv': 3.9,
                            'ppv1': 3.9,
                            'ppv2': 0.0,
                            'ppv_text': '3.9 W',
                            'priority_choose': 0.0,
                            'serial_num': 'SARN744005',
                            'soc': 100.0,
                            'soc_text': '100%',
                            'status': 5,
                            'status_text': 'PV Bat Online',
                            'sys_en': False,
                            'sys_fault_word': 0,
                            'sys_fault_word1': 0,
                            'sys_fault_word2': 0,
                            'sys_fault_word3': 0,
                            'sys_fault_word4': 0,
                            'sys_fault_word5': 0,
                            'sys_fault_word6': 0,
                            'sys_fault_word7': 256,
                            'temp1': 34.0,
                            'temp2': 33.099998474121094,
                            'temp3': 33.099998474121094,
                            'time': datetime.datetime(2019, 3, 5, 14, 35, 43),
                            'time_total': 8509378.5,
                            'ups_fac': 0.0,
                            'ups_load_percent': 0.0,
                            'ups_pac1': 0.0,
                            'ups_pac2': 0.0,
                            'ups_pac3': 0.0,
                            'ups_pf': 1000.0,
                            'ups_vac1': 0.0,
                            'uw_sys_work_mode': 5,
                            'v_bat_dsp': 0.0,
                            'v_bus1': 0.0,
                            'v_bus2': 0.0,
                            'vac1': 219.89999389648438,
                            'vac2': 0.0,
                            'vac3': 0.0,
                            'vbat': 56.70000076293945,
                            'vpv1': 264.79998779296875,
                            'vpv2': 0.0,
                            'warn_code': 0,
                            'warn_text': 'Unknown',
                            'with_time': False},
                'datalogger_sn': 'BQC0733010',
                'device_sn': 'SARN744005',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/mix/mix_last_data",
            data={
                "mix_sn": device_sn,
            },
        )

        return SphEnergyOverview.model_validate(response)

    def energy_multiple(
        self,
        device_sn: Union[str, List[str]],
        page: Optional[int] = None,
    ) -> SphEnergyOverviewMultiple:
        """
        Get the latest real-time data of SPH in batches
        Interface to obtain the latest real-time data of inverters in batches
        https://www.showdoc.com.cn/262556420217021/6129786427013561

        Note:
            Only applicable to devices with device type 5 (sph) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: System error
        * 10002: Device serial number error
        * 10003: Date format error
        * 10004: Date interval exceeds seven days
        * 10005: Mix does not exist

        Args:
            device_sn (Union[str, List[str]]): SPH/MIX serial number or list of (multiple) SPH/MIX serial numbers (max 100)
            page (Optional[int]): page number, default 1, max 2

        Returns:
            SphEnergyOverviewMultiple
            {   'data': [   {   'data': {   'ac_charge_energy_today': 0.0,
                                            'ac_charge_energy_total': 0.0,
                                            'ac_charge_power': 0.0,
                                            'address': 0,
                                            'again': False,
                                            'alias': None,
                                            'battery_temperature': 329.0,
                                            'battery_type': 1,
                                            'bms_battery_curr': -10.489999771118164,
                                            'bms_battery_temp': 32.0,
                                            'bms_battery_volt': 53.0,
                                            'bms_cell10_volt': 3.313999891281128,
                                            'bms_cell11_volt': 3.315000057220459,
                                            'bms_cell12_volt': 3.313999891281128,
                                            'bms_cell13_volt': 3.315000057220459,
                                            'bms_cell14_volt': 3.315000057220459,
                                            'bms_cell15_volt': 3.315000057220459,
                                            'bms_cell16_volt': 3.313999891281128,
                                            'bms_cell1_volt': 3.313999891281128,
                                            'bms_cell2_volt': 3.313999891281128,
                                            'bms_cell3_volt': 3.313999891281128,
                                            'bms_cell4_volt': 3.313999891281128,
                                            'bms_cell5_volt': 3.313999891281128,
                                            'bms_cell6_volt': 3.313999891281128,
                                            'bms_cell7_volt': 3.313999891281128,
                                            'bms_cell8_volt': 3.313999891281128,
                                            'bms_cell9_volt': 3.313999891281128,
                                            'bms_constant_volt': 56.79999923706055,
                                            'bms_cycle_cnt': 196,
                                            'bms_delta_volt': 1.0,
                                            'bms_error': 0,
                                            'bms_error_old': 0,
                                            'bms_fw': 70,
                                            'bms_gauge_fcc': 228.0,
                                            'bms_gauge_rm': 204.5399932861328,
                                            'bms_info': 16720,
                                            'bms_max_curr': 128.0,
                                            'bms_max_dischg_curr': 170.0,
                                            'bms_mcu_version': 70,
                                            'bms_pack_info': 16720,
                                            'bms_soc': 84,
                                            'bms_soh': 100,
                                            'bms_status': 355,
                                            'bms_status_old': 0,
                                            'bms_using_cap': 0,
                                            'bms_warn_info': 0,
                                            'bms_warn_info_old': 0,
                                            'calendar': {   'first_day_of_week': 1,
                                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                            'lenient': True,
                                                            'minimal_days_in_first_week': 1,
                                                            'time': {'date': 8, 'day': 5, 'hours': 18, 'minutes': 10, 'month': 0, 'seconds': 31, 'time': 1610100631000, 'timezone_offset': -480, 'year': 121},
                                                            'time_in_millis': 1610100631000,
                                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                            'week_date_supported': True,
                                                            'week_year': 2021,
                                                            'weeks_in_week_year': 52},
                                            'datalogger_sn': None,
                                            'day': None,
                                            'day_map': None,
                                            'e_to_grid_today': 19.2,
                                            'e_to_grid_total': 1539.7,
                                            'e_to_user_today': 1.2,
                                            'e_to_user_total': 3077.6,
                                            'eac_today': 37.599998474121094,
                                            'eac_total': 6595.9,
                                            'echarge1_today': 6.6,
                                            'echarge1_total': 2230.6,
                                            'edischarge1_today': 4.4,
                                            'edischarge1_total': 2280.8,
                                            'elocal_load_today': 18.9,
                                            'elocal_load_total': 30892.6,
                                            'eps_vac2': 0.0,
                                            'eps_vac3': 0.0,
                                            'epv1_today': 20.899999618530273,
                                            'epv1_total': 3527.3,
                                            'epv2_today': 21.200000762939453,
                                            'epv2_total': 3409.1,
                                            'epv_total': 6936.4,
                                            'error_code': 0,
                                            'error_text': 'Unknown',
                                            'fac': 50.029998779296875,
                                            'fault_bit_code': 0,
                                            'fault_code': 0,
                                            'lost': True,
                                            'mix_bean': None,
                                            'pac': 780.9,
                                            'pac1': 783.0,
                                            'pac2': 0.0,
                                            'pac3': 0.0,
                                            'pac_to_grid_r': 0.0,
                                            'pac_to_grid_total': 0.0,
                                            'pac_to_user_r': 67.3,
                                            'pac_to_user_total': 67.3,
                                            'pcharge1': 0.0,
                                            'pdischarge1': 605.1,
                                            'plocal_load_r': 949.8,
                                            'plocal_load_total': 949.8,
                                            'ppv': 245.4,
                                            'ppv1': 113.7,
                                            'ppv2': 131.7,
                                            'ppv_text': '245.4 W',
                                            'priority_choose': 0.0,
                                            'serial_num': 'NTCF946079',
                                            'soc': 84.0,
                                            'soc_text': '84%',
                                            'status': 5,
                                            'status_text': 'PV Bat Online',
                                            'sys_en': 17056,
                                            'sys_fault_word': 0,
                                            'sys_fault_word1': 0,
                                            'sys_fault_word2': 0,
                                            'sys_fault_word3': 0,
                                            'sys_fault_word4': 0,
                                            'sys_fault_word5': 0,
                                            'sys_fault_word6': 0,
                                            'sys_fault_word7': 0,
                                            'temp1': 48.0,
                                            'temp2': 44.0,
                                            'temp3': 45.0,
                                            'time': datetime.datetime(2021, 1, 8, 18, 10, 31),
                                            'time_total': 26446612.5,
                                            'ups_fac': 0.0,
                                            'ups_load_percent': 0.0,
                                            'ups_pac1': 0.0,
                                            'ups_pac2': 0.0,
                                            'ups_pac3': 0.0,
                                            'ups_pf': 1000.0,
                                            'ups_vac1': 0.0,
                                            'uw_sys_work_mode': 5,
                                            'v_bat_dsp': 53.29999923706055,
                                            'v_bus1': 370.0,
                                            'v_bus2': 298.0,
                                            'vac1': 231.10000610351562,
                                            'vac2': 0.0,
                                            'vac3': 0.0,
                                            'vbat': 53.0,
                                            'vpv1': 324.70001220703125,
                                            'vpv2': 328.8999938964844,
                                            'warn_code': 0,
                                            'warn_text': 'Unknown',
                                            'with_time': False},
                                'datalogger_sn': 'NAC59173CA',
                                'device_sn': 'NTCF946079'},
                            {   'data': {   'ac_charge_energy_today': 0.0, ...},
                                'datalogger_sn': 'NAC59173CA',
                                'device_sn': 'NTCF946079'}],
                'error_code': 0,
                'error_msg': None,
                'page_num': 1}
        """

        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/mix/mixs_data",
            data={
                "mixs": device_sn,
                "pageNum": page or 1,
            },
        )

        # Unfortunately, the original response cannot be parsed by pydantic as the inverter_sn is used as key
        # To fix this, resulting data is restructured
        devices = [
            SphEnergyOverviewMultipleItem(
                device_sn=inverter_sn,
                datalogger_sn=response.get("data", {})
                .get(inverter_sn, {})
                .get("dataloggerSn", None),
                data=response.get("data", {})
                .get(inverter_sn, {})
                .get(inverter_sn, None),
            )
            for inverter_sn in response.get("mixs", [])
        ]
        response.pop("mixs", None)
        response["data"] = devices

        return SphEnergyOverviewMultiple.model_validate(response)

    def energy_history(
        self,
        device_sn: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> SphEnergyHistory:
        """
        Get historical data of a SPH
        Interface to get historical data of a certain Mix
        https://www.showdoc.com.cn/262556420217021/6129765461123058

        Note:
            Only applicable to devices with device type 5 (sph) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Device serial number error
        * 10003: Date format error
        * 10004: Date interval exceeds seven days
        * 10005: Mix does not exist

        Args:
            device_sn (str): SPH/MIX serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            SphEnergyHistory
            {   'data': {   'count': 9225,
                            'datalogger_sn': 'BQC0733010',
                            'datas': [   {   'ac_charge_energy_today': 0.0,
                                             'ac_charge_energy_total': 124.30000305175781,
                                             'ac_charge_power': 0.0,
                                             'address': 0,
                                             'again': False,
                                             'alias': None,
                                             'battery_temperature': 0.0,
                                             'battery_type': 1,
                                             'bms_battery_curr': 0.0,
                                             'bms_battery_temp': 28.0,
                                             'bms_battery_volt': 56.7400016784668,
                                             'bms_cell10_volt': 3.549999952316284,
                                             'bms_cell11_volt': 3.549999952316284,
                                             'bms_cell12_volt': 3.5510001182556152,
                                             'bms_cell13_volt': 3.5490000247955322,
                                             'bms_cell14_volt': 3.5490000247955322,
                                             'bms_cell15_volt': 3.5490000247955322,
                                             'bms_cell16_volt': 3.5480000972747803,
                                             'bms_cell1_volt': 3.5480000972747803,
                                             'bms_cell2_volt': 3.5480000972747803,
                                             'bms_cell3_volt': 3.549999952316284,
                                             'bms_cell4_volt': 3.549999952316284,
                                             'bms_cell5_volt': 3.549999952316284,
                                             'bms_cell6_volt': 3.5510001182556152,
                                             'bms_cell7_volt': 3.549999952316284,
                                             'bms_cell8_volt': 3.549999952316284,
                                             'bms_cell9_volt': 3.510999917984009,
                                             'bms_constant_volt': 56.79999923706055,
                                             'bms_cycle_cnt': 1331,
                                             'bms_delta_volt': 40.0,
                                             'bms_error': 0,
                                             'bms_error_old': 0,
                                             'bms_fw': 257,
                                             'bms_gauge_fcc': 100.0,
                                             'bms_gauge_rm': 49.97999954223633,
                                             'bms_info': 257,
                                             'bms_max_curr': 100.0,
                                             'bms_max_dischg_curr': 0.0,
                                             'bms_mcu_version': 512,
                                             'bms_pack_info': 257,
                                             'bms_soc': 100,
                                             'bms_soh': 47,
                                             'bms_status': 361,
                                             'bms_status_old': 361,
                                             'bms_using_cap': 5000,
                                             'bms_warn_info': 0,
                                             'bms_warn_info_old': 0,
                                             'calendar': {   'first_day_of_week': 1,
                                                             'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                             'lenient': True,
                                                             'minimal_days_in_first_week': 1,
                                                             'time': {'date': 5, 'day': 2, 'hours': 15, 'minutes': 51, 'month': 2, 'seconds': 22, 'time': 1551772282000, 'timezone_offset': -480, 'year': 119},
                                                             'time_in_millis': 1551772282000,
                                                             'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                             'week_date_supported': True,
                                                             'week_year': 2019,
                                                             'weeks_in_week_year': 52},
                                             'datalogger_sn': None,
                                             'day': None,
                                             'day_map': None,
                                             'e_to_grid_today': 0.3,
                                             'e_to_grid_total': 2293.4,
                                             'e_to_user_today': 0.0,
                                             'e_to_user_total': 11991.1,
                                             'eac_today': 0.0,
                                             'eac_total': 2015.9,
                                             'echarge1_today': 0.2,
                                             'echarge1_total': 6113.2,
                                             'edischarge1_today': 0.4,
                                             'edischarge1_total': 5540.6,
                                             'elocal_load_today': 0.4,
                                             'elocal_load_total': 26980.8,
                                             'eps_vac2': 0.0,
                                             'eps_vac3': 0.0,
                                             'epv1_today': 0.5,
                                             'epv1_total': 2352.3,
                                             'epv2_today': 0.0,
                                             'epv2_total': 0.0,
                                             'epv_total': 2352.3,
                                             'error_code': 0,
                                             'error_text': 'Unknown',
                                             'fac': 49.97999954223633,
                                             'fault_bit_code': 0,
                                             'fault_code': 0,
                                             'lost': True,
                                             'mix_bean': None,
                                             'pac': 0.0,
                                             'pac1': 0.0,
                                             'pac2': 0.0,
                                             'pac3': 0.0,
                                             'pac_to_grid_r': 37.7,
                                             'pac_to_grid_total': 37.7,
                                             'pac_to_user_r': 0.0,
                                             'pac_to_user_total': 0.0,
                                             'pcharge1': 0.0,
                                             'pdischarge1': 24.1,
                                             'plocal_load_r': 0.0,
                                             'plocal_load_total': 0.0,
                                             'ppv': 93.5,
                                             'ppv1': 93.5,
                                             'ppv2': 0.0,
                                             'ppv_text': '93.5 W',
                                             'priority_choose': 0.0,
                                             'serial_num': 'SARN744005',
                                             'soc': 100.0,
                                             'soc_text': '100%',
                                             'status': 5,
                                             'status_text': 'PV Bat Online',
                                             'sys_en': 8864,
                                             'sys_fault_word': 0,
                                             'sys_fault_word1': 0,
                                             'sys_fault_word2': 0,
                                             'sys_fault_word3': 0,
                                             'sys_fault_word4': 0,
                                             'sys_fault_word5': 0,
                                             'sys_fault_word6': 0,
                                             'sys_fault_word7': 256,
                                             'temp1': 34.0,
                                             'temp2': 33.0,
                                             'temp3': 33.0,
                                             'time': datetime.datetime(2019, 3, 5, 15, 51, 22),
                                             'time_total': 8513914.5,
                                             'ups_fac': 0.0,
                                             'ups_load_percent': 0.0,
                                             'ups_pac1': 0.0,
                                             'ups_pac2': 0.0,
                                             'ups_pac3': 0.0,
                                             'ups_pf': 1000.0,
                                             'ups_vac1': 0.0,
                                             'uw_sys_work_mode': 5,
                                             'v_bat_dsp': 56.70000076293945,
                                             'v_bus1': 391.0,
                                             'v_bus2': 322.0,
                                             'vac1': 219.10000610351562,
                                             'vac2': 0.0,
                                             'vac3': 0.0,
                                             'vbat': 56.70000076293945,
                                             'vpv1': 264.20001220703125,
                                             'vpv2': 0.0,
                                             'warn_code': 0,
                                             'warn_text': 'Unknown',
                                             'with_time': False}],
                            'device_sn': 'SARN744005',
                            'next_page_start_id': 21},
                'error_code': 0,
                'error_msg': None}
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
            endpoint="device/mix/mix_data",
            data={
                "mix_sn": device_sn,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return SphEnergyHistory.model_validate(response)

    def alarms(
        self,
        device_sn: str,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> SphAlarms:
        """
        Get the alarm data of a certain SPH
        Interface to get the alarm data of a certain Mix
        https://www.showdoc.com.cn/262556420217021/6129766025111256

        Note:
            Only applicable to devices with device type 5 (sph) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10005: Mix does not exist

        Args:
            device_sn (str): SPH/MIX device serial number
            date_ (Optional[date]): Date - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            SphAlarms
            e.g.
            {
                'data': {
                    'alarms': [
                        {
                            'alarm_code': 1,
                            'alarm_message': '',
                            'end_time': datetime.datetime(2018, 12, 17, 14, 5, 54),
                            'start_time': datetime.datetime(2018, 12, 17, 14, 5, 54),
                            'status': 1
                        }
                    ],
                    'count': 1,
                    'device_sn': 'SARN744005'
                },
                'error_code': 0,
                'error_msg': None
            }
        """

        if date_ is None:
            date_ = date.today()

        response = self.session.post(
            endpoint="device/mix/alarm_data",
            data={
                "mix_sn": device_sn,
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return SphAlarms.model_validate(response)
