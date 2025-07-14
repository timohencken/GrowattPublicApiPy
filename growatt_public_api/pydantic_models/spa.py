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
    ForcedTime,
)


# #####################################################################################################################
# Spa setting read ####################################################################################################


class SpaSettingRead(ApiResponse):
    data: Union[EmptyStrToNone, str] = None  # current setting / register value


# #####################################################################################################################
# Spa setting write ###################################################################################################


class SpaSettingWrite(ApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# #####################################################################################################################
# Spa details #########################################################################################################


def _spa_detail_data_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "bat_aging_test_step": "bagingTestStep",
        "buck_ups_volt_set": "buckUPSVoltSet",
        "datalogger_sn": "dataLogSn",
        "discharge_power_command": "disChargePowerCommand",
        "parent_id": "parentID",
        "pv_pf_cmd_memory_state_mix": "pvPfCmdMemoryState",  # added _mix to differentiate from pv_pf_cmd_memory_state
        "plant_name": "plantname",
        "tree_id": "treeID",
        "baudrate": "wselectBaudrate",
        "vbat_start_for_charge": "vbatStartforCharge",
        "w_charge_soc_low_limit1": "wchargeSOCLowLimit1",
        "w_charge_soc_low_limit2": "wchargeSOCLowLimit2",
        "w_discharge_soc_low_limit1": "wdisChargeSOCLowLimit1",
        "w_discharge_soc_low_limit2": "wdisChargeSOCLowLimit2",
    }
    return override.get(snake, to_camel(snake=snake))


