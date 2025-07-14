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
# Max setting read ####################################################################################################


class MaxSettingRead(ApiResponse):
    data: Union[EmptyStrToNone, str] = None  # current setting / register value


# #####################################################################################################################
# Max setting write ###################################################################################################


class MaxSettingWrite(ApiResponse):
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

    active_rate: Union[EmptyStrToNone, float] = None  # e.g. 0
    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. 'FDCJQ00003'
    backflow_default_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    big_device: Union[EmptyStrToNone, bool] = None  # alias, e.g. False
    children: List[Any]  # e.g. []
    communication_version: Union[EmptyStrToNone, str] = None  # Communication version number, e.g. 'GJAA-0003'
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'VC51030322020001'
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    dtc: Union[EmptyStrToNone, int] = None  # e.g. 5000
    e_today: Union[EmptyStrToNone, float] = None  # Today’s power generation, e.g. 0  # DEPRECATED
    e_total: Union[EmptyStrToNone, float] = None  # Total Power Generation, e.g. 0  # DEPRECATED
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_day_map: Union[EmptyStrToNone, dict] = None  # e.g. {}
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    export_limit: Union[EmptyStrToNone, int] = None  # e.g. 0
    export_limit_power_rate: Union[EmptyStrToNone, float] = None  # e.g. 0
    fac_high: Union[EmptyStrToNone, float] = None  # e.g. 0
    fac_low: Union[EmptyStrToNone, float] = None  # e.g. 0
    frequency_high_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    frequency_low_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'GJ1.0'
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Internal version number, e.g. 'GJAA03xx'
    is_authorize: Union[EmptyStrToNone, bool] = None  # e.g. 0
    is_timing_authorize: Union[EmptyStrToNone, bool] = None  # e.g. 0
    last_update_time: Union[EmptyStrToNone, GrowattTime] = (
        None  # Last update time, e.g. {'date': 12, 'day': 2, 'hours': 16, 'minutes': 46, 'month': 3, 'seconds': 22, 'time': 1649753182000, 'timezoneOffset': -480, 'year': 122}
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-12 16:46:22'
    lcd_language: Union[EmptyStrToNone, int] = None  # e.g. 0
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    location: Union[EmptyStrToNone, str] = None  # address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: disconnected), e.g. True
    max_set_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    model: Union[EmptyStrToNone, int] = None  # model, e.g. 2666130979655057522
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'S25B00D00T00P0FU01M0072'
    normal_power: Union[EmptyStrToNone, int] = None  # e.g. 80000
    on_off: Union[EmptyStrToNone, bool] = None  # e.g. 0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_VC51030322020001_22'
    pf: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep1_pf: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep1_lp: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep2_lp: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep2_pf: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep3_lp: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep3_pf: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep4_lp: Union[EmptyStrToNone, float] = None  # e.g. 0
    pflinep4_pf: Union[EmptyStrToNone, float] = None  # e.g. 0
    pf_model: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'port_name'
    power: Union[EmptyStrToNone, float] = None  # Current power, e.g. 0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. ''
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, bool] = None  # e.g. 0
    reactive_rate: Union[EmptyStrToNone, float] = None  # e.g. 0
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    remain_day: Union[EmptyStrToNone, float] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'FDCJQ00003'
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: waiting, 1: self-check, 3: failure, 4: upgrade, 5, 6, 7, 8: normal mode), e.g. 0
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'tlx.status.operating'
    str_num: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. ''
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. '47.107.154.111'
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_FDCJQ00003'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    vac_high: Union[EmptyStrToNone, float] = None  # e.g. 0
    vac_low: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_high_limit: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_low_limit: Union[EmptyStrToNone, float] = None  # e.g. 0


