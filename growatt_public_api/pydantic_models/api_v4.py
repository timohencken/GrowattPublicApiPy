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
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "parent_id": "parentID",
        "tree_id": "treeID",
        "baudrate": "wselectBaudrate",
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
# NOAH: TODO: what's the matching v1 device_type for NOAH???


def _noah_details_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
    }
    return override.get(snake, to_camel(snake=snake))


class NoahDetailDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_noah_details_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    address: Union[EmptyStrToNone, int] = None  # Inverter Address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # Alias, e.g. None
    associated_inv_sn: Union[EmptyStrToNone, str] = None  # Associated Inverter, e.g. None
    bms_version: Union[EmptyStrToNone, str] = None  # BMS Version, e.g. '213005'
    charging_soc_high_limit: Union[EmptyStrToNone, float] = None  # Charging SOC Upper Limit, e.g. 100
    charging_soc_low_limit: Union[EmptyStrToNone, float] = None  # Charging SOC Lower Limit, e.g. 0
    component_power: Union[EmptyStrToNone, float] = None  # Component Power (W), e.g. 0.0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Data Logger Number, e.g. '0PVPOXIEGENGHUI1'
    default_power: Union[EmptyStrToNone, float] = None  # Default Micro-Inverter Output Power, e.g. 200
    device_sn: Union[EmptyStrToNone, str] = None  # Device Number, e.g. '0PVPOXIEGENGHUI1'
    ebm_order_num: Union[EmptyStrToNone, int] = None  # Extended Battery Pack Serial Number, e.g. 0
    fw_version: Union[EmptyStrToNone, str] = None  # Hardware Version, e.g. None
    last_update_time: Union[EmptyStrToNone, int] = None  # Last update time, e.g. 1720667148000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-07-11 11:05:48'
    location: Union[EmptyStrToNone, str] = None  # address, e.g. None
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: disconnected), e.g. True
    model: Union[EmptyStrToNone, str] = None  # Model, e.g. 'Noah 2000'
    mppt_version: Union[EmptyStrToNone, str] = None  # MPPT Version, e.g. '212004'
    ota_device_type_code_high: Union[EmptyStrToNone, str] = None  # OTA Device Type Code (High), e.g. 'PB'
    ota_device_type_code_low: Union[EmptyStrToNone, str] = None  # e.g. 'FU'
    pd_version: Union[EmptyStrToNone, str] = None  # PD Version, e.g. '211005'
    port_name: Union[EmptyStrToNone, str] = None  # Communication Port Name, e.g. 'ShinePano-0PVPOXIEGENGHUI1'
    smart_socket_power: Union[EmptyStrToNone, float] = None  # Smart Socket Power, e.g. 0.0
    status: Union[EmptyStrToNone, int] = None  # Device Status (1: Normal; 4: Fault; 5: Heating), e.g. 0
    sys_time: Union[EmptyStrToNone, int] = None  # System time, e.g. 1720660008000
    temp_type: Union[EmptyStrToNone, int] = None  # Temperature Type, e.g. 0
    time1_enable: Union[EmptyStrToNone, bool] = None  # Time Slot 1 Switch, e.g. 1
    time1_end: Union[EmptyStrToNone, ForcedTime] = None  # Time Slot 1 End, e.g. '23:59'
    time1_mode: Union[EmptyStrToNone, int] = None  # Time Slot 1 Mode, e.g. 0
    time1_power: Union[EmptyStrToNone, float] = None  # Time Slot 1 Output Power Control, e.g. 400
    time1_start: Union[EmptyStrToNone, ForcedTime] = None  # Time Slot 1 Start, e.g. '0:0'
    time2_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    time2_end: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time2_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time2_power: Union[EmptyStrToNone, float] = None  # e.g. 200
    time2_start: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time3_enable: Union[EmptyStrToNone, bool] = None  # 0
    time3_end: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time3_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time3_power: Union[EmptyStrToNone, float] = None  # e.g. 200
    time3_start: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time4_enable: Union[EmptyStrToNone, bool] = None  # 0
    time4_end: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time4_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time4_power: Union[EmptyStrToNone, float] = None  # e.g. 2000
    time4_start: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time5_enable: Union[EmptyStrToNone, bool] = None  # 0
    time5_end: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time5_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time5_power: Union[EmptyStrToNone, float] = None  # e.g. 200
    time5_start: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time6_enable: Union[EmptyStrToNone, bool] = None  # 0
    time6_end: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time6_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time6_power: Union[EmptyStrToNone, float] = None  # e.g. 200
    time6_start: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time7_enable: Union[EmptyStrToNone, bool] = None  # 0
    time7_end: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time7_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time7_power: Union[EmptyStrToNone, float] = None  # e.g. 200
    time7_start: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time8_enable: Union[EmptyStrToNone, bool] = None  # 0
    time8_end: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time8_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time8_power: Union[EmptyStrToNone, float] = None  # e.g. 200
    time8_start: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time9_enable: Union[EmptyStrToNone, bool] = None  # 0
    time9_end: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'
    time9_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    time9_power: Union[EmptyStrToNone, float] = None  # e.g. 200
    time9_start: Union[EmptyStrToNone, ForcedTime] = None  # e.g. '0:0'


class NoahDetailsDataV4(ApiModel):
    noah: List[NoahDetailDataV4] = None


class NoahDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, NoahDetailsDataV4] = None


# #####################################################################################################################
# Device energy #######################################################################################################


def _inverter_energy_to_camel(snake: str) -> str:
    override = {
        "device_sn": "inverterId",  # align with other endpoints using "deviceSn" instead
        "real_op_percent": "realOPPercent",
        "w_pid_fault_value": "wPIDFaultValue",
    }
    return override.get(snake, to_camel(snake=snake))


class InverterEnergyDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_inverter_energy_to_camel,
    )

    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    big_device: Union[EmptyStrToNone, bool] = None  # e.g. False
    current_string1: Union[EmptyStrToNone, float] = None  # Current of channel 1 (A), e.g. 0.0
    current_string2: Union[EmptyStrToNone, float] = None  # Current of channel 2 (A), e.g. 0.0
    current_string3: Union[EmptyStrToNone, float] = None  # Current of channel 3 (A), e.g. 0.0
    current_string4: Union[EmptyStrToNone, float] = None  # Current of channel 4 (A), e.g. 0.0
    current_string5: Union[EmptyStrToNone, float] = None  # Current of channel 5 (A), e.g. 0.0
    current_string6: Union[EmptyStrToNone, float] = None  # Current of channel 6 (A), e.g. 0.0
    current_string7: Union[EmptyStrToNone, float] = None  # Current of channel 7 (A), e.g. 0.0
    current_string8: Union[EmptyStrToNone, float] = None  # Current of channel 8 (A), e.g. 0.0
    dw_string_warning_value1: Union[EmptyStrToNone, int] = None  # dwStringWarn warning, e.g. 0
    e_rac_today: Union[EmptyStrToNone, float] = None  # Reactive power generated today (kWh), e.g. 11.0
    e_rac_total: Union[EmptyStrToNone, float] = None  # Total reactive power generated (kWh), e.g. 110.0
    epv1_today: Union[EmptyStrToNone, float] = None  # Input channel 1 power generated today (kWh), e.g. 18.2
    epv1_total: Union[EmptyStrToNone, float] = None  # Input channel 1 total power generated (kWh), e.g. 139.3
    epv2_today: Union[EmptyStrToNone, float] = None  # Input channel 2 power generated today (kWh), e.g. 6.0
    epv2_total: Union[EmptyStrToNone, float] = None  # Input channel 2 total power generated (kWh), e.g. 60.0
    epv_total: Union[EmptyStrToNone, float] = None  # Total input power generated (kWh), e.g. 139.3
    fac: Union[EmptyStrToNone, float] = None  # Frequency (Hz), e.g. 49.98
    fault_type: Union[EmptyStrToNone, int] = None  # Fault code, e.g. 0
    i_pid_pvape: Union[EmptyStrToNone, float] = None  # PID PVAPE current, e.g. 0.0
    i_pid_pvbpe: Union[EmptyStrToNone, float] = None  # PID PVBPE current, e.g. 0.0
    iacr: Union[EmptyStrToNone, float] = None  # Output current channel 1 (A), e.g. 1.0
    iacs: Union[EmptyStrToNone, float] = None  # Output current channel 2 (A), e.g. 1.1
    iact: Union[EmptyStrToNone, float] = None  # Output current channel 3 (A), e.g. 1.1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "NHB691514F" (original: "inverterId")
    ipm_temperature: Union[EmptyStrToNone, float] = None  # IPM temperature, e.g. 40.7
    ipv1: Union[EmptyStrToNone, float] = None  # Input current channel 1 (A), e.g. 1.5
    ipv2: Union[EmptyStrToNone, float] = None  # Input current channel 2 (A), e.g. 0
    ipv3: Union[EmptyStrToNone, float] = None  # Input current channel 3 (A), e.g. 0
    n_bus_voltage: Union[EmptyStrToNone, float] = None  # N BUS voltage (V), e.g. 382.2
    op_fullwatt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    p_bus_voltage: Union[EmptyStrToNone, float] = None  # P BUS voltage (V), e.g. 381.7
    pac: Union[EmptyStrToNone, float] = None  # Output power (W), e.g. 936.6
    pacr: Union[EmptyStrToNone, float] = None  # Output power channel 1 (W), e.g. 277.4
    pacs: Union[EmptyStrToNone, float] = None  # Output power channel 2 (W), e.g. 315.3
    pact: Union[EmptyStrToNone, float] = None  # Output power channel 3 (W), e.g. 320.2
    pf: Union[EmptyStrToNone, float] = None  # Power factor, e.g. 1.0
    pid_status: Union[EmptyStrToNone, int] = None  # PID status, e.g. 0
    power_today: Union[EmptyStrToNone, float] = None  # Power generated today (kWh), e.g. 15.7
    power_total: Union[EmptyStrToNone, float] = None  # Total power generated (kWh), e.g. 130.3
    ppv: Union[EmptyStrToNone, float] = None  # Input PV power (W), e.g. 1111.9
    ppv1: Union[EmptyStrToNone, float] = None  # Input power channel 1 (W), e.g. 1111.9
    ppv2: Union[EmptyStrToNone, float] = None  # Input power channel 2 (W), e.g. 0
    ppv3: Union[EmptyStrToNone, float] = None  # Input power channel 3 (W), e.g. 0
    rac: Union[EmptyStrToNone, float] = None  # e.g. 6553.5
    real_op_percent: Union[EmptyStrToNone, float] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = None  # Inverter status (0: Waiting, 1: Normal, 3: Fault), e.g. 1
    status_text: Union[EmptyStrToNone, str] = None  # e.g. "Normal"
    str_fault: Union[EmptyStrToNone, float] = None  # PID strFault, e.g. 0
    temperature: Union[EmptyStrToNone, float] = None  # Temperature (°C), e.g. 47.1
    time: Union[EmptyStrToNone, datetime.datetime] = None  # Data time, e.g. "2024-05-25 16:56:33"
    time_calendar: Union[EmptyStrToNone, int] = None  # e.g. 1716627393328
    time_total: Union[EmptyStrToNone, float] = None  # Runtime, e.g. 94.97958333333334
    time_total_text: Union[EmptyStrToNone, str] = None  # e.g. "95"
    v_pid_pvape: Union[EmptyStrToNone, float] = None  # PID PVAPE voltage, e.g. 0.0
    v_pid_pvbpe: Union[EmptyStrToNone, float] = None  # PID PVBPE voltage, e.g. 0.0
    v_string1: Union[EmptyStrToNone, float] = None  # Voltage of channel 1 (V), e.g. 0.0
    v_string2: Union[EmptyStrToNone, float] = None  # Voltage of channel 2 (V), e.g. 0.0
    v_string3: Union[EmptyStrToNone, float] = None  # Voltage of channel 3 (V), e.g. 0.0
    v_string4: Union[EmptyStrToNone, float] = None  # Voltage of channel 4 (V), e.g. 0.0
    v_string5: Union[EmptyStrToNone, float] = None  # Voltage of channel 5 (V), e.g. 0.0
    v_string6: Union[EmptyStrToNone, float] = None  # Voltage of channel 6 (V), e.g. 0.0
    v_string7: Union[EmptyStrToNone, float] = None  # Voltage of channel 7 (V), e.g. 0.0
    v_string8: Union[EmptyStrToNone, float] = None  # Voltage of channel 8 (V), e.g. 0.0
    vacr: Union[EmptyStrToNone, float] = None  # Output voltage channel 1 (V), e.g. 481.6
    vacs: Union[EmptyStrToNone, float] = None  # Output voltage channel 2 (V), e.g. 497.5
    vact: Union[EmptyStrToNone, float] = None  # Output voltage channel 3 (V), e.g. 505.3
    vpv1: Union[EmptyStrToNone, float] = None  # Input voltage channel 1 (V), e.g. 741.3
    vpv2: Union[EmptyStrToNone, float] = None  # Input voltage channel 2 (V), e.g. 82.1
    vpv3: Union[EmptyStrToNone, float] = None  # Input voltage channel 3 (V), e.g. 0
    w_pid_fault_value: Union[EmptyStrToNone, int] = None  # wPIDFaultValue error code, e.g. 0
    w_string_status_value: Union[EmptyStrToNone, int] = None  # wStringStatusValue error code, e.g. 0
    warn_code: Union[EmptyStrToNone, int] = None  # Warning code, e.g. 0
    warning_value1: Union[EmptyStrToNone, int] = None  # e.g. 0
    warning_value2: Union[EmptyStrToNone, int] = None  # e.g. 0


class InverterEnergyOverviewDataV4(ApiModel):
    inv: List[InverterEnergyDataV4] = None


class InverterEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterEnergyOverviewDataV4] = None


# ------------------------------------------------------------------------------------------------