class SpaDetailData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spa_detail_data_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    active_p_rate: Union[EmptyStrToNone, int] = None  # Set active power, e.g. 100
    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. 'LHD0847002'
    backflow_setting: Union[EmptyStrToNone, str] = None  # Backflow prevention setting, e.g. ''
    bat_aging_test_step: Union[EmptyStrToNone, int] = (
        None  # battery self-test (0: default, 1: charge, 2: discharge), e.g. 0
    )
    bat_first_switch1: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_first_switch2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_first_switch3: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_temp_lower_limit_c: Union[EmptyStrToNone, float] = None  # Lower limit of battery charging temperature, e.g. 110
    bat_temp_lower_limit_d: Union[EmptyStrToNone, float] = (
        None  # Lower limit of battery discharge temperature, e.g. 110
    )
    bat_temp_upper_limit_c: Union[EmptyStrToNone, float] = None  # Upper limit of battery charging temperature, e.g. 60
    bat_temp_upper_limit_d: Union[EmptyStrToNone, float] = None  # Upper limit of battery discharge temperature, e.g. 70
    battery_type: Union[EmptyStrToNone, int] = None  # Battery type selection, e.g. 1
    bct_adjust: Union[EmptyStrToNone, int] = None  # Sensor adjustment enable, e.g. 0
    bct_mode: Union[EmptyStrToNone, int] = None  # Sensor type (0=cWiredCT, 1=cWirelessCT, 2=METER), e.g. 0
    buck_ups_volt_set: Union[EmptyStrToNone, float] = None  # Off-grid voltage, e.g. 0
    buck_ups_fun_en: Union[EmptyStrToNone, bool] = None  # Off-grid enable, e.g. 1
    charge_power_command: Union[EmptyStrToNone, int] = None  # Charging power setting, e.g. 100
    charge_time1: Union[EmptyStrToNone, str] = None  # e.g. ''
    charge_time2: Union[EmptyStrToNone, str] = None  # e.g. ''
    charge_time3: Union[EmptyStrToNone, str] = None  # e.g. ''
    children: List[Any]  # e.g. []
    com_address: Union[EmptyStrToNone, int] = None  # Mailing address, e.g. 1
    communication_version: Union[EmptyStrToNone, str] = None  # Communication version number, e.g. 'GJAA-0003'
    country_selected: Union[EmptyStrToNone, int] = None  # country selection, e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'VC51030322020001'
    discharge_power_command: Union[EmptyStrToNone, int] = None  # Discharge power setting, e.g. 100
    discharge_time1: Union[EmptyStrToNone, str] = None  # e.g. ''
    discharge_time2: Union[EmptyStrToNone, str] = None  # e.g. ''
    discharge_time3: Union[EmptyStrToNone, str] = None  # e.g. ''
    dtc: Union[EmptyStrToNone, int] = None  # Device code, e.g. 3501
    energy_day: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_day_map: Union[EmptyStrToNone, Any] = None  # e.g. {}
    energy_month: Union[EmptyStrToNone, float] = None  # e.g. 0
    energy_month_text: Union[EmptyStrToNone, str] = None  # e.g. '0'
    eps_freq_set: Union[EmptyStrToNone, int] = None  # Emergency power frequency, e.g. 1
    eps_fun_en: Union[EmptyStrToNone, bool] = None  # Emergency power enable, e.g. 1
    eps_volt_set: Union[EmptyStrToNone, int] = None  # Emergency power supply voltage, e.g. 1
    equipment_type: Union[EmptyStrToNone, str] = None  # e.g. ''
    float_charge_current_limit: Union[EmptyStrToNone, float] = None  # float charge current limit, e.g. 600
    forced_charge_time_start1: Union[EmptyStrToNone, ForcedTime] = None  # Charge 1 start time, e.g. '18:0'
    forced_charge_time_start2: Union[EmptyStrToNone, ForcedTime] = None  # Charge 2 start time, e.g. '21:30'
    forced_charge_time_start3: Union[EmptyStrToNone, ForcedTime] = None  # Charge 3 start time, e.g. '3:0'
    forced_charge_time_stop1: Union[EmptyStrToNone, ForcedTime] = None  # Charge 1 stop time, e.g. '19:30'
    forced_charge_time_stop2: Union[EmptyStrToNone, ForcedTime] = None  # Charge 2 stop time, e.g. '23:0'
    forced_charge_time_stop3: Union[EmptyStrToNone, ForcedTime] = None  # Charge 3 stop time, e.g. '4:30'
    forced_discharge_time_start1: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 1 start time, e.g. '0:0'
    forced_discharge_time_start2: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 2 start time, e.g. '0:0'
    forced_discharge_time_start3: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 3 start time, e.g. '0:0'
    forced_discharge_time_stop1: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 1 stop time, e.g. '0:0'
    forced_discharge_time_stop2: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 2 stop time, e.g. '0:0'
    forced_discharge_time_stop3: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 3 stop time, e.g. '0:0'
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'RH1.0'
    grid_first_switch1: Union[EmptyStrToNone, bool] = None  # e.g. 0
    grid_first_switch2: Union[EmptyStrToNone, bool] = None  # e.g. 0
    grid_first_switch3: Union[EmptyStrToNone, bool] = None  # e.g. 0
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Internal version number, e.g. 'rHAA020202'
    last_update_time: Union[EmptyStrToNone, GrowattTime] = (
        None  # Last update time, e.g. {'date': 12, 'day': 2, 'hours': 16, 'minutes': 46, 'month': 3, 'seconds': 22, 'time': 1649753182000, 'timezoneOffset': -480, 'year': 122}
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-12 16:46:22'
    lcd_language: Union[EmptyStrToNone, int] = None  # e.g. 1
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    load_first_start_time1: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 1 start time, e.g. '0:0'
    load_first_start_time2: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 2 start time, e.g. '4:30'
    load_first_start_time3: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 3 start time, e.g. '0:0'
    load_first_stop_time1: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 1 end time, e.g. '23:59'
    load_first_stop_time2: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 2 end time, e.g. '7:29'
    load_first_stop_time3: Union[EmptyStrToNone, ForcedTime] = None  # Load priority period 3 end time, e.g. '0:0'
    load_first_switch1: Union[EmptyStrToNone, bool] = None  # Load priority enable bit 1, e.g. 0
    load_first_switch2: Union[EmptyStrToNone, bool] = None  # Load priority enable bit 2, e.g. 0
    load_first_switch3: Union[EmptyStrToNone, bool] = None  # Load priority enable bit 3, e.g. 0
    location: Union[EmptyStrToNone, str] = None  # address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: disconnected), e.g. True
    manufacturer: Union[EmptyStrToNone, str] = None  # Manufacturer Code, e.g. 'New Energy'
    modbus_version: Union[EmptyStrToNone, int] = None  # MODBUS version, e.g. 305
    model: Union[EmptyStrToNone, int] = None  # model, e.g. 2666130979655057522
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'S25B00D00T00P0FU01M0072'
    on_off: Union[EmptyStrToNone, bool] = None  # Switch machine, e.g. 0
    p_charge: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_discharge: Union[EmptyStrToNone, float] = None  # e.g. 0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_VC51030322020001_22'
    pf_cmd_memory_state: Union[EmptyStrToNone, int] = None  # Set storage PF command, e.g. 0
    pf_sys_year: Union[EmptyStrToNone, str] = None  # Set time, e.g. ''
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. 0
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    pmax: Union[EmptyStrToNone, int] = None  # Rated power, e.g. 0
    port_name: Union[EmptyStrToNone, str] = None  # e.g. 'port_name'
    power_factor: Union[EmptyStrToNone, float] = None  # PF value, e.g. 0
    power_max: Union[EmptyStrToNone, float] = None  # e.g. ''
    power_max_text: Union[EmptyStrToNone, str] = None  # e.g. ''
    power_max_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    priority_choose: Union[EmptyStrToNone, int] = None  # Energy priority selection, e.g. 0
    pv_active_p_rate: Union[EmptyStrToNone, float] = None  # Set active power, e.g. ''
    pv_grid_voltage_high: Union[EmptyStrToNone, float] = None  # Mains voltage upper limit, e.g. ''
    pv_grid_voltage_low: Union[EmptyStrToNone, float] = None  # Mains voltage lower limit, e.g. ''
    pv_on_off: Union[EmptyStrToNone, bool] = None  # Switch, e.g. ''
    pv_pf_cmd_memory_state: Union[EmptyStrToNone, bool] = (
        None  # Set whether to store the following PF commands, e.g. ''
    )
    pv_power_factor: Union[EmptyStrToNone, float] = None  # Set PF value, e.g. ''
    pv_reactive_p_rate: Union[EmptyStrToNone, float] = None  # Set reactive power, e.g. ''
    pv_reactive_p_rate_two: Union[EmptyStrToNone, float] = None  # No power capacity/inductive, e.g. ''
    reactive_p_rate: Union[EmptyStrToNone, int] = None  # Reactive power, e.g. 100
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'LHD0847002'
    spa_ac_discharge_frequency: Union[EmptyStrToNone, float] = None  # Off-grid frequency, e.g. ''
    spa_ac_discharge_voltage: Union[EmptyStrToNone, float] = None  # Off-grid voltage, e.g. ''
    spa_off_grid_enable: Union[EmptyStrToNone, bool] = None  # Off-grid enable, e.g. ''
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: waiting, 1: self-check, 3: failure, 4: upgrade, 5, 6, 7, 8: normal mode), e.g. 0
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'tlx.status.operating'
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # System Time, e.g. '2019-03-05 10:37:29'
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. '47.107.154.111'
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_FDCJQ00003'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    usp_freq_set: Union[EmptyStrToNone, int] = None  # Off-grid frequency, e.g. 0
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    vac_high: Union[EmptyStrToNone, float] = None  # Mains voltage upper limit, e.g. 264.5
    vac_low: Union[EmptyStrToNone, float] = None  # Mains voltage lower limit, e.g. 184
    vbat_start_for_discharge: Union[EmptyStrToNone, float] = None  # Lower limit of battery discharge voltage, e.g. 48
    vbat_start_for_charge: Union[EmptyStrToNone, float] = None  # Battery charging upper limit voltage, e.g. 58
    vbat_stop_for_charge: Union[EmptyStrToNone, float] = None  # Battery charging stop voltage, e.g. 5.75
    vbat_stop_for_discharge: Union[EmptyStrToNone, float] = (
        None  # Battery discharge stop voltage, e.g. 4.699999809265137
    )
    vbat_warn_clr: Union[EmptyStrToNone, float] = None  # Low battery voltage recovery point, e.g. 5
    vbat_warning: Union[EmptyStrToNone, float] = None  # Low battery voltage alarm point, e.g. 480
    w_charge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load priority mode charging, e.g. 100
    w_charge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Battery priority mode charging, e.g. 100
    w_discharge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Discharge in load priority mode, e.g. 100
    w_discharge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Grid priority mode discharge, e.g. 5
    baudrate: Union[EmptyStrToNone, int] = None  # Baud rate selection, e.g. 0