class MaxDetails(ApiResponse):
    data: Union[EmptyStrToNone, MaxDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the energy storage machine, e.g. "ZT00100001"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Max energy overview #################################################################################################


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
        "device_sn": "serialNum",  # align with other endpoints using "deviceSn" instead
        "str_unbalance": "strUnblance",
        "w_pid_fault_value": "wPIDFaultValue",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxEnergyOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_energy_overview_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    afci_pv1: Union[EmptyStrToNone, int] = None  # e.g. 0
    afci_pv2: Union[EmptyStrToNone, int] = None  # e.g. 0
    afci_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    apf_status: Union[EmptyStrToNone, float] = None  # APF/SVG status, e.g. 0
    apf_status_text: Union[EmptyStrToNone, str] = None  # e.g. 'None'
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    comp_har_ir: Union[EmptyStrToNone, float] = None  # R phase compensation harmonic content, e.g. 0
    comp_har_is: Union[EmptyStrToNone, float] = None  # S phase compensation harmonic content, e.g. 0
    comp_har_it: Union[EmptyStrToNone, float] = None  # T phase compensation harmonic content, e.g. 0
    comp_qr: Union[EmptyStrToNone, float] = None  # R phase compensation reactive power, e.g. 0
    comp_qs: Union[EmptyStrToNone, float] = None  # S phase compensation reactive power, e.g. 0
    comp_qt: Union[EmptyStrToNone, float] = None  # T phase compensation reactive power, e.g. 0
    ct_har_ir: Union[EmptyStrToNone, float] = None  # R phase CT side harmonic content, e.g. 0
    ct_har_is: Union[EmptyStrToNone, float] = None  # S phase CT side harmonic content, e.g. 0
    ct_har_it: Union[EmptyStrToNone, float] = None  # T phase CT side harmonic content, e.g. 0
    ct_ir: Union[EmptyStrToNone, float] = None  # R phase CT side current, e.g. 0
    ct_is: Union[EmptyStrToNone, float] = None  # S phase CT side current, e.g. 0
    ct_it: Union[EmptyStrToNone, float] = None  # T phase CT side current, e.g. 0
    ct_qr: Union[EmptyStrToNone, float] = None  # R phase CT side reactive power, e.g. 0
    ct_qs: Union[EmptyStrToNone, float] = None  # S phase CT side reactive power, e.g. 0
    ct_qt: Union[EmptyStrToNone, float] = None  # T phase CT side electric power, e.g. 0
    current_string1: Union[EmptyStrToNone, float] = None  # String current 1, e.g. 0
    current_string2: Union[EmptyStrToNone, float] = None  # String current 2, e.g. 0
    current_string3: Union[EmptyStrToNone, float] = None  # String current 3, e.g. 0
    current_string4: Union[EmptyStrToNone, float] = None  # String current 4, e.g. 0
    current_string5: Union[EmptyStrToNone, float] = None  # String current 5, e.g. 0
    current_string6: Union[EmptyStrToNone, float] = None  # String current 6, e.g. 0
    current_string7: Union[EmptyStrToNone, float] = None  # String current 7, e.g. 0
    current_string8: Union[EmptyStrToNone, float] = None  # String current 8, e.g. 0
    current_string9: Union[EmptyStrToNone, float] = None  # String current 9, e.g. 0
    current_string10: Union[EmptyStrToNone, float] = None  # String current 10, e.g. 0
    current_string11: Union[EmptyStrToNone, float] = None  # String current 11, e.g. 0
    current_string12: Union[EmptyStrToNone, float] = None  # String current 12, e.g. 0
    current_string13: Union[EmptyStrToNone, float] = None  # String current 13, e.g. 0
    current_string14: Union[EmptyStrToNone, float] = None  # String current 14, e.g. 0
    current_string15: Union[EmptyStrToNone, float] = None  # String current 15, e.g. 0
    current_string16: Union[EmptyStrToNone, float] = None  # String current 16, e.g. 0
    current_string17: Union[EmptyStrToNone, float] = None  # String current n
    current_string18: Union[EmptyStrToNone, float] = None  # String current n
    current_string19: Union[EmptyStrToNone, float] = None  # String current n
    current_string20: Union[EmptyStrToNone, float] = None  # String current n
    current_string21: Union[EmptyStrToNone, float] = None  # String current n
    current_string22: Union[EmptyStrToNone, float] = None  # String current n
    current_string23: Union[EmptyStrToNone, float] = None  # String current n
    current_string24: Union[EmptyStrToNone, float] = None  # String current n
    current_string25: Union[EmptyStrToNone, float] = None  # String current n
    current_string26: Union[EmptyStrToNone, float] = None  # String current n
    current_string27: Union[EmptyStrToNone, float] = None  # String current n
    current_string28: Union[EmptyStrToNone, float] = None  # String current n
    current_string29: Union[EmptyStrToNone, float] = None  # String current n
    current_string30: Union[EmptyStrToNone, float] = None  # String current n
    current_string31: Union[EmptyStrToNone, float] = None  # String current n
    current_string32: Union[EmptyStrToNone, float] = None  # String current n
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'QMN0000000000000'
    day: Union[EmptyStrToNone, str] = None  # e.g. ''
    debug1: Union[EmptyStrToNone, str] = None  # e.g. '160, 0, 0, 0, 324, 0, 0, 0'
    debug2: Union[EmptyStrToNone, str] = None  # e.g. '0,0,0,0,0,0,0,0'
    debug3: Union[EmptyStrToNone, str] = None  # e.g. '0,0,0,0,0,0,0,0'
    derating_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    dw_string_warning_value1: Union[EmptyStrToNone, int] = None  # e.g. 0
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
    epv9_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv9_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv10_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv10_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv11_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv11_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv12_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv12_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv13_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv13_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv14_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv14_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv15_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv15_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv16_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv16_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_rac_today: Union[EmptyStrToNone, float] = None  # Reactive power of the day kWh, e.g. 0
    e_rac_total: Union[EmptyStrToNone, float] = None  # Total reactive power kWh, e.g. 0
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 50.0099983215332
    fault_code1: Union[EmptyStrToNone, int] = None  # e.g. 2
    fault_code2: Union[EmptyStrToNone, int] = None  # e.g. 0
    fault_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    fault_value: Union[EmptyStrToNone, int] = None  # e.g. 3
    gfci: Union[EmptyStrToNone, float] = None  # e.g. 78
    iacr: Union[EmptyStrToNone, float] = None  # e.g. 0
    iacs: Union[EmptyStrToNone, float] = None  # e.g. 0
    iact: Union[EmptyStrToNone, float] = None  # e.g. 0
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    i_pid_pvape: Union[EmptyStrToNone, float] = None  # pid current 1 (A), e.g. 0
    i_pid_pvbpe: Union[EmptyStrToNone, float] = None  # pid current 2 (A), e.g. 0
    i_pid_pvcpe: Union[EmptyStrToNone, float] = None  # pid current 3 (A), e.g. 0
    i_pid_pvdpe: Union[EmptyStrToNone, float] = None  # pid current 4 (A), e.g. 0
    i_pid_pvepe: Union[EmptyStrToNone, float] = None  # pid current 5 (A), e.g. 0
    i_pid_pvfpe: Union[EmptyStrToNone, float] = None  # pid current 6 (A), e.g. 0
    i_pid_pvgpe: Union[EmptyStrToNone, float] = None  # pid current 7 (A), e.g. 0
    i_pid_pvhpe: Union[EmptyStrToNone, float] = None  # pid current 8 (A), e.g. 0
    i_pid_pvpe9: Union[EmptyStrToNone, float] = None  # pid current 9 (A), e.g. 0
    i_pid_pvpe10: Union[EmptyStrToNone, float] = None  # pid current 10 (A), e.g. 0
    i_pid_pvpe11: Union[EmptyStrToNone, float] = None  # pid current 11 (A), e.g. 0
    i_pid_pvpe12: Union[EmptyStrToNone, float] = None  # pid current 12 (A), e.g. 0
    i_pid_pvpe13: Union[EmptyStrToNone, float] = None  # pid current 13 (A), e.g. 0
    i_pid_pvpe14: Union[EmptyStrToNone, float] = None  # pid current 14 (A), e.g. 0
    i_pid_pvpe15: Union[EmptyStrToNone, float] = None  # pid current 15 (A), e.g. 0
    i_pid_pvpe16: Union[EmptyStrToNone, float] = None  # pid current 16 (A), e.g. 0
    ipm_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv1: Union[EmptyStrToNone, float] = None  # PV1 input current, e.g. 5.800000190734863
    ipv2: Union[EmptyStrToNone, float] = None  # PV2 input current, e.g. 6.099999904632568
    ipv3: Union[EmptyStrToNone, float] = None  # PV3 input current, e.g. 0
    ipv4: Union[EmptyStrToNone, float] = None
    ipv5: Union[EmptyStrToNone, float] = None
    ipv6: Union[EmptyStrToNone, float] = None
    ipv7: Union[EmptyStrToNone, float] = None
    ipv8: Union[EmptyStrToNone, float] = None
    ipv9: Union[EmptyStrToNone, float] = None
    ipv10: Union[EmptyStrToNone, float] = None
    ipv11: Union[EmptyStrToNone, float] = None
    ipv12: Union[EmptyStrToNone, float] = None
    ipv13: Union[EmptyStrToNone, float] = None
    ipv14: Union[EmptyStrToNone, float] = None
    ipv15: Union[EmptyStrToNone, float] = None
    ipv16: Union[EmptyStrToNone, float] = None
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    max_bean: Union[EmptyStrToNone, Any] = None
    n_bus_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    op_fullwatt: Union[EmptyStrToNone, float] = None  # e.g. 0
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 2503.8
    pacr: Union[EmptyStrToNone, float] = None  # e.g. 0
    pacs: Union[EmptyStrToNone, float] = None  # e.g. 0
    pact: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_bus_voltage: Union[EmptyStrToNone, float] = None  # e.g. 367
    pf: Union[EmptyStrToNone, float] = None  # e.g. 0.08100000023841858
    pid_bus: Union[EmptyStrToNone, float] = None
    pid_fault_code: Union[EmptyStrToNone, int] = None
    pid_status: Union[EmptyStrToNone, int] = None
    pid_status_text: Union[EmptyStrToNone, str] = None
    power_today: Union[EmptyStrToNone, float] = None
    power_total: Union[EmptyStrToNone, float] = None
    ppv: Union[EmptyStrToNone, float] = None  # PV input power, e.g. 1058
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power, e.g. 1058
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power, e.g. 1058
    ppv3: Union[EmptyStrToNone, float] = None  # PV3 input power, e.g. 0
    ppv4: Union[EmptyStrToNone, float] = None  # PV4 input power, e.g. 0
    ppv5: Union[EmptyStrToNone, float] = None
    ppv6: Union[EmptyStrToNone, float] = None
    ppv7: Union[EmptyStrToNone, float] = None
    ppv8: Union[EmptyStrToNone, float] = None
    ppv9: Union[EmptyStrToNone, float] = None
    ppv10: Union[EmptyStrToNone, float] = None
    ppv11: Union[EmptyStrToNone, float] = None
    ppv12: Union[EmptyStrToNone, float] = None
    ppv13: Union[EmptyStrToNone, float] = None
    ppv14: Union[EmptyStrToNone, float] = None
    ppv15: Union[EmptyStrToNone, float] = None
    ppv16: Union[EmptyStrToNone, float] = None
    pv_iso: Union[EmptyStrToNone, float] = None  # Insulation resistance
    rac: Union[EmptyStrToNone, float] = None  # Reactive power W
    r_dci: Union[EmptyStrToNone, float] = None  # R-phase DC component
    react_power: Union[EmptyStrToNone, float] = None
    react_power_max: Union[EmptyStrToNone, float] = None
    react_power_total: Union[EmptyStrToNone, float] = None
    real_op_percent: Union[EmptyStrToNone, float] = None  # e.g. 50
    s_dci: Union[EmptyStrToNone, float] = None  # S-phase DC component
    device_sn: Union[EmptyStrToNone, str] = None  # e.g. 'BNE9A5100D'
    status: Union[EmptyStrToNone, int] = None  # Max status (0: Standby, 1: , 2: Discharge, 3: Fault, 4: Flash), e.g. 1
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Normal'
    str_break: Union[EmptyStrToNone, int] = None  # The string is not connected
    str_fault: Union[EmptyStrToNone, int] = None  # String error
    str_unbalance: Union[EmptyStrToNone, int] = None  # Uneven string flow
    str_unmatch: Union[EmptyStrToNone, int] = None  # The string does not match
    t_dci: Union[EmptyStrToNone, float] = None  # T-phase DC component, e.g. 0
    temperature: Union[EmptyStrToNone, float] = None  # AMTemp1(°C), e.g. 47.79999923706055
    temperature2: Union[EmptyStrToNone, float] = None  # INVTemp(°C), e.g. 0
    temperature3: Union[EmptyStrToNone, float] = None  # BTTemp(°C), e.g. 0
    temperature4: Union[EmptyStrToNone, float] = None  # OUTTemp(°C), e.g. 0
    temperature5: Union[EmptyStrToNone, float] = None  # AMTemp2(°C), e.g. 51.70000076293945
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-09 14:52:39'
    time_calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    time_total: Union[EmptyStrToNone, float] = None  # Total running time, e.g. 1625146.9
    vacr: Union[EmptyStrToNone, float] = None  # R phase voltage (V), e.g. 239.5
    vac_rs: Union[EmptyStrToNone, float] = None  # RS line voltage, e.g. 239.5
    vacs: Union[EmptyStrToNone, float] = None  # S phase voltage (V), e.g. 239.5
    vac_st: Union[EmptyStrToNone, float] = None  # ST line voltage, e.g. 0
    vact: Union[EmptyStrToNone, float] = None  # T phase voltage (V), e.g. 239.5
    vac_tr: Union[EmptyStrToNone, float] = None  # TR line voltage, e.g. 0
    v_pid_pvape: Union[EmptyStrToNone, float] = None  # pid voltage 1 (V), e.g. 239.5
    v_pid_pvbpe: Union[EmptyStrToNone, float] = None
    v_pid_pvcpe: Union[EmptyStrToNone, float] = None
    v_pid_pvdpe: Union[EmptyStrToNone, float] = None
    v_pid_pvepe: Union[EmptyStrToNone, float] = None
    v_pid_pvfpe: Union[EmptyStrToNone, float] = None
    v_pid_pvgpe: Union[EmptyStrToNone, float] = None
    v_pid_pvhpe: Union[EmptyStrToNone, float] = None
    v_pid_pvpe9: Union[EmptyStrToNone, float] = None
    v_pid_pvpe10: Union[EmptyStrToNone, float] = None
    v_pid_pvpe11: Union[EmptyStrToNone, float] = None
    v_pid_pvpe12: Union[EmptyStrToNone, float] = None
    v_pid_pvpe13: Union[EmptyStrToNone, float] = None
    v_pid_pvpe14: Union[EmptyStrToNone, float] = None
    v_pid_pvpe15: Union[EmptyStrToNone, float] = None
    v_pid_pvpe16: Union[EmptyStrToNone, float] = None
    vpv1: Union[EmptyStrToNone, float] = None  # PV1 input voltage, e.g. 0
    vpv2: Union[EmptyStrToNone, float] = None
    vpv3: Union[EmptyStrToNone, float] = None
    vpv4: Union[EmptyStrToNone, float] = None
    vpv5: Union[EmptyStrToNone, float] = None
    vpv6: Union[EmptyStrToNone, float] = None
    vpv7: Union[EmptyStrToNone, float] = None
    vpv8: Union[EmptyStrToNone, float] = None
    vpv9: Union[EmptyStrToNone, float] = None
    vpv10: Union[EmptyStrToNone, float] = None
    vpv11: Union[EmptyStrToNone, float] = None
    vpv12: Union[EmptyStrToNone, float] = None
    vpv13: Union[EmptyStrToNone, float] = None
    vpv14: Union[EmptyStrToNone, float] = None
    vpv15: Union[EmptyStrToNone, float] = None
    vpv16: Union[EmptyStrToNone, float] = None
    v_string1: Union[EmptyStrToNone, float] = None
    v_string2: Union[EmptyStrToNone, float] = None
    v_string3: Union[EmptyStrToNone, float] = None
    v_string4: Union[EmptyStrToNone, float] = None
    v_string5: Union[EmptyStrToNone, float] = None
    v_string6: Union[EmptyStrToNone, float] = None
    v_string7: Union[EmptyStrToNone, float] = None
    v_string8: Union[EmptyStrToNone, float] = None
    v_string9: Union[EmptyStrToNone, float] = None
    v_string10: Union[EmptyStrToNone, float] = None
    v_string11: Union[EmptyStrToNone, float] = None
    v_string12: Union[EmptyStrToNone, float] = None
    v_string13: Union[EmptyStrToNone, float] = None
    v_string14: Union[EmptyStrToNone, float] = None
    v_string15: Union[EmptyStrToNone, float] = None
    v_string16: Union[EmptyStrToNone, float] = None
    v_string17: Union[EmptyStrToNone, float] = None
    v_string18: Union[EmptyStrToNone, float] = None
    v_string19: Union[EmptyStrToNone, float] = None
    v_string20: Union[EmptyStrToNone, float] = None
    v_string21: Union[EmptyStrToNone, float] = None
    v_string22: Union[EmptyStrToNone, float] = None
    v_string23: Union[EmptyStrToNone, float] = None
    v_string24: Union[EmptyStrToNone, float] = None
    v_string25: Union[EmptyStrToNone, float] = None
    v_string26: Union[EmptyStrToNone, float] = None
    v_string27: Union[EmptyStrToNone, float] = None
    v_string28: Union[EmptyStrToNone, float] = None
    v_string29: Union[EmptyStrToNone, float] = None
    v_string30: Union[EmptyStrToNone, float] = None
    v_string31: Union[EmptyStrToNone, float] = None
    v_string32: Union[EmptyStrToNone, float] = None
    warn_bit: Union[EmptyStrToNone, int] = None
    warn_code: Union[EmptyStrToNone, int] = None  # e.g. 220
    warning_value1: Union[EmptyStrToNone, int] = None
    warning_value2: Union[EmptyStrToNone, int] = None
    warning_value3: Union[EmptyStrToNone, int] = None
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the data sent has its own time, e.g. False
    w_pid_fault_value: Union[EmptyStrToNone, int] = None
    w_string_status_value: Union[EmptyStrToNone, int] = None


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

    data: Union[EmptyStrToNone, MaxEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Max energy overview multiple ########################################################################################


class MaxEnergyOverviewMultipleItem(ApiModel):
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    data: Union[EmptyStrToNone, MaxEnergyOverviewData] = None


class MaxEnergyOverviewMultiple(ApiResponse):
    data: List[MaxEnergyOverviewMultipleItem] = None
    page_num: Union[EmptyStrToNone, int] = None  # Page number, e.g. 1


# #####################################################################################################################
# Max energy history ##################################################################################################


def _max_energy_history_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "max_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class MaxEnergyHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_max_energy_history_data_to_camel,
    )

    count: int  # Total Records
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. ""SATA818009""
    datas: List[MaxEnergyOverviewData]
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. ""TLMAX00B01""
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21


class MaxEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, MaxEnergyHistoryData] = None


# #####################################################################################################################
# Max alarms ##########################################################################################################


class MaxAlarm(ApiModel):
    alarm_code: Union[EmptyStrToNone, int] = None  # alarm code, e.g. 25
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    end_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm start time, e.g. "2019-03-09 09:55:55.0"
    start_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm end time, e.g. "2019-03-09 09:55:55.0"
    alarm_message: Union[EmptyStrToNone, str] = None  # alarm information, e.g. "No utility."


def _max_alarms_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "max_sn",
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