def _storage_energy_to_camel(snake: str) -> str:
    override = {
        "bms_c_volt": "bmsCvolt",
        "bms_max_current_charge": "bmsMaxCurrChg",
        "buck1_ntc_temperature": "buck1_NTCTemperature",
        "buck2_ntc_temperature": "buck2_NTCTemperature",
        "charge_bat_num": "chgBatNum",
        "charge_current": "chgCurr",
        "charge_energy": "chgEnergy",
        "datalogger_sn": "dataLogSn",
        "discharge_month_2": "disChargeMonth",  # avoid name collision
        "discharge_month": "dischargeMonth",  # avoid name collision
        "discharge_current": "dischgCurr",
        "e_bat_charge_today": "eBatChgToday",
        "e_bat_charge_total": "eBatChgTotal",
        "e_bat_discharge_today": "eBatDisChargeToday",
        "e_bat_discharge_total": "eBatDisChargeTotal",
        "e_gen_discharge_power": "eGenDischrPower",
        "e_gen_discharge_power1": "eGenDischrPower1",
        "e_gen_discharge_power2": "eGenDischrPower2",
        "e_gen_discharge_today": "eGenDischrToday",
        "e_gen_discharge_total": "eGenDischrTotal",
        "eac_discharge_today": "eacDisChargeToday",
        "eac_discharge_total": "eacDisChargeTotal",
        "eop_discharge_today": "eopDischrToday",
        "eop_discharge_total": "eopDischrTotal",
        "e_today": "etoday",
        "e_total": "etotal",
        "freq_output": "freqOutPut",
        "gauge2_rm1": "gauge2RM1",
        "gauge2_rm2": "gauge2RM2",
        "gauge_battery_status": "gaugeBattteryStatus",
        "gauge_fcc": "gaugeFCC",
        "gauge_ic_current": "gaugeICCurrent",
        "gauge_rm": "gaugeRM",
        "gauge_rm1": "gaugeRM1",
        "gauge_rm2": "gaugeRM2",
        "i_charge_pv1": "iChargePV1",
        "i_charge_pv2": "iChargePV2",
        "inner_cw_code": "innerCWCode",
        "llc_temperature": "llctemperature",
        "max_min_cell_temp_serial_num": "maxminCellTempSerialNum",
        "max_min_cell_volt_num": "maxminCellVoltNum",
        "max_min_soc": "maxminSoc",
        "output_current": "outPutCurrent",
        "output_current2": "outPutCurrent2",
        "output_power": "outPutPower",
        "output_power1": "outPutPower1",
        "output_power2": "outPutPower2",
        "output_volt": "outPutVolt",
        "output_volt2": "outPutVolt2",
        "p_ac_input": "pAcInPut",
        "p_ac_input1": "pAcInPut1",
        "p_ac_input2": "pAcInPut2",
        "p_ac_output": "pAcOutPut",
        "protect_pack_id": "protectPackID",
        "rate_va": "rateVA",
        "device_sn": "serialNum",  # align with other endpoints using "deviceSn" instead
    }
    return override.get(snake, to_camel(snake=snake))


class StorageEnergyDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_storage_energy_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. None
    b_light_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    bat_depower_reason: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_protect1: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_protect2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_protect3: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_serial_num_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_serial_number: Union[EmptyStrToNone, str] = None  # e.g. None
    bat_temp: Union[EmptyStrToNone, float] = None  # e.g. 43.0
    bat_warn_info1: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_warn_info2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_battery_curr: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_battery_temp: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_battery_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt4: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt5: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt6: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt7: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt8: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt9: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt10: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt11: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt12: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt13: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt14: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt15: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_volt16: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_cell_voltage1: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage2: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage3: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage4: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage5: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage6: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage7: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage8: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage9: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage10: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage11: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage12: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage13: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage14: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage15: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_cell_voltage16: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_constant_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_current2: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_c_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_delta_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_error: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_error2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_info: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_max_current_charge: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_pack_info: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_soh: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_status2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_temperature2: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_using_cap: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_warn_info: Union[EmptyStrToNone, int] = None  # e.g. 0
    buck1_ntc_temperature: Union[EmptyStrToNone, float] = None  # Buck1 Temperature, e.g. 24.3
    buck2_ntc_temperature: Union[EmptyStrToNone, float] = None  # Buck2 Temperature, e.g. 28.2
    calendar: Union[EmptyStrToNone, int] = None  # e.g. 1716985060479
    capacity: Union[EmptyStrToNone, float] = None  # Battery capacity (percent), e.g. 90
    capacity_text: Union[EmptyStrToNone, str] = None  # e.g. '90 %'
    cell_voltage1: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage2: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage3: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage4: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage5: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage6: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage7: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage8: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage9: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage10: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage11: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage12: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage13: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage14: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage15: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell_voltage16: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage1: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage2: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage3: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage4: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage5: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage6: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage7: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage8: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage9: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage10: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage11: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage12: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage13: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage14: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage15: Union[EmptyStrToNone, float] = None  # e.g. 0
    cell2_voltage16: Union[EmptyStrToNone, float] = None  # e.g. 0
    charge_day_map: Union[EmptyStrToNone, dict] = None  # e.g. {}
    charge_map: Union[EmptyStrToNone, dict] = None  # e.g. {}
    charge_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    charge_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    charge_to_standby_reason: Union[EmptyStrToNone, int] = None  # e.g. 0
    charge_to_standby_reason_text: Union[EmptyStrToNone, str] = None  # e.g. "Unknown"
    charge_way: Union[EmptyStrToNone, int] = None  # e.g. 0
    charge_bat_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    charge_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    charge_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    constant_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    constant_volt2: Union[EmptyStrToNone, float] = None  # e.g. 0
    cycle_count: Union[EmptyStrToNone, int] = None  # e.g. 0
    cycle_count2: Union[EmptyStrToNone, int] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'JVH0CJ5177'
    day: Union[EmptyStrToNone, int] = None  # e.g. None
    day_map: Union[EmptyStrToNone, Any] = None  # e.g. None
    dc_dc_temperature: Union[EmptyStrToNone, float] = None  # DcDc Temp, e.g. 26.6
    delta_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    delta_volt2: Union[EmptyStrToNone, float] = None  # e.g. 0
    device_type: Union[EmptyStrToNone, int] = None  # Storage device type (0: SP2000, 1: SP3000), e.g. 3
    discharge_month_2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    discharge_map: Union[EmptyStrToNone, dict] = None  # e.g. {}
    discharge_map_map: Union[EmptyStrToNone, dict] = None  # e.g. {}
    discharge_month: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    discharge_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    discharge_to_standby_reason: Union[EmptyStrToNone, int] = None  # e.g. 0
    discharge_to_standby_reason_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    discharge_current: Union[EmptyStrToNone, float] = None  # e.g. 10.1
    do_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    dsg_bat_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    dsg_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_bat_charge_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_bat_charge_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_bat_discharge_today: Union[EmptyStrToNone, float] = None  # Today's battery discharging energy, e.g. 2.1
    e_bat_discharge_total: Union[EmptyStrToNone, float] = None  # Total battery discharging energy, e.g. 560.6
    e_charge_today: Union[EmptyStrToNone, float] = None  # Today's AC charging energy, e.g. 0.0
    e_charge_today2: Union[EmptyStrToNone, float] = None  # SP3000 today's charging energy (kWh), e.g. 0.0
    e_charge_today_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 kWh'
    e_charge_total: Union[EmptyStrToNone, float] = None  # Total charging energy (kWh), e.g. 2.3
    e_charge_total2: Union[EmptyStrToNone, float] = None  # SP3000 total charging energy (kWh), e.g. 2.6
    e_charge_total_text: Union[EmptyStrToNone, str] = None  # e.g. '2.3 kWh'
    e_discharge_today: Union[EmptyStrToNone, float] = None  # Today's discharging energy (kWh), e.g. 0.0
    e_discharge_today2: Union[EmptyStrToNone, float] = None  # SP3000 today's discharging energy (kWh), e.g. 0-0
    e_discharge_today_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 kWh'
    e_discharge_total: Union[EmptyStrToNone, float] = None  # Total discharging energy (kWh), e.g. 1.7
    e_discharge_total2: Union[EmptyStrToNone, float] = None  # SP3000 total discharging energy (kWh), e.g. 1.7
    e_discharge_total_text: Union[EmptyStrToNone, str] = None  # e.g. '1.7 kWh'
    e_gen_discharge_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_gen_discharge_power1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_gen_discharge_power2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_gen_discharge_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_gen_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # Today's energy (user-to-grid) (kWh), e.g. 250.5
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # Total energy (user-to-grid) (kWh), e.g. 7648481.6
    e_to_user_today: Union[EmptyStrToNone, float] = None  # Today's energy (grid-to-user) (kWh), e.g. 6
    e_to_user_total: Union[EmptyStrToNone, float] = None  # Total energy (grid-to-user) (kWh), e.g. 24137119.8
    eac_charge_today: Union[EmptyStrToNone, float] = None  # AC charging energy of the day, e.g. 0.0
    eac_charge_total: Union[EmptyStrToNone, float] = None  # AC total charging energy, e.g. 2.1
    eac_discharge_today: Union[EmptyStrToNone, float] = None  # Today’s AC bypass load energy, e.g. 0
    eac_discharge_total: Union[EmptyStrToNone, float] = None  # Total AC bypass load energy, e.g. 474.1
    env_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    eop_discharge_today: Union[EmptyStrToNone, float] = None  # e.g. 7.2
    eop_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 582.6
    epv_today: Union[EmptyStrToNone, float] = None  # Today's panel energy (kWh), e.g. 3.3
    epv_today2: Union[EmptyStrToNone, float] = None  # SP3000 today's panel energy (kWh), e.g. 3.2
    epv_total: Union[EmptyStrToNone, float] = None  # Total panel energy (kWh), e.g. 539.6
    epv_total2: Union[EmptyStrToNone, float] = None  # SP3000 total panel energy (kWh), e.g. 511.5
    error_code: Union[EmptyStrToNone, int] = None  # Error code, e.g. 0
    error_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    e_today: Union[EmptyStrToNone, float] = None  # e.g. 6.5
    e_total: Union[EmptyStrToNone, float] = None  # e.g. 1049.6000000000001
    fault_code: Union[EmptyStrToNone, int] = None  # Fault code, e.g. 0
    float_charge_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    freq_grid: Union[EmptyStrToNone, float] = None  # Mains frequency, e.g. 49.92
    freq_output: Union[EmptyStrToNone, float] = None  # Output frequency, e.g. 49.97
    gauge2_rm1: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge2_rm2: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge_battery_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    gauge_fcc: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge_ic_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge_operation_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    gauge_pack_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    gauge_rm: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge_rm1: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge_rm2: Union[EmptyStrToNone, float] = None  # e.g. 0
    gen_current: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_current1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_current2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_volt2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    hardware_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    i_ac_charge: Union[EmptyStrToNone, float] = None  # AC charging current, e.g. 0.0
    i_ac_charge1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    i_ac_charge2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    i_charge: Union[EmptyStrToNone, float] = None  # PV end charging current (A), e.g. 0.0
    i_charge_pv1: Union[EmptyStrToNone, float] = None  # PV1 charging current, e.g. 0.0
    i_charge_pv2: Union[EmptyStrToNone, float] = None  # PV2 charging current, e.g. 0.0
    i_charge_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    i_discharge: Union[EmptyStrToNone, float] = None  # PV end discharging current (A), e.g. 0.0
    i_discharge_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    iac_to_grid: Union[EmptyStrToNone, float] = None  # Grid side current (A), e.g. 0.0
    iac_to_grid_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    iac_to_user: Union[EmptyStrToNone, float] = None  # User side current (A), e.g. 0.0
    iac_to_user_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    inner_cw_code: Union[EmptyStrToNone, str] = None  # e.g. None
    inv_temperature: Union[EmptyStrToNone, float] = None  # InvTemp, e.g. 28.1
    ipm_temperature: Union[EmptyStrToNone, float] = None  # IPM temperature (°C), e.g. 39.900001525878906
    ipv: Union[EmptyStrToNone, float] = None  # Input PV current (A) / SP3000 Charging power (W), e.g. 0.0
    ipv_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    llc_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    load_percent: Union[EmptyStrToNone, float] = None  # Load percentage, e.g. 12.5
    load_percent1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    load_percent2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    manual_start_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    manufacture: Union[EmptyStrToNone, int] = None  # e.g. 0
    max_cell_temp: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    max_cell_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    max_charge_or_discharge_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    max_charge_or_discharge_current2: Union[EmptyStrToNone, float] = None  # e.g. 0
    max_min_cell_temp_serial_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    max_min_cell_volt_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    max_min_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    min_cell_temp: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    min_cell_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    module2_max_temp: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    module2_max_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    module2_min_temp: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    module2_min_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    module_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    module_id2: Union[EmptyStrToNone, int] = None  # e.g. 0
    module_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    module_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    module_total_curr: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    module_total_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    normal_power: Union[EmptyStrToNone, int] = None  # Current power (W), e.g. 0
    output_current: Union[EmptyStrToNone, float] = None  # Output current, e.g. 2.7
    output_current2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    output_power: Union[EmptyStrToNone, float] = None  # Output power, e.g. 498.0
    output_power1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    output_power2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    output_volt: Union[EmptyStrToNone, float] = None  # Output voltage, e.g. 229.8
    output_volt2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    p_ac_charge: Union[EmptyStrToNone, float] = None  # AC charging power, e.g. 0.0
    p_ac_input: Union[EmptyStrToNone, float] = None  # AC input energy, e.g. 0.0
    p_ac_input1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    p_ac_input2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    p_ac_output: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    p_bat: Union[EmptyStrToNone, float] = None  # e.g. 534.0
    p_charge: Union[EmptyStrToNone, float] = None  # Charging power (W), e.g. 0.0
    p_charge2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    p_charge_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 W'
    p_discharge: Union[EmptyStrToNone, float] = None  # Discharge power (W), e.g. 0.0
    p_discharge2: Union[EmptyStrToNone, float] = None  # SP3000 Discharge power (W), e.g. 0.0
    p_discharge_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 W'
    pac_to_grid: Union[EmptyStrToNone, float] = None  # Grid side power (W), e.g. 0.0
    pac_to_grid_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 W'
    pac_to_user: Union[EmptyStrToNone, float] = None  # User-side power (V), e.g. 1922.9
    pac_to_user_text: Union[EmptyStrToNone, str] = None  # e.g. '1922.9 W'
    pack_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    parallel_hight_softwar_ver: Union[EmptyStrToNone, int] = None  # e.g. 0
    pow_saving_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv: Union[EmptyStrToNone, float] = None  # Panel input power (W), e.g. 1075.4
    ppv2: Union[EmptyStrToNone, float] = None  # SP3000 panel input power (W), e.g. 991.7
    ppv_text: Union[EmptyStrToNone, str] = None  # e.g. '1075.4 W'
    protect_pack_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    q_bat: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    rate_va: Union[EmptyStrToNone, float] = None  # e.g. 0
    rate_watt: Union[EmptyStrToNone, float] = None  # e.g. 0
    remote_cntl_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    remote_cntl_fail_reason: Union[EmptyStrToNone, int] = None  # e.g. 0
    request_battery_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    sci_loss_chk_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    device_sn: Union[EmptyStrToNone, str] = None  # Storage device SN, e.g. 'CDL0CJF08Z'
    software_version1: Union[EmptyStrToNone, str] = None  # e.g. None
    software_version2: Union[EmptyStrToNone, str] = None  # e.g. None
    software_version3: Union[EmptyStrToNone, str] = None  # e.g. None
    soh: Union[EmptyStrToNone, float] = None  # e.g. 0
    soh2: Union[EmptyStrToNone, float] = None  # e.g. 0
    spf5000_status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Battery Discharging'
    status: Union[EmptyStrToNone, int] = (
        None  # Storage device status (0: Operating, 1: Charge, 2: Discharge, 3: Fault, 4: Flash), e.g. 2
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Discharge'
    storage_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    sys_out: Union[EmptyStrToNone, float] = None  # e.g. 2067.1000000000004
    temperature: Union[EmptyStrToNone, float] = None  # temperature (°C), e.g. 39.79999923706055
    time: Union[EmptyStrToNone, datetime.datetime] = None  # Data time, e.g. '2024-05-29 20:17:40'
    total_cell_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    update_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_bat_type2: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_bat: Union[EmptyStrToNone, float] = None  # Battery voltage (V), e.g. 50.20000076293945
    v_bat_text: Union[EmptyStrToNone, str] = None  # e.g. '50.2 V'
    v_buck: Union[EmptyStrToNone, float] = None  # vBuk (A), e.g. 161.39999389648438
    v_buck2: Union[EmptyStrToNone, float] = None  # vBuck2 (A), e.g. 167.3000030517578
    v_buck_text: Union[EmptyStrToNone, str] = None  # e.g. '161.4 V'
    v_bus: Union[EmptyStrToNone, float] = None  # e.g. 171.6999969482422
    v_grid: Union[EmptyStrToNone, float] = None  # Mains voltage, e.g. 0
    v_grid2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    vac: Union[EmptyStrToNone, float] = None  # Grid voltage (V), e.g. 226.5
    vac_Text: Union[EmptyStrToNone, str] = None  # e.g. '226.5 V'
    vpv: Union[EmptyStrToNone, float] = None  # Input PV voltage (V), e.g. 161.39999389648438
    vpv2: Union[EmptyStrToNone, float] = None  # SP3000 input PV voltage (V), e.g. 167.60000610351562
    vpv_text: Union[EmptyStrToNone, str] = None  # e.g. '161.4 V'
    warn_code: Union[EmptyStrToNone, int] = None  # Warning code, e.g. 0
    warn_code2: Union[EmptyStrToNone, int] = None  # Warning Code, e.g. 0
    warn_code3: Union[EmptyStrToNone, int] = None  # Warning Code, e.g. 0
    warn_info: Union[EmptyStrToNone, int] = None  # e.g. 0
    warn_info2: Union[EmptyStrToNone, int] = None  # e.g. 0
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    with_time: Union[EmptyStrToNone, bool] = None  # e.g. False


class StorageEnergyOverviewDataV4(ApiModel):
    storage: List[StorageEnergyDataV4] = None


class StorageEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, StorageEnergyOverviewDataV4] = None


