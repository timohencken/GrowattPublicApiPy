import datetime
from typing import List, Union, Any, Dict

from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from .api_model import (
    NewApiResponse,
    ApiModel,
    EmptyStrToNone,
    ForcedTime,
)


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
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. 1613805596000
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


def _inverter_details_data_to_camel(snake: str) -> str:
    override = {
        "devices": "inv",
    }
    return override.get(snake, to_camel(snake=snake))


class InverterDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_inverter_details_data_to_camel,
    )

    devices: List[InverterDetailDataV4] = None


class InverterDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


def _storage_details_to_camel(snake: str) -> str:
    override = {
        "ac_max_charge_curr": "acmaxChargeCurr",
        "address": "addr",
        "buzzer_en": "buzzerEN",
        "datalogger_sn": "dataLogSn",
        "feed_uti_high_frequency_loss": "feedUtiHihFrequencyLoss",
        "gfci_protect_set": "gfciprotectSet",
        "no_afci": "noAFCI",
        "out_ct_sample_rate_set": "outCTSampleRateSet",
        "out_ct_set": "outCTSet",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "rate_va": "rateVA",
        "relay_ng": "relayNG",
        "tree_id": "treeID",
        "user_id": "userID",
        "uti_output2_off_soc": "utiOutput2OffSOC",
        "uti_output2_on_soc": "utiOutput2OnSOC",
        "uw_fault_restart_en": "uwFaultResartEn",
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
    anti_reverse_flow_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    b_light_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_low_to_uti_volt: Union[EmptyStrToNone, float] = None  # e.g. 46.0
    battery_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    battery_undervoltage_cutoff_point: Union[EmptyStrToNone, float] = None  # e.g. 42.0
    bulk_charge_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    buzzer_en: Union[EmptyStrToNone, int] = None  # e.g. 1
    charge_config: Union[EmptyStrToNone, int] = None  # e.g. 0
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. None
    chip_select: Union[EmptyStrToNone, int] = None  # e.g. 0
    comboard_version: Union[EmptyStrToNone, int] = None  # e.g. 14300
    communication_version: Union[EmptyStrToNone, str] = None  # e.g. None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # SN of the data logger associated with the energy storage device, e.g. "DDD0CGA0CF"
    )
    debug_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 3
    dtc: Union[EmptyStrToNone, int] = None  # e.g. 20105
    feed_uti_high_voltage_loss: Union[EmptyStrToNone, float] = None  # e.g. 0
    feed_uti_high_frequency_loss: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    feed_uti_low_frequency_loss: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    feed_uti_low_voltage_loss: Union[EmptyStrToNone, float] = None  # e.g. 0
    float_charge_volt: Union[EmptyStrToNone, float] = None  # e.g. 54.0
    fw_version: Union[EmptyStrToNone, str] = None  # Firmware version of the energy storage device, e.g. "067.01/068.01"
    gen_dry_contact_en: Union[EmptyStrToNone, bool] = None  # e.g. 0
    gfci_protect_set: Union[EmptyStrToNone, int] = None  # e.g. 0
    ground_line_detection: Union[EmptyStrToNone, int] = None  # e.g. 0
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Software version, e.g. 'null'
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. 1716979679000
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
    max_gen_chg_curr: Union[EmptyStrToNone, float] = None  # e.g. 20.0
    max_gen_run_time: Union[EmptyStrToNone, float] = None  # e.g. 0
    menu_return: Union[EmptyStrToNone, int] = None  # e.g. 0
    model: Union[EmptyStrToNone, int] = None  # e.g. 0
    model_text: Union[EmptyStrToNone, str] = None  # e.g. "A0B0D0T0P0U0M0S0"
    no_afci: Union[EmptyStrToNone, int] = None  # e.g. 0
    out_ct_sample_rate_set: Union[EmptyStrToNone, int] = None  # e.g. 0
    out_ct_set: Union[EmptyStrToNone, int] = None  # e.g. 0
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
    pvios_detection: Union[EmptyStrToNone, int] = None  # e.g. 0
    rate_va: Union[EmptyStrToNone, float] = None  # e.g. 5000
    rate_watt: Union[EmptyStrToNone, float] = None  # e.g. 5000
    record: Union[EmptyStrToNone, str] = None  # e.g. None
    redundant_relay_detection: Union[EmptyStrToNone, int] = None  # e.g. 0
    regulation_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    relay_ng: Union[EmptyStrToNone, int] = None  # e.g. 0
    reset_to_factory: Union[EmptyStrToNone, int] = None  # e.g. 0
    sci_loss_chk_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'JNK1CJM0GR'
    smart_port: Union[EmptyStrToNone, int] = None  # e.g. 0
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
    typical_set: Union[EmptyStrToNone, int] = None  # e.g. 0
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. None
    uti_charge_end: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_charge_end_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_charge_start: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_charge_start_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_en_output2_always_on: Union[EmptyStrToNone, int] = None  # e.g. 0
    uti_out_end: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_out_end_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_out_start: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_out_start_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_output2_off_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_output2_off_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uti_output2_on_pv: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uti_output2_on_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_output2_on_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uti_output2_time_end1: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_output2_time_end2: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_output2_time_end3: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_output2_time_start1: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_output2_time_start2: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_output2_time_start3: Union[EmptyStrToNone, str] = None  # e.g. ''
    uti_peak_shaving_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uti_peak_shaving_set: Union[EmptyStrToNone, int] = None  # e.g. 0
    utility_priority: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_bat_community_fail_en: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_bat_feed_curr: Union[EmptyStrToNone, float] = None  # e.g. 250.0
    uw_bat_feed_en: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_bat_feed_soc_back: Union[EmptyStrToNone, float] = None  # e.g. 90
    uw_bat_feed_soc_loss: Union[EmptyStrToNone, float] = None  # e.g. 50
    uw_bat_feed_time_end1: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_bat_feed_time_end1_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_bat_feed_time_end2: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_bat_feed_time_end2_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_bat_feed_time_end3: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_bat_feed_time_end3_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_bat_feed_time_start1: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_bat_feed_time_start1_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_bat_feed_time_start2: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_bat_feed_time_start2_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_bat_feed_time_start3: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_bat_feed_time_start3_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_bat_feed_v_back: Union[EmptyStrToNone, float] = None  # e.g. 54.0
    uw_bat_feed_v_loss: Union[EmptyStrToNone, float] = None  # e.g. 50.0
    uw_bat_type2: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_fault_restart_en: Union[EmptyStrToNone, bool] = None  # e.g. 1
    uw_feed_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_feed_pow: Union[EmptyStrToNone, float] = None  # e.g. 12.0
    uw_feed_range: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_grid_chg_time_end1: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_grid_chg_time_end1_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_grid_chg_time_end2: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_grid_chg_time_end2_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_grid_chg_time_end3: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_grid_chg_time_end3_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_grid_chg_time_start1: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_grid_chg_time_start1_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_grid_chg_time_start2: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_grid_chg_time_start2_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_grid_chg_time_start3: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_grid_chg_time_start3_new: Union[EmptyStrToNone, str] = None  # e.g. ''
    uw_load_first: Union[EmptyStrToNone, float] = None  # e.g. 0
    var1_address: Union[EmptyStrToNone, int] = None  # e.g. 0
    var1_setting: Union[EmptyStrToNone, int] = None  # e.g. 0
    var1_value: Union[EmptyStrToNone, int] = None  # e.g. 0
    var2_address: Union[EmptyStrToNone, int] = None  # e.g. 0
    var2_value: Union[EmptyStrToNone, int] = None  # e.g. 0


def _storage_details_data_to_camel(snake: str) -> str:
    override = {
        "devices": "storage",
    }
    return override.get(snake, to_camel(snake=snake))


class StorageDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_storage_details_data_to_camel,
    )

    devices: List[StorageDetailDataV4] = None


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
        "grid_hv_reduce_load_high": "gridHVReduceLoadHigh",
        "grid_hv_reduce_load_low": "gridHVReduceLoadLow",
        "off_grid_discharge_soc": "offGridDischargeSOC",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "pv_pf_cmd_memory_state_mix": "pvPfCmdMemoryState",  # avoid name collision
        "pv_pf_cmd_memory_state": "pv_pf_cmd_memory_state",  # avoid name collision
        "qv_out_hv_power_per": "qvOutHVPowerPer",
        "qv_in_lv_power_per": "qvInLVPowerPer",
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
    active_rate: Union[EmptyStrToNone, float] = None  # Active power, e.g. 100
    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # Alias, e.g. 'OZD0849010'
    anti_island_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
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
    device_model: Union[EmptyStrToNone, Any] = None  # e.g. None
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
    grid_hv_reduce_load_high: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    grid_hv_reduce_load_low: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    group_id: Union[EmptyStrToNone, int] = None  # Inverter Group, e.g. -1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    in_power: Union[EmptyStrToNone, float] = None  # e.g. 20.0
    inner_version: Union[EmptyStrToNone, str] = None  # Internal Version Number, e.g. 'GJAA03xx'
    inv_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last Update Time, e.g. 1716535653000
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
    qv_out_hv_power_per: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    qv_in_lv_power_per: Union[EmptyStrToNone, float] = None  # e.g. 1
    reactive_delay: Union[EmptyStrToNone, float] = None  # e.g. 150.0
    reactive_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 48.0
    reactive_rate: Union[EmptyStrToNone, float] = None  # Reactive power, e.g. 100
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
    vpp_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    w_charge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load Priority Mode Charge, e.g. 100
    w_charge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Battery Priority Mode Charge, e.g. 100
    w_discharge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load Priority Mode Discharge, e.g. 100
    w_discharge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Grid Priority Mode Discharge, e.g. 5
    baudrate: Union[EmptyStrToNone, int] = None  # Baud Rate Selection, e.g. 0


def _sph_details_data_to_camel(snake: str) -> str:
    override = {
        "devices": "sph",
    }
    return override.get(snake, to_camel(snake=snake))


class SphDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sph_details_data_to_camel,
    )

    devices: List[SphDetailDataV4] = None


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
    export_limit: Union[EmptyStrToNone, int] = None  # e.g. 0
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
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. 1716534733000
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-24 15:12:13'
    lcd_language: Union[EmptyStrToNone, int] = None  # e.g. 0
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    location: Union[EmptyStrToNone, str] = None  # Address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: offline), e.g. True
    max_set_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    model: Union[EmptyStrToNone, int] = None  # model, e.g. 720575940631003386
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'S0AB00D00T00P0FU01M00FA'
    normal_power: Union[EmptyStrToNone, int] = None  # Rated power, e.g. 25000
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
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, bool] = None  # e.g. 0
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


def _max_details_data_to_camel(snake: str) -> str:
    override = {
        "devices": "max",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_details_data_to_camel,
    )

    devices: List[MaxDetailDataV4] = None


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
    export_limit: Union[EmptyStrToNone, int] = None  # e.g. 0
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
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last Update Time, e.g. 1716435475000
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
    vpp_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    w_charge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load Priority Mode Charge, e.g. 100
    w_charge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Battery Priority Mode Charge, e.g. 100
    w_discharge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load Priority Mode Discharge, e.g. 100
    w_discharge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Grid Priority Mode Discharge, e.g. 5
    w_load_soc_low_limit1: Union[EmptyStrToNone, int] = None  # e.g. 0
    w_load_soc_low_limit2: Union[EmptyStrToNone, int] = None  # e.g. 0
    baudrate: Union[EmptyStrToNone, int] = None  # Baud Rate Selection, e.g. 0


def _spa_details_data_to_camel(snake: str) -> str:
    override = {
        "devices": "spa",
    }
    return override.get(snake, to_camel(snake=snake))


class SpaDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spa_details_data_to_camel,
    )

    devices: List[SpaDetailDataV4] = None


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

    afci_version: Union[EmptyStrToNone, str] = None  # e.g. ''
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
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. 1716535759000
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
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # System time, e.g. ''
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


def _min_details_data_to_camel(snake: str) -> str:
    override = {
        "devices": "min",
    }
    return override.get(snake, to_camel(snake=snake))


class MinDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_min_details_data_to_camel,
    )

    devices: List[MinDetailDataV4] = None


class MinDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, MinDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


def _wit_details_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "communication_version": "comVersion",
        "datalogger_sn": "dataLogSn",
        "parent_id": "parentID",
        "line_n_disconnect_enable": "lineNdisconnectEnable",
        "outer_ct_enable": "outerCTEnable",
        "over_freq_drop_point": "overFreDropPoint",
        "over_freq_load_reduction_delay_time": "overFreLoRedDelayTime",
        "over_freq_load_reduction_reset_time": "overFreLoRedResTime",
        "over_freq_load_reduction_slope": "overFreLoRedSlope",
        "power_ud_forced_enable": "powerUDForcedEnable",
        "safety_function": "saftyFunc",
        "under_freq_load_delay_time": "underfreqLoadDelayTime",
        "under_freq_load_enable": "underfreqLoadEnable",
        "under_freq_load_point": "underfreqLoadPoint",
        "under_freq_load_reset_time": "underfreqLoadResTime",
        "under_freq_load_slope": "underfreqLoadSlope",
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
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. 1716963248000
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
    outer_ct_enable: Union[EmptyStrToNone, bool] = None  # e.g. 1
    over_freq_drop_point: Union[EmptyStrToNone, float] = None  # Over frequency drop point, e.g. 50.3
    over_freq_load_reduction_delay_time: Union[EmptyStrToNone, float] = (
        None  # Over frequency load reduction delay time, e.g. 0.0
    )
    over_freq_load_reduction_reset_time: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    over_freq_load_reduction_slope: Union[EmptyStrToNone, float] = None  # Over frequency derating slope, e.g. 50
    over_freq_time1: Union[EmptyStrToNone, int] = None  # e.g. 0
    over_freq_time2: Union[EmptyStrToNone, int] = None  # e.g. 0
    over_freq_time3: Union[EmptyStrToNone, int] = None  # e.g. 0
    over_volt_time1: Union[EmptyStrToNone, int] = None  # e.g. 0
    over_volt_time2: Union[EmptyStrToNone, int] = None  # e.g. 0
    over_volt_time3: Union[EmptyStrToNone, int] = None  # e.g. 0
    parallel_enable: Union[EmptyStrToNone, bool] = None  # e.g. 1
    parallel_num: Union[EmptyStrToNone, int] = None  # e.g. 0
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
    second_load_down_soc: Union[EmptyStrToNone, int] = None  # e.g. -1
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. '0ZFN00R23ZBF0002'
    single_export: Union[EmptyStrToNone, int] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = None  # Device Status, e.g. 0
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'wit.status.operating'
    str_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    svg_function: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_optical_storage_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # System time, e.g. ''
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
    under_freq_load_delay_time: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    under_freq_load_enable: Union[EmptyStrToNone, int] = None  # e.g. -1
    under_freq_load_point: Union[EmptyStrToNone, float] = None  # e.g. 49.8
    under_freq_load_reset_time: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    under_freq_load_slope: Union[EmptyStrToNone, int] = None  # e.g. 400
    under_freq_time1: Union[EmptyStrToNone, int] = None  # e.g. 0
    under_freq_time2: Union[EmptyStrToNone, int] = None  # e.g. 0
    under_freq_time3: Union[EmptyStrToNone, int] = None  # e.g. 0
    under_volt_time1: Union[EmptyStrToNone, int] = None  # e.g. 0
    under_volt_time2: Union[EmptyStrToNone, int] = None  # e.g. 0
    under_volt_time3: Union[EmptyStrToNone, int] = None  # e.g. 0
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
    vpp_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    vpv_start: Union[EmptyStrToNone, float] = None  # e.g. 250.0
    w_anti_backflow_meter_power_limit: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    w_power_restart_slope_ee: Union[EmptyStrToNone, float] = None  # e.g. 50.0
    w_power_start_slope: Union[EmptyStrToNone, float] = None  # e.g. 50.0
    wide_voltage_enable: Union[EmptyStrToNone, bool] = None  # e.g. 0
    baudrate: Union[EmptyStrToNone, int] = None  # Baud Rate Selection, e.g. 0


