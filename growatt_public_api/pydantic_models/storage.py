import datetime
from typing import Union, Any, List

from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from .api_model import (
    ApiResponse,
    EmptyStrToNone,
    GrowattTime,
    ApiModel,
    GrowattTimeCalendar,
)


# #####################################################################################################################
# Storage setting read #####################################################################################


class StorageSettingRead(ApiResponse):
    data: Union[EmptyStrToNone, str] = None  # current setting / register value


# #####################################################################################################################
# Storaged setting write ####################################################################################


class StorageSettingWrite(ApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# #####################################################################################################################
# Storage details #####################################################################################################


def _storage_detail_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "tree_id": "treeID",
        "user_id": "userID",
        "buzzer_en": "buzzerEN",
        "rate_va": "rateVA",
    }
    return override.get(snake, to_camel(snake=snake))


class StorageDetailData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_storage_detail_data_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    ac_in_model: Union[EmptyStrToNone, float] = None  # e.g. 0
    address: Union[EmptyStrToNone, int] = None  # e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. "ZT00100001"
    b_light_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_low_to_uti_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    battery_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bulk_charge_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    buzzer_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    charge_config: Union[EmptyStrToNone, int] = None  # e.g. 0
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    communication_version: Union[EmptyStrToNone, str] = None  # e.g. ''
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. "CRAZT00001"
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 1
    float_charge_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    fw_version: Union[EmptyStrToNone, str] = None  # Energy storage device firmware version, e.g. "G.2.0")
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_yellow.gif',
    inner_version: Union[EmptyStrToNone, str] = None  # e.g. 'fbaa1816',
    last_update_time: Union[EmptyStrToNone, GrowattTime] = None  # Last update time, e.g. {"time": 1547000577000, ...}
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. "2019-01-09 10:22:57"
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    location: Union[EmptyStrToNone, str] = None  # Address, e.g. ""
    lost: Union[EmptyStrToNone, bool] = (
        None  # whether the device is online or not (0: online, 1: disconnected), e.g. false
    )
    manual_start_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    max_charge_curr: Union[EmptyStrToNone, float] = None  # e.g. 0
    model: Union[EmptyStrToNone, int] = None  # e.g. 61748
    model_text: Union[EmptyStrToNone, str] = None  # e.g. "A0B0D0T0PFU1M3S4"
    output_config: Union[EmptyStrToNone, float] = None  # e.g. 0
    output_freq_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    output_volt_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    over_load_restart: Union[EmptyStrToNone, float] = None  # e.g. 0
    over_temp_restart: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_charge: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_discharge: Union[EmptyStrToNone, float] = None  # e.g. 0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_IUB38210F9_96'
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. ""
    port_name: Union[EmptyStrToNone, str] = None  # e.g. ""
    pow_saving_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    pv_model: Union[EmptyStrToNone, int] = None  # e.g. 0
    rate_va: Union[EmptyStrToNone, float] = None  # e.g. 0
    rate_watt: Union[EmptyStrToNone, float] = None  # e.g. 0
    record: Union[EmptyStrToNone, str] = None  # e.g. null
    sci_loss_chk_en: Union[EmptyStrToNone, int] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'JZB674901B'
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: disconnect, 1: online, 2: charge, 3: discharge, 4: error, 5: burn, 6: solar charge, 7: mains charge, 8: combined charging (solar and mains), 9: combined charging and bypass (mains) output, 10: PV charging and bypass (mains) output, 11: mains charging and bypass (mains) output, 12 : Bypass (mains) output, 13: Solar charge and discharge at the same time, 14: Mains charge and discharge at the same time), e.g. 1
    )
    status_led1: Union[EmptyStrToNone, bool] = None  # e.g. False
    status_led2: Union[EmptyStrToNone, bool] = None  # e.g. True
    status_led3: Union[EmptyStrToNone, bool] = None  # e.g. True
    status_led4: Union[EmptyStrToNone, bool] = None  # e.g. False
    status_led5: Union[EmptyStrToNone, bool] = None  # e.g. False
    status_led6: Union[EmptyStrToNone, bool] = None  # e.g. True
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'storage.status.operating'
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. "127.0.0.1"
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_JZB674901B'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. '2',
    updating: Union[EmptyStrToNone, bool] = None  # e.g. false
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ""
    uti_charge_end: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_charge_start: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_out_end: Union[EmptyStrToNone, float] = None  # e.g. 0
    uti_out_start: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_bat_type2: Union[EmptyStrToNone, int] = None  # e.g. 0


