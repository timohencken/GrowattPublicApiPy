import datetime
from typing import Union, Any, List, Optional, TypeAlias

from pydantic import (
    ConfigDict,
    BeforeValidator,
)
from pydantic.alias_generators import to_camel

from growatt_public_api.pydantic_models.api_model import (
    ApiResponse,
    EmptyStrToNone,
    GrowattTime,
    ApiModel,
)

from typing import Annotated


# #####################################################################################################################
# Min settings ####################################################################################################


def _min_tlx_settings_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "backflow_single_ctrl": "backFlowSingleCtrl",
        "discharge_power_command": "disChargePowerCommand",
        "on_grid_discharge_stop_soc": "onGridDischargeStopSOC",
        "ub_ac_charging_stop_soc": "ubAcChargingStopSOC",
        "ub_peak_shaving_backup_soc": "ubPeakShavingBackupSOC",
        "uw_hf_rt2_ee": "uwHFRT2EE",
        "uw_hf_rt_ee": "uwHFRTEE",
        "uw_hv_rt2_ee": "uwHVRT2EE",
        "uw_hv_rt_ee": "uwHVRTEE",
        "uw_lf_rt2_ee": "uwLFRT2EE",
        "uw_lf_rt_ee": "uwLFRTEE",
        "uw_lv_rt2_ee": "uwLVRT2EE",
        "uw_lv_rt_ee": "uwLVRTEE",
        "vbat_start_for_charge": "vbatStartforCharge",
        "w_charge_soc_low_Limit": "wchargeSOCLowLimit",
        "w_discharge_soc_low_limit": "wdisChargeSOCLowLimit",
        "win_mode_off_grid_discharge_stop_soc": "winModeOffGridDischargeStopSOC",
        "win_mode_on_grid_discharge_stop_soc": "winModeOnGridDischargeStopSOC",
    }
    return override.get(snake, to_camel(snake=snake))


def parse_forced_time(value: Optional[str] = None):
    """support 0:0 for 00:00"""
    if value and value.strip():
        try:
            return datetime.datetime.strptime(value, "%H:%M").time()
        except Exception as e:
            raise ValueError(str(e))
    else:
        return None


ForcedTime: TypeAlias = Annotated[
    Union[datetime.time, None], BeforeValidator(parse_forced_time)
]