def _wit_details_data_to_camel(snake: str) -> str:
    override = {
        "devices": "wit",
    }
    return override.get(snake, to_camel(snake=snake))


class WitDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_wit_details_data_to_camel,
    )

    devices: List[WitDetailDataV4] = None


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

    active_rate: Union[EmptyStrToNone, float] = None  # Active power, e.g. 100
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
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last Update Time, e.g. 1716963973000
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
    reactive_rate: Union[EmptyStrToNone, float] = None  # Reactive power, e.g. 100
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
        "devices": "sph-s",
    }
    return override.get(snake, to_camel(snake=snake))


class SphsDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sphs_details_data_to_camel,
    )

    devices: List[SphsDetailDataV4] = None


class SphsDetailsV4(NewApiResponse):
    data: Union[EmptyStrToNone, SphsDetailsDataV4] = None


# ------------------------------------------------------------------------------------------------


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
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. 1720667148000
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
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # System time, e.g. 1720660008000
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


def _noah_details_data_to_camel(snake: str) -> str:
    override = {
        "devices": "noah",
    }
    return override.get(snake, to_camel(snake=snake))


class NoahDetailsDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_noah_details_data_to_camel,
    )

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
    inverter_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
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
    time_calendar: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. 1716627393328
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


def _inverter_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "devices": "inv",
    }
    return override.get(snake, to_camel(snake=snake))


class InverterEnergyOverviewDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_inverter_energy_overview_data_to_camel,
    )

    devices: List[InverterEnergyDataV4] = None


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
    bms_info: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_max_current_charge: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_pack_info: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_soh: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_status2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_temperature2: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_using_cap: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_warn_info: Union[EmptyStrToNone, int] = None  # e.g. 0
    buck1_ntc_temperature: Union[EmptyStrToNone, float] = None  # Buck1 Temperature, e.g. 24.3
    buck2_ntc_temperature: Union[EmptyStrToNone, float] = None  # Buck2 Temperature, e.g. 28.2
    calendar: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. 1716985060479
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


def _storage_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "devices": "storage",
    }
    return override.get(snake, to_camel(snake=snake))


class StorageEnergyOverviewDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_storage_energy_overview_data_to_camel,
    )

    devices: List[StorageEnergyDataV4] = None


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
    calendar: Union[EmptyStrToNone, datetime.datetime] = None  # Time (Calendar), e.g. 1716618863392
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
    time_calendar: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. 1716618863392
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


def _max_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "devices": "max",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxEnergyOverviewDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_energy_overview_data_to_camel,
    )

    devices: List[MaxEnergyDataV4] = None


class MaxEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, MaxEnergyOverviewDataV4] = None


# ------------------------------------------------------------------------------------------------


def _sph_energy_to_camel(snake: str) -> str:
    override = {
        "acc_discharge_power": "accdischargePower",
        "capacity_add": "capacityADD",
        "datalogger_sn": "dataLogSn",
        "bms_fw": "bmsFW",
        "bms_gauge_fcc": "bmsGaugeFCC",
        "bms_gauge_rm": "bmsGaugeRM",
        "bms_max_discharge_curr": "bmsMaxDischgCurr",
        "bms_mcu_version": "bmsMCUVersion",
        "bms_soc": "bmsSOC",
        "bms_soh": "bmsSOH",
        "e_charge1_today": "echarge1Today",
        "e_charge1_total": "echarge1Total",
        "e_discharge1_today": "edischarge1Today",
        "e_discharge1_total": "edischarge1Total",
        "e_local_load_today": "elocalLoadToday",
        "e_local_load_total": "elocalLoadTotal",
        "epv_today": "epvtoday",
        "e_self_today": "eselftoday",
        "e_self_total": "eselftotal",
        "e_system_today": "esystemtoday",
        "e_system_total": "esystemtotal",
        "e_to_grid_today": "etoGridToday",
        "e_to_user_today": "etoUserToday",
        "e_to_user_total": "etoUserTotal",
        "e_to_grid_total": "etogridTotal",
        "first_batt_fault_sn": "firstBattFaultSn",
        "max_soc": "maxSOC",
        "min_soc": "minSOC",
        "p_self": "pself",
        "p_system": "psystem",
        "device_sn": "serialNum",  # align with other endpoints using "deviceSn" instead
        "ups_load_percent": "upsLoadpercent",
        "ups_pf": "upsPF",
    }
    return override.get(snake, to_camel(snake=snake))


class SphEnergyDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sph_energy_to_camel,
    )

    ac_charge_energy_today: Union[EmptyStrToNone, float] = None  # AC daily charge energy, e.g. 0.0
    ac_charge_energy_total: Union[EmptyStrToNone, float] = None  # AC total charge energy, e.g. 0.0
    ac_charge_power: Union[EmptyStrToNone, float] = None  # AC charge power, e.g. 0.0
    acc_charge_pack_sn: Union[EmptyStrToNone, int] = None  # e.g. -1
    acc_charge_power: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    acc_discharge_pack_sn: Union[EmptyStrToNone, int] = None  # e.g. -1
    acc_discharge_power: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. None
    b_module_num: Union[EmptyStrToNone, int] = None  # e.g. -1
    b_total_cell_num: Union[EmptyStrToNone, int] = None  # e.g. -1
    backup_warning: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_error_union: Union[EmptyStrToNone, int] = None  # e.g. 0
    batt_history_fault_code1: Union[EmptyStrToNone, int] = None  # e.g. -1
    batt_history_fault_code2: Union[EmptyStrToNone, int] = None  # e.g. -1
    batt_history_fault_code3: Union[EmptyStrToNone, int] = None  # e.g. -1
    batt_history_fault_code4: Union[EmptyStrToNone, int] = None  # e.g. -1
    batt_history_fault_code5: Union[EmptyStrToNone, int] = None  # e.g. -1
    batt_history_fault_code6: Union[EmptyStrToNone, int] = None  # e.g. -1
    batt_history_fault_code7: Union[EmptyStrToNone, int] = None  # e.g. -1
    batt_history_fault_code8: Union[EmptyStrToNone, int] = None  # e.g. -1
    battery_temperature: Union[EmptyStrToNone, float] = None  # Battery temperature, e.g. 0.0
    battery_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_battery_curr: Union[EmptyStrToNone, float] = None  # Battery current, e.g. 0.0
    bms_battery_temp: Union[EmptyStrToNone, float] = None  # Battery temperature, e.g. 28.0
    bms_battery_volt: Union[EmptyStrToNone, float] = None  # Battery voltage, e.g. 56.7400016784668
    bms_cell1_volt: Union[EmptyStrToNone, float] = None  # Battery cell 1 voltage, e.g. 3.5480000972747803
    bms_cell2_volt: Union[EmptyStrToNone, float] = None  # Battery cell 2 voltage, e.g. 3.5480000972747803
    bms_cell3_volt: Union[EmptyStrToNone, float] = None  # Battery cell 3 voltage, e.g. 3.549999952316284
    bms_cell4_volt: Union[EmptyStrToNone, float] = None  # Battery cell 4 voltage, e.g. 3.549999952316284
    bms_cell5_volt: Union[EmptyStrToNone, float] = None  # Battery cell 5 voltage, e.g. 3.549999952316284
    bms_cell6_volt: Union[EmptyStrToNone, float] = None  # Battery cell 6 voltage, e.g. 3.5510001182556152
    bms_cell7_volt: Union[EmptyStrToNone, float] = None  # Battery cell 7 voltage, e.g. 3.549999952316284
    bms_cell8_volt: Union[EmptyStrToNone, float] = None  # Battery cell 8 voltage, e.g. 3.549999952316284
    bms_cell9_volt: Union[EmptyStrToNone, float] = None  # Battery cell 9 voltage, e.g. 3.513000011444092
    bms_cell10_volt: Union[EmptyStrToNone, float] = None  # Battery cell 10 voltage, e.g. 3.549999952316284
    bms_cell11_volt: Union[EmptyStrToNone, float] = None  # Battery cell 11 voltage, e.g. 3.549999952316284
    bms_cell12_volt: Union[EmptyStrToNone, float] = None  # Battery cell 12 voltage, e.g. 3.549999952316284
    bms_cell13_volt: Union[EmptyStrToNone, float] = None  # Battery cell 13 voltage, e.g. 3.5490000247955322
    bms_cell14_volt: Union[EmptyStrToNone, float] = None  # Battery cell 14 voltage, e.g. 3.5490000247955322
    bms_cell15_volt: Union[EmptyStrToNone, float] = None  # Battery cell 15 voltage, e.g. 3.5490000247955322
    bms_cell16_volt: Union[EmptyStrToNone, float] = None  # Battery cell 16 voltage, e.g. 3.549999952316284
    bms_constant_volt: Union[EmptyStrToNone, float] = None  # Battery constant voltage point, e.g. 56.79999923706055
    bms_cycle_cnt: Union[EmptyStrToNone, int] = None  # Battery cycle count, e.g. 1331
    bms_delta_volt: Union[EmptyStrToNone, float] = None  # Voltage difference between battery cells, e.g. 38.0
    bms_error: Union[EmptyStrToNone, int] = None  # Battery fault, e.g. 0
    bms_error2: Union[EmptyStrToNone, int] = None  # e.g. -1
    bms_error3: Union[EmptyStrToNone, int] = None  # e.g. -1
    bms_error_expansion: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_error_old: Union[EmptyStrToNone, int] = None  # Battery historical fault, e.g. 0
    bms_fw: Union[EmptyStrToNone, int] = None  # BMS firmware version number, e.g. 257
    bms_gauge_fcc: Union[EmptyStrToNone, float] = None  # Rated capacity, e.g. 100
    bms_gauge_rm: Union[EmptyStrToNone, float] = None  # System Capacity, e.g. 49.9900016784668
    bms_hardware_version: Union[EmptyStrToNone, int] = None  # e.g. -1
    bms_hardware_version2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_highest_soft_version: Union[EmptyStrToNone, int] = None  # e.g. -1
    bms_info: Union[EmptyStrToNone, float] = None  # BMS Information, e.g. 257
    bms_mcu_version: Union[EmptyStrToNone, int] = None  # BMS firmware version, e.g. 512
    bms_max_curr: Union[EmptyStrToNone, float] = None  # Maximum charge/discharge current, e.g. 100.0
    bms_max_discharge_curr: Union[EmptyStrToNone, float] = None  # Maximum discharge current, e.g. 0.0
    bms_pack_info: Union[EmptyStrToNone, float] = None  # Battery Pack Information, e.g. 257
    bms_protection: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_request_type: Union[EmptyStrToNone, int] = None  # e.g. -1
    bms_soc: Union[EmptyStrToNone, int] = None  # Battery state of charge, e.g. 100
    bms_soh: Union[EmptyStrToNone, int] = None  # Battery state of health, e.g. 47
    bms_status: Union[EmptyStrToNone, int] = None  # Battery Status, e.g. 361
    bms_status_old: Union[EmptyStrToNone, int] = None  # Battery historical status, e.g. 361
    bms_using_cap: Union[EmptyStrToNone, float] = None  # Battery pack power type, e.g. 5000
    bms_warn_info: Union[EmptyStrToNone, int] = None  # Battery warning information, e.g. 0
    bms_warn_info2: Union[EmptyStrToNone, int] = None  # e.g. -1
    bms_warn_info_old: Union[EmptyStrToNone, int] = None  # Battery historical warning information, e.g. 0
    calendar: Union[EmptyStrToNone, datetime.datetime] = None  # Time, e.g. 1716618931362
    capacity_add: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    charge_cutoff_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    charge_forbidden_mark: Union[EmptyStrToNone, Any] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'JAD084800B'
    day: Union[EmptyStrToNone, str] = None  # e.g. None
    day_map: Union[EmptyStrToNone, Any] = None  # , e.g. None
    discharge_cutoff_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    discharge_forbidden_mark: Union[EmptyStrToNone, int] = None  # e.g. 0
    dsgip_start_date_time: Union[EmptyStrToNone, int] = None  # e.g. None
    eac_today: Union[EmptyStrToNone, float] = None  # Inverter daily output energy, e.g. 21.600000381469727
    eac_total: Union[EmptyStrToNone, float] = None  # Inverter total output energy, e.g. 1859.5
    e_charge1_today: Union[EmptyStrToNone, float] = None  # Battery daily charge energy, e.g. 0.2
    e_charge1_total: Union[EmptyStrToNone, float] = None  # Total battery charge energy, e.g. 6113.2
    e_discharge1_today: Union[EmptyStrToNone, float] = None  # Battery daily discharge energy, e.g. 0.4
    e_discharge1_total: Union[EmptyStrToNone, float] = None  # Total battery discharge energy, e.g. 5540.6
    eex_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    eex_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_local_load_today: Union[EmptyStrToNone, float] = None  # Local load daily consumption energy, e.g. 0
    e_local_load_total: Union[EmptyStrToNone, float] = None  # Total local load consumption energy, e.g. 26980.8
    eps_vac2: Union[EmptyStrToNone, float] = None  # Off-grid side S phase voltage, e.g.  0
    eps_vac3: Union[EmptyStrToNone, float] = None  # Off-grid side T phase voltage, e.g. 0
    epv1_today: Union[EmptyStrToNone, float] = None  # PV1 daily generated energy, e.g. 13.199999809265137
    epv1_total: Union[EmptyStrToNone, float] = None  # PV1 total generated energy, e.g. 926.6
    epv2_today: Union[EmptyStrToNone, float] = None  # PV2 daily generated energy, e.g. 8.199999809265137
    epv2_total: Union[EmptyStrToNone, float] = None  # PV2 total generated energy, e.g. 906.4
    epv_total: Union[EmptyStrToNone, float] = None  # Total PV generated energy, e.g. 0
    epv_today: Union[EmptyStrToNone, float] = None  # e.g. 9.600000381469727
    error_code: Union[EmptyStrToNone, int] = None  # error code, e.g. 0
    error_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    e_self_today: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    e_self_total: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    e_system_today: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    e_system_total: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # Grid daily input energy, e.g. 0.3
    e_to_user_today: Union[EmptyStrToNone, float] = None  # Grid daily output energy, e.g. 0
    e_to_user_total: Union[EmptyStrToNone, float] = None  # Total grid output energy, e.g. 11991.1
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # Total grid input energy, e.g. 2293
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 50.0099983215332
    fault_bit_code: Union[EmptyStrToNone, int] = None  # Inverter fault bit code, e.g. 0
    fault_code: Union[EmptyStrToNone, int] = None  # Inverter fault code, e.g. 0
    first_batt_fault_sn: Union[EmptyStrToNone, int] = None  # e.g. -1
    fourth_batt_fault_sn: Union[EmptyStrToNone, int] = None  # e.g. -1
    iac1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    iac2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    iac3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    max_soc: Union[EmptyStrToNone, float] = None  # e.g. -1
    max_single_cell_tem: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    max_single_cell_tem_no: Union[EmptyStrToNone, int] = None  # e.g. 0
    max_single_cell_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    max_single_cell_volt_no: Union[EmptyStrToNone, int] = None  # e.g. 0
    min_soc: Union[EmptyStrToNone, float] = None  # e.g. -1
    min_single_cell_tem: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    min_single_cell_tem_no: Union[EmptyStrToNone, int] = None  # e.g. 0
    min_single_cell_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    min_single_cell_volt_no: Union[EmptyStrToNone, int] = None  # e.g. 0
    mix_bean: Union[EmptyStrToNone, Any] = None
    module_qty: Union[EmptyStrToNone, int] = None  # e.g. 0
    module_series_qty: Union[EmptyStrToNone, int] = None  # e.g. 0
    number_of_batt_codes: Union[EmptyStrToNone, int] = None  # e.g. -1
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 2503.8
    pac1: Union[EmptyStrToNone, float] = None  # Inverter apparent output power, e.g. 0
    pac2: Union[EmptyStrToNone, float] = None  # AC side power, e.g. 0
    pac3: Union[EmptyStrToNone, float] = None  # AC side power, e.g. 0
    pac_r: Union[EmptyStrToNone, float] = None  # e.g. 0
    pac_s: Union[EmptyStrToNone, float] = None  # e.g. 0
    pac_t: Union[EmptyStrToNone, float] = None  # e.g. 0
    pac_to_grid_r: Union[EmptyStrToNone, float] = None  # Grid reverse power, e.g. 38.6
    pac_to_grid_total: Union[EmptyStrToNone, float] = None  # Total grid reverse power, e.g. 38.6
    pac_to_user_r: Union[EmptyStrToNone, float] = None  # Grid forward power, e.g. 0
    pac_to_user_total: Union[EmptyStrToNone, float] = None  # Total grid forward power, e.g. 0
    pcharge1: Union[EmptyStrToNone, float] = None  # Battery charge power, e.g. 0
    pdischarge1: Union[EmptyStrToNone, float] = None  # Battery discharge power, e.g. 16.5
    pex: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    plocal_load_r: Union[EmptyStrToNone, float] = None  # Local load consumption power, e.g. 0
    plocal_load_r2: Union[EmptyStrToNone, float] = None  # e.g. 0
    plocal_load_s: Union[EmptyStrToNone, float] = None  # e.g. 0
    plocal_load_t: Union[EmptyStrToNone, float] = None  # e.g. 0
    plocal_load_total: Union[EmptyStrToNone, float] = None  # Total local load consumption power, e.g. 0
    pm_r: Union[EmptyStrToNone, float] = None  # e.g. 0
    pm_s: Union[EmptyStrToNone, float] = None  # e.g. 0
    pm_t: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv: Union[EmptyStrToNone, float] = None  # Total PV input power, e.g. 1058
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power, e.g. 1058
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power, e.g. 1058
    ppv_text: Union[EmptyStrToNone, str] = None  # e.g. '3.9 W'
    priority_choose: Union[EmptyStrToNone, float] = None  # e.g. 0
    protect_pack_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    p_self: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    p_system: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    second_batt_fault_sn: Union[EmptyStrToNone, int] = None  # e.g. -1
    device_sn: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. 'BNE9A5100D'
    sgip_cycl_cnt: Union[EmptyStrToNone, int] = None  # e.g. 0
    sgip_start_cycl_cnt: Union[EmptyStrToNone, int] = None  # e.g. 0
    soc: Union[EmptyStrToNone, float] = None  # Battery state of charge, e.g. 100
    soc_text: Union[EmptyStrToNone, str] = None  # e.g. '100%'
    software_develop_major_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    software_develop_minor_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    software_major_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    software_minor_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = None  # Mix Status 0 = waiting, 1 = normal, 2 = fault, e.g. 5
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'PV Bat Online'
    sys_en: Union[EmptyStrToNone, int] = None  # System enable bit, e.g. 17056
    sys_fault_word: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word1: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word2: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word3: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word4: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word5: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word6: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word7: Union[EmptyStrToNone, int] = None  # e.g. 256
    temp1: Union[EmptyStrToNone, float] = None  # Temperature 1, e.g. 34
    temp2: Union[EmptyStrToNone, float] = None  # Temperature 2, e.g. 33.099998474121094
    temp3: Union[EmptyStrToNone, float] = None  # Temperature 3, e.g. 33.099998474121094
    third_batt_fault_sn: Union[EmptyStrToNone, int] = None  # e.g. -1
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-25 14:35:31'
    time_total: Union[EmptyStrToNone, float] = None  # Total running time, e.g. 13534574.5
    ups_fac: Union[EmptyStrToNone, float] = None  # Emergency power frequency, e.g. 0
    ups_load_percent: Union[EmptyStrToNone, float] = None  # Emergency output load percentage, e.g. 0
    ups_pf: Union[EmptyStrToNone, float] = None  # Emergency output power factor, e.g. 1000
    ups_pac1: Union[EmptyStrToNone, float] = None  # Emergency apparent output power, e.g. 0
    ups_pac2: Union[EmptyStrToNone, float] = None  # Off-grid side power, e.g. 0
    ups_pac3: Union[EmptyStrToNone, float] = None  # Off-grid side power, e.g. 0
    ups_vac1: Union[EmptyStrToNone, float] = None  # Emergency voltage, e.g. 0
    uw_bat_cycle_cnt_pre: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_dc_dc_debug_data: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_dsp_dc_dc_debug_data1: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_dsp_dc_dc_debug_data2: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_dsp_dc_dc_debug_data3: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_dsp_dc_dc_debug_data4: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_dsp_inv_debug_data: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_dsp_inv_debug_data1: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_dsp_inv_debug_data2: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_dsp_inv_debug_data3: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_dsp_inv_debug_data4: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_max_cell_vol: Union[EmptyStrToNone, float] = None  # e.g. -0.0010000000474974513
    uw_max_tempr_cell: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    uw_max_tempr_cell_no: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_max_volt_cell_no: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_min_cell_vol: Union[EmptyStrToNone, float] = None  # e.g. -0.0010000000474974513
    uw_min_tempr_cell: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    uw_min_tempr_cell_no: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_min_volt_cell_no: Union[EmptyStrToNone, int] = None  # e.g. -1
    uw_sys_work_mode: Union[EmptyStrToNone, int] = None  # System working mode, e.g. 5
    v_bat_dsp: Union[EmptyStrToNone, float] = None  # DSP collected battery voltage, e.g. 0
    v_bus1: Union[EmptyStrToNone, float] = None  # Bus 1 voltage, e.g. 0
    v_bus2: Union[EmptyStrToNone, float] = None  # Bus 2 voltage, e.g. 0
    vac1: Union[EmptyStrToNone, float] = None  # Grid voltage, e.g. 219.89999389648438
    vac2: Union[EmptyStrToNone, float] = None  # AC side S phase voltage, e.g. 0
    vac3: Union[EmptyStrToNone, float] = None  # AC side T phase voltage, e.g. 0
    vbat: Union[EmptyStrToNone, float] = None  # battery voltage, e.g. 56.70000076293945
    vpv1: Union[EmptyStrToNone, float] = None  # PV1 input voltage, e.g. 0
    vpv2: Union[EmptyStrToNone, float] = None  # PV2 input voltage, e.g. 0.0
    warn_code: Union[EmptyStrToNone, int] = None  # Warning code, e.g. 220
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the incoming data includes time, e.g. False


