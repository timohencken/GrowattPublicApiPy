from datetime import date, timedelta, time
from typing import Optional, Union, List, Dict, Any, Tuple

from ..growatt_types import DeviceType
from ..pydantic_models import VppSoc, VppWrite
from ..pydantic_models.api_v4 import (
    MinDetailsV4,
    MinEnergyV4,
    MinEnergyHistoryV4,
    MinEnergyHistoryMultipleV4,
    SettingWriteV4,
    SettingReadVppV4,
)
from ..pydantic_models.min import (
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
from ..session.growatt_api_session import GrowattApiSession  # noqa: E402
from ..api_v4.api_v4 import ApiV4  # noqa: E402
from ..vpp.vpp import Vpp  # noqa: E402


class Min:
    """
    endpoints for MIN / TLX inverters
    https://www.showdoc.com.cn/262556420217021/6129816412127075

    Note:
        Only applicable to devices with device type 7 (min) returned by plant.list_devices()
    """

    session: GrowattApiSession
    device_sn: Optional[str] = None
    _api_v4: ApiV4
    _api_vpp: Vpp

    def __init__(self, session: GrowattApiSession, device_sn: Optional[str] = None) -> None:
        self.session = session
        self.device_sn = device_sn
        self._api_v4 = ApiV4(session=session)
        self._api_vpp = Vpp(session=session)

    def _device_sn(self, device_sn: Optional[Union[str, List[str]]]) -> Union[str, List[str]]:
        """
        Use device_sn explicitly provided, fallback to the one from the instance
        """
        device_sn = device_sn or self.device_sn
        if device_sn is None:
            raise AttributeError("device_sn must be provided")
        return device_sn

    def settings(
        self,
        device_sn: Optional[str] = None,
    ) -> MinSettings:
        """
        Read Min settings
        https://www.showdoc.com.cn/262556420217021/8696815667375182

        Note:
            Only applicable to devices with device type 7 (min) returned by plant.list_devices()

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
                "device_sn": self._device_sn(device_sn),
            },
        )

        return MinSettings.model_validate(response)

    def setting_read(
        self,
        device_sn: Optional[str] = None,
        parameter_id: Optional[str] = None,
        start_address: Optional[int] = None,
        end_address: Optional[int] = None,
    ) -> MinSettingRead:
        """
        Read Min setting parameter interface
        https://www.showdoc.com.cn/262556420217021/6119793934974232

        Note:
            Only applicable to devices with device type 7 (min) returned by plant.list_devices()

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
                "device_sn": self._device_sn(device_sn),
                "paramId": parameter_id,
                "startAddr": start_address,
                "endAddr": end_address,
            },
        )

        return MinSettingRead.model_validate(response)

    def setting_read_vpp_param(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        parameter_id: str,
        device_sn: Optional[str] = None,
    ) -> SettingReadVppV4:
        """
        Read VPP parameters using "new-api" endpoint
        Read the VPP related parameters of the device according to the SN of the device.
        https://www.showdoc.com.cn/2598832417617967/11558629942271434

        Note:
        * The current interface only supports
          * MIN 2500-6000TL-XH US
          * MIN 2500-6000TL-XH

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Allowed/known values for vpp_param:
          see self.setting_write_vpp_param()

        Args:
            device_sn (str): Inverter serial number
            parameter_id (str): Set parameter enumeration, example: set_param_1

        Returns:
            SettingReadVppV4
            e.g.
            {   'data': 0,
                'error_code': 0,
                'error_msg': 'success'}

        """

        return self._api_v4.setting_read_vpp_param(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.MIN,
            parameter_id=parameter_id,
        )

    # noinspection PyUnusedLocal
    def setting_write(
        self,
        parameter_id: str,
        parameter_value_1: Union[str, int],
        device_sn: Optional[str] = None,
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
            Only applicable to devices with device type 7 (min) returned by plant.list_devices()

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
                "tlx_sn": self._device_sn(device_sn),
                "type": parameter_id,
                **{f"param{i}": parameters[i] for i in range(1, 20)},
            },
        )

        return MinSettingWrite.model_validate(response)

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
            device_type=DeviceType.MIN,
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
            device_type=DeviceType.MIN,
            active_power=active_power_percent,
        )

    def setting_write_vpp_param(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        parameter_id: str,
        value: Union[int, str],
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set VPP parameters using "new-api" endpoint
        Set the VPP related parameters of the device according to the SN of the device.
        https://www.showdoc.com.cn/2598832417617967/11558385202215329

        Note:
        * The current interface only supports
          * MIN 2500-6000TL-XH US
          * MIN 2500-6000TL-XH

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Allowed/known values for vpp_param:
        ========================+===============+===========================+============================================================================
        description             | parameter_id  | parameter_value           | comment
        ========================+===============+===========================+============================================================================
        Control authority       | set_param_1   | 0 ~ 1                     | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        On off command          | set_param_2   | 0 ~ 1                     | Not storage
                                |               |                           | 0 = power off
                                |               |                           | 1 = power on (default)
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        System time             | set_param_3   | yyyy-mm-dd HH:MM:SS       | Example: 2024-10-10 13:14:14
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        SYN enable              | set_param_4   | 0 ~ 1                     | Offline box enable
                                |               |                           | 0: not enabled (default)
                                |               |                           | 1: enable
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Active power            | set_param_5   | 0 ~ 100                   | Power limit percentage
         percentage derating    |               |                           | default value = 100
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Static active power     | set_param_6   | 0 ~ 100                   | Power limit percent
                                |               |                           | Actual active power is the less one between Active power percentage derating
                                |               |                           |  and Static active power limitation - Not storage
                                |               |                           | default value = 100
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EPS offline enable      | set_param_7   | 0 ~ 1                     | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EPS offline frequency   | set_param_8   | 0 ~ 1                     | 0 = 50 Hz (default)
                                |               |                           | 1 = 60 Hz
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EPS offline voltage(3)  | set_param_9   | 0 ~ 6                     | 0 = 230 V (default)
                                |               |                           | 1 = 208V
                                |               |                           | 2 = 240V
                                |               |                           | 3 = 220V
                                |               |                           | 4 = 127V
                                |               |                           | 5 = 277V
                                |               |                           | 6 = 254V
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Fix Q                   | set_param_10  | 0 ~ 60                    | Power limit percentage
                                |               |                           | default value = 60
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Reactive power mode     | set_param_11  | 0 ~ 5                     | 0: PF=1 (default)
                                |               |                           | 1: Pf value setting
                                |               |                           | 2: Default pf curve(reserve)
                                |               |                           | 3: User set pf curve(reserve)
                                |               |                           | 4: Lagging reactive power (+)
                                |               |                           | 5: Leading reactive power (-)
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Power factor            | set_param_12  | 0 ~ 20000                 | Actual power factor = (10000 - set_value) * 0.0001
                                |               |                           | default value = 10000
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Dynamic export          | set_param_13  | 0 ~ 1                     | 0 = disabled (default)
         limitation             |               |                           | 1 = single machine anti-back flow enable
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Export limitation power | set_param_14  | -100 ~ 100                | Positive value is backflow, negative value is fair current
                                |               |                           | default value = 0
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Failure value of        | set_param_15  | 0 ~ 100                   | When the communication with meter failed (30204 is 1), use this register
         anti-backflow limiting |               |                           |  to limit reactive power，for backflow control
         power                  |               |                           | default value = 0
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-back flow fail     | set_param_16  | 0 ~ 300                   | default value = 30
         time/EMS communicating |               |                           |
         fail time              |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EMS communicating fail  | set_param_17  | 0 ~ 1                     | 0 = disabled (default)
         enable                 |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Super anti-backflow     | set_param_18  | 0 ~ 1                     | 0 = disabled (default)
         enable                 |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow feed      | set_param_19  | 0 ~ 20000                 | default value = 27
         power change slope     |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow single    | set_param_20  | 0 ~ 1                     | 0 = disabled (default)
         phase ctrl enable      |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow           | set_param_21  | 0 ~ 1                     | 0 = Default mode (default)
         protection mode（1）    |               |                           | 1 = software and hardware control mode
                                |               |                           | 2 = software control mode
                                |               |                           | 3 = hardware control mode
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Charging cut off SOC    | set_param_22  | 70 ~ 100                  | default value = 100
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Online discharge cut    | set_param_23  | 10 ~ 30                   | default value = 10
         off SOC                |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Load priority discharge | set_param_24  | 10 ~ 20                   | default value = 10
         cut off SOC (2)        |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Remote power control    | set_param_25  | 0 ~ 1                     | Not storage
         enable                 |               |                           | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Remote power control    | set_param_26  | 0 ~ 1440                  | Not storage
         charging time          |               |                           | 0: unlimited time (default)
                                |               |                           | 1 ~ 1440 min: control the power duration according to the set time
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Remote charge and       | set_param_27  | -100 ~ 100                | Not storage
         discharge power        |               |                           | negative value = discharge, positive value = charge
                                |               |                           | default value = 0
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        AC charging enable      | set_param_28  | 0 ~ 1                     | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Offline discharge cut   | set_param_29  | 10 ~ 30                   | default value = 10
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery charge stop     | set_param_30  | 0 ~ 15000                 | Lead-acid battery used - Distinguished by voltage level
         voltage                |               |                           |  3800 = 127 V
                                |               |                           | 10000 = 227 V
                                |               |                           |  8000 = Others
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery discharge stop  | set_param_31  | 0 ~ 15000                 | Lead-acid battery used - Distinguished by voltage level
         voltage                |               |                           | 3800 = 127 V
                                |               |                           | 7500 = 227 V
                                |               |                           | 6500 = Others
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery max charge      | set_param_32  | 0 ~ 2000                  | Lead-acid battery used
         current                |               |                           | default value = 1500
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery max discharge   | set_param_33  | 0 ~ 2000                  | Lead-acid battery used
         current                |               |                           | default value = 1500
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Charging and discharging| set_param_34  | 0 ~ 2000                  | Set time period (json format: [{percentage: power, startTime: start time, endTime: end time}]
         in different periods   |               |                           | time range: 0-1440
          (20 sections)         |               |                           | e.g.: [{"percentage":95,"startTime":0,"endTime":300},{"percentage":-60,"startTime":301,"endTime":720}]
        ========================+===============+===========================+============================================================================
        see https://www.showdoc.com.cn/2598832417617967/11558385130027995 or https://www.showdoc.com.cn/p/fc84c86facd79b3692f585fbd7a6e33b
        ========================+===============+===========================+============================================================================


        Args:
            device_sn (str): Inverter serial number
            parameter_id (str): Set parameter enumeration, example: set_param_1
            value (Union[int, str]): the parameter value set, example:value


        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_vpp_param(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.MIN,
            parameter_id=parameter_id,
            value=value,
        )

    def details(
        self,
        device_sn: Optional[str] = None,
    ) -> MinDetails:
        """
        Get Min basic information
        Interface to get basic information of Min
        https://www.showdoc.com.cn/262556420217021/6129816412127075

        Note:
            Only applicable to devices with device type 7 (min) returned by plant.list_devices()

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
                "device_sn": self._device_sn(device_sn),
            },
        )

        return MinDetails.model_validate(response)

    def details_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> MinDetailsV4:
        """
        Batch device information using "new-api" endpoint
        Retrieve basic information of devices in bulk based on device SN.
        https://www.showdoc.com.cn/2540838290984246/11292915673945114

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            MinDetailsV4
            e.g.
            {   'data': {   'min': [   {   'address': 1,
                                           'alias': 'BZP3N6U09K',
                                           'bat_aging_test_step': 0,
                                           'bat_parallel_num': 0,
                                           'bat_series_num': 0,
                                           'bat_sys_energy': 0.0,
                                           'bat_temp_lower_limit_c': 0.0,
                                           'bat_temp_lower_limit_d': 0.0,
                                           'bat_temp_upper_limit_c': 0.0,
                                           'bat_temp_upper_limit_d': 0.0,
                                           'battery_type': 0,
                                           'baudrate': 0,
                                           'bct_adjust': 0,
                                           'bct_mode': 0,
                                           'bcu_version': None,
                                           'bdc1_model': '0',
                                           'bdc1_sn': None,
                                           'bdc1_version': '\x00\x00\x00\x00-0',
                                           'bdc_auth_version': 0,
                                           'bdc_mode': 0,
                                           'bms_communication_type': 0,
                                           'bms_software_version': None,
                                           'children': None,
                                           'com_address': 1,
                                           'communication_version': 'GJAA-0004',
                                           'country_selected': 1,
                                           'datalogger_sn': 'QMN000BZP3N6U09K',
                                           'device_type': 5,
                                           'dtc': 5203,
                                           'e_today': 0.0,
                                           'e_total': 0.0,
                                           'energy_day_map': {},
                                           'energy_month': 0.0,
                                           'energy_month_text': '0',
                                           'fw_version': 'GJ1.0',
                                           'group_id': -1,
                                           'hw_version': '0',
                                           'id': 1404608,
                                           'img_path': './css/img/status_gray.gif',
                                           'inner_version': 'GJAA04xx',
                                           'last_update_time': 1742876493000,
                                           'last_update_time_text': datetime.datetime(2025, 3, 25, 12, 21, 33),
                                           'level': 4,
                                           'li_battery_fw_version': None,
                                           'li_battery_manufacturers': None,
                                           'location': None,
                                           'lost': False,
                                           'manufacturer': '   PV Inverter  ',
                                           'modbus_version': 0,
                                           'model': 504403158517219338,
                                           'model_text': 'S07B00D00T00P0FU01M000A',
                                           'monitor_version': None,
                                           'mppt': 513.0,
                                           'optimizer_list': None,
                                           'p_charge': 0.0,
                                           'p_discharge': 0.0,
                                           'parent_id': 'LIST_QMN000BZP3N6U09K_22',
                                           'plant_id': 0,
                                           'plantname': None,
                                           'pmax': 1000,
                                           'port_name': 'ShinePano-QMN000BZP3N6U09K',
                                           'power': 0.0,
                                           'power_max': None,
                                           'power_max_text': None,
                                           'power_max_time': None,
                                           'priority_choose': 0,
                                           'pv_num': 0,
                                           'record': None,
                                           'restart_time': 65,
                                           'safety_version': 0,
                                           'serial_num': 'BZP3N6U09K',
                                           'start_time': 65,
                                           'status': 1,
                                           'status_text': 'tlx.status.checking',
                                           'str_num': -1,
                                           'sys_time': None,
                                           'tcp_server_ip': '47.254.132.50',
                                           'timezone': 1.0,
                                           'tlx_set_bean': None,
                                           'tracker_model': 0,
                                           'tree_id': 'ST_BZP3N6U09K',
                                           'tree_name': 'BZP3N6U09K',
                                           'updating': False,
                                           'user_name': None,
                                           'vbat_start_for_discharge': 0.0,
                                           'vbat_stop_for_charge': 0.0,
                                           'vbat_stop_for_discharge': 0.0,
                                           'vbat_warn_clr': 0.0,
                                           'vbat_warning': 0.0,
                                           'vnormal': 280.0,
                                           'vpp_open': 0.0}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.details(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.MIN,
        )

    def energy(
        self,
        device_sn: Optional[str] = None,
    ) -> MinEnergyOverview:
        """
        Get the latest real-time data of Min
        Interface to get the latest real-time data of Min
        https://www.showdoc.com.cn/262556420217021/6129822090975531

        Note:
            Only applicable to devices with device type 7 (min) returned by plant.list_devices()

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
                "tlx_sn": self._device_sn(device_sn),
            },
        )

        return MinEnergyOverview.model_validate(response)

    def energy_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> MinEnergyV4:
        """
        Batch equipment data information using "new-api" endpoint
        Retrieve the last detailed data for multiple devices based on their SN and device type.
        https://www.showdoc.com.cn/2540838290984246/11292915898375566

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            MinEnergyV4
            e.g.
            {   'data': {   'min': [   {   'address': 0,
                                           'again': False,
                                           'alias': None,
                                           'b_merter_connect_flag': False,
                                           'bat_sn': None,
                                           'battery_no': -1,
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
                                           'bms_info': 0.0,
                                           'bms_ios_status': 0,
                                           'bms_max_curr': 0.0,
                                           'bms_mcu_version': '0',
                                           'bms_pack_info': 0.0,
                                           'bms_soc': 0.0,
                                           'bms_soh': 0.0,
                                           'bms_status': 0,
                                           'bms_temp1_bat': 0.0,
                                           'bms_using_cap': 0.0,
                                           'bms_vbat': 0.0,
                                           'bms_vdelta': 0.0,
                                           'bms_warn2': 0,
                                           'bms_warn_code': 0.0,
                                           'bsystem_work_mode': 0,
                                           'calendar': 1742974615711,
                                           'datalogger_sn': 'QMN000BZP3N6U09K',
                                           'day': None,
                                           'dc_voltage': 0.0,
                                           'dci_r': 0.0,
                                           'dci_s': 0.0,
                                           'dci_t': 0.0,
                                           'debug1': '0，0，0，0，0，2，2，0',
                                           'debug2': '0，1，9，5660，0，12260，1，0',
                                           'derating_mode': 0,
                                           'device_sn': 'BZP3N6U09K',
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
                                           'eac_today': 0.2,
                                           'eac_total': 76.8,
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
                                           'epv1_today': 0.3,
                                           'epv1_total': 83.5,
                                           'epv2_today': 0.0,
                                           'epv2_total': 0.0,
                                           'epv3_today': 0.0,
                                           'epv3_total': 0.0,
                                           'epv4_today': 0.0,
                                           'epv4_total': 0.0,
                                           'epv_total': 83.5,
                                           'error_text': 'Unknown',
                                           'fac': 50.0,
                                           'fault_type': 0,
                                           'fault_type1': 0,
                                           'gfci': 0.0,
                                           'iac1': 0.1,
                                           'iac2': 0.0,
                                           'iac3': 0.0,
                                           'iacr': 0.0,
                                           'inv_delay_time': 65.0,
                                           'ipv1': 0.7,
                                           'ipv2': 0.0,
                                           'ipv3': 0.0,
                                           'ipv4': 0.0,
                                           'is_again': False,
                                           'iso': 2648.0,
                                           'load_percent': 0.0,
                                           'lost': True,
                                           'mtnc_mode': 0,
                                           'mtnc_rqst': 0.0,
                                           'n_bus_voltage': 0.0,
                                           'new_warn_code': 0,
                                           'new_warn_sub_code': 0,
                                           'op_fullwatt': 0.0,
                                           'operating_mode': 0,
                                           'p_bus_voltage': 447.8,
                                           'p_self': 0.0,
                                           'p_system': 0.0,
                                           'pac': 10.6,
                                           'pac1': 17.2,
                                           'pac2': 0.0,
                                           'pac3': 0.0,
                                           'pac_to_grid_total': 0.0,
                                           'pac_to_local_load': 0.0,
                                           'pac_to_user_total': 0.0,
                                           'pacr': 0.0,
                                           'pex1': -0.1,
                                           'pex2': -0.1,
                                           'pf': 1.0,
                                           'ppv': 21.6,
                                           'ppv1': 21.6,
                                           'ppv2': 0.0,
                                           'ppv3': 0.0,
                                           'ppv4': 0.0,
                                           'real_op_percent': 1.0,
                                           'soc1': 0.0,
                                           'soc2': 0.0,
                                           'status': 1,
                                           'status_text': 'Normal',
                                           'sys_fault_word': 0,
                                           'sys_fault_word1': 2,
                                           'sys_fault_word2': 0,
                                           'sys_fault_word3': 0,
                                           'sys_fault_word4': 0,
                                           'sys_fault_word5': 0,
                                           'sys_fault_word6': 0,
                                           'sys_fault_word7': 0,
                                           't_mtnc_strt': None,
                                           't_win_end': None,
                                           't_win_start': None,
                                           'temp1': 21.2,
                                           'temp2': 21.2,
                                           'temp3': 21.2,
                                           'temp4': 21.2,
                                           'temp5': 0.0,
                                           'time': datetime.datetime(2025, 3, 26, 15, 36, 55),
                                           'time_total': 3055520.5,
                                           'tlx_bean': None,
                                           'total_working_time': 0.0,
                                           'uw_sys_work_mode': 0,
                                           'vac1': 233.4,
                                           'vac2': 0.0,
                                           'vac3': 0.0,
                                           'vac_rs': 233.4,
                                           'vac_st': 0.0,
                                           'vac_tr': 0.0,
                                           'vacr': 0.0,
                                           'vacrs': 0.0,
                                           'vpv1': 28.8,
                                           'vpv2': 10.1,
                                           'vpv3': 0.0,
                                           'vpv4': 0.0,
                                           'warn_code': 220,
                                           'warn_code1': 2,
                                           'warn_text': 'Unknown',
                                           'win_mode': 0,
                                           'win_off_grid_soc': 0.0,
                                           'win_on_grid_soc': 0.0,
                                           'win_request': 0,
                                           'with_time': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy(device_sn=self._device_sn(device_sn), device_type=DeviceType.MIN)

    def energy_multiple(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        page: Optional[int] = None,
    ) -> MinEnergyOverviewMultiple:
        """
        Get the latest real-time data of min in batches
        Interface to obtain the latest real-time data of inverters in batches
        https://www.showdoc.com.cn/262556420217021/6129830403882881

        Note:
            Only applicable to devices with device type 7 (min) returned by plant.list_devices()

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

        device_sn = self._device_sn(device_sn)
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
        device_sn: Optional[str] = None,
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
            Only applicable to devices with device type 7 (min) returned by plant.list_devices()

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
                "tlx_sn": self._device_sn(device_sn),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return MinEnergyHistory.model_validate(response)

    def energy_history_v4(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
    ) -> MinEnergyHistoryV4:
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
            MinEnergyHistoryV4
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
            device_sn=self._device_sn(device_sn), device_type=DeviceType.MIN, date_=date_
        )

    def energy_history_multiple_v4(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        date_: Optional[date] = None,
    ) -> MinEnergyHistoryMultipleV4:
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
            MinEnergyHistoryMultipleV4
            e.g.
            {   'data': {   'NHB691514F': [   {
                                                  <see energy_v4() for attributes>
                                              }]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

        """

        return self._api_v4.energy_history_multiple(
            device_sn=self._device_sn(device_sn), device_type=DeviceType.MIN, date_=date_
        )

    def alarms(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> MinAlarms:
        """
        Get the alarm data of a certain Min
        Interface to get alarm data of a certain Min
        https://www.showdoc.com.cn/262556420217021/6129824764736661

        Note:
            Only applicable to devices with device type 7 (min) returned by plant.list_devices()

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
                "tlx_sn": self._device_sn(device_sn),
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return MinAlarms.model_validate(response)

    def soc(
        self,
        device_sn: Optional[str] = None,
    ) -> VppSoc:
        """
        Get machine SOC value (VPP)
        Get machine SOC value interface (only supports MIN SPA SPH models)
        https://www.showdoc.com.cn/262556420217021/7178565721512898

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: read failure
        * 10002: device does not exist
        * 10003: device serial number is empty

        Args:
            device_sn (str): VPP SN

        Returns:
            VppSoc
            {
                'error_code': 0,
                'error_msg': None,
                'soc': 65.0,
                'datalogger_sn': 'JPC5A11700',
                'device_sn': 'MIXECN6000'
            }
        """

        return self._api_vpp.soc(device_sn=self._device_sn(device_sn))

    def settings_write_vpp_now(
        self,
        time_: time,
        percentage: int,
        device_sn: Optional[str] = None,
    ) -> VppWrite:
        """
        Read the machine to perform battery charging contr
        The reading machine immediately executes the battery charging control interface (only supports MIN SPA SPH models)
        https://www.showdoc.com.cn/262556420217021/7178602212464389

        Note: this endpoint is poorly documented

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 500: Set Parameter Failure
        * 10001: Reading failed
        * 10012: Device does not exist
        * 10004: Device serial number is empty
        * 10005: Collector offline
        * 10007: Setting parameter is null
        * 10008: Setting value is out of range Or abnormal
        * 10009: The type of the read setting parameter does not exist
        * 10011: No permission

        Args:
            device_sn (str): VPP SN
            time_ (time): Set time - 00:00 ~ 24:00 (hh:mm),
            percentage (int): Set the power positive number for charging - negative number for discharge -100 ~ 100

        Returns:
            VppWrite
            {
                'error_code': 0,
                'error_msg': None,
                'data': 0,
            }
        """

        return self._api_vpp.write(
            device_sn=self._device_sn(device_sn),
            time_=time_,
            percentage=percentage,
        )

    def settings_write_vpp_schedule(
        self, schedules: List[Tuple[int, time, time]], device_sn: Optional[str] = None
    ) -> VppWrite:
        """
        Read and set VPP time period parameters (VPP)
        Read and set VPP time period parameter interface (only support MIN SPA SPH model)
        https://www.showdoc.com.cn/262556420217021/7178602212464389

        Note: this endpoint is poorly documented

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: Reading/Writing failed
        * 10012: Device does not exist
        * 10004: Device serial number is empty
        * 10005: Collector offline
        * 10007: Setting parameter is null
        * 10008: Setting value is out of range Or abnormal
        * 10009: The type of the read setting parameter does not exist
        * 10011: No permission

        Args:
            device_sn (str): VPP SN
            schedules (List[Tuple[int, time, time]]): Set time period
                Tuple with (power_percentage (int), start_time (time), end_time (time))
                percentage: positive number for charge 0 ~ 100, negative number for discharge -100 ~ 0
                e.g. [
                    (95, time(hour=0, minute=0), time(hour=5, minute=0)),    # 00:00 ~ 05:00 95% charge
                    (-60, time(hour=5, minute=1), time(hour=12, minute=0)),  # 05:01 ~ 12:00 60% discharge
                ]

        Returns:
            VppWrite
            {
                'error_code': 0,
                'error_msg': None,
                'data': 0,
            }
        """

        return self._api_vpp.write_multiple(device_sn=self._device_sn(device_sn), schedules=schedules)
