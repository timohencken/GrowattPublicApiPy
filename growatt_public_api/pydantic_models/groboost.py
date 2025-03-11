import datetime
from typing import Union, Any, List, Optional, TypeAlias

from pydantic import (
    ConfigDict,
    BeforeValidator,
)
from pydantic.alias_generators import to_camel

from growatt_public_api.pydantic_models.api_model import (
    ApiResponse,
    EmptyStrToNone,
    GrowattTime,
    ApiModel,
)

from typing import Annotated

from pydantic_models.env_sensor import EnvSensorMetricsOverviewData
from pydantic_models.smart_meter import SmartMeterEnergyOverviewData


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


def _growatt_time_calendar_timezone_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "dst_savings": "DSTSavings",
        "id": "ID",
    }
    return override.get(snake, to_camel(snake=snake))


class GrowattTimeCalendarTimeZone(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_growatt_time_calendar_timezone_to_camel,
    )

    dirty: Union[EmptyStrToNone, bool] = None  # e.g. false
    display_name: Union[EmptyStrToNone, str] = None  # e.g. "China Standard Time"
    dst_savings: Union[EmptyStrToNone, int] = None  # e.g. 0
    id: Union[EmptyStrToNone, str] = None  # e.g. "Asia/Shanghai"
    last_rule_instance: Union[EmptyStrToNone, str] = None  # e.g. null
    raw_offset: Union[EmptyStrToNone, int] = None  # e.g. 28800000


