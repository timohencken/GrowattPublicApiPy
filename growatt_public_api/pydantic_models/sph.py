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
# Sph setting read ####################################################################################################


class SphSettingRead(ApiResponse):
    data: Union[EmptyStrToNone, str] = None  # current setting / register value


# #####################################################################################################################
# Sph setting write ###################################################################################################


class SphSettingWrite(ApiResponse):
    data: Union[EmptyStrToNone, Any] = None


# #####################################################################################################################
# Sph details #########################################################################################################


def _sph_detail_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "address": "addr",
        "bat_aging_test_step": "bagingTestStep",
        "buck_ups_volt_set": "buckUPSVoltSet",
        "datalogger_sn": "dataLogSn",
        "discharge_power_command": "disChargePowerCommand",
        "parent_id": "parentID",
        "pf_cmd_memory_state": "pfCMDmemoryState",
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


class SphDetailData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sph_detail_data_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    ac_charge_enable: Union[EmptyStrToNone, bool] = None  # AC charging enable, e.g. 1
    active_rate: Union[EmptyStrToNone, float] = None  # Active power, e.g. 1
    address: Union[EmptyStrToNone, int] = None  # Inverter address, e.g. 1
    alias: Union[EmptyStrToNone, str] = None  # alias, e.g. 'FDCJQ00003'
    backflow_setting: Union[EmptyStrToNone, str] = None  # Backflow prevention setting, e.g. ''
    bat_aging_test_step: Union[EmptyStrToNone, int] = (
        None  # battery self-test (0: default, 1: charge, 2: discharge), e.g. 0
    )
    bat_first_switch1: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_first_switch2: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_first_switch3: Union[EmptyStrToNone, int] = None  # e.g. 0
    bat_parallel_num: Union[EmptyStrToNone, int] = None  # Number of parallel cells, e.g. 0
    bat_series_num: Union[EmptyStrToNone, int] = None  # Number of cells in series, e.g. 0
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
    cc_current: Union[EmptyStrToNone, float] = None  # e.g. 0
    charge_power_command: Union[EmptyStrToNone, int] = None  # Charging power setting, e.g. 100
    charge_time1: Union[EmptyStrToNone, str] = None  # e.g. ''
    charge_time2: Union[EmptyStrToNone, str] = None  # e.g. ''
    charge_time3: Union[EmptyStrToNone, str] = None  # e.g. ''
    children: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    com_address: Union[EmptyStrToNone, int] = None  # Mailing address, e.g. 1
    communication_version: Union[EmptyStrToNone, str] = None  # Communication version number, e.g. 'GJAA-0003'
    country_selected: Union[EmptyStrToNone, int] = None  # country selection, e.g. 0
    cv_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'VC51030322020001'
    device_type: Union[EmptyStrToNone, int] = None  # 0: Mix6k, 1: Mix4-10k, e.g. 0
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
    export_limit: Union[EmptyStrToNone, int] = None  # Backflow prevention enable, e.g. 0
    export_limit_power_rate: Union[EmptyStrToNone, float] = None  # Backflow prevention, e.g. 0
    failsafe: Union[EmptyStrToNone, int] = None  # e.g. 0
    float_charge_current_limit: Union[EmptyStrToNone, float] = None  # float charge current limit, e.g. 600
    forced_charge_stop_switch1: Union[EmptyStrToNone, bool] = None  # Charge 1 enable bit, e.g. 1
    forced_charge_stop_switch2: Union[EmptyStrToNone, bool] = None  # Charge 2 enable bit, e.g. 1
    forced_charge_stop_switch3: Union[EmptyStrToNone, bool] = None  # Charge 3 enable bit, e.g. 1
    forced_charge_time_start1: Union[EmptyStrToNone, ForcedTime] = None  # Charge 1 start time, e.g. '18:0'
    forced_charge_time_start2: Union[EmptyStrToNone, ForcedTime] = None  # Charge 2 start time, e.g. '21:30'
    forced_charge_time_start3: Union[EmptyStrToNone, ForcedTime] = None  # Charge 3 start time, e.g. '3:0'
    forced_charge_time_stop1: Union[EmptyStrToNone, ForcedTime] = None  # Charge 1 stop time, e.g. '19:30'
    forced_charge_time_stop2: Union[EmptyStrToNone, ForcedTime] = None  # Charge 2 stop time, e.g. '23:0'
    forced_charge_time_stop3: Union[EmptyStrToNone, ForcedTime] = None  # Charge 3 stop time, e.g. '4:30'
    forced_discharge_stop_switch1: Union[EmptyStrToNone, bool] = None  # Discharge 1 enable bit, e.g. 1
    forced_discharge_stop_switch2: Union[EmptyStrToNone, bool] = None  # Discharge 2 enable bit, e.g. 1
    forced_discharge_stop_switch3: Union[EmptyStrToNone, bool] = None  # Discharge 3 enable bit, e.g. 1
    forced_discharge_time_start1: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 1 start time, e.g. '0:0'
    forced_discharge_time_start2: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 2 start time, e.g. '0:0'
    forced_discharge_time_start3: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 3 start time, e.g. '0:0'
    forced_discharge_time_stop1: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 1 stop time, e.g. '0:0'
    forced_discharge_time_stop2: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 2 stop time, e.g. '0:0'
    forced_discharge_time_stop3: Union[EmptyStrToNone, ForcedTime] = None  # Discharge 3 stop time, e.g. '0:0'
    fw_version: Union[EmptyStrToNone, str] = None  # Inverter version, e.g. 'RA1.0'
    grid_first_switch1: Union[EmptyStrToNone, bool] = None  # e.g. 0
    grid_first_switch2: Union[EmptyStrToNone, bool] = None  # e.g. 0
    grid_first_switch3: Union[EmptyStrToNone, bool] = None  # e.g. 0
    group_id: Union[EmptyStrToNone, int] = None  # e.g. -1
    id: Union[EmptyStrToNone, int] = None  # e.g. 0
    img_path: Union[EmptyStrToNone, str] = None  # e.g. './css/img/status_gray.gif'
    inner_version: Union[EmptyStrToNone, str] = None  # Internal version number, e.g. 'GJAA03xx'
    last_update_time: Union[EmptyStrToNone, GrowattTime] = (
        None  # Last update time, e.g. {'date': 12, 'day': 2, 'hours': 16, 'minutes': 46, 'month': 3, 'seconds': 22, 'time': 1649753182000, 'timezoneOffset': -480, 'year': 122}
    )
    last_update_time_text: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-12 16:46:22'
    lcd_language: Union[EmptyStrToNone, int] = None  # e.g. 1
    level: Union[EmptyStrToNone, int] = None  # e.g. 4
    location: Union[EmptyStrToNone, str] = None  # address, e.g. ''
    lost: Union[EmptyStrToNone, bool] = None  # Device online status (0: online, 1: disconnected), e.g. True
    lv_voltage: Union[EmptyStrToNone, float] = None  # e.g. 0
    manufacturer: Union[EmptyStrToNone, str] = None  # Manufacturer Code, e.g. 'New Energy'
    mix_ac_discharge_frequency: Union[EmptyStrToNone, float] = None  # Off-grid frequency, e.g. ''
    mix_ac_discharge_voltage: Union[EmptyStrToNone, float] = None  # Off-grid voltage, e.g. ''
    mix_off_grid_enable: Union[EmptyStrToNone, bool] = None  # Off-grid enable, e.g. ''
    modbus_version: Union[EmptyStrToNone, int] = None  # MODBUS version, e.g. 305
    model: Union[EmptyStrToNone, int] = None  # model, e.g. 2666130979655057522
    model_text: Union[EmptyStrToNone, str] = None  # model, e.g. 'S25B00D00T00P0FU01M0072'
    on_off: Union[EmptyStrToNone, bool] = None  # Switch machine, e.g. 0
    p_charge: Union[EmptyStrToNone, float] = None  # e.g. 0
    p_discharge: Union[EmptyStrToNone, float] = None  # e.g. 0
    parent_id: Union[EmptyStrToNone, str] = None  # e.g. 'LIST_VC51030322020001_22'
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
    pv_pf_cmd_memory_state_mix: Union[EmptyStrToNone, bool] = (
        None  # mix Does the inverter store the following commands, e.g. 1
    )
    pv_power_factor: Union[EmptyStrToNone, float] = None  # Set PF value, e.g. ''
    pv_reactive_p_rate: Union[EmptyStrToNone, float] = None  # Set reactive power, e.g. ''
    pv_reactive_p_rate_two: Union[EmptyStrToNone, float] = None  # No power capacity/inductive, e.g. ''
    reactive_rate: Union[EmptyStrToNone, float] = None  # Reactive power, e.g. 100
    record: Union[EmptyStrToNone, Any] = None  # e.g. None
    serial_num: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'FDCJQ00003'
    status: Union[EmptyStrToNone, int] = (
        None  # Device status (0: waiting, 1: self-check, 3: failure, 4: upgrade, 5, 6, 7, 8: normal mode), e.g. 0
    )
    status_text: Union[EmptyStrToNone, str] = None  # e.g. 'tlx.status.operating'
    sys_time: Union[EmptyStrToNone, datetime.datetime] = None  # System Time, e.g. '2019-03-05 10:37:29'
    tcp_server_ip: Union[EmptyStrToNone, str] = None  # Server address, e.g. '47.107.154.111'
    tree_id: Union[EmptyStrToNone, str] = None  # e.g. 'ST_FDCJQ00003'
    tree_name: Union[EmptyStrToNone, str] = None  # e.g. 'FDCJQ00003'
    under_excited: Union[EmptyStrToNone, int] = None  # Capacitive or Perceptual, e.g. 0
    updating: Union[EmptyStrToNone, bool] = None  # e.g. False
    user_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    usp_freq_set: Union[EmptyStrToNone, int] = None  # Off-grid frequency, e.g. 0
    vbat_start_for_discharge: Union[EmptyStrToNone, float] = None  # Lower limit of battery discharge voltage, e.g. 48
    vbat_start_for_charge: Union[EmptyStrToNone, float] = None  # Battery charging upper limit voltage, e.g. 58
    vbat_stop_for_charge: Union[EmptyStrToNone, float] = None  # Battery charging stop voltage, e.g. 5.75
    vbat_stop_for_discharge: Union[EmptyStrToNone, float] = (
        None  # Battery discharge stop voltage, e.g. 4.699999809265137
    )
    vbat_warn_clr: Union[EmptyStrToNone, float] = None  # Low battery voltage recovery point, e.g. 5
    vbat_warning: Union[EmptyStrToNone, float] = None  # Low battery voltage alarm point, e.g. 480
    vnormal: Union[EmptyStrToNone, float] = None  # Rated PV voltage, e.g. 360
    voltage_high_limit: Union[EmptyStrToNone, float] = None  # Mains voltage upper limit, e.g. 263
    voltage_low_limit: Union[EmptyStrToNone, float] = None  # Mains voltage lower limit, e.g. 186
    w_charge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Load priority mode charging, e.g. 100
    w_charge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Battery priority mode charging, e.g. 100
    w_discharge_soc_low_limit1: Union[EmptyStrToNone, int] = None  # Discharge in load priority mode, e.g. 100
    w_discharge_soc_low_limit2: Union[EmptyStrToNone, int] = None  # Grid priority mode discharge, e.g. 5
    baudrate: Union[EmptyStrToNone, int] = None  # Baud rate selection, e.g. 0


