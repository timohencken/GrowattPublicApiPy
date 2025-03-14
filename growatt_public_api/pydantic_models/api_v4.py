import datetime
from typing import List, Union, Any, Optional, Annotated, TypeAlias

from pydantic import ConfigDict, BeforeValidator
from pydantic.alias_generators import to_camel

from pydantic_models.api_model import (
    NewApiResponse,
    ApiModel,
    EmptyStrToNone,
)


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

    create_date: Union[EmptyStrToNone, datetime.datetime] = (
        None  # Date Added, e.g. '2024-11-30 17:37:26'
    )
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # Collector Serial Number, e.g. 'QMN000BZP3N6U09K'
    )
    device_sn: Union[EmptyStrToNone, str] = (
        None  # Device Serial Number, e.g. 'BZP3N6U09K'
    )
    device_type: Union[EmptyStrToNone, str] = None  # Device Type, e.g. 'min'


class DeviceListDataV4(ApiModel):
    count: Union[EmptyStrToNone, int] = None  # Device Count, e.g. 1
    data: List[DeviceDataV4] = []
    last_pager: Union[EmptyStrToNone, bool] = None  # e.g. True
    not_pager: Union[EmptyStrToNone, bool] = None  # e.g. False
    other: Union[EmptyStrToNone, Any] = None  # e.g. None
    page_size: Union[EmptyStrToNone, int] = None  # e.g. 100
    pages: Union[EmptyStrToNone, int] = None  # e.g. 1
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
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # Associated data logger serial number, e.g. "JPC2101182"
    )
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
    last_update_time: Union[EmptyStrToNone, int] = (
        None  # Last update time, e.g. 1613805596000
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. "2021-02-20 15:19:56"
    )
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    load_text: Union[EmptyStrToNone, str] = None  # e.g. "0%"
    location: Union[EmptyStrToNone, str] = None  # Address, e.g. "在这"
    lost: Union[EmptyStrToNone, bool] = (
        None  # Device online status (0: online, 1: offline), e.g. True
    )
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
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: waiting, 1: normal, 3: fault), e.g. -1
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. "inverter.status.lost"
    tcp_server_ip: Union[EmptyStrToNone, str] = (
        None  # Server address, e.g. "192.168.3.35"
    )
    temperature: Union[EmptyStrToNone, float] = None  # e.g. 0.0
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
    fw_version: Union[EmptyStrToNone, str] = (
        None  # Firmware version of the energy storage device, e.g. "067.01/068.01"
    )
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Software version, e.g. 'null'
    last_update_time: Union[EmptyStrToNone, int] = (
        None  # Last update time, e.g. 1716979679000
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # Last update time, e.g. '2024-05-29 18:47:59'
    )
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    li_battery_protocol_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    location: Union[EmptyStrToNone, str] = None  # Address, e.g. ""
    lost: Union[EmptyStrToNone, bool] = (
        None  # Device online status (0: Online, 1: Offline), e.g. True
    )
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
    sys_time: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. '2024-05-29 07:57',
    )
    tcp_server_ip: Union[EmptyStrToNone, str] = (
        None  # Server address, e.g. "47.119.28.147"
    )
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
        "pv_pf_cmd_memory_state_sph": "pvPfCmdMemoryState",  # avoid name collision
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
        "wcharge_soc_low_limit1": "wchargeSOCLowLimit1",
        "wcharge_soc_low_limit2": "wchargeSOCLowLimit2",
        "wdis_charge_soc_low_limit1": "wdisChargeSOCLowLimit1",
        "wdis_charge_soc_low_limit2": "wdisChargeSOCLowLimit2",
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

    ac_charge_enable: Union[EmptyStrToNone, bool] = None  # AC charging enable, e.g. 1
    active_rate: Union[EmptyStrToNone, int] = None  # Active power, e.g. 100
    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. 'OZD0849010'
    back_up_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    backflow_setting: Union[EmptyStrToNone, str] = (
        None  # Backflow prevention setting, e.g. None
    )
    bat_aging_test_step: Union[EmptyStrToNone, int] = (
        None  # battery self-test (0: default, 1: charge, 2: discharge), e.g. 0
    )
    bat_first_switch1: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_first_switch2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_first_switch3: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_parallel_num: Union[EmptyStrToNone, int] = (
        None  # Number of parallel cells, e.g. 0
    )
    bat_series_num: Union[EmptyStrToNone, int] = (
        None  # Number of cells in series, e.g. 0
    )
    bat_sys_rate_energy: Union[EmptyStrToNone, float] = None  # e.g. -0.1,
    bat_temp_lower_limit_c: Union[EmptyStrToNone, float] = (
        None  # Lower limit of battery charging temperature, e.g. 110.0
    )
    bat_temp_lower_limit_d: Union[EmptyStrToNone, float] = (
        None  # Lower limit of battery discharge temperature, e.g. 110.0
    )
    bat_temp_upper_limit_c: Union[EmptyStrToNone, float] = (
        None  # Upper limit of battery charging temperature, e.g. 60.0
    )
    bat_temp_upper_limit_d: Union[EmptyStrToNone, float] = (
        None  # Upper limit of battery discharge temperature, e.g. 70.0
    )
    battery_type: Union[EmptyStrToNone, int] = None  # Battery type selection, e.g. 1
    bct_adjust: Union[EmptyStrToNone, int] = None  # Sensor adjustment enable, e.g. 0
    bct_mode: Union[EmptyStrToNone, int] = (
        None  # Sensor type (0=cWiredCT, 1=cWirelessCT, 2=METER), e.g. 0
    )
    buck_ups_volt_set: Union[EmptyStrToNone, float] = None  # Off-grid voltage, e.g. 0
    buck_ups_fun_en: Union[EmptyStrToNone, bool] = None  # Off-grid enable, e.g. 1
    cc_current: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    charge_power_command: Union[EmptyStrToNone, int] = (
        None  # Charging power setting, e.g. 100
    )
    charge_time1: Union[EmptyStrToNone, str] = None  # e.g. None
    charge_time2: Union[EmptyStrToNone, str] = None  # e.g. None
    charge_time3: Union[EmptyStrToNone, str] = None  # e.g. None
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    com_address: Union[EmptyStrToNone, int] = None  # Mailing address, e.g. 1
    communication_version: Union[EmptyStrToNone, str] = (
        None  # Communication version number, e.g. 'GJAA-0003'
    )
    country_selected: Union[EmptyStrToNone, int] = None  # country selection, e.g. 0
    cv_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The serial number of the collector, e.g. 'JAD084800B'
    )
    device_type: Union[EmptyStrToNone, int] = None  # 0: Mix6k, 1: Mix4-10k, e.g. 0
    discharge_power_command: Union[EmptyStrToNone, int] = (
        None  # Discharge power setting, e.g. 100
    )
    discharge_time1: Union[EmptyStrToNone, str] = None  # e.g. None
    discharge_time2: Union[EmptyStrToNone, str] = None  # e.g. None
    discharge_time3: Union[EmptyStrToNone, str] = None  # e.g. None
    dtc: Union[EmptyStrToNone, int] = None  # Device code, e.g. 3501
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    eps_freq_set: Union[EmptyStrToNone, int] = None  # Emergency power frequency, e.g. 1
    eps_fun_en: Union[EmptyStrToNone, bool] = None  # Emergency power enable, e.g. 1
    eps_volt_set: Union[EmptyStrToNone, int] = (
        None  # Emergency power supply voltage, e.g. 1
    )
    export_limit: Union[EmptyStrToNone, int] = (
        None  # Backflow prevention enable, e.g. 0
    )
    export_limit_power_rate: Union[EmptyStrToNone, float] = (
        None  # Backflow prevention, e.g. 0.0
    )
    failsafe: Union[EmptyStrToNone, int] = None  # e.g. 0
    float_charge_current_limit: Union[EmptyStrToNone, float] = (
        None  # float charge current limit, e.g. 660.0
    )
    forced_charge_stop_switch1: Union[EmptyStrToNone, bool] = (
        None  # Charge 1 enable bit, e.g. 1
    )
    forced_charge_stop_switch2: Union[EmptyStrToNone, bool] = (
        None  # Charge 2 enable bit, e.g. 1
    )
    forced_charge_stop_switch3: Union[EmptyStrToNone, bool] = (
        None  # Charge 3 enable bit, e.g. 1
    )
    forced_charge_stop_switch4: Union[EmptyStrToNone, bool] = (
        None  # Charge 4 enable bit, e.g. 1
    )
    forced_charge_stop_switch5: Union[EmptyStrToNone, bool] = (
        None  # Charge 5 enable bit, e.g. 1
    )
    forced_charge_stop_switch6: Union[EmptyStrToNone, bool] = (
        None  # Charge 6 enable bit, e.g. 1
    )
    forced_charge_time_start1: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 1 start time, e.g. '18:0'
    )
    forced_charge_time_start2: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 2 start time, e.g. '21:30'
    )
    forced_charge_time_start3: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 3 start time, e.g. '3:0'
    )
    forced_charge_time_start4: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 4 start time, e.g. '3:0'
    )
    forced_charge_time_start5: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 5 start time, e.g. '3:0'
    )
    forced_charge_time_start6: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 6 start time, e.g. '3:0'
    )
    forced_charge_time_stop1: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 1 stop time, e.g. '19:30'
    )
    forced_charge_time_stop2: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 2 stop time, e.g. '23:0'
    )
    forced_charge_time_stop3: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 3 stop time, e.g. '4:30'
    )
    forced_charge_time_stop4: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 4 stop time, e.g. '4:30'
    )
    forced_charge_time_stop5: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 5 stop time, e.g. '4:30'
    )
    forced_charge_time_stop6: Union[EmptyStrToNone, ForcedTime] = (
        None  # Charge 6 stop time, e.g. '4:30'
    )
    forced_discharge_stop_switch1: Union[EmptyStrToNone, bool] = (
        None  # Discharge 1 enable bit, e.g. 1
    )
    forced_discharge_stop_switch2: Union[EmptyStrToNone, bool] = (
        None  # Discharge 2 enable bit, e.g. 1
    )
    forced_discharge_stop_switch3: Union[EmptyStrToNone, bool] = (
        None  # Discharge 3 enable bit, e.g. 1
    )
    forced_discharge_stop_switch4: Union[EmptyStrToNone, bool] = (
        None  # Discharge 4 enable bit, e.g. 1
    )
    forced_discharge_stop_switch5: Union[EmptyStrToNone, bool] = (
        None  # Discharge 5 enable bit, e.g. 1
    )
    forced_discharge_stop_switch6: Union[EmptyStrToNone, bool] = (
        None  # Discharge 6 enable bit, e.g. 1
    )
    forced_discharge_time_start1: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 1 start time, e.g. '0:0'
    )
    forced_discharge_time_start2: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 2 start time, e.g. '0:0'
    )
    forced_discharge_time_start3: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 3 start time, e.g. '0:0'
    )
    forced_discharge_time_start4: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 4 start time, e.g. '0:0'
    )
    forced_discharge_time_start5: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 5 start time, e.g. '0:0'
    )
    forced_discharge_time_start6: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 6 start time, e.g. '0:0'
    )
    forced_discharge_time_stop1: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 1 stop time, e.g. '0:0'
    )
    forced_discharge_time_stop2: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 2 stop time, e.g. '0:0'
    )
    forced_discharge_time_stop3: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 3 stop time, e.g. '0:0'
    )
    forced_discharge_time_stop4: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 4 stop time, e.g. '0:0'
    )
    forced_discharge_time_stop5: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 5 stop time, e.g. '0:0'
    )
    forced_discharge_time_stop6: Union[EmptyStrToNone, ForcedTime] = (
        None  # Discharge 6 stop time, e.g. '0:0'
    )
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'RA1.0'
    grid_first_switch1: Union[EmptyStrToNone, bool] = None  # e.g. 0
    grid_first_switch2: Union[EmptyStrToNone, bool] = None  # e.g. 0
    grid_first_switch3: Union[EmptyStrToNone, bool] = None  # e.g. 0
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    in_power: Union[EmptyStrToNone, float] = None  # e.g. 20.0
    inner_version: Union[EmptyStrToNone, str] = (
        None  # Internal version number, e.g. 'GJAA03xx'
    )
    inv_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    last_update_time: Union[EmptyStrToNone, int] = (
        None  # Last update time, e.g. 1716535653000
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. '2024-05-24 15:27:33'
    )
    lcd_language: Union[EmptyStrToNone, int] = None  # e.g. 1
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    load_first_control: Union[EmptyStrToNone, int] = None  # e.g. 0
    load_first_stop_soc_set: Union[EmptyStrToNone, int] = None  # e.g. 0
    location: Union[EmptyStrToNone, str] = None  # address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = (
        None  # Device online status (0: online, 1: disconnected), e.g. True
    )
    lv_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    manufacturer: Union[EmptyStrToNone, str] = (
        None  # Manufacturer Code, e.g. 'New Energy'
    )
    mc_version: Union[EmptyStrToNone, str] = None  # e.g. 'null'
    mix_ac_discharge_frequency: Union[EmptyStrToNone, float] = (
        None  # Off-grid frequency, e.g. None
    )
    mix_ac_discharge_voltage: Union[EmptyStrToNone, float] = (
        None  # Off-grid voltage, e.g. None
    )
    mix_off_grid_enable: Union[EmptyStrToNone, bool] = (
        None  # Off-grid enable, e.g. None
    )
    modbus_version: Union[EmptyStrToNone, int] = None  # MODBUS version, e.g. 305
    model: Union[EmptyStrToNone, int] = None  # model, e.g. 1159635200000
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'A0B0DBT0PFU2M4S0'
    monitor_version: Union[EmptyStrToNone, str] = None  # e.g. 'null'
    new_sw_version_flag: Union[EmptyStrToNone, int] = None  # e.g. 0
    off_grid_discharge_soc: Union[EmptyStrToNone, int] = None  # e.g. -1
    old_error_flag: Union[EmptyStrToNone, int] = None  # e.g. 0
    on_off: Union[EmptyStrToNone, bool] = None  # Switch machine, e.g. 0
    out_power: Union[EmptyStrToNone, float] = None  # e.g. 20.0
    p_charge: Union[EmptyStrToNone, int] = None  # e.g. 0
    p_discharge: Union[EmptyStrToNone, int] = None  # e.g. 0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_JAD084800B_96'
    pf_sys_year: Union[EmptyStrToNone, str] = None  # Set time, e.g. None
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. None
    pmax: Union[EmptyStrToNone, int] = None  # Rated power, e.g. 0
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'ShinePano - JAD084800B'
    power_factor: Union[EmptyStrToNone, float] = None  # PF value, e.g. 0.0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. None
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. None
    priority_choose: Union[EmptyStrToNone, int] = (
        None  # Energy priority selection, e.g. 1
    )
    pv_pf_cmd_memory_state_sph: Union[EmptyStrToNone, bool] = (
        None  # Set whether to store the following PF commands, e.g. ''
    )
    pv_active_p_rate: Union[EmptyStrToNone, float] = None  # Set active power, e.g. ''
    pv_grid_voltage_high: Union[EmptyStrToNone, float] = (
        None  # Mains voltage upper limit, e.g. ''
    )
    pv_grid_voltage_low: Union[EmptyStrToNone, float] = (
        None  # Mains voltage lower limit, e.g. ''
    )
    pv_on_off: Union[EmptyStrToNone, bool] = None  # Switch, e.g. ''
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, bool] = (
        None  # Set whether to store the following PF commands, e.g. ''
    )
    pv_pf_cmd_memory_state_mix: Union[EmptyStrToNone, bool] = (
        None  # mix Does the inverter store the following commands, e.g. 1
    )
    pv_power_factor: Union[EmptyStrToNone, float] = None  # Set PF value, e.g. ''
    pv_reactive_p_rate: Union[EmptyStrToNone, float] = (
        None  # Set reactive power, e.g. ''
    )
    pv_reactive_p_rate_two: Union[EmptyStrToNone, float] = (
        None  # No power capacity/inductive, e.g. ''
    )
    reactive_delay: Union[EmptyStrToNone, float] = None  # e.g. 150.0
    reactive_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 48.0
    reactive_rate: Union[EmptyStrToNone, int] = None  # Reactive power, e.g. 100
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    region: Union[EmptyStrToNone, int] = None  # e.g. -1
    safety: Union[EmptyStrToNone, str] = None  # e.g. '00'
    safety_num: Union[EmptyStrToNone, str] = None  # e.g. '4E'
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'FDCJQ00003'
    sgip_en: Union[EmptyStrToNone, bool] = None  # e.g. 0
    single_export: Union[EmptyStrToNone, int] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = (
        None  # Mix Status (0: Waiting Mode, 1: Self-check Mode, 3: Fault Mode, 4: Upgrading, 5-8: Normal Mode), e.g. 5
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'mix.status.normal'
    sys_time: Union[EmptyStrToNone, datetime.datetime] = (
        None  # System Time, e.g. '2019-03-05 10:37:29'
    )
    sys_time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. '2024-05-24 05:20:52'
    )
    tcp_server_ip: Union[EmptyStrToNone, str] = (
        None  # Server address, e.g. '47.119.173.58'
    )
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_FDCJQ00003'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    under_excited: Union[EmptyStrToNone, int] = None  # Capacitive or Perceptual, e.g. 0
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. None
    usp_freq_set: Union[EmptyStrToNone, int] = None  # Off-grid frequency, e.g. 0
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
    vbat_start_for_discharge: Union[EmptyStrToNone, float] = (
        None  # Lower limit of battery discharge voltage, e.g. 48.0
    )
    vbat_start_for_charge: Union[EmptyStrToNone, float] = (
        None  # Battery charging upper limit voltage, e.g. 58.0
    )
    vbat_stop_for_charge: Union[EmptyStrToNone, float] = (
        None  # Battery charging stop voltage, e.g. 5.75
    )
    vbat_stop_for_discharge: Union[EmptyStrToNone, float] = (
        None  # Battery discharge stop voltage, e.g. 4.7
    )
    vbat_warn_clr: Union[EmptyStrToNone, float] = (
        None  # Low battery voltage recovery point, e.g. 5.0
    )
    vbat_warning: Union[EmptyStrToNone, float] = (
        None  # Low battery voltage alarm point, e.g. 480.0
    )
    vnormal: Union[EmptyStrToNone, float] = None  # Rated PV voltage, e.g. 360.0
    voltage_high_limit: Union[EmptyStrToNone, float] = (
        None  # Mains voltage upper limit, e.g. 263.0
    )
    voltage_low_limit: Union[EmptyStrToNone, float] = (
        None  # Mains voltage lower limit, e.g. 186.0
    )
    vpp_open: Union[EmptyStrToNone, float] = None  # e.g. 0
    wcharge_soc_low_limit1: Union[EmptyStrToNone, int] = (
        None  # Load priority mode charging, e.g. 100
    )
    wcharge_soc_low_limit2: Union[EmptyStrToNone, int] = (
        None  # Battery priority mode charging, e.g. 100
    )
    wdis_charge_soc_low_limit1: Union[EmptyStrToNone, int] = (
        None  # Discharge in load priority mode, e.g. 100
    )
    wdis_charge_soc_low_limit2: Union[EmptyStrToNone, int] = (
        None  # Grid priority mode discharge, e.g. 5
    )
    baudrate: Union[EmptyStrToNone, int] = None  # Baud rate selection, e.g. 0


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

    # TODO

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
    last_update_time: Union[EmptyStrToNone, int] = (
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


class MaxDetailsDataV4(ApiModel):
    max: List[MaxDetailDataV4] = None


class MaxDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, MaxDetailsDataV4] = None


class MaxDetailsV4Max(NewApiResponse):
    data: Union[EmptyStrToNone, InverterDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


class SpaDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


class MinDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


class WitDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


class SphsDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


class NoahDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterDetailsDataV4] = None