class GrowattTimeCalendar(ApiModel):
    minimal_days_in_first_week: Union[EmptyStrToNone, int] = None  # e.g. 1
    week_year: Union[EmptyStrToNone, int] = None  # e.g. 2018
    time: Union[EmptyStrToNone, GrowattTime] = None
    weeks_in_week_year: Union[EmptyStrToNone, int] = None  # e.g. 52
    gregorian_change: Union[EmptyStrToNone, GrowattTime] = None
    time_zone: Union[EmptyStrToNone, GrowattTimeCalendarTimeZone] = None
    time_in_millis: Union[EmptyStrToNone, int] = None  # e.g. 1544670232000
    lenient: Union[EmptyStrToNone, bool] = None  # e.g. true
    first_day_of_week: Union[EmptyStrToNone, int] = None  # e.g. 1
    week_date_supported: Union[EmptyStrToNone, bool] = None


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

    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    a_freq: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_ipv: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_jobs_model: Union[EmptyStrToNone, int] = None  # e.g. 0
    a_load_normal_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_max_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_min_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_on_off: Union[EmptyStrToNone, bool] = None  # e.g. 0
    a_ppv: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_set_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_start_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    a_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_vpv: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_freq: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_ipv: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_load_normal_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_max_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_min_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_on_off: Union[EmptyStrToNone, bool] = None  # e.g. 0
    b_ppv: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_start_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    b_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_vpv: Union[EmptyStrToNone, float] = None  # e.g. 0
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = (
        None  # e.g. {'firstDayOfWeek: 1,...}
    )
    c_freq: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_ipv: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_load_normal_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_max_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_min_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_on_off: Union[EmptyStrToNone, bool] = None  # e.g. 0
    c_ppv: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_start_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    c_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    current: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_vpv: Union[EmptyStrToNone, float] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. ''
    device_type: Union[EmptyStrToNone, str] = None  # e.g. ''
    d_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    dry_contact_on_off: Union[EmptyStrToNone, bool] = None  # e.g. 0
    dry_contact_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    dry_contact_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    d_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    fw_version: Union[EmptyStrToNone, str] = None  # e.g. ''
    jobs_model: Union[EmptyStrToNone, int] = None  # e.g. 0
    load_device_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    load_priority: Union[EmptyStrToNone, int] = None  # e.g. 0
    max_temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    min_time: Union[EmptyStrToNone, float] = None  # e.g. 0
    power: Union[EmptyStrToNone, float] = None  # e.g. 0
    power_factor: Union[EmptyStrToNone, float] = None  # e.g. 0
    reset_factory: Union[EmptyStrToNone, int] = None  # e.g. 0
    restart: Union[EmptyStrToNone, int] = None  # e.g. 0
    rf_command: Union[EmptyStrToNone, str] = None  # e.g. ''
    rf_pair: Union[EmptyStrToNone, float] = None  # e.g. 0
    rs485_addr: Union[EmptyStrToNone, int] = None  # e.g. 0
    rs485_baudrate: Union[EmptyStrToNone, int] = None  # e.g. 0
    serial_num: Union[EmptyStrToNone, str] = None  # e.g. ''
    status: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    target_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    temp: Union[EmptyStrToNone, float] = None  # e.g. 0
    temp_enable: Union[EmptyStrToNone, float] = None  # e.g. 0
    temperature: Union[EmptyStrToNone, float] = None  # e.g. 0
    time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. '2021-05-11 15:39:48'
    )
    total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    total_number: Union[EmptyStrToNone, int] = None  # e.g. 0
    tuning_state: Union[EmptyStrToNone, int] = None  # e.g. 0
    v9420_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    version: Union[EmptyStrToNone, str] = None  # e.g. ''
    voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    water_heater_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    water_state: Union[EmptyStrToNone, int] = None  # e.g. 0
    with_time: Union[EmptyStrToNone, bool] = None  # e.g. False


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
    ammeter_data: Union[EmptyStrToNone, SmartMeterEnergyOverviewData] = (
        None  # e.g. {'aActivePower': 0,...}
    )
    boost_data: Union[EmptyStrToNone, BoostData] = None  # e.g. {'addr': 0,...}
    box_data: Union[EmptyStrToNone, Any] = None  # e.g. None
    children: List[Any]  # e.g. []
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # Collector serial number, e.g. 'NACTEST128'
    )
    device_name: Union[EmptyStrToNone, str] = None  # Device name, e.g. 'GRO_BOOST'
    device_sn: Union[EmptyStrToNone, str] = None  # Serial Number, e.g. 'GRO2020102'
    device_type: Union[EmptyStrToNone, str] = None  # Device type, e.g. 'WIFI_METER'
    device_type_int: Union[EmptyStrToNone, int] = None  # Meter type, e.g. 69
    env_data: Union[EmptyStrToNone, EnvSensorMetricsOverviewData] = (
        None  # e.g. {'addr': 0,...}
    )
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
    lost: Union[EmptyStrToNone, bool] = (
        None  # Whether communication is lost, e.g. False
    )
    meter_ct: Union[EmptyStrToNone, int] = (
        None  # CT value of electric meter, dedicated for 645 electric meter, e.g. 0
    )
    parent_id: Union[EmptyStrToNone, str] = (
        None  # Collector serial number + device type value, e.g. 'LIST_NACTEST128_69'
    )
    parent_sn: Union[EmptyStrToNone, str] = None  # Owning superior device SN, e.g. ''
    pid_data: Union[EmptyStrToNone, Any] = None  # e.g. None
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    pr_month: Union[EmptyStrToNone, float] = None  # Monthly Pr value, e.g. 0
    raillog: Union[EmptyStrToNone, bool] = (
        None  # Is it ShineLink (0: Yes 1: No), e.g. 0
    )
    spct_data: Union[EmptyStrToNone, SpctData] = None  # e.g. {'activeEnergy': 0,...}
    tcp_server_ip: Union[EmptyStrToNone, str] = (
        None  # TCP server IP address, e.g. '47.107.154.111'
    )
    timezone: Union[EmptyStrToNone, int] = None  # Time zone, e.g. 0
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'OD_NACTEST128_69_addr84'
    tree_name: Union[EmptyStrToNone, str] = (
        None  # Device name + device address, e.g. 'GRO_BOOST#84
    )


class GroboostDetails(ApiResponse):
    data: Union[EmptyStrToNone, GroboostDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # Collector serial number, e.g. "NACTEST128"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "GRO2020102"


# #####################################################################################################################
# Groboost metrics overview ###########################################################################################


def _groboost_metrics_overview_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
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
        "win_off_grid_soc": "winOffGridSOC",
        "win_on_grid_soc": "winOnGridSOC",
    }
    return override.get(snake, to_camel(snake=snake))


