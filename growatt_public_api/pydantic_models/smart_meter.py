import datetime
from typing import Union, List

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
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the smart meter, e.g. 'CRAZT00001'
    device_name: Union[EmptyStrToNone, str] = None  # device name, e.g. 'AMMETER'
    device_type: Union[EmptyStrToNone, str] = (
        None  # Device type (64: smart meter, 66: SDM one-way meter, 67: SDM three-way meter, 70: CHNT one-way meter, 71: CHNT three-way meter), e.g. '64'
    )
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. '2019-01-09 10:33:06'
    lost: Union[EmptyStrToNone, bool] = None  # The online status of the device (0: online, 1: disconnected), e.g. 0


class SmartMeterListData(ApiModel):
    count: int  # Total number of devices
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'CRAZT00001'
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

    a_active_power: Union[EmptyStrToNone, float] = None  # A-phase active power, e.g. 0
    a_current: Union[EmptyStrToNone, float] = None  # A phase current, e.g. 0
    a_power_factor: Union[EmptyStrToNone, float] = None  # A-phase power factor, e.g. 0
    a_reactive_power: Union[EmptyStrToNone, float] = None  # e.g. 0
    a_voltage: Union[EmptyStrToNone, float] = None  # Phase A voltage, e.g. 0
    active_energy: Union[EmptyStrToNone, float] = (
        None  # Total active energy / Combined active power, e.g. 48.900001525878906
    )
    active_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    active_power: Union[EmptyStrToNone, float] = None  # Total active power, e.g. 5589.60009765625
    active_power_l1: Union[EmptyStrToNone, float] = None  # active power L1, e.g. 0
    active_power_l2: Union[EmptyStrToNone, float] = None  # active power L2, e.g. 0
    active_power_l3: Union[EmptyStrToNone, float] = None  # active power L3, e.g. 0
    active_power_max_need: Union[EmptyStrToNone, float] = None  # Total active power maximum demand, e.g. 0
    active_power_max_need_one: Union[EmptyStrToNone, float] = None  # Maximum total active power demand, e.g. 0
    active_power_need: Union[EmptyStrToNone, float] = None  # Current total active power demand, e.g. 0
    active_power_need_one: Union[EmptyStrToNone, float] = None  # Total active power demand, e.g. 0
    address: Union[EmptyStrToNone, int] = None  # Smart meter device address, e.g. 1
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alarm_Code: Union[EmptyStrToNone, int] = None  # e.g. ''
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    apparent_energy: Union[EmptyStrToNone, float] = None  # apparent energy, e.g. 0
    apparent_energy_max_need: Union[EmptyStrToNone, float] = None  # Current total apparent power maximum demand, e.g. 0
    apparent_energy_need: Union[EmptyStrToNone, float] = None  # Current total apparent power demand, e.g. 0
    apparent_power: Union[EmptyStrToNone, float] = None  # Total apparent power, e.g. 6025.5
    apparent_power_l1: Union[EmptyStrToNone, float] = None  # Apparent Power L1, e.g. 0
    apparent_power_l2: Union[EmptyStrToNone, float] = None  # Apparent Power L2, e.g. 0
    apparent_power_l3: Union[EmptyStrToNone, float] = None  # Apparent Power L3, e.g. 0
    b_active_power: Union[EmptyStrToNone, float] = None  # Phase B active power, e.g. 0
    b_power_factor: Union[EmptyStrToNone, float] = None  # B-phase power factor, e.g. 0
    b_reactive_power: Union[EmptyStrToNone, float] = None  # Phase B reactive power, e.g. 0
    c_active_power: Union[EmptyStrToNone, float] = None  # C-phase active power, e.g. 0
    c_power_factor: Union[EmptyStrToNone, float] = None  # C-phase power factor, e.g. 0
    c_reactive_power: Union[EmptyStrToNone, float] = None  # C-phase reactive power, e.g. 0
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None  # e.g. {'firstDayOfWeek: 1, ...}
    com_address: Union[EmptyStrToNone, int] = None  # e.g. 0
    combined_reactive_power1: Union[EmptyStrToNone, float] = None  # e.g. 0
    combined_reactive_power2: Union[EmptyStrToNone, float] = None  # e.g. 0
    comm_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    current: Union[EmptyStrToNone, float] = None  # current, e.g. 0
    current_active_demand: Union[EmptyStrToNone, float] = None  # e.g. 0
    current_harmonic_avg: Union[EmptyStrToNone, float] = (
        None  # Average value of total harmonic content of three-phase current, e.g. 0
    )
    current_ia: Union[EmptyStrToNone, float] = None  # Three-phase current Ia, e.g. 0
    current_ib: Union[EmptyStrToNone, float] = None  # Three-phase current Ib, e.g. 0
    current_ic: Union[EmptyStrToNone, float] = None  # Three-phase current Ic, e.g. 0
    current_l1: Union[EmptyStrToNone, float] = None  # current L1, e.g. 0
    current_l1_max_need: Union[EmptyStrToNone, float] = None  # L1 current maximum demand, e.g. 0
    current_l1_need: Union[EmptyStrToNone, float] = None  # Current L1 current demand, e.g. 0
    current_l2: Union[EmptyStrToNone, float] = None  # current L2, e.g. 0
    current_l2_max_need: Union[EmptyStrToNone, float] = None  # L2 current maximum demand, e.g. 0
    current_l2_need: Union[EmptyStrToNone, float] = None  # Current L2 current demand, e.g. 0
    current_l3: Union[EmptyStrToNone, float] = None  # current L3, e.g. 0
    current_l3_max_need: Union[EmptyStrToNone, float] = None  # L3 current maximum demand, e.g. 0
    current_l3_need: Union[EmptyStrToNone, float] = None  # Current L3 current demand, e.g. 0
    current_max_need: Union[EmptyStrToNone, float] = None  # Maximum current demand, e.g. 0
    current_need: Union[EmptyStrToNone, float] = None  # Current demand, e.g. 0
    current_reactive_demand: Union[EmptyStrToNone, float] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the smart meter, e.g. 'CRAZT00001'
    device_sn: Union[EmptyStrToNone, str] = None  # e.g. ''
    ex_power_factor: Union[EmptyStrToNone, float] = None  # e.g. 0
    fei_lv_bo_z_energy: Union[EmptyStrToNone, float] = None  # Rate wave forward active power, e.g. 15.899999618530273
    fei_lv_feng_z_energy: Union[EmptyStrToNone, float] = (
        None  # Rate peak positive active power, e.g. 10.199999809265137
    )
    fei_lv_gu_z_energy: Union[EmptyStrToNone, float] = None  # Rate Valley Positive Active Power, e.g. 5.400000095367432
    fei_lv_ping_z_energy: Union[EmptyStrToNone, float] = None  # The rate is flat positive active power, e.g. 6.5
    forward_active_max_need: Union[EmptyStrToNone, float] = None  # Maximum forward active power demand, e.g. 0
    forward_active_need: Union[EmptyStrToNone, float] = None  # forward active power demand, e.g. 0
    frequency: Union[EmptyStrToNone, float] = None  # frequency, e.g. 0
    generic_meter: Union[EmptyStrToNone, int] = None  # e.g. None
    grid_energy: Union[EmptyStrToNone, float] = None  # Grid-side electricity, e.g. 0
    grid_frequency: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 0
    history_number: Union[EmptyStrToNone, int] = None  # e.g. 0
    instant_total_apparent_power: Union[EmptyStrToNone, float] = None  # Instantaneous total apparent power, e.g. 0
    instant_total_active_power: Union[EmptyStrToNone, float] = None  # instantly total active power, e.g. 0
    instant_total_reactive_power: Union[EmptyStrToNone, float] = None  # instantly total reactive power, e.g. 0
    l1_current_harmonic: Union[EmptyStrToNone, float] = None  # L1 current total harmonic content, e.g. 0
    l1_voltage2: Union[EmptyStrToNone, float] = None  # L1-2 line voltage, e.g. 0
    l1_voltage_harmonic: Union[EmptyStrToNone, float] = None  # L1 phase voltage total harmonic content, e.g. 0
    l1_voltage_harmonic2: Union[EmptyStrToNone, float] = None  # L1-2 line voltage total harmonic content, e.g. 0
    l2_current_harmonic: Union[EmptyStrToNone, float] = None  # L2 current total harmonic content, e.g. 0
    l2_voltage3: Union[EmptyStrToNone, float] = None  # L2-3 line voltage, e.g. 0
    l2_voltage_harmonic: Union[EmptyStrToNone, float] = None  # L2 phase voltage total harmonic content, e.g. 0
    l2_voltage_harmonic3: Union[EmptyStrToNone, float] = None  # L2-3 line voltage total harmonic content, e.g. 0
    l3_current_harmonic: Union[EmptyStrToNone, float] = None  # L3 current total harmonic content, e.g. 0
    l3_voltage1: Union[EmptyStrToNone, float] = None  # L3-1 line voltage, e.g. 0
    l3_voltage_harmonic: Union[EmptyStrToNone, float] = None  # L3 phase voltage total harmonic content, e.g. 0
    l3_voltage_harmonic1: Union[EmptyStrToNone, float] = None  # L3-1 line voltage total harmonic content, e.g. 0
    line_voltage_harmonic_avg: Union[EmptyStrToNone, float] = (
        None  # Average value of total harmonic content of three-phase line voltage, e.g. 0
    )
    lost: Union[EmptyStrToNone, bool] = None  # e.g. False
    meter_dh: Union[EmptyStrToNone, float] = None  # e.g. 0
    meter_ms: Union[EmptyStrToNone, float] = None  # e.g. 0
    meter_ym: Union[EmptyStrToNone, float] = None  # e.g. 0
    mode_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    month_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    posi_active_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    posi_active_power: Union[EmptyStrToNone, float] = None  # Positive active power, e.g. 0
    posi_reactive_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    posi_reactive_power: Union[EmptyStrToNone, float] = None  # Positive reactive power, e.g. 0
    positive_active_today_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    positive_active_total_energy: Union[EmptyStrToNone, float] = None  # positive active total energy, e.g. 0
    power_factor: Union[EmptyStrToNone, float] = (
        None  # Total power factor / combined power factor, e.g. 0.9991999864578247
    )
    power_factor_l1: Union[EmptyStrToNone, float] = None  # Power Factor L1, e.g. 0
    power_factor_l2: Union[EmptyStrToNone, float] = None  # Power Factor L2, e.g. 0
    power_factor_l3: Union[EmptyStrToNone, float] = None  # Power Factor L3, e.g. 0
    reactive_energy: Union[EmptyStrToNone, float] = (
        None  # Total reactive energy / combined reactive power, e.g. 0.10000000149011612
    )
    reactive_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reactive_power: Union[EmptyStrToNone, float] = None  # Total reactive power, e.g. 168.89999389648438
    reactive_power_l1: Union[EmptyStrToNone, float] = None  # Reactive Power L1, e.g. 0
    reactive_power_l2: Union[EmptyStrToNone, float] = None  # Reactive Power L2, e.g. 0
    reactive_power_l3: Union[EmptyStrToNone, float] = None  # Reactive Power L3, e.g. 0
    reverse_active_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_active_power: Union[EmptyStrToNone, float] = None  # reverse active power, e.g. 0
    reverse_apparent_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_reactive_net_total_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_reactive_power: Union[EmptyStrToNone, float] = None  # Reverse reactive power, e.g. 0
    reverse_active_energy: Union[EmptyStrToNone, float] = None  # e.g. 0
    reverse_active_max_need: Union[EmptyStrToNone, float] = None  # Maximum reverse active power demand, e.g. 0
    reverse_active_need: Union[EmptyStrToNone, float] = None  # reverse active power demand, e.g. 0
    reverse_active_today_energy: Union[EmptyStrToNone, float] = None  # Reverse active total energy, e.g. 0
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
    time_text: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. '2019-01-09 15:00:34'
    today_energy: Union[EmptyStrToNone, float] = None  # Total Energy, e.g. 0
    total_active_energy_l1: Union[EmptyStrToNone, float] = None  # total active energy L1, e.g. 0
    total_active_energy_l2: Union[EmptyStrToNone, float] = None  # total active energy L2, e.g. 0
    total_active_energy_l3: Union[EmptyStrToNone, float] = None  # total active energy L3, e.g. 0
    total_energy: Union[EmptyStrToNone, float] = None  # Total energy of the meter, e.g. 0
    total_reactive_energy_l1: Union[EmptyStrToNone, float] = None  # total reactive energy L1, e.g. 0
    total_reactive_energy_l2: Union[EmptyStrToNone, float] = None  # total reactive energy L2, e.g. 0
    total_reactive_energy_l3: Union[EmptyStrToNone, float] = None  # total reactive energy L3, e.g. 0
    user_energy: Union[EmptyStrToNone, float] = None  # User-side power, e.g. 0
    voltage: Union[EmptyStrToNone, float] = None  # voltage, e.g. 0
    voltage_harmonic_avg: Union[EmptyStrToNone, float] = (
        None  # Average value of total harmonic content of three-phase voltage, e.g. 0
    )
    voltage_l1: Union[EmptyStrToNone, float] = None  # voltage L1, e.g. 0
    voltage_l2: Union[EmptyStrToNone, float] = None  # voltage L2, e.g. 0
    voltage_l3: Union[EmptyStrToNone, float] = None  # voltage L3, e.g. 0
    voltage_ua: Union[EmptyStrToNone, float] = None  # Three-phase phase voltage Ua, e.g. 0
    voltage_uab: Union[EmptyStrToNone, float] = None  # Three-phase line voltage Uab, e.g. 0
    voltage_ub: Union[EmptyStrToNone, float] = None  # Three-phase phase voltage Ub, e.g. 0
    voltage_ubc: Union[EmptyStrToNone, float] = None  # Three-phase line voltage Ubc, e.g. 0
    voltage_uc: Union[EmptyStrToNone, float] = None  # Three-phase phase voltage Uc, e.g. 0
    voltage_uca: Union[EmptyStrToNone, float] = None  # Three-phase line voltage Uca, e.g. 0
    with_time: Union[EmptyStrToNone, bool] = None  # e.g. False
    zero_line_max_need: Union[EmptyStrToNone, float] = None  # zero line current maximum demand, e.g. 0
    zero_line_need: Union[EmptyStrToNone, float] = None  # The current zero line current demand, e.g. 0


class SmartMeterEnergyOverview(ApiResponse):
    data: Union[EmptyStrToNone, SmartMeterEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "MONITOR003"


# #####################################################################################################################
# Smart meter energy history ##########################################################################################


class SmartMeterEnergyHistoryData(ApiModel):
    count: int  # Total Records
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "CRAZT00001"
    meter_data: List[SmartMeterEnergyOverviewData]


class SmartMeterEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, SmartMeterEnergyHistoryData] = None
