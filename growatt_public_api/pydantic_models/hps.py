import datetime
from typing import Union, Any, List, Optional

from pydantic import (
    ConfigDict,
)
from pydantic.alias_generators import to_camel

from .api_model import (
    ApiResponse,
    EmptyStrToNone,
    ApiModel,
    GrowattTimeCalendar,
)


# #####################################################################################################################
# Hps details #########################################################################################################


def _hps_detail_data_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "discharge_day_map": "disChargeDayMap",
        "discharge_month": "disChargeMonth",
        "parent_id": "parentID",
        "plant_name": "plantname",
        "tree_id": "treeID",
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


class HpsDetailData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_hps_detail_data_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 9
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. 'PCS000001'
    charge_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {},
    charge_month: Union[EmptyStrToNone, int] = None  # e.g. 0,
    children: List[Any]  # e.g. []
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'WFD091500E'
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    discharge_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    discharge_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_charge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_discharge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'RH1.0'
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    hps_set_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    id: Union[EmptyStrToNone, int] = None  # e.g. 26
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Internal version number, e.g. 'null'
    last_update_time: Union[EmptyStrToNone, GrowattTimeCalendar] = (
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
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'port_name'
    power_max: Union[EmptyStrToNone, float] = None  # e.g. ''
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    pv_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'LHD0847002'
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: disconnected, 1: online, 2: standby, 3: failure, all others are offline), e.g. 0
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'hps.status.los'
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. '47.107.154.111'
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_FDCJQ00003'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ''


class HpsDetails(ApiResponse):
    data: Union[EmptyStrToNone, HpsDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the energy storage machine, e.g. "WFD091500E"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "UHD0918003"


# #####################################################################################################################
# Hps energy overview #################################################################################################


def _hps_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "dataLogSn",
    }
    return override.get(snake, to_camel(snake=snake))


class HpsEnergyOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_hps_energy_overview_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alarm_code1: Union[EmptyStrToNone, int] = None  # e.g. 0
    alarm_code2: Union[EmptyStrToNone, int] = None  # e.g. 0
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    ats_bypass: Union[EmptyStrToNone, int] = None  # e.g. 0
    b_active_power: Union[EmptyStrToNone, float] = None  # e.g. 19
    batcdct: Union[EmptyStrToNone, float] = None  # e.g. 0
    batldt: Union[EmptyStrToNone, float] = None  # e.g. 0
    batnir: Union[EmptyStrToNone, float] = None  # e.g. 0
    batpir: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_protection: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_show_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_status: Union[EmptyStrToNone, int] = None  # Battery Status, e.g. 361
    bms_volt_status: Union[EmptyStrToNone, int] = None  # e.g. 1690
    bmstc: Union[EmptyStrToNone, float] = None  # e.g. 0
    bmstv: Union[EmptyStrToNone, float] = None  # e.g. 0
    bvbus: Union[EmptyStrToNone, float] = None  # e.g. 59
    bvbus_nega: Union[EmptyStrToNone, float] = None  # e.g. 61
    bvbus_posi: Union[EmptyStrToNone, float] = None  # e.g. 60
    bypass_freq: Union[EmptyStrToNone, float] = None  # e.g. 8.100000381469727
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    capacity: Union[EmptyStrToNone, float] = None  # e.g. 470
    cfdllc1: Union[EmptyStrToNone, float] = None  # e.g. 0
    cfdllc2: Union[EmptyStrToNone, float] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'QMN0000000000000'
    day: Union[EmptyStrToNone, str] = None  # e.g. ''
    dg_grid_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    dg_grid_select: Union[EmptyStrToNone, int] = None  # e.g. 0
    e_bat_charge_time_total: Union[EmptyStrToNone, float] = None  # e.g. 4.8
    e_bat_charge_total: Union[EmptyStrToNone, float] = None  # e.g. 12
    e_bat_discharge_time_total: Union[EmptyStrToNone, float] = None  # e.g. 0.6
    e_bat_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 0.3
    e_charge_time_today: Union[EmptyStrToNone, float] = None  # e.g. 27
    e_charge_today: Union[EmptyStrToNone, float] = None  # The amount of charge in the system that day, e.g. 26
    e_discharge_time_today: Union[EmptyStrToNone, float] = None  # e.g. 25
    e_discharge_today: Union[EmptyStrToNone, float] = None  # System discharge capacity of the day, e.g. 24
    e_grid_time_today: Union[EmptyStrToNone, float] = None  # e.g. 573.5
    e_grid_time_total: Union[EmptyStrToNone, float] = None  # e.g. 8.90000057220459
    e_grid_today: Union[EmptyStrToNone, float] = None  # e.g. 1.899999976158142
    e_grid_total: Union[EmptyStrToNone, float] = None  # e.g. 1.899999976158142
    e_load_time_today: Union[EmptyStrToNone, float] = None  # e.g. 92.80000305175781
    e_load_time_total: Union[EmptyStrToNone, float] = None  # e.g. 1.2000000476837158
    e_load_today: Union[EmptyStrToNone, float] = None  # e.g. 4.800000190734863
    e_load_total: Union[EmptyStrToNone, float] = None  # e.g. 4.800000190734863
    e_to_grid_time_today: Union[EmptyStrToNone, float] = None  # e.g. 296.29998779296875
    e_to_grid_time_total: Union[EmptyStrToNone, float] = None  # e.g. 4.400000095367432
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # Daily incoming electricity of the grid, e.g. 5
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # Total grid power, e.g. 5
    effectiveness: Union[EmptyStrToNone, float] = None  # e.g. 99
    epv_time_today: Union[EmptyStrToNone, float] = None  # e.g. 358.1
    epv_time_total: Union[EmptyStrToNone, float] = None  # e.g. 5.5
    epv_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv_total: Union[EmptyStrToNone, float] = None  # PV total power generation, e.g. 21.8
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 0
    grid_freq: Union[EmptyStrToNone, float] = None  # e.g. 210
    gvpvuv: Union[EmptyStrToNone, float] = None  # e.g. 230.5
    gvpvvw: Union[EmptyStrToNone, float] = None  # e.g. 0
    gvpvwu: Union[EmptyStrToNone, float] = None  # e.g. 0
    hps_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    i_buck1: Union[EmptyStrToNone, float] = None  # e.g. 0.10000000149011612
    i_buck2: Union[EmptyStrToNone, float] = None  # e.g. 0.10000000149011612
    i_buck3: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_buck4: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_buck5: Union[EmptyStrToNone, float] = None  # e.g. 0
    ibat: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    iboard: Union[EmptyStrToNone, float] = None  # e.g. -0.10000000149011612
    id: Union[EmptyStrToNone, int] = None  # e.g. 4
    inductor_curr: Union[EmptyStrToNone, float] = None  # e.g. 0
    insul_detec_nega: Union[EmptyStrToNone, float] = None  # e.g. 1000
    insul_detec_posi: Union[EmptyStrToNone, float] = None  # e.g.  1000
    invuv: Union[EmptyStrToNone, float] = None  # e.g. 0
    invvw: Union[EmptyStrToNone, float] = None  # e.g. 0
    invwu: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv: Union[EmptyStrToNone, float] = None  # e.g. 0.8999999761581421
    ipv2: Union[EmptyStrToNone, float] = None  # PV2 input current, e.g. 0.800000011920929
    ipva: Union[EmptyStrToNone, float] = None  # e.g. 0.4000000059604645
    ipvb: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipvc: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipvu: Union[EmptyStrToNone, float] = None  # e.g. 0.10000000149011612
    ipvv: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipvw: Union[EmptyStrToNone, float] = None  # e.g. 0
    load_active_power: Union[EmptyStrToNone, float] = None  # e.g. 49
    load_ia: Union[EmptyStrToNone, float] = None  # e.g. 53
    load_ib: Union[EmptyStrToNone, float] = None  # e.g. 54
    load_ic: Union[EmptyStrToNone, float] = None  # e.g. 55
    load_pf: Union[EmptyStrToNone, float] = None  # e.g. 52
    load_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 50
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
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 0
    pac1: Union[EmptyStrToNone, float] = None  # Inverter output apparent power 1, e.g. 0
    pac2: Union[EmptyStrToNone, float] = None  # Inverter output apparent power 2, e.g. 0
    pf: Union[EmptyStrToNone, float] = None  # e.g. 0.23000000417232513
    pf_symbol: Union[EmptyStrToNone, int] = None  # e.g. 220
    ppv: Union[EmptyStrToNone, float] = None  # Total PV input power, e.g. 0
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power, e.g. 0
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power, e.g. 0
    pvnir1: Union[EmptyStrToNone, float] = None  # e.g. 1000
    pvpir1: Union[EmptyStrToNone, float] = None  # e.g. 1000
    rac: Union[EmptyStrToNone, float] = None  # e.g. 0
    run_model: Union[EmptyStrToNone, int] = None  # e.g. 5
    run_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    scrtemp: Union[EmptyStrToNone, float] = None  # e.g. 0
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
    sys_fault_word9: Union[EmptyStrToNone, int] = None  # e.g. 256
    temp1: Union[EmptyStrToNone, float] = None  # Temperature 1, e.g. 34
    temp2: Union[EmptyStrToNone, float] = None  # Temperature 2, e.g. 33.099998474121094
    temp3: Union[EmptyStrToNone, float] = None  # e.g. 32
    temp4: Union[EmptyStrToNone, float] = None  # e.g. 33
    temp5: Union[EmptyStrToNone, float] = None  # e.g. 35
    temp6: Union[EmptyStrToNone, float] = None  # e.g. 36
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-09 14:52:39'
    type_flag: Union[EmptyStrToNone, int] = None  # e.g. 1430
    vbat: Union[EmptyStrToNone, float] = None  # e.g. -1.5
    vpv: Union[EmptyStrToNone, float] = None  # e.g. 1.7000000476837158
    vpv2: Union[EmptyStrToNone, float] = None  # PV2 input voltage, e.g. -0.5
    vpvun: Union[EmptyStrToNone, float] = None  # e.g. 1
    vpvuv: Union[EmptyStrToNone, float] = None  # e.g. 56
    vpvvn: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpvvw: Union[EmptyStrToNone, float] = None  # e.g. 57
    vpvwn: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpvwu: Union[EmptyStrToNone, float] = None  # e.g. 58
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the data sent has its own time, e.g. False