def _sph_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "devices": "sph",
    }
    return override.get(snake, to_camel(snake=snake))


class SphEnergyOverviewDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sph_energy_overview_data_to_camel,
    )

    devices: List[SphEnergyDataV4] = None


class SphEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, SphEnergyOverviewDataV4] = None


# ------------------------------------------------------------------------------------------------


def _spa_energy_to_camel(snake: str) -> str:
    override = {
        "acc_discharge_power": "accdischargePower",
        "datalogger_sn": "dataLogSn",
        "bms_fw": "bmsFW",
        "bms_gauge_fcc": "bmsGaugeFCC",
        "bms_gauge_rm": "bmsGaugeRM",
        "bms_max_discharge_curr": "bmsMaxDischgCurr",
        "bms_mcu_version": "bmsMCUVersion",
        "bms_soc": "bmsSOC",
        "bms_soh": "bmsSOH",
        "e_charge1_today": "echarge1Today",
        "e_charge1_total": "echarge1Total",
        "e_discharge1_today": "edischargeToday",
        "e_discharge1_total": "edischargeTotal",
        "e_local_load_today": "elocalLoadToday",
        "e_local_load_total": "elocalLoadTotal",
        "e_self_today": "eselftoday",
        "e_self_total": "eselftotal",
        "e_system_today": "esystemtoday",
        "e_system_total": "esystemtotal",
        "e_to_grid_today": "etoGridToday",
        "e_to_user_today": "etoUserToday",
        "e_to_user_total": "etoUserTotal",
        "e_to_grid_total": "etogridTotal",
        "max_soc": "maxSOC",
        "min_soc": "minSOC",
        "p_self": "pself",
        "p_system": "psystem",
        "device_sn": "serialNum",  # align with other endpoints using "deviceSn" instead
        "ups_load_percent": "upsLoadpercent",
        "ups_pf": "upsPF",
    }
    return override.get(snake, to_camel(snake=snake))


class SpaEnergyDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spa_energy_to_camel,
    )

    ac_charge_energy_today: Union[EmptyStrToNone, float] = None  # AC daily charge energy, e.g. 0.0
    ac_charge_energy_total: Union[EmptyStrToNone, float] = None  # AC total charge energy, e.g. 8.3
    ac_charge_power: Union[EmptyStrToNone, float] = None  # AC charge power, e.g. 0.0
    acc_charge_pack_sn: Union[EmptyStrToNone, int] = None  # e.g. 0
    acc_charge_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    acc_discharge_pack_sn: Union[EmptyStrToNone, int] = None  # e.g. 0
    acc_discharge_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. None
    b_module_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_total_cell_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    batt_history_fault_code1: Union[EmptyStrToNone, int] = None  # e.g. 0
    batt_history_fault_code2: Union[EmptyStrToNone, int] = None  # e.g. 0
    batt_history_fault_code3: Union[EmptyStrToNone, int] = None  # e.g. 0
    batt_history_fault_code4: Union[EmptyStrToNone, int] = None  # e.g. 0
    batt_history_fault_code5: Union[EmptyStrToNone, int] = None  # e.g. 0
    batt_history_fault_code6: Union[EmptyStrToNone, int] = None  # e.g. 0
    batt_history_fault_code7: Union[EmptyStrToNone, int] = None  # e.g. 0
    batt_history_fault_code8: Union[EmptyStrToNone, int] = None  # e.g. 0
    battery_temperature: Union[EmptyStrToNone, float] = None  # Battery temperature, e.g. 0.0
    battery_type: Union[EmptyStrToNone, int] = None  # e.g. 1
    bms_battery_curr: Union[EmptyStrToNone, float] = None  # Battery current, e.g. 0.0
    bms_battery_temp: Union[EmptyStrToNone, float] = None  # Battery temperature, e.g. 28.0
    bms_battery_volt: Union[EmptyStrToNone, float] = None  # Battery voltage, e.g. 56.7400016784668
    bms_cell1_volt: Union[EmptyStrToNone, float] = None  # Battery cell 1 voltage, e.g. 3.5480000972747803
    bms_cell2_volt: Union[EmptyStrToNone, float] = None  # Battery cell 2 voltage, e.g. 3.5480000972747803
    bms_cell3_volt: Union[EmptyStrToNone, float] = None  # Battery cell 3 voltage, e.g. 3.549999952316284
    bms_cell4_volt: Union[EmptyStrToNone, float] = None  # Battery cell 4 voltage, e.g. 3.549999952316284
    bms_cell5_volt: Union[EmptyStrToNone, float] = None  # Battery cell 5 voltage, e.g. 3.549999952316284
    bms_cell6_volt: Union[EmptyStrToNone, float] = None  # Battery cell 6 voltage, e.g. 3.5510001182556152
    bms_cell7_volt: Union[EmptyStrToNone, float] = None  # Battery cell 7 voltage, e.g. 3.549999952316284
    bms_cell8_volt: Union[EmptyStrToNone, float] = None  # Battery cell 8 voltage, e.g. 3.549999952316284
    bms_cell9_volt: Union[EmptyStrToNone, float] = None  # Battery cell 9 voltage, e.g. 3.513000011444092
    bms_cell10_volt: Union[EmptyStrToNone, float] = None  # Battery cell 10 voltage, e.g. 3.549999952316284
    bms_cell11_volt: Union[EmptyStrToNone, float] = None  # Battery cell 11 voltage, e.g. 3.549999952316284
    bms_cell12_volt: Union[EmptyStrToNone, float] = None  # Battery cell 12 voltage, e.g. 3.549999952316284
    bms_cell13_volt: Union[EmptyStrToNone, float] = None  # Battery cell 13 voltage, e.g. 3.5490000247955322
    bms_cell14_volt: Union[EmptyStrToNone, float] = None  # Battery cell 14 voltage, e.g. 3.5490000247955322
    bms_cell15_volt: Union[EmptyStrToNone, float] = None  # Battery cell 15 voltage, e.g. 3.5490000247955322
    bms_cell16_volt: Union[EmptyStrToNone, float] = None  # Battery cell 16 voltage, e.g. 3.549999952316284
    bms_constant_volt: Union[EmptyStrToNone, float] = (
        None  # Battery constant voltage charging point, e.g. 56.79999923706055
    )
    bms_cycle_cnt: Union[EmptyStrToNone, int] = None  # Battery cycle count, e.g. 1331
    bms_delta_volt: Union[EmptyStrToNone, float] = None  # Battery cell voltage difference, e.g. 38.0
    bms_error: Union[EmptyStrToNone, int] = None  # Battery fault, e.g. 0
    bms_error2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_error3: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_error_old: Union[EmptyStrToNone, int] = None  # Battery historical fault, e.g. 0
    bms_fw: Union[EmptyStrToNone, int] = None  # BMS firmware version, e.g. 257
    bms_gauge_fcc: Union[EmptyStrToNone, float] = None  # Rated capacity, e.g. 100
    bms_gauge_rm: Union[EmptyStrToNone, float] = None  # System Capacity, e.g. 49.9900016784668
    bms_hardware_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_hardware_version2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_highest_soft_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_info: Union[EmptyStrToNone, float] = None  # BMS Information, e.g. 257
    bms_mcu_version: Union[EmptyStrToNone, int] = None  # BMS firmware version, e.g. 512
    bms_max_curr: Union[EmptyStrToNone, float] = None  # Maximum charge-discharge current, e.g. 100
    bms_max_discharge_curr: Union[EmptyStrToNone, float] = None  # Maximum discharge current, e.g. 0.0
    bms_pack_info: Union[EmptyStrToNone, float] = None  # Battery Pack Information, e.g. 257
    bms_request_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_soc: Union[EmptyStrToNone, int] = None  # Battery state of charge, e.g. 100
    bms_soh: Union[EmptyStrToNone, int] = None  # Battery state of health, e.g. 47
    bms_status: Union[EmptyStrToNone, int] = None  # Battery Status, e.g. 361
    bms_status_old: Union[EmptyStrToNone, int] = None  # Battery historical status, e.g. 361
    bms_using_cap: Union[EmptyStrToNone, float] = None  # Battery pack power type, e.g. 5000
    bms_warn_info: Union[EmptyStrToNone, int] = None  # Battery warning information, e.g. 0
    bms_warn_info_old: Union[EmptyStrToNone, int] = None  # Battery historical warning information, e.g. 0
    calendar: Union[EmptyStrToNone, datetime.datetime] = None  # Time, e.g. 1716435473718
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'XGD6CMM2VY'
    day: Union[EmptyStrToNone, str] = None  # e.g. ''
    day_map: Union[EmptyStrToNone, Any] = None  # , e.g. None
    eac_today: Union[EmptyStrToNone, float] = None  # Inverter daily output energy, e.g. 21.600000381469727
    eac_total: Union[EmptyStrToNone, float] = None  # Inverter total output energy, e.g. 1859.5
    e_charge1_today: Union[EmptyStrToNone, float] = None  # Battery daily charge energy, e.g. 0.2
    e_charge1_total: Union[EmptyStrToNone, float] = None  # Battery total charge energy, e.g. 6113.2
    e_discharge1_today: Union[EmptyStrToNone, float] = None  # Battery daily discharge energy, e.g. 0.4
    e_discharge1_total: Union[EmptyStrToNone, float] = None  # Battery total discharge energy, e.g. 5540.6
    e_local_load_today: Union[EmptyStrToNone, float] = None  # Local load daily energy consumption, e.g. 0
    e_local_load_total: Union[EmptyStrToNone, float] = None  # Local total load energy consumption, e.g. 26980.8
    epv_inverter_today: Union[EmptyStrToNone, float] = None  # PV inverter daily energy generation, e.g. 0.6
    epv_inverter_total: Union[EmptyStrToNone, float] = None  # PV inverter total energy generation, e.g. 0.6
    error_code: Union[EmptyStrToNone, int] = None  # error code, e.g. 0
    error_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    e_self_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_self_total: Union[EmptyStrToNone, float] = None  # e.g. 5.9
    e_system_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_system_total: Union[EmptyStrToNone, float] = None  # e.g. 5.9
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # Grid daily energy intake, e.g. 0.3
    e_to_user_today: Union[EmptyStrToNone, float] = None  # Grid daily energy output, e.g. 0
    e_to_user_total: Union[EmptyStrToNone, float] = None  # Grid total energy output, e.g. 11991.1
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # Grid total energy intake, e.g. 2293
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 50.0099983215332
    fault_bit_code: Union[EmptyStrToNone, int] = None  # Inverter fault bit code, e.g. 0
    fault_code: Union[EmptyStrToNone, int] = None  # Inverter fault code, e.g. 0
    first_batt_fault_sn: Union[EmptyStrToNone, int] = None  # e.g. 0
    fourth_batt_fault_sn: Union[EmptyStrToNone, int] = None  # e.g. 0
    iac1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    iac2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    iac3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    max_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    min_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    module_series_qty: Union[EmptyStrToNone, int] = None  # e.g. 0
    monitor: Union[EmptyStrToNone, int] = None  # e.g. 1
    number_of_batt_codes: Union[EmptyStrToNone, int] = None  # e.g. 0
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 2503.8
    pac1: Union[EmptyStrToNone, float] = None  # Inverter apparent output power, e.g. 0
    pac_r: Union[EmptyStrToNone, float] = None  # e.g. 0
    pac_s: Union[EmptyStrToNone, float] = None  # e.g. 0
    pac_t: Union[EmptyStrToNone, float] = None  # e.g. 0
    pac_to_grid_r: Union[EmptyStrToNone, float] = None  # Grid reverse power, e.g. 38.6
    pac_to_grid_total: Union[EmptyStrToNone, float] = None  # Grid total reverse power, e.g. 38.6
    pac_to_user_r: Union[EmptyStrToNone, float] = None  # Grid forward power, e.g. 0
    pac_to_user_total: Union[EmptyStrToNone, float] = None  # Grid total forward power, e.g. 0
    pcharge1: Union[EmptyStrToNone, float] = None  # Battery charge power, e.g. 0
    pdischarge1: Union[EmptyStrToNone, float] = None  # Battery discharge power, e.g. 16.5
    plocal_load_r: Union[EmptyStrToNone, float] = None  # Local load power consumption, e.g. 0
    plocal_load_r2: Union[EmptyStrToNone, float] = None  # e.g. 0
    plocal_load_s: Union[EmptyStrToNone, float] = None  # e.g. 0
    plocal_load_t: Union[EmptyStrToNone, float] = None  # e.g. 0
    plocal_load_total: Union[EmptyStrToNone, float] = None  # Local total load power consumption, e.g. 0
    pm_r: Union[EmptyStrToNone, float] = None  # e.g. 0
    pm_s: Union[EmptyStrToNone, float] = None  # e.g. 0
    pm_t: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv_inverter: Union[EmptyStrToNone, float] = None  # PV inverter power generation, e.g. 6.8
    priority_choose: Union[EmptyStrToNone, float] = None  # e.g. 2
    protect_pack_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    p_self: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    p_system: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    second_batt_fault_sn: Union[EmptyStrToNone, int] = None  # e.g. 0
    device_sn: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. 'MTN0H6800E'
    soc: Union[EmptyStrToNone, float] = None  # Battery state of charge, e.g. 100
    soc_text: Union[EmptyStrToNone, str] = None  # e.g. '100%'
    spa_bean: Union[EmptyStrToNone, Any] = None  # e.g. None,
    status: Union[EmptyStrToNone, int] = None  # e.g. 9
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Bypass'
    sys_en: Union[EmptyStrToNone, int] = None  # System enable bit, e.g. 17056
    sys_fault_word: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word1: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word2: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word3: Union[EmptyStrToNone, int] = None  # e.g. 33280
    sys_fault_word4: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word5: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word6: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word7: Union[EmptyStrToNone, int] = None  # e.g. 256
    temp1: Union[EmptyStrToNone, float] = None  # Temperature 1, e.g. 34
    temp2: Union[EmptyStrToNone, float] = None  # Temperature 2, e.g. 33.099998474121094
    temp3: Union[EmptyStrToNone, float] = None  # Temperature 3, e.g. 27.7
    third_batt_fault_sn: Union[EmptyStrToNone, int] = None  # e.g. 0
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-23 11:37:53'
    time_total: Union[EmptyStrToNone, float] = None  # Total operating time, e.g. 265549.0
    ups_fac: Union[EmptyStrToNone, float] = None  # UPS frequency, e.g. 0
    ups_iac1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ups_iac2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ups_iac3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ups_load_percent: Union[EmptyStrToNone, float] = None  # UPS load percentage, e.g. 0
    ups_pf: Union[EmptyStrToNone, float] = None  # UPS power factor, e.g. 1000
    ups_pac1: Union[EmptyStrToNone, float] = None  # UPS apparent output power, e.g. 0
    ups_pac2: Union[EmptyStrToNone, float] = None  # e.g. 0
    ups_pac3: Union[EmptyStrToNone, float] = None  # e.g. 0
    ups_vac1: Union[EmptyStrToNone, float] = None  # UPS voltage, e.g. 0
    ups_vac2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ups_vac3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sys_work_mode: Union[EmptyStrToNone, int] = None  # System working mode, e.g. 5
    uw_dsp_dc_dc_debug_data: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_dc_dc_debug_data1: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_dc_dc_debug_data2: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_dc_dc_debug_data3: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_dc_dc_debug_data4: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_inv_debug_data: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_inv_debug_data1: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_inv_debug_data2: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_inv_debug_data3: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_dsp_inv_debug_data4: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_max_cell_vol: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_max_tempr_cell: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_max_tempr_cell_no: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_max_volt_cell_no: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_min_cell_vol: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_min_tempr_cell: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_min_tempr_cell_no: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_min_volt_cell_no: Union[EmptyStrToNone, int] = None  # e.g. 0
    v_bat_dsp: Union[EmptyStrToNone, float] = None  # DSP collected battery voltage, e.g. 0
    v_bus1: Union[EmptyStrToNone, float] = None  # Bus 1 voltage, e.g. 0
    v_bus2: Union[EmptyStrToNone, float] = None  # Bus 2 voltage, e.g. 0
    vac1: Union[EmptyStrToNone, float] = None  # Grid voltage, e.g. 219.89999389648438
    vac2: Union[EmptyStrToNone, float] = None  # e.g. 0
    vac3: Union[EmptyStrToNone, float] = None  # e.g. 0
    vbat: Union[EmptyStrToNone, float] = None  # battery voltage, e.g. 56.70000076293945
    warn_code: Union[EmptyStrToNone, int] = None  # Warning code, e.g. 220
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the received data includes time, e.g. False


def _spa_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "devices": "spa",
    }
    return override.get(snake, to_camel(snake=snake))


class SpaEnergyOverviewDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spa_energy_overview_data_to_camel,
    )

    devices: List[SpaEnergyDataV4] = None


class SpaEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, SpaEnergyOverviewDataV4] = None


# ------------------------------------------------------------------------------------------------


def _min_energy_to_camel(snake: str) -> str:
    override = {
        "battery_sn": "batterySN",
        "datalogger_sn": "dataLogSn",
        "e_charge_today": "echargeToday",
        "e_charge_total": "echargeTotal",
        "e_discharge_today": "edischargeToday",
        "e_discharge_total": "edischargeTotal",
        "e_local_load_today": "elocalLoadToday",
        "e_local_load_total": "elocalLoadTotal",
        "e_self_today": "eselfToday",
        "e_self_total": "eselfTotal",
        "e_system_today": "esystemToday",
        "e_system_total": "esystemTotal",
        "e_to_grid_today": "etoGridToday",
        "e_to_grid_total": "etoGridTotal",
        "e_to_user_today": "etoUserToday",
        "e_to_user_total": "etoUserTotal",
        "p_self": "pself",
        "p_system": "psystem",
        "real_op_percent": "realOPPercent",
        "device_sn": "serialNum",  # align with other endpoints using "deviceSn" instead
        "win_off_grid_soc": "winOffGridSOC",
        "win_on_grid_soc": "winOnGridSOC",
    }
    return override.get(snake, to_camel(snake=snake))


class MinEnergyDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_min_energy_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. None
    b_merter_connect_flag: Union[EmptyStrToNone, bool] = None  # e.g. 0
    bat_sn: Union[EmptyStrToNone, str] = None  # e.g. None
    battery_no: Union[EmptyStrToNone, int] = None  # Battery pack number, e.g. 0
    battery_sn: Union[EmptyStrToNone, str] = None  # Battery serial number, e.g. ''
    bdc1_charge_power: Union[EmptyStrToNone, float] = None  # BDC1 charging power, e.g. 0.0
    bdc1_charge_total: Union[EmptyStrToNone, float] = None  # BDC1 total charging energy, e.g. 0.0
    bdc1_discharge_power: Union[EmptyStrToNone, float] = None  # BDC1 discharging power, e.g. 0.0
    bdc1_discharge_total: Union[EmptyStrToNone, float] = None  # BDC1 total discharging energy, e.g. 0.0
    bdc1_fault_type: Union[EmptyStrToNone, int] = None  # BDC1 fault code, e.g. 0
    bdc1_ibat: Union[EmptyStrToNone, float] = None  # BDC1 battery current, e.g. 0.0
    bdc1_ibb: Union[EmptyStrToNone, float] = None  # BDC1 BUCK-BOOST Current, e.g. 0.0
    bdc1_illc: Union[EmptyStrToNone, float] = None  # BDC1 LLC Current, e.g. 0.0
    bdc1_mode: Union[EmptyStrToNone, int] = None  # BDC1 mode, e.g. 0
    bdc1_soc: Union[EmptyStrToNone, float] = None  # BDC1 battery capacity, e.g. 0
    bdc1_status: Union[EmptyStrToNone, int] = None  # BDC1 status, e.g. 0
    bdc1_temp1: Union[EmptyStrToNone, float] = None  # BDC1 Temperature A, e.g. 0.0
    bdc1_temp2: Union[EmptyStrToNone, float] = None  # BDC1 Temperature B, e.g. 0.0
    bdc1_vbat: Union[EmptyStrToNone, float] = None  # BDC1 battery voltage, e.g. 0.0
    bdc1_vbus1: Union[EmptyStrToNone, float] = None  # BDC1 Bus1 voltage, e.g. 0.0
    bdc1_vbus2: Union[EmptyStrToNone, float] = None  # BDC1 Bus2 voltage, e.g. 0.0
    bdc1_warn_code: Union[EmptyStrToNone, int] = None  # BDC1 warning code, e.g. 0
    bdc2_charge_power: Union[EmptyStrToNone, float] = None  # BDC2 charging power, e.g. 0.0
    bdc2_charge_total: Union[EmptyStrToNone, float] = None  # BDC2 total charging energy, e.g. 0.0
    bdc2_discharge_power: Union[EmptyStrToNone, float] = None  # BDC2 discharging power, e.g. 0.0
    bdc2_discharge_total: Union[EmptyStrToNone, float] = None  # BDC2 total discharging energy, e.g. 0.0
    bdc2_fault_type: Union[EmptyStrToNone, int] = None  # BDC2 fault code, e.g. 0
    bdc2_ibat: Union[EmptyStrToNone, float] = None  # BDC2 battery current, e.g. 0.0
    bdc2_ibb: Union[EmptyStrToNone, float] = None  # BDC2 BUCK-BOOST Current, e.g. 0.0
    bdc2_illc: Union[EmptyStrToNone, float] = None  # BDC2 LLC Current, e.g. 0.0
    bdc2_mode: Union[EmptyStrToNone, int] = None  # BDC2 mode, e.g. 0
    bdc2_soc: Union[EmptyStrToNone, float] = None  # BDC2 battery capacity, e.g. 0
    bdc2_status: Union[EmptyStrToNone, int] = None  # BDC2 status, e.g. 0
    bdc2_temp1: Union[EmptyStrToNone, float] = None  # BDC2 Temperature A, e.g. 0.0
    bdc2_temp2: Union[EmptyStrToNone, float] = None  # BDC2 Temperature B, e.g. 0.0
    bdc2_vbat: Union[EmptyStrToNone, float] = None  # BDC2 battery voltage, e.g. 0.0
    bdc2_vbus1: Union[EmptyStrToNone, float] = None  # BDC2 Bus1 voltage, e.g. 0.0
    bdc2_vbus2: Union[EmptyStrToNone, float] = None  # BDC2 Bus2 voltage, e.g. 0.0
    bdc2_warn_code: Union[EmptyStrToNone, int] = None  # BDC2 warning code, e.g. 0
    bdc_bus_ref: Union[EmptyStrToNone, int] = None  # BUS soft start flag, e.g. 0.0
    bdc_derate_reason: Union[EmptyStrToNone, int] = None  # BDC derating reason, e.g. 0
    bdc_fault_sub_code: Union[EmptyStrToNone, int] = None  # BDC fault sub-code, e.g. 0
    bdc_status: Union[EmptyStrToNone, int] = None  # BDC connection status, e.g. 0
    bdc_vbus2_neg: Union[EmptyStrToNone, float] = None  # BDC BUS2Neg voltage, e.g. 0.0
    bdc_warn_sub_code: Union[EmptyStrToNone, int] = None  # BDC warning sub-code, e.g. 0
    bgrid_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_communication_type: Union[EmptyStrToNone, int] = None  # BMS communication type (0=RS485, 1=CAN) e.g. 0
    bms_cv_volt: Union[EmptyStrToNone, float] = None  # BMS lithium battery CV voltage, e.g. 0.0
    bms_error2: Union[EmptyStrToNone, int] = None  # Battery error 2, e.g. 0
    bms_error3: Union[EmptyStrToNone, int] = None  # Battery error 3, e.g. 0
    bms_error4: Union[EmptyStrToNone, int] = None  # Battery error 4, e.g. 0
    bms_fault_type: Union[EmptyStrToNone, int] = None  # BMS fault code, e.g. 0
    bms_fw_version: Union[EmptyStrToNone, str] = None  # BMS internal version, e.g. '0'
    bms_ibat: Union[EmptyStrToNone, float] = None  # BMS battery current, e.g. 0.0
    bms_icycle: Union[EmptyStrToNone, float] = None  # BMS battery cycle count, e.g. 0
    bms_info: Union[EmptyStrToNone, float] = None  # BMS information, e.g. 0.0
    bms_ios_status: Union[EmptyStrToNone, int] = None  # Battery ISO detection status, e.g. 0
    bms_max_curr: Union[EmptyStrToNone, float] = None  # BMS maximum current, e.g. 0.0
    bms_mcu_version: Union[EmptyStrToNone, str] = None  # BMS battery MCU version, e.g. '0'
    bms_pack_info: Union[EmptyStrToNone, float] = None  # BMS battery pack information, e.g. 0.0
    bms_soc: Union[EmptyStrToNone, float] = None  # BMS battery capacity, e.g. 0
    bms_soh: Union[EmptyStrToNone, float] = None  # BMS battery health index, e.g. 0
    bms_status: Union[EmptyStrToNone, int] = None  # BMS status, e.g. 0
    bms_temp1_bat: Union[EmptyStrToNone, float] = None  # BMS battery temperature, e.g. 0
    bms_using_cap: Union[EmptyStrToNone, float] = None  # BMS battery capacity, e.g. 0.0
    bms_vbat: Union[EmptyStrToNone, float] = None  # BMS battery voltage, e.g. 0
    bms_vdelta: Union[EmptyStrToNone, float] = None  # BMS Delta voltage, e.g. 0.0
    bms_warn2: Union[EmptyStrToNone, int] = None  # Battery warning 2, e.g. 0
    bms_warn_code: Union[EmptyStrToNone, float] = None  # BMS warning code, e.g. 0
    bsystem_work_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    calendar: Union[EmptyStrToNone, datetime.datetime] = None  # Time, e.g. 1716619122927
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'BLE094404C'
    day: Union[EmptyStrToNone, str] = None  # e.g. None
    dc_voltage: Union[EmptyStrToNone, float] = None  # DC Voltage, e.g. 0.0
    dci_r: Union[EmptyStrToNone, float] = None  # R phase DC current component, e.g. 12.0
    dci_s: Union[EmptyStrToNone, float] = None  # S phase DC current component, e.g. 0.0
    dci_t: Union[EmptyStrToNone, float] = None  # T phase DC current component, e.g. 0.0
    debug1: Union[EmptyStrToNone, str] = (
        None  # Debug data 1-8, separated by Chinese characters, e.g. '160, 0, 0, 0, 324, 0, 0, 0'
    )
    debug2: Union[EmptyStrToNone, str] = (
        None  # Debug data 9-16, separated by Chinese characters, e.g. '0,0,0,0,0,0,0,0'
    )
    derating_mode: Union[EmptyStrToNone, int] = None  # Derating mode, e.g. 0
    dry_contact_status: Union[EmptyStrToNone, int] = None  # Dry contact connection status, e.g. 0
    eac_charge_today: Union[EmptyStrToNone, float] = None  # AC daily charging energy, e.g. 0.0
    eac_charge_total: Union[EmptyStrToNone, float] = None  # AC total charging energy, e.g. 0.0
    eac_today: Union[EmptyStrToNone, float] = None  # Inverter daily output energy, e.g. 21.600000381469727
    eac_total: Union[EmptyStrToNone, float] = None  # Inverter total output energy, e.g. 1859.5
    e_charge_today: Union[EmptyStrToNone, float] = None  # System daily charging energy, e.g. 0.0
    e_charge_total: Union[EmptyStrToNone, float] = None  # System total charging energy, e.g. 0.0
    e_discharge_today: Union[EmptyStrToNone, float] = None  # System daily discharging energy, e.g. 0.0
    e_discharge_total: Union[EmptyStrToNone, float] = None  # System total discharging energy, e.g. 0.0
    eex1_today: Union[EmptyStrToNone, float] = None  # Daily PV inverter 1 output, 3254-3255, e.g. -0.1
    eex1_total: Union[EmptyStrToNone, float] = None  # Total PV inverter 1 output, 3258-3259, e.g. -0.1
    eex2_today: Union[EmptyStrToNone, float] = None  # Daily PV inverter 2 output, 3256-3257, e.g. -0.1
    eex2_total: Union[EmptyStrToNone, float] = None  # Total PV inverter 2 output, 3260-3261, e.g. -0.1
    e_local_load_today: Union[EmptyStrToNone, float] = None  # Daily user load energy consumption, e.g. 0.0
    e_local_load_total: Union[EmptyStrToNone, float] = None  # Total user load energy consumption, e.g. 0.0
    eps_fac: Union[EmptyStrToNone, float] = None  # Off-grid frequency, e.g. 0.0
    eps_iac1: Union[EmptyStrToNone, float] = None  # Off-grid R current, e.g. 0.0
    eps_iac2: Union[EmptyStrToNone, float] = None  # Off-grid S current, e.g. 0.0
    eps_iac3: Union[EmptyStrToNone, float] = None  # Off-grid T current, e.g. 0.0
    eps_pac: Union[EmptyStrToNone, float] = None  # Off-grid output power, e.g. 0.0
    eps_pac1: Union[EmptyStrToNone, float] = None  # Off-grid R power, e.g. 0.0
    eps_pac2: Union[EmptyStrToNone, float] = None  # Off-grid S power, e.g. 0.0
    eps_pac3: Union[EmptyStrToNone, float] = None  # Off-grid T power, e.g. 0.0
    eps_pf: Union[EmptyStrToNone, float] = None  # Off-grid power factor value, e.g. -1.0
    eps_vac1: Union[EmptyStrToNone, float] = None  # Off-grid R voltage, e.g. 0.0
    eps_vac2: Union[EmptyStrToNone, float] = None  # Off-grid S voltage, e.g. 0.0
    eps_vac3: Union[EmptyStrToNone, float] = None  # Off-grid T voltage, e.g. 0.0
    epv1_today: Union[EmptyStrToNone, float] = None  # PV1 daily energy generation, e.g. 13.199999809265137
    epv1_total: Union[EmptyStrToNone, float] = None  # PV1 total energy generation, e.g. 926.6
    epv2_today: Union[EmptyStrToNone, float] = None  # PV2 daily energy generation, e.g. 8.199999809265137
    epv2_total: Union[EmptyStrToNone, float] = None  # PV2 total energy generation, e.g. 906.4
    epv3_today: Union[EmptyStrToNone, float] = None  # PV3 daily energy generation, e.g. 0.0
    epv3_total: Union[EmptyStrToNone, float] = None  # PV3 total energy generation, e.g. 0.0
    epv4_today: Union[EmptyStrToNone, float] = None  # PV4 daily energy generation, e.g. 0.0
    epv4_total: Union[EmptyStrToNone, float] = None  # PV4 total energy generation, e.g. 0.0
    epv_total: Union[EmptyStrToNone, float] = None  # Total PV energy generation, e.g. 1833.0
    error_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    e_self_today: Union[EmptyStrToNone, float] = (
        None  # Daily self-consumption energy generation kWh, 3139-3140, e.g. 0.0
    )
    e_self_total: Union[EmptyStrToNone, float] = (
        None  # Total self-consumption energy generation kWh, 3141-3142, e.g. 0.0
    )
    e_system_today: Union[EmptyStrToNone, float] = None  # Daily system energy generation kWh, 3123-3124, e.g. 0.0
    e_system_total: Union[EmptyStrToNone, float] = None  # Total system energy generation kWh, 3137-3138, e.g. 0.0
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # Daily grid input energy, e.g. 0.0
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # Total grid input energy, e.g. 0.0
    e_to_user_today: Union[EmptyStrToNone, float] = None  # Daily grid output energy, e.g. 0.0
    e_to_user_total: Union[EmptyStrToNone, float] = None  # Total grid output energy, e.g. 0.0
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 50.0099983215332
    fault_type: Union[EmptyStrToNone, int] = None  # Fault code, e.g. 0
    fault_type1: Union[EmptyStrToNone, int] = None  # e.g. 0
    gfci: Union[EmptyStrToNone, float] = None  # Grid leakage current, e.g. 78
    iac1: Union[EmptyStrToNone, float] = None  # Grid current 1, e.g. 10.699999809265137
    iac2: Union[EmptyStrToNone, float] = None  # Grid current 2, e.g. 0
    iac3: Union[EmptyStrToNone, float] = None  # Grid current 3, e.g. 0
    iacr: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    inv_delay_time: Union[EmptyStrToNone, float] = None  # Grid-tied inverter countdown, e.g. 0.0
    ipv1: Union[EmptyStrToNone, float] = None  # PV1 input current, e.g. 5.800000190734863
    ipv2: Union[EmptyStrToNone, float] = None  # PV2 input current, e.g. 6.099999904632568
    ipv3: Union[EmptyStrToNone, float] = None  # PV3 input current, e.g. 0.0
    ipv4: Union[EmptyStrToNone, float] = None  # PV4 input current, e.g. 0.0
    is_again: Union[EmptyStrToNone, bool] = None  # Is it a retransmission, e.g. False
    iso: Union[EmptyStrToNone, float] = None  # PV insulation resistance, e.g. 3135
    load_percent: Union[EmptyStrToNone, float] = None  # Off-grid load percentage, e.g. 0.0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    mtnc_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    mtnc_rqst: Union[EmptyStrToNone, float] = None  # e.g. 0
    n_bus_voltage: Union[EmptyStrToNone, float] = None  # N Bus Voltage, e.g. 0.0
    new_warn_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    new_warn_sub_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    op_fullwatt: Union[EmptyStrToNone, float] = None  # Output power limit, e.g. 0.0
    operating_mode: Union[EmptyStrToNone, int] = None  # Inverter operating mode, e.g. 0
    p_bus_voltage: Union[EmptyStrToNone, float] = None  # P Bus Voltage, e.g. 367.0
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 2503.8
    pac1: Union[EmptyStrToNone, float] = None  # Inverter apparent output power 1, e.g. 2530.699951171875
    pac2: Union[EmptyStrToNone, float] = None  # Inverter apparent output power 2, e.g. 0.0
    pac3: Union[EmptyStrToNone, float] = None  # Inverter apparent output power 3, e.g. 0.0
    pac_to_grid_total: Union[EmptyStrToNone, float] = None  # Total reverse power to the grid, e.g. 0.0
    pac_to_local_load: Union[EmptyStrToNone, float] = None  # Total power to the grid, e.g. 0.0
    pac_to_user_total: Union[EmptyStrToNone, float] = None  # Grid downstream total power, e.g. 0.0
    pacr: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pex1: Union[EmptyStrToNone, float] = None  # PV inverter 1 power, 3250-3251, e.g. -0.1
    pex2: Union[EmptyStrToNone, float] = None  # PV inverter 2 power, 3252-3253, e.g. -0.1
    pf: Union[EmptyStrToNone, float] = None  # Power factor value, e.g. 0.08100000023841858
    ppv: Union[EmptyStrToNone, float] = None  # Total PV input power, e.g. 2558.7
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power, e.g. 1500.7
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power, e.g. 1058
    ppv3: Union[EmptyStrToNone, float] = None  # PV3 input power, e.g. 0
    ppv4: Union[EmptyStrToNone, float] = None  # PV4 total power, e.g. 0
    p_self: Union[EmptyStrToNone, float] = None  # Self-consumption power W, 3121-3122, e.g. 0.0
    p_system: Union[EmptyStrToNone, float] = None  # System power generation W, 3019-3020, e.g. 0.0
    real_op_percent: Union[EmptyStrToNone, float] = None  # R, e.g. 50.0
    device_sn: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. 'AFE494403F'
    soc1: Union[EmptyStrToNone, float] = None  # e.g. 0
    soc2: Union[EmptyStrToNone, float] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = None  # Min Status (0: waiting, 1: normal, 2: fault), e.g. 1
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Normal'
    sys_fault_word: Union[EmptyStrToNone, int] = None  # Register 1001, e.g. 0
    sys_fault_word1: Union[EmptyStrToNone, int] = None  # Register 1002, e.g. 0
    sys_fault_word2: Union[EmptyStrToNone, int] = None  # Register 1003, e.g. 0
    sys_fault_word3: Union[EmptyStrToNone, int] = None  # Register 1004, e.g. 0
    sys_fault_word4: Union[EmptyStrToNone, int] = None  # Register 1005, e.g. 0
    sys_fault_word5: Union[EmptyStrToNone, int] = None  # Register 1006, e.g. 0
    sys_fault_word6: Union[EmptyStrToNone, int] = None  # Register 1007, e.g. 0
    sys_fault_word7: Union[EmptyStrToNone, int] = None  # Register 1008, e.g. 0
    t_mtnc_strt: Union[EmptyStrToNone, str] = None  # e.g. None
    t_win_end: Union[EmptyStrToNone, str] = None  # e.g. None
    t_win_start: Union[EmptyStrToNone, str] = None  # e.g. None
    temp1: Union[EmptyStrToNone, float] = None  # Temperature 1, e.g. 47.79999923706055
    temp2: Union[EmptyStrToNone, float] = None  # Temperature 2, e.g. 0.0
    temp3: Union[EmptyStrToNone, float] = None  # Temperature 3, e.g. 0.0
    temp4: Union[EmptyStrToNone, float] = None  # Temperature 4, e.g. 0.0
    temp5: Union[EmptyStrToNone, float] = None  # Temperature 5, e.g. 51.70000076293945
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-09 14:52:39'
    time_total: Union[EmptyStrToNone, float] = None  # Total run time, e.g. 12798429.9
    tlx_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    total_working_time: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sys_work_mode: Union[EmptyStrToNone, int] = None  # System work mode 1000, e.g. 0
    vac1: Union[EmptyStrToNone, float] = None  # Grid voltage 1, e.g. 239.5
    vac2: Union[EmptyStrToNone, float] = None  # Grid voltage 2, e.g. 0.0
    vac3: Union[EmptyStrToNone, float] = None  # Grid voltage 3, e.g. 0.0
    vac_rs: Union[EmptyStrToNone, float] = None  # RS line voltage, e.g. 239.5
    vac_st: Union[EmptyStrToNone, float] = None  # ST line voltage, e.g. 0.0
    vac_tr: Union[EmptyStrToNone, float] = None  # TR line voltage, e.g. 0.0
    vacr: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    vacrs: Union[EmptyStrToNone, float] = None  # RS line voltage, e.g. 0.0
    vpv1: Union[EmptyStrToNone, float] = None  # PV1 input voltage, e.g. 258.6000061035156
    vpv2: Union[EmptyStrToNone, float] = None  # PV2 input voltage, e.g. 9.899999618530273
    vpv3: Union[EmptyStrToNone, float] = None  # PV3 input voltage, e.g. 0.0
    vpv4: Union[EmptyStrToNone, float] = None  # PV4 input voltage, e.g. 0.0
    warn_code: Union[EmptyStrToNone, int] = None  # Warning code, e.g. 220
    warn_code1: Union[EmptyStrToNone, int] = None  # e.g. 2
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    win_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    win_off_grid_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    win_on_grid_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    win_request: Union[EmptyStrToNone, int] = None  # e.g. 0
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the incoming data includes time, e.g. False


def _min_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "devices": "min",
    }
    return override.get(snake, to_camel(snake=snake))


class MinEnergyOverviewDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_min_energy_overview_data_to_camel,
    )

    devices: List[MinEnergyDataV4] = None


class MinEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, MinEnergyOverviewDataV4] = None


# ------------------------------------------------------------------------------------------------