class MinTlxSettingsData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_min_tlx_settings_data_to_camel,
    )

    ac_charge_enable: Union[EmptyStrToNone, bool] = (
        None  # AC charging enable; (0=disable, 1=enable), e.g. 0
    )
    ac_charge: Union[EmptyStrToNone, str] = None  # e.g. ''
    active_power_enable: Union[EmptyStrToNone, bool] = (
        None  # Active Power Enable, e.g. 0
    )
    active_rate: Union[EmptyStrToNone, float] = None  # Active power, e.g. 100
    afci_enabled: Union[EmptyStrToNone, int] = (
        None  # AFCI enabled (register 541), e.g. -1
    )
    afci_reset: Union[EmptyStrToNone, int] = None  # AFCI reset (register 543), e.g. -1
    afci_self_check: Union[EmptyStrToNone, int] = (
        None  # AFCI SelfCheck (register 542), e.g. -1
    )
    afci_threshold_d: Union[EmptyStrToNone, int] = (
        None  # AFCI threshold (register 545), e.g. -1
    )
    afci_threshold_h: Union[EmptyStrToNone, int] = (
        None  # AFCI Threshold High (register 546), e.g. -1
    )
    afci_threshold_l: Union[EmptyStrToNone, int] = (
        None  # AFCI Threshold Low (register 544), e.g. -1
    )
    backflow_single_ctrl: Union[EmptyStrToNone, int] = None  # e.g. 0
    backflow_default_power: Union[EmptyStrToNone, float] = (
        None  # Anti-backflow default power, e.g. 0
    )
    bdc_mode: Union[EmptyStrToNone, int] = (
        None  # Battery mode (0 = self-use, 1 = battery priority, 2 = grid priority, 255 = disabled), e.g. -1
    )
    bgrid_type: Union[EmptyStrToNone, int] = None  # Grid Type (register 613), e.g. 0
    bsystem_work_mode: Union[EmptyStrToNone, float] = (
        None  # Work Mode (register 612), e.g. 50
    )
    charge_power_command: Union[EmptyStrToNone, float] = (
        None  # Charge power setting in %, e.g. 100
    )
    charge_power: Union[EmptyStrToNone, float] = None  # e.g. ''
    charge_stop_soc: Union[EmptyStrToNone, float] = None  # e.g. ''
    compatible_flag: Union[EmptyStrToNone, int] = None  # e.g. 0
    delay_time: Union[EmptyStrToNone, int] = None  # Q(V) delay time, e.g. 10000
    demand_manage_enable: Union[EmptyStrToNone, int] = None  # e.g. 0
    discharge_power_command: Union[EmptyStrToNone, float] = (
        None  # Discharge power setting in %, e.g. 100
    )
    discharge_power: Union[EmptyStrToNone, str] = None  # e.g. ''
    discharge_stop_soc: Union[EmptyStrToNone, float] = None  # e.g. ''
    dry_contact_func_en: Union[EmptyStrToNone, bool] = (
        None  # Dry contact function enable, e.g. 0
    )
    dry_contact_off_rate: Union[EmptyStrToNone, float] = (
        None  # Dry contact off power percentage, e.g. 40
    )
    dry_contact_on_rate: Union[EmptyStrToNone, float] = (
        None  # Dry contact conduction power percentage, e.g. 50
    )
    dry_contact_power: Union[EmptyStrToNone, float] = (
        None  # Dry contact opening power, e.g. 50
    )
    enable_n_line: Union[EmptyStrToNone, int] = None  # e.g. 0
    eps_freq_set: Union[EmptyStrToNone, float] = (
        None  # Emergency power frequency (0=50Hz, 1=60Hz), e.g. 0
    )
    eps_fun_en: Union[EmptyStrToNone, bool] = (
        None  # Emergency power enable (0=disable 1=enable), e.g. 1
    )
    eps_volt_set: Union[EmptyStrToNone, int] = (
        None  # emergency power supply voltage (0=230, 1=208, 2=240), e.g. 2
    )
    export_limit: Union[EmptyStrToNone, float] = None  # Anti-backflow enable, e.g. 0
    export_limit_power_rate: Union[EmptyStrToNone, float] = (
        None  # Backflow Prevention, e.g. 0
    )
    export_limit_power_rate_str: Union[EmptyStrToNone, str] = None  # e.g. ''
    exter_comm_off_grid_en: Union[EmptyStrToNone, bool] = (
        None  # Manual off-grid enable, e.g. 0
    )
    fail_safe_curr: Union[EmptyStrToNone, float] = None  # e.g. 0
    fft_threshold_count: Union[EmptyStrToNone, int] = (
        None  # Threshold exceeded (register 547), e.g. -1
    )
    float_charge_current_limit: Union[EmptyStrToNone, float] = (
        None  # float charge current limit in 0.1A, e.g. 600 = 60 A
    )
    forced_stop_switch1: Union[EmptyStrToNone, int] = None  # e.g. 0
    forced_stop_switch2: Union[EmptyStrToNone, int] = None  # e.g. 0
    forced_stop_switch3: Union[EmptyStrToNone, int] = None  # e.g. 0
    forced_stop_switch4: Union[EmptyStrToNone, int] = None  # e.g. 0
    forced_stop_switch5: Union[EmptyStrToNone, int] = None  # e.g. 0
    forced_stop_switch6: Union[EmptyStrToNone, int] = None  # e.g. 0
    forced_stop_switch7: Union[EmptyStrToNone, int] = None  # e.g. 0
    forced_stop_switch8: Union[EmptyStrToNone, int] = None  # e.g. 0
    forced_stop_switch9: Union[EmptyStrToNone, int] = None  # e.g. 0
    forced_time_start1: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 1 start time; hours:minutes, e.g. '0:0'
    )
    forced_time_start2: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 2 start time; hours:minutes, e.g. '0:0'
    )
    forced_time_start3: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 3 start time; hours:minutes, e.g. '0:0'
    )
    forced_time_start4: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 4 start time; hours:minutes, e.g. '0:0'
    )
    forced_time_start5: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 5 start time; hours:minutes, e.g. '0:0'
    )
    forced_time_start6: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 6 start time; hours:minutes, e.g. '0:0'
    )
    forced_time_start7: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 7 start time; hours:minutes, e.g. '0:0'
    )
    forced_time_start8: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 8 start time; hours:minutes, e.g. '0:0'
    )
    forced_time_start9: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 9 start time; hours:minutes, e.g. '0:0'
    )
    forced_time_stop1: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 1 end time; hours:minutes, e.g. '0:0'
    )
    forced_time_stop2: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 2 end time; hours:minutes, e.g. '0:0'
    )
    forced_time_stop3: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 3 end time; hours:minutes, e.g. '0:0'
    )
    forced_time_stop4: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 4 end time; hours:minutes, e.g. '0:0'
    )
    forced_time_stop5: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 5 end time; hours:minutes, e.g. '0:0'
    )
    forced_time_stop6: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 6 end time; hours:minutes, e.g. '0:0'
    )
    forced_time_stop7: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 7 end time; hours:minutes, e.g. '0:0'
    )
    forced_time_stop8: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 8 end time; hours:minutes, e.g. '0:0'
    )
    forced_time_stop9: Union[EmptyStrToNone, ForcedTime] = (
        None  # Time period 9 end time; hours:minutes, e.g. '0:0'
    )
    frequency_high_limit: Union[EmptyStrToNone, float] = (
        None  # Mains frequency upper limit, e.g. 50.099998474121094
    )
    frequency_low_limit: Union[EmptyStrToNone, float] = (
        None  # Mains frequency lower limit, e.g. 47.650001525878906
    )
    gen_charge_enable: Union[EmptyStrToNone, int] = None  # e.g. 0
    gen_ctrl: Union[EmptyStrToNone, int] = None  # e.g. 0
    gen_rated_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    last_update_time: Union[EmptyStrToNone, GrowattTime] = (
        None  # e.g. {'date': 12, 'day': 2, 'hours': 16, 'minutes': 39, 'month': 3, 'seconds': 23, 'time': 1649752763000, 'timezoneOffset': -480, 'year': 122}
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. '2025-02-26 21:09:12'
    )
    lcd_language: Union[EmptyStrToNone, int] = None  # Language settings, e.g. 1
    limit_device: Union[EmptyStrToNone, float] = None  # Sensor selection, e.g. -1
    loading_rate: Union[EmptyStrToNone, float] = None  # loading rate, e.g. 20
    maintain_mode_request: Union[EmptyStrToNone, int] = None  # e.g. 0
    maintain_mode_start_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    max_allow_curr: Union[EmptyStrToNone, float] = None  # e.g. 0
    on_grid_discharge_stop_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    on_grid_mode: Union[EmptyStrToNone, int] = None  # e.g. -1
    on_grid_status: Union[EmptyStrToNone, int] = None  # e.g. -1
    on_off: Union[EmptyStrToNone, int] = None  # On/Off (1=on; 0=off), e.g. 1
    over_fre_drop_point: Union[EmptyStrToNone, float] = (
        None  # Over frequency drop point, e.g. 50.20000076293945
    )
    over_fre_lo_red_delay_time: Union[EmptyStrToNone, float] = (
        None  # Over frequency load reduction delay time, e.g. 0
    )
    over_fre_lo_red_slope: Union[EmptyStrToNone, float] = (
        None  # Over frequency derating slope, e.g. 40
    )
    peak_shaving_enable: Union[EmptyStrToNone, float] = None  # e.g. 0
    pf: Union[EmptyStrToNone, float] = None  # power factor, e.g. 0.8899999856948853
    pf_model: Union[EmptyStrToNone, float] = None  # PF model, e.g. 0
    pf_sys_year: Union[EmptyStrToNone, str] = None  # e.g. ''
    pflinep1_lp: Union[EmptyStrToNone, float] = (
        None  # PF limit line point 1 load percentage, e.g. 255
    )
    pflinep1_pf: Union[EmptyStrToNone, float] = (
        None  # PF limit line point 1 power factor, e.g. 1
    )
    pflinep2_lp: Union[EmptyStrToNone, float] = (
        None  # PF limit line point 2 load percentage, e.g. 255
    )
    pflinep2_pf: Union[EmptyStrToNone, float] = (
        None  # PF limit line point 2 power factor, e.g. 1
    )
    pflinep3_lp: Union[EmptyStrToNone, float] = (
        None  # PF limit line point 3 load percentage, e.g. 255
    )
    pflinep3_pf: Union[EmptyStrToNone, float] = (
        None  # PF limit line point 3 power factor, e.g. 1
    )
    pflinep4_lp: Union[EmptyStrToNone, float] = (
        None  # PF limit line point 4 load percentage, e.g. 255
    )
    pflinep4_pf: Union[EmptyStrToNone, float] = (
        None  # PF limit line point 4 power factor, e.g. 1
    )
    power_down_enable: Union[EmptyStrToNone, int] = None  # e.g. 0
    pre_pto: Union[EmptyStrToNone, float] = None  # e.g. 0
    prot_enable: Union[EmptyStrToNone, int] = None  # e.g. 0
    pu_enable: Union[EmptyStrToNone, int] = None  # e.g. 0
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, bool] = (
        None  # Whether to store commands, e.g. 0
    )
    pv_grid_frequency_high: Union[EmptyStrToNone, float] = None  # e.g. ''
    pv_grid_frequency_low: Union[EmptyStrToNone, float] = None  # e.g. ''
    pv_grid_voltage_high: Union[EmptyStrToNone, float] = None  # e.g. ''
    pv_grid_voltage_low: Union[EmptyStrToNone, float] = None  # e.g. ''
    q_percent_max: Union[EmptyStrToNone, float] = (
        None  # Q(V) reactive power percentage (Qmax of Q(V) curve), e.g. 43
    )
    qv_h1: Union[EmptyStrToNone, float] = (
        None  # Q(V) Cut into low voltage QV-H1, e.g. 236.89999389648438
    )
    qv_h2: Union[EmptyStrToNone, float] = (
        None  # Q(V) cut into high voltage QV-H2, e.g. 246.10000610351562
    )
    qv_l1: Union[EmptyStrToNone, float] = (
        None  # Q(V) cut out high voltage QV-L1, e.g. 223.10000610351562
    )
    qv_l2: Union[EmptyStrToNone, float] = (
        None  # Q(V) cut out low voltage QV-L2, e.g. 213.89999389648438
    )
    reactive_rate: Union[EmptyStrToNone, float] = None  # reactive power, e.g. 0
    region: Union[EmptyStrToNone, int] = None  # e.g. 0
    restart_loading_rate: Union[EmptyStrToNone, float] = (
        None  # restart loading rate, e.g. 20
    )
    rrcr_enable: Union[EmptyStrToNone, float] = None  # e.g. 0
    safety_correspond_num: Union[EmptyStrToNone, float] = None  # e.g. 0
    safety_num: Union[EmptyStrToNone, float] = None  # e.g. ''
    season1_month_time: Union[EmptyStrToNone, str] = (
        None  # Season 1 (month parameter_is enabled), e.g. '0_0_0'
    )
    season1_time1: Union[EmptyStrToNone, str] = (
        None  # Season 1 time period 1 (mode_week_start_end_time period_enable), e.g. '0_0_0_0_0_0_0'
    )
    season1_time2: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season1_time3: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season1_time4: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season1_time5: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season1_time6: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season1_time7: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season1_time8: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season1_time9: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season2_month_time: Union[EmptyStrToNone, str] = (
        None  # Season 2 (month parameter_is enabled), e.g. '0_0_0'
    )
    season2_time1: Union[EmptyStrToNone, str] = (
        None  # Season 2 time period 1 (mode_week_start_end_time period_enable), e.g. '0_0_0_0_0_0_0'
    )
    season2_time2: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season2_time3: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season2_time4: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season2_time5: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season2_time6: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season2_time7: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season2_time8: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season2_time9: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season3_month_time: Union[EmptyStrToNone, str] = (
        None  # Season 3 (month parameter_is enabled), e.g. '0_0_0'
    )
    season3_time1: Union[EmptyStrToNone, str] = (
        None  # Season 3 time period 1 (mode_week_start_end_time period_enable), e.g. '0_0_0_0_0_0_0'
    )
    season3_time2: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season3_time3: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season3_time4: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season3_time5: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season3_time6: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season3_time7: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season3_time8: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season3_time9: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season4_month_time: Union[EmptyStrToNone, str] = (
        None  # Season 4 (month parameter_is enabled), e.g. '0_0_0'
    )
    season4_time1: Union[EmptyStrToNone, str] = (
        None  # Season 4 time period 1 (mode_week_start_end_time period_enable), e.g. '0_0_0_0_0_0_0'
    )
    season4_time2: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season4_time3: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season4_time4: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season4_time5: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season4_time6: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season4_time7: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season4_time8: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    season4_time9: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    serial_num: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    show_peak_shaving: Union[EmptyStrToNone, int] = None  # e.g. 0
    special1_month_time: Union[EmptyStrToNone, str] = (
        None  # Special day 1 (date parameter_is enabled), e.g. '0_0_0'
    )
    special1_time1: Union[EmptyStrToNone, str] = (
        None  # Special day 1 time period 1 (mode_start_end time period_enable or not), e.g. '0_0_0_0_0_0'
    )
    special1_time2: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special1_time3: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special1_time4: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special1_time5: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special1_time6: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special1_time7: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special1_time8: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special1_time9: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special2_month_time: Union[EmptyStrToNone, str] = (
        None  # Special day 2 (date parameter_is enabled), e.g. '0_0_0'
    )
    special2_time1: Union[EmptyStrToNone, str] = (
        None  # Special day 2 time period 1 (mode_start_end time period_enable or not), e.g. '0_0_0_0_0_0'
    )
    special2_time2: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special2_time3: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special2_time4: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special2_time5: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special2_time6: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special2_time7: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special2_time8: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    special2_time9: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0'
    syn_enable: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_time: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. '2025-02-26 14:09:08'
    )
    sys_time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. '2025-02-26 14:09:08'
    )
    time1_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time2_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time3_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time4_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time5_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time6_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time7_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time8_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time9_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    tlx_ac_discharge_frequency: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_ac_discharge_voltage: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_backflow_default_power: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_cc_current: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_cv_voltage: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_dry_contact_enable: Union[EmptyStrToNone, int] = None  # e.g. ''
    tlx_dry_contact_off_power: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_dry_contact_power: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_exter_comm_off_griden: Union[EmptyStrToNone, str] = None  # e.g. ''
    tlx_lcd_language: Union[EmptyStrToNone, int] = None  # e.g. ''
    tlx_limit_device: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_off_grid_enable: Union[EmptyStrToNone, int] = None  # e.g. ''
    tlx_on_off: Union[EmptyStrToNone, int] = None  # e.g. ''
    tlx_pf: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_pflinep1_lp: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_pflinep1_pf: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_pflinep2_lp: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_pflinep2_pf: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_pflinep3_lp: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_pflinep3_pf: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_pflinep4_lp: Union[EmptyStrToNone, float] = None  # e.g. ''
    tlx_pflinep4_pf: Union[EmptyStrToNone, float] = None  # e.g. ''
    ub_ac_charging_stop_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    ub_peak_shaving_backup_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    us_battery_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_ac_charging_max_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_demand_mgt_down_strm_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_demand_mgt_revse_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_hf_rt2_ee: Union[EmptyStrToNone, float] = (
        None  # Second-order high frequency crossover point @, e.g. 51.5
    )
    uw_hf_rt_ee: Union[EmptyStrToNone, float] = (
        None  # First-order high frequency crossover point @, e.g. 51.5
    )
    uw_hv_rt2_ee: Union[EmptyStrToNone, float] = (
        None  # Second-order high voltage crossover point @, e.g. 287.5
    )
    uw_hv_rt_ee: Union[EmptyStrToNone, float] = (
        None  # First-order high voltage crossing point @, e.g. 287.5
    )
    uw_lf_rt2_ee: Union[EmptyStrToNone, float] = (
        None  # Second-order low frequency crossover point @, e.g. 47.5
    )
    uw_lf_rt_ee: Union[EmptyStrToNone, float] = (
        None  # First-order low frequency crossover point @, e.g. 47.5
    )
    uw_lv_rt2_ee: Union[EmptyStrToNone, float] = (
        None  # Second-order low-voltage crossover point @, e.g. 103.5
    )
    uw_lv_rt_ee: Union[EmptyStrToNone, float] = (
        None  # First-order low voltage crossover point @, e.g. 184
    )
    vbat_start_for_discharge: Union[EmptyStrToNone, float] = (
        None  # Battery discharge lower limit voltage in 0.01V, e.g. 0
    )
    vbat_start_for_charge: Union[EmptyStrToNone, float] = (
        None  # Battery charging upper limit voltage in 0.01V, e.g. 5800 = 58 V
    )
    vbat_stop_for_charge: Union[EmptyStrToNone, float] = (
        None  # Battery charge stop voltage; 0.01V, e.g. 0
    )
    vbat_stop_for_discharge: Union[EmptyStrToNone, float] = (
        None  # Battery discharge stop voltage in 0.01V, e.g. 0
    )
    vbat_warn_clr: Union[EmptyStrToNone, float] = (
        None  # Battery voltage low voltage recovery point in 0.1V, e.g. 0
    )
    vbat_warning: Union[EmptyStrToNone, int] = (
        None  # Battery voltage low voltage alarm point in 0.1V, e.g. 0
    )
    voltage_high_limit: Union[EmptyStrToNone, float] = (
        None  # Mains voltage upper limit, e.g. 253
    )
    voltage_low_limit: Union[EmptyStrToNone, float] = (
        None  # Mains voltage lower limit, e.g. 195.5
    )
    w_charge_soc_low_limit: Union[EmptyStrToNone, float] = (
        None  # Load priority mode charging SOC stop value (register 1041) in %, e.g. 100
    )
    w_discharge_soc_low_limit: Union[EmptyStrToNone, float] = (
        None  # Load priority mode discharge SOC stop value in %, e.g. 5
    )
    win_mode_end_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    win_mode_flag: Union[EmptyStrToNone, int] = None  # e.g. 0
    win_mode_off_grid_discharge_stop_soc: Union[EmptyStrToNone, float] = None  # e.g. 10
    win_mode_on_grid_discharge_stop_soc: Union[EmptyStrToNone, float] = None  # e.g. 10
    win_mode_start_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    year_month_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    year_time1: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    year_time2: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    year_time3: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    year_time4: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    year_time5: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    year_time6: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    year_time7: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    year_time8: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'
    year_time9: Union[EmptyStrToNone, str] = None  # e.g. '0_0_0_0_0_0_0'


