import datetime
from typing import List, Union, Any, Optional, Annotated, TypeAlias

from pydantic import ConfigDict, BeforeValidator
from pydantic.alias_generators import to_camel

from pydantic_models.api_model import (
    NewApiResponse,
    ApiModel,
    EmptyStrToNone,
)


# !!! added NULL handling
def parse_forced_time(value: Optional[str] = None):
    """support 0:0 for 00:00"""
    if value and value.strip() and value != "null":
        try:
            return datetime.datetime.strptime(value, "%H:%M").time()
        except Exception as e:
            raise ValueError(str(e))
    else:
        return None


ForcedTime: TypeAlias = Annotated[Union[datetime.time, None], BeforeValidator(parse_forced_time)]

# #####################################################################################################################
# Device list #########################################################################################################


def _device_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "datalogSn",
    }
    return override.get(snake, to_camel(snake=snake))


class DeviceDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_device_data_to_camel,
    )

    create_date: Union[EmptyStrToNone, datetime.datetime] = None  # Date Added, e.g. '2024-11-30 17:37:26'
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Collector Serial Number, e.g. 'QMN000BZP3N6U09K'
    device_sn: Union[EmptyStrToNone, str] = None  # Device Serial Number, e.g. 'BZP3N6U09K'
    device_type: Union[EmptyStrToNone, str] = None  # Device Type, e.g. 'min'


class DeviceListDataV4(ApiModel):
    count: Union[EmptyStrToNone, int] = None  # Device Count, e.g. 1
    data: List[DeviceDataV4] = []
    last_pager: Union[EmptyStrToNone, bool] = None  # e.g. True
    not_pager: Union[EmptyStrToNone, bool] = None  # e.g. False
    other: Union[EmptyStrToNone, Any] = None  # e.g. None
    pages: Union[EmptyStrToNone, int] = None  # e.g. 1
    page_size: Union[EmptyStrToNone, int] = None  # e.g. 100
    start_count: Union[EmptyStrToNone, int] = None  # e.g. 0


class DeviceListV4(NewApiResponse):
    data: Union[EmptyStrToNone, DeviceListDataV4] = None


# #####################################################################################################################
# Device details ######################################################################################################


def _inverter_details_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "dataLogSn",
        "group_id": "groupID",
        "optimizer_list": "optimezerList",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "tree_id": "treeID",
        "user_id": "userID",
    }
    return override.get(snake, to_camel(snake=snake))


class InverterDetailDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_inverter_details_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    address: Union[EmptyStrToNone, int] = None  # Address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # Alias, e.g. "HPB3744071"
    big_device: Union[EmptyStrToNone, bool] = None  # e.g. False
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    communication_version: Union[EmptyStrToNone, str] = None  # e.g. None
    create_date: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. null
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Associated data logger serial number, e.g. "JPC2101182"
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    e_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_day_map: Union[EmptyStrToNone, dict] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. "0"
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. "AH1.0"
    group_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    id: Union[EmptyStrToNone, int] = None  # e.g. 7
    img_path: Union[EmptyStrToNone, str] = None  # e.g. "./css/img/status_gray.gif"
    inner_version: Union[EmptyStrToNone, str] = None  # e.g. "ahbb1916"
    inv_set_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    inverter_info_status_css: Union[EmptyStrToNone, str] = None  # e.g. "vsts_table_ash"
    ipm_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    last_update_time: Union[EmptyStrToNone, int] = None  # Last update time, e.g. 1613805596000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. "2021-02-20 15:19:56"
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    load_text: Union[EmptyStrToNone, str] = None  # e.g. "0%"
    location: Union[EmptyStrToNone, str] = None  # Address, e.g. "在这"
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: offline), e.g. True
    model: Union[EmptyStrToNone, int] = None  # e.g. 269545841
    model_text: Union[EmptyStrToNone, str] = None  # e.g. "A1B0D1T0PFU1M7S1"
    nominal_power: Union[EmptyStrToNone, int] = None  # Nominal power, e.g. 6000
    optimizer_list: Union[EmptyStrToNone, Any] = None  # e.g. None
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. "LIST_JPC2101182_0"
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. None
    power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. None
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ""
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. None
    record: Union[EmptyStrToNone, str] = None  # e.g. None
    rf_stick: Union[EmptyStrToNone, str] = None  # e.g. None
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "HPB3744071"
    status: Union[EmptyStrToNone, int] = None  # Device status (0: waiting, 1: normal, 3: fault), e.g. -1
    status_text: Union[EmptyStrToNone, str] = None  # e.g. "inverter.status.lost"
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. "192.168.3.35"
    temperature: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. "HPB3744071"
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. "HPB3744071"
    update_exist: Union[EmptyStrToNone, bool] = None  # e.g. false
    updating: Union[EmptyStrToNone, bool] = None  # e.g. false
    user_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ""


class InverterDetailsDataV4(ApiModel):
    inv: List[InverterDetailDataV4] = None


class InverterDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


def _storage_details_to_camel(snake: str) -> str:
    override = {
        "ac_max_charge_curr": "acmaxChargeCurr",
        "address": "addr",
        "buzzer_en": "buzzerEN",
        "datalogger_sn": "dataLogSn",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "rate_va": "rateVA",
        "tree_id": "treeID",
        "user_id": "userID",
    }
    return override.get(snake, to_camel(snake=snake))


class StorageDetailDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_storage_details_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    ac_in_model: Union[EmptyStrToNone, float] = None  # e.g. 1
    ac_max_charge_curr: Union[EmptyStrToNone, float] = None  # e.g. 30
    address: Union[EmptyStrToNone, int] = None  # Address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # Alias, e.g. "裁床照明+插座+大空调"
    b_light_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_low_to_uti_volt: Union[EmptyStrToNone, float] = None  # e.g. 46.0
    battery_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    battery_undervoltage_cutoff_point: Union[EmptyStrToNone, float] = None  # e.g. 42.0
    bulk_charge_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    buzzer_en: Union[EmptyStrToNone, int] = None  # e.g. 1
    charge_config: Union[EmptyStrToNone, int] = None  # e.g. 0
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. None
    communication_version: Union[EmptyStrToNone, str] = None  # e.g. None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # SN of the data logger associated with the energy storage device, e.g. "DDD0CGA0CF"
    )
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 3
    dtc: Union[EmptyStrToNone, int] = None  # e.g. 20105
    float_charge_volt: Union[EmptyStrToNone, float] = None  # e.g. 54.0
    fw_version: Union[EmptyStrToNone, str] = None  # Firmware version of the energy storage device, e.g. "067.01/068.01"
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Software version, e.g. 'null'
    last_update_time: Union[EmptyStrToNone, int] = None  # Last update time, e.g. 1716979679000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # Last update time, e.g. '2024-05-29 18:47:59'
    )
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    li_battery_protocol_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    location: Union[EmptyStrToNone, str] = None  # Address, e.g. ""
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: Online, 1: Offline), e.g. True
    mains_to_battery_operat_point: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    manual_start_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    max_charge_curr: Union[EmptyStrToNone, float] = None  # e.g. 1000
    model: Union[EmptyStrToNone, int] = None  # e.g. 0
    model_text: Union[EmptyStrToNone, str] = None  # e.g. "A0B0D0T0P0U0M0S0"
    output_config: Union[EmptyStrToNone, float] = None  # e.g. 3
    output_freq_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    output_volt_type: Union[EmptyStrToNone, int] = None  # e.g. 1
    over_load_restart: Union[EmptyStrToNone, float] = None  # e.g. 1
    over_temp_restart: Union[EmptyStrToNone, float] = None  # e.g. 1
    p_charge: Union[EmptyStrToNone, float] = None  # Charging power, e.g. 0.0
    p_discharge: Union[EmptyStrToNone, float] = None  # Discharging power, e.g. 0.0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_DDD0CGA0CF_96'
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. None
    port_name: Union[EmptyStrToNone, str] = None  # e.g. None
    pow_saving_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    pv_model: Union[EmptyStrToNone, int] = None  # e.g. 0
    rate_va: Union[EmptyStrToNone, float] = None  # e.g. 5000
    rate_watt: Union[EmptyStrToNone, float] = None  # e.g. 5000
    record: Union[EmptyStrToNone, str] = None  # e.g. None
    sci_loss_chk_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'JNK1CJM0GR'
    status: Union[EmptyStrToNone, int] = (  # e.g. 5
        # Device status
        # 0: Offline
        # 1: Online
        # 2: Charging
        # 3: Discharging
        # 4: Error
        # 5: Burning
        # 6: Solar Charging
        # 7: Grid Charging
        # 8: Combined Charging (both solar and grid)
        # 9: Combined Charging and Bypass (Grid) Output
        # 10: PV Charging and Bypass (Grid) Output
        # 11: Grid Charging and Bypass (Grid) Output
        # 12: Bypass (Grid) Output
        # 13: Solar Charging and Discharging Simultaneously
        # 14: Grid Charging and Discharging Simultaneously)
        # Shangk:
        # 1: No Output
        # 2: Reserved
        # 3: Discharging
        # 4: Error
        # 5: Burning
        # 6: Solar Charging
        # 7: Grid Charging
        # 8: Combined Charging (both solar and grid)
        # 9: Combined Charging and Bypass (Grid) Output
        # 10: PV Charging and Bypass (Grid) Output
        # 11: Grid Charging and Bypass (Grid) Output
        # 12: Bypass (Grid) Output
        # 13: Solar Charging and Discharging Simultaneously
        None
    )
    status_led1: Union[EmptyStrToNone, bool] = None  # e.g. False
    status_led2: Union[EmptyStrToNone, bool] = None  # e.g. True
    status_led3: Union[EmptyStrToNone, bool] = None  # e.g. True
    status_led4: Union[EmptyStrToNone, bool] = None  # e.g. False
    status_led5: Union[EmptyStrToNone, bool] = None  # e.g. False
    status_led6: Union[EmptyStrToNone, bool] = None  # e.g. True
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'inverter.status.lost'
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-29 07:57',
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. "47.119.28.147"
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_JNK1CJM0GR'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. '裁床照明+插座+大空调',
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. None
    uti_charge_end: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_charge_start: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_out_end: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_out_start: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_bat_type2: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_feed_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_feed_range: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_load_first: Union[EmptyStrToNone, float] = None  # e.g. 0