def _wit_energy_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "dataLogSn",
        "e_charge1_today": "echarge1Today",
        "e_charge1_total": "echarge1Total",
        "e_charge2_today": "echarge2Today",
        "e_charge2_total": "echarge2Total",
        "e_charge3_today": "echarge3Today",
        "e_charge3_total": "echarge3Total",
        "e_discharge1_today": "edischarge1Today",
        "e_discharge1_total": "edischarge1Total",
        "e_discharge2_today": "edischarge2Today",
        "e_discharge2_total": "edischarge2Total",
        "e_discharge3_today": "edischarge3Today",
        "e_discharge3_total": "edischarge3Total",
        "e_local_load_today": "elocalLoadToday",
        "e_local_load_total": "elocalLoadTotal",
        "e_self_today": "eselftoday",
        "e_self_total": "eselftotal",
        "e_system_today": "esystemtoday",
        "e_system_total": "esystemtotal",
        "e_to_grid_today": "etoGridToday",
        "e_to_user_today": "etoUserToday",
        "e_to_user_total": "etoUserTotal",
        "e_to_grid_total": "etoGridTotal",
        "off_grid_status": "offgridStatus",
        "p_self": "pself",
        "p_system": "psystem",
        "real_op_percent": "realOPPercent",
        "device_sn": "serialNum",  # align with other endpoints using "deviceSn" instead
        "str_unbalance": "strUnblance",
        "str_unbalance2": "strUnblance2",
        "str_warning_value1": "strWaringvalue1",
        "str_warning_value2": "strWaringvalue2",
        "ud_op_rst_watt_first": "udOpRSTWattFirst",
        "ud_op_rst_watt_sec": "udOpRSTWattSec",
        "ud_fault_bit_high": "udfaultBitHigh",
        "ud_fault_bit_low": "udfaultBitLow",
        "usb_aging_test_ok_flag": "usbagingTestOkFlag",
        "uw_op_line_rs_first": "uwOpLineRSFirst",
        "uw_op_line_rs_sec": "uwOpLineRSSec",
        "uw_op_line_st_first": "uwOpLineSTFirst",
        "uw_op_line_st_sec": "uwOpLineSTSec",
        "uw_op_line_tr_first": "uwOpLineTRFirst",
        "uw_op_line_tr_sec": "uwOpLineTRSec",
        "uw_rdci_curr_first": "uwRDCICurrFirst",
        "uw_rdci_curr_sec": "uwRDCICurrSec",
        "uw_sdci_curr_first": "uwSDCICurrFirst",
        "uw_sdci_curr_sec": "uwSDCICurrSec",
        "uw_tdci_curr_first": "uwTDCICurrFirst",
        "uw_tdci_curr_sec": "uwTDCICurrSec",
    }
    return override.get(snake, to_camel(snake=snake))


class WitEnergyDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_wit_energy_to_camel,
    )

    ac_charge_energy_today: Union[EmptyStrToNone, float] = None  # AC daily charge energy, e.g. 0.0
    ac_charge_energy_total: Union[EmptyStrToNone, float] = None  # AC total charge energy, e.g. 0.0,
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    b_afci_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_alarm_sub_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_bat_bus_target: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    b_bms_sta: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_cluster_cnt: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_fault_sub_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_flag_chg_dis: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_packs_cnt: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_sig_mode_cell_cnt: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_sig_pack_mode_cnt: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_soc: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    b_soh: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    b_status_first: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_status_sec: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_sys_avg_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_sys_max_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_sys_max_soc_pack_num: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    b_sys_min_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_sys_min_soc_pack_num: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bat_curr_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bat_curr_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bat_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bat_power2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bat_power3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bat_type: Union[EmptyStrToNone, float] = None  # e.g. 0
    bat_volt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bat_volt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    battery_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_bat_vol2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_bat_vol3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_battery_volt: Union[EmptyStrToNone, float] = None  # e.g. 48.0
    bms_max_temp2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_max_temp3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_min_temp2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_min_temp3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_sell_max_vol2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_sell_max_vol3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_sell_min_vol2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_sell_min_vol3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bus_cap_using: Union[EmptyStrToNone, float] = None  # e.g. 0
    calendar: Union[EmptyStrToNone, datetime.datetime] = None  # Time, e.g. 1716965658551
    cbat: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    cbat2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    cbat3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
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
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'XGD6E452V7'
    day_map: Union[EmptyStrToNone, Any] = None  # , e.g. None
    delay_time: Union[EmptyStrToNone, float] = None  # e.g. 0
    derating_mode: Union[EmptyStrToNone, int] = None  # Derating mode, e.g. 0
    eac_today: Union[EmptyStrToNone, float] = None  # Inverter daily output energy, e.g. 21.600000381469727
    eac_total: Union[EmptyStrToNone, float] = None  # Inverter total output energy, e.g. 1859.5
    e_charge1_today: Union[EmptyStrToNone, float] = None  # Battery daily charge energy, e.g. 0.0
    e_charge1_total: Union[EmptyStrToNone, float] = None  # Total battery charge energy, e.g. 0.0
    e_charge2_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_charge2_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_charge3_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_charge3_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_discharge1_today: Union[EmptyStrToNone, float] = None  # Battery daily discharge energy, e.g. 0.4
    e_discharge1_total: Union[EmptyStrToNone, float] = None  # Total battery discharge energy, e.g. 5540.6
    e_discharge2_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_discharge2_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_discharge3_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_discharge3_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    eex_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    eex_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_local_load_today: Union[EmptyStrToNone, float] = None  # Daily energy consumption of user load, e.g. 0
    e_local_load_total: Union[EmptyStrToNone, float] = None  # Total energy consumption of user load, e.g. 26980.8
    epv1_today: Union[EmptyStrToNone, float] = None  # PV1 daily generation, e.g. 13.199999809265137
    epv1_total: Union[EmptyStrToNone, float] = None  # PV1 total generation, e.g. 926.6
    epv2_today: Union[EmptyStrToNone, float] = None  # PV2 daily generation, e.g. 8.199999809265137
    epv2_total: Union[EmptyStrToNone, float] = None  # PV2 total generation, e.g. 906.4
    epv3_today: Union[EmptyStrToNone, float] = None  # PV3 daily generation, e.g. 0
    epv3_total: Union[EmptyStrToNone, float] = None  # PV3 total generation, e.g. 0
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
    epv_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    epv_total: Union[EmptyStrToNone, float] = None  # Total PV generation, e.g. 115372.9
    error_code: Union[EmptyStrToNone, int] = None  # error code, e.g. 0
    error_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    e_self_today: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    e_self_total: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    e_system_today: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    e_system_total: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # Grid daily input energy, e.g. 0.3
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # Grid total input energy, e.g. 2293
    e_to_user_today: Union[EmptyStrToNone, float] = None  # Grid daily output energy, e.g. 0
    e_to_user_total: Union[EmptyStrToNone, float] = None  # Grid total output energy, e.g. 11991.1
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 49.98
    fan_fault_bit: Union[EmptyStrToNone, float] = None  # e.g. 0
    fault_bit_code: Union[EmptyStrToNone, int] = None  # Inverter fault bit code, e.g. 0
    fault_code: Union[EmptyStrToNone, int] = None  # Inverter fault code, e.g. 0
    fault_value: Union[EmptyStrToNone, int] = None  # Fault value, e.g. 3
    flash_erase_aging_ok_flag: Union[EmptyStrToNone, bool] = None  # e.g. 0
    gen_port1_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_port2_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_port3_volt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gfci: Union[EmptyStrToNone, float] = None  # Grid leakage current, e.g. 166
    hcpc_low_volt_num: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    hcpc_max_volt_num: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    hcpc_single_low_temp_num: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    hcpc_single_low_volt_num: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    hcpc_single_max_temp_num: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    hcpc_single_max_volt_num: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    hcpc_temp_num: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    hcpc_temp_num1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    iac1: Union[EmptyStrToNone, float] = None  # Grid current 1, e.g. 5.0
    iac2: Union[EmptyStrToNone, float] = None  # Grid current 2, e.g. 5.5
    iac3: Union[EmptyStrToNone, float] = None  # Grid current 3, e.g. 0.0
    iac_load: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    iacs_load: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    iact_load: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    inv_r_volt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    inv_r_volt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    inv_s_volt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    inv_s_volt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    inv_t_volt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    inv_t_volt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ipv1: Union[EmptyStrToNone, float] = None  # PV1 input current, e.g. 0.7
    ipv2: Union[EmptyStrToNone, float] = None  # PV2 input current, e.g. 2.4
    ipv3: Union[EmptyStrToNone, float] = None  # PV3 input current, e.g. 0.0
    ipv4: Union[EmptyStrToNone, float] = None  # PV4 current (A), e.g. 0.0
    ipv5: Union[EmptyStrToNone, float] = None  # PV5 current (A), e.g. 0.0
    ipv6: Union[EmptyStrToNone, float] = None  # PV6 current (A), e.g. 0.0
    ipv7: Union[EmptyStrToNone, float] = None  # PV7 current (A), e.g. 0.0
    ipv8: Union[EmptyStrToNone, float] = None  # PV8 current (A), e.g. 0.0
    ipv9: Union[EmptyStrToNone, float] = None  # PV9 current (A), e.g. 0.0
    ipv10: Union[EmptyStrToNone, float] = None  # PV10 current (A), e.g. 0.0
    off_grid_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    on_off_grid_state: Union[EmptyStrToNone, int] = None  # e.g. 0
    on_off_grid_state_first: Union[EmptyStrToNone, int] = None  # e.g. 0
    on_off_grid_state_sec: Union[EmptyStrToNone, int] = None  # e.g. 0
    op_fullwatt: Union[EmptyStrToNone, float] = None  # Output power limit, e.g. 0.0
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 2038.9
    pac1: Union[EmptyStrToNone, float] = None  # Inverter apparent power 1, e.g. 1119.5
    pac2: Union[EmptyStrToNone, float] = None  # Inverter apparent power 2, e.g. 0.0
    pac3: Union[EmptyStrToNone, float] = None  # Inverter apparent power 3, e.g. 0.0
    pac_to_grid_total: Union[EmptyStrToNone, float] = None  # Total power to grid (reverse), e.g. 38.6
    pac_to_user_total: Union[EmptyStrToNone, float] = None  # Total power to grid (forward), e.g. 0
    pex: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    pf: Union[EmptyStrToNone, float] = None  # Power factor value, e.g. 1.0
    pid_bus: Union[EmptyStrToNone, float] = None  # PID BUS voltage, e.g. 0.0
    pid_fault_code: Union[EmptyStrToNone, int] = None  # pid fault code, e.g. 0
    pid_status: Union[EmptyStrToNone, int] = None  # pid status, e.g. 0
    plocal_load_total: Union[EmptyStrToNone, float] = None  # Total local load consumption power, e.g. 0
    pm_derate: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv: Union[EmptyStrToNone, float] = None  # Total PV input power, e.g. 2069.9
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power (W), e.g. 410.4
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power (W), e.g. 1551.6
    ppv3: Union[EmptyStrToNone, float] = None  # PV3 input power (W), e.g. 0.0
    ppv4: Union[EmptyStrToNone, float] = None  # PV4 input power (W), e.g. 0.0
    ppv5: Union[EmptyStrToNone, float] = None  # PV5 input power (W), e.g. 0.0
    ppv6: Union[EmptyStrToNone, float] = None  # PV6 input power (W), e.g. 0.0
    ppv7: Union[EmptyStrToNone, float] = None  # PV7 input power (W), e.g. 0.0
    ppv8: Union[EmptyStrToNone, float] = None  # PV8 input power (W), e.g. 0.0
    ppv9: Union[EmptyStrToNone, float] = None  # PV9 input power (W)r, e.g. 0.0
    ppv10: Union[EmptyStrToNone, float] = None  # PV10 input power (W), e.g. 0.0
    priority_choose: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_self: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    p_system: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    pv_iso: Union[EmptyStrToNone, float] = None  # Insulation resistance, e.g. 3004
    r_dci: Union[EmptyStrToNone, float] = None  # R-phase DC component, e.g. 0.2
    react_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    react_power_max: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    react_power_total: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    reactive_power_real_value_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    reactive_power_real_value_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    real_op_percent: Union[EmptyStrToNone, float] = None  # Real output percentage, e.g. 50
    real_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_curr1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    reverse_curr2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    reverse_curr3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    run_time: Union[EmptyStrToNone, float] = None  # e.g. 0
    s_dci: Union[EmptyStrToNone, float] = None  # S-phase DC component, e.g. 0.7
    sac: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    device_sn: Union[EmptyStrToNone, str] = None  # Max device SN, e.g. 'QWL0DC3002'
    soc: Union[EmptyStrToNone, float] = None  # Battery state of charge, e.g. 100
    soc2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    soc3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    soh: Union[EmptyStrToNone, float] = None  # e.g. 0
    soh2: Union[EmptyStrToNone, float] = None  # e.g. 0
    soh3: Union[EmptyStrToNone, float] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = None  # Min Status (0:waiting, 1:normal, 2:fault), e.g. 1
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Operating'
    str_break: Union[EmptyStrToNone, int] = None  # String not connected, e.g. 0
    str_break2: Union[EmptyStrToNone, int] = None  # e.g. 0
    str_unbalance: Union[EmptyStrToNone, int] = None  # String current imbalance, e.g. 0
    str_unbalance2: Union[EmptyStrToNone, int] = None  # e.g. 0
    str_unmatch: Union[EmptyStrToNone, int] = None  # String mismatch, e.g. 0
    str_unmatch2: Union[EmptyStrToNone, int] = None  # e.g. 0
    str_warning_value1: Union[EmptyStrToNone, int] = None  # e.g. 0
    str_warning_value2: Union[EmptyStrToNone, int] = None  # e.g. 0
    string_prompt: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_on_pack_cnt: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    t_dci: Union[EmptyStrToNone, float] = None  # T-phase DC component, e.g. 6552.7
    temp1: Union[EmptyStrToNone, float] = None  # Temperature 1, e.g. 34
    temp2: Union[EmptyStrToNone, float] = None  # Temperature 2, e.g. 33.099998474121094
    temp3: Union[EmptyStrToNone, float] = None  # Temperature 3, e.g. 33.099998474121094
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-29 14:54:18'
    time_total: Union[EmptyStrToNone, float] = None  # Total runtime, e.g. 44968542.0
    u_ac_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    u_bat_chg_p: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    u_bat_dsg_p: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_acc_chg_soe: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_acc_dis_soe: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_calib_apparent_power_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_calib_apparent_power_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_op_rst_watt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_op_rst_watt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_op_r_watt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_op_r_watt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_op_s_watt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_op_s_watt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_op_t_watt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_op_t_watt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    ud_fault_bit_high: Union[EmptyStrToNone, bool] = None  # e.g. 0
    ud_fault_bit_low: Union[EmptyStrToNone, bool] = None  # e.g. 0
    usb_aging_test_ok_flag: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_alarm_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_ambient_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_ambient_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_bat_enable1: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_bat_enable2: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_bat_enable3: Union[EmptyStrToNone, bool] = None  # e.g. 0
    uw_cell_max_v_chg: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_cell_min_v_dis: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_cell_tavg_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_cell_tmax_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_cell_tmin_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_cell_uavg_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_cell_umax_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_cell_umin_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_charge_max_vol: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_fault_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_freq_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_freq_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_full_charge_capacity: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_gen_port_dev_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_inv_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_inv_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_inv_warn_value: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_load_per_first: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_load_per_sec: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_main_code_first: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_main_code_sec: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_main_warn_first: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_main_warn_sec: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_mod_max_bla_temp_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_mod_max_vol_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_mod_min_bla_temp_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_mode_avg_vol_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_mode_min_vol_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_mode_rated_cap: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_mode_rated_vol: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_n_bus_volt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_n_bus_volt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_line_rs_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_line_rs_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_line_st_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_line_st_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_line_tr_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_line_tr_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_r_curr_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_r_curr_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_r_volt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_r_volt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_s_curr_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_s_curr_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_s_volt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_s_volt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_t_curr_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_t_curr_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_t_volt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_op_phase_t_volt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_output_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_output_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_p_bus_volt_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_p_bus_volt_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_rdci_curr_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_rdci_curr_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_rated_battery_capacity: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_rated_battery_power_energy: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sdci_curr_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sdci_curr_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sub_code_first: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_sub_code_sec: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_sub_warn_first: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_sub_warn_sec: Union[EmptyStrToNone, int] = None  # e.g. 0
    uw_sys_load_vol_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sys_max_allow_ichg: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sys_max_allow_idis: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sys_max_vtotalchg: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sys_min_vtotaldis: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sys_tota_vol_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_sys_total_i_value: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_tdci_curr_first: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_tdci_curr_sec: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    uw_upack_rated: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    v_bat_dsp: Union[EmptyStrToNone, float] = None  # DSP collected battery voltage, e.g. 0
    v_bus_n: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    v_bus_p: Union[EmptyStrToNone, float] = None  # e.g. 0.0
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
    vac: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    vac1: Union[EmptyStrToNone, float] = None  # Grid voltage 1, e.g. 222.8
    vac2: Union[EmptyStrToNone, float] = None  # Grid voltage 2, e.g. 223.1
    vac3: Union[EmptyStrToNone, float] = None  # Grid voltage 3, e.g. 0.0
    vac_rs: Union[EmptyStrToNone, float] = None  # RS line voltage (V), e.g. 414.30002
    vac_rs1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    vac_st: Union[EmptyStrToNone, float] = None  # ST line voltage (V), e.g. 407.2
    vac_st1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    vac_tr: Union[EmptyStrToNone, float] = None  # TR line voltage (V), e.g. 407.2
    vac_tr1: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    vacs: Union[EmptyStrToNone, float] = None  # S-phase voltage (V), e.g. 234.1
    vact: Union[EmptyStrToNone, float] = None  # T-phase voltage (V), e.g. 237.0
    vbat: Union[EmptyStrToNone, float] = None  # battery voltage, e.g. 0.0
    vbat2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    vbat3: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    vpp_work_status: Union[EmptyStrToNone, int] = None  # e.g. 0
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
    warn_code: Union[EmptyStrToNone, int] = None  # Warning code, e.g. 220
    warn_code1: Union[EmptyStrToNone, int] = None  # e.g. 0
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    warning_value1: Union[EmptyStrToNone, int] = None  # Warning value 1, e.g. 0
    warning_value2: Union[EmptyStrToNone, int] = None  # Warning value 2, e.g. 0
    warning_value3: Union[EmptyStrToNone, int] = None  # Warning value 3, e.g. 0
    wit_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the incoming data includes time, e.g. False


