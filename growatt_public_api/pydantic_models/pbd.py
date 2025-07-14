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
# PBD details #########################################################################################################


def _pbd_detail_data_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "discharge_day_map": "disChargeDayMap",
        "discharge_month": "disChargeMonth",
        "discharge_month_2": "dischargeMonth",  # avoid name collision
        "parent_id": "parentID",
        "plant_name": "plantname",
        "riso_min": "risomin",
        "tree_id": "treeID",
    }
    return override.get(snake, to_camel(snake=snake))


class PbdDetailData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pbd_detail_data_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 9
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. 'PCS000001'
    biout: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_enable: Union[EmptyStrToNone, bool] = None  # 1
    bvout: Union[EmptyStrToNone, float] = None  # 0
    charge_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {},
    charge_month: Union[EmptyStrToNone, int] = None  # e.g. 0,
    children: List[Any]  # e.g. []
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'WFD091500E'
    discharge_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    discharge_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    discharge_month_2: Union[EmptyStrToNone, float] = None  # e.g. 0
    discharge_month_text: Union[EmptyStrToNone, str] = None  # '0'
    e_charge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_discharge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'RH1.0'
    grid_detection_time: Union[EmptyStrToNone, float] = None  # 60
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    i_out_max: Union[EmptyStrToNone, float] = None  # 0
    i_out_min: Union[EmptyStrToNone, float] = None  # 500
    i_pv_l_max: Union[EmptyStrToNone, float] = None  # 500
    i_pv_max: Union[EmptyStrToNone, float] = None  # 500
    icharge: Union[EmptyStrToNone, float] = None  # 1
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Internal version number, e.g. 'null'
    ipv: Union[EmptyStrToNone, float] = None  # 0
    ipv1: Union[EmptyStrToNone, float] = None  # 0
    ipv2: Union[EmptyStrToNone, float] = None  # 0
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
    on_off: Union[EmptyStrToNone, bool] = None  # 1
    out_power_max: Union[EmptyStrToNone, float] = None  # 100
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_VC51030322020001_22'
    peak_clipping: Union[EmptyStrToNone, float] = None  # 0
    peak_clipping_total: Union[EmptyStrToNone, float] = None  # 0
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'port_name'
    power_start: Union[EmptyStrToNone, float] = None  # 1
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    restore: Union[EmptyStrToNone, float] = None  # 0
    riso_enable: Union[EmptyStrToNone, float] = None  # 0
    riso_min: Union[EmptyStrToNone, float] = None  # 33
    rs_addr: Union[EmptyStrToNone, float] = None  # 3
    safety: Union[EmptyStrToNone, float] = None  # 2
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'LHD0847002'
    soc_max: Union[EmptyStrToNone, float] = None  # 0
    soc_min: Union[EmptyStrToNone, float] = None  # 0
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: disconnected, 1: online, 2: standby, 3: failure, all others are offline), e.g. 0
    )
    status_lang: Union[EmptyStrToNone, str] = None  # 'Lost'
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'hps.status.los'
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. '47.107.154.111'
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_FDCJQ00003'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    type: Union[EmptyStrToNone, int] = None  # 1
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    v_mppt_max: Union[EmptyStrToNone, float] = None  # 844.7999877929688
    v_mppt_min: Union[EmptyStrToNone, float] = None  # 14.800000190734863
    v_out_max: Union[EmptyStrToNone, float] = None  # 450
    v_out_min: Union[EmptyStrToNone, float] = None  # 450
    v_pv_max: Union[EmptyStrToNone, float] = None  # 1000
    v_start: Union[EmptyStrToNone, float] = None  # 450
    vpv: Union[EmptyStrToNone, float] = None  # 0
    vpv1: Union[EmptyStrToNone, float] = None  # 0
    vpv2: Union[EmptyStrToNone, float] = None  # 545.5


