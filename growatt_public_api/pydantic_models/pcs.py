import datetime
from typing import Union, Any, List

from pydantic import (
    ConfigDict,
)
from pydantic.alias_generators import to_camel

from .api_model import (
    ApiResponse,
    EmptyStrToNone,
    GrowattTime,
    ApiModel,
    GrowattTimeCalendar,
)


# #####################################################################################################################
# Pcs details #########################################################################################################


def _pcs_detail_data_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "discharge_day_map": "disChargeDayMap",
        "discharge_month": "disChargeMonth",
        "discharge_month_2": "dischargeMonth",  # avoid name collision
        "parent_id": "parentID",
        "plant_name": "plantname",
        "tree_id": "treeID",
    }
    return override.get(snake, to_camel(snake=snake))


class PcsDetailData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pcs_detail_data_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 9
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. 'PCS000001'
    charge_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {},
    charge_month: Union[EmptyStrToNone, int] = None  # e.g. 0,
    charge_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0',
    children: List[Any]  # e.g. []
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'MONITOR002'
    discharge_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    discharge_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    discharge_month_2: Union[EmptyStrToNone, float] = None  # e.g. 0
    discharge_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    e_charge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_discharge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'RH1.0'
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Internal version number, e.g. 'rHAA020202'
    last_update_time: Union[EmptyStrToNone, GrowattTime] = (
        None  # Last update time, e.g. {'date': 12, 'day': 2, 'hours': 16, 'minutes': 46, 'month': 3, 'seconds': 22, 'time': 1649753182000, 'timezoneOffset': -480, 'year': 122}
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-12 16:46:22'
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    location: Union[EmptyStrToNone, str] = None  # address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: disconnected), e.g. True
    model: Union[EmptyStrToNone, int] = None  # model, e.g. 2666130979655057522
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'S25B00D00T00P0FU01M0072'
    normalPower: Union[EmptyStrToNone, int] = None  # e.g. 500000
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_VC51030322020001_22'
    peak_clipping: Union[EmptyStrToNone, float] = None  # e.g. 0
    peak_clipping_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'port_name'
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'LHD0847002'
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: disconnected, 1: online, 2: standby, 3: failure, all others are offline), e.g. 0
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'tlx.status.operating'
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. '47.107.154.111'
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_FDCJQ00003'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ''


class PcsDetails(ApiResponse):
    data: Union[EmptyStrToNone, PcsDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the energy storage machine, e.g. "MONITOR002"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "PCS000001"


# #####################################################################################################################
# Pcs energy overview #################################################################################################


def _pcs_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "dataLogSn",
        "power_grid": "powerGird",
        "to_power_grid": "toPowerGird",
    }
    return override.get(snake, to_camel(snake=snake))


class PcsEnergyOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pcs_energy_overview_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alarm_code1: Union[EmptyStrToNone, int] = None  # e.g. 0
    alarm_code2: Union[EmptyStrToNone, int] = None  # e.g. 0
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    ats_bypass: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_active_power: Union[EmptyStrToNone, float] = None  # e.g. 19
    b_apparent_power: Union[EmptyStrToNone, float] = None  # e.g. 18
    b_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 20
    bipv: Union[EmptyStrToNone, float] = None  # e.g. 2
    bipvu: Union[EmptyStrToNone, float] = None  # e.g. 7
    bipvv: Union[EmptyStrToNone, float] = None  # e.g. 8
    bipvw: Union[EmptyStrToNone, float] = None  # e.g. 9
    bms_protection: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_status: Union[EmptyStrToNone, int] = None  # Battery Status, e.g. 361
    bms_volt_status: Union[EmptyStrToNone, int] = None  # e.g. 1690
    bvbus: Union[EmptyStrToNone, float] = None  # e.g. 59
    bvbus_nega: Union[EmptyStrToNone, float] = None  # e.g. 61
    bvbus_posi: Union[EmptyStrToNone, float] = None  # e.g. 60
    bvpv: Union[EmptyStrToNone, float] = None  # e.g. 1
    bvpvuv: Union[EmptyStrToNone, float] = None  # e.g. 13
    bvpvvw: Union[EmptyStrToNone, float] = None  # e.g. 14
    bvpvwu: Union[EmptyStrToNone, float] = None  # e.g. 15
    bypass_freq: Union[EmptyStrToNone, float] = None  # e.g. 8.100000381469727
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    capacity: Union[EmptyStrToNone, float] = None  # e.g. 470
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'QMN0000000000000'
    day: Union[EmptyStrToNone, str] = None  # e.g. ''
    dg_grid_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    dg_grid_select: Union[EmptyStrToNone, int] = None  # e.g. 0
    e_charge_time_today: Union[EmptyStrToNone, float] = None  # e.g. 27
    e_charge_time_total: Union[EmptyStrToNone, float] = None  # e.g. 1690932
    e_charge_today: Union[EmptyStrToNone, float] = None  # The amount of charge in the system that day, e.g. 26
    e_charge_total: Union[EmptyStrToNone, float] = None  # Total system charge, e.g. 1690930
    e_discharge_time_today: Union[EmptyStrToNone, float] = None  # e.g. 25
    e_discharge_time_total: Union[EmptyStrToNone, float] = None  # e.g. 1690932
    e_discharge_today: Union[EmptyStrToNone, float] = None  # System discharge capacity of the day, e.g. 24
    e_discharge_total: Union[EmptyStrToNone, float] = None  # Total system discharge, e.g. 1690930
    electric_state: Union[EmptyStrToNone, int] = None  # e.g. 5
    gfdi1: Union[EmptyStrToNone, float] = None  # e.g. 42
    gfdi2: Union[EmptyStrToNone, float] = None  # e.g. 43
    grid_freq: Union[EmptyStrToNone, float] = None  # e.g. 210
    grid_time_today: Union[EmptyStrToNone, float] = None  # e.g. 95
    grid_time_total: Union[EmptyStrToNone, float] = None  # e.g. 6422627
    grid_today: Union[EmptyStrToNone, float] = None  # e.g. 94
    grid_total: Union[EmptyStrToNone, float] = None  # e.g. 6291553
    i1a: Union[EmptyStrToNone, float] = None  # e.g. 10
    i1b: Union[EmptyStrToNone, float] = None  # e.g. 11
    i1c: Union[EmptyStrToNone, float] = None  # e.g. 12
    load_active_power: Union[EmptyStrToNone, float] = None  # e.g. 49
    load_apparent_power: Union[EmptyStrToNone, float] = None  # e.g. 48
    load_ia: Union[EmptyStrToNone, float] = None  # e.g. 53
    load_ib: Union[EmptyStrToNone, float] = None  # e.g. 54
    load_ic: Union[EmptyStrToNone, float] = None  # e.g. 55
    load_pf: Union[EmptyStrToNone, float] = None  # e.g. 52
    load_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 50
    load_time_today: Union[EmptyStrToNone, float] = None  # e.g. 83
    load_time_total: Union[EmptyStrToNone, float] = None  # e.g. 5636183
    load_today: Union[EmptyStrToNone, float] = None  # e.g. 82
    load_total: Union[EmptyStrToNone, float] = None  # e.g. 5505109
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    max_charge_curr: Union[EmptyStrToNone, float] = None  # e.g. 100
    max_discharge_curr: Union[EmptyStrToNone, float] = None  # e.g. 101
    max_min_temp_cell: Union[EmptyStrToNone, float] = None  # e.g. 6
    max_temp: Union[EmptyStrToNone, float] = None  # e.g. 6
    max_temp_num: Union[EmptyStrToNone, float] = None  # e.g. 6
    max_volt: Union[EmptyStrToNone, float] = None  # e.g. 1
    max_volt_cell: Union[EmptyStrToNone, float] = None  # e.g. 6
    max_volt_num: Union[EmptyStrToNone, float] = None  # e.g. 194
    maxmin_volt_cell: Union[EmptyStrToNone, float] = None  # e.g. 6
    min_temp: Union[EmptyStrToNone, float] = None  # e.g. 174
    min_temp_group: Union[EmptyStrToNone, float] = None  # e.g. 134
    min_temp_num: Union[EmptyStrToNone, float] = None  # e.g. 164
    min_volt: Union[EmptyStrToNone, float] = None  # e.g. 1
    min_volt_cell: Union[EmptyStrToNone, float] = None  # e.g. 6
    min_volt_group: Union[EmptyStrToNone, float] = None  # e.g. 144
    min_volt_num: Union[EmptyStrToNone, float] = None  # e.g. 184
    mvpv: Union[EmptyStrToNone, float] = None  # e.g. 0.46000000834465027
    out_apparent_power: Union[EmptyStrToNone, float] = None  # e.g. 78
    out_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 80
    pac_to_battery: Union[EmptyStrToNone, float] = None  # e.g. 17
    pac_to_grid: Union[EmptyStrToNone, float] = None  # e.g. 0
    pcs_active_power: Union[EmptyStrToNone, float] = None  # e.g. 79
    pcs_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    pf: Union[EmptyStrToNone, float] = None  # e.g. 0.23000000417232513
    pf_symbol: Union[EmptyStrToNone, int] = None  # e.g. 220
    power_grid: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv: Union[EmptyStrToNone, float] = None  # Total PV input power, e.g. 108000
    pv_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    riso_batn: Union[EmptyStrToNone, float] = None  # e.g. 41
    riso_batp: Union[EmptyStrToNone, float] = None  # e.g. 40
    self_time: Union[EmptyStrToNone, float] = None  # e.g. 450
    serial_num: Union[EmptyStrToNone, str] = None  # e.g. 'LHD0847002'
    status: Union[EmptyStrToNone, int] = None  # e.g. 5
    status_lang: Union[EmptyStrToNone, str] = None  # e.g. 'common_normal'
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'PV Bat Online'
    sys_fault_word1: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word2: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word3: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word4: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word5: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word6: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word7: Union[EmptyStrToNone, int] = None  # e.g. 256
    sys_fault_word8: Union[EmptyStrToNone, int] = None  # e.g. 256
    temp1: Union[EmptyStrToNone, float] = None  # Temperature 1, e.g. 34
    temp2: Union[EmptyStrToNone, float] = None  # Temperature 2, e.g. 33.099998474121094
    temp3: Union[EmptyStrToNone, float] = None  # e.g. 32
    temp4: Union[EmptyStrToNone, float] = None  # e.g. 33
    temp5: Union[EmptyStrToNone, float] = None  # e.g. 35
    temp6: Union[EmptyStrToNone, float] = None  # e.g. 36
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-09 14:52:39'
    to_grid_time_today: Union[EmptyStrToNone, float] = None  # e.g. 89
    to_grid_time_total: Union[EmptyStrToNone, float] = None  # e.g. 6029405
    to_grid_today: Union[EmptyStrToNone, float] = None  # e.g. 88
    to_grid_total: Union[EmptyStrToNone, float] = None  # e.g. 5898331
    to_power_grid: Union[EmptyStrToNone, float] = None  # e.g. 0
    type_flag: Union[EmptyStrToNone, int] = None  # e.g. 1430
    vac_frequency: Union[EmptyStrToNone, float] = None  # e.g. 1.600000023841858
    vacu: Union[EmptyStrToNone, float] = None  # e.g. 135
    vacuv: Union[EmptyStrToNone, float] = None  # e.g. 4
    vacv: Union[EmptyStrToNone, float] = None  # e.g. 136
    vacvw: Union[EmptyStrToNone, float] = None  # e.g. 5
    vacw: Union[EmptyStrToNone, float] = None  # e.g. 137
    vacwu: Union[EmptyStrToNone, float] = None  # e.g. 6
    vpvuv: Union[EmptyStrToNone, float] = None  # e.g. 56
    vpvvw: Union[EmptyStrToNone, float] = None  # e.g. 57
    vpvwu: Union[EmptyStrToNone, float] = None  # e.g. 58
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the data sent has its own time, e.g. False