def _wit_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "devices": "wit",
    }
    return override.get(snake, to_camel(snake=snake))


class WitEnergyOverviewDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_wit_energy_overview_data_to_camel,
    )

    devices: List[WitEnergyDataV4] = None


class WitEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, WitEnergyOverviewDataV4] = None


# ------------------------------------------------------------------------------------------------


def _sphs_energy_to_camel(snake: str) -> str:
    override = {
        "bms_soc": "bmsSOC",
        "bms_soh": "bmsSOH",
        "datalogger_sn": "dataLogSn",
        "e_charge1_today": "echarge1Today",
        "e_charge1_total": "echarge1Total",
        "e_discharge1_today": "edischarge1Today",
        "e_discharge1_total": "edischarge1Total",
        "e_local_load_hour": "elocalLoadHour",
        "e_local_load_month": "elocalLoadMonth",
        "e_local_load_today": "elocalLoadToday",
        "e_local_load_total": "elocalLoadTotal",
        "e_local_load_year": "elocalLoadYear",
        "e_self_hour": "eselfHour",
        "e_self_month": "eselfMonth",
        "e_self_year": "eselfYear",
        "e_self_today": "eselftoday",
        "e_self_total": "eselftotal",
        "e_system_today": "esystemtoday",
        "e_system_total": "esystemtotal",
        "e_system_hour": "esystemHour",
        "e_system_month": "esystemMonth",
        "e_system_year": "esystemYear",
        "e_to_grid_today": "etoGridToday",
        "e_to_grid_total": "etoGridTotal",
        "e_to_user_today": "etoUserToday",
        "e_to_user_total": "etoUserTotal",
        "p_self": "pself",
        "p_system": "psystem",
        "device_sn": "serialNum",  # align with other endpoints using "deviceSn" instead
    }
    return override.get(snake, to_camel(snake=snake))


class SphsEnergyDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sphs_energy_to_camel,
    )

    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    bat_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    bms_battery_curr: Union[EmptyStrToNone, float] = None  # Battery current, e.g. 0.0
    bms_battery_temp: Union[EmptyStrToNone, float] = None  # Battery temperature, e.g. 35.3
    bms_battery_volt: Union[EmptyStrToNone, float] = None  # Battery voltage, e.g. 5.34
    bms_constant_volt: Union[EmptyStrToNone, float] = None  # Battery constant voltage point, e.g. 5.68
    bms_soc: Union[EmptyStrToNone, int] = None  # BDC2 battery capacity, e.g. 100
    bms_soh: Union[EmptyStrToNone, int] = None  # BMS battery health index, e.g. 0
    bms_using_cap: Union[EmptyStrToNone, float] = None  # BMS battery capacity, e.g. 2000
    calendar: Union[EmptyStrToNone, datetime.datetime] = None  # Time, e.g. 1716965431997
    chip_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'VC41010123438079'
    day_map: Union[EmptyStrToNone, Any] = None  # , e.g. None
    dc_temp: Union[EmptyStrToNone, float] = None  # e.g. 56.7
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    e_to_grid_hour: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_to_grid_month: Union[EmptyStrToNone, float] = None  # e.g. 5.7
    e_to_grid_year: Union[EmptyStrToNone, float] = None  # e.g. 6.4
    e_to_user_hour: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    e_to_user_month: Union[EmptyStrToNone, float] = None  # e.g. 186.5
    e_to_user_year: Union[EmptyStrToNone, float] = None  # e.g. 535.8
    e_charge1_today: Union[EmptyStrToNone, float] = None  # Battery daily charge energy, e.g. 9.5
    e_charge1_total: Union[EmptyStrToNone, float] = None  # Total battery charge energy, e.g. 177.9
    e_discharge1_today: Union[EmptyStrToNone, float] = None  # Battery daily discharge energy, e.g. 4.2
    e_discharge1_total: Union[EmptyStrToNone, float] = None  # Total battery discharge energy, e.g. 172.7
    e_local_load_hour: Union[EmptyStrToNone, float] = None  # e.g. 0.7
    e_local_load_month: Union[EmptyStrToNone, float] = None  # e.g. 509.7
    e_local_load_today: Union[EmptyStrToNone, float] = None  # User load daily consumption, e.g. 1018.2
    e_local_load_total: Union[EmptyStrToNone, float] = None  # User load total consumption, e.g. 1071.6
    e_local_load_year: Union[EmptyStrToNone, float] = None  # e.g. 1071.6
    eac_today: Union[EmptyStrToNone, float] = None  # Daily power generation
    eac_total: Union[EmptyStrToNone, float] = None  # Total power generation
    eps_iac1: Union[EmptyStrToNone, float] = None  # Off-grid R current, e.g. 3.8
    eps_iac2: Union[EmptyStrToNone, float] = None  # Off-grid S current, e.g. 0.0
    eps_vac2: Union[EmptyStrToNone, float] = None  # Off-grid S voltage, e.g.  0.0
    epv1_today: Union[EmptyStrToNone, float] = None  # PV1 daily generated energy, e.g. 13.199999809265137
    epv1_total: Union[EmptyStrToNone, float] = None  # PV1 total generated energy, e.g. 0.0
    epv2_today: Union[EmptyStrToNone, float] = None  # PV2 daily generated energy, e.g. 0.0
    epv2_total: Union[EmptyStrToNone, float] = None  # PV2 total generated energy, e.g. 0.0
    epv3_today: Union[EmptyStrToNone, float] = None  # PV3 daily generated energy, e.g. 14.0
    epv3_total: Union[EmptyStrToNone, float] = None  # PV3 total generated energy, e.g. 0.0
    epv_hour: Union[EmptyStrToNone, float] = None  # e.g. 0.7
    epv_month: Union[EmptyStrToNone, float] = None  # e.g. 256.6
    epv_today: Union[EmptyStrToNone, float] = None  # e.g. 14.0
    epv_total: Union[EmptyStrToNone, float] = None  # Total PV generated energy, e.g. 494.0
    epv_year: Union[EmptyStrToNone, float] = None  # e.g. 494.0
    error_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    e_self_hour: Union[EmptyStrToNone, float] = None  # e.g. 0.7
    e_self_month: Union[EmptyStrToNone, float] = None  # e.g. 323.2
    e_self_year: Union[EmptyStrToNone, float] = None  # e.g. 660.3
    e_self_today: Union[EmptyStrToNone, float] = None  # e.g. 18.200000762939453
    e_self_total: Union[EmptyStrToNone, float] = None  # e.g. 660.2999877929688
    e_system_hour: Union[EmptyStrToNone, float] = None  # e.g. 0.7
    e_system_month: Union[EmptyStrToNone, float] = None  # e.g. 328.9
    e_system_year: Union[EmptyStrToNone, float] = None  # e.g. 666.7
    e_system_today: Union[EmptyStrToNone, float] = None  # e.g. 18.200000762939453
    e_system_total: Union[EmptyStrToNone, float] = None  # e.g. 666.7000122070312
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # Grid daily input energy, e.g. 0.0
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # Grid total input energy, e.g. 6.4
    e_to_user_today: Union[EmptyStrToNone, float] = None  # Grid daily output energy, e.g. 1.0
    e_to_user_total: Union[EmptyStrToNone, float] = None  # Grid total output energy, e.g. 535.8
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 49.98
    fault_bit_code: Union[EmptyStrToNone, int] = None  # Inverter fault bit code, e.g. 0
    fault_code: Union[EmptyStrToNone, int] = None  # Inverter fault code, e.g. 0
    gen_curr: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_energy: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_energy_today: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_freq: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_power: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    gen_vol: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    grid_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    hmi_version: Union[EmptyStrToNone, Any] = None  # e.g. None
    iac1: Union[EmptyStrToNone, float] = None  # Grid current 1, e.g. 1.3
    iac2: Union[EmptyStrToNone, float] = None  # Grid current 2, e.g. 0.0
    ibat: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    inv_Temp: Union[EmptyStrToNone, float] = None  # e.g. 47.4
    ipv1: Union[EmptyStrToNone, float] = None  # PV1 input current, e.g. 0.0
    ipv2: Union[EmptyStrToNone, float] = None  # PV2 input current, e.g. 0.0
    ipv3: Union[EmptyStrToNone, float] = None  # PV3 input current, e.g. 2.7
    load_power1: Union[EmptyStrToNone, float] = None  # e.g. 760.0
    load_power2: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    m1_version: Union[EmptyStrToNone, Any] = None  # e.g. None
    m2_version: Union[EmptyStrToNone, Any] = None  # e.g. None
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 888.0
    pac1: Union[EmptyStrToNone, float] = None  # Inverter apparent power 1, e.g. 0.0
    pac2: Union[EmptyStrToNone, float] = None  # Inverter apparent power 2, e.g. 0.0
    pac_to_grid_r: Union[EmptyStrToNone, float] = None  # Grid reverse power, e.g. 0.0
    pac_to_grid_s: Union[EmptyStrToNone, float] = None  # Grid reverse power, e.g. 0.0
    pac_to_grid_total: Union[EmptyStrToNone, float] = None  # Total power flowing back from the grid, e.g. 0.0
    pac_to_user_r: Union[EmptyStrToNone, float] = None  # Grid forward power, e.g. 0.0
    pac_to_user_total: Union[EmptyStrToNone, float] = None  # Total power flowing to the grid, e.g. 0.0
    pcharge1: Union[EmptyStrToNone, float] = None  # Battery charge power, e.g. 0.0
    pdischarge1: Union[EmptyStrToNone, float] = None  # Battery discharge power, e.g. 0.0
    pex: Union[EmptyStrToNone, float] = None  # e.g. 888.0
    pf: Union[EmptyStrToNone, float] = None  # pf value, e.g. -1.0
    plocal_load_r: Union[EmptyStrToNone, float] = None  # Local load consumption power, e.g. 0.0
    plocal_load_s: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    plocal_load_total: Union[EmptyStrToNone, float] = None  # Total local load consumption power, e.g. 888.0
    ppv: Union[EmptyStrToNone, float] = None  # Total PV input power, e.g. 948.0
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power, e.g. 0.0
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power, e.g. 0.0
    ppv3: Union[EmptyStrToNone, float] = None  # PV3 input power, e.g. 948.0
    ppv_text: Union[EmptyStrToNone, str] = None  # e.g. '948.0 W'
    priority_choose: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_self: Union[EmptyStrToNone, float] = None  # e.g. 942.0
    p_system: Union[EmptyStrToNone, float] = None  # e.g. 942.0
    r_load_vol: Union[EmptyStrToNone, float] = None  # e.g. 229.8
    r_local_energy: Union[EmptyStrToNone, float] = None  # e.g. 904.3
    s_load_vol: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    s_local_energy: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    device_sn: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. 'EFP0N1J023'
    soc: Union[EmptyStrToNone, float] = None  # Battery state of charge, e.g. 100
    soc_text: Union[EmptyStrToNone, str] = None  # e.g. '100%'
    sp_status: Union[EmptyStrToNone, int] = None  # e.g. 1
    sph_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    status: Union[EmptyStrToNone, int] = None  # Min Status 0: waiting, 1: normal, 2: fault, e.g. 6
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Fault'
    sys_fault_word: Union[EmptyStrToNone, int] = None  # e.g. 12337
    sys_fault_word1: Union[EmptyStrToNone, int] = None  # e.g. 12851
    sys_fault_word2: Union[EmptyStrToNone, int] = None  # e.g. 13365
    sys_fault_word3: Union[EmptyStrToNone, int] = None  # e.g. 13879
    sys_fault_word4: Union[EmptyStrToNone, int] = None  # e.g. 14393
    sys_fault_word5: Union[EmptyStrToNone, int] = None  # e.g. 16706
    sys_fault_word6: Union[EmptyStrToNone, int] = None  # e.g. 17220
    sys_fault_word7: Union[EmptyStrToNone, int] = None  # e.g. 17734
    sys_status: Union[EmptyStrToNone, int] = None  # e.g. 3
    system_fault: Union[EmptyStrToNone, int] = None  # e.g. 0
    system_warn: Union[EmptyStrToNone, int] = None  # e.g. 0
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-05-29 14:50:31'
    time_total: Union[EmptyStrToNone, float] = None  # Total operating time, e.g. 0.0.5
    ups_fac: Union[EmptyStrToNone, float] = None  # Emergency power frequency, e.g. 50.0
    ups_pac1: Union[EmptyStrToNone, float] = None  # Emergency apparent output power, e.g. 888.0
    ups_pac2: Union[EmptyStrToNone, float] = None  # Off-grid side power, e.g. 0.0
    ups_vac1: Union[EmptyStrToNone, float] = None  # Emergency voltage, e.g. 229.5
    uw_sys_work_mode: Union[EmptyStrToNone, int] = None  # System working mode, e.g. 6
    vac1: Union[EmptyStrToNone, float] = None  # Grid voltage 1, e.g. 230.3
    vac2: Union[EmptyStrToNone, float] = None  # Grid voltage 2, e.g. 0.0
    vbat: Union[EmptyStrToNone, float] = None  # battery voltage, e.g. 53.4
    vbat1: Union[EmptyStrToNone, float] = None  # e.g. 53.3
    vpv1: Union[EmptyStrToNone, float] = None  # PV1 input voltage, e.g. 0.0
    vpv2: Union[EmptyStrToNone, float] = None  # PV2 input voltage, e.g. 0.0
    vpv3: Union[EmptyStrToNone, float] = None  # PV3 input voltage, e.g. 349.5
    warn_code: Union[EmptyStrToNone, int] = None  # Warning code, e.g. 0
    warn_code1: Union[EmptyStrToNone, int] = None  # Warning code, e.g. 0
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the incoming data includes time, e.g. False