class PbdDetails(ApiResponse):
    data: Union[EmptyStrToNone, PbdDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the energy storage machine, e.g. "MONITOR003"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "HPS0000001"


# #####################################################################################################################
# PBD energy overview #################################################################################################


def _pbd_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "dataLogSn",
        "biout_buck1": "biOutBuck1",
        "biout_buck2": "biOutBuck2",
        "pbd_out_power": "pbdOutPowe",
        "riso_bat_n": "risoBatn",
        "riso_bat_p": "risoBatp",
        "riso_bus_n": "risoBusn",
        "riso_bus_p": "risoBusp",
        "riso_pv_n": "risoPVn",
        "riso_pv_p": "risoPVp",
    }
    return override.get(snake, to_camel(snake=snake))


class PbdEnergyOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pbd_energy_overview_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alarm_code1: Union[EmptyStrToNone, int] = None  # e.g. 0
    alarm_code2: Union[EmptyStrToNone, int] = None  # e.g. 0
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    biout_buck1: Union[EmptyStrToNone, float] = None  # e.g. 192
    biout_buck2: Union[EmptyStrToNone, float] = None  # e.g. 193
    biout: Union[EmptyStrToNone, float] = None  # e.g. 191
    bipv_buck1: Union[EmptyStrToNone, float] = None  # e.g. 157
    bipv_buck2: Union[EmptyStrToNone, float] = None  # e.g. 158
    bipv_buck3: Union[EmptyStrToNone, float] = None  # e.g. 211
    bipv_buck4: Union[EmptyStrToNone, float] = None  # e.g. 212
    bipv_buck5: Union[EmptyStrToNone, float] = None  # e.g. 213
    bms_protection: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_status: Union[EmptyStrToNone, int] = None  # Battery Status, e.g. 361
    bms_volt_status: Union[EmptyStrToNone, int] = None  # e.g. 1690
    bvbus: Union[EmptyStrToNone, float] = None  # e.g. 59
    bvout: Union[EmptyStrToNone, float] = None  # e.g. 190
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    capacity: Union[EmptyStrToNone, float] = None  # e.g. 470
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'QMN0000000000000'
    day: Union[EmptyStrToNone, str] = None  # e.g. ''
    e_charge_time_today: Union[EmptyStrToNone, float] = None  # e.g. 27
    e_charge_time_total: Union[EmptyStrToNone, float] = None  # e.g. 156
    e_charge_today: Union[EmptyStrToNone, float] = None  # The amount of charge in the system that day, e.g. 26
    e_charge_total: Union[EmptyStrToNone, float] = None  # Total system charge, e.g. 154
    e_discharge_time_today: Union[EmptyStrToNone, float] = None  # e.g. 25
    e_discharge_time_total: Union[EmptyStrToNone, float] = None  # e.g. 152
    e_discharge_today: Union[EmptyStrToNone, float] = None  # System discharge capacity of the day, e.g. 24
    e_discharge_total: Union[EmptyStrToNone, float] = None  # Total system discharge, e.g. 150
    e_out_today: Union[EmptyStrToNone, float] = None  # e.g. 201
    e_out_total: Union[EmptyStrToNone, float] = None  # e.g. 13238500.0
    electric_state: Union[EmptyStrToNone, int] = None  # e.g. -1
    epv_time_today: Union[EmptyStrToNone, float] = None  # e.g. 358.1
    epv_time_total: Union[EmptyStrToNone, float] = None  # e.g. 5.5
    epv_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv_total: Union[EmptyStrToNone, float] = None  # PV total power generation, e.g. 21.8
    id: Union[EmptyStrToNone, int] = None  # e.g. 4
    ipv: Union[EmptyStrToNone, float] = None  # e.g. 0.8999999761581421
    ipv1: Union[EmptyStrToNone, float] = None  # PV1 input current, e.g. 84
    ipv2: Union[EmptyStrToNone, float] = None  # PV2 input current, e.g. 0.800000011920929
    ipv3: Union[EmptyStrToNone, float] = None  # PV3 input current, e.g. 208
    ipv4: Union[EmptyStrToNone, float] = None  # PV4 input current, e.g. 209
    ipv5: Union[EmptyStrToNone, float] = None  # PV5 input current, e.g. 210
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
    pbd_bat_power: Union[EmptyStrToNone, float] = None  # e.g. 98
    pbd_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    pbd_out_power: Union[EmptyStrToNone, float] = None  # e.g. 194
    ppv: Union[EmptyStrToNone, float] = None  # Total PV input power, e.g. 0
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power, e.g. 0
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power, e.g. 0
    ppv3: Union[EmptyStrToNone, float] = None  # PV3 input power, e.g. 214
    ppv4: Union[EmptyStrToNone, float] = None  # PV4 input power, e.g. 215
    ppv5: Union[EmptyStrToNone, float] = None  # PV5 input power, e.g. 216
    riso_bat_n: Union[EmptyStrToNone, float] = None  # e.g. 122
    riso_bat_p: Union[EmptyStrToNone, float] = None  # e.g. 121
    riso_bus_n: Union[EmptyStrToNone, float] = None  # e.g. 200
    riso_bus_p: Union[EmptyStrToNone, float] = None  # e.g. 199
    riso_pv_n: Union[EmptyStrToNone, float] = None  # e.g. 120
    riso_pv_p: Union[EmptyStrToNone, float] = None  # e.g. 119
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
    temp: Union[EmptyStrToNone, float] = None  # Temperature, e.g. 117
    tempout_buck_l: Union[EmptyStrToNone, float] = None  # e.g. 198
    tempout_buck_module: Union[EmptyStrToNone, float] = None  # e.g. 196
    temppv_buck_l: Union[EmptyStrToNone, float] = None  # e.g. 197
    temppv_buck_module: Union[EmptyStrToNone, float] = None  # e.g. 195
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-09 14:52:39'
    type_flag: Union[EmptyStrToNone, int] = None  # e.g. 1430
    vbat: Union[EmptyStrToNone, float] = None  # e.g. -1.5
    vpv: Union[EmptyStrToNone, float] = None  # e.g. 1.7000000476837158
    vpv1: Union[EmptyStrToNone, float] = None  # PV1 input voltage, e.g. 81
    vpv2: Union[EmptyStrToNone, float] = None  # PV2 input voltage, e.g. -0.5
    vpv3: Union[EmptyStrToNone, float] = None  # PV3 input voltage, e.g. 204
    vpv4: Union[EmptyStrToNone, float] = None  # PV4 input voltage, e.g. 205
    vpv5: Union[EmptyStrToNone, float] = None  # PV5 input voltage, e.g. 207
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the data sent has its own time, e.g. False