def _pcs_energy_overview_to_camel(snake: str) -> str:
    override = {
        "device_sn": "pcs_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class PcsEnergyOverview(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pcs_energy_overview_to_camel,
    )

    data: Union[EmptyStrToNone, PcsEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "WFD0947012"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "TND093000E"


# #####################################################################################################################
# Pcs energy history ##################################################################################################


def _pcs_energy_history_data_to_camel(snake: str) -> str:
    override = {
        "device_sn": "pcs_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class PcsEnergyHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pcs_energy_history_data_to_camel,
    )

    count: int  # Total Records
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "MONITOR001"
    datas: List[PcsEnergyOverviewData]
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "PCS1234567"
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21


class PcsEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, PcsEnergyHistoryData] = None


# #####################################################################################################################
# Pcs alarms ##########################################################################################################


class PcsAlarm(ApiModel):
    alarm_code: Union[EmptyStrToNone, int] = None  # alarm code, e.g. 25
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    end_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm start time, e.g. "2019-03-09 09:55:55.0"
    start_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm end time, e.g. "2019-03-09 09:55:55.0"
    alarm_message: Union[EmptyStrToNone, str] = None  # alarm information, e.g. "No utility."


def _pcs_alarms_data_to_camel(snake: str) -> str:
    override = {
        "device_sn": "pcs_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class PcsAlarmsData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pcs_alarms_data_to_camel,
    )

    count: int  # Total Records
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "SARN744005"
    alarms: List[PcsAlarm]


class PcsAlarms(ApiResponse):
    data: Union[EmptyStrToNone, PcsAlarmsData] = None