def _hps_energy_overview_to_camel(snake: str) -> str:
    override = {
        "device_sn": "hps_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class HpsEnergyOverview(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_hps_energy_overview_to_camel,
    )

    data: Union[EmptyStrToNone, HpsEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "JPC2827188"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "LHD0847002"


# #####################################################################################################################
# Hps energy history ##################################################################################################


def _hps_energy_history_data_to_camel(snake: str) -> str:
    override = {
        "device_sn": "hps_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class HpsEnergyHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_hps_energy_history_data_to_camel,
    )

    count: int  # Total Records
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. ""SATA818009""
    datas: List[HpsEnergyOverviewData]
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. ""TLMAX00B01""
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21


class HpsEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, HpsEnergyHistoryData] = None


# #####################################################################################################################
# Hps alarms ##########################################################################################################


class HpsAlarm(ApiModel):
    alarm_code: Union[EmptyStrToNone, str] = None  # alarm code, e.g. 5-110-2
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    end_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm start time, e.g. "2019-03-09 09:55:55.0"
    start_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm end time, e.g. "2019-03-09 09:55:55.0"
    alarm_message: Union[EmptyStrToNone, str] = None  # alarm information, e.g. "BYTE110_2"


def _hps_alarms_data_to_camel(snake: str) -> str:
    override = {
        "device_sn": "hps_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class HpsAlarmsData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_hps_alarms_data_to_camel,
    )

    count: int  # Total Records
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "UHD0918003"
    alarms: List[HpsAlarm]


class HpsAlarms(ApiResponse):
    data: Union[EmptyStrToNone, HpsAlarmsData] = None