class StorageDetailsDataV4(ApiModel):
    storage: List[StorageDetailDataV4] = None


class StorageDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, StorageDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


def _sph_details_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "bat_aging_test_step": "bagingTestStep",
        "buck_ups_volt_set": "buckUPSVoltSet",
        "datalogger_sn": "dataLogSn",
        "discharge_power_command": "disChargePowerCommand",
        "off_grid_discharge_soc": "offGridDischargeSOC",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "pv_pf_cmd_memory_state_mix": "pvPfCmdMemoryState",  # avoid name collision
        "pv_pf_cmd_memory_state": "pv_pf_cmd_memory_state",  # avoid name collision
        "tree_id": "treeID",
        "uw_hf_rt2_ee": "uwHFRT2EE",
        "uw_hf_rt_ee": "uwHFRTEE",
        "uw_hf_rt_time_ee": "uwHFRTTimeEE",
        "uw_hf_rt_time2_ee": "uwHFRTTime2EE",
        "uw_hv_rt2_ee": "uwHVRT2EE",
        "uw_hv_rt_ee": "uwHVRTEE",
        "uw_hv_rt_time_ee": "uwHVRTTimeEE",
        "uw_hv_rt_time2_ee": "uwHVRTTime2EE",
        "uw_lf_rt2_ee": "uwLFRT2EE",
        "uw_lf_rt_ee": "uwLFRTEE",
        "uw_lf_rt_time_ee": "uwLFRTTimeEE",
        "uw_lf_rt_time2_ee": "uwLFRTTime2EE",
        "uw_lv_rt2_ee": "uwLVRT2EE",
        "uw_lv_rt3_ee": "uwLVRT3EE",
        "uw_lv_rt_ee": "uwLVRTEE",
        "uw_lv_rt_time2_ee": "uwLVRTTime2EE",
        "uw_lv_rt_time3_ee": "uwLVRTTime3EE",
        "uw_lv_rt_time_ee": "uwLVRTTimeEE",
        "vbat_start_for_charge": "vbatStartforCharge",
        "w_charge_soc_low_limit1": "wchargeSOCLowLimit1",
        "w_charge_soc_low_limit2": "wchargeSOCLowLimit2",
        "w_discharge_soc_low_limit1": "wdisChargeSOCLowLimit1",
        "w_discharge_soc_low_limit2": "wdisChargeSOCLowLimit2",
        "baudrate": "wselectBaudrate",
    }
    return override.get(snake, to_camel(snake=snake))


class SphDetailDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sph_details_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    ac_charge_enable: Union[EmptyStrToNone, bool] = None  # AC Charge Enable, e.g. 1
    active_rate: Union[EmptyStrToNone, int] = None  # Active power, e.g. 100
    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # Alias, e.g. 'OZD0849010'
    back_up_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    backflow_setting: Union[EmptyStrToNone, str] = None  # Anti-Backflow Setting, e.g. None
    bat_aging_test_step: Union[EmptyStrToNone, int] = (
        None  # Battery Self-Test (0: default, 1: charge, 2: discharge), e.g. 0
    )
    bat_first_switch1: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_first_switch2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_first_switch3: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_pack_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_parallel_num: Union[EmptyStrToNone, int] = None  # Number of Battery Parallel, e.g. 0
    bat_serial_num: Union[EmptyStrToNone, str] = None  # e.g. None
    bat_series_num: Union[EmptyStrToNone, int] = None  # Number of Battery Series, e.g. 0
    bat_sys_rate_energy: Union[EmptyStrToNone, float] = None  # e.g. -0.1,
    bat_temp_lower_limit_c: Union[EmptyStrToNone, float] = None  # Battery Charge Lower Temperature Limit, e.g. 110.0
    bat_temp_lower_limit_d: Union[EmptyStrToNone, float] = None  # Battery Discharge Lower Temperature Limit, e.g. 110.0
    bat_temp_upper_limit_c: Union[EmptyStrToNone, float] = None  # Battery Charge Upper Temperature Limit, e.g. 60.0
    bat_temp_upper_limit_d: Union[EmptyStrToNone, float] = None  # Battery Discharge Upper Temperature Limit, e.g. 70.0
    battery_type: Union[EmptyStrToNone, int] = None  # Battery Type Selection, e.g. 1
    bct_adjust: Union[EmptyStrToNone, int] = None  # Sensor adjustment enable, e.g. 0
    bct_mode: Union[EmptyStrToNone, int] = None  # Sensor type (0=cWiredCT, 1=cWirelessCT, 2=METER), e.g. 0
    buck_ups_volt_set: Union[EmptyStrToNone, float] = None  # Off-Grid Voltage, e.g. 0
    buck_ups_fun_en: Union[EmptyStrToNone, bool] = None  # Off-Grid Enable, e.g. 1
    cc_current: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    charge_power_command: Union[EmptyStrToNone, int] = None  # Charge Power Setting, e.g. 100
    charge_time1: Union[EmptyStrToNone, str] = None  # e.g. None
    charge_time2: Union[EmptyStrToNone, str] = None  # e.g. None
    charge_time3: Union[EmptyStrToNone, str] = None  # e.g. None
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    com_address: Union[EmptyStrToNone, int] = None  # Communication Address, e.g. 1
    communication_version: Union[EmptyStrToNone, str] = None  # Communication version number, e.g. 'GJAA-0003'
    country_selected: Union[EmptyStrToNone, int] = None  # Country Selection, e.g. 0
    cv_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # DataLog Serial Number, e.g. 'JAD084800B'
    device_type: Union[EmptyStrToNone, int] = None  # Device Type (0: Mix6k, 1: Mix4-10k), e.g. 0
    discharge_power_command: Union[EmptyStrToNone, int] = None  # Discharge Power Setting, e.g. 100
    discharge_time1: Union[EmptyStrToNone, str] = None  # e.g. None
    discharge_time2: Union[EmptyStrToNone, str] = None  # e.g. None
    discharge_time3: Union[EmptyStrToNone, str] = None  # e.g. None
    dtc: Union[EmptyStrToNone, int] = None  # Device code, e.g. 3501
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    eps_freq_set: Union[EmptyStrToNone, int] = None  # Emergency Power Supply Frequency, e.g. 1
    eps_fun_en: Union[EmptyStrToNone, bool] = None  # Emergency Power Supply Enable, e.g. 1
    eps_volt_set: Union[EmptyStrToNone, int] = None  # Emergency Power Supply Voltage, e.g. 1
    export_limit: Union[EmptyStrToNone, int] = None  # Anti-Backflow Enable, e.g. 0
    export_limit_power_rate: Union[EmptyStrToNone, float] = None  # Anti-Backflow, e.g. 0.0
    failsafe: Union[EmptyStrToNone, int] = None  # e.g. 0
    float_charge_current_limit: Union[EmptyStrToNone, float] = None  # Float Charge Current Limit, e.g. 660.0
    forced_charge_stop_switch1: Union[EmptyStrToNone, bool] = None  # Forced Charge 1 Enable, e.g. 1
    forced_charge_stop_switch2: Union[EmptyStrToNone, bool] = None  # Forced Charge 2 Enable, e.g. 1
    forced_charge_stop_switch3: Union[EmptyStrToNone, bool] = None  # Forced Charge 3 Enable, e.g. 1
    forced_charge_stop_switch4: Union[EmptyStrToNone, bool] = None  # Forced Charge 4 Enable, e.g. 1
    forced_charge_stop_switch5: Union[EmptyStrToNone, bool] = None  # Forced Charge 5 Enable, e.g. 1
    forced_charge_stop_switch6: Union[EmptyStrToNone, bool] = None  # Forced Charge 6 Enable, e.g. 1
    forced_charge_time_start1: Union[EmptyStrToNone, ForcedTime] = None  # Forced Charge Time 1 Start, e.g. '18:0'
    forced_charge_time_start2: Union[EmptyStrToNone, ForcedTime] = None  # Forced Charge Time 2 Start, e.g. '21:30'
    forced_charge_time_start3: Union[EmptyStrToNone, ForcedTime] = None  # Forced Charge Time 3 Start, e.g. '3:0'
    forced_charge_time_start4: Union[EmptyStrToNone, ForcedTime] = None  # Forced Charge Time 4 Start, e.g. '3:0'
    forced_charge_time_start5: Union[EmptyStrToNone, ForcedTime] = None  # Forced Charge Time 5 Start, e.g. '3:0'
    forced_charge_time_start6: Union[EmptyStrToNone, ForcedTime] = None  # Forced Charge Time 6 Start, e.g. '3:0'
    forced_charge_time_stop1: Union[EmptyStrToNone, ForcedTime] = None  # Charge 1 stop time, e.g. '19:30'
    forced_charge_time_stop2: Union[EmptyStrToNone, ForcedTime] = None  # Charge 2 stop time, e.g. '23:0'
    forced_charge_time_stop3: Union[EmptyStrToNone, ForcedTime] = None  # Charge 3 stop time, e.g. '4:30'
    forced_charge_time_stop4: Union[EmptyStrToNone, ForcedTime] = None  # Charge 4 stop time, e.g. '4:30'
    forced_charge_time_stop5: Union[EmptyStrToNone, ForcedTime] = None  # Charge 5 stop time, e.g. '4:30'
    forced_charge_time_stop6: Union[EmptyStrToNone, ForcedTime] = None  # Charge 6 stop time, e.g. '4:30'
    forced_discharge_stop_switch1: Union[EmptyStrToNone, bool] = None  # Forced Discharge 1 Enable, e.g. 1
    forced_discharge_stop_switch2: Union[EmptyStrToNone, bool] = None  # Forced Discharge 2 Enable, e.g. 1
    forced_discharge_stop_switch3: Union[EmptyStrToNone, bool] = None  # Forced Discharge 3 Enable, e.g. 1
    forced_discharge_stop_switch4: Union[EmptyStrToNone, bool] = None  # Forced Discharge 4 Enable, e.g. 1
    forced_discharge_stop_switch5: Union[EmptyStrToNone, bool] = None  # Forced Discharge 5 Enable, e.g. 1
    forced_discharge_stop_switch6: Union[EmptyStrToNone, bool] = None  # Forced Discharge 6 Enable, e.g. 1
    forced_discharge_time_start1: Union[EmptyStrToNone, ForcedTime] = None  # Forced Discharge Time 1 Start, e.g. '0:0'
    forced_discharge_time_start2: Union[EmptyStrToNone, ForcedTime] = None  # Forced Discharge Time 2 Start, e.g. '0:0'
    forced_discharge_time_start3: Union[EmptyStrToNone, ForcedTime] = None  # Forced Discharge Time 3 Start, e.g. '0:0'
    forced_discharge_time_start4: Union[EmptyStrToNone, ForcedTime] = None  # Forced Discharge Time 4 Start, e.g. '0:0'
    forced_discharge_time_start5: Union[EmptyStrToNone, ForcedTime] = None  # Forced Discharge Time 5 Start, e.g. '0:0'
    forced_discharge_time_start6: Union[EmptyStrToNone, ForcedTime] = None  # Forced Discharge Time 6 Start, e.g. '0:0'
    forced_discharge_time_stop1: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 1 stop time, e.g. '0:0'
    forced_discharge_time_stop2: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 2 stop time, e.g. '0:0'
    forced_discharge_time_stop3: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 3 stop time, e.g. '0:0'
    forced_discharge_time_stop4: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 4 stop time, e.g. '0:0'
    forced_discharge_time_stop5: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 5 stop time, e.g. '0:0'
    forced_discharge_time_stop6: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 6 stop time, e.g. '0:0'
    fw_version: Union[EmptyStrToNone, str] = None  # Firmware Version, e.g. 'RA1.0'
    grid_first_switch1: Union[EmptyStrToNone, bool] = None  # e.g. 0
    grid_first_switch2: Union[EmptyStrToNone, bool] = None  # e.g. 0
    grid_first_switch3: Union[EmptyStrToNone, bool] = None  # e.g. 0
    group_id: Union[EmptyStrToNone, int] = None  # Inverter Group, e.g. -1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    in_power: Union[EmptyStrToNone, float] = None  # e.g. 20.0
    inner_version: Union[EmptyStrToNone, str] = None  # Internal Version Number, e.g. 'GJAA03xx'
    inv_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    last_update_time: Union[EmptyStrToNone, int] = None  # Last Update Time, e.g. 1716535653000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-24 15:27:33'
    lcd_language: Union[EmptyStrToNone, int] = None  # LCD Language, e.g. 1
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    load_first_control: Union[EmptyStrToNone, int] = None  # e.g. 0
    load_first_stop_soc_set: Union[EmptyStrToNone, int] = None  # e.g. 0
    location: Union[EmptyStrToNone, str] = None  # Location, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Communication Lost Status, e.g. True
    lv_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    manufacturer: Union[EmptyStrToNone, str] = None  # Manufacturer Code, e.g. 'New Energy'
    mc_version: Union[EmptyStrToNone, str] = None  # e.g. '\x00\x00\x00\x00-0000'
    mix_ac_discharge_frequency: Union[EmptyStrToNone, float] = None  # Off-Grid Frequency, e.g. None
    mix_ac_discharge_voltage: Union[EmptyStrToNone, float] = None  # Off-Grid Voltage, e.g. None
    mix_off_grid_enable: Union[EmptyStrToNone, bool] = None  # Off-Grid Enable, e.g. None
    modbus_version: Union[EmptyStrToNone, int] = None  # MODBUS version, e.g. 305
    model: Union[EmptyStrToNone, int] = None  # Model, e.g. 1159635200000
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'A0B0DBT0PFU2M4S0'
    monitor_version: Union[EmptyStrToNone, str] = None  # e.g. 'null'
    new_sw_version_flag: Union[EmptyStrToNone, int] = None  # e.g. 0
    off_grid_discharge_soc: Union[EmptyStrToNone, int] = None  # e.g. -1
    old_error_flag: Union[EmptyStrToNone, int] = None  # e.g. 0
    on_off: Union[EmptyStrToNone, bool] = None  # Power State (On/Off), e.g. 0
    out_power: Union[EmptyStrToNone, float] = None  # e.g. 20.0
    p_charge: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_discharge: Union[EmptyStrToNone, float] = None  # e.g. 0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_JAD084800B_96'
    pf_sys_year: Union[EmptyStrToNone, str] = None  # Set time, e.g. None
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. None
    pmax: Union[EmptyStrToNone, int] = None  # Rated Power, e.g. 0
    port_name: Union[EmptyStrToNone, str] = (
        None  # Communication Port Information (Type and Address), e.g. 'ShinePano - JAD084800B'
    )
    power_factor: Union[EmptyStrToNone, float] = None  # PF value, e.g. 0.0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. None
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. None
    priority_choose: Union[EmptyStrToNone, int] = None  # Energy Priority Selection, e.g. 1
    pro_pto: Union[EmptyStrToNone, float] = None  # e.g. 0
    pu_enable: Union[EmptyStrToNone, int] = None  # e.g. 0
    pv_active_p_rate: Union[EmptyStrToNone, float] = None  # Set Active Power, e.g. ''
    pv_grid_voltage_high: Union[EmptyStrToNone, float] = None  # Utility Voltage Upper Limit, e.g. ''
    pv_grid_voltage_low: Union[EmptyStrToNone, float] = None  # Utility Voltage Lower Limit, e.g. ''
    pv_on_off: Union[EmptyStrToNone, bool] = None  # Power State (On/Off), e.g. ''
    pv_pf_cmd_memory_state_mix: Union[EmptyStrToNone, bool] = (
        None  # (pvPfCmdMemoryState) Whether the Mix Inverter Stores the Following Commands, e.g. ''
    )
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, bool] = (
        None  # (pv_pf_cmd_memory_state) Set Whether to Store the Following PF Commands, e.g. 1
    )
    pv_power_factor: Union[EmptyStrToNone, float] = None  # Set PF Value, e.g. ''
    pv_reactive_p_rate: Union[EmptyStrToNone, float] = None  # Set Reactive Power, e.g. ''
    pv_reactive_p_rate_two: Union[EmptyStrToNone, float] = None  # Reactive Power (Capacitive/Inductive), e.g. ''
    reactive_delay: Union[EmptyStrToNone, float] = None  # e.g. 150.0
    reactive_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 48.0
    reactive_rate: Union[EmptyStrToNone, int] = None  # Reactive power, e.g. 100
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    region: Union[EmptyStrToNone, int] = None  # e.g. -1
    rrcr_enable: Union[EmptyStrToNone, int] = None  # e.g. 1
    safety: Union[EmptyStrToNone, str] = None  # e.g. '00'
    safety_correspond_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    safety_num: Union[EmptyStrToNone, str] = None  # e.g. '4E'
    safety_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. 'FDCJQ00003'
    sgip_en: Union[EmptyStrToNone, bool] = None  # e.g. 0
    single_export: Union[EmptyStrToNone, int] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = (
        None  # Mix Status (0: Waiting Mode, 1: Self-check Mode, 3: Fault Mode, 4: Upgrading, 5-8: Normal Mode), e.g. 5
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'mix.status.normal'
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # System Time, e.g. '2019-03-05 10:37:29'
    sys_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-24 05:20:52'
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # TCP Server IP Address, e.g. '47.119.173.58'
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_FDCJQ00003'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    under_excited: Union[EmptyStrToNone, int] = None  # Capacitive or Inductive, e.g. 0
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. None
    usp_freq_set: Union[EmptyStrToNone, int] = None  # Off-Grid Frequency, e.g. 0
    uw_grid_watt_delay: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_hf_rt2_ee: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_hf_rt_ee: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_hf_rt_time_ee: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_hf_rt_time2_ee: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_hv_rt2_ee: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_hv_rt_ee: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_hv_rt_time_ee: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_hv_rt_time2_ee: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_lf_rt2_ee: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_lf_rt_ee: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_lf_rt_time_ee: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_lf_rt_time2_ee: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_lv_rt2_ee: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_lv_rt3_ee: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_lv_rt_ee: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_lv_rt_time2_ee: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_lv_rt_time3_ee: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_lv_rt_time_ee: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_nominal_grid_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_reconnect_start_slope: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    v1: Union[EmptyStrToNone, float] = None  # e.g. 122.0
    v2: Union[EmptyStrToNone, float] = None  # e.g. 119.0
    v3: Union[EmptyStrToNone, float] = None  # e.g. 146.0
    v4: Union[EmptyStrToNone, float] = None  # e.g. 143.0
    vbat_start_for_discharge: Union[EmptyStrToNone, float] = None  # Lower limit of battery discharge voltage, e.g. 48.0
    vbat_start_for_charge: Union[EmptyStrToNone, float] = None  # Battery charging upper limit voltage, e.g. 58.0
    vbat_stop_for_charge: Union[EmptyStrToNone, float] = None  # Battery charging stop voltage, e.g. 5.75
    vbat_stop_for_discharge: Union[EmptyStrToNone, float] = None  # Battery discharge stop voltage, e.g. 4.7
    vbat_warn_clr: Union[EmptyStrToNone, float] = None  # Low battery voltage recovery point, e.g. 5.0
    vbat_warning: Union[EmptyStrToNone, float] = None  # Low battery voltage alarm point, e.g. 480.0
    vnormal: Union[EmptyStrToNone, float] = None  # Rated PV Voltage, e.g. 360.0
    voltage_high_limit: Union[EmptyStrToNone, float] = None  # Utility Voltage Upper Limit, e.g. 263.0
    voltage_low_limit: Union[EmptyStrToNone, float] = None  # Utility Voltage Lower Limit, e.g. 186.0
    vpp_open: Union[EmptyStrToNone, float] = None  # e.g. 160
    w_charge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load Priority Mode Charge, e.g. 100
    w_charge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Battery Priority Mode Charge, e.g. 100
    w_discharge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load Priority Mode Discharge, e.g. 100
    w_discharge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Grid Priority Mode Discharge, e.g. 5
    baudrate: Union[EmptyStrToNone, int] = None  # Baud Rate Selection, e.g. 0


class SphDetailsDataV4(ApiModel):
    sph: List[SphDetailDataV4] = None


class SphDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, SphDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


def _max_details_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "tree_id": "treeID",
        "baudrate": "wselectBaudrate",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxDetailDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_details_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    active_rate: Union[EmptyStrToNone, float] = None  # e.g. 0
    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # Alias, e.g. 'FDCJQ00003'
    backflow_default_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    big_device: Union[EmptyStrToNone, bool] = None  # alias, e.g. False
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    communication_version: Union[EmptyStrToNone, str] = None  # Communication version number, e.g. 'GJAA-0003'
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Data logger serial number, e.g. 'VC51030322020001'
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 1
    dtc: Union[EmptyStrToNone, int] = None  # e.g. 5001
    e_today: Union[EmptyStrToNone, float] = None  # Today's generated power at the backend, e.g. 0  # DEPRECATED
    e_total: Union[EmptyStrToNone, float] = None  # Total generated power at the backend, e.g. 0  # DEPRECATED
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    export_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    export_limit_power_rate: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    fac_high: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    fac_low: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    frequency_high_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    frequency_low_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter firmware version, e.g. 'TJ1.0'
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Internal version number, e.g. 'TJAA08020002'
    is_authorize: Union[EmptyStrToNone, bool] = None  # e.g. 0
    is_timing_authorize: Union[EmptyStrToNone, bool] = None  # e.g. 0
    last_update_time: Union[EmptyStrToNone, int] = None  # Last update time, e.g. 1716534733000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-24 15:12:13'
    lcd_language: Union[EmptyStrToNone, int] = None  # e.g. 0
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    location: Union[EmptyStrToNone, str] = None  # Address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: offline), e.g. True
    max_set_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    model: Union[EmptyStrToNone, int] = None  # model, e.g. 720575940631003386
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'S0AB00D00T00P0FU01M00FA'
    normal_power: Union[EmptyStrToNone, float] = None  # Rated power, e.g. 25000
    on_off: Union[EmptyStrToNone, bool] = None  # e.g. 0
    open_authorize: Union[EmptyStrToNone, bool] = None  # e.g. 0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_BLE4BEQ0BW_3'
    permission_switch: Union[EmptyStrToNone, bool] = None  # e.g. 0
    pf: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf_model: Union[EmptyStrToNone, int] = None  # e.g. 0
    pflinep1_lp: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep1_pf: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pflinep2_lp: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep2_pf: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pflinep3_lp: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep3_pf: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pflinep4_lp: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep4_pf: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. None
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'ShinePano - BLE4BEQ0BW'
    power: Union[EmptyStrToNone, float] = None  # Current power, e.g. 0.0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. None
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. None
    pv_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, int] = None  # e.g. 0
    reactive_rate: Union[EmptyStrToNone, float] = None  # e.g. 0
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    remain_day: Union[EmptyStrToNone, float] = None  # e.g. 0
    safety_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'HPJ0BF20FU'
    status: Union[EmptyStrToNone, int] = (  # e.g. 1
        # Device status
        # 0: offline
        # 1: online
        # 2: standby
        # 3: fault
        # others: disconnected
        None
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'max.status.normal'
    str_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. None
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. '47.119.22.101'
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'HPJ0BF20FU'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'HPJ0BF20FU'
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. None
    vac_high: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    vac_low: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    voltage_high_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    voltage_low_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.0


class MaxDetailsDataV4(ApiModel):
    max: List[MaxDetailDataV4] = None


class MaxDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, MaxDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


def _spa_details_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "bat_aging_test_step": "bagingTestStep",
        "buck_ups_volt_set": "buckUPSVoltSet",
        "datalogger_sn": "dataLogSn",
        "discharge_power_command": "disChargePowerCommand",
        "off_grid_discharge_soc": "offGridDischargeSOC",
        "parent_id": "parentID",
        "pf_cmd_memory_state": "pfCMDmemoryState",
        "plant_name": "plantname",
        "tree_id": "treeID",
        "vbat_start_for_charge": "vbatStartforCharge",
        "w_charge_soc_low_limit1": "wchargeSOCLowLimit1",
        "w_charge_soc_low_limit2": "wchargeSOCLowLimit2",
        "w_discharge_soc_low_limit1": "wdisChargeSOCLowLimit1",
        "w_discharge_soc_low_limit2": "wdisChargeSOCLowLimit2",
        "w_load_soc_low_limit1": "wloadSOCLowLimit1",
        "w_load_soc_low_limit2": "wloadSOCLowLimit2",
        "baudrate": "wselectBaudrate",
    }
    return override.get(snake, to_camel(snake=snake))


class SpaDetailDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spa_details_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    ac_charge_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    active_p_rate: Union[EmptyStrToNone, int] = None  # Active Power Setting, e.g. 100
    address: Union[EmptyStrToNone, int] = None  # Inverter Address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # Alias, e.g. 'MTN0H6800E'
    backflow_setting: Union[EmptyStrToNone, str] = None  # Anti-backflow Setting, e.g. None
    bat_aging_test_step: Union[EmptyStrToNone, int] = (
        None  # Battery Self-check (0: default, 1: charge, 2: discharge), e.g. 0
    )
    bat_first_switch1: Union[EmptyStrToNone, int] = None  # Battery Priority Enable Bit 1, e.g. 0
    bat_first_switch2: Union[EmptyStrToNone, int] = None  # Battery Priority Enable Bit 2, e.g. 0
    bat_first_switch3: Union[EmptyStrToNone, int] = None  # Battery Priority Enable Bit 3, e.g. 0
    bat_pack_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_serial_num: Union[EmptyStrToNone, str] = None  # e.g. None
    bat_sys_rate_energy: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bat_temp_lower_limit_c: Union[EmptyStrToNone, float] = None  # Battery Charge Temperature Lower Limit, e.g. 110.0
    bat_temp_lower_limit_d: Union[EmptyStrToNone, float] = None  # Battery Discharge Temperature Lower Limit, e.g. 110.0
    bat_temp_upper_limit_c: Union[EmptyStrToNone, float] = None  # Battery Charge Temperature Upper Limit, e.g. 60.0
    bat_temp_upper_limit_d: Union[EmptyStrToNone, float] = None  # Battery Discharge Temperature Upper Limit, e.g. 70.0
    battery_type: Union[EmptyStrToNone, int] = None  # Battery Type Selection, e.g. 1
    bct_adjust: Union[EmptyStrToNone, int] = None  # Sensor Adjustment Enable, e.g. 0
    bct_mode: Union[EmptyStrToNone, int] = None  # Sensor type (0=cWiredCT, 1=cWirelessCT, 2=METER), e.g. 0
    buck_ups_volt_set: Union[EmptyStrToNone, float] = None  # Off-grid voltage, e.g. 0
    buck_ups_fun_en: Union[EmptyStrToNone, bool] = None  # Off-grid enable, e.g. 1
    charge_power_command: Union[EmptyStrToNone, int] = None  # Charge Power Setting, e.g. 100
    charge_time1: Union[EmptyStrToNone, str] = None  # Charge Time Period 1, e.g. None
    charge_time2: Union[EmptyStrToNone, str] = None  # Charge Time Period 2, e.g. None
    charge_time3: Union[EmptyStrToNone, str] = None  # Charge Time Period 3, e.g. None
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    com_address: Union[EmptyStrToNone, int] = None  # Communication Address, e.g. 1
    communication_version: Union[EmptyStrToNone, str] = None  # Communication Version Number, e.g. 'ZCBC-0006'
    country_selected: Union[EmptyStrToNone, int] = None  # Country Selection, e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'XGD6CMM2VY'
    device_type: Union[EmptyStrToNone, int] = None  # 2
    discharge_power_command: Union[EmptyStrToNone, int] = None  # Discharge Power Setting, e.g. 100
    discharge_time1: Union[EmptyStrToNone, str] = None  # Discharge Time Period 1, e.g. None
    discharge_time2: Union[EmptyStrToNone, str] = None  # Discharge Time Period 2, e.g. None
    discharge_time3: Union[EmptyStrToNone, str] = None  # Discharge Time Period 3, e.g. None
    dtc: Union[EmptyStrToNone, int] = None  # Device Code 43, e.g. 3501
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    eps_freq_set: Union[EmptyStrToNone, int] = None  # Emergency Power Supply Frequency, e.g. 0
    eps_fun_en: Union[EmptyStrToNone, bool] = None  # Emergency Power Supply Enable, e.g. 0
    eps_volt_set: Union[EmptyStrToNone, int] = None  # Emergency Power Supply Voltage, e.g. 0
    equipment_type: Union[EmptyStrToNone, str] = None  # e.g. None
    export_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    export_limit_power_rate: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    failsafe: Union[EmptyStrToNone, int] = None  # e.g. 0
    float_charge_current_limit: Union[EmptyStrToNone, float] = None  # Float Charge Current Limit, e.g. 600.0
    forced_charge_stop_switch4: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_charge_stop_switch5: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_charge_stop_switch6: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_charge_time_start1: Union[EmptyStrToNone, ForcedTime] = None  # Charge 1 start time, e.g. '18:0'
    forced_charge_time_start2: Union[EmptyStrToNone, ForcedTime] = None  # Charge 2 start time, e.g. '21:30'
    forced_charge_time_start3: Union[EmptyStrToNone, ForcedTime] = None  # Charge 3 start time, e.g. '3:0'
    forced_charge_time_start4: Union[EmptyStrToNone, ForcedTime] = None  # Charge 4 start time, e.g. '3:0'
    forced_charge_time_start5: Union[EmptyStrToNone, ForcedTime] = None  # Charge 5 start time, e.g. '3:0'
    forced_charge_time_start6: Union[EmptyStrToNone, ForcedTime] = None  # Charge 6 start time, e.g. '3:0'
    forced_charge_time_stop1: Union[EmptyStrToNone, ForcedTime] = None  # Charge 1 stop time, e.g. '19:30'
    forced_charge_time_stop2: Union[EmptyStrToNone, ForcedTime] = None  # Charge 2 stop time, e.g. '23:0'
    forced_charge_time_stop3: Union[EmptyStrToNone, ForcedTime] = None  # Charge 3 stop time, e.g. '4:30'
    forced_charge_time_stop4: Union[EmptyStrToNone, ForcedTime] = None  # Charge 4 stop time, e.g. '0:0'
    forced_charge_time_stop5: Union[EmptyStrToNone, ForcedTime] = None  # Charge 5 stop time, e.g. '0:0'
    forced_charge_time_stop6: Union[EmptyStrToNone, ForcedTime] = None  # Charge 6 stop time, e.g. '0:0'
    forced_discharge_stop_switch4: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_discharge_stop_switch5: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_discharge_stop_switch6: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_discharge_time_start1: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 1 Start Time, e.g. '0:0'
    forced_discharge_time_start2: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 2 start time, e.g. '0:0'
    forced_discharge_time_start3: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 3 start time, e.g. '0:0'
    forced_discharge_time_start4: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 4 start time, e.g. '0:0'
    forced_discharge_time_start5: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 5 start time, e.g. '0:0'
    forced_discharge_time_start6: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 6 start time, e.g. '0:0'
    forced_discharge_time_stop1: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 1 stop time, e.g. '0:0'
    forced_discharge_time_stop2: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 2 stop time, e.g. '0:0'
    forced_discharge_time_stop3: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 3 stop time, e.g. '0:0'
    forced_discharge_time_stop4: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 4 stop time, e.g. '0:0'
    forced_discharge_time_stop5: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 5 stop time, e.g. '0:0'
    forced_discharge_time_stop6: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 6 stop time, e.g. '0:0'
    fw_version: Union[EmptyStrToNone, str] = None  # Firmware Version, e.g. 'RA1.0'
    grid_first_switch1: Union[EmptyStrToNone, bool] = None  # Grid Priority Enable Bit 1082, e.g. 1
    grid_first_switch2: Union[EmptyStrToNone, bool] = None  # Grid Priority Enable Bit 1085, e.g. 0
    grid_first_switch3: Union[EmptyStrToNone, bool] = None  # Grid Priority Enable Bit 1088, e.g. 0
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Internal Version Number, e.g. 'RBCA050306'
    inv_version: Union[EmptyStrToNone, int] = None  # e.g. 1
    last_update_time: Union[EmptyStrToNone, int] = None  # Last Update Time, e.g. 1716435475000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-12 16:46:22'
    lcd_language: Union[EmptyStrToNone, int] = None  # LCD Language, e.g. 1
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    load_first_start_time1: Union[EmptyStrToNone, ForcedTime] = None  # Load Priority Period 1 Start Time, e.g. '0:0'
    load_first_start_time2: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 2 start time, e.g. '4:30'
    load_first_start_time3: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 3 start time, e.g. 'null'
    load_first_stop_time1: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 1 end time, e.g. '23:59'
    load_first_stop_time2: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 2 end time, e.g. '7:29'
    load_first_stop_time3: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 3 end time, e.g. 'null'
    load_first_switch1: Union[EmptyStrToNone, bool] = None  # Load priority enable bit 1, e.g. 0
    load_first_switch2: Union[EmptyStrToNone, bool] = None  # Load priority enable bit 2, e.g. 0
    load_first_switch3: Union[EmptyStrToNone, bool] = None  # Load priority enable bit 3, e.g. 0
    location: Union[EmptyStrToNone, str] = None  # Location, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Communication Loss Indicator, e.g. True
    manufacturer: Union[EmptyStrToNone, str] = None  # Manufacturer Code, e.g. 'New Energy'
    mc_version: Union[EmptyStrToNone, str] = None  # e.g. '-0000'
    modbus_version: Union[EmptyStrToNone, int] = None  # MODBUS version, e.g. 307
    model: Union[EmptyStrToNone, int] = None  # Model, e.g. 1710134400000
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'A0B1D0T4PFU2M2S0'
    monitor_version: Union[EmptyStrToNone, str] = None  # e.g. 'FFFF-30840'
    new_sw_version_flag: Union[EmptyStrToNone, int] = None  # e.g. 0
    off_grid_discharge_soc: Union[EmptyStrToNone, float] = None  # e.g. 20
    old_error_flag: Union[EmptyStrToNone, int] = None  # e.g.0
    on_off: Union[EmptyStrToNone, bool] = None  # Power On/Off, e.g. 0
    p_charge: Union[EmptyStrToNone, float] = None  # Charge Power, e.g. 0.0
    p_discharge: Union[EmptyStrToNone, float] = None  # Discharge Power, e.g. 0.0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_XGD6CMM2VY_96'
    pf_cmd_memory_state: Union[EmptyStrToNone, int] = None  # PF Command Storage Setting, e.g. 0
    pf_sys_year: Union[EmptyStrToNone, str] = None  # Time Setting, e.g. ''
    plant_id: Union[EmptyStrToNone, int] = None  # Plant ID, e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # Plant Name, e.g. None
    pmax: Union[EmptyStrToNone, int] = None  # Rated power, e.g. 3000
    port_name: Union[EmptyStrToNone, str] = (
        None  # Communication Port Information (Type and Address), e.g. 'ShinePano - XGD6CMM2VY'
    )
    power_factor: Union[EmptyStrToNone, float] = None  # PF Value Setting, e.g. 10000
    power_max: Union[EmptyStrToNone, float] = None  # e.g. None
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. None
    priority_choose: Union[EmptyStrToNone, int] = None  # Energy Priority Selection, e.g. 2
    pro_pto: Union[EmptyStrToNone, float] = None  # e.g. 0
    pv_active_p_rate: Union[EmptyStrToNone, float] = None  # Active Power Setting, e.g. None
    pv_grid_voltage_high: Union[EmptyStrToNone, float] = None  # Grid Voltage Upper Limit, e.g. None
    pv_grid_voltage_low: Union[EmptyStrToNone, float] = None  # Grid Voltage Lower Limit, e.g. None
    pv_on_off: Union[EmptyStrToNone, bool] = None  # Power On/Off, e.g. None
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, bool] = None  # PF Command Storage Setting, e.g. None
    pv_power_factor: Union[EmptyStrToNone, float] = None  # PF Value Setting, e.g. None
    pv_reactive_p_rate: Union[EmptyStrToNone, float] = None  # Reactive Power Setting, e.g. None
    pv_reactive_p_rate_two: Union[EmptyStrToNone, float] = None  # Reactive Power Capacity, e.g. None
    reactive_p_rate: Union[EmptyStrToNone, int] = None  # Reactive Power Setting, e.g. 100
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    region: Union[EmptyStrToNone, int] = None  # e.g. 0
    safety_correspond_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    safety_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. 'MTN0H6800E'
    spa_ac_discharge_frequency: Union[EmptyStrToNone, float] = None  # Off-grid Frequency, e.g. None
    spa_ac_discharge_voltage: Union[EmptyStrToNone, float] = None  # Off-grid Voltage, e.g. None
    spa_off_grid_enable: Union[EmptyStrToNone, bool] = None  # Off-grid Enable, e.g. None
    status: Union[EmptyStrToNone, int] = (  # e.g. -1
        # Spa Status
        # 0: Waiting Mode
        # 1: Self-check Mode
        # 3: Fault Mode
        # 4: Upgrading
        # 5-8: Normal Mode
        None
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'spa.status.lost'
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # System Time, e.g. '2024-05-23 11:34'
    sys_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-23 11:34:33'
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # TCP Server IP Address, e.g. '127.0.0.1'
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_MTN0H6800E'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'MTN0H6800E'
    under_excited: Union[EmptyStrToNone, int] = None  # e.g. 0
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    ups_freq_set: Union[EmptyStrToNone, float] = None  # Off-grid frequency, e.g. 0
    user_name: Union[EmptyStrToNone, str] = None  # e.g. None
    vac_high: Union[EmptyStrToNone, float] = None  # Grid Voltage Upper Limit, e.g. 264.5
    vac_low: Union[EmptyStrToNone, float] = None  # Grid Voltage Lower Limit, e.g. 184
    vbat_start_for_discharge: Union[EmptyStrToNone, float] = None  # Battery Discharge Lower Limit Voltage, e.g. 48
    vbat_start_for_charge: Union[EmptyStrToNone, float] = None  # Battery Charge Upper Limit Voltage, e.g. 58
    vbat_stop_for_charge: Union[EmptyStrToNone, float] = None  # Battery Charge Stop Voltage, e.g. 5.75
    vbat_stop_for_discharge: Union[EmptyStrToNone, float] = (
        None  # Battery Discharge Stop Voltage, e.g. 4.699999809265137
    )
    vbat_warn_clr: Union[EmptyStrToNone, float] = None  # Battery Low Voltage Recovery Point, e.g. 5
    vbat_warning: Union[EmptyStrToNone, float] = None  # Battery Low Voltage Warning Point, e.g. 480
    vpp_open: Union[EmptyStrToNone, float] = None  # e.g. 0
    w_charge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load Priority Mode Charge, e.g. 100
    w_charge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Battery Priority Mode Charge, e.g. 100
    w_discharge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load Priority Mode Discharge, e.g. 100
    w_discharge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Grid Priority Mode Discharge, e.g. 5
    w_load_soc_low_limit1: Union[EmptyStrToNone, int] = None  # e.g. 0
    w_load_soc_low_limit2: Union[EmptyStrToNone, int] = None  # e.g. 0
    baudrate: Union[EmptyStrToNone, int] = None  # Baud Rate Selection, e.g. 0


class SpaDetailsDataV4(ApiModel):
    spa: List[SpaDetailDataV4] = None


class SpaDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, SpaDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


def _min_details_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "bat_aging_test_step": "bagingTestStep",
        "bdc_auth_version": "bdcAuthversion",
        "datalogger_sn": "dataLogSn",
        "optimizer_list": "optimezerList",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "tlx_set_bean": "tlxSetbean",
        "tracker_model": "trakerModel",
        "tree_id": "treeID",
        "baudrate": "wselectBaudrate",
    }
    return override.get(snake, to_camel(snake=snake))


class MinDetailDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_min_details_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. 'AFE494403F'
    bat_aging_test_step: Union[EmptyStrToNone, int] = (
        None  # Battery self-test (0: Default, 1: Charge, 2: Discharge), e.g. 0
    )
    bat_parallel_num: Union[EmptyStrToNone, int] = None  # Number of battery parallels, e.g. 0
    bat_series_num: Union[EmptyStrToNone, int] = None  # Number of battery series, e.g. 0
    bat_sys_energy: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bat_temp_lower_limit_c: Union[EmptyStrToNone, float] = (
        None  # Battery charging temperature lower limit in 0.1°C, e.g. 0.0
    )
    bat_temp_lower_limit_d: Union[EmptyStrToNone, float] = (
        None  # Battery discharge temperature lower limit in 0.1°C,e.g. 0.0
    )
    bat_temp_upper_limit_c: Union[EmptyStrToNone, float] = (
        None  # Battery charging temperature upper limit in 0.1°C,e.g. 0.0
    )
    bat_temp_upper_limit_d: Union[EmptyStrToNone, float] = (
        None  # Battery discharge temperature upper limit in 0.1°C,e.g. 0.0
    )
    battery_type: Union[EmptyStrToNone, int] = None  # Battery Type (0:Lithium, 1:Lead-acid, 2:other), e.g. 0
    bct_adjust: Union[EmptyStrToNone, int] = None  # Sensor adjustment enable (0: Disable, 1: Enable), e.g. 0
    bct_mode: Union[EmptyStrToNone, int] = None  # Sensor class type (0:cWiredCT, 1:cWirelessCT, 2:METER), e.g. 0
    bcu_version: Union[EmptyStrToNone, str] = None  # e.g. ''
    bdc1_model: Union[EmptyStrToNone, str] = None  # BDC1 model, e.g. '0'
    bdc1_sn: Union[EmptyStrToNone, str] = None  # BDC1 serial number, e.g. 'XXXXXXXXXXXXXXXX'
    bdc1_version: Union[EmptyStrToNone, str] = None  # BDC1 version, e.g. '\x00\x00\x00\x00-0'
    bdc_auth_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc_mode: Union[EmptyStrToNone, int] = None  # e.g. -1/0
    bms_communication_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_software_version: Union[EmptyStrToNone, str] = None  # e.g. ''
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    com_address: Union[EmptyStrToNone, int] = None  # Communication address 30, e.g. 1
    communication_version: Union[EmptyStrToNone, str] = None  # Communication version number, e.g. 'ZAAA-0004'
    country_selected: Union[EmptyStrToNone, int] = None  # Country selection, e.g. 1
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Data logger serial number, e.g. 'BLE094404C'
    device_type: Union[EmptyStrToNone, int] = None  # (0:Inverter, 1:Mix), e.g. 5
    dtc: Union[EmptyStrToNone, int] = None  # Device code, e.g. 5203
    e_today: Union[EmptyStrToNone, float] = None  # Today’s power generation, e.g. 0  # DEPRECATED
    e_total: Union[EmptyStrToNone, float] = None  # Total Power Generation, e.g. 0  # DEPRECATED
    energy_day_map: Union[EmptyStrToNone, dict] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'AK1.0'
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    hw_version: Union[EmptyStrToNone, str] = None  # e.g. 'null'/'0'
    id: Union[EmptyStrToNone, int] = None  # e.g. 1627
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Internal version number, e.g. 'AKAA0501'
    last_update_time: Union[EmptyStrToNone, int] = None  # Last update time, e.g. 1716535759000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-24 15:29:19'
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    li_battery_fw_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    li_battery_manufacturers: Union[EmptyStrToNone, int] = None  # e.g. 0
    location: Union[EmptyStrToNone, str] = None  # address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: disconnected), e.g. True
    manufacturer: Union[EmptyStrToNone, str] = None  # Manufacturer code 34-41, e.g. 'PV Inverter'
    modbus_version: Union[EmptyStrToNone, int] = None  # Modbus version, e.g. 307
    model: Union[EmptyStrToNone, int] = None  # Model, e.g. 2666130979655057522
    model_text: Union[EmptyStrToNone, str] = None  # Model, e.g. 'S25B00D00T00P0FU01M0072'
    monitor_version: Union[EmptyStrToNone, str] = None  # e.g. 'null'
    mppt: Union[EmptyStrToNone, float] = None  # MPPT voltage, e.g. 513.0
    optimizer_list: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    p_charge: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    p_discharge: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_BLE094404C_22'
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    pmax: Union[EmptyStrToNone, int] = None  # Rated power (maybe in 0.1VA), e.g. 11400 for 1140.0 W
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'ShinePano - BLE094404C'
    power: Union[EmptyStrToNone, float] = None  # Current power, e.g. 0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. ''
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. None
    priority_choose: Union[EmptyStrToNone, int] = None  # Energy priority selection (0:Load, 1:Battery, 2:Grid), e.g. 0
    pv_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    restart_time: Union[EmptyStrToNone, int] = None  # Reconnection countdown, e.g. 65
    safety_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'AFE494403F'
    start_time: Union[EmptyStrToNone, int] = None  # Startup countdown, e.g. 65
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: waiting, 1: self-check, 3: failure, 4: upgrade, 5, 6, 7, 8: normal mode), e.g. 0
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'tlx.status.operating'
    str_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_time: Union[EmptyStrToNone, str] = None  # System time, e.g. ''
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. '47.119.160.91'
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0 / 1.0
    tlx_set_bean: Union[EmptyStrToNone, Any] = None  # FYI: in API v1, we see MinTlxSettingsData here
    tracker_model: Union[EmptyStrToNone, int] = None  # Task model, e.g. 0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_AFE494403F'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'AFE494403F'
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    vbat_start_for_discharge: Union[EmptyStrToNone, float] = (
        None  # Battery discharge lower limit voltage in 0.01V, e.g. 0
    )
    vbat_stop_for_charge: Union[EmptyStrToNone, float] = None  # Battery charge stop voltage in 0.01V, e.g. 0
    vbat_stop_for_discharge: Union[EmptyStrToNone, float] = None  # Battery discharge stop voltage in 0.01V, e.g. 0
    vbat_warn_clr: Union[EmptyStrToNone, float] = None  # Battery low voltage recovery point in 0.1V, e.g. 0
    vbat_warning: Union[EmptyStrToNone, float] = None  # Battery low voltage warning point in 0.1V, e.g. 0
    vnormal: Union[EmptyStrToNone, float] = None  # Rated PV voltage in 0.1V, e.g. 280 for 28.0 V
    vpp_open: Union[EmptyStrToNone, float] = None  # e.g. 0
    baudrate: Union[EmptyStrToNone, int] = None  # Baud Rate Selection, e.g. 0