class SphDetails(ApiResponse):
    data: Union[EmptyStrToNone, SphDetailData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN of the energy storage machine, e.g. "ZT00100001"
    )
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"


# #####################################################################################################################
# Sph energy overview #################################################################################################


def _sph_energy_overview_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "datalogger_sn": "dataLogSn",
        "real_op_percent": "realOPPercent",
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


class SphEnergyOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sph_energy_overview_data_to_camel,
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
    eps_vac2: Union[EmptyStrToNone, float] = None  # S-phase voltage on off-grid side, e.g.  0
    eps_vac3: Union[EmptyStrToNone, float] = None  # T-phase voltage on off-grid side, e.g. 0
    epv1_today: Union[EmptyStrToNone, float] = None  # e.g. 13.199999809265137
    epv1_total: Union[EmptyStrToNone, float] = None  # e.g. 926.6
    epv2_today: Union[EmptyStrToNone, float] = None  # e.g. 8.199999809265137
    epv2_total: Union[EmptyStrToNone, float] = None  # e.g. 906.4
    epv_total: Union[EmptyStrToNone, float] = None  # e.g. 0
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
    mix_bean: Union[EmptyStrToNone, Any] = None
    pac: Union[EmptyStrToNone, float] = None  # Inverter output power, e.g. 2503.8
    pac1: Union[EmptyStrToNone, float] = None  # Inverter output apparent power, e.g. 0
    pac2: Union[EmptyStrToNone, float] = None  # AC side power, e.g. 0
    pac3: Union[EmptyStrToNone, float] = None  # AC side power, e.g. 0
    pac_to_grid_r: Union[EmptyStrToNone, float] = None  # Grid reverse current power, e.g. 38.6
    pac_to_grid_total: Union[EmptyStrToNone, float] = None  # Total grid countercurrent power, e.g. 38.6
    pac_to_user_r: Union[EmptyStrToNone, float] = None  # Grid downstream power, e.g. 0
    pac_to_user_total: Union[EmptyStrToNone, float] = None  # Total downstream power of the grid, e.g. 0
    pcharge1: Union[EmptyStrToNone, float] = None  # Battery charging power, e.g. 0
    pdischarge1: Union[EmptyStrToNone, float] = None  # Battery discharge power, e.g. 16.5
    plocal_load_r: Union[EmptyStrToNone, float] = None  # Local load power consumption, e.g. 0
    plocal_load_total: Union[EmptyStrToNone, float] = None  # Total local load power consumption, e.g. 0
    ppv: Union[EmptyStrToNone, float] = None  # PV input power, e.g. 1058
    ppv1: Union[EmptyStrToNone, float] = None  # PV1 input power, e.g. 1058
    ppv2: Union[EmptyStrToNone, float] = None  # PV2 input power, e.g. 1058
    ppv_text: Union[EmptyStrToNone, str] = None  # e.g. '3.9 W'
    priority_choose: Union[EmptyStrToNone, float] = None  # e.g. 0
    device_sn: Union[EmptyStrToNone, str] = None  # e.g. 'BNE9A5100D'
    soc: Union[EmptyStrToNone, float] = None  # remaining battery capacity, e.g. 100
    soc_text: Union[EmptyStrToNone, str] = None  # e.g. '100%'
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
    temp3: Union[EmptyStrToNone, float] = None  # Temperature 3, e.g. 33.099998474121094
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2022-04-09 14:52:39'
    time_total: Union[EmptyStrToNone, float] = None  # Total running time, e.g. 1625146.9
    ups_fac: Union[EmptyStrToNone, float] = None  # Emergency power frequency, e.g. 0
    ups_load_percent: Union[EmptyStrToNone, float] = None  # Emergency output load rate, e.g. 0
    ups_pf: Union[EmptyStrToNone, float] = None  # Emergency output power factor, e.g. 1000
    ups_pac1: Union[EmptyStrToNone, float] = None  # Emergency output apparent power, e.g. 0
    ups_pac2: Union[EmptyStrToNone, float] = None  # Off-grid side power, e.g. 0
    ups_pac3: Union[EmptyStrToNone, float] = None  # Off-grid side power, e.g. 0
    ups_vac1: Union[EmptyStrToNone, float] = None  # Emergency voltage, e.g. 0
    uw_sys_work_mode: Union[EmptyStrToNone, int] = None  # System working mode, e.g. 5
    v_bat_dsp: Union[EmptyStrToNone, float] = None  # Battery voltage collected by DSP, e.g. 0
    v_bus1: Union[EmptyStrToNone, float] = None  # Bus 1 voltage, e.g. 0
    v_bus2: Union[EmptyStrToNone, float] = None  # Bus 2 voltage, e.g. 0
    vac1: Union[EmptyStrToNone, float] = None  # Grid voltage, e.g. 219.89999389648438
    vac2: Union[EmptyStrToNone, float] = None  # AC side S phase voltage, e.g. 0
    vac3: Union[EmptyStrToNone, float] = None  # AC side T phase voltage, e.g. 0
    vbat: Union[EmptyStrToNone, float] = None  # battery voltage, e.g. 56.70000076293945
    vpv1: Union[EmptyStrToNone, float] = None  # PV1 input voltage, e.g. 0
    vpv2: Union[EmptyStrToNone, float] = None
    warn_code: Union[EmptyStrToNone, int] = None  # e.g. 220
    warn_text: Union[EmptyStrToNone, str] = None  # e.g. 'Unknown'
    with_time: Union[EmptyStrToNone, bool] = None  # Whether the data sent has its own time, e.g. False


