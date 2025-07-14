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

from .env_sensor import EnvSensorMetricsOverviewData
from .smart_meter import SmartMeterEnergyOverviewData


# #####################################################################################################################
# Groboost details ####################################################################################################


def _boost_data_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "a_freq": "afreq",
        "a_ipv": "aipv",
        "a_jobs_model": "ajobsModel",
        "a_load_normal_power": "aloadNormalPower",
        "a_max_temp": "amaxTemp",
        "a_min_temp": "aminTemp",
        "a_on_off": "aonOff",
        "a_ppv": "appv",
        "a_set_power": "asetPower",
        "a_start_power": "astartPower",
        "a_temp": "atemp",
        "a_time": "atime",
        "a_total_energy": "atotalEnergy",
        "a_vpv": "avpv",
        "b_freq": "bfreq",
        "b_ipv": "bipv",
        "b_load_normal_power": "bloadNormalPower",
        "b_max_temp": "bmaxTemp",
        "b_min_temp": "bminTemp",
        "b_on_off": "bonOff",
        "b_ppv": "bppv",
        "b_start_power": "bstartPower",
        "b_temp": "btemp",
        "b_time": "btime",
        "b_total_energy": "btotalEnergy",
        "b_vpv": "bvpv",
        "c_freq": "cfreq",
        "c_ipv": "cipv",
        "c_load_normal_power": "cloadNormalPower",
        "c_max_temp": "cmaxTemp",
        "c_min_temp": "cminTemp",
        "c_on_off": "conOff",
        "c_ppv": "cppv",
        "c_start_power": "cstartPower",
        "c_temp": "ctemp",
        "c_time": "ctime",
        "c_total_energy": "ctotalEnergy",
        "c_vpv": "cvpv",
        "datalogger_sn": "datalogger_sn",
        "d_power": "dpower",
        "d_total_energy": "dtotalEnergy",
        "rs485_baudrate": "rs485BaudRate",
        "total_energy": "totalEneny",
    }
    return override.get(snake, to_camel(snake=snake))