class GroboostMetricsOverviewBasic(ApiModel):
    """
    energy() returns full set of parameters -> MinEnergyOverviewFull
    energy_history() returns reduced set of parameters -> MinEnergyOverviewBasic
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_groboost_metrics_overview_data_to_camel,
    )

    battery_no: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc1_charge_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_charge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_discharge_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_fault_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc1_ibat: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_ibb: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_illc: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc1_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc1_temp1: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_temp2: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_vbat: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_vbus1: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_vbus2: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc1_warn_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc2_charge_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_charge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_discharge_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_fault_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc2_ibat: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_ibb: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_illc: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc2_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc2_temp1: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_temp2: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_vbat: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_vbus1: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_vbus2: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc2_warn_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc_bus_ref: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc_derate_reason: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc_fault_sub_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    bdc_vbus2_neg: Union[EmptyStrToNone, float] = None  # e.g. 0
    bdc_warn_sub_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_communication_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_cv_volt: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_error2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_error3: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_error4: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_fault_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_fw_version: Union[EmptyStrToNone, str] = None  # e.g. '0'
    bms_ibat: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_icycle: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_info: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_ios_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_max_curr: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_mcu_version: Union[EmptyStrToNone, str] = None  # e.g. '0'
    bms_pack_info: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_soh: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_temp1_bat: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_using_cap: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_vbat: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_vdelta: Union[EmptyStrToNone, float] = None  # e.g. 0
    bms_warn2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_warn_code: Union[EmptyStrToNone, float] = None  # e.g. 0
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    dc_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    dci_r: Union[EmptyStrToNone, float] = None  # e.g. 12
    dci_s: Union[EmptyStrToNone, float] = None  # e.g. 0
    dci_t: Union[EmptyStrToNone, float] = None  # e.g. 0
    debug1: Union[EmptyStrToNone, str] = None  # e.g. '160, 0, 0, 0, 324, 0, 0, 0'
    debug2: Union[EmptyStrToNone, str] = None  # e.g. '0,0,0,0,0,0,0,0'
    derating_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    dry_contact_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    eac_charge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    eac_charge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    eac_today: Union[EmptyStrToNone, float] = None  # e.g. 21.600000381469727
    eac_total: Union[EmptyStrToNone, float] = None  # e.g. 1859.5
    e_charge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_charge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_discharge_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_discharge_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    eex1_today: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    eex1_total: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    eex2_today: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    eex2_total: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    e_local_load_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_local_load_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_fac: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_iac1: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_iac2: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_iac3: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_pac: Union[EmptyStrToNone, float] = None  # Off grid output power, e.g. 0
    eps_pac1: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_pac2: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_pac3: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_pf: Union[EmptyStrToNone, float] = None  # e.g. -1
    eps_vac1: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_vac2: Union[EmptyStrToNone, float] = None  # e.g. 0
    eps_vac3: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv1_today: Union[EmptyStrToNone, float] = None  # e.g. 13.199999809265137
    epv1_total: Union[EmptyStrToNone, float] = None  # e.g. 926.6
    epv2_today: Union[EmptyStrToNone, float] = None  # e.g. 8.199999809265137
    epv2_total: Union[EmptyStrToNone, float] = None  # e.g. 906.4
    epv3_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv3_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv4_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv4_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    epv_total: Union[EmptyStrToNone, float] = None  # e.g. 1833
    e_self_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_self_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_system_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_system_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_to_user_today: Union[EmptyStrToNone, float] = None  # e.g. 0
    e_to_user_total: Union[EmptyStrToNone, float] = None  # e.g. 0
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 50.0099983215332
    fault_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    fault_type1: Union[EmptyStrToNone, int] = None  # e.g. 0
    gfci: Union[EmptyStrToNone, float] = None  # e.g. 78
    iac1: Union[EmptyStrToNone, float] = None  # Grid Current1, e.g. 10.699999809265137
    iac2: Union[EmptyStrToNone, float] = None  # Grid Current2, e.g. 0
    iac3: Union[EmptyStrToNone, float] = None  # Grid Current3, e.g. 0
    inv_delay_time: Union[EmptyStrToNone, float] = None  # e.g. 0
    ipv1: Union[EmptyStrToNone, float] = (
        None  # PV1 input current, e.g. 5.800000190734863
    )
    ipv2: Union[EmptyStrToNone, float] = (
        None  # PV2 input current, e.g. 6.099999904632568
    )
    ipv3: Union[EmptyStrToNone, float] = None  # PV3 input current, e.g. 0
    ipv4: Union[EmptyStrToNone, float] = None  # PV4 input current, e.g. 0
    is_again: Union[EmptyStrToNone, bool] = None  # Is it a continuation, e.g. False
    iso: Union[EmptyStrToNone, float] = None  # e.g. 3135
    load_percent: Union[EmptyStrToNone, float] = None  # e.g. 0
    n_bus_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    new_warn_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    new_warn_sub_code: Union[EmptyStrToNone, int] = None  # e.g. 0
    op_fullwatt: Union[EmptyStrToNone, float] = None  # e.g. 0
    operating_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    p_bus_voltage: Union[EmptyStrToNone, float] = None  # e.g. 367
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 2503.8
    pac1: Union[EmptyStrToNone, float] = (
        None  # Inverter output apparent power 1, e.g. 2530.699951171875
    )
    pac2: Union[EmptyStrToNone, float] = (
        None  # Inverter output apparent power 2, e.g. 0
    )
    pac3: Union[EmptyStrToNone, float] = (
        None  # Inverter output apparent power 3, e.g. 0
    )
    pac_to_grid_total: Union[EmptyStrToNone, float] = (
        None  # Grid countercurrent total power, e.g. 0
    )
    pac_to_local_load: Union[EmptyStrToNone, float] = None  # Total load power, e.g. 0
    pac_to_user_total: Union[EmptyStrToNone, float] = (
        None  # Grid downstream total power, e.g. 0
    )
    pex1: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    pex2: Union[EmptyStrToNone, float] = None  # e.g. -0.1
    pf: Union[EmptyStrToNone, float] = None  # e.g. 0.08100000023841858
    ppv: Union[EmptyStrToNone, float] = None  # PV input total power, e.g. 2558.7
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power, e.g. 1500.7
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power, e.g. 1058
    ppv3: Union[EmptyStrToNone, float] = None  # PV3 input power, e.g. 0
    ppv4: Union[EmptyStrToNone, float] = None  # PV4 input power, e.g. 0
    p_self: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_system: Union[EmptyStrToNone, float] = None  # e.g. 0
    real_op_percent: Union[EmptyStrToNone, float] = None  # e.g. 50
    serial_num: Union[EmptyStrToNone, str] = None  # e.g. 'BNE9A5100D'
    status: Union[EmptyStrToNone, int] = (
        None  # Min Status (0: waiting, 1: normal, 2: fault), e.g. 1
    )
    sys_fault_word: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word1: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word2: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word3: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word4: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word5: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word6: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word7: Union[EmptyStrToNone, int] = None  # e.g. 0
    temp1: Union[EmptyStrToNone, float] = None  # e.g. 47.79999923706055
    temp2: Union[EmptyStrToNone, float] = None  # e.g. 0
    temp3: Union[EmptyStrToNone, float] = None  # e.g. 0
    temp4: Union[EmptyStrToNone, float] = None  # e.g. 0
    temp5: Union[EmptyStrToNone, float] = None  # e.g. 51.70000076293945
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-09 14:52:39'
    time_total: Union[EmptyStrToNone, float] = (
        None  # Total running time, e.g. 1625146.9
    )
    total_working_time: Union[EmptyStrToNone, float] = None  # e.g. 0
    uw_sys_work_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    vac1: Union[EmptyStrToNone, float] = None  # Grid voltage 1, e.g. 239.5
    vac2: Union[EmptyStrToNone, float] = None  # Grid voltage 2, e.g. 0
    vac3: Union[EmptyStrToNone, float] = None  # Grid voltage 3, e.g. 0
    vac_rs: Union[EmptyStrToNone, float] = None  # RS line voltage, e.g. 239.5
    vac_st: Union[EmptyStrToNone, float] = None  # ST line voltage, e.g. 0
    vac_tr: Union[EmptyStrToNone, float] = None  # TR line voltage, e.g. 0
    vpv1: Union[EmptyStrToNone, float] = (
        None  # PV1 input voltage, e.g. 258.6000061035156
    )
    vpv2: Union[EmptyStrToNone, float] = (
        None  # PV2 input voltage, e.g. 9.899999618530273
    )
    vpv3: Union[EmptyStrToNone, float] = None  # PV3 input voltage, e.g. 0
    vpv4: Union[EmptyStrToNone, float] = None  # PV4 input voltage, e.g. 0
    warn_code: Union[EmptyStrToNone, int] = None  # e.g. 220
    warn_code1: Union[EmptyStrToNone, int] = None  # e.g. 2


class GroboostMetricsOverviewFull(GroboostMetricsOverviewBasic):
    """
    energy() returns full set of parameters -> MinEnergyOverviewFull
    energy_history() returns reduced set of parameters -> MinEnergyOverviewBasic
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_groboost_metrics_overview_data_to_camel,
    )
    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    b_merter_connect_flag: Union[EmptyStrToNone, bool] = None  # e.g. 0
    bat_sn: Union[EmptyStrToNone, str] = None  # e.g. ''
    battery_sn: Union[EmptyStrToNone, str] = None  # e.g. ''
    bgrid_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bsystem_work_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'QMN0000000000000'
    day: Union[EmptyStrToNone, str] = None  # e.g. ''
    error_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    iacr: Union[EmptyStrToNone, float] = None  # e.g. 0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    mtnc_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    mtnc_rqst: Union[EmptyStrToNone, float] = None  # e.g. 0
    pacr: Union[EmptyStrToNone, float] = None  # e.g. 0
    soc1: Union[EmptyStrToNone, float] = None  # e.g. 0
    soc2: Union[EmptyStrToNone, float] = None  # e.g. 0
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'Normal'
    t_mtnc_strt: Union[EmptyStrToNone, str] = None  # e.g. ''
    t_win_end: Union[EmptyStrToNone, str] = None  # e.g. ''
    t_win_start: Union[EmptyStrToNone, str] = None  # e.g. ''
    tlx_bean: Union[EmptyStrToNone, Any] = None  # e.g. None
    vacr: Union[EmptyStrToNone, float] = None  # e.g. 0
    vacrs: Union[EmptyStrToNone, float] = None  # e.g. 0
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    win_mode: Union[EmptyStrToNone, int] = None  # e.g. 0
    win_off_grid_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    win_on_grid_soc: Union[EmptyStrToNone, float] = None  # e.g. 0
    win_request: Union[EmptyStrToNone, int] = None  # e.g. 0
    with_time: Union[EmptyStrToNone, bool] = (
        None  # Whether the data sent has its own time, e.g. False
    )


def _groboost_metrics_overview_to_camel(snake: str) -> str:
    override = {
        "device_sn": "tlx_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class GroboostMetricsOverview(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_groboost_metrics_overview_to_camel,
    )

    data: Union[EmptyStrToNone, GroboostMetricsOverviewFull] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the inverter, e.g. "ZT00100001"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Groboost metrics overview multiple ##################################################################################


class GroboostMetricsOverviewMultipleItem(ApiModel):
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the inverter, e.g. "ZT00100001"
    )
    data: Union[EmptyStrToNone, GroboostMetricsOverviewFull] = None


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
        "device_sn": "tlx_sn",
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
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the inverter, e.g. "ZT00100001"
    )
    datas: List[GroboostMetricsOverviewBasic]


class GroboostMetricsHistory(ApiResponse):
    data: Union[EmptyStrToNone, GroboostMetricsHistoryData] = None