class MinSettings(ApiResponse):
    data: Union[EmptyStrToNone, MinTlxSettingsData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the energy storage machine, e.g. "ZT00100001"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Min setting read ####################################################################################################


class MinSettingRead(ApiResponse):
    data: Union[EmptyStrToNone, str] = None  # current setting / register value


# #####################################################################################################################
# Min setting write ###################################################################################################


class MinSettingWrite(ApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# #####################################################################################################################
# Max details #########################################################################################################


def _max_detail_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "tree_id": "treeID",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxDetailData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_detail_data_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. 'FDCJQ00003'
    big_device: Union[EmptyStrToNone, bool] = None  # alias, e.g. False
    children: List[Any]  # e.g. []
    communication_version: Union[EmptyStrToNone, str] = (
        None  # Communication version number, e.g. 'GJAA-0003'
    )
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The serial number of the collector, e.g. 'VC51030322020001'
    )
    e_today: Union[EmptyStrToNone, float] = (
        None  # Today’s power generation, e.g. 0  # DEPRECATED
    )
    e_total: Union[EmptyStrToNone, float] = (
        None  # Total Power Generation, e.g. 0  # DEPRECATED
    )
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'GJ1.0'
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = (
        None  # Internal version number, e.g. 'GJAA03xx'
    )
    last_update_time: Union[EmptyStrToNone, GrowattTime] = (
        None  # Last update time, e.g. {'date': 12, 'day': 2, 'hours': 16, 'minutes': 46, 'month': 3, 'seconds': 22, 'time': 1649753182000, 'timezoneOffset': -480, 'year': 122}
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. '2022-04-12 16:46:22'
    )
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    location: Union[EmptyStrToNone, str] = None  # address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = (
        None  # Device online status (0: online, 1: disconnected), e.g. True
    )
    model: Union[EmptyStrToNone, int] = None  # model, e.g. 2666130979655057522
    model_text: Union[EmptyStrToNone, str] = (
        None  # model, e.g. 'S25B00D00T00P0FU01M0072'
    )
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_VC51030322020001_22'
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plantname: Union[EmptyStrToNone, str] = None  # e.g. ''
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'port_name'
    power: Union[EmptyStrToNone, float] = None  # Current power, e.g. 0
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'FDCJQ00003'
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: waiting, 1: self-check, 3: failure, 4: upgrade, 5, 6, 7, 8: normal mode), e.g. 0
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'tlx.status.operating'
    tcp_server_ip: Union[EmptyStrToNone, str] = (
        None  # Server address, e.g. '47.107.154.111'
    )
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_FDCJQ00003'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ''