class BoostData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_boost_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # address, e.g. 0
    a_freq: Union[EmptyStrToNone, float] = None  # Phase A frequency, e.g. 0
    a_ipv: Union[EmptyStrToNone, float] = None  # A phase current, e.g. 0
    a_jobs_model: Union[EmptyStrToNone, int] = None  # A job mode, e.g. 0
    a_load_normal_power: Union[EmptyStrToNone, float] = None  # A load rated power, e.g. 0
    a_max_temp: Union[EmptyStrToNone, float] = None  # Maximum temperature of channel A, e.g. 0
    a_min_temp: Union[EmptyStrToNone, float] = None  # A minimum temperature, e.g. 0
    a_on_off: Union[EmptyStrToNone, bool] = None  # A time switch, e.g. 0
    a_ppv: Union[EmptyStrToNone, float] = None  # A phase power, e.g. 0
    a_set_power: Union[EmptyStrToNone, float] = None  # A set target power, e.g. 0
    a_start_power: Union[EmptyStrToNone, float] = None  # A start power, e.g. 0
    a_temp: Union[EmptyStrToNone, float] = None  # A road temperature, e.g. 0
    a_time: Union[EmptyStrToNone, str] = None  # A road timing time, e.g. ''
    a_total_energy: Union[EmptyStrToNone, float] = None  # A phase total energy, e.g. 0
    a_vpv: Union[EmptyStrToNone, float] = None  # Phase A voltage, e.g. 0
    b_freq: Union[EmptyStrToNone, float] = None  # Phase B frequency, e.g. 0
    b_ipv: Union[EmptyStrToNone, float] = None  # Phase B current, e.g. 0
    b_load_normal_power: Union[EmptyStrToNone, float] = None  # B load rated power, e.g. 0
    b_max_temp: Union[EmptyStrToNone, float] = None  # B path temperature maximum, e.g. 0
    b_min_temp: Union[EmptyStrToNone, float] = None  # Minimum temperature of channel B, e.g. 0
    b_on_off: Union[EmptyStrToNone, bool] = None  # B road timer switch, e.g. 0
    b_ppv: Union[EmptyStrToNone, float] = None  # B-phase power, e.g. 0
    b_start_power: Union[EmptyStrToNone, float] = None  # B start power, e.g. 0
    b_temp: Union[EmptyStrToNone, float] = None  # B road temperature, e.g. 0
    b_time: Union[EmptyStrToNone, str] = None  # B road timing time, e.g. ''
    b_total_energy: Union[EmptyStrToNone, float] = None  # B-phase total energy, e.g. 0
    b_vpv: Union[EmptyStrToNone, float] = None  # Phase B voltage, e.g. 0
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None  # e.g. {'firstDayOfWeek: 1,...}
    c_freq: Union[EmptyStrToNone, float] = None  # C phase frequency, e.g. 0
    c_ipv: Union[EmptyStrToNone, float] = None  # C phase current, e.g. 0
    c_load_normal_power: Union[EmptyStrToNone, float] = None  # C load rated power, e.g. 0
    c_max_temp: Union[EmptyStrToNone, float] = None  # Maximum temperature of C road, e.g. 0
    c_min_temp: Union[EmptyStrToNone, float] = None  # C road temperature minimum, e.g. 0
    c_on_off: Union[EmptyStrToNone, bool] = None  # C time switch, e.g. 0
    c_ppv: Union[EmptyStrToNone, float] = None  # C phase power, e.g. 0
    c_start_power: Union[EmptyStrToNone, float] = None  # C start power, e.g. 0
    c_temp: Union[EmptyStrToNone, float] = None  # C road temperature, e.g. 0
    c_time: Union[EmptyStrToNone, str] = None  # C road timing time, e.g. ''
    c_total_energy: Union[EmptyStrToNone, float] = None  # C-phase total energy, e.g. 0
    current: Union[EmptyStrToNone, float] = None  # current, e.g. 0
    c_vpv: Union[EmptyStrToNone, float] = None  # C phase voltage, e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'NACTEST128'
    device_type: Union[EmptyStrToNone, str] = None  # Device type, e.g. ''
    d_power: Union[EmptyStrToNone, float] = (
        None  # The total power of phase A under three-phase + single-phase type, e.g. 0
    )
    dry_contact_on_off: Union[EmptyStrToNone, bool] = None  # Dry contact time switch, e.g. 0
    dry_contact_status: Union[EmptyStrToNone, int] = None  # dry contact status, e.g. 0
    dry_contact_time: Union[EmptyStrToNone, str] = None  # Dry contact timing time, e.g. ''
    d_total_energy: Union[EmptyStrToNone, float] = (
        None  # Total energy of phase A under three-phase + single-phase type, e.g. 0
    )
    fw_version: Union[EmptyStrToNone, str] = None  # Hardware version, e.g. ''
    jobs_model: Union[EmptyStrToNone, int] = None  # shineBoost work mode, e.g. 0
    load_device_type: Union[EmptyStrToNone, int] = None  # load device type, e.g. 0
    load_priority: Union[EmptyStrToNone, int] = None  # ABC phase load priority, e.g. 0
    max_temp: Union[EmptyStrToNone, float] = None  # SCR temperature limit, e.g. 0
    min_time: Union[EmptyStrToNone, float] = None  # Minimum working time, e.g. 0
    power: Union[EmptyStrToNone, float] = None  # power, e.g. 0
    power_factor: Union[EmptyStrToNone, float] = None  # Power factor, e.g. 0
    reset_factory: Union[EmptyStrToNone, int] = None  # Restore factory settings, e.g. 0
    restart: Union[EmptyStrToNone, int] = None  # restart, e.g. 0
    rf_command: Union[EmptyStrToNone, str] = None  # RF communication channel, e.g. ''
    rf_pair: Union[EmptyStrToNone, float] = None  # RF pairing, e.g. 0
    rs485_addr: Union[EmptyStrToNone, int] = None  # 485 communication address, e.g. 0
    rs485_baudrate: Union[EmptyStrToNone, int] = None  # 485 baud rate, e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. ''
    status: Union[EmptyStrToNone, int] = None  # ABC phase relay status, e.g. 0
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # Time, e.g. ''
    target_power: Union[EmptyStrToNone, float] = None  # Adjust the target power, e.g. 3600
    temp: Union[EmptyStrToNone, float] = None  # SCR temperature, e.g. 0
    temp_enable: Union[EmptyStrToNone, float] = None  # ABC temperature enable switch, e.g. 0
    temperature: Union[EmptyStrToNone, float] = None  # temperature, e.g. 0
    time_text: Union[EmptyStrToNone, datetime.datetime] = None  # time, e.g. '2021-05-11 15:39:48'
    total_energy: Union[EmptyStrToNone, float] = None  # Total power consumption, e.g. 0
    total_number: Union[EmptyStrToNone, int] = None  # The power adjustment ratio, e.g. 0
    tuning_state: Union[EmptyStrToNone, int] = None  # Power adjustment state, e.g. 0
    v9420_status: Union[EmptyStrToNone, int] = None  # V9420 working status, e.g. 0
    version: Union[EmptyStrToNone, str] = None  # Software version, e.g. '9.1.0.2'
    voltage: Union[EmptyStrToNone, float] = None  # voltage, e.g. 0
    water_heater_power: Union[EmptyStrToNone, float] = None  # Water heater rated power, e.g. 0
    water_state: Union[EmptyStrToNone, int] = None  # Water heater working state, e.g. 0
    with_time: Union[EmptyStrToNone, bool] = None  # Whether to bring time, e.g. False


def _spct_data_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "device_sn": "deviceSN",
    }
    return override.get(snake, to_camel(snake=snake))


