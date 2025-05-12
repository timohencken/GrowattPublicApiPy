import datetime
from typing import Union, List, Optional, TypeAlias, Annotated

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
# Smart meter list ####################################################################################################


def _smart_meter_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "datalog_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class SmartMeterData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_smart_meter_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # device address, e.g. '1'
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the smart meter, e.g. 'CRAZT00001'
    )
    device_name: Union[EmptyStrToNone, str] = None  # device name, e.g. 'AMMETER'
    device_type: Union[EmptyStrToNone, str] = (
        None  # Device type (64: smart meter, 66: SDM one-way meter, 67: SDM three-way meter, 70: CHNT one-way meter, 71: CHNT three-way meter), e.g. '64'
    )
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = (
        None  # Last update time, e.g. '2019-01-09 10:33:06'
    )
    lost: Union[EmptyStrToNone, bool] = (
        None  # The online status of the device (0: online, 1: disconnected), e.g. 0
    )


class SmartMeterListData(ApiModel):
    count: int  # Total number of devices
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The serial number of the collector, e.g. 'CRAZT00001'
    )
    meters: List[SmartMeterData]


class SmartMeterList(ApiResponse):
    data: Union[EmptyStrToNone, SmartMeterListData] = None


# #####################################################################################################################
# Smart meter energy overview #########################################################################################


def _smart_meter_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "instant_total_apparent_power": "instantaneousTotalApparentPower",
        "instant_total_active_power": "instantlyTotalActivePower",
        "instant_total_reactive_power": "instantlyTotalReactivePower",
        "reverse_active_net_total_energy": "reverActiveNetTotalEnergy",
        "reverse_active_power": "reverActivePower",
        "reverse_apparent_energy": "reverApparentEnergy",
        "reverse_reactive_net_total_energy": "reverReactiveNetTotalEnergy",
        "reverse_reactive_power": "reverReactivePower",
        "reverse_instant_total_active_power": "reverseInstantlyTotalActivePower",
    }
    return override.get(snake, to_camel(snake=snake))


class SmartMeterEnergyOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_smart_meter_energy_overview_data_to_camel,
    )

    a_active_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_power_factor: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_energy: Union[EmptyStrToNone, float] = (
        None  # active energy, e.g. 48.900001525878906
    )
    active_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_power: Union[EmptyStrToNone, float] = (
        None  # active power, e.g. 5589.60009765625
    )
    active_power_l1: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_power_l2: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_power_l3: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_power_max_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_power_max_need_one: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_power_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_power_need_one: Union[EmptyStrToNone, float] = None  # e.g. 0
    address: Union[EmptyStrToNone, int] = None  # Smart meter device address, e.g. 1
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alarm_Code: Union[EmptyStrToNone, int] = None  # e.g. ''
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    apparent_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    apparent_energy_max_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    apparent_energy_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    apparent_power: Union[EmptyStrToNone, float] = None  # Apparent Power, e.g. 6025.5
    apparent_power_l1: Union[EmptyStrToNone, float] = None  # e.g. 0
    apparent_power_l2: Union[EmptyStrToNone, float] = None  # e.g. 0
    apparent_power_l3: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_active_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_power_factor: Union[EmptyStrToNone, float] = None  # e.g. 0
    b_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_active_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_power_factor: Union[EmptyStrToNone, float] = None  # e.g. 0
    c_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = (
        None  # e.g. {'firstDayOfWeek: 1, ...}
    )
    com_address: Union[EmptyStrToNone, int] = None  # e.g. 0
    combined_reactive_power1: Union[EmptyStrToNone, float] = None  # e.g. 0
    combined_reactive_power2: Union[EmptyStrToNone, float] = None  # e.g. 0
    comm_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    current: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_active_demand: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_harmonic_avg: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_ia: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_ib: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_ic: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_l1: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_l1_max_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_l1_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_l2: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_l2_max_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_l2_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_l3: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_l3_max_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_l3_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_max_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_reactive_demand: Union[EmptyStrToNone, float] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the smart meter, e.g. 'CRAZT00001'
    )
    device_sn: Union[EmptyStrToNone, str] = None  # e.g. ''
    ex_power_factor: Union[EmptyStrToNone, float] = None  # e.g. 0
    fei_lv_bo_z_energy: Union[EmptyStrToNone, float] = (
        None  # Rate wave forward active power, e.g. 15.899999618530273
    )
    fei_lv_feng_z_energy: Union[EmptyStrToNone, float] = (
        None  # Rate peak positive active power, e.g. 10.199999809265137
    )
    fei_lv_gu_z_energy: Union[EmptyStrToNone, float] = (
        None  # Rate Valley Positive Active Power, e.g. 5.400000095367432
    )
    fei_lv_ping_z_energy: Union[EmptyStrToNone, float] = (
        None  # The rate is flat positive active power, e.g. 6.5
    )
    forward_active_max_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    forward_active_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    frequency: Union[EmptyStrToNone, float] = None  # e.g. 0
    generic_meter: Union[EmptyStrToNone, int] = None  # e.g. None
    grid_energy: Union[EmptyStrToNone, float] = None  # Grid-side electricity, e.g. 0
    grid_frequency: Union[EmptyStrToNone, float] = None  # e.g. 0
    history_number: Union[EmptyStrToNone, int] = None  # e.g. 0
    instant_total_apparent_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    instant_total_active_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    instant_total_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    l1_current_harmonic: Union[EmptyStrToNone, float] = None  # e.g. 0
    l1_voltage2: Union[EmptyStrToNone, float] = None  # e.g. 0
    l1_voltage_harmonic: Union[EmptyStrToNone, float] = None  # e.g. 0
    l1_voltage_harmonic2: Union[EmptyStrToNone, float] = None  # e.g. 0
    l2_current_harmonic: Union[EmptyStrToNone, float] = None  # e.g. 0
    l2_voltage3: Union[EmptyStrToNone, float] = None  # e.g. 0
    l2_voltage_harmonic: Union[EmptyStrToNone, float] = None  # e.g. 0
    l2_voltage_harmonic3: Union[EmptyStrToNone, float] = None  # e.g. 0
    l3_current_harmonic: Union[EmptyStrToNone, float] = None  # e.g. 0
    l3_voltage1: Union[EmptyStrToNone, float] = None  # e.g. 0
    l3_voltage_harmonic: Union[EmptyStrToNone, float] = None  # e.g. 0
    l3_voltage_harmonic1: Union[EmptyStrToNone, float] = None  # e.g. 0
    line_voltage_harmonic_avg: Union[EmptyStrToNone, float] = None  # e.g. 0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. False
    meter_dh: Union[EmptyStrToNone, float] = None  # e.g. 0
    meter_ms: Union[EmptyStrToNone, float] = None  # e.g. 0
    meter_ym: Union[EmptyStrToNone, float] = None  # e.g. 0
    mode_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    month_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    posi_active_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    posi_active_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    posi_reactive_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    posi_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    positive_active_today_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    positive_active_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    power_factor: Union[EmptyStrToNone, float] = (
        None  # Power factor, e.g. 0.9991999864578247
    )
    power_factor_l1: Union[EmptyStrToNone, float] = None  # e.g. 0
    power_factor_l2: Union[EmptyStrToNone, float] = None  # e.g. 0
    power_factor_l3: Union[EmptyStrToNone, float] = None  # e.g. 0
    reactive_energy: Union[EmptyStrToNone, float] = (
        None  # Reactive energy, e.g. 0.10000000149011612
    )
    reactive_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reactive_power: Union[EmptyStrToNone, float] = (
        None  # reactive power, e.g. 168.89999389648438
    )
    reactive_power_l1: Union[EmptyStrToNone, float] = None  # e.g. 0
    reactive_power_l2: Union[EmptyStrToNone, float] = None  # e.g. 0
    reactive_power_l3: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_active_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_active_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_apparent_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_reactive_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_active_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_active_max_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_active_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_active_today_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_active_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_instant_total_active_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    run_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    soft_code: Union[EmptyStrToNone, int] = None  # e.g. ''
    soft_version: Union[EmptyStrToNone, int] = None  # e.g. 0
    status_last_update_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    thdi1: Union[EmptyStrToNone, float] = None  # e.g. 0
    thdi2: Union[EmptyStrToNone, float] = None  # e.g. 0
    thdi3: Union[EmptyStrToNone, float] = None  # e.g. 0
    thdv1: Union[EmptyStrToNone, float] = None  # e.g. 0
    thdv2: Union[EmptyStrToNone, float] = None  # e.g. 0
    thdv3: Union[EmptyStrToNone, float] = None  # e.g. 0
    time_text: Union[EmptyStrToNone, datetime.datetime] = (
        None  # Last update time, e.g. '2019-01-09 15:00:34'
    )
    today_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    total_active_energy_l1: Union[EmptyStrToNone, float] = None  # e.g. 0
    total_active_energy_l2: Union[EmptyStrToNone, float] = None  # e.g. 0
    total_active_energy_l3: Union[EmptyStrToNone, float] = None  # e.g. 0
    total_energy: Union[EmptyStrToNone, float] = (
        None  # Total energy of the meter, e.g. 0
    )
    total_reactive_energy_l1: Union[EmptyStrToNone, float] = None  # e.g. 0
    total_reactive_energy_l2: Union[EmptyStrToNone, float] = None  # e.g. 0
    total_reactive_energy_l3: Union[EmptyStrToNone, float] = None  # e.g. 0
    user_energy: Union[EmptyStrToNone, float] = None  # User-side power, e.g. 0
    voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_harmonic_avg: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_l1: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_l2: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_l3: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_ua: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_uab: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_ub: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_ubc: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_uc: Union[EmptyStrToNone, float] = None  # e.g. 0
    voltage_uca: Union[EmptyStrToNone, float] = None  # e.g. 0
    with_time: Union[EmptyStrToNone, bool] = None  # e.g. False
    zero_line_max_need: Union[EmptyStrToNone, float] = None  # e.g. 0
    zero_line_need: Union[EmptyStrToNone, float] = None  # e.g. 0


class SmartMeterEnergyOverview(ApiResponse):
    data: Union[EmptyStrToNone, SmartMeterEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the inverter, e.g. "MONITOR003"
    )


# #####################################################################################################################
# Smart meter energy history ##########################################################################################


class PbdEnergyHistoryData(ApiModel):
    count: int  # Total Records
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the inverter, e.g. "CRAZT00001"
    )
    meter_data: List[SmartMeterEnergyOverviewData]


class SmartMeterEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, PbdEnergyHistoryData] = None
