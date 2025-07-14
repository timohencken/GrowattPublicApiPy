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
# Inverter setting read ###############################################################################################


class InverterSettingRead(ApiResponse):
    data: Union[EmptyStrToNone, str] = None  # current setting / register value


# #####################################################################################################################
# Inverter setting write ##############################################################################################


class InverterSettingWrite(ApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# #####################################################################################################################
# Inverter details ####################################################################################################


def _inverter_detail_data_to_camel(snake: str) -> str:
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


class InverterDetailData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_inverter_detail_data_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. "ZT00100001"
    big_device: Union[EmptyStrToNone, bool] = None  # e.g. false
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    communication_version: Union[EmptyStrToNone, str] = None  # Communication version number, e.g. ''
    create_date: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. null
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. "CRAZT00001"
    device_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_day_map: Union[EmptyStrToNone, dict] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. "0"
    e_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. "G.2.0"
    group_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    id: Union[EmptyStrToNone, int] = None  # e.g. 116
    img_path: Union[EmptyStrToNone, str] = None  # e.g. "./css/img/status_green.gif"
    inner_version: Union[EmptyStrToNone, str] = None  # e.g. "1.2.3.4."
    inv_set_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    inverter_info_status_css: Union[EmptyStrToNone, str] = None  # e.g. "vsts_table_green"
    ipm_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0
    last_update_time: Union[EmptyStrToNone, GrowattTime] = None  # Last update time, e.g. {"time": 1547000577000, ...}
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. "2019-01-09 10:22:57"
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    load_text: Union[EmptyStrToNone, str] = None  # e.g. "0%"
    location: Union[EmptyStrToNone, str] = None  # Address, e.g. ""
    lost: Union[EmptyStrToNone, bool] = (
        None  # whether the device is online or not (0: online, 1: disconnected), e.g. false
    )
    model: Union[EmptyStrToNone, int] = None  # e.g. 61748
    model_text: Union[EmptyStrToNone, str] = None  # e.g. "A0B0D0T0PFU1M3S4"
    nominal_power: Union[EmptyStrToNone, int] = None  # nominal power, e.g. 20000
    optimizer_list: Union[EmptyStrToNone, Any] = None  # e.g. None
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. "LIST_CRAZT00001_0"
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. ""
    power: Union[EmptyStrToNone, float] = None  # e.g. 0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. ""
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ""
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. ""
    record: Union[EmptyStrToNone, str] = None  # e.g. null
    rf_stick: Union[EmptyStrToNone, str] = None  # e.g. null
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "ZT00100001"
    status: Union[EmptyStrToNone, int] = None  # Device status, status (0: waiting, 1: normal, 3: failure), e.g. 1
    status_text: Union[EmptyStrToNone, str] = None  # e.g. "inverter.status.normal"
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. "127.0.0.1"
    temperature: Union[EmptyStrToNone, float] = None  # e.g. 0
    timezone: Union[EmptyStrToNone, float] = None  # e.g. 8.0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. "ZT00100001"
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. "ZT00100001"
    update_exist: Union[EmptyStrToNone, bool] = None  # e.g. false
    updating: Union[EmptyStrToNone, bool] = None  # e.g. false
    user_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ""


class InverterDetails(ApiResponse):
    data: Union[EmptyStrToNone, InverterDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Inverter energy overview ############################################################################################


def _inverter_energy_overview_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "inverterId",  # align with other endpoints using "deviceSn" instead
        "real_op_percent": "realOPPercent",
        "w_pid_fault_value": "wPIDFaultValue",
    }
    return override.get(snake, to_camel(snake=snake))


class InverterEnergyOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_inverter_energy_overview_data_to_camel,
    )

    again: Union[EmptyStrToNone, bool] = None  # e.g. false
    apf_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    big_device: Union[EmptyStrToNone, bool] = None  # e.g. false
    compharir: Union[EmptyStrToNone, float] = None  # e.g. 0
    compharis: Union[EmptyStrToNone, float] = None  # e.g. 0
    compharit: Union[EmptyStrToNone, float] = None  # e.g. 0
    compqr: Union[EmptyStrToNone, float] = None  # e.g. 0
    compqs: Union[EmptyStrToNone, float] = None  # e.g. 0
    compqt: Union[EmptyStrToNone, float] = None  # e.g. 0
    ctharir: Union[EmptyStrToNone, float] = None  # e.g. 0
    ctharis: Union[EmptyStrToNone, float] = None  # e.g. 0
    ctharit: Union[EmptyStrToNone, float] = None  # e.g. 0
    ctir: Union[EmptyStrToNone, float] = None  # e.g. 0
    ctis: Union[EmptyStrToNone, float] = None  # e.g. 0
    ctit: Union[EmptyStrToNone, float] = None  # e.g. 0
    ctqr: Union[EmptyStrToNone, float] = None  # e.g. 0
    ctqs: Union[EmptyStrToNone, float] = None  # e.g. 0
    ctqt: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string1: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string2: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string3: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string4: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string5: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string6: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string7: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string8: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string9: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string10: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string11: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string12: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string13: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string14: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string15: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string16: Union[EmptyStrToNone, float] = None  # e.g. 0
    debug1: Union[EmptyStrToNone, str] = None  # e.g. ""
    debug2: Union[EmptyStrToNone, str] = None  # e.g. ""
    derating_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    dw_string_warning_value1: Union[EmptyStrToNone, int] = None  # e.g. 0
    epv1_today: Union[EmptyStrToNone, float] = None  # e.g. 6
    epv1_total: Union[EmptyStrToNone, float] = None  # e.g. 60
    epv2_today: Union[EmptyStrToNone, float] = None  # e.g. 6
    epv2_total: Union[EmptyStrToNone, float] = None  # e.g. 60
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
    epv_total: Union[EmptyStrToNone, float] = None  # e.g. 120
    e_rac_today: Union[EmptyStrToNone, float] = None  # e.g. 11
    e_rac_total: Union[EmptyStrToNone, float] = None  # e.g. 110
    fac: Union[EmptyStrToNone, float] = None  # e.g. 50
    fault_code1: Union[EmptyStrToNone, int] = None  # e.g. 0
    fault_code2: Union[EmptyStrToNone, int] = None  # e.g. 0
    fault_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    fault_value: Union[EmptyStrToNone, int] = None  # e.g. 0
    gfci: Union[EmptyStrToNone, int] = None  # e.g. 0
    iacr: Union[EmptyStrToNone, float] = None  # e.g. 12
    iacs: Union[EmptyStrToNone, float] = None  # e.g. 12
    iact: Union[EmptyStrToNone, float] = None  # e.g. 12
    id: Union[EmptyStrToNone, int] = None  # e.g. 90180
    device_sn: Union[EmptyStrToNone, str] = None  # e.g. "ZT00100001"
    i_pid_pvape: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_pid_pvbpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_pid_pvcpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_pid_pvdpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_pid_pvepe: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_pid_pvfpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_pid_pvgpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    i_pid_pvhpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipm_temperature: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv1: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv2: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv3: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv4: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv5: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv6: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv7: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv8: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv9: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv10: Union[EmptyStrToNone, float] = None  # e.g. 0
    n_bus_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    op_fullwatt: Union[EmptyStrToNone, float] = None  # e.g. 0
    pac: Union[EmptyStrToNone, float] = None  # e.g. 8912.400390625
    pacr: Union[EmptyStrToNone, float] = None  # e.g. 2760
    pacs: Union[EmptyStrToNone, float] = None  # e.g. 2760
    pact: Union[EmptyStrToNone, float] = None  # e.g. 2760
    p_bus_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    pf: Union[EmptyStrToNone, float] = None  # e.g. -1
    pid_bus: Union[EmptyStrToNone, float] = None  # e.g. 0
    pid_fault_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    pid_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    power_today: Union[EmptyStrToNone, float] = None  # e.g. 7.599999904632568
    power_total: Union[EmptyStrToNone, float] = None  # e.g. 7.6
    ppv: Union[EmptyStrToNone, float] = None  # e.g. 9981.7998046875
    ppv1: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv2: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv3: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv4: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv5: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv6: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv7: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv8: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv9: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv10: Union[EmptyStrToNone, float] = None  # e.g. 0
    pv_iso: Union[EmptyStrToNone, float] = None  # e.g. 0
    rac: Union[EmptyStrToNone, float] = None  # e.g. 6553.5
    r_dci: Union[EmptyStrToNone, float] = None  # e.g. 0
    real_op_percent: Union[EmptyStrToNone, float] = None  # e.g. 0
    s_dci: Union[EmptyStrToNone, float] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    status_text: Union[EmptyStrToNone, str] = None  # e.g. "Normal"
    str_break: Union[EmptyStrToNone, float] = None  # e.g. 0
    str_fault: Union[EmptyStrToNone, float] = None  # e.g. 0
    str_unblance: Union[EmptyStrToNone, float] = None  # e.g. 0
    str_unmatch: Union[EmptyStrToNone, float] = None  # e.g. 0
    t_dci: Union[EmptyStrToNone, float] = None  # e.g. 0
    temperature: Union[EmptyStrToNone, float] = None  # e.g. 75
    temperature2: Union[EmptyStrToNone, float] = None  # e.g. 0
    temperature3: Union[EmptyStrToNone, float] = None  # e.g. 0
    temperature4: Union[EmptyStrToNone, float] = None  # e.g. 0
    temperature5: Union[EmptyStrToNone, float] = None  # e.g. 0
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. "2018-12-13 11:03:52"
    time_calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    time_total: Union[EmptyStrToNone, float] = None  # e.g. 1.0833333333333333
    time_total_text: Union[EmptyStrToNone, str] = None  # e.g. "1.1"
    vacr: Union[EmptyStrToNone, float] = None  # e.g. 220
    vac_rs: Union[EmptyStrToNone, float] = None  # e.g. 0
    vacs: Union[EmptyStrToNone, float] = None  # e.g. 220
    vac_st: Union[EmptyStrToNone, float] = None  # e.g. 0
    vact: Union[EmptyStrToNone, float] = None  # e.g. 220
    vac_tr: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_pid_pvape: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_pid_pvbpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_pid_pvcpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_pid_pvdpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_pid_pvepe: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_pid_pvfpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_pid_pvgpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_pid_pvhpe: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpv1: Union[EmptyStrToNone, float] = None  # e.g. 248
    vpv2: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpv3: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpv4: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpv5: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpv6: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpv7: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpv8: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpv9: Union[EmptyStrToNone, float] = None  # e.g. 0
    vpv10: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string1: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string2: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string3: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string4: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string5: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string6: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string7: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string8: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string9: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string10: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string11: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string12: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string13: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string14: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string15: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string16: Union[EmptyStrToNone, float] = None  # e.g. 0
    warn_bit: Union[EmptyStrToNone, int] = None  # e.g. 0
    warn_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    warning_value1: Union[EmptyStrToNone, int] = None  # e.g. 0
    warning_value2: Union[EmptyStrToNone, int] = None  # e.g. 0
    warning_value3: Union[EmptyStrToNone, int] = None  # e.g. 0
    w_pid_fault_value: Union[EmptyStrToNone, int] = None  # e.g. 0
    w_string_status_value: Union[EmptyStrToNone, int] = None  # e.g. 0