def _sphs_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "devices": "sph-s",
    }
    return override.get(snake, to_camel(snake=snake))


class SphsEnergyOverviewDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sphs_energy_overview_data_to_camel,
    )

    devices: List[SphsEnergyDataV4] = None


class SphsEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, SphsEnergyOverviewDataV4] = None


# ------------------------------------------------------------------------------------------------


def _noah_energy_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "dataLogSn",
    }
    return override.get(snake, to_camel(snake=snake))


class NoahEnergyDataV4(ApiModel):
    """
    Note: NOAH documentation is VERY incomplete (json shows SPH-S instead).
          see https://www.showdoc.com.cn/2540838290984246/11315141402697236
    Therefore, attributes listed here are possible not complete.
    A real NOAH device would be required to find the correct attributes
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_noah_energy_to_camel,
    )

    # no sample response in API docs - just parameter descriptions
    battery_package_quantity: Union[EmptyStrToNone, int] = None  # Number of parallel battery packs
    battery1_protect_status: Union[EmptyStrToNone, int] = (
        None  # Battery pack 1 protection status, BIT0: Low voltage protection, BIT1: High voltage protection, BIT2: Low charging temperature protection, BIT3: High charging temperature protection, BIT4: Low discharging temperature protection, BIT5: High discharging temperature protection, BIT6: Charging overcurrent protection, BIT7: Discharging overcurrent protection, BIT8: Battery error, BIT9: NTC disconnection, BIT10: Voltage sampling line disconnection, BIT11~BIT15: Reserved
    )
    battery1_serial_num: Union[EmptyStrToNone, str] = None  # Battery pack 1—SN
    battery1_soc: Union[EmptyStrToNone, int] = None  # Battery pack 1_SOC
    battery1_temp: Union[EmptyStrToNone, float] = None  # Battery pack 1 temperature
    battery1_warn_status: Union[EmptyStrToNone, int] = (
        None  # Battery pack 1 warning status, BIT0: Low voltage warning, BIT1: High voltage warning, BIT2: Low charging temperature warning, BIT3: High charging temperature warning, BIT4: Low discharging temperature warning, BIT5: High discharging temperature warning, BIT6: Charging overcurrent warning, BIT7: Discharging overcurrent warning, BIT8~BIT15: Reserved
    )
    battery2_protect_status: Union[EmptyStrToNone, int] = (
        None  # Battery pack 2 protection status, BIT0: Low voltage protection, BIT1: High voltage protection, BIT2: Low charging temperature protection, BIT3: High charging temperature protection, BIT4: Low discharging temperature protection, BIT5: High discharging temperature protection, BIT6: Charging overcurrent protection, BIT7: Discharging overcurrent protection, BIT8: Battery error, BIT9: NTC disconnection, BIT10: Voltage sampling line disconnection, BIT11~BIT15: Reserved
    )
    battery2_serial_num: Union[EmptyStrToNone, str] = None  # Battery pack 2—SN
    battery2_soc: Union[EmptyStrToNone, int] = None  # Battery pack 2_SOC
    battery2_temp: Union[EmptyStrToNone, float] = None  # Battery pack 2 temperature
    battery2_warn_status: Union[EmptyStrToNone, int] = (
        None  # Battery pack 2 warning status, BIT0: Low voltage warning, BIT1: High voltage warning, BIT2: Low charging temperature warning, BIT3: High charging temperature warning, BIT4: Low discharging temperature warning, BIT5: High discharging temperature warning, BIT6: Charging overcurrent warning, BIT7: Discharging overcurrent warning, BIT8~BIT15: Reserved
    )
    battery3_protect_status: Union[EmptyStrToNone, int] = (
        None  # Battery pack 3 protection status, BIT0: Low voltage protection, BIT1: High voltage protection, BIT2: Low charging temperature protection, BIT3: High charging temperature protection, BIT4: Low discharging temperature protection, BIT5: High discharging temperature protection, BIT6: Charging overcurrent protection, BIT7: Discharging overcurrent protection, BIT8: Battery error, BIT9: NTC disconnection, BIT10: Voltage sampling line disconnection, BIT11~BIT15: Reserved
    )
    battery3_serial_num: Union[EmptyStrToNone, str] = None  # Battery pack 3—SN
    battery3_soc: Union[EmptyStrToNone, int] = None  # Battery pack 3_SOC
    battery3_temp: Union[EmptyStrToNone, float] = None  # Battery pack 3 temperature
    battery3_warn_status: Union[EmptyStrToNone, int] = (
        None  # Battery pack 3 warning status, BIT0: Low voltage warning, BIT1: High voltage warning, BIT2: Low charging temperature warning, BIT3: High charging temperature warning, BIT4: Low discharging temperature warning, BIT5: High discharging temperature warning, BIT6: Charging overcurrent warning, BIT7: Discharging overcurrent warning, BIT8~BIT15: Reserved
    )
    battery4_protect_status: Union[EmptyStrToNone, int] = (
        None  # Battery pack 4 protection status, BIT0: Low voltage protection, BIT1: High voltage protection, BIT2: Low charging temperature protection, BIT3: High charging temperature protection, BIT4: Low discharging temperature protection, BIT5: High discharging temperature protection, BIT6: Charging overcurrent protection, BIT7: Discharging overcurrent protection, BIT8: Battery error, BIT9: NTC disconnection, BIT10: Voltage sampling line disconnection, BIT11~BIT15: Reserved
    )
    battery4_serial_num: Union[EmptyStrToNone, str] = None  # Battery pack 4—SN
    battery4_soc: Union[EmptyStrToNone, int] = None  # Battery pack 4_SOC
    battery4_temp: Union[EmptyStrToNone, float] = None  # Battery pack 4 temperature
    battery4_warn_status: Union[EmptyStrToNone, int] = (
        None  # Battery pack 4 warning status, BIT0: Low voltage warning, BIT1: High voltage warning, BIT2: Low charging temperature warning, BIT3: High charging temperature warning, BIT4: Low discharging temperature warning, BIT5: High discharging temperature warning, BIT6: Charging overcurrent warning, BIT7: Discharging overcurrent warning, BIT8~BIT15: Reserved
    )
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Data logger serial number
    device_sn: Union[EmptyStrToNone, str] = None  # Device number
    eac_month: Union[EmptyStrToNone, float] = None  # Monthly power generation
    eac_today: Union[EmptyStrToNone, float] = None  # Daily power generation
    eac_total: Union[EmptyStrToNone, float] = None  # Total power generation
    eac_year: Union[EmptyStrToNone, float] = None  # Annual power generation
    fault_status: Union[EmptyStrToNone, int] = (
        None  # Fault status, BIT0: Battery pack 1 fault, BIT1: Battery pack 2 fault, BIT2: Battery pack 3 fault, BIT3: Battery pack 4 fault
    )
    heating_status: Union[EmptyStrToNone, int] = (
        None  # Heating status, BIT0: Battery pack 1 is heating, BIT1: Battery pack 2 is heating, BIT2: Battery pack 3 is heating, BIT3: Battery pack 4 is heating
    )
    is_Again: Union[EmptyStrToNone, bool] = None  # Whether it is retransmitted data
    mppt_protect_status: Union[EmptyStrToNone, int] = (
        None  # BIT0: PV1 overvoltage protection, BIT1: PV1 overcurrent protection, BIT2: PV1 overtemperature protection, BIT3: Reserved, BIT4: PV2 overvoltage protection, BIT5: PV2 overcurrent protection
    )
    pac: Union[EmptyStrToNone, float] = None  # BUCK output power
    pd_warn_status: Union[EmptyStrToNone, int] = (
        None  # BIT0: Communication with BMS failed, BIT1: Communication with MPPT failed
    )
    ppv: Union[EmptyStrToNone, float] = None  # Photovoltaic power (W)
    status: Union[EmptyStrToNone, int] = None  # 1: Normal, 4: Fault, 5: Heating
    time: Union[EmptyStrToNone, datetime.datetime] = None  # Time
    total_battery_pack_charging_power: Union[EmptyStrToNone, int] = None  # Total battery charging/discharging power
    total_battery_pack_charging_status: Union[EmptyStrToNone, int] = (
        None  # BIT0: Charging, BIT1: Discharging, if neither, display standby
    )
    total_battery_pack_soc: Union[EmptyStrToNone, int] = None  # Total battery pack SOC (State of Charge) percentage
    work_mode: Union[EmptyStrToNone, int] = None  # Current time period working mode


def _noah_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "devices": "noah",
    }
    return override.get(snake, to_camel(snake=snake))


class NoahEnergyOverviewDataV4(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_noah_energy_overview_data_to_camel,
    )

    devices: List[NoahEnergyDataV4] = None


class NoahEnergyV4(NewApiResponse):
    data: Union[EmptyStrToNone, NoahEnergyOverviewDataV4] = None


# #####################################################################################################################
# Device energy #######################################################################################################


class InverterEnergyHistoryDataV4(ApiModel):
    datas: List[InverterEnergyDataV4] = []
    have_next: Union[EmptyStrToNone, bool] = None  # e.g. False
    start: Union[EmptyStrToNone, int] = None  # e.g. False


class InverterEnergyHistoryV4(NewApiResponse):
    data: Union[EmptyStrToNone, InverterEnergyHistoryDataV4] = None


class InverterEnergyHistoryMultipleV4(NewApiResponse):
    data: Union[EmptyStrToNone, Dict[str, List[InverterEnergyDataV4]]] = None


# ------------------------------------------------------------------------------------------------


class StorageEnergyHistoryDataV4(ApiModel):
    datas: List[StorageEnergyDataV4] = []
    have_next: Union[EmptyStrToNone, bool] = None  # e.g. False
    start: Union[EmptyStrToNone, int] = None  # e.g. False


class StorageEnergyHistoryV4(NewApiResponse):
    data: Union[EmptyStrToNone, StorageEnergyHistoryDataV4] = None


class StorageEnergyHistoryMultipleV4(NewApiResponse):
    data: Union[EmptyStrToNone, Dict[str, List[StorageEnergyDataV4]]] = None


# ------------------------------------------------------------------------------------------------


class SphEnergyHistoryDataV4(ApiModel):
    datas: List[SphEnergyDataV4] = []
    have_next: Union[EmptyStrToNone, bool] = None  # e.g. False
    start: Union[EmptyStrToNone, int] = None  # e.g. False


class SphEnergyHistoryV4(NewApiResponse):
    data: Union[EmptyStrToNone, SphEnergyHistoryDataV4] = None


class SphEnergyHistoryMultipleV4(NewApiResponse):
    data: Union[EmptyStrToNone, Dict[str, List[SphEnergyDataV4]]] = None


# ------------------------------------------------------------------------------------------------


class MaxEnergyHistoryDataV4(ApiModel):
    datas: List[MaxEnergyDataV4] = []
    have_next: Union[EmptyStrToNone, bool] = None  # e.g. False
    start: Union[EmptyStrToNone, int] = None  # e.g. False


class MaxEnergyHistoryV4(NewApiResponse):
    data: Union[EmptyStrToNone, MaxEnergyHistoryDataV4] = None


class MaxEnergyHistoryMultipleV4(NewApiResponse):
    data: Union[EmptyStrToNone, Dict[str, List[MaxEnergyDataV4]]] = None


# ------------------------------------------------------------------------------------------------


class SpaEnergyHistoryDataV4(ApiModel):
    datas: List[SpaEnergyDataV4] = []
    have_next: Union[EmptyStrToNone, bool] = None  # e.g. False
    start: Union[EmptyStrToNone, int] = None  # e.g. False


class SpaEnergyHistoryV4(NewApiResponse):
    data: Union[EmptyStrToNone, SpaEnergyHistoryDataV4] = None


class SpaEnergyHistoryMultipleV4(NewApiResponse):
    data: Union[EmptyStrToNone, Dict[str, List[SpaEnergyDataV4]]] = None


# ------------------------------------------------------------------------------------------------


class MinEnergyHistoryDataV4(ApiModel):
    datas: List[MinEnergyDataV4] = []
    have_next: Union[EmptyStrToNone, bool] = None  # e.g. False
    start: Union[EmptyStrToNone, int] = None  # e.g. False


class MinEnergyHistoryV4(NewApiResponse):
    data: Union[EmptyStrToNone, MinEnergyHistoryDataV4] = None


class MinEnergyHistoryMultipleV4(NewApiResponse):
    data: Union[EmptyStrToNone, Dict[str, List[MinEnergyDataV4]]] = None


# ------------------------------------------------------------------------------------------------


class WitEnergyHistoryDataV4(ApiModel):
    datas: List[WitEnergyDataV4] = []
    have_next: Union[EmptyStrToNone, bool] = None  # e.g. False
    start: Union[EmptyStrToNone, int] = None  # e.g. False


class WitEnergyHistoryV4(NewApiResponse):
    data: Union[EmptyStrToNone, WitEnergyHistoryDataV4] = None


class WitEnergyHistoryMultipleV4(NewApiResponse):
    data: Union[EmptyStrToNone, Dict[str, List[WitEnergyDataV4]]] = None


# ------------------------------------------------------------------------------------------------


class SphsEnergyHistoryDataV4(ApiModel):
    datas: List[SphsEnergyDataV4] = []
    have_next: Union[EmptyStrToNone, bool] = None  # e.g. False
    start: Union[EmptyStrToNone, int] = None  # e.g. False


class SphsEnergyHistoryV4(NewApiResponse):
    data: Union[EmptyStrToNone, SphsEnergyHistoryDataV4] = None


class SphsEnergyHistoryMultipleV4(NewApiResponse):
    data: Union[EmptyStrToNone, Dict[str, List[SphsEnergyDataV4]]] = None


# ------------------------------------------------------------------------------------------------


class NoahEnergyHistoryDataV4(ApiModel):
    datas: List[NoahEnergyDataV4] = []
    have_next: Union[EmptyStrToNone, bool] = None  # e.g. False
    start: Union[EmptyStrToNone, int] = None  # e.g. False


class NoahEnergyHistoryV4(NewApiResponse):
    data: Union[EmptyStrToNone, NoahEnergyHistoryDataV4] = None


class NoahEnergyHistoryMultipleV4(NewApiResponse):
    data: Union[EmptyStrToNone, Dict[str, List[NoahEnergyDataV4]]] = None


# #####################################################################################################################
# Setting write #######################################################################################################


class SettingWriteV4(NewApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# #####################################################################################################################
# Setting read VPP ####################################################################################################


class VppTimePeriodV4(ApiModel):
    percentage: Union[EmptyStrToNone, int] = None
    start_time: Union[EmptyStrToNone, int] = None  # time in minutes
    end_time: Union[EmptyStrToNone, int] = None  # time in minutes


class SettingReadVppV4(NewApiResponse):
    data: Union[EmptyStrToNone, int, float, List[VppTimePeriodV4]] = None