class SpaDetails(ApiResponse):
    data: Union[EmptyStrToNone, SpaDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the energy storage machine, e.g. "JPC2827188"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "LHD0847002"


# #####################################################################################################################
# Spa energy overview #################################################################################################


def _spa_energy_overview_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "dataLogSn",
        "bms_fw": "bmsFW",
        "bms_gauge_fcc": "bmsGaugeFCC",
        "bms_gauge_rm": "bmsGaugeRM",
        "bms_max_discharge_curr": "bmsMaxDischgCurr",
        "bms_mcu_version": "bmsMCUVersion",
        "bms_soc": "bmsSOC",
        "bms_soh": "bmsSOH",
        "e_charge1_today": "echarge1Today",
        "e_charge1_total": "echarge1Total",
        "e_discharge1_today": "edischargeToday",
        "e_discharge1_total": "edischargeTotal",
        "e_local_load_today": "elocalLoadToday",
        "e_local_load_total": "elocalLoadTotal",
        "e_to_grid_today": "etoGridToday",
        "e_to_user_today": "etoUserToday",
        "e_to_user_total": "etoUserTotal",
        "e_to_grid_total": "etogridTotal",
        "device_sn": "serialNum",  # align with other endpoints using "deviceSn" instead
        "ups_load_percent": "upsLoadpercent",
        "ups_pf": "upsPF",
    }
    return override.get(snake, to_camel(snake=snake))


class SpaEnergyOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spa_energy_overview_data_to_camel,
    )

    ac_charge_energy_today: Union[EmptyStrToNone, float] = None  # AC daily charge, e.g. 0
    ac_charge_energy_total: Union[EmptyStrToNone, float] = None  # AC total charge, e.g. 0
    ac_charge_power: Union[EmptyStrToNone, float] = None  # AC charging power, e.g. 0
    address: Union[EmptyStrToNone, int] = None  # e.g. 0
    again: Union[EmptyStrToNone, bool] = None  # e.g. False
    alias: Union[EmptyStrToNone, str] = None  # e.g. ''
    battery_temperature: Union[EmptyStrToNone, float] = None  # Battery temperature, e.g. 0
    battery_type: Union[EmptyStrToNone, int] = None  # e.g. 0
    bms_battery_curr: Union[EmptyStrToNone, float] = None  # Battery current, e.g. 0
    bms_battery_temp: Union[EmptyStrToNone, float] = None  # Battery temperature, e.g. 28
    bms_battery_volt: Union[EmptyStrToNone, float] = None  # Battery voltage, e.g. 56.7400016784668
    bms_cell1_volt: Union[EmptyStrToNone, float] = None  # Battery cell 1 voltage, e.g. 3.5480000972747803
    bms_cell2_volt: Union[EmptyStrToNone, float] = None  # Battery single cell 2 voltage, e.g. 3.5480000972747803
    bms_cell3_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.549999952316284
    bms_cell4_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.549999952316284
    bms_cell5_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.549999952316284
    bms_cell6_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.5510001182556152
    bms_cell7_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.549999952316284
    bms_cell8_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.549999952316284
    bms_cell9_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.513000011444092
    bms_cell10_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.549999952316284
    bms_cell11_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.549999952316284
    bms_cell12_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.549999952316284
    bms_cell13_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.5490000247955322
    bms_cell14_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.5490000247955322
    bms_cell15_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.5490000247955322
    bms_cell16_volt: Union[EmptyStrToNone, float] = None  # Battery single cell n voltage, e.g. 3.549999952316284
    bms_constant_volt: Union[EmptyStrToNone, float] = (
        None  # Battery charging constant voltage point, e.g. 56.79999923706055
    )
    bms_cycle_cnt: Union[EmptyStrToNone, int] = None  # Number of battery cycles, e.g. 1331
    bms_delta_volt: Union[EmptyStrToNone, float] = None  # Pressure difference between battery cells, e.g. 38
    bms_error: Union[EmptyStrToNone, int] = None  # Battery failure, e.g. 0
    bms_error_old: Union[EmptyStrToNone, int] = None  # Battery history failure, e.g. 0
    bms_fw: Union[EmptyStrToNone, int] = None  # BMS firmware version number, e.g. 257
    bms_gauge_fcc: Union[EmptyStrToNone, float] = None  # Rated capacity, e.g. 100
    bms_gauge_rm: Union[EmptyStrToNone, float] = None  # System Capacity, e.g. 49.9900016784668
    bms_info: Union[EmptyStrToNone, float] = None  # BMS Information, e.g. 257
    bms_mcu_version: Union[EmptyStrToNone, int] = None  # BMS firmware version, e.g. 512
    bms_max_curr: Union[EmptyStrToNone, float] = None  # Maximum charge and discharge current, e.g. 100
    bms_max_discharge_curr: Union[EmptyStrToNone, float] = None  # Maximum discharge current, e.g. 0
    bms_pack_info: Union[EmptyStrToNone, float] = None  # Battery Pack Information, e.g. 257
    bms_soc: Union[EmptyStrToNone, int] = None  # Battery remaining capacity, e.g. 100
    bms_soh: Union[EmptyStrToNone, int] = None  # Battery health status, e.g. 47
    bms_status: Union[EmptyStrToNone, int] = None  # Battery Status, e.g. 361
    bms_status_old: Union[EmptyStrToNone, int] = None  # Battery history status, e.g. 361
    bms_using_cap: Union[EmptyStrToNone, float] = None  # Battery pack power type, e.g. 5000
    bms_warn_info: Union[EmptyStrToNone, int] = None  # Battery warning information, e.g. 0
    bms_warn_info_old: Union[EmptyStrToNone, int] = None  # Battery historical warning information, e.g. 0
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'QMN0000000000000'
    day: Union[EmptyStrToNone, str] = None  # e.g. ''
    day_map: Union[EmptyStrToNone, Any] = None  # , e.g. None
    eac_today: Union[EmptyStrToNone, float] = None  # e.g. 21.600000381469727
    eac_total: Union[EmptyStrToNone, float] = None  # e.g. 1859.5
    e_charge1_today: Union[EmptyStrToNone, float] = None  # Daily battery charge, e.g. 0.2
    e_charge1_total: Union[EmptyStrToNone, float] = None  # Total battery charge, e.g. 6113.2
    e_discharge1_today: Union[EmptyStrToNone, float] = None  # Daily battery discharge, e.g. 0.4
    e_discharge1_total: Union[EmptyStrToNone, float] = None  # Total battery discharge, e.g. 5540.6
    e_local_load_today: Union[EmptyStrToNone, float] = None  # Daily power consumption of local load, e.g. 0
    e_local_load_total: Union[EmptyStrToNone, float] = None  # Total local load power consumption, e.g. 26980.8
    epv_inverter_today: Union[EmptyStrToNone, float] = (
        None  # Daily electricity generated by photovoltaic inverter, e.g. 0.6
    )
    epv_inverter_total: Union[EmptyStrToNone, float] = (
        None  # Accumulated electricity generated by photovoltaic inverter, e.g. 0.6
    )
    error_code: Union[EmptyStrToNone, int] = None  # error code, e.g. 0
    error_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    e_to_user_today: Union[EmptyStrToNone, float] = None  # Grid Sunrise Electricity, e.g. 0
    e_to_user_total: Union[EmptyStrToNone, float] = None  # Total grid electricity output, e.g. 11991.1
    e_to_grid_today: Union[EmptyStrToNone, float] = None  # Daily grid electricity, e.g. 0.3
    e_to_grid_total: Union[EmptyStrToNone, float] = None  # Total grid power, e.g. 2293
    fac: Union[EmptyStrToNone, float] = None  # grid frequency, e.g. 50.0099983215332
    fault_bit_code: Union[EmptyStrToNone, int] = None  # Inverter fault code, e.g. 0
    fault_code: Union[EmptyStrToNone, int] = None  # Inverter fault code, e.g. 0
    lost: Union[EmptyStrToNone, bool] = None  # e.g. True
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 2503.8
    pac1: Union[EmptyStrToNone, float] = None  # Inverter output apparent power, e.g. 0
    pac_to_grid_r: Union[EmptyStrToNone, float] = None  # Grid reverse current power, e.g. 38.6
    pac_to_grid_total: Union[EmptyStrToNone, float] = None  # Total grid countercurrent power, e.g. 38.6
    pac_to_user_r: Union[EmptyStrToNone, float] = None  # Grid downstream power, e.g. 0
    pac_to_user_total: Union[EmptyStrToNone, float] = None  # Total downstream power of the grid, e.g. 0
    pcharge1: Union[EmptyStrToNone, float] = None  # Battery charging power, e.g. 0
    pdischarge1: Union[EmptyStrToNone, float] = None  # Battery discharge power, e.g. 16.5
    plocal_load_r: Union[EmptyStrToNone, float] = None  # Local load power consumption, e.g. 0
    plocal_load_total: Union[EmptyStrToNone, float] = None  # Total local load power consumption, e.g. 0
    ppv_inverter: Union[EmptyStrToNone, float] = None  # Photovoltaic inverter power generation, e.g. 6.8
    priority_choose: Union[EmptyStrToNone, float] = None  # e.g. 2
    device_sn: Union[EmptyStrToNone, str] = None  # e.g. 'LHD0847002'
    soc: Union[EmptyStrToNone, float] = None  # remaining battery capacity, e.g. 100
    soc_text: Union[EmptyStrToNone, str] = None  # e.g. '100%'
    spa_bean: Union[EmptyStrToNone, Any] = None  # e.g. None,
    status: Union[EmptyStrToNone, int] = None  # Mix Status 0 = waiting, 1 = normal, 2 = fault, e.g. 5
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'PV Bat Online'
    sys_en: Union[EmptyStrToNone, int] = None  # System enable bit, e.g. 17056
    sys_fault_word: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word1: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word2: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word3: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word4: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word5: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word6: Union[EmptyStrToNone, int] = None  # e.g. 0
    sys_fault_word7: Union[EmptyStrToNone, int] = None  # e.g. 256
    temp1: Union[EmptyStrToNone, float] = None  # Temperature 1, e.g. 34
    temp2: Union[EmptyStrToNone, float] = None  # Temperature 2, e.g. 33.099998474121094
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-09 14:52:39'
    time_total: Union[EmptyStrToNone, float] = None  # Total running time, e.g. 1625146.9
    ups_fac: Union[EmptyStrToNone, float] = None  # Emergency power frequency, e.g. 0
    ups_load_percent: Union[EmptyStrToNone, float] = None  # Emergency output load rate, e.g. 0
    ups_pf: Union[EmptyStrToNone, float] = None  # Emergency output power factor, e.g. 1000
    ups_pac1: Union[EmptyStrToNone, float] = None  # Emergency output apparent power, e.g. 0
    ups_vac1: Union[EmptyStrToNone, float] = None  # Emergency voltage, e.g. 0
    uw_sys_work_mode: Union[EmptyStrToNone, int] = None  # System working mode, e.g. 5
    v_bat_dsp: Union[EmptyStrToNone, float] = None  # Battery voltage collected by DSP, e.g. 0
    v_bus1: Union[EmptyStrToNone, float] = None  # Bus 1 voltage, e.g. 0
    v_bus2: Union[EmptyStrToNone, float] = None  # Bus 2 voltage, e.g. 0
    vac1: Union[EmptyStrToNone, float] = None  # Grid voltage, e.g. 219.89999389648438
    vbat: Union[EmptyStrToNone, float] = None  # battery voltage, e.g. 56.70000076293945
    warn_code: Union[EmptyStrToNone, int] = None  # e.g. 220
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the data sent has its own time, e.g. False