class MinDetailsDataV4(ApiModel):
    min: List[MinDetailDataV4] = None


class MinDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, MinDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------
# WIT: TODO: what's the matching v1 device_type for WIT???


def _wit_details_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "communication_version": "comVersion",
        "datalogger_sn": "dataLogSn",
        "parent_id": "parentID",
        "line_n_disconnect_enable": "lineNdisconnectEnable",
        "power_ud_forced_enable": "powerUDForcedEnable",
        "safety_function": "saftyFunc",
        "uw_1th_bat_charge_limit": "uw1thBatChgLimit",
        "uw_1th_bat_discharge_limit": "uw1thBatDisChgLimit",
        "uw_2th_bat_cap": "uw2thBatCap",
        "uw_2th_bat_charge_limit": "uw2thBatChgLimit",
        "uw_2th_bat_discharge_limit": "uw2thBatDisChgLimit",
        "uw_2th_bat_end_of_vol": "uw2thBatEndOfVol",
        "uw_2th_bat_max_charge_curr": "uw2thBatMaxChgCurr",
        "uw_2th_bat_max_charge_vol": "uw2thBatMaxChgVol",
        "uw_2th_bat_max_discharge_curr": "uw2thBatMaxDisChgCurr",
        "uw_3th_bat_cap": "uw3thBatCap",
        "uw_3th_bat_charge_limit": "uw3thBatChgLimit",
        "uw_3th_bat_discharge_limit": "uw3thBatDisChgLimit",
        "uw_3th_bat_end_of_vol": "uw3thBatEndOfVol",
        "uw_3th_bat_max_charge_curr": "uw3thBatMaxChgCurr",
        "uw_3th_bat_max_charge_vol": "uw3thBatMaxChgVol",
        "uw_3th_bat_max_discharge_curr": "uw3thBatMaxDisChgCurr",
        "uw_ac_charge_enable": "uwACChargeEnable",
        "uw_ac_charge_power_rate": "uwACChargePowerRate",
        "uw_a_couple_end_soc": "uwACoupleEndSOC",
        "uw_a_couple_start_soc": "uwACoupleStartSOC",
        "uw_bat_discharge_stop_soc": "uwBatDisChargeStopSoc",
        "uw_bat_discharge_stop_soc2": "uwBatDisChargeStopSoc2",
        "uw_bat_discharge_stop_soc3": "uwBatDisChargeStopSoc3",
        "uw_bat_max_discharge_current": "uwBatMaxDisChargeCurrent",
        "uw_batt_eod_vol": "uwBattEODVol",
        "uw_demand_mange_charge_power_limit": "uwDemandMangeChgPowerLimit",
        "uw_demand_mange_discharge_power_limit": "uwDemandMangeDisChgPowerLimit",
        "uw_disconnect_phase_mode": "uwDisConnectPhaseMode",
        "w_power_restart_slope_ee": "wPowerRestartSlopeEE",
        "tree_id": "treeID",
        "baudrate": "wselectBaudrate",
    }
    return override.get(snake, to_camel(snake=snake))


class WitDetailDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_wit_details_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    ac_stop_charging_soc: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    active_rate: Union[EmptyStrToNone, float] = None  # Active power, 50
    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 5
    alias: Union[EmptyStrToNone, str] = None  # Alias, e.g. '0ZFN00R23ZBF0002'
    anti_backflow_failure_power_percent: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    anti_backflow_failure_time: Union[EmptyStrToNone, float] = None  # e.g. -1
    anti_backflow_flag: Union[EmptyStrToNone, bool] = None  # e.g. 0
    ats_version: Union[EmptyStrToNone, str] = None  # e.g. ''
    b_bak_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_bak_bat2_soc: Union[EmptyStrToNone, float] = None  # e.g. -1
    b_bak_bat3_soc: Union[EmptyStrToNone, float] = None  # e.g. -1
    bat_connection_type: Union[EmptyStrToNone, int] = None  # e.g. 1
    bat_connection_type2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_connection_type3: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_serial_num1: Union[EmptyStrToNone, str] = None  # e.g. '0WZN00R23ZB0000C'
    bat_serial_num2: Union[EmptyStrToNone, str] = None  # e.g. ''
    bat_serial_num3: Union[EmptyStrToNone, str] = None  # e.g. ''
    bat_serial_num4: Union[EmptyStrToNone, str] = None  # e.g. ''
    bat_serial_num5: Union[EmptyStrToNone, str] = None  # e.g. ''
    bat_sleep_wake_up1: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_sleep_wake_up2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_sleep_wake_up3: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms1_enable: Union[EmptyStrToNone, bool] = None  # e.g. 1
    bms2_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    bms3_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    charge_soc_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. None
    com_address: Union[EmptyStrToNone, int] = None  # Communication address 30, e.g. 2
    com_name: Union[EmptyStrToNone, str] = None  # e.g. 'null'
    communication_version: Union[EmptyStrToNone, str] = None  # Communication version number, e.g. 'ZBea-0037'
    country_selected: Union[EmptyStrToNone, int] = None  # country selected, e.g. 1
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Data Logger Serial Number, e.g. 'TTN0D9E01P'
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 218
    discharge_soc_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    drms_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    drms_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    dtc: Union[EmptyStrToNone, int] = None  # Device code, e.g. 5600
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_day_map: Union[EmptyStrToNone, dict] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    fac_high: Union[EmptyStrToNone, float] = None  # e.g. 525.0
    fac_high2: Union[EmptyStrToNone, float] = None  # e.g. 50.5
    fac_high3: Union[EmptyStrToNone, float] = None  # e.g. 50.5
    fac_low: Union[EmptyStrToNone, float] = None  # e.g. 475.0
    fac_low2: Union[EmptyStrToNone, float] = None  # e.g. 47.5
    fac_low3: Union[EmptyStrToNone, float] = None  # e.g. 47.5
    forced_stop_switch1: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_stop_switch2: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_stop_switch3: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_stop_switch4: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_stop_switch5: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_stop_switch6: Union[EmptyStrToNone, bool] = None  # e.g. 0
    forced_time_start1: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '21:0'
    forced_time_start2: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    forced_time_start3: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    forced_time_start4: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    forced_time_start5: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    forced_time_start6: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    forced_time_stop1: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '22:0'
    forced_time_stop2: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    forced_time_stop3: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    forced_time_stop4: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    forced_time_stop5: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    forced_time_stop6: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    freq_change_enable: Union[EmptyStrToNone, int] = None  # e.g. -1
    freq_high_limit: Union[EmptyStrToNone, float] = None  # e.g. 50.5
    freq_low_limit: Union[EmptyStrToNone, float] = None  # e.g. 47.5
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'TO1.0'
    grid_meter_enable: Union[EmptyStrToNone, bool] = None  # e.g. 1
    grid_reconnection_time: Union[EmptyStrToNone, int] = None  # e.g. 300
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    heat_up_time: Union[EmptyStrToNone, float] = None  # e.g. -1
    hl_voltage_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    id: Union[EmptyStrToNone, int] = None  # e.g. 1627
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    last_update_time: Union[EmptyStrToNone, int] = None  # Last update time, e.g. 1716963248000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-29 14:14:08'
    lcd_language: Union[EmptyStrToNone, int] = None  # Language settings, e.g. 1
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    line_n_disconnect_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    load_red_rate: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    location: Union[EmptyStrToNone, str] = None  # address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: disconnected), e.g. True
    max_spontaneous_selfuse: Union[EmptyStrToNone, float] = None  # e.g. 0
    modbus_version: Union[EmptyStrToNone, int] = None  # Modbus version, e.g. 305
    model: Union[EmptyStrToNone, int] = None  # model, e.g. 2377905207708287976
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'S21B00D04T30P0FU01M03E8'
    module1: Union[EmptyStrToNone, int] = None  # e.g. 0
    module2: Union[EmptyStrToNone, int] = None  # e.g. 0
    module3: Union[EmptyStrToNone, int] = None  # e.g. 0
    module4: Union[EmptyStrToNone, int] = None  # e.g. 0
    oil_charge_power_limit: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    oil_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    oil_rated_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    on_off: Union[EmptyStrToNone, bool] = None  # On/Off (1=on; 0=off), 1
    over_fre_drop_point: Union[EmptyStrToNone, float] = None  # Over frequency drop point, e.g. 50.3
    over_fre_lo_red_delay_time: Union[EmptyStrToNone, float] = (
        None  # Over frequency load reduction delay time, e.g. 0.0
    )
    over_fre_lo_red_res_time: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    over_fre_lo_red_slope: Union[EmptyStrToNone, float] = None  # Over frequency derating slope, e.g. 50
    parallel_enable: Union[EmptyStrToNone, bool] = None  # e.g. 1
    param_protect_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_BLE094404C_22'
    pf_level1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf_level2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf_level3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf_level4: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf_level5: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf_level6: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf_level7: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf_level8: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf_model: Union[EmptyStrToNone, float] = None  # PF model, e.g. 0
    pflinep1_lp: Union[EmptyStrToNone, float] = None  # PF limit line point 1 load percentage, e.g. 0
    pflinep1_pf: Union[EmptyStrToNone, float] = None  # PF limit line point 1 power factor, e.g. -1.0
    pflinep2_lp: Union[EmptyStrToNone, float] = None  # PF limit line point 2 load percentage, e.g. 0
    pflinep2_pf: Union[EmptyStrToNone, float] = None  # PF limit line point 2 power factor, e.g. -1.0
    pflinep3_lp: Union[EmptyStrToNone, float] = None  # PF limit line point 3 load percentage, e.g. 0
    pflinep3_pf: Union[EmptyStrToNone, float] = None  # PF limit line point 3 power factor, e.g. -1.0
    pflinep4_lp: Union[EmptyStrToNone, float] = None  # PF limit line point 4 load percentage, e.g. 0
    pflinep4_pf: Union[EmptyStrToNone, float] = None  # PF limit line point 4 power factor, e.g. -1.0
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. None
    pmax: Union[EmptyStrToNone, int] = None  # Rated power, e.g. 100000
    pmax_level1: Union[EmptyStrToNone, float] = None  # e.g. 0
    pmax_level2: Union[EmptyStrToNone, float] = None  # e.g. 0
    pmax_level3: Union[EmptyStrToNone, float] = None  # e.g. 0
    pmax_level4: Union[EmptyStrToNone, float] = None  # e.g. 0
    pmax_level5: Union[EmptyStrToNone, float] = None  # e.g. 0
    pmax_level6: Union[EmptyStrToNone, float] = None  # e.g. 0
    pmax_level7: Union[EmptyStrToNone, float] = None  # e.g. 0
    pmax_level8: Union[EmptyStrToNone, float] = None  # e.g. 0
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'ShinePano - TTN0D9E01P'
    power_factor: Union[EmptyStrToNone, float] = None  # e.g. 1.0
    power_imbalance_control_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. None
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. None
    power_ud_forced_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    pu_enable: Union[EmptyStrToNone, int] = None  # e.g. 0
    pv_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, bool] = None  # Whether to store commands, e.g. 0
    reactive_output_priority: Union[EmptyStrToNone, int] = None  # e.g. 0
    reactive_rate: Union[EmptyStrToNone, float] = None  # reactive power, e.g. 0
    reactive_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    restart_time: Union[EmptyStrToNone, int] = None  # Reconnection countdown, e.g. 10
    rrcr_enable: Union[EmptyStrToNone, float] = None  # e.g. 0
    safety_correspond_num: Union[EmptyStrToNone, float] = None  # e.g. 0
    safety_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    safety_function: Union[EmptyStrToNone, int] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. '0ZFN00R23ZBF0002'
    single_export: Union[EmptyStrToNone, int] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = None  # Device Status, e.g. 0
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'wit.status.operating'
    str_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    svg_function: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_optical_storage_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_time: Union[EmptyStrToNone, str] = None  # System time, e.g. ''
    sys_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-29 14:00:25'
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. '120.25.191.20'
    time1_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time1_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    time2_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time2_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    time3_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time3_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    time4_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time4_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    time5_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time5_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    time6_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time6_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    time_start: Union[EmptyStrToNone, int] = None  # e.g. 30
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_0ZFN00R23ZBF0002'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. '0ZFN00R23ZBF0002'
    underfreq_load_delay_time: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    underfreq_load_enable: Union[EmptyStrToNone, int] = None  # e.g. -1
    underfreq_load_point: Union[EmptyStrToNone, float] = None  # e.g. 49.8
    underfreq_load_res_time: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    underfreq_load_slope: Union[EmptyStrToNone, int] = None  # e.g. 400
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. None
    uw_1th_bat_charge_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_1th_bat_discharge_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.1
    uw_2th_bat_cap: Union[EmptyStrToNone, float] = None  # e.g. 10000
    uw_2th_bat_charge_limit: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_2th_bat_discharge_limit: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_2th_bat_end_of_vol: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_2th_bat_max_charge_curr: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_2th_bat_max_charge_vol: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_2th_bat_max_discharge_curr: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_3th_bat_cap: Union[EmptyStrToNone, float] = None  # e.g. 10000
    uw_3th_bat_charge_limit: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_3th_bat_discharge_limit: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_3th_bat_end_of_vol: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_3th_bat_max_charge_curr: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_3th_bat_max_charge_vol: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_3th_bat_max_discharge_curr: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    uw_ac_charge_enable: Union[EmptyStrToNone, bool] = None  # e.g. 1
    uw_ac_charge_power_rate: Union[EmptyStrToNone, float] = None  # e.g. 100
    uw_a_couple_enable: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_a_couple_end_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_a_couple_start_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_anti_backflow: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_bat_cap: Union[EmptyStrToNone, float] = None  # e.g. 100
    uw_bat_charge_stop_soc: Union[EmptyStrToNone, float] = None  # e.g. 100
    uw_bat_charge_stop_soc2: Union[EmptyStrToNone, float] = None  # e.g. -1
    uw_bat_charge_stop_soc3: Union[EmptyStrToNone, float] = None  # e.g. -1
    uw_bat_cnn_way: Union[EmptyStrToNone, float] = None  # e.g. 10000
    uw_bat_discharge_stop_soc: Union[EmptyStrToNone, float] = None  # e.g. 10
    uw_bat_discharge_stop_soc2: Union[EmptyStrToNone, float] = None  # e.g. -1
    uw_bat_discharge_stop_soc3: Union[EmptyStrToNone, float] = None  # e.g. -1
    uw_bat_enable1: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_bat_enable2: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_bat_enable3: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_bat_max_charge_current: Union[EmptyStrToNone, float] = None  # e.g. 140.0
    uw_bat_max_discharge_current: Union[EmptyStrToNone, float] = None  # e.g. 140.0
    uw_batt_eod_vol: Union[EmptyStrToNone, float] = None  # e.g. 678.0
    uw_batt_max_charge_vol: Union[EmptyStrToNone, float] = None  # e.g. 854.0
    uw_batt_type1: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_batt_type2: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_batt_type3: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_connect_phase_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_demand_mange_charge_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_demand_mange_discharge_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_demand_mange_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_dg_start_soc: Union[EmptyStrToNone, float] = None  # e.g. 20
    uw_dg_stop_soc: Union[EmptyStrToNone, float] = None  # e.g. 30
    uw_disconnect_phase_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_gen_port_dev_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_gen_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_load_pv_inverter: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_off_grid_enable: Union[EmptyStrToNone, bool] = None  # e.g. 1
    uw_off_grid_freq: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_off_grid_soc1: Union[EmptyStrToNone, float] = None  # e.g. 5
    uw_off_grid_soc2: Union[EmptyStrToNone, float] = None  # e.g. -1
    uw_off_grid_soc3: Union[EmptyStrToNone, float] = None  # e.g. -1
    uw_off_grid_vol: Union[EmptyStrToNone, float] = None  # e.g. 1.0
    uw_on_off_change_manual_mode: Union[EmptyStrToNone, int] = None  # e.g. 1
    uw_on_off_change_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_on_off_grid_set: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_pcs_type: Union[EmptyStrToNone, int] = None  # e.g. 1
    v_bak_soc_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    vac_high: Union[EmptyStrToNone, float] = None  # e.g. 458.1
    vac_high2: Union[EmptyStrToNone, float] = None  # e.g. 537.8
    vac_high3: Union[EmptyStrToNone, float] = None  # e.g. 537.8
    vac_low: Union[EmptyStrToNone, float] = None  # e.g. 276.0
    vac_low2: Union[EmptyStrToNone, float] = None  # e.g. 199.1
    vac_low3: Union[EmptyStrToNone, float] = None  # e.g. 199.1
    version: Union[EmptyStrToNone, str] = None  # e.g. 'TOaa181390'
    vnormal: Union[EmptyStrToNone, float] = None  # Nominal PV voltage, e.g. 2.0
    voltage_high_limit: Union[EmptyStrToNone, float] = None  # Mains voltage upper limit, e.g. 456.4
    voltage_low_limit: Union[EmptyStrToNone, float] = None  # Mains voltage lower limit, e.g. 277.7
    vpv_start: Union[EmptyStrToNone, float] = None  # e.g. 250.0
    w_anti_backflow_meter_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    w_power_restart_slope_ee: Union[EmptyStrToNone, float] = None  # e.g. 50.0
    w_power_start_slope: Union[EmptyStrToNone, float] = None  # e.g. 50.0
    wide_voltage_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    baudrate: Union[EmptyStrToNone, int] = None  # Baud Rate Selection, e.g. 0