# ------------------------------------------------------------------------------------------------


def _max_energy_to_camel(snake: str) -> str:
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
        "device_sn": "serialNum",  # align with other endpoints using "deviceSn" instead
        "str_unbalance": "strUnblance",
        "w_pid_fault_value": "wPIDFaultValue",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxEnergyDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_energy_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    afci_pv1: Union[EmptyStrToNone, int] = None  # e.g. 0
    afci_pv2: Union[EmptyStrToNone, int] = None  # e.g. 0
    afci_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. None
    apf_status: Union[EmptyStrToNone, float] = None  # APF/SVG status, e.g. 0
    apf_status_text: Union[EmptyStrToNone, str] = None  # e.g. 'None'
    calendar: Union[EmptyStrToNone, int] = None  # Time (Calendar), e.g. 1716618863392
    comp_har_ir: Union[EmptyStrToNone, float] = None  # R-phase compensation harmonic amount, e.g. 0.0
    comp_har_is: Union[EmptyStrToNone, float] = None  # S-phase compensation harmonic amount, e.g. 0.0
    comp_har_it: Union[EmptyStrToNone, float] = None  # T-phase compensation harmonic amount, e.g. 0.0
    comp_qr: Union[EmptyStrToNone, float] = None  # R-phase compensation reactive power, e.g. 0.0
    comp_qs: Union[EmptyStrToNone, float] = None  # S-phase compensation reactive power, e.g. 0.0
    comp_qt: Union[EmptyStrToNone, float] = None  # T-phase compensation reactive power, e.g. 0.0
    ct_har_ir: Union[EmptyStrToNone, float] = None  # R-phase CT side harmonic amount, e.g. 0.0
    ct_har_is: Union[EmptyStrToNone, float] = None  # S-phase CT side harmonic amount, e.g. 0.0
    ct_har_it: Union[EmptyStrToNone, float] = None  # T-phase CT side harmonic amount, e.g. 0.0
    ct_ir: Union[EmptyStrToNone, float] = None  # R-phase CT side current, e.g. 0.0
    ct_is: Union[EmptyStrToNone, float] = None  # S-phase CT side current, e.g. 0.0
    ct_it: Union[EmptyStrToNone, float] = None  # T-phase CT side current, e.g. 0.0
    ct_qr: Union[EmptyStrToNone, float] = None  # R-phase CT side reactive power, e.g. 0.0
    ct_qs: Union[EmptyStrToNone, float] = None  # S-phase CT side reactive power, e.g. 0.0
    ct_qt: Union[EmptyStrToNone, float] = None  # T-phase CT side power, e.g. 0.0
    current_string1: Union[EmptyStrToNone, float] = None  # String current 1, e.g. 0.0
    current_string2: Union[EmptyStrToNone, float] = None  # String current 2, e.g. 0.0
    current_string3: Union[EmptyStrToNone, float] = None  # String current 3, e.g. 0.0
    current_string4: Union[EmptyStrToNone, float] = None  # String current 4, e.g. 0.0
    current_string5: Union[EmptyStrToNone, float] = None  # String current 5, e.g. 0.0
    current_string6: Union[EmptyStrToNone, float] = None  # String current 6, e.g. 0.0
    current_string7: Union[EmptyStrToNone, float] = None  # String current 7, e.g. 0.0
    current_string8: Union[EmptyStrToNone, float] = None  # String current 8, e.g. 0.0
    current_string9: Union[EmptyStrToNone, float] = None  # String current 9, e.g. 0.0
    current_string10: Union[EmptyStrToNone, float] = None  # String current 10, e.g. 0.0
    current_string11: Union[EmptyStrToNone, float] = None  # String current 11, e.g. 0.0
    current_string12: Union[EmptyStrToNone, float] = None  # String current 12, e.g. 0.0
    current_string13: Union[EmptyStrToNone, float] = None  # String current 13, e.g. 0.0
    current_string14: Union[EmptyStrToNone, float] = None  # String current 14, e.g. 0.0
    current_string15: Union[EmptyStrToNone, float] = None  # String current 15, e.g. 0.0
    current_string16: Union[EmptyStrToNone, float] = None  # String current 16, e.g. 0.0
    current_string17: Union[EmptyStrToNone, float] = None  # String current 17, e.g. 0.0
    current_string18: Union[EmptyStrToNone, float] = None  # String current 18, e.g. 0.0
    current_string19: Union[EmptyStrToNone, float] = None  # String current 19, e.g. 0.0
    current_string20: Union[EmptyStrToNone, float] = None  # String current 20, e.g. 0.0
    current_string21: Union[EmptyStrToNone, float] = None  # String current 21, e.g. 0.0
    current_string22: Union[EmptyStrToNone, float] = None  # String current 22, e.g. 0.0
    current_string23: Union[EmptyStrToNone, float] = None  # String current 23, e.g. 0.0
    current_string24: Union[EmptyStrToNone, float] = None  # String current 24, e.g. 0.0
    current_string25: Union[EmptyStrToNone, float] = None  # String current 25, e.g. 0.0
    current_string26: Union[EmptyStrToNone, float] = None  # String current 26, e.g. 0.0
    current_string27: Union[EmptyStrToNone, float] = None  # String current 27, e.g. 0.0
    current_string28: Union[EmptyStrToNone, float] = None  # String current 28, e.g. 0.0
    current_string29: Union[EmptyStrToNone, float] = None  # String current 29, e.g. 0.0
    current_string30: Union[EmptyStrToNone, float] = None  # String current 30, e.g. 0.0
    current_string31: Union[EmptyStrToNone, float] = None  # String current 31, e.g. 0.0
    current_string32: Union[EmptyStrToNone, float] = None  # String current 32, e.g. 0.0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'BLE4BEQ0BW'
    day: Union[EmptyStrToNone, str] = None  # Time - Day, e.g. None
    debug1: Union[EmptyStrToNone, str] = None  # e.g. '160, 0, 0, 0, 324, 0, 0, 0'
    debug2: Union[EmptyStrToNone, str] = None  # e.g. '0,0,0,0,0,0,0,0'
    debug3: Union[EmptyStrToNone, str] = None  # e.g. '0,0,0,0,0,0,0,0'
    derating_mode: Union[EmptyStrToNone, int] = None  # Derating mode, e.g. 0
    dw_string_warning_value1: Union[EmptyStrToNone, int] = None  # e.g. 0
    eac_today: Union[EmptyStrToNone, float] = None  # Energy generated today, e.g. 21.600000381469727
    e_rac_today: Union[EmptyStrToNone, float] = None  # Reactive energy today (kWh / kVarh), e.g. 0
    e_rac_total: Union[EmptyStrToNone, float] = None  # Total reactive energy (kWh / kVarh), e.g. 0
    eac_total: Union[EmptyStrToNone, float] = None  # Total energy generated, e.g. 1859.5
    epv1_today: Union[EmptyStrToNone, float] = None  # PV1 energy generated today, e.g. 13.199999809265137
    epv1_total: Union[EmptyStrToNone, float] = None  # Total PV1 energy generated, e.g. 926.6
    epv2_today: Union[EmptyStrToNone, float] = None  # PV2 energy generated today, e.g. 8.199999809265137
    epv2_total: Union[EmptyStrToNone, float] = None  # Total PV2 energy generated, e.g. 906.4
    epv3_today: Union[EmptyStrToNone, float] = None  # PV3 energy generated today, e.g. 0
    epv3_total: Union[EmptyStrToNone, float] = None  # Total PV3 energy generated, e.g. 0
    epv4_today: Union[EmptyStrToNone, float] = None  # PV4 energy generated today, e.g. 0
    epv4_total: Union[EmptyStrToNone, float] = None  # Total PV4 energy generated, e.g. 0
    epv5_today: Union[EmptyStrToNone, float] = None  # PV5 energy generated today, e.g. 0
    epv5_total: Union[EmptyStrToNone, float] = None  # Total PV5 energy generated, e.g. 0
    epv6_today: Union[EmptyStrToNone, float] = None  # PV6 energy generated today, e.g. 0
    epv6_total: Union[EmptyStrToNone, float] = None  # Total PV6 energy generated, e.g. 0
    epv7_today: Union[EmptyStrToNone, float] = None  # PV7 energy generated today, e.g. 0
    epv7_total: Union[EmptyStrToNone, float] = None  # Total PV7 energy generated, e.g. 0
    epv8_today: Union[EmptyStrToNone, float] = None  # PV8 energy generated today, e.g. 0
    epv8_total: Union[EmptyStrToNone, float] = None  # Total PV8 energy generated, e.g. 0
    epv9_today: Union[EmptyStrToNone, float] = None  # PV9 energy generated today, e.g. 0
    epv9_total: Union[EmptyStrToNone, float] = None  # Total PV9 energy generated, e.g. 0
    epv10_today: Union[EmptyStrToNone, float] = None  # PV10 energy generated today, e.g. 0
    epv10_total: Union[EmptyStrToNone, float] = None  # Total PV10 energy generated, e.g. 0
    epv11_today: Union[EmptyStrToNone, float] = None  # PV11 energy generated today, e.g. 0
    epv11_total: Union[EmptyStrToNone, float] = None  # Total PV11 energy generated, e.g. 0
    epv12_today: Union[EmptyStrToNone, float] = None  # PV12 energy generated today, e.g. 0
    epv12_total: Union[EmptyStrToNone, float] = None  # Total PV12 energy generated, e.g. 0
    epv13_today: Union[EmptyStrToNone, float] = None  # PV13 energy generated today, e.g. 0
    epv13_total: Union[EmptyStrToNone, float] = None  # Total PV13 energy generated, e.g. 0
    epv14_today: Union[EmptyStrToNone, float] = None  # PV14 energy generated today, e.g. 0
    epv14_total: Union[EmptyStrToNone, float] = None  # Total PV14 energy generated, e.g. 0
    epv15_today: Union[EmptyStrToNone, float] = None  # PV15 energy generated today, e.g. 0
    epv15_total: Union[EmptyStrToNone, float] = None  # Total PV15 energy generated, e.g. 0
    epv16_today: Union[EmptyStrToNone, float] = None  # PV16 energy generated today, e.g. 0
    epv16_total: Union[EmptyStrToNone, float] = None  # Total PV16 energy generated, e.g. 0
    epv_total: Union[EmptyStrToNone, float] = None  # Total PV energy generated, e.g. 115372.9
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 49.98
    fault_code1: Union[EmptyStrToNone, int] = None  # Fault code, e.g. 2
    fault_code2: Union[EmptyStrToNone, int] = None  # Fault code, e.g. 0
    fault_type: Union[EmptyStrToNone, int] = None  # Fault code, e.g. 0
    fault_value: Union[EmptyStrToNone, int] = None  # Fault value, e.g. 3
    gfci: Union[EmptyStrToNone, float] = None  # Leakage current, e.g. 166
    i_pid_pvape: Union[EmptyStrToNone, float] = None  # pid current 1 (A), e.g. 0.0
    i_pid_pvbpe: Union[EmptyStrToNone, float] = None  # pid current 2 (A), e.g. 0.0
    i_pid_pvcpe: Union[EmptyStrToNone, float] = None  # pid current 3 (A), e.g. 0.0
    i_pid_pvdpe: Union[EmptyStrToNone, float] = None  # pid current 4 (A), e.g. 0.0
    i_pid_pvepe: Union[EmptyStrToNone, float] = None  # pid current 5 (A), e.g. 0.0
    i_pid_pvfpe: Union[EmptyStrToNone, float] = None  # pid current 6 (A), e.g. 0.0
    i_pid_pvgpe: Union[EmptyStrToNone, float] = None  # pid current 7 (A), e.g. 0.0
    i_pid_pvhpe: Union[EmptyStrToNone, float] = None  # pid current 8 (A), e.g. 0.0
    i_pid_pvpe9: Union[EmptyStrToNone, float] = None  # pid current 9 (A), e.g. 0.0
    i_pid_pvpe10: Union[EmptyStrToNone, float] = None  # pid current 10 (A), e.g. 0.0
    i_pid_pvpe11: Union[EmptyStrToNone, float] = None  # pid current 11 (A), e.g. 0.0
    i_pid_pvpe12: Union[EmptyStrToNone, float] = None  # pid current 12 (A), e.g. 0.0
    i_pid_pvpe13: Union[EmptyStrToNone, float] = None  # pid current 13 (A), e.g. 0.0
    i_pid_pvpe14: Union[EmptyStrToNone, float] = None  # pid current 14 (A), e.g. 0.0
    i_pid_pvpe15: Union[EmptyStrToNone, float] = None  # pid current 15 (A), e.g. 0.0
    i_pid_pvpe16: Union[EmptyStrToNone, float] = None  # pid current 16 (A), e.g. 0.0
    iacr: Union[EmptyStrToNone, float] = None  # R-phase current (A), e.g. 3.1000001
    iacs: Union[EmptyStrToNone, float] = None  # S-phase current (A), e.g. 3.2
    iact: Union[EmptyStrToNone, float] = None  # T-phase current (A), e.g. 3.2
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    ipm_temperature: Union[EmptyStrToNone, float] = None  # IPM temperature, e.g. 0.0
    ipv1: Union[EmptyStrToNone, float] = None  # PV1 current (A), e.g. 0.7
    ipv2: Union[EmptyStrToNone, float] = None  # PV2 current (A), e.g. 2.4
    ipv3: Union[EmptyStrToNone, float] = None  # PV3 current (A), e.g. 0.0
    ipv4: Union[EmptyStrToNone, float] = None  # PV4 current (A), e.g. 0.0
    ipv5: Union[EmptyStrToNone, float] = None  # PV5 current (A), e.g. 0.0
    ipv6: Union[EmptyStrToNone, float] = None  # PV6 current (A), e.g. 0.0
    ipv7: Union[EmptyStrToNone, float] = None  # PV7 current (A), e.g. 0.0
    ipv8: Union[EmptyStrToNone, float] = None  # PV8 current (A), e.g. 0.0
    ipv9: Union[EmptyStrToNone, float] = None  # PV9 current (A), e.g. 0.0
    ipv10: Union[EmptyStrToNone, float] = None  # PV10 current (A), e.g. 0.0
    ipv11: Union[EmptyStrToNone, float] = None  # PV11 current (A), e.g. 0.0
    ipv12: Union[EmptyStrToNone, float] = None  # PV12 current (A), e.g. 0.0
    ipv13: Union[EmptyStrToNone, float] = None  # PV13 current (A), e.g. 0.0
    ipv14: Union[EmptyStrToNone, float] = None  # PV14 current (A), e.g. 0.0
    ipv15: Union[EmptyStrToNone, float] = None  # PV15 current (A), e.g. 0.0
    ipv16: Union[EmptyStrToNone, float] = None  # PV16 current (A), e.g. 0.0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    max_bean: Union[EmptyStrToNone, Any] = None
    n_bus_voltage: Union[EmptyStrToNone, float] = None  # N Bus voltage, e.g. 334.9
    op_fullwatt: Union[EmptyStrToNone, float] = None  # e.g. 27500.0
    p_bus_voltage: Union[EmptyStrToNone, float] = None  # P Bus voltage, e.g. 332.6
    pac: Union[EmptyStrToNone, float] = None  # Output power (W), e.g. 2038.9
    pacr: Union[EmptyStrToNone, float] = None  # R-phase output power (W), e.g. 740.9
    pacs: Union[EmptyStrToNone, float] = None  # S-phase output power (W), e.g. 749.1
    pact: Union[EmptyStrToNone, float] = None  # T-phase output power (W), e.g. 782.1
    pf: Union[EmptyStrToNone, float] = None  # pf value, e.g. 1.0
    pid_bus: Union[EmptyStrToNone, float] = None  # PID BUS voltage, e.g. 0.0
    pid_fault_code: Union[EmptyStrToNone, int] = None  # pid fault code, e.g. 0
    pid_status: Union[EmptyStrToNone, int] = None  # pid status, e.g. 0
    pid_status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Lost'
    power_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    power_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ppv: Union[EmptyStrToNone, float] = None  # Total PV input power (W), e.g. 2069.9
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 power (W), e.g. 410.4
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 power (W), e.g. 1551.6
    ppv3: Union[EmptyStrToNone, float] = None  # PV3 power (W), e.g. 0.0
    ppv4: Union[EmptyStrToNone, float] = None  # PV4 power (W), e.g. 0.0
    ppv5: Union[EmptyStrToNone, float] = None  # PV5 power (W), e.g. 0.0
    ppv6: Union[EmptyStrToNone, float] = None  # PV6 power (W), e.g. 0.0
    ppv7: Union[EmptyStrToNone, float] = None  # PV7 power (W), e.g. 0.0
    ppv8: Union[EmptyStrToNone, float] = None  # PV8 power (W), e.g. 0.0
    ppv9: Union[EmptyStrToNone, float] = None  # PV9 power (W)r, e.g. 0.0
    ppv10: Union[EmptyStrToNone, float] = None  # PV10 power (W), e.g. 0.0
    ppv11: Union[EmptyStrToNone, float] = None  # PV11 power (W), e.g. 0.0
    ppv12: Union[EmptyStrToNone, float] = None  # PV12 power (W), e.g. 0.0
    ppv13: Union[EmptyStrToNone, float] = None  # PV13 power (W), e.g. 0.0
    ppv14: Union[EmptyStrToNone, float] = None  # PV14 power (W), e.g. 0.0
    ppv15: Union[EmptyStrToNone, float] = None  # PV15 power (W), e.g. 0.0
    ppv16: Union[EmptyStrToNone, float] = None  # PV16 power (W), e.g. 0.0
    pv_iso: Union[EmptyStrToNone, float] = None  # Insulation resistance, e.g. 3004
    r_dci: Union[EmptyStrToNone, float] = None  # R-phase DC component, e.g. 0.2
    rac: Union[EmptyStrToNone, float] = None  # Reactive power (W / Var), e.g. 0.0
    react_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    react_power_max: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    react_power_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    real_op_percent: Union[EmptyStrToNone, float] = None  # e.g. 50
    s_dci: Union[EmptyStrToNone, float] = None  # S-phase DC component, e.g. 0.7
    device_sn: Union[EmptyStrToNone, str] = None  # Max device SN, e.g. 'HPJ0BF20FU'
    status: Union[EmptyStrToNone, int] = None  # Max status (0: Standby, 1: , 2: Discharge, 3: Fault, 4: Flash), e.g. 1
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Normal'
    str_break: Union[EmptyStrToNone, int] = None  # String not connected, e.g. 0
    str_fault: Union[EmptyStrToNone, int] = None  # String error, e.g. 0
    str_unbalance: Union[EmptyStrToNone, int] = None  # String current imbalance, e.g. 0
    str_unmatch: Union[EmptyStrToNone, int] = None  # String mismatch, e.g. 0
    t_dci: Union[EmptyStrToNone, float] = None  # T-phase DC component, e.g. 6552.7
    temperature: Union[EmptyStrToNone, float] = None  # AMTemp1(°C), e.g. 52.5
    temperature2: Union[EmptyStrToNone, float] = None  # INVTemp(°C), e.g. 41.4
    temperature3: Union[EmptyStrToNone, float] = None  # BTTemp(°C), e.g. 39.100002
    temperature4: Union[EmptyStrToNone, float] = None  # OUTTemp(°C), e.g. 0.0
    temperature5: Union[EmptyStrToNone, float] = None  # AMTemp2(°C), e.g. 35.8
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-25 14:34:23'
    time_calendar: Union[EmptyStrToNone, int] = None  # e.g. 1716618863392
    time_total: Union[EmptyStrToNone, float] = None  # Total run time, e.g. 44968542.0
    v_pid_pvape: Union[EmptyStrToNone, float] = None  # pid voltage 1 (V), e.g. 239.5
    v_pid_pvbpe: Union[EmptyStrToNone, float] = None  # pid voltage 2 (V), e.g. 0.0
    v_pid_pvcpe: Union[EmptyStrToNone, float] = None  # pid voltage 3 (V), e.g. 0.0
    v_pid_pvdpe: Union[EmptyStrToNone, float] = None  # pid voltage 4 (V), e.g. 0.0
    v_pid_pvepe: Union[EmptyStrToNone, float] = None  # pid voltage 5 (V), e.g. 0.0
    v_pid_pvfpe: Union[EmptyStrToNone, float] = None  # pid voltage 6 (V), e.g. 0.0
    v_pid_pvgpe: Union[EmptyStrToNone, float] = None  # pid voltage 7 (V), e.g. 0.0
    v_pid_pvhpe: Union[EmptyStrToNone, float] = None  # pid voltage 8 (V), e.g. 0.0
    v_pid_pvpe9: Union[EmptyStrToNone, float] = None  # pid voltage 9 (V), e.g. 0.0
    v_pid_pvpe10: Union[EmptyStrToNone, float] = None  # pid voltage 10 (V), e.g. 0.0
    v_pid_pvpe11: Union[EmptyStrToNone, float] = None  # pid voltage 11 (V), e.g. 0.0
    v_pid_pvpe12: Union[EmptyStrToNone, float] = None  # pid voltage 12 (V), e.g. 0.0
    v_pid_pvpe13: Union[EmptyStrToNone, float] = None  # pid voltage 13 (V), e.g. 0.0
    v_pid_pvpe14: Union[EmptyStrToNone, float] = None  # pid voltage 14 (V), e.g. 0.0
    v_pid_pvpe15: Union[EmptyStrToNone, float] = None  # pid voltage 15 (V), e.g. 0.0
    v_pid_pvpe16: Union[EmptyStrToNone, float] = None  # pid voltage 16 (V), e.g. 0.0
    v_string1: Union[EmptyStrToNone, float] = None  # String voltage 1, e.g. 0.0
    v_string2: Union[EmptyStrToNone, float] = None  # String voltage 2, e.g. 0.0
    v_string3: Union[EmptyStrToNone, float] = None  # String voltage 3, e.g. e.g. 0.0
    v_string4: Union[EmptyStrToNone, float] = None  # String voltage 4, e.g. e.g. 0.0
    v_string5: Union[EmptyStrToNone, float] = None  # String voltage 5, e.g. e.g. 0.0
    v_string6: Union[EmptyStrToNone, float] = None  # String voltage 6, e.g. e.g. 0.0
    v_string7: Union[EmptyStrToNone, float] = None  # String voltage 7, e.g. e.g. 0.0
    v_string8: Union[EmptyStrToNone, float] = None  # String voltage 8, e.g. e.g. 0.0
    v_string9: Union[EmptyStrToNone, float] = None  # String voltage 9, e.g. e.g. 0.0
    v_string10: Union[EmptyStrToNone, float] = None  # String voltage 10, e.g. e.g. 0.0
    v_string11: Union[EmptyStrToNone, float] = None  # String voltage 11, e.g. 0.0
    v_string12: Union[EmptyStrToNone, float] = None  # String voltage 12, e.g. 0.0
    v_string13: Union[EmptyStrToNone, float] = None  # String voltage 13, e.g. 0.0
    v_string14: Union[EmptyStrToNone, float] = None  # String voltage 14, e.g. 0.0
    v_string15: Union[EmptyStrToNone, float] = None  # String voltage 15, e.g. 0.0
    v_string16: Union[EmptyStrToNone, float] = None  # String voltage 16, e.g. 0.0
    v_string17: Union[EmptyStrToNone, float] = None  # String voltage 17, e.g. 0.0
    v_string18: Union[EmptyStrToNone, float] = None  # String voltage 18, e.g. 0.0
    v_string19: Union[EmptyStrToNone, float] = None  # String voltage 19, e.g. 0.0
    v_string20: Union[EmptyStrToNone, float] = None  # String voltage 20, e.g. 0.0
    v_string21: Union[EmptyStrToNone, float] = None  # String voltage 21, e.g. 0.0
    v_string22: Union[EmptyStrToNone, float] = None  # String voltage 22, e.g. 0.0
    v_string23: Union[EmptyStrToNone, float] = None  # String voltage 23, e.g. 0.0
    v_string24: Union[EmptyStrToNone, float] = None  # String voltage 24, e.g. 0.0
    v_string25: Union[EmptyStrToNone, float] = None  # String voltage 25, e.g. 0.0
    v_string26: Union[EmptyStrToNone, float] = None  # String voltage 26, e.g. 0.0
    v_string27: Union[EmptyStrToNone, float] = None  # String voltage 27, e.g. 0.0
    v_string28: Union[EmptyStrToNone, float] = None  # String voltage 28, e.g. 0.0
    v_string29: Union[EmptyStrToNone, float] = None  # String voltage 29, e.g. 0.0
    v_string30: Union[EmptyStrToNone, float] = None  # String voltage 30, e.g. 0.0
    v_string31: Union[EmptyStrToNone, float] = None  # String voltage 31, e.g. 0.0
    v_string32: Union[EmptyStrToNone, float] = None  # String voltage 32, e.g. 0.0
    vac_rs: Union[EmptyStrToNone, float] = None  # RS line voltage (V), e.g. 414.30002
    vac_st: Union[EmptyStrToNone, float] = None  # ST line voltage (V), e.g. 407.2
    vac_tr: Union[EmptyStrToNone, float] = None  # TR line voltage (V), e.g. 407.2
    vacr: Union[EmptyStrToNone, float] = None  # R-phase voltage (V), e.g. 239.0
    vacs: Union[EmptyStrToNone, float] = None  # S-phase voltage (V), e.g. 234.1
    vact: Union[EmptyStrToNone, float] = None  # T-phase voltage (V), e.g. 237.0
    vpv1: Union[EmptyStrToNone, float] = None  # PV1 voltage (V), e.g. 586.4
    vpv2: Union[EmptyStrToNone, float] = None  # PV2 voltage (V), e.g. 646.5
    vpv3: Union[EmptyStrToNone, float] = None  # PV3 voltage (V), e.g. 0.0
    vpv4: Union[EmptyStrToNone, float] = None  # PV4 voltage (V), e.g. 0.0
    vpv5: Union[EmptyStrToNone, float] = None  # PV5 voltage (V), e.g. 0.0
    vpv6: Union[EmptyStrToNone, float] = None  # PV6 voltage (V), e.g. 0.0
    vpv7: Union[EmptyStrToNone, float] = None  # PV7 voltage (V), e.g. 0.0
    vpv8: Union[EmptyStrToNone, float] = None  # PV8 voltage (V), e.g. 0.0
    vpv9: Union[EmptyStrToNone, float] = None  # PV9 voltage (V), e.g. 0.0
    vpv10: Union[EmptyStrToNone, float] = None  # PV10 voltage (V), e.g. 0.0
    vpv11: Union[EmptyStrToNone, float] = None  # PV11 voltage (V), e.g. 0.0
    vpv12: Union[EmptyStrToNone, float] = None  # PV12 voltage (V), e.g. 0.0
    vpv13: Union[EmptyStrToNone, float] = None  # PV13 voltage (V), e.g. 0.0
    vpv14: Union[EmptyStrToNone, float] = None  # PV14 voltage (V), e.g. 0.0
    vpv15: Union[EmptyStrToNone, float] = None  # PV15 voltage (V), e.g. 0.0
    vpv16: Union[EmptyStrToNone, float] = None  # PV16 voltage (V), e.g. 0.0
    w_pid_fault_value: Union[EmptyStrToNone, int] = None  # e.g. 0
    w_string_status_value: Union[EmptyStrToNone, int] = None  # e.g. 0
    warn_bit: Union[EmptyStrToNone, int] = None  # Fault bit, e.g. 0
    warn_code: Union[EmptyStrToNone, int] = None  # Warning code, e.g. 220
    warning_value1: Union[EmptyStrToNone, int] = None  # Warning value 1, e.g. 0
    warning_value2: Union[EmptyStrToNone, int] = None  # Warning value 2, e.g. 0
    warning_value3: Union[EmptyStrToNone, int] = None  # Warning value 3, e.g. 0
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the data sent has its own time, e.g. False


class MaxEnergyOverviewDataV4(ApiModel):
    max: List[MaxEnergyDataV4] = None


class MaxEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, MaxEnergyOverviewDataV4] = None


# ------------------------------------------------------------------------------------------------


class SphEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# ------------------------------------------------------------------------------------------------


class SpaEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# ------------------------------------------------------------------------------------------------


class MinEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# ------------------------------------------------------------------------------------------------


class WitEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# ------------------------------------------------------------------------------------------------


class SphsEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# ------------------------------------------------------------------------------------------------


class NoahEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# ------------------------------------------------------------------------------------------------