class MaxDetails(ApiResponse):
    data: Union[EmptyStrToNone, MaxDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the energy storage machine, e.g. "ZT00100001"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Max energy overview #################################################################################################


def _growatt_time_calendar_timezone_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "dst_savings": "DSTSavings",
        "id": "ID",
    }
    return override.get(snake, to_camel(snake=snake))


class GrowattTimeCalendarTimeZone(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_growatt_time_calendar_timezone_to_camel,
    )

    dirty: Union[EmptyStrToNone, bool] = None  # e.g. false
    display_name: Union[EmptyStrToNone, str] = None  # e.g. "China Standard Time"
    dst_savings: Union[EmptyStrToNone, int] = None  # e.g. 0
    id: Union[EmptyStrToNone, str] = None  # e.g. "Asia/Shanghai"
    last_rule_instance: Union[EmptyStrToNone, str] = None  # e.g. null
    raw_offset: Union[EmptyStrToNone, int] = None  # e.g. 28800000


class GrowattTimeCalendar(ApiModel):
    minimal_days_in_first_week: Union[EmptyStrToNone, int] = None  # e.g. 1
    week_year: Union[EmptyStrToNone, int] = None  # e.g. 2018
    time: Union[EmptyStrToNone, GrowattTime] = None
    weeks_in_week_year: Union[EmptyStrToNone, int] = None  # e.g. 52
    gregorian_change: Union[EmptyStrToNone, GrowattTime] = None
    time_zone: Union[EmptyStrToNone, GrowattTimeCalendarTimeZone] = None
    time_in_millis: Union[EmptyStrToNone, int] = None  # e.g. 1544670232000
    lenient: Union[EmptyStrToNone, bool] = None  # e.g. true
    first_day_of_week: Union[EmptyStrToNone, int] = None  # e.g. 1
    week_date_supported: Union[EmptyStrToNone, bool] = None