class WitDetailsDataV4(ApiModel):
    wit: List[WitDetailDataV4] = None


class WitDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, WitDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


def _sphs_details_to_camel(snake: str) -> str:
    # TODO copied from SPH
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "parent_id": "parentID",
        # "tree_id": "treeID",
        # "uw_hf_rt2_ee": "uwHFRT2EE",
        # "uw_hf_rt_ee": "uwHFRTEE",
        # "uw_hf_rt_time_ee": "uwHFRTTimeEE",
        # "uw_hf_rt_time2_ee": "uwHFRTTime2EE",
        # "uw_hv_rt2_ee": "uwHVRT2EE",
        # "uw_hv_rt_ee": "uwHVRTEE",
        # "uw_hv_rt_time_ee": "uwHVRTTimeEE",
        # "uw_hv_rt_time2_ee": "uwHVRTTime2EE",
        # "uw_lf_rt2_ee": "uwLFRT2EE",
        # "uw_lf_rt_ee": "uwLFRTEE",
        # "uw_lf_rt_time_ee": "uwLFRTTimeEE",
        # "uw_lf_rt_time2_ee": "uwLFRTTime2EE",
        # "uw_lv_rt2_ee": "uwLVRT2EE",
        # "uw_lv_rt3_ee": "uwLVRT3EE",
        # "uw_lv_rt_ee": "uwLVRTEE",
        # "uw_lv_rt_time2_ee": "uwLVRTTime2EE",
        # "uw_lv_rt_time3_ee": "uwLVRTTime3EE",
        # "uw_lv_rt_time_ee": "uwLVRTTimeEE",
        # "vbat_start_for_charge": "vbatStartforCharge",
        # "w_charge_soc_low_limit1": "wchargeSOCLowLimit1",
        # "w_charge_soc_low_limit2": "wchargeSOCLowLimit2",
        # "w_discharge_soc_low_limit1": "wdisChargeSOCLowLimit1",
        # "w_discharge_soc_low_limit2": "wdisChargeSOCLowLimit2",
        # "baudrate": "wselectBaudrate",
    }
    return override.get(snake, to_camel(snake=snake))


class SphsDetailDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sphs_details_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    active_rate: Union[EmptyStrToNone, int] = None  # Active power, e.g. 100
    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # Alias, e.g. 'AGP0N1600D'
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    com_address: Union[EmptyStrToNone, int] = None  # Communication Address, e.g. 1
    communication_version: Union[EmptyStrToNone, str] = None  # Communication version number, e.g. 'SKaa-0001'
    country_selected: Union[EmptyStrToNone, int] = None  # Country Selection, e.g. 1
    datalogger_sn: Union[EmptyStrToNone, str] = None  # DataLog Serial Number, e.g. 'VC51010323468084'
    device_type: Union[EmptyStrToNone, int] = None  # Device Type, e.g. 280
    dtc: Union[EmptyStrToNone, int] = None  # Device code, e.g. 21200
    e_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    export_limit: Union[EmptyStrToNone, int] = None  # Anti-Backflow Enable, e.g. 1
    export_limit_power_rate: Union[EmptyStrToNone, float] = None  # Anti-Backflow, e.g. 100.0
    failsafe: Union[EmptyStrToNone, int] = None  # e.g. 0
    freq_high_limit: Union[EmptyStrToNone, float] = None  # e.g. 60.5
    freq_low_limit: Union[EmptyStrToNone, float] = None  # e.g. 59.3
    fw_version: Union[EmptyStrToNone, str] = None  # e.g. 'UL2.0'
    group_id: Union[EmptyStrToNone, int] = None  # Inverter Group, e.g. -1
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    last_update_time: Union[EmptyStrToNone, int] = None  # Last Update Time, e.g. 1716963973000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-29 14:26:13'
    lcd_language: Union[EmptyStrToNone, int] = None  # LCD Language, e.g. 1
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    location: Union[EmptyStrToNone, str] = None  # Location, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Communication Lost Status, e.g. False
    manufacturer: Union[EmptyStrToNone, str] = None  # Manufacturer Code, e.g. 'www.sacolar.com'
    modbus_version: Union[EmptyStrToNone, int] = None  # MODBUS version, e.g. 207
    model: Union[EmptyStrToNone, int] = None  # Model, e.g. 0
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'S00B00D00T00P00U00M0000'
    p_charge: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    p_discharge: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_VC51010323468084_260'
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. None
    pmax: Union[EmptyStrToNone, int] = None  # Rated Power, e.g. 15000
    port_name: Union[EmptyStrToNone, str] = (
        None  # Communication Port Information (Type and Address), e.g. 'ShinePano - VC51010323468084'
    )
    power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. None
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. None
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, bool] = None  # Set Whether to Store the Following PF Commands, e.g. 0
    reactive_output_priority: Union[EmptyStrToNone, int] = None  # e.g. 1
    reactive_rate: Union[EmptyStrToNone, int] = None  # Reactive power, e.g. 100
    reactive_value: Union[EmptyStrToNone, float] = None  # e.g. 1000.0
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    serial_num: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. 'AGP0N1600D'
    sph_set_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: offline, 1: online, 2: standby, 3: fault, other values indicate disconnection), e.g. 3
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'sph.status.fault'
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # System Time, e.g. '2018-01-01 00:00:00'
    sys_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2018-01-01 00:00:00'
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # TCP Server IP Address, e.g. '47.119.16.193'
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_AGP0N1600D'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'AGP0N1600D'
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. None
    uw_grid_watt_delay: Union[EmptyStrToNone, float] = None  # e.g. 1000
    uw_nominal_grid_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_reconnect_start_slope: Union[EmptyStrToNone, float] = None  # e.g. 10.0
    version: Union[EmptyStrToNone, str] = None  # e.g. 'ULSP0000xx'
    vnormal: Union[EmptyStrToNone, float] = None  # Rated PV Voltage, e.g. 350.0
    voltage_high_limit: Union[EmptyStrToNone, float] = None  # Utility Voltage Upper Limit, e.g. 264.0
    voltage_low_limit: Union[EmptyStrToNone, float] = None  # Utility Voltage Lower Limit, e.g. 213.0
    baudrate: Union[EmptyStrToNone, int] = None  # Baud Rate Selection, e.g. 0


def _sphs_details_data_to_camel(snake: str) -> str:
    override = {
        "sphs": "sph-s",
    }
    return override.get(snake, to_camel(snake=snake))


class SphsDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sphs_details_data_to_camel,
    )
    sphs: List[SphsDetailDataV4] = None


class SphsDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, SphsDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


class NoahDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterDetailsDataV4] = None