class StorageDetails(ApiResponse):
    data: Union[EmptyStrToNone, StorageDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the energy storage machine, e.g. "ZT00100001"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Storage energy overview #############################################################################################


def _storage_energy_overview_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "datalogger_sn": "dataLogSn",
        "charge_current": "chgCurr",
        "e_today": "etoday",
        "e_total": "etotal",
        "freq_output": "freqOutPut",
        "gauge_battery_status": "gaugeBattteryStatus",
        "gauge_ic_current": "gaugeICCurrent",
        "gauge_rm1": "gaugeRM1",
        "gauge_rm2": "gaugeRM2",
        "gauge2_rm1": "gauge2RM1",
        "gauge2_rm2": "gauge2RM2",
        "i_charge_pv1": "iChargePV1",
        "i_charge_pv2": "iChargePV2",
        "inner_cw_code": "innerCWCode",
        "output_current": "outPutCurrent",
        "output_power": "outPutPower",
        "output_volt": "outPutVolt",
        "p_ac_input": "pAcInPut",
        "rate_va": "rateVA",
        "discharge_month": "disChargeMonth",
        "discharge_current": "dischgCurr",
        "e_bat_discharge_today": "eBatDisChargeToday",
        "e_bat_discharge_total": "eBatDisChargeTotal",
        "eac_discharge_today": "eacDisChargeToday",
        "eac_discharge_total": "eacDisChargeTotal",
        "eop_discharge_today": "eopDischrToday",
        "eop_discharge_total": "eopDischrTotal",
    }
    return override.get(snake, to_camel(snake=snake))


class StorageEnergyOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_storage_energy_overview_data_to_camel,
    )
    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    b_light_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    bat_temp: Union[EmptyStrToNone, float] = None  # e.g. 43
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
    bms_delta_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_error: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_error2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_soh: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_status2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_temperature2: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_warn_info: Union[EmptyStrToNone, int] = None  # e.g. 0
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    capacity: Union[EmptyStrToNone, float] = None  # Battery capacity (percent), e.g. 52
    capacity_text: Union[EmptyStrToNone, str] = None  # e.g. '52 %'
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
    charge_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    charge_to_standby_reason: Union[EmptyStrToNone, int] = None  # e.g. 5
    charge_to_standby_reason_text: Union[EmptyStrToNone, str] = (
        None  # e.g. "Reason of state change from charge to operating: Battery voltage high for charge"
    )
    charge_way: Union[EmptyStrToNone, int] = None  # e.g. 0
    charge_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    constant_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    constant_volt2: Union[EmptyStrToNone, float] = None  # e.g. 0
    cycle_count: Union[EmptyStrToNone, int] = None  # e.g. 0
    cycle_count2: Union[EmptyStrToNone, int] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. ''
    day: Union[EmptyStrToNone, int] = None  # e.g. ''
    day_map: Union[EmptyStrToNone, Any] = None  # e.g. None
    delta_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    delta_volt2: Union[EmptyStrToNone, float] = None  # e.g. 0
    device_type: Union[EmptyStrToNone, int] = None  # Energy storage type (0: SP2000, 1: SP3000), e.g. 0
    discharge_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    discharge_to_standby_reason: Union[EmptyStrToNone, int] = None  # e.g. 5
    discharge_to_standby_reason_text: Union[EmptyStrToNone, str] = (
        None  # e.g. 'Reason of state change from discharge to operating: Battery voltage low for discharge'
    )
    discharge_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_bat_discharge_today: Union[EmptyStrToNone, float] = None  # Battery discharge energy on the day, e.g. 0
    e_bat_discharge_total: Union[EmptyStrToNone, float] = None  # Total battery discharge energy, e.g. 0
    e_charge_today: Union[EmptyStrToNone, float] = None  # Charge energy of the day (kWh), e.g. 0
    e_charge_today2: Union[EmptyStrToNone, float] = None  # SP3000 today’s charging power (kWh), e.g. 0
    e_charge_today_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 kWh'
    e_charge_total: Union[EmptyStrToNone, float] = None  # Total charging energy (kWh), e.g. 2.3
    e_charge_total2: Union[EmptyStrToNone, float] = None  # SP3000 accumulative charging power (kWh), e.g. 2.6
    e_charge_total_text: Union[EmptyStrToNone, str] = None  # e.g. '2.3 kWh'
    e_discharge_today: Union[EmptyStrToNone, float] = None  # Discharge energy of the day (kWh), e.g. 0
    e_discharge_today2: Union[EmptyStrToNone, float] = None  # SP3000 Discharge Today (kWh), e.g. 0
    e_discharge_today_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 kWh'
    e_discharge_total: Union[EmptyStrToNone, float] = None  # Total discharge energy (kWh), e.g. 1.7
    e_discharge_total2: Union[EmptyStrToNone, float] = None  # SP3000 cumulative discharge (kWh), e.g. 1.7
    e_discharge_total_text: Union[EmptyStrToNone, str] = None  # e.g. '1.7 kWh'
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # Current day (user-grid) electricity (kWh), e.g. 0
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # Total (user-grid) electricity (kWh), e.g. 7648481.6
    e_to_user_today: Union[EmptyStrToNone, float] = None  # Current day (grid-user) electricity (kWh), e.g. 6
    e_to_user_total: Union[EmptyStrToNone, float] = None  # Total (grid-user) electricity (kWh), e.g. 24137119.8
    e_today: Union[EmptyStrToNone, float] = None  # e.g. 6.5
    e_total: Union[EmptyStrToNone, float] = None  # e.g. 1049.6000000000001
    eac_charge_today: Union[EmptyStrToNone, float] = None  # AC charging energy of the day, e.g. 0
    eac_charge_total: Union[EmptyStrToNone, float] = None  # AC total charging energy, e.g. 2.1
    eac_discharge_today: Union[EmptyStrToNone, float] = None  # Bypass load energy on the day of the utility, e.g. 0
    eac_discharge_total: Union[EmptyStrToNone, float] = None  # Mains total bypass load energy, e.g. 0
    eop_discharge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    eop_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv_today: Union[EmptyStrToNone, float] = None  # Panel power of the day (kWh), e.g. 3.3
    epv_today2: Union[EmptyStrToNone, float] = None  # SP3000 The current panel power (kWh), e.g. 3.2
    epv_total: Union[EmptyStrToNone, float] = None  # Total panel power (kWh), e.g. 539.6
    epv_total2: Union[EmptyStrToNone, float] = None  # SP3000 panel cumulative power (kWh), e.g. 511.5
    error_code: Union[EmptyStrToNone, int] = None  # error code, e.g. 0
    error_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    fault_code: Union[EmptyStrToNone, int] = None  # error code, e.g. 0
    freq_grid: Union[EmptyStrToNone, float] = None  # Mains frequency, e.g. 0
    freq_output: Union[EmptyStrToNone, float] = None  # Output frequency, e.g. 0
    gauge_battery_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    gauge_ic_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge_operation_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    gauge_pack_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    gauge_rm1: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge_rm2: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge2_rm1: Union[EmptyStrToNone, float] = None  # e.g. 0
    gauge2_rm2: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_ac_charge: Union[EmptyStrToNone, float] = None  # AC charging current, e.g. 0
    i_charge: Union[EmptyStrToNone, float] = None  # PV terminal charging current (A), e.g. 0
    i_charge_pv1: Union[EmptyStrToNone, float] = None  # PV1 charging current, e.g. 0
    i_charge_pv2: Union[EmptyStrToNone, float] = None  # PV2 charging current, e.g. 0
    i_charge_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    i_discharge: Union[EmptyStrToNone, float] = None  # PV end discharge current (A), e.g. 0
    i_discharge_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    iac_to_grid: Union[EmptyStrToNone, float] = None  # Grid side current (A), e.g. 0
    iac_to_grid_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    iac_to_user: Union[EmptyStrToNone, float] = None  # User side current (A), e.g. 0
    iac_to_user_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    inner_cw_code: Union[EmptyStrToNone, str] = None  # e.g. '0_0'
    ipm_temperature: Union[EmptyStrToNone, float] = None  # IPM temperature (°C), e.g. 39.900001525878906
    ipv: Union[EmptyStrToNone, float] = None  # Input PV current (A) / SP3000 Charging power (W), e.g. 0
    ipv_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 A'
    load_percent: Union[EmptyStrToNone, float] = None  # Percentage of load, e.g. 0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    manual_start_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    max_charge_or_discharge_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    max_charge_or_discharge_current2: Union[EmptyStrToNone, float] = None  # e.g. 0
    normal_power: Union[EmptyStrToNone, int] = None  # Current power (W), e.g. 0
    output_current: Union[EmptyStrToNone, float] = None  # Output current, e.g. 0
    output_power: Union[EmptyStrToNone, float] = None  # Output power, e.g. 0
    output_volt: Union[EmptyStrToNone, float] = None  # Output voltage, e.g. 0
    p_ac_charge: Union[EmptyStrToNone, float] = None  # AC charging power, e.g. 0
    p_ac_input: Union[EmptyStrToNone, float] = None  # AC input energy, e.g. 0
    p_bat: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_charge: Union[EmptyStrToNone, float] = None  # Charging power (W), e.g. 0
    p_charge2: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_charge_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 W'
    p_discharge: Union[EmptyStrToNone, float] = None  # Discharge power (W), e.g. 0
    p_discharge2: Union[EmptyStrToNone, float] = None  # SP3000 Discharge power (W), e.g. 0
    p_discharge_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 W'
    pac_to_grid: Union[EmptyStrToNone, float] = None  # Grid side power (W), e.g. 0
    pac_to_grid_text: Union[EmptyStrToNone, str] = None  # e.g. '0.0 W'
    pac_to_user: Union[EmptyStrToNone, float] = None  # User-side power (V), e.g. 1922.9
    pac_to_user_text: Union[EmptyStrToNone, float] = None  # e.g. '1922.9 W'
    pow_saving_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv: Union[EmptyStrToNone, float] = None  # Panel input power (W), e.g. 1075.4
    ppv2: Union[EmptyStrToNone, float] = None  # SP3000 panel input power (W), e.g. 991.7
    ppv_text: Union[EmptyStrToNone, str] = None  # e.g. '1075.4 W'
    rate_va: Union[EmptyStrToNone, float] = None  # e.g. 0
    rate_watt: Union[EmptyStrToNone, float] = None  # e.g. 0
    remote_cntl_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    remote_cntl_fail_reason: Union[EmptyStrToNone, int] = None  # e.g. 0
    sci_loss_chk_en: Union[EmptyStrToNone, float] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # e.g. 'JZB674901B'
    soh: Union[EmptyStrToNone, float] = None  # e.g. 0
    soh2: Union[EmptyStrToNone, float] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = (
        None  # Energy storage machine status (0: Operating, 1: Charge, 2: Discharge, 3: Fault, 4: Flash), e.g. 0
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Operating'
    storage_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    sys_out: Union[EmptyStrToNone, float] = None  # e.g. 2067.1000000000004
    temperature: Union[EmptyStrToNone, float] = None  # temperature (°C), e.g. 39.79999923706055
    time: Union[EmptyStrToNone, datetime.datetime] = None  # Data time, e.g. '2019-01-14 13:20:57'
    uw_bat_type2: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_bat: Union[EmptyStrToNone, float] = None  # Battery voltage (V), e.g. 50.20000076293945
    v_bat_text: Union[EmptyStrToNone, str] = None  # e.g. '50.2 V'
    v_buck: Union[EmptyStrToNone, float] = None  # vBuk (A), e.g. 161.39999389648438
    v_buck2: Union[EmptyStrToNone, float] = None  # vBuck2 (A), e.g. 167.3000030517578
    v_buck_text: Union[EmptyStrToNone, str] = None  # e.g. '161.4 V'
    v_bus: Union[EmptyStrToNone, float] = None  # e.g. 171.6999969482422
    v_grid: Union[EmptyStrToNone, float] = None  # Mains voltage, e.g. 0
    vac: Union[EmptyStrToNone, float] = None  # Grid voltage (V), e.g. 226.5
    vac_Text: Union[EmptyStrToNone, str] = None  # e.g. '226.5 V'
    vpv: Union[EmptyStrToNone, float] = None  # Input PV voltage (V), e.g. 161.39999389648438
    vpv2: Union[EmptyStrToNone, float] = None  # SP3000 Input PV voltage (V), e.g. 167.60000610351562
    vpv_text: Union[EmptyStrToNone, str] = None  # e.g. '161.4 V'
    warn_code: Union[EmptyStrToNone, int] = None  # Warn Code, e.g. 0
    warn_info: Union[EmptyStrToNone, int] = None  # e.g. 0
    warn_info2: Union[EmptyStrToNone, int] = None  # e.g. 0
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    with_time: Union[EmptyStrToNone, bool] = None  # e.g. False


def _storage_energy_overview_to_camel(snake: str) -> str:
    override = {
        "device_sn": "storage_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class StorageEnergyOverview(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_storage_energy_overview_to_camel,
    )

    data: Union[EmptyStrToNone, StorageEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Storage energy history #############################################################################################


def _storage_energy_history_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "storage_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class StorageEnergyHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_storage_energy_history_data_to_camel,
    )

    count: int  # Total Records
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    datas: List[StorageEnergyOverviewData]


class StorageEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, StorageEnergyHistoryData] = None


# #####################################################################################################################
# Storage alarms #####################################################################################################


class StorageAlarm(ApiModel):
    alarm_code: Union[EmptyStrToNone, int] = None  # alarm code, e.g. 25
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    end_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm start time, e.g. "2019-03-09 09:55:55.0"
    start_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm end time, e.g. "2019-03-09 09:55:55.0"
    alarm_message: Union[EmptyStrToNone, str] = None  # alarm information, e.g. "No utility."


def _storage_alarms_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "sn",
    }
    return override.get(snake, to_camel(snake=snake))


class StorageAlarmsData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_storage_alarms_data_to_camel,
    )

    count: int  # Total Records
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    alarms: List[StorageAlarm]


class StorageAlarms(ApiResponse):
    data: Union[EmptyStrToNone, StorageAlarmsData] = None