class InverterEnergyOverview(ApiResponse):
    data: Union[EmptyStrToNone, InverterEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Inverter energy overview multiple ###################################################################################


class InverterEnergyOverviewMultipleItem(ApiModel):
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    data: Union[EmptyStrToNone, InverterEnergyOverviewData] = None


class InverterEnergyOverviewMultiple(ApiResponse):
    data: List[InverterEnergyOverviewMultipleItem] = None
    page_num: Union[EmptyStrToNone, int] = None  # Page number, e.g. 1


# #####################################################################################################################
# Inverter energy history #############################################################################################


class InverterEnergyHistoryDataItem(ApiModel):
    current_string1: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string2: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string3: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string4: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string5: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string6: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string7: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string8: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string9: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string10: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string11: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string12: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string13: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string14: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string15: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_string16: Union[EmptyStrToNone, float] = None  # e.g. 0
    fac: Union[EmptyStrToNone, float] = None  # Frequency (Hz), e.g. 50
    iac1: Union[EmptyStrToNone, float] = None  # Output current 1 (A), e.g. 12
    iac2: Union[EmptyStrToNone, float] = None  # Output current 2 (A), e.g. 12
    iac3: Union[EmptyStrToNone, float] = None  # Output current 3 (A), e.g. 12
    ipv1: Union[EmptyStrToNone, float] = None  # Input current 1 (A), e.g. 0
    ipv2: Union[EmptyStrToNone, float] = None  # Input current 2 (A), e.g. 0
    ipv3: Union[EmptyStrToNone, float] = None  # Input current 3 (A), e.g. 0
    ipv4: Union[EmptyStrToNone, float] = None  # Input current 3 (A), e.g. 0
    ipv5: Union[EmptyStrToNone, float] = None  # Input current 3 (A), e.g. 0
    ipv6: Union[EmptyStrToNone, float] = None  # Input current 3 (A), e.g. 0
    ipv7: Union[EmptyStrToNone, float] = None  # Input current 3 (A), e.g. 0
    ipv8: Union[EmptyStrToNone, float] = None  # Input current 3 (A), e.g. 0
    ipv9: Union[EmptyStrToNone, float] = None  # Input current 3 (A), e.g. 0
    ipv10: Union[EmptyStrToNone, float] = None  # Input current 3 (A), e.g. 0
    power: Union[EmptyStrToNone, float] = None  # Output power (W), e.g. 8912.400390625
    power_factor: Union[EmptyStrToNone, float] = None  # Power factor, e.g. -1
    ppv: Union[EmptyStrToNone, float] = None  # e.g. 9981.7998046875
    ppv1: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv2: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv3: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv4: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv5: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv6: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv7: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv8: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv9: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv10: Union[EmptyStrToNone, float] = None  # e.g. 0
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    temperature: Union[EmptyStrToNone, float] = None  # temperature (°C), e.g. 75
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. "2018-12-13 11:03:52"
    today_energy: Union[EmptyStrToNone, float] = None  # Today's power generation (kWh), e.g. "7.6"
    total_energy: Union[EmptyStrToNone, float] = None  # Total power generation (kWh), e.g. "7.6"
    vac1: Union[EmptyStrToNone, float] = None  # Output voltage 1 (V), e.g. 220
    vac2: Union[EmptyStrToNone, float] = None  # Output voltage 2 (V), e.g. 220
    vac3: Union[EmptyStrToNone, float] = None  # Output voltage 3 (V), e.g. 220
    vpv1: Union[EmptyStrToNone, float] = None  # Input voltage 1 (V), e.g. 248
    vpv2: Union[EmptyStrToNone, float] = None  # Input voltage 2 (V), e.g. 0
    vpv3: Union[EmptyStrToNone, float] = None  # Input voltage 3 (V), e.g. 0
    vpv4: Union[EmptyStrToNone, float] = None  # Input voltage 3 (V), e.g. 0
    vpv5: Union[EmptyStrToNone, float] = None  # Input voltage 3 (V), e.g. 0
    vpv6: Union[EmptyStrToNone, float] = None  # Input voltage 3 (V), e.g. 0
    vpv7: Union[EmptyStrToNone, float] = None  # Input voltage 3 (V), e.g. 0
    vpv8: Union[EmptyStrToNone, float] = None  # Input voltage 3 (V), e.g. 0
    vpv9: Union[EmptyStrToNone, float] = None  # Input voltage 3 (V), e.g. 0
    vpv10: Union[EmptyStrToNone, float] = None  # Input voltage 3 (V), e.g. 0
    v_string1: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string2: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string3: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string4: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string5: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string6: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string7: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string8: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string9: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string10: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string11: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string12: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string13: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string14: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string15: Union[EmptyStrToNone, float] = None  # e.g. 0
    v_string16: Union[EmptyStrToNone, float] = None  # e.g. 0


def _inverter_energy_history_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "sn",
    }
    return override.get(snake, to_camel(snake=snake))


class InverterEnergyHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_inverter_energy_history_data_to_camel,
    )

    count: Union[EmptyStrToNone, int] = None  # Total Records
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    datas: List[InverterEnergyHistoryDataItem]
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


class InverterEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, InverterEnergyHistoryData] = None


# #####################################################################################################################
# Inverter alarms #####################################################################################################


class InverterAlarm(ApiModel):
    alarm_code: Union[EmptyStrToNone, int] = None  # alarm code, e.g. 25
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    end_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm start time, e.g. "2019-03-09 09:55:55.0"
    start_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm end time, e.g. "2019-03-09 09:55:55.0"
    alarm_message: Union[EmptyStrToNone, str] = None  # alarm information, e.g. "No utility."


def _inverter_alarms_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "sn",
    }
    return override.get(snake, to_camel(snake=snake))


class InverterAlarmsData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_inverter_alarms_data_to_camel,
    )

    count: int  # Total Records
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    alarms: List[InverterAlarm]


class InverterAlarms(ApiResponse):
    data: Union[EmptyStrToNone, InverterAlarmsData] = None
