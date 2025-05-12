from datetime import date, timedelta
from typing import Optional, Union, List, Dict, Any

import truststore

from pydantic_models.min import (
    MinSettingRead,
    MinSettingWrite,
    MinDetails,
    MinEnergyOverview,
    MinEnergyHistory,
    MinAlarms,
    MinEnergyOverviewMultiple,
    MinEnergyOverviewMultipleItem,
    MinSettings,
)

truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


class Min:
    """
    endpoints for MIN / TLX inverters
    https://www.showdoc.com.cn/262556420217021/6129816412127075

    Note:
        Only applicable to devices with device type 7 (min) returned by device.list()
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def settings(
        self,
        device_sn: str,
    ) -> MinSettings:
        """
        Read Min settings
        https://www.showdoc.com.cn/262556420217021/8696815667375182

        Note:
            Only applicable to devices with device type 7 (min) returned by device.list()

        Args:
            device_sn (str): inverter SN

        Returns:
            MinSettings
            {   'data': {   'ac_charge': None,
                            'ac_charge_enable': False,
                            'active_power_enable': False,
                            'active_rate': 100.0,
                            'afci_enabled': -1,
                            'afci_reset': -1,
                            'afci_self_check': -1,
                            'afci_threshold_d': -1.0,
                            'afci_threshold_h': -1.0,
                            'afci_threshold_l': -1.0,
                            'backflow_default_power': 0.0,
                            'backflow_single_ctrl': None,
                            'bdc_mode': -1,
                            'bgrid_type': 0,
                            'bsystem_work_mode': 500.0,
                            'charge_power': None,
                            'charge_power_command': 100.0,
                            'charge_stop_soc': None,
                            'compatible_flag': None,
                            'delay_time': 0,
                            'demand_manage_enable': None,
                            'discharge_power': None,
                            'discharge_power_command': 100.0,
                            'discharge_stop_soc': None,
                            'dry_contact_func_en': 0.0,
                            'dry_contact_off_rate': 40.0,
                            'dry_contact_on_rate': 40.0,
                            'dry_contact_power': 50.0,
                            'enable_n_line': None,
                            'eps_freq_set': 0.0,
                            'eps_fun_en': 1.0,
                            'eps_volt_set': 2.0,
                            'export_limit': 0.0,
                            'export_limit_power_rate': 0.0,
                            'export_limit_power_rate_str': None,
                            'exter_comm_off_grid_en': 0,
                            'fail_safe_curr': None,
                            'fft_threshold_count': -1,
                            'float_charge_current_limit': 600.0,
                            'forced_stop_switch1': 0,
                            'forced_stop_switch2': 0,
                            'forced_stop_switch3': 0,
                            'forced_stop_switch4': 0,
                            'forced_stop_switch5': 0,
                            'forced_stop_switch6': 0,
                            'forced_stop_switch7': 0,
                            'forced_stop_switch8': 0,
                            'forced_stop_switch9': 0,
                            'forced_time_start1': datetime.time(0, 0),
                            'forced_time_start2': datetime.time(0, 0),
                            'forced_time_start3': datetime.time(0, 0),
                            'forced_time_start4': datetime.time(0, 0),
                            'forced_time_start5': datetime.time(0, 0),
                            'forced_time_start6': datetime.time(0, 0),
                            'forced_time_start7': datetime.time(0, 0),
                            'forced_time_start8': datetime.time(0, 0),
                            'forced_time_start9': datetime.time(0, 0),
                            'forced_time_stop1': datetime.time(0, 0),
                            'forced_time_stop2': datetime.time(0, 0),
                            'forced_time_stop3': datetime.time(0, 0),
                            'forced_time_stop4': datetime.time(0, 0),
                            'forced_time_stop5': datetime.time(0, 0),
                            'forced_time_stop6': datetime.time(0, 0),
                            'forced_time_stop7': datetime.time(0, 0),
                            'forced_time_stop8': datetime.time(0, 0),
                            'forced_time_stop9': datetime.time(0, 0),
                            'frequency_high_limit': 50.099998474121094,
                            'frequency_low_limit': 49.5,
                            'gen_charge_enable': None,
                            'gen_ctrl': None,
                            'gen_rated_power': None,
                            'last_update_time': {'date': 12, 'day': 2, 'hours': 10, 'minutes': 11, 'month': 3, 'seconds': 9, 'time': 1649729469000, 'timezone_offset': -480, 'year': 122},
                            'last_update_time_text': datetime.datetime(2022, 4, 12, 10, 11, 9),
                            'lcd_language': 1,
                            'limit_device': -1.0,
                            'loading_rate': 20.0,
                            'maintain_mode_request': None,
                            'maintain_mode_start_time': None,
                            'max_allow_curr': None,
                            'on_grid_discharge_stop_soc': None,
                            'on_grid_mode': None,
                            'on_grid_status': None,
                            'on_off': 1,
                            'over_fre_drop_point': 50.029998779296875,
                            'over_fre_lo_red_delay_time': 0.0,
                            'over_fre_lo_red_slope': 41.0,
                            'peak_shaving_enable': None,
                            'pf': 0.8899999856948853,
                            'pf_model': 0.0,
                            'pf_sys_year': None,
                            'pflinep1_lp': 255.0,
                            'pflinep1_pf': 1.0,
                            'pflinep2_lp': 255.0,
                            'pflinep2_pf': 1.0,
                            'pflinep3_lp': 255.0,
                            'pflinep3_pf': 1.0,
                            'pflinep4_lp': 255.0,
                            'pflinep4_pf': 1.0,
                            'power_down_enable': None,
                            'pre_pto': None,
                            'prot_enable': None,
                            'pu_enable': None,
                            'pv_grid_frequency_high': None,
                            'pv_grid_frequency_low': None,
                            'pv_grid_voltage_high': None,
                            'pv_grid_voltage_low': None,
                            'pv_pf_cmd_memory_state': 0,
                            'q_percent_max': 44.0,
                            'qv_h1': 247.1999969482422,
                            'qv_h2': 256.79998779296875,
                            'qv_l1': 232.0,
                            'qv_l2': 220.8000030517578,
                            'reactive_rate': 0.0,
                            'region': None,
                            'restart_loading_rate': 20.0,
                            'rrcr_enable': None,
                            'safety_correspond_num': None,
                            'safety_num': None,
                            'season1_month_time': '0_0_0',
                            'season1_time1': '0_0_0_0_0_0_0',
                            'season1_time2': '0_0_0_0_0_0_0',
                            'season1_time3': '0_0_0_0_0_0_0',
                            'season1_time4': '0_0_0_0_0_0_0',
                            'season1_time5': '0_0_0_0_0_0_0',
                            'season1_time6': '0_0_0_0_0_0_0',
                            'season1_time7': '0_0_0_0_0_0_0',
                            'season1_time8': '0_0_0_0_0_0_0',
                            'season1_time9': '0_0_0_0_0_0_0',
                            'season2_month_time': '0_0_0',
                            'season2_time1': '0_0_0_0_0_0_0',
                            'season2_time2': '0_0_0_0_0_0_0',
                            'season2_time3': '0_0_0_0_0_0_0',
                            'season2_time4': '0_0_0_0_0_0_0',
                            'season2_time5': '0_0_0_0_0_0_0',
                            'season2_time6': '0_0_0_0_0_0_0',
                            'season2_time7': '0_0_0_0_0_0_0',
                            'season2_time8': '0_0_0_0_0_0_0',
                            'season2_time9': '0_0_0_0_0_0_0',
                            'season3_month_time': '0_0_0',
                            'season3_time1': '0_0_0_0_0_0_0',
                            'season3_time2': '0_0_0_0_0_0_0',
                            'season3_time3': '0_0_0_0_0_0_0',
                            'season3_time4': '0_0_0_0_0_0_0',
                            'season3_time5': '0_0_0_0_0_0_0',
                            'season3_time6': '0_0_0_0_0_0_0',
                            'season3_time7': '0_0_0_0_0_0_0',
                            'season3_time8': '0_0_0_0_0_0_0',
                            'season3_time9': '0_0_0_0_0_0_0',
                            'season4_month_time': '0_0_0',
                            'season4_time1': '0_0_0_0_0_0_0',
                            'season4_time2': '0_0_0_0_0_0_0',
                            'season4_time3': '0_0_0_0_0_0_0',
                            'season4_time4': '0_0_0_0_0_0_0',
                            'season4_time5': '0_0_0_0_0_0_0',
                            'season4_time6': '0_0_0_0_0_0_0',
                            'season4_time7': '0_0_0_0_0_0_0',
                            'season4_time8': '0_0_0_0_0_0_0',
                            'season4_time9': '0_0_0_0_0_0_0',
                            'serial_num': 'FDCJQ00003',
                            'show_peak_shaving': None,
                            'special1_month_time': '0_0_0',
                            'special1_time1': '0_0_0_0_0_0',
                            'special1_time2': '0_0_0_0_0_0',
                            'special1_time3': '0_0_0_0_0_0',
                            'special1_time4': '0_0_0_0_0_0',
                            'special1_time5': '0_0_0_0_0_0',
                            'special1_time6': '0_0_0_0_0_0',
                            'special1_time7': '0_0_0_0_0_0',
                            'special1_time8': '0_0_0_0_0_0',
                            'special1_time9': '0_0_0_0_0_0',
                            'special2_month_time': '0_0_0',
                            'special2_time1': '0_0_0_0_0_0',
                            'special2_time2': '0_0_0_0_0_0',
                            'special2_time3': '0_0_0_0_0_0',
                            'special2_time4': '0_0_0_0_0_0',
                            'special2_time5': '0_0_0_0_0_0',
                            'special2_time6': '0_0_0_0_0_0',
                            'special2_time7': '0_0_0_0_0_0',
                            'special2_time8': '0_0_0_0_0_0',
                            'special2_time9': '0_0_0_0_0_0',
                            'syn_enable': None,
                            'sys_time': datetime.datetime(2022, 4, 12, 10, 11, 7),
                            'sys_time_text': datetime.datetime(2022, 4, 12, 10, 11, 7),
                            'time1_mode': 0,
                            'time2_mode': 0,
                            'time3_mode': 0,
                            'time4_mode': 0,
                            'time5_mode': 0,
                            'time6_mode': 0,
                            'time7_mode': 0,
                            'time8_mode': 0,
                            'time9_mode': 0,
                            'tlx_ac_discharge_frequency': None,
                            'tlx_ac_discharge_voltage': None,
                            'tlx_backflow_default_power': None,
                            'tlx_cc_current': None,
                            'tlx_cv_voltage': None,
                            'tlx_dry_contact_enable': None,
                            'tlx_dry_contact_off_power': None,
                            'tlx_dry_contact_power': None,
                            'tlx_exter_comm_off_griden': None,
                            'tlx_lcd_language': None,
                            'tlx_limit_device': None,
                            'tlx_off_grid_enable': None,
                            'tlx_on_off': None,
                            'tlx_pf': None,
                            'tlx_pflinep1_lp': None,
                            'tlx_pflinep1_pf': None,
                            'tlx_pflinep2_lp': None,
                            'tlx_pflinep2_pf': None,
                            'tlx_pflinep3_lp': None,
                            'tlx_pflinep3_pf': None,
                            'tlx_pflinep4_lp': None,
                            'tlx_pflinep4_pf': None,
                            'ub_ac_charging_stop_soc': None,
                            'ub_peak_shaving_backup_soc': None,
                            'us_battery_type': None,
                            'uw_ac_charging_max_power_limit': None,
                            'uw_demand_mgt_down_strm_power_limit': None,
                            'uw_demand_mgt_revse_power_limit': None,
                            'uw_hf_rt2_ee': 52.0,
                            'uw_hf_rt_ee': 51.20000076293945,
                            'uw_hv_rt2_ee': 288.0,
                            'uw_hv_rt_ee': 264.0,
                            'uw_lf_rt2_ee': 46.5,
                            'uw_lf_rt_ee': 48.5,
                            'uw_lv_rt2_ee': 120.0,
                            'uw_lv_rt_ee': 211.1999969482422,
                            'vbat_start_for_charge': 5800.0,
                            'vbat_start_for_discharge': 0.0,
                            'vbat_stop_for_charge': 0.0,
                            'vbat_stop_for_discharge': 0.0,
                            'vbat_warn_clr': 0.0,
                            'vbat_warning': 0,
                            'voltage_high_limit': 252.0,
                            'voltage_low_limit': 220.0,
                            'w_charge_soc_low_limit': None,
                            'w_discharge_soc_low_limit': 5.0,
                            'win_mode_end_time': None,
                            'win_mode_flag': None,
                            'win_mode_off_grid_discharge_stop_soc': None,
                            'win_mode_on_grid_discharge_stop_soc': None,
                            'win_mode_start_time': None,
                            'year_month_time': None,
                            'year_time1': '0_0_0_0_0_0_0',
                            'year_time2': '0_0_0_0_0_0_0',
                            'year_time3': '0_0_0_0_0_0_0',
                            'year_time4': '0_0_0_0_0_0_0',
                            'year_time5': '0_0_0_0_0_0_0',
                            'year_time6': '0_0_0_0_0_0_0',
                            'year_time7': '0_0_0_0_0_0_0',
                            'year_time8': '0_0_0_0_0_0_0',
                            'year_time9': '0_0_0_0_0_0_0'},
                'datalogger_sn': 'VC51030322020001',
                'device_sn': 'FDCJQ00003',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/tlx/tlx_set_info",
            params={
                "device_sn": device_sn,
            },
        )

        return MinSettings.model_validate(response)

    def setting_read(
        self,
        device_sn: str,
        parameter_id: Optional[str] = None,
        start_address: Optional[int] = None,
        end_address: Optional[int] = None,
    ) -> MinSettingRead:
        """
        Read Min setting parameter interface
        https://www.showdoc.com.cn/262556420217021/6119793934974232

        Note:
            Only applicable to devices with device type 7 (min) returned by device.list()

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
            device_sn (str): inverter SN
            parameter_id (Optional[str]): parameter ID - specify either parameter_id ort start/end_address
            start_address (Optional[int]): register address to start reading from - specify either parameter_id ort start/end_address
            end_address (Optional[int]): register address to stop reading at

        Returns:
            MinSettingRead
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
            endpoint="readMinParam",
            data={
                "device_sn": device_sn,
                "paramId": parameter_id,
                "startAddr": start_address,
                "endAddr": end_address,
            },
        )

        return MinSettingRead.model_validate(response)

    # noinspection PyUnusedLocal
    def setting_write(
        self,
        device_sn: str,
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
    ) -> MinSettingWrite:
        """
        Min parameter setting
        Min parameter setting interface
        https://www.showdoc.com.cn/262556420217021/6129826876191828

        Note:
            Only applicable to devices with device type 7 (min) returned by device.list()

        This method allows to set
        * predefined settings (see table below)
          * use parameter_id=<string defined below>
          * number of parameter_value_* maps to the setting number from the table below
        * any register value (see table below for most relevant settings, google for "Growatt Inverter Modbus RTU Protocol V1.20" for more)
          * use parameter_id="set_any_reg"
          * parameter_value_1 is the register number to set
          * parameter_value_2 is the value to set (decimal)
          * parameter_value_3~19 must not be set

        Predefined settings
        ========================+=======================================+===========================+============================================================================
        description             | parameter_id                          | parameter_value_[n]       | comment
        ========================+=======================================+===========================+============================================================================
        Backflow prevention     | backflow_setting                      | [1]: 0 ~ 2                | 0 = disable, 1 = enable the meter, 2 = enable CT
         setting item           |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set switch machine      | tlx_on_off                            | [1]: 0000 or 0001         | 0000 = shut down, 0001 = switch on
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set time                | pf_sys_year                           | [1]: YYYY-MM-DD hh:mm:ss  | 0 = enable, 1 = disable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set upper limit of      | pv_grid_voltage_high                  | [1]: 270                  |
         mains voltage          |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set lower limit of      | pv_grid_voltage_low                   | [1]: 180                  |
         mains voltage          |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set off-grid enable     | tlx_off_grid_enable                   | [1]: 0 or 1               | 0 = prohibited, 1 = enable/yes
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set off-grid frequency  | tlx_ac_discharge_frequency            | [1]: 0 or 1               | 0 = 50 Hz, 1 = 60 Hz
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set off-grid voltage    | tlx_ac_discharge_voltage              | [1]: 0 ~ 2                | 0 = 230 V, 1 = 208 V, 2 = 240 V
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set active power        | pv_active_p_rate                      | [1]: 0 ~ 100              |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set none Power          | pv_reactive_p_rate                    | [1]: 0 ~ 100              |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set PF value            | pv_power_factor                       | [1]: -0.8 ~ -1            |
                                |                                       |    or 0.8 ~  1            |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Charging power          | charge_power                          | [1]: 0 ~ 100              | charging power
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Charge stop SOC         | charge_stop_soc                       | [1]: 0 ~ 100              | charging stop SOC
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Discharge power         | discharge_power                       | [1]: 0 ~ 100              | discharging power
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Discharge stop SOC      | discharge_stop_soc                    | [1]: 0 ~ 100              | discharging stop SOC
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Mains charging          | ac_charge                             | [1]: 0 or 1               | Mains enable: 0 = disable, 1 = enable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Time period 1           | time_segment1                         | [1]: 0 ~ 2                | [1]: Mode: 0 = load priority, 1 = battery priority, 2 = grid priority
                                |                                       | [2]: Time: 0 ~ 23         | [2]: start hour
                                |                                       | [3]: Time: 0 ~ 59         | [3]: start minute
                                |                                       | [4]: Time: 0 ~ 23         | [4]: end hour
                                |                                       | [5]: Time: 0 ~ 59         | [5]: end hour
                                |                                       | [6]: 0 or 1               | [6]: 0 = disable, 1 = enable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Time period 2 ~ 9       | time_segment2 ~ time_segment9         | see Time period 1         | see Time period 1
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------

        Register settings
        ========================+=======================================+===========================+============================================================================
        description             | parameter_id                          | parameter_value_[n]       | comment
        ========================+=======================================+===========================+============================================================================
        Remote On/Off           | set_any_reg                           | [1]: 0                    | [1]: register 1 is "OnOff"
                                |                                       | [2]: 0 or 1               | [2]: 0 = Off, 1 = On
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        ...                     | set_any_reg                           | [1]: 1 ~ 5000             | [1]: register no - google for "Growatt Inverter Modbus RTU Protocol V1.20"
                                |                                       | [2]: 0 ~ 65535            | [2]: allowed values are specific for each register setting
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------

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
            parameter_value_1 (Union[str, int]): parameter value 1 // register number when using "set_any_reg"
            parameter_value_2 (Optional[Union[str, int]]): parameter value 2 // register value to set when using "set_any_reg"
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
        parameters: Dict[int, Any] = {}
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
            endpoint="tlxSet",
            data={
                "tlx_sn": device_sn,
                "type": parameter_id,
                **{f"param{i}": parameters[i] for i in range(1, 20)},
            },
        )

        return MinSettingWrite.model_validate(response)

    def details(
        self,
        device_sn: str,
    ) -> MinDetails:
        """
        Get Min basic information
        Interface to get basic information of Min
        https://www.showdoc.com.cn/262556420217021/6129816412127075

        Note:
            Only applicable to devices with device type 7 (min) returned by device.list()

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Args:
            device_sn (str): TLX device SN

        Returns:
            MinDetails
            {   'data': {   'address': 1,
                            'alias': 'FDCJQ00003',
                            'bat_aging_test_step': 0,
                            'bat_parallel_num': 0,
                            'bat_series_num': 0,
                            'bat_sys_energy': None,
                            'bat_temp_lower_limit_c': 0,
                            'bat_temp_lower_limit_d': 0,
                            'bat_temp_upper_limit_c': 0,
                            'bat_temp_upper_limit_d': 0,
                            'battery_type': 0,
                            'baudrate': 0.0,
                            'bct_adjust': 0,
                            'bct_mode': 0.0,
                            'bcu_version': None,
                            'bdc1_model': '0',
                            'bdc1_sn': 'XXXXXXXXXXXXXXXX',
                            'bdc1_version': ' -0',
                            'bdc_auth_version': 0,
                            'bdc_mode': -1,
                            'bms_communication_type': 0,
                            'bms_software_version': '0',
                            'children': [],
                            'com_address': 1,
                            'communication_version': 'ZAca-0017',
                            'country_selected': 0,
                            'datalogger_sn': 'VC51030322020001',
                            'device_type': 2,
                            'dtc': 5300,
                            'e_today': 0.0,
                            'e_total': 0.0,
                            'energy_day_map': {},
                            'energy_month': 0.0,
                            'energy_month_text': 0.0,
                            'fw_version': 'xx1.0',
                            'group_id': -1,
                            'hw_version': None,
                            'id': 0,
                            'img_path': './css/img/status_gray.gif',
                            'inner_version': 'xxxxxxxx',
                            'last_update_time': {'date': 12, 'day': 2, 'hours': 16, 'minutes': 46, 'month': 3, 'seconds': 22, 'time': 1649753182000, 'timezone_offset': -480, 'year': 122},
                            'last_update_time_text': datetime.datetime(2022, 4, 12, 16, 46, 22),
                            'level': 4,
                            'li_battery_fw_version': 0,
                            'li_battery_manufacturers': 0,
                            'location': None,
                            'lost': False,
                            'manufacturer': 'PV Inverter',
                            'modbus_version': 305,
                            'model': 2666130979655057522,
                            'model_text': 'S25B00D00T00P0FU01M0072',
                            'monitor_version': None,
                            'mppt': 513.0,
                            'optimizer_list': [],
                            'p_charge': 0.0,
                            'p_discharge': 0.0,
                            'parent_id': 'LIST_VC51030322020001_22',
                            'plant_Id': 0,
                            'plantname': None,
                            'pmax': 11400,
                            'port_name': 'port_name',
                            'power': 0.0,
                            'power_max': None,
                            'power_max_text': None,
                            'power_max_time': None,
                            'priority_choose': 0,
                            'record': None,
                            'restart_time': 300,
                            'safety_version': None,
                            'serial_num': 'FDCJQ00003',
                            'start_time': 300,
                            'status': 0,
                            'status_text': 'tlx.status.operating',
                            'str_num': 0,
                            'sys_time': None,
                            'tcp_server_ip': '47.107.154.111',
                            'timezone': 8,
                            'tlx_set_bean': {   'ac_charge': None,
                                                'ac_charge_enable': False,
                                                'active_power_enable': False,
                                                'active_rate': 100.0,
                                                'afci_enabled': -1,
                                                'afci_reset': -1,
                                                'afci_self_check': -1,
                                                'afci_threshold_d': -1.0,
                                                'afci_threshold_h': -1.0,
                                                'afci_threshold_l': -1.0,
                                                'backflow_default_power': 0.0,
                                                'backflow_single_ctrl': None,
                                                'bdc_mode': -1,
                                                'bgrid_type': 0,
                                                'bsystem_work_mode': 500.0,
                                                'charge_power': None,
                                                'charge_power_command': 100.0,
                                                'charge_stop_soc': None,
                                                'compatible_flag': None,
                                                'delay_time': 0,
                                                'demand_manage_enable': None,
                                                'discharge_power': None,
                                                'discharge_power_command': 100.0,
                                                'discharge_stop_soc': None,
                                                'dry_contact_func_en': 0.0,
                                                'dry_contact_off_rate': 40.0,
                                                'dry_contact_on_rate': 40.0,
                                                'dry_contact_power': 50.0,
                                                'enable_n_line': None,
                                                'eps_freq_set': 0.0,
                                                'eps_fun_en': 1.0,
                                                'eps_volt_set': 2.0,
                                                'export_limit': 0.0,
                                                'export_limit_power_rate': 0.0,
                                                'export_limit_power_rate_str': None,
                                                'exter_comm_off_grid_en': 0,
                                                'fail_safe_curr': None,
                                                'fft_threshold_count': -1,
                                                'float_charge_current_limit': 600.0,
                                                'forced_stop_switch1': 0,
                                                'forced_stop_switch2': 0,
                                                'forced_stop_switch3': 0,
                                                'forced_stop_switch4': 0,
                                                'forced_stop_switch5': 0,
                                                'forced_stop_switch6': 0,
                                                'forced_stop_switch7': 0,
                                                'forced_stop_switch8': 0,
                                                'forced_stop_switch9': 0,
                                                'forced_time_start1': datetime.time(0, 0),
                                                'forced_time_start2': datetime.time(0, 0),
                                                'forced_time_start3': datetime.time(0, 0),
                                                'forced_time_start4': datetime.time(0, 0),
                                                'forced_time_start5': datetime.time(0, 0),
                                                'forced_time_start6': datetime.time(0, 0),
                                                'forced_time_start7': datetime.time(0, 0),
                                                'forced_time_start8': datetime.time(0, 0),
                                                'forced_time_start9': datetime.time(0, 0),
                                                'forced_time_stop1': datetime.time(0, 0),
                                                'forced_time_stop2': datetime.time(0, 0),
                                                'forced_time_stop3': datetime.time(0, 0),
                                                'forced_time_stop4': datetime.time(0, 0),
                                                'forced_time_stop5': datetime.time(0, 0),
                                                'forced_time_stop6': datetime.time(0, 0),
                                                'forced_time_stop7': datetime.time(0, 0),
                                                'forced_time_stop8': datetime.time(0, 0),
                                                'forced_time_stop9': datetime.time(0, 0),
                                                'frequency_high_limit': 50.099998474121094,
                                                'frequency_low_limit': 49.5,
                                                'gen_charge_enable': None,
                                                'gen_ctrl': None,
                                                'gen_rated_power': None,
                                                'last_update_time': {'date': 12, 'day': 2, 'hours': 16, 'minutes': 39, 'month': 3, 'seconds': 23, 'time': 1649752763000, 'timezone_offset': -480, 'year': 122},
                                                'last_update_time_text': datetime.datetime(2022, 4, 12, 16, 39, 23),
                                                'lcd_language': 1,
                                                'limit_device': -1.0,
                                                'loading_rate': 20.0,
                                                'maintain_mode_request': None,
                                                'maintain_mode_start_time': None,
                                                'max_allow_curr': None,
                                                'on_grid_discharge_stop_soc': None,
                                                'on_grid_mode': None,
                                                'on_grid_status': None,
                                                'on_off': 1,
                                                'over_fre_drop_point': 50.029998779296875,
                                                'over_fre_lo_red_delay_time': 0.0,
                                                'over_fre_lo_red_slope': 41.0,
                                                'peak_shaving_enable': None,
                                                'pf': 0.8899999856948853,
                                                'pf_model': 0.0,
                                                'pf_sys_year': None,
                                                'pflinep1_lp': 255.0,
                                                'pflinep1_pf': 1.0,
                                                'pflinep2_lp': 255.0,
                                                'pflinep2_pf': 1.0,
                                                'pflinep3_lp': 255.0,
                                                'pflinep3_pf': 1.0,
                                                'pflinep4_lp': 255.0,
                                                'pflinep4_pf': 1.0,
                                                'power_down_enable': None,
                                                'pre_pto': None,
                                                'prot_enable': None,
                                                'pu_enable': None,
                                                'pv_grid_frequency_high': None,
                                                'pv_grid_frequency_low': None,
                                                'pv_grid_voltage_high': None,
                                                'pv_grid_voltage_low': None,
                                                'pv_pf_cmd_memory_state': 0,
                                                'q_percent_max': 44.0,
                                                'qv_h1': 247.1999969482422,
                                                'qv_h2': 256.79998779296875,
                                                'qv_l1': 232.0,
                                                'qv_l2': 220.8000030517578,
                                                'reactive_rate': 0.0,
                                                'region': None,
                                                'restart_loading_rate': 20.0,
                                                'rrcr_enable': None,
                                                'safety_correspond_num': None,
                                                'safety_num': None,
                                                'season1_month_time': '0_0_0',
                                                'season1_time1': '0_0_0_0_0_0_0',
                                                'season1_time2': '0_0_0_0_0_0_0',
                                                'season1_time3': '0_0_0_0_0_0_0',
                                                'season1_time4': '0_0_0_0_0_0_0',
                                                'season1_time5': '0_0_0_0_0_0_0',
                                                'season1_time6': '0_0_0_0_0_0_0',
                                                'season1_time7': '0_0_0_0_0_0_0',
                                                'season1_time8': '0_0_0_0_0_0_0',
                                                'season1_time9': '0_0_0_0_0_0_0',
                                                'season2_month_time': '0_0_0',
                                                'season2_time1': '0_0_0_0_0_0_0',
                                                'season2_time2': '0_0_0_0_0_0_0',
                                                'season2_time3': '0_0_0_0_0_0_0',
                                                'season2_time4': '0_0_0_0_0_0_0',
                                                'season2_time5': '0_0_0_0_0_0_0',
                                                'season2_time6': '0_0_0_0_0_0_0',
                                                'season2_time7': '0_0_0_0_0_0_0',
                                                'season2_time8': '0_0_0_0_0_0_0',
                                                'season2_time9': '0_0_0_0_0_0_0',
                                                'season3_month_time': '0_0_0',
                                                'season3_time1': '0_0_0_0_0_0_0',
                                                'season3_time2': '0_0_0_0_0_0_0',
                                                'season3_time3': '0_0_0_0_0_0_0',
                                                'season3_time4': '0_0_0_0_0_0_0',
                                                'season3_time5': '0_0_0_0_0_0_0',
                                                'season3_time6': '0_0_0_0_0_0_0',
                                                'season3_time7': '0_0_0_0_0_0_0',
                                                'season3_time8': '0_0_0_0_0_0_0',
                                                'season3_time9': '0_0_0_0_0_0_0',
                                                'season4_month_time': '0_0_0',
                                                'season4_time1': '0_0_0_0_0_0_0',
                                                'season4_time2': '0_0_0_0_0_0_0',
                                                'season4_time3': '0_0_0_0_0_0_0',
                                                'season4_time4': '0_0_0_0_0_0_0',
                                                'season4_time5': '0_0_0_0_0_0_0',
                                                'season4_time6': '0_0_0_0_0_0_0',
                                                'season4_time7': '0_0_0_0_0_0_0',
                                                'season4_time8': '0_0_0_0_0_0_0',
                                                'season4_time9': '0_0_0_0_0_0_0',
                                                'serial_num': 'FDCJQ00003',
                                                'show_peak_shaving': None,
                                                'special1_month_time': '0_0_0',
                                                'special1_time1': '0_0_0_0_0_0',
                                                'special1_time2': '0_0_0_0_0_0',
                                                'special1_time3': '0_0_0_0_0_0',
                                                'special1_time4': '0_0_0_0_0_0',
                                                'special1_time5': '0_0_0_0_0_0',
                                                'special1_time6': '0_0_0_0_0_0',
                                                'special1_time7': '0_0_0_0_0_0',
                                                'special1_time8': '0_0_0_0_0_0',
                                                'special1_time9': '0_0_0_0_0_0',
                                                'special2_month_time': '0_0_0',
                                                'special2_time1': '0_0_0_0_0_0',
                                                'special2_time2': '0_0_0_0_0_0',
                                                'special2_time3': '0_0_0_0_0_0',
                                                'special2_time4': '0_0_0_0_0_0',
                                                'special2_time5': '0_0_0_0_0_0',
                                                'special2_time6': '0_0_0_0_0_0',
                                                'special2_time7': '0_0_0_0_0_0',
                                                'special2_time8': '0_0_0_0_0_0',
                                                'special2_time9': '0_0_0_0_0_0',
                                                'syn_enable': None,
                                                'sys_time': datetime.datetime(2022, 4, 12, 16, 39, 21),
                                                'sys_time_text': datetime.datetime(2022, 4, 12, 16, 39, 21),
                                                'time1_mode': 0,
                                                'time2_mode': 0,
                                                'time3_mode': 0,
                                                'time4_mode': 0,
                                                'time5_mode': 0,
                                                'time6_mode': 0,
                                                'time7_mode': 0,
                                                'time8_mode': 0,
                                                'time9_mode': 0,
                                                'tlx_ac_discharge_frequency': None,
                                                'tlx_ac_discharge_voltage': None,
                                                'tlx_backflow_default_power': None,
                                                'tlx_cc_current': None,
                                                'tlx_cv_voltage': None,
                                                'tlx_dry_contact_enable': None,
                                                'tlx_dry_contact_off_power': None,
                                                'tlx_dry_contact_power': None,
                                                'tlx_exter_comm_off_griden': None,
                                                'tlx_lcd_language': None,
                                                'tlx_limit_device': None,
                                                'tlx_off_grid_enable': None,
                                                'tlx_on_off': None,
                                                'tlx_pf': None,
                                                'tlx_pflinep1_lp': None,
                                                'tlx_pflinep1_pf': None,
                                                'tlx_pflinep2_lp': None,
                                                'tlx_pflinep2_pf': None,
                                                'tlx_pflinep3_lp': None,
                                                'tlx_pflinep3_pf': None,
                                                'tlx_pflinep4_lp': None,
                                                'tlx_pflinep4_pf': None,
                                                'ub_ac_charging_stop_soc': None,
                                                'ub_peak_shaving_backup_soc': None,
                                                'us_battery_type': None,
                                                'uw_ac_charging_max_power_limit': None,
                                                'uw_demand_mgt_down_strm_power_limit': None,
                                                'uw_demand_mgt_revse_power_limit': None,
                                                'uw_hf_rt2_ee': 52.0,
                                                'uw_hf_rt_ee': 51.20000076293945,
                                                'uw_hv_rt2_ee': 288.0,
                                                'uw_hv_rt_ee': 264.0,
                                                'uw_lf_rt2_ee': 46.5,
                                                'uw_lf_rt_ee': 48.5,
                                                'uw_lv_rt2_ee': 120.0,
                                                'uw_lv_rt_ee': 211.1999969482422,
                                                'vbat_start_for_charge': 5800.0,
                                                'vbat_start_for_discharge': 0.0,
                                                'vbat_stop_for_charge': 0.0,
                                                'vbat_stop_for_discharge': 0.0,
                                                'vbat_warn_clr': 0.0,
                                                'vbat_warning': 0,
                                                'voltage_high_limit': 252.0,
                                                'voltage_low_limit': 220.0,
                                                'w_charge_soc_low_limit': None,
                                                'w_discharge_soc_low_limit': 5.0,
                                                'win_mode_end_time': None,
                                                'win_mode_flag': None,
                                                'win_mode_off_grid_discharge_stop_soc': None,
                                                'win_mode_on_grid_discharge_stop_soc': None,
                                                'win_mode_start_time': None,
                                                'year_month_time': None,
                                                'year_time1': None,
                                                'year_time2': None,
                                                'year_time3': None,
                                                'year_time4': None,
                                                'year_time5': None,
                                                'year_time6': None,
                                                'year_time7': None,
                                                'year_time8': None,
                                                'year_time9': None},
                            'tracker_model': 0,
                            'tree_id': 'ST_FDCJQ00003',
                            'tree_name': 'FDCJQ00003',
                            'updating': False,
                            'user_name': None,
                            'vbat_start_for_discharge': 0,
                            'vbat_stop_for_charge': 0,
                            'vbat_stop_for_discharge': 0,
                            'vbat_warn_clr': 0,
                            'vbat_warning': 0,
                            'vnormal': 800.0,
                            'vpp_open': None},
                'datalogger_sn': 'VC51030322020001',
                'device_sn': 'FDCJQ00003',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/tlx/tlx_data_info",
            params={
                "device_sn": device_sn,
            },
        )

        return MinDetails.model_validate(response)

    def energy(
        self,
        device_sn: str,
    ) -> MinEnergyOverview:
        """
        Get the latest real-time data of Min
        Interface to get the latest real-time data of Min
        https://www.showdoc.com.cn/262556420217021/6129822090975531

        Note:
            Only applicable to devices with device type 7 (min) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Min does not exist
        * 10003: Device SN error

        Args:
            device_sn (str): Inverter serial number

        Returns:
            StorageEnergyOverview
            e.g.
            {   'data': {   'address': 0,
                            'again': False,
                            'alias': None,
                            'b_merter_connect_flag': None,
                            'bat_sn': None,
                            'battery_no': 0,
                            'battery_sn': None,
                            'bdc1_charge_power': 0.0,
                            'bdc1_charge_total': 0.0,
                            'bdc1_discharge_power': 0.0,
                            'bdc1_discharge_total': 0.0,
                            'bdc1_fault_type': 0,
                            'bdc1_ibat': 0.0,
                            'bdc1_ibb': 0.0,
                            'bdc1_illc': 0.0,
                            'bdc1_mode': 0,
                            'bdc1_soc': 0.0,
                            'bdc1_status': 0,
                            'bdc1_temp1': 0.0,
                            'bdc1_temp2': 0.0,
                            'bdc1_vbat': 0.0,
                            'bdc1_vbus1': 0.0,
                            'bdc1_vbus2': 0.0,
                            'bdc1_warn_code': 0,
                            'bdc2_charge_power': 0.0,
                            'bdc2_charge_total': 0.0,
                            'bdc2_discharge_power': 0.0,
                            'bdc2_discharge_total': 0.0,
                            'bdc2_fault_type': 0,
                            'bdc2_ibat': 0.0,
                            'bdc2_ibb': 0.0,
                            'bdc2_illc': 0.0,
                            'bdc2_mode': 0,
                            'bdc2_soc': 0.0,
                            'bdc2_status': 0,
                            'bdc2_temp1': 0.0,
                            'bdc2_temp2': 0.0,
                            'bdc2_vbat': 0.0,
                            'bdc2_vbus1': 0.0,
                            'bdc2_vbus2': 0.0,
                            'bdc2_warn_code': 0,
                            'bdc_bus_ref': 0,
                            'bdc_derate_reason': 0,
                            'bdc_fault_sub_code': 0,
                            'bdc_status': 0,
                            'bdc_vbus2_neg': 0.0,
                            'bdc_warn_sub_code': 0,
                            'bgrid_type': 0,
                            'bms_communication_type': 0,
                            'bms_cv_volt': 0.0,
                            'bms_error2': 0,
                            'bms_error3': 0,
                            'bms_error4': 0,
                            'bms_fault_type': 0,
                            'bms_fw_version': '0',
                            'bms_ibat': 0.0,
                            'bms_icycle': 0.0,
                            'bms_info': 0,
                            'bms_ios_status': 0,
                            'bms_max_curr': 0.0,
                            'bms_mcu_version': '0',
                            'bms_pack_info': 0,
                            'bms_soc': 0.0,
                            'bms_soh': 0.0,
                            'bms_status': 0,
                            'bms_temp1_bat': 0.0,
                            'bms_using_cap': 0,
                            'bms_vbat': 0.0,
                            'bms_vdelta': 0.0,
                            'bms_warn2': 0,
                            'bms_warn_code': 0.0,
                            'bsystem_work_mode': 0,
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 9, 'day': 6, 'hours': 14, 'minutes': 52, 'month': 3, 'seconds': 39, 'time': 1649487159000, 'timezone_offset': -480, 'year': 122},
                                            'time_in_millis': 1649487159000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2022,
                                            'weeks_in_week_year': 53},
                            'datalogger_sn': None,
                            'day': None,
                            'dc_voltage': 0.0,
                            'dci_r': 12.0,
                            'dci_s': 0.0,
                            'dci_t': 0.0,
                            'debug1': '160, 0, 0, 0, 324, 0, 0, 0',
                            'debug2': '0,0,0,0,0,0,0,0',
                            'derating_mode': 0,
                            'dry_contact_status': 0,
                            'e_charge_today': 0.0,
                            'e_charge_total': 0.0,
                            'e_discharge_today': 0.0,
                            'e_discharge_total': 0.0,
                            'e_local_load_today': 0.0,
                            'e_local_load_total': 0.0,
                            'e_self_today': 0.0,
                            'e_self_total': 0.0,
                            'e_system_today': 0.0,
                            'e_system_total': 0.0,
                            'e_to_grid_today': 0.0,
                            'e_to_grid_total': 0.0,
                            'e_to_user_today': 0.0,
                            'e_to_user_total': 0.0,
                            'eac_charge_today': 0.0,
                            'eac_charge_total': 0.0,
                            'eac_today': 21.600000381469727,
                            'eac_total': 1859.5,
                            'eex1_today': -0.1,
                            'eex1_total': -0.1,
                            'eex2_today': -0.1,
                            'eex2_total': -0.1,
                            'eps_fac': 0.0,
                            'eps_iac1': 0.0,
                            'eps_iac2': 0.0,
                            'eps_iac3': 0.0,
                            'eps_pac': 0.0,
                            'eps_pac1': 0.0,
                            'eps_pac2': 0.0,
                            'eps_pac3': 0.0,
                            'eps_pf': -1.0,
                            'eps_vac1': 0.0,
                            'eps_vac2': 0.0,
                            'eps_vac3': 0.0,
                            'epv1_today': 13.199999809265137,
                            'epv1_total': 926.6,
                            'epv2_today': 8.199999809265137,
                            'epv2_total': 906.4,
                            'epv3_today': 0.0,
                            'epv3_total': 0.0,
                            'epv4_today': 0.0,
                            'epv4_total': 0.0,
                            'epv_total': 1833.0,
                            'error_text': 'Unknown',
                            'fac': 50.0099983215332,
                            'fault_type': 0,
                            'fault_type1': None,
                            'gfci': 78.0,
                            'iac1': 10.699999809265137,
                            'iac2': 0.0,
                            'iac3': 0.0,
                            'iacr': 0.0,
                            'inv_delay_time': 0.0,
                            'ipv1': 5.800000190734863,
                            'ipv2': 6.099999904632568,
                            'ipv3': 0.0,
                            'ipv4': 0.0,
                            'is_again': False,
                            'iso': 3135.0,
                            'load_percent': 0.0,
                            'lost': True,
                            'mtnc_mode': None,
                            'mtnc_rqst': None,
                            'n_bus_voltage': 0.0,
                            'new_warn_code': None,
                            'new_warn_sub_code': None,
                            'op_fullwatt': 0.0,
                            'operating_mode': 0,
                            'p_bus_voltage': 367.0,
                            'p_self': 0.0,
                            'p_system': 0.0,
                            'pac': 2503.8,
                            'pac1': 2530.699951171875,
                            'pac2': 0.0,
                            'pac3': 0.0,
                            'pac_to_grid_total': 0.0,
                            'pac_to_local_load': 0.0,
                            'pac_to_user_total': 0.0,
                            'pacr': 0.0,
                            'pex1': -0.1,
                            'pex2': -0.1,
                            'pf': 1.0,
                            'ppv': 2558.7,
                            'ppv1': 1500.7,
                            'ppv2': 1058.0,
                            'ppv3': 0.0,
                            'ppv4': 0.0,
                            'real_op_percent': 50.0,
                            'serial_num': 'BNE9A5100D',
                            'soc1': None,
                            'soc2': None,
                            'status': 1,
                            'status_text': 'Normal',
                            'sys_fault_word': 0,
                            'sys_fault_word1': 0,
                            'sys_fault_word2': 0,
                            'sys_fault_word3': 0,
                            'sys_fault_word4': 0,
                            'sys_fault_word5': 0,
                            'sys_fault_word6': 0,
                            'sys_fault_word7': 0,
                            't_mtnc_strt': None,
                            't_win_end': None,
                            't_win_start': None,
                            'temp1': 47.79999923706055,
                            'temp2': 0.0,
                            'temp3': 0.0,
                            'temp4': 0.0,
                            'temp5': 51.70000076293945,
                            'time': datetime.datetime(2022, 4, 9, 14, 52, 39),
                            'time_total': 1625146.9,
                            'tlx_bean': None,
                            'total_working_time': None,
                            'uw_sys_work_mode': 0,
                            'vac1': 239.5,
                            'vac2': 0.0,
                            'vac3': 0.0,
                            'vac_rs': 239.5,
                            'vac_st': 0.0,
                            'vac_tr': 0.0,
                            'vacr': 0.0,
                            'vacrs': 0.0,
                            'vpv1': 258.6000061035156,
                            'vpv2': 168.0,
                            'vpv3': 0.0,
                            'vpv4': 0.0,
                            'warn_code': 0,
                            'warn_code1': None,
                            'warn_text': 'Unknown',
                            'win_mode': None,
                            'win_off_grid_soc': None,
                            'win_on_grid_soc': None,
                            'win_request': None,
                            'with_time': False},
                'datalogger_sn': 'LTH0BFD08J',
                'device_sn': 'BNE9A5100D',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/tlx/tlx_last_data",
            data={
                "tlx_sn": device_sn,
            },
        )

        return MinEnergyOverview.model_validate(response)

    def energy_multiple(
        self,
        device_sn: Union[str, List[str]],
        page: Optional[int] = None,
    ) -> MinEnergyOverviewMultiple:
        """
        Get the latest real-time data of min in batches
        Interface to obtain the latest real-time data of inverters in batches
        https://www.showdoc.com.cn/262556420217021/6129830403882881

        Note:
            Only applicable to devices with device type 7 (min) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: Min does not exist
        * 10003: device SN error

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)
            page (Optional[int]): page number, default 1, max 2

        Returns:
            MinEnergyOverviewMultiple
            {   'data': [   {   'datalogger_sn': 'XGD4A371YB',
                                'device_sn': 'HMG2A3807H',
                                'data': {   'address': 0,
                                            'again': False,
                                            'alias': None,
                                            'b_merter_connect_flag': None,
                                            'bat_sn': None,
                                            'battery_no': None,
                                            'battery_sn': None,
                                            'bdc1_charge_power': 0.0,
                                            'bdc1_charge_total': 0.0,
                                            'bdc1_discharge_power': 0.0,
                                            'bdc1_discharge_total': 0.0,
                                            'bdc1_fault_type': 0,
                                            'bdc1_ibat': 0.0,
                                            'bdc1_ibb': 0.0,
                                            'bdc1_illc': 0.0,
                                            'bdc1_mode': 0,
                                            'bdc1_soc': 0.0,
                                            'bdc1_status': 0,
                                            'bdc1_temp1': 0.0,
                                            'bdc1_temp2': 0.0,
                                            'bdc1_vbat': 0.0,
                                            'bdc1_vbus1': 0.0,
                                            'bdc1_vbus2': 0.0,
                                            'bdc1_warn_code': 0,
                                            'bdc2_charge_power': 0.0,
                                            'bdc2_charge_total': 0.0,
                                            'bdc2_discharge_power': 0.0,
                                            'bdc2_discharge_total': 0.0,
                                            'bdc2_fault_type': 0,
                                            'bdc2_ibat': 0.0,
                                            'bdc2_ibb': 0.0,
                                            'bdc2_illc': 0.0,
                                            'bdc2_mode': 0,
                                            'bdc2_soc': 0.0,
                                            'bdc2_status': 0,
                                            'bdc2_temp1': 0.0,
                                            'bdc2_temp2': 0.0,
                                            'bdc2_vbat': 0.0,
                                            'bdc2_vbus1': 0.0,
                                            'bdc2_vbus2': 0.0,
                                            'bdc2_warn_code': 0,
                                            'bdc_bus_ref': 0,
                                            'bdc_derate_reason': 0,
                                            'bdc_fault_sub_code': 0,
                                            'bdc_status': 0,
                                            'bdc_vbus2_neg': 0.0,
                                            'bdc_warn_sub_code': 0,
                                            'bgrid_type': None,
                                            'bms_communication_type': 0,
                                            'bms_cv_volt': 0.0,
                                            'bms_error2': 0,
                                            'bms_error3': 0,
                                            'bms_error4': None,
                                            'bms_fault_type': 0,
                                            'bms_fw_version': '0',
                                            'bms_ibat': 0.0,
                                            'bms_icycle': 0.0,
                                            'bms_info': 0,
                                            'bms_ios_status': None,
                                            'bms_max_curr': 0.0,
                                            'bms_mcu_version': '0',
                                            'bms_pack_info': 0,
                                            'bms_soc': 0.0,
                                            'bms_soh': 0.0,
                                            'bms_status': 0,
                                            'bms_temp1_bat': 0.0,
                                            'bms_using_cap': 0,
                                            'bms_vbat': 0.0,
                                            'bms_vdelta': 0.0,
                                            'bms_warn2': 0,
                                            'bms_warn_code': 0.0,
                                            'bsystem_work_mode': None,
                                            'calendar': {   'first_day_of_week': 1,
                                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                            'lenient': True,
                                                            'minimal_days_in_first_week': 1,
                                                            'time': {'date': 7, 'day': 4, 'hours': 19, 'minutes': 29, 'month': 0, 'seconds': 10, 'time': 1610018950000, 'timezone_offset': -480, 'year': 121},
                                                            'time_in_millis': 1610018950000,
                                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                            'week_date_supported': True,
                                                            'week_year': 2021,
                                                            'weeks_in_week_year': 52},
                                            'datalogger_sn': None,
                                            'day': None,
                                            'dc_voltage': 0.0,
                                            'dci_r': 6.0,
                                            'dci_s': 0.0,
                                            'dci_t': 0.0,
                                            'debug1': '208, 15, 1, 2595, 2235, 3600, 0, 0',
                                            'debug2': '0, 106, 165, 0, 0, 0, 7, 0',
                                            'derating_mode': 15,
                                            'dry_contact_status': 0,
                                            'e_charge_today': 0.0,
                                            'e_charge_total': 0.0,
                                            'e_discharge_today': 0.0,
                                            'e_discharge_total': 0.0,
                                            'e_local_load_today': 0.0,
                                            'e_local_load_total': 0.0,
                                            'e_self_today': 0.0,
                                            'e_self_total': 0.0,
                                            'e_system_today': 0.0,
                                            'e_system_total': 0.0,
                                            'e_to_grid_today': 0.0,
                                            'e_to_grid_total': 0.0,
                                            'e_to_user_today': 0.0,
                                            'e_to_user_total': 0.0,
                                            'eac_charge_today': 0.0,
                                            'eac_charge_total': 0.0,
                                            'eac_today': 41.900001525878906,
                                            'eac_total': 668.4,
                                            'eex1_today': None,
                                            'eex1_total': None,
                                            'eex2_today': None,
                                            'eex2_total': None,
                                            'eps_fac': 0.0,
                                            'eps_iac1': 0.0,
                                            'eps_iac2': 0.0,
                                            'eps_iac3': 0.0,
                                            'eps_pac': 0.0,
                                            'eps_pac1': 0.0,
                                            'eps_pac2': 0.0,
                                            'eps_pac3': 0.0,
                                            'eps_pf': -1.0,
                                            'eps_vac1': 0.0,
                                            'eps_vac2': 0.0,
                                            'eps_vac3': 0.0,
                                            'epv1_today': 22.899999618530273,
                                            'epv1_total': 367.9,
                                            'epv2_today': 20.100000381469727,
                                            'epv2_total': 318.5,
                                            'epv3_today': 0.0,
                                            'epv3_total': 0.0,
                                            'epv4_today': None,
                                            'epv4_total': None,
                                            'epv_total': 686.4,
                                            'error_text': 'Unknown',
                                            'fac': 50.0099983215332,
                                            'fault_type': 0,
                                            'fault_type1': None,
                                            'gfci': 68.0,
                                            'iac1': 0.30000001192092896,
                                            'iac2': 0.0,
                                            'iac3': 0.0,
                                            'iacr': 0.0,
                                            'inv_delay_time': 0.0,
                                            'ipv1': 0.0,
                                            'ipv2': 0.0,
                                            'ipv3': 0.0,
                                            'ipv4': 0.0,
                                            'is_again': False,
                                            'iso': 23182.0,
                                            'load_percent': 0.0,
                                            'lost': True,
                                            'mtnc_mode': None,
                                            'mtnc_rqst': None,
                                            'n_bus_voltage': 0.0,
                                            'new_warn_code': None,
                                            'new_warn_sub_code': None,
                                            'op_fullwatt': 0.0,
                                            'operating_mode': 0,
                                            'p_bus_voltage': 358.29998779296875,
                                            'p_self': 0.0,
                                            'p_system': 0.0,
                                            'pac': 1.2,
                                            'pac1': 3.0999999046325684,
                                            'pac2': 0.0,
                                            'pac3': 0.0,
                                            'pac_to_grid_total': 0.0,
                                            'pac_to_local_load': 0.0,
                                            'pac_to_user_total': 0.0,
                                            'pacr': 0.0,
                                            'pex1': None,
                                            'pex2': None,
                                            'pf': 1.0,
                                            'ppv': 1.4,
                                            'ppv1': 1.0,
                                            'ppv2': 0.4,
                                            'ppv3': 0.0,
                                            'ppv4': 0.0,
                                            'real_op_percent': 0.0,
                                            'serial_num': 'HMG2A3807H',
                                            'soc1': None,
                                            'soc2': None,
                                            'status': 1,
                                            'status_text': 'Normal',
                                            'sys_fault_word': 0,
                                            'sys_fault_word1': 0,
                                            'sys_fault_word2': 0,
                                            'sys_fault_word3': 106,
                                            'sys_fault_word4': 165,
                                            'sys_fault_word5': 0,
                                            'sys_fault_word6': 0,
                                            'sys_fault_word7': 0,
                                            't_mtnc_strt': None,
                                            't_win_end': None,
                                            't_win_start': None,
                                            'temp1': 33.599998474121094,
                                            'temp2': 0.0,
                                            'temp3': 0.0,
                                            'temp4': 0.0,
                                            'temp5': 42.099998474121094,
                                            'time': datetime.datetime(2021, 1, 7, 19, 29, 10),
                                            'time_total': 169507.4,
                                            'tlx_bean': None,
                                            'total_working_time': None,
                                            'uw_sys_work_mode': 0,
                                            'vac1': 231.0,
                                            'vac2': 0.0,
                                            'vac3': 0.0,
                                            'vac_rs': 231.0,
                                            'vac_st': 0.0,
                                            'vac_tr': 0.0,
                                            'vacr': 0.0,
                                            'vacrs': 0.0,
                                            'vpv1': 257.0,
                                            'vpv2': 224.0,
                                            'vpv3': 0.0,
                                            'vpv4': 0.0,
                                            'warn_code': 0,
                                            'warn_code1': None,
                                            'warn_text': 'Unknown',
                                            'win_mode': None,
                                            'win_off_grid_soc': None,
                                            'win_on_grid_soc': None,
                                            'win_request': None,
                                            'with_time': False},
                            },
                            {   'datalogger_sn': 'XGD3A206CA',
                                'device_sn': 'XTD7A2562B',
                                'data': {   'address': 0,
                                            # ...
                                            'with_time': False},
                                }],
                'error_code': 0,
                'error_msg': None,
                'page_num': 1}
        """

        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/tlx/tlxs_data",
            data={
                "tlxs": device_sn,
                "pageNum": page or 1,
            },
        )

        # Unfortunately, the original response cannot be parsed by pydantic as the inverter_sn is used as key
        # To fix this, resulting data is restructured
        devices = [
            MinEnergyOverviewMultipleItem(
                device_sn=inverter_sn,
                datalogger_sn=response.get("data", {}).get(inverter_sn, {}).get("dataloggerSn", None),
                data=response.get("data", {}).get(inverter_sn, {}).get(inverter_sn, None),
            )
            for inverter_sn in response.get("tlxs", [])
        ]
        response.pop("tlxs", None)
        response["data"] = devices

        return MinEnergyOverviewMultiple.model_validate(response)

    def energy_history(
        self,
        device_sn: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> MinEnergyHistory:
        """
        Get historical data of a Min
        An interface for obtaining historical data of a Min
        https://www.showdoc.com.cn/262556420217021/8559849784929961

        Note:
            Only applicable to devices with device type 7 (min) returned by device.list()

        This endpoint returns only a subset of the parameters returned by the min.energy() endpoint

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: serial number is empty
        * 10003: start date is wrong
        * 10004: start date interval has exceeded seven days
        * 10005: Min does not exist
        * 10011: permission is not satisfied

        Args:
            device_sn (str): Inverter serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            StorageEnergyHistory
            e.g.
            {   'data': {   'count': 125,
                            'datalogger_sn': 'QMN0000000000000',
                            'datas': [   {   'battery_no': -1,
                                             'bdc1_charge_power': 0.0,
                                             'bdc1_charge_total': 0.0,
                                             'bdc1_discharge_power': 0.0,
                                             'bdc1_discharge_total': 0.0,
                                             'bdc1_fault_type': 0,
                                             'bdc1_ibat': 0.0,
                                             'bdc1_ibb': 0.0,
                                             'bdc1_illc': 0.0,
                                             'bdc1_mode': 0,
                                             'bdc1_soc': 0.0,
                                             'bdc1_status': 0,
                                             'bdc1_temp1': 0.0,
                                             'bdc1_temp2': 0.0,
                                             'bdc1_vbat': 0.0,
                                             'bdc1_vbus1': 0.0,
                                             'bdc1_vbus2': 0.0,
                                             'bdc1_warn_code': 0,
                                             'bdc2_charge_power': 0.0,
                                             'bdc2_charge_total': 0.0,
                                             'bdc2_discharge_power': 0.0,
                                             'bdc2_discharge_total': 0.0,
                                             'bdc2_fault_type': 0,
                                             'bdc2_ibat': 0.0,
                                             'bdc2_ibb': 0.0,
                                             'bdc2_illc': 0.0,
                                             'bdc2_mode': 0,
                                             'bdc2_soc': 0.0,
                                             'bdc2_status': 0,
                                             'bdc2_temp1': 0.0,
                                             'bdc2_temp2': 0.0,
                                             'bdc2_vbat': 0.0,
                                             'bdc2_vbus1': 0.0,
                                             'bdc2_vbus2': 0.0,
                                             'bdc2_warn_code': 0,
                                             'bdc_bus_ref': 0,
                                             'bdc_derate_reason': 0,
                                             'bdc_fault_sub_code': 0,
                                             'bdc_status': 0,
                                             'bdc_vbus2_neg': 0.0,
                                             'bdc_warn_sub_code': 0,
                                             'bms_communication_type': 0,
                                             'bms_cv_volt': 0.0,
                                             'bms_error2': 0,
                                             'bms_error3': 0,
                                             'bms_error4': 0,
                                             'bms_fault_type': 0,
                                             'bms_fw_version': '0',
                                             'bms_ibat': 0.0,
                                             'bms_icycle': 0.0,
                                             'bms_info': 0,
                                             'bms_ios_status': 0,
                                             'bms_max_curr': 0.0,
                                             'bms_mcu_version': '0',
                                             'bms_pack_info': 0,
                                             'bms_soc': 0.0,
                                             'bms_soh': 0.0,
                                             'bms_status': 0,
                                             'bms_temp1_bat': 0.0,
                                             'bms_using_cap': 0,
                                             'bms_vbat': 0.0,
                                             'bms_vdelta': 0.0,
                                             'bms_warn2': 0,
                                             'bms_warn_code': 0.0,
                                             'calendar': {   'first_day_of_week': 1,
                                                             'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                             'lenient': True,
                                                             'minimal_days_in_first_week': 1,
                                                             'time': {'date': 21, 'day': 5, 'hours': 16, 'minutes': 4, 'month': 1, 'seconds': 37, 'time': 1740125077000, 'timezone_offset': -480, 'year': 125},
                                                             'time_in_millis': 1740125077000,
                                                             'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                             'week_date_supported': True,
                                                             'week_year': 2025,
                                                             'weeks_in_week_year': 52},
                                             'dc_voltage': 0.0,
                                             'dci_r': 0.0,
                                             'dci_s': 0.0,
                                             'dci_t': 0.0,
                                             'debug1': '0，0，0，0，0，0，0，0',
                                             'debug2': '0，0，9，5387，0，12260，1，0',
                                             'derating_mode': 0,
                                             'dry_contact_status': 0,
                                             'e_charge_today': 0.0,
                                             'e_charge_total': 0.0,
                                             'e_discharge_today': 0.0,
                                             'e_discharge_total': 0.0,
                                             'e_local_load_today': 0.0,
                                             'e_local_load_total': 0.0,
                                             'e_self_today': 0.0,
                                             'e_self_total': 0.0,
                                             'e_system_today': 0.0,
                                             'e_system_total': 0.0,
                                             'e_to_grid_today': 0.0,
                                             'e_to_grid_total': 0.0,
                                             'e_to_user_today': 0.0,
                                             'e_to_user_total': 0.0,
                                             'eac_charge_today': 0.0,
                                             'eac_charge_total': 0.0,
                                             'eac_today': 1.8,
                                             'eac_total': 43.5,
                                             'eex1_today': -0.1,
                                             'eex1_total': -0.1,
                                             'eex2_today': -0.1,
                                             'eex2_total': -0.1,
                                             'eps_fac': 0.0,
                                             'eps_iac1': 0.0,
                                             'eps_iac2': 0.0,
                                             'eps_iac3': 0.0,
                                             'eps_pac': 0.0,
                                             'eps_pac1': 0.0,
                                             'eps_pac2': 0.0,
                                             'eps_pac3': 0.0,
                                             'eps_pf': -1.0,
                                             'eps_vac1': 0.0,
                                             'eps_vac2': 0.0,
                                             'eps_vac3': 0.0,
                                             'epv1_today': 1.9,
                                             'epv1_total': 47.1,
                                             'epv2_today': 0.0,
                                             'epv2_total': 0.0,
                                             'epv3_today': 0.0,
                                             'epv3_total': 0.0,
                                             'epv4_today': 0.0,
                                             'epv4_total': 0.0,
                                             'epv_total': 47.1,
                                             'fac': 50.03,
                                             'fault_type': 0,
                                             'fault_type1': 0,
                                             'gfci': 0.0,
                                             'iac1': 0.7,
                                             'iac2': 0.0,
                                             'iac3': 0.0,
                                             'inv_delay_time': 65.0,
                                             'ipv1': 5.8,
                                             'ipv2': 0.0,
                                             'ipv3': 0.0,
                                             'ipv4': 0.0,
                                             'is_again': False,
                                             'iso': 2630.0,
                                             'load_percent': 0.0,
                                             'n_bus_voltage': 0.0,
                                             'new_warn_code': 0,
                                             'new_warn_sub_code': 0,
                                             'op_fullwatt': 0.0,
                                             'operating_mode': 0,
                                             'p_bus_voltage': 447.7,
                                             'p_self': 0.0,
                                             'p_system': 0.0,
                                             'pac': 163.8,
                                             'pac1': 164.8,
                                             'pac2': 0.0,
                                             'pac3': 0.0,
                                             'pac_to_grid_total': 0.0,
                                             'pac_to_local_load': 0.0,
                                             'pac_to_user_total': 0.0,
                                             'pex1': -0.1,
                                             'pex2': -0.1,
                                             'pf': 0.9974,
                                             'ppv': 170.6,
                                             'ppv1': 170.6,
                                             'ppv2': 0.0,
                                             'ppv3': 0.0,
                                             'ppv4': 0.0,
                                             'real_op_percent': 16.0,
                                             'serial_num': 'BZP0000000',
                                             'status': 1,
                                             'sys_fault_word': 0,
                                             'sys_fault_word1': 2,
                                             'sys_fault_word2': 0,
                                             'sys_fault_word3': 0,
                                             'sys_fault_word4': 0,
                                             'sys_fault_word5': 0,
                                             'sys_fault_word6': 0,
                                             'sys_fault_word7': 0,
                                             'temp1': 33.0,
                                             'temp2': 33.0,
                                             'temp3': 33.0,
                                             'temp4': 33.0,
                                             'temp5': 0.0,
                                             'time': datetime.datetime(2025, 2, 21, 16, 4, 37),
                                             'time_total': 1894833.0,
                                             'total_working_time': 0.0,
                                             'uw_sys_work_mode': 0,
                                             'vac1': 235.1,
                                             'vac2': 0.0,
                                             'vac3': 0.0,
                                             'vac_rs': 235.1,
                                             'vac_st': 0.0,
                                             'vac_tr': 0.0,
                                             'vpv1': 29.2,
                                             'vpv2': 10.1,
                                             'vpv3': 0.0,
                                             'vpv4': 0.0,
                                             'warn_code': 220,
                                             'warn_code1': 2}],
                            'device_sn': 'BZP0000000',
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
        if end_date - start_date >= timedelta(days=7):
            raise ValueError("date interval must not exceed 7 days")

        response = self.session.post(
            endpoint="device/tlx/tlx_data",
            data={
                "tlx_sn": device_sn,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return MinEnergyHistory.model_validate(response)

    def alarms(
        self,
        device_sn: str,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> MinAlarms:
        """
        Get the alarm data of a certain Min
        Interface to get alarm data of a certain Min
        https://www.showdoc.com.cn/262556420217021/6129824764736661

        Note:
            Only applicable to devices with device type 7 (min) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10005: Min does not exist

        Args:
            device_sn (str): Inverter serial number
            date_ (Optional[date]): Date - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            MinAlarms
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
            endpoint="device/tlx/alarm_data",
            data={
                "tlx_sn": device_sn,
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return MinAlarms.model_validate(response)