def _pbd_energy_overview_to_camel(snake: str) -> str:
    override = {
        "device_sn": "pbd_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class PbdEnergyOverview(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pbd_energy_overview_to_camel,
    )

    data: Union[EmptyStrToNone, PbdEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "MONITOR003"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "HPS0000001"


# #####################################################################################################################
# PBD energy history ##################################################################################################


def _pbd_energy_history_data_to_camel(snake: str) -> str:
    override = {
        "device_sn": "pbd_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class PbdEnergyHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pbd_energy_history_data_to_camel,
    )

    count: int  # Total Records
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. ""MONITOR003""
    datas: List[PbdEnergyOverviewData]
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. ""HPS0000001""
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21


class PbdEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, PbdEnergyHistoryData] = None


# #####################################################################################################################
# PBD alarms ##########################################################################################################


class PbdAlarm(ApiModel):
    alarm_code: Union[EmptyStrToNone, str] = None  # alarm code, e.g. 5-110-2
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    end_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm start time, e.g. "2019-03-09 09:55:55.0"
    start_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm end time, e.g. "2019-03-09 09:55:55.0"
    alarm_message: Union[EmptyStrToNone, str] = None  # alarm information, e.g. "BYTE110_2"


def _pbd_alarms_data_to_camel(snake: str) -> str:
    override = {
        "device_sn": "pbd_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class PbdAlarmsData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_pbd_alarms_data_to_camel,
    )

    count: int  # Total Records
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "UHD0918003"
    alarms: List[PbdAlarm]


class PbdAlarms(ApiResponse):
    data: Union[EmptyStrToNone, PbdAlarmsData] = None