def _sph_energy_overview_to_camel(snake: str) -> str:
    override = {
        "device_sn": "mix_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class SphEnergyOverview(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sph_energy_overview_to_camel,
    )

    data: Union[EmptyStrToNone, SphEnergyOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "BQC0733010"
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "SARN744005"


# #####################################################################################################################
# Sph energy overview multiple ########################################################################################


class SphEnergyOverviewMultipleItem(ApiModel):
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "CRAZT00001"
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "ZT00100001"
    data: Union[EmptyStrToNone, SphEnergyOverviewData] = None


class SphEnergyOverviewMultiple(ApiResponse):
    data: List[SphEnergyOverviewMultipleItem] = None
    page_num: Union[EmptyStrToNone, int] = None  # Page number, e.g. 1


# #####################################################################################################################
# Sph energy history ##################################################################################################


def _sph_energy_history_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "mix_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class SphEnergyHistoryData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sph_energy_history_data_to_camel,
    )

    count: int  # Total Records
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. ""SATA818009""
    datas: List[SphEnergyOverviewData]
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. ""TLMAX00B01""
    next_page_start_id: Union[EmptyStrToNone, int] = None  # 21


class SphEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, SphEnergyHistoryData] = None


# #####################################################################################################################
# Sph alarms ##########################################################################################################


class SphAlarm(ApiModel):
    alarm_code: Union[EmptyStrToNone, int] = None  # alarm code, e.g. 25
    status: Union[EmptyStrToNone, int] = None  # e.g. 1
    end_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm start time, e.g. "2019-03-09 09:55:55.0"
    start_time: Union[EmptyStrToNone, datetime.datetime] = None  # Alarm end time, e.g. "2019-03-09 09:55:55.0"
    alarm_message: Union[EmptyStrToNone, str] = None  # alarm information, e.g. "No utility."


def _sph_alarms_data_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "device_sn": "mix_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class SphAlarmsData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_sph_alarms_data_to_camel,
    )

    count: int  # Total Records
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. "SARN744005"
    alarms: List[SphAlarm]


class SphAlarms(ApiResponse):
    data: Union[EmptyStrToNone, SphAlarmsData] = None