def _max_energy_overview_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "comp_har_ir": "compharir",
        "comp_har_is": "compharis",
        "comp_har_it": "compharit",
        "comp_qr": "compqr",
        "comp_qs": "compqs",
        "comp_qt": "compqt",
        "ct_har_ir": "ctharir",
        "ct_har_is": "ctharis",
        "ct_har_it": "ctharit",
        "ct_ir": "ctir",
        "ct_is": "ctis",
        "ct_it": "ctit",
        "ct_qr": "ctqr",
        "ct_qs": "ctqs",
        "ct_qt": "ctqt",
        "datalogger_sn": "dataLogSn",
        "real_op_percent": "realOPPercent",
        "str_unbalance": "strUnblance",
        "w_pid_fault_value": "wPIDFaultValue",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxEnergyOverviewBasic(ApiModel):
    """
    energy() returns full set of parameters -> MinEnergyOverviewFull
    energy_history() returns reduced set of parameters -> MinEnergyOverviewBasic
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_energy_overview_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    apf_status: Union[EmptyStrToNone, float] = None  # APF/SVG status, e.g. 0
    apf_status_text: Union[EmptyStrToNone, str] = None  # e.g. 'None'
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    comp_har_ir: Union[EmptyStrToNone, int] = (
        None  # R phase compensation harmonic content, e.g. 0
    )
    comp_har_is: Union[EmptyStrToNone, int] = (
        None  # S phase compensation harmonic content, e.g. 0
    )
    comp_har_it: Union[EmptyStrToNone, int] = (
        None  # T phase compensation harmonic content, e.g. 0
    )
    comp_qr: Union[EmptyStrToNone, int] = (
        None  # R phase compensation reactive power, e.g. 0
    )
    comp_qs: Union[EmptyStrToNone, int] = (
        None  # S phase compensation reactive power, e.g. 0
    )
    comp_qt: Union[EmptyStrToNone, int] = (
        None  # T phase compensation reactive power, e.g. 0
    )
    ct_har_ir: Union[EmptyStrToNone, int] = (
        None  # R phase CT side harmonic content, e.g. 0
    )
    ct_har_is: Union[EmptyStrToNone, int] = (
        None  # S phase CT side harmonic content, e.g. 0
    )
    ct_har_it: Union[EmptyStrToNone, int] = (
        None  # T phase CT side harmonic content, e.g. 0
    )
    ct_ir: Union[EmptyStrToNone, int] = None  # R phase CT side current, e.g. 0
    ct_is: Union[EmptyStrToNone, int] = None  # S phase CT side current, e.g. 0
    ct_it: Union[EmptyStrToNone, int] = None  # T phase CT side current, e.g. 0
    ct_qr: Union[EmptyStrToNone, int] = None  # R phase CT side reactive power, e.g. 0
    ct_qs: Union[EmptyStrToNone, int] = None  # S phase CT side reactive power, e.g. 0
    ct_qt: Union[EmptyStrToNone, int] = None  # T phase CT side electric power, e.g. 0
    current_string1: Union[EmptyStrToNone, float] = None  # String current 1, e.g. 0
    current_string10: Union[EmptyStrToNone, float] = None  # String current 10, e.g. 0
    current_string11: Union[EmptyStrToNone, float] = None  # String current 11, e.g. 0
    current_string12: Union[EmptyStrToNone, float] = None  # String current 12, e.g. 0
    current_string13: Union[EmptyStrToNone, float] = None  # String current 13, e.g. 0
    current_string14: Union[EmptyStrToNone, float] = None  # String current 14, e.g. 0
    current_string15: Union[EmptyStrToNone, float] = None  # String current 15, e.g. 0
    current_string16: Union[EmptyStrToNone, float] = None  # String current 16, e.g. 0
    current_string2: Union[EmptyStrToNone, float] = None  # String current 2, e.g. 0
    current_string3: Union[EmptyStrToNone, float] = None  # String current 3, e.g. 0
    current_string4: Union[EmptyStrToNone, float] = None  # String current 4, e.g. 0
    current_string5: Union[EmptyStrToNone, float] = None  # String current 5, e.g. 0
    current_string6: Union[EmptyStrToNone, float] = None  # String current 6, e.g. 0
    current_string7: Union[EmptyStrToNone, float] = None  # String current 7, e.g. 0
    current_string8: Union[EmptyStrToNone, float] = None  # String current 8, e.g. 0
    current_string9: Union[EmptyStrToNone, float] = None  # String current 9, e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'QMN0000000000000'
    day: Union[EmptyStrToNone, str] = None  # e.g. ''
    debug1: Union[EmptyStrToNone, str] = None  # e.g. '160, 0, 0, 0, 324, 0, 0, 0'
    debug2: Union[EmptyStrToNone, str] = None  # e.g. '0,0,0,0,0,0,0,0'
    derating_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    e_rac_today: Union[EmptyStrToNone, float] = (
        None  # Reactive power of the day kWh, e.g. 0
    )
    e_rac_total: Union[EmptyStrToNone, float] = None  # Total reactive power kWh, e.g. 0
    eac_today: Union[EmptyStrToNone, float] = None  # e.g. 21.600000381469727
    eac_total: Union[EmptyStrToNone, float] = None  # e.g. 1859.5
    epv1_today: Union[EmptyStrToNone, float] = None  # e.g. 13.199999809265137
    epv1_total: Union[EmptyStrToNone, float] = None  # e.g. 926.6
    epv2_today: Union[EmptyStrToNone, float] = None  # e.g. 8.199999809265137
    epv2_total: Union[EmptyStrToNone, float] = None  # e.g. 906.4
    epv3_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv3_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv4_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv4_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv5_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv5_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv6_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv6_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv7_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv7_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv8_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv8_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 50.0099983215332
    fault_code1: Union[EmptyStrToNone, int] = None  # e.g. 2
    fault_code2: Union[EmptyStrToNone, int] = None  # e.g. 0
    fault_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    fault_value: Union[EmptyStrToNone, int] = None  # e.g. 3
    gfci: Union[EmptyStrToNone, float] = None  # e.g. 78
    i_pid_pvape: Union[EmptyStrToNone, float] = None  # pid current 1 (A), e.g. 0
    i_pid_pvbpe: Union[EmptyStrToNone, float] = None  # pid current 2 (A), e.g. 0
    i_pid_pvcpe: Union[EmptyStrToNone, float] = None  # pid current 3 (A), e.g. 0
    i_pid_pvdpe: Union[EmptyStrToNone, float] = None  # pid current 4 (A), e.g. 0
    i_pid_pvepe: Union[EmptyStrToNone, float] = None  # pid current 5 (A), e.g. 0
    i_pid_pvfpe: Union[EmptyStrToNone, float] = None  # pid current 6 (A), e.g. 0
    i_pid_pvgpe: Union[EmptyStrToNone, float] = None  # pid current 7 (A), e.g. 0
    i_pid_pvhpe: Union[EmptyStrToNone, float] = None  # pid current 8 (A), e.g. 0
    iacr: Union[EmptyStrToNone, float] = None  # e.g. 0
    iacs: Union[EmptyStrToNone, float] = None  # e.g. 0
    iact: Union[EmptyStrToNone, float] = None  # e.g. 0
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    ipm_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv1: Union[EmptyStrToNone, float] = (
        None  # PV1 input current, e.g. 5.800000190734863
    )
    ipv2: Union[EmptyStrToNone, float] = (
        None  # PV2 input current, e.g. 6.099999904632568
    )
    ipv3: Union[EmptyStrToNone, float] = None  # PV3 input current, e.g. 0
    ipv4: Union[EmptyStrToNone, float] = None  # PV4 input current, e.g. 0
    ipv5: Union[EmptyStrToNone, float] = None  # PV4 input current, e.g. 0
    ipv6: Union[EmptyStrToNone, float] = None  # PV4 input current, e.g. 0
    ipv7: Union[EmptyStrToNone, float] = None  # PV4 input current, e.g. 0
    ipv8: Union[EmptyStrToNone, float] = None  # PV4 input current, e.g. 0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    max_bean: Union[EmptyStrToNone, Any] = None
    n_bus_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    op_fullwatt: Union[EmptyStrToNone, float] = None  # e.g. 0
    operating_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    p_bus_voltage: Union[EmptyStrToNone, float] = None  # e.g. 367
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 2503.8
    pacr: Union[EmptyStrToNone, float] = None  # e.g. 0
    pacs: Union[EmptyStrToNone, float] = None  # e.g. 0
    pact: Union[EmptyStrToNone, float] = None  # e.g. 0
    pf: Union[EmptyStrToNone, float] = None  # e.g. 0.08100000023841858
    pid_bus: Union[EmptyStrToNone, int] = None
    pid_fault_code: Union[EmptyStrToNone, int] = None
    pid_status_text: Union[EmptyStrToNone, str] = None
    power_today: Union[EmptyStrToNone, float] = None
    power_total: Union[EmptyStrToNone, float] = None
    ppv: Union[EmptyStrToNone, float] = None  # PV input power, e.g. 1058
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power, e.g. 1058
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power, e.g. 1058
    ppv3: Union[EmptyStrToNone, float] = None  # PV3 input power, e.g. 0
    ppv4: Union[EmptyStrToNone, float] = None  # PV4 input power, e.g. 0
    pv_iso: Union[EmptyStrToNone, float] = None  # Insulation resistance
    r_dci: Union[EmptyStrToNone, float] = None  # R-phase DC component
    rac: Union[EmptyStrToNone, float] = None  # Reactive power W
    real_op_percent: Union[EmptyStrToNone, float] = None  # e.g. 50
    s_dci: Union[EmptyStrToNone, float] = None  # S-phase DC component
    serial_num: Union[EmptyStrToNone, str] = None  # e.g. 'BNE9A5100D'
    status: Union[EmptyStrToNone, int] = (
        None  # Min Status (0: waiting, 1: normal, 2: fault), e.g. 1
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Normal'
    str_Break: Union[EmptyStrToNone, int] = None  # The string is not connected
    str_Fault: Union[EmptyStrToNone, int] = None  # String error
    strUnblance: Union[EmptyStrToNone, int] = None  # Uneven string flow
    str_unmatch: Union[EmptyStrToNone, int] = None  # The string does not match
    temperature: Union[EmptyStrToNone, float] = (
        None  # AMTemp1(°C), e.g. 47.79999923706055
    )
    temperature2: Union[EmptyStrToNone, float] = None  # INVTemp(°C), e.g. 0
    temperature3: Union[EmptyStrToNone, float] = None  # BTTemp(°C), e.g. 0
    temperature4: Union[EmptyStrToNone, float] = None  # OUTTemp(°C), e.g. 0
    temperature5: Union[EmptyStrToNone, float] = (
        None  # AMTemp2(°C), e.g. 51.70000076293945
    )
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-09 14:52:39'
    time_total: Union[EmptyStrToNone, float] = (
        None  # Total running time, e.g. 1625146.9
    )
    vac_rs: Union[EmptyStrToNone, float] = None  # RS line voltage, e.g. 239.5
    vac_st: Union[EmptyStrToNone, float] = None  # ST line voltage, e.g. 0
    vac_tr: Union[EmptyStrToNone, float] = None  # TR line voltage, e.g. 0
    vacr: Union[EmptyStrToNone, float] = None  # R phase voltage (V), e.g. 239.5
    vacs: Union[EmptyStrToNone, float] = None  # S phase voltage (V), e.g. 239.5
    vact: Union[EmptyStrToNone, float] = None  # T phase voltage (V), e.g. 239.5
    v_pid_pvape: Union[EmptyStrToNone, float] = None  # pid voltage 1 (V), e.g. 239.5
    v_pid_pvbpe: Union[EmptyStrToNone, float] = None
    v_pid_pvcpe: Union[EmptyStrToNone, float] = None
    v_pid_pvdpe: Union[EmptyStrToNone, float] = None
    v_pid_pvepe: Union[EmptyStrToNone, float] = None
    v_pid_pvfpe: Union[EmptyStrToNone, float] = None
    v_pid_pvgpe: Union[EmptyStrToNone, float] = None
    v_pid_pvhpe: Union[EmptyStrToNone, float] = None
    vpv1: Union[EmptyStrToNone, float] = None  # PV1 input voltage, e.g. 0
    vpv2: Union[EmptyStrToNone, float] = None
    vpv3: Union[EmptyStrToNone, float] = None
    vpv4: Union[EmptyStrToNone, float] = None
    vpv5: Union[EmptyStrToNone, float] = None
    vpv6: Union[EmptyStrToNone, float] = None
    vpv7: Union[EmptyStrToNone, float] = None
    vpv8: Union[EmptyStrToNone, float] = None
    w_pid_fault_value: Union[EmptyStrToNone, int] = None
    w_string_status_value: Union[EmptyStrToNone, int] = None
    warn_bit: Union[EmptyStrToNone, int] = None
    warn_code: Union[EmptyStrToNone, int] = None  # e.g. 220
    warn_code1: Union[EmptyStrToNone, int] = None
    warning_value1: Union[EmptyStrToNone, int] = None
    warning_value2: Union[EmptyStrToNone, int] = None
    warning_value3: Union[EmptyStrToNone, int] = None
    with_time: Union[EmptyStrToNone, bool] = (
        None  # Whether the data sent has its own time, e.g. False
    )


class MaxEnergyOverviewFull(MaxEnergyOverviewBasic):
    """
    energy() returns full set of parameters -> MinEnergyOverviewFull
    energy_history() returns reduced set of parameters -> MinEnergyOverviewBasic
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_energy_overview_data_to_camel,
    )
    # TODO put here items not in Basic View
    pass