def _spa_energy_overview_to_camel(snake: str) -> str:
    override = {
        "device_sn": "spa_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class SpaEnergyOverview(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spa_energy_overview_to_camel,
    )

    data: Union[EmptyStrToNone, SpaEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "JPC2827188"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "LHD0847002"


# #####################################################################################################################
# Spa energy overview multiple ########################################################################################


class SpaEnergyOverviewMultipleItem(ApiModel):
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    data: Union[EmptyStrToNone, SpaEnergyOverviewData] = None


class SpaEnergyOverviewMultiple(ApiResponse):
    data: List[SpaEnergyOverviewMultipleItem] = None
    page_num: Union[EmptyStrToNone, int] = None  # Page number, e.g. 1


# #####################################################################################################################
# Spa energy history ##################################################################################################


def _spa_energy_history_data_to_camel(snake: str) -> str:
    override = {
        "device_sn": "spa_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class SpaEnergyHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spa_energy_history_data_to_camel,
    )

    count: int  # Total Records
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. ""SATA818009""
    datas: List[SpaEnergyOverviewData]
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. ""TLMAX00B01""
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21


class SpaEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, SpaEnergyHistoryData] = None


# #####################################################################################################################
# Spa alarms ##########################################################################################################


class SpaAlarm(ApiModel):
    alarm_code: Union[EmptyStrToNone, int] = None  # alarm code, e.g. 25
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    end_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm start time, e.g. "2019-03-09 09:55:55.0"
    start_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm end time, e.g. "2019-03-09 09:55:55.0"
    alarm_message: Union[EmptyStrToNone, str] = None  # alarm information, e.g. "No utility."


def _spa_alarms_data_to_camel(snake: str) -> str:
    override = {
        "device_sn": "spa_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class SpaAlarmsData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_spa_alarms_data_to_camel,
    )

    count: int  # Total Records
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "SARN744005"
    alarms: List[SpaAlarm]


class SpaAlarms(ApiResponse):
    data: Union[EmptyStrToNone, SpaAlarmsData] = None