class SpctData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spct_data_to_camel,
    )

    active_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    apparent_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None  # e.g. None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. ''
    device_sn: Union[EmptyStrToNone, str] = None  # e.g. ''
    fei_lv_bo_z_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    fei_lv_feng_z_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    fei_lv_gu_z_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    fei_lv_ping_z_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    grid_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    grid_energy_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    install_location: Union[EmptyStrToNone, float] = None  # e.g. 0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. False
    power_factor: Union[EmptyStrToNone, float] = None  # e.g. 0
    reactive_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    time_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    user_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    user_energy_today: Union[EmptyStrToNone, float] = None  # e.g. 0


def _groboost_detail_data_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "meter_ct": "meterCT",
        "parent_id": "parentID",
        "parent_sn": "parentSN",
        "tree_id": "treeID",
    }
    return override.get(snake, to_camel(snake=snake))


class GroboostDetailData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_groboost_detail_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # e.g. 84
    ammeter_data: Union[EmptyStrToNone, SmartMeterEnergyOverviewData] = None  # e.g. {'aActivePower': 0,...}
    boost_data: Union[EmptyStrToNone, BoostData] = None  # e.g. {'addr': 0,...}
    box_data: Union[EmptyStrToNone, Any] = None  # e.g. None
    children: List[Any]  # e.g. []
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Collector serial number, e.g. 'NACTEST128'
    device_name: Union[EmptyStrToNone, str] = None  # Device name, e.g. 'GRO_BOOST'
    device_sn: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. 'GRO2020102'
    device_type: Union[EmptyStrToNone, str] = None  # Device type, e.g. 'WIFI_METER'
    device_type_int: Union[EmptyStrToNone, int] = None  # Meter type, e.g. 69
    env_data: Union[EmptyStrToNone, EnvSensorMetricsOverviewData] = None  # e.g. {'addr': 0,...}
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_green.gif'
    irradiantion: Union[EmptyStrToNone, float] = None  # Insolation, e.g. 0
    jdameter_data: Union[EmptyStrToNone, Any] = None  # e.g. None
    key: Union[EmptyStrToNone, str] = (
        None  # Collector serial number + device type value + address, e.g. 'NACTEST128_69_addr84'
    )
    last_update_time: Union[EmptyStrToNone, GrowattTime] = (
        None  # Last update time, e.g. {'date': 12, 'day': 2, 'hours': 16, 'minutes': 46, 'month': 3, 'seconds': 22, 'time': 1649753182000, 'timezoneOffset': -480, 'year': 122}
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # Last update time, e.g. '2021-05-11 15:33:11'
    )
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    location: Union[EmptyStrToNone, str] = None  # location, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Whether communication is lost, e.g. False
    meter_ct: Union[EmptyStrToNone, int] = None  # CT value of electric meter, dedicated for 645 electric meter, e.g. 0
    parent_id: Union[EmptyStrToNone, str] = (
        None  # Collector serial number + device type value, e.g. 'LIST_NACTEST128_69'
    )
    parent_sn: Union[EmptyStrToNone, str] = None  # Owning superior device SN, e.g. ''
    pid_data: Union[EmptyStrToNone, Any] = None  # e.g. None
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    pr_month: Union[EmptyStrToNone, float] = None  # Monthly Pr value, e.g. 0
    raillog: Union[EmptyStrToNone, bool] = None  # Is it ShineLink (0: Yes 1: No), e.g. 0
    spct_data: Union[EmptyStrToNone, SpctData] = None  # e.g. {'activeEnergy': 0,...}
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # TCP server IP address, e.g. '47.107.154.111'
    timezone: Union[EmptyStrToNone, float] = None  # Time zone, e.g. 0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'OD_NACTEST128_69_addr84'
    tree_name: Union[EmptyStrToNone, str] = None  # Device name + device address, e.g. 'GRO_BOOST#84


class GroboostDetails(ApiResponse):
    data: Union[EmptyStrToNone, GroboostDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Collector serial number, e.g. "NACTEST128"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "GRO2020102"


# #####################################################################################################################
# Groboost metrics overview ###########################################################################################


def _groboost_metrics_overview_to_camel(snake: str) -> str:
    override = {
        "device_sn": "boost_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class GroboostMetricsOverview(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_groboost_metrics_overview_to_camel,
    )

    data: Union[EmptyStrToNone, BoostData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN, e.g. "NACTEST128"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "GRO2020102"


# #####################################################################################################################
# Groboost metrics overview multiple ##################################################################################


class GroboostMetricsOverviewMultipleItem(ApiModel):
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    data: Union[EmptyStrToNone, BoostData] = None


class GroboostMetricsOverviewMultiple(ApiResponse):
    data: List[GroboostMetricsOverviewMultipleItem] = None
    page_num: Union[EmptyStrToNone, int] = None  # Page number, e.g. 1


# #####################################################################################################################
# Groboost metrics history ############################################################################################


def _groboost_metrics_history_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "boost_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class GroboostMetricsHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_groboost_metrics_history_data_to_camel,
    )

    count: int  # Total Records
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "GRO2020102"
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "NACTEST128"
    datas: List[BoostData]


class GroboostMetricsHistory(ApiResponse):
    data: Union[EmptyStrToNone, GroboostMetricsHistoryData] = None