def _max_energy_overview_to_camel(snake: str) -> str:
    override = {
        "device_sn": "max_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxEnergyOverview(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_energy_overview_to_camel,
    )

    data: Union[EmptyStrToNone, MaxEnergyOverviewFull] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the inverter, e.g. "ZT00100001"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Min energy overview multiple ########################################################################################


class MinEnergyOverviewMultipleItem(ApiModel):
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the inverter, e.g. "ZT00100001"
    )
    data: Union[EmptyStrToNone, MaxEnergyOverviewFull] = None


class MinEnergyOverviewMultiple(ApiResponse):
    data: List[MinEnergyOverviewMultipleItem] = None
    page_num: Union[EmptyStrToNone, int] = None  # Page number, e.g. 1


# #####################################################################################################################
# Min energy history ##################################################################################################


def _min_energy_history_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "tlx_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class MinEnergyHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_min_energy_history_data_to_camel,
    )

    count: int  # Total Records
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the inverter, e.g. "ZT00100001"
    )
    datas: List[MaxEnergyOverviewBasic]


class MinEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, MinEnergyHistoryData] = None


# #####################################################################################################################
# Max alarms ##########################################################################################################


class MaxAlarm(ApiModel):
    alarm_code: Union[EmptyStrToNone, int] = None  # alarm code, e.g. 25
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    end_time: Union[EmptyStrToNone, datetime.datetime] = (
        None  # Alarm start time, e.g. "2019-03-09 09:55:55.0"
    )
    start_time: Union[EmptyStrToNone, datetime.datetime] = (
        None  # Alarm end time, e.g. "2019-03-09 09:55:55.0"
    )
    alarm_message: Union[EmptyStrToNone, str] = (
        None  # alarm information, e.g. "No utility."
    )


def _max_alarms_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "tlx_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxAlarmsData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_alarms_data_to_camel,
    )

    count: int  # Total Records
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    alarms: List[MaxAlarm]


class MaxAlarms(ApiResponse):
    data: Union[EmptyStrToNone, MaxAlarmsData] = None
