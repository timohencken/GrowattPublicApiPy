import datetime
from typing import List, Union, Any, Dict

from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from .api_model import (
    ApiResponse,
    ApiModel,
    EmptyStrToNone,
    GrowattTime,
)

# #####################################################################################################################
# Add datalogger ######################################################################################################


class DataloggerAdd(ApiResponse):
    data: Union[EmptyStrToNone, str] = None


# #####################################################################################################################
# Delete datalogger ###################################################################################################


class DataloggerDelete(ApiResponse):
    data: Union[EmptyStrToNone, str] = None


# #####################################################################################################################
# Device list #########################################################################################################


class DeviceData(ApiModel):
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The collector SN corresponding to the device, e.g. 'QMN000BZP0000000'
    )
    device_id: Union[EmptyStrToNone, int] = None
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'BZP0000000'
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = (
        None  # Last data received time, e.g. '2025-02-24 17:28:13'
    )
    lost: Union[EmptyStrToNone, bool] = None  # whether the device is online or not (False=online, True=disconnected)
    manufacturer: Union[EmptyStrToNone, str] = None  # Equipment manufacturer, e.g. 'Growatt'
    model: Union[EmptyStrToNone, str] = None  # device model, e.g. 'S00B00D00T00P00U00M0000'
    status: Union[EmptyStrToNone, int] = (
        None  # Device status, if the device is 1 (inverter), then status (0: disconnected, 1: online, 2: standby, 3; fault, all others are offline), if the device is 2 ( Energy storage machine), then status (0: standby, 1: charging, 2: discharging, 3: fault, 4: burning, others are offline), if the device is 4 (Max device), then status(0: Standby, 1: online, 2: standby, 3; failure, all others are offline); if the device is 6 (Spa) Status 0: waiting mode 1: self-check mode, 3: failure mode, 4: upgrading, 5 , 6, 7, 8: normal mode, all others are offline; if the device is 5 (Mix) Status 0: waiting mode, 1: self-check mode, 3: failure mode, 4: upgrading, 5, 6, 7 , 8: Normal mode, all others are offline; if the device is in 7 (MIN) state, status (0 disconnected, 1: online, 2: standby, 3; failure, all others are offline)
    )
    type: Union[EmptyStrToNone, int] = (
        None  # Equipment type: 1=inverter (including MAX), 2=storage, 3=other, 4=max, 5=sph, 6=spa, 7=min, 8=pcs, 9=hps, 10=pbd
    )


class DeviceListData(ApiModel):
    count: int  # Total number of devices
    devices: List[DeviceData]


class DeviceList(ApiResponse):
    data: Union[EmptyStrToNone, DeviceListData] = None


# #####################################################################################################################
# Datalogger list #####################################################################################################


def _plant_two_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "e_year_money_text": "EYearMoneyText",
        "latitude_d": "latitude_d",
        "latitude_f": "latitude_f",
        "latitude_m": "latitude_m",
        "longitude_d": "longitude_d",
        "longitude_f": "longitude_f",
        "longitude_m": "longitude_m",
        "map_area_id": "map_areaId",
        "map_city_id": "map_cityId",
        "map_country_id": "map_countryId",
        "map_province_id": "map_provinceId",
        "parent_id": "parentID",
        "plant_lat": "plant_lat",
        "plant_lng": "plant_lng",
        "storage_battery_percentage": "storage_BattoryPercentage",
        "storage_today_to_grid": "storage_TodayToGrid",
        "storage_today_to_user": "storage_TodayToUser",
        "storage_total_to_grid": "storage_TotalToGrid",
        "storage_total_to_user": "storage_TotalToUser",
        "storage_e_charge_today": "storage_eChargeToday",
        "storage_e_discharge_today": "storage_eDisChargeToday",
        "tree_id": "treeID",
    }
    return override.get(snake, to_camel(snake=snake))


class PlantTwo(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_plant_two_to_camel,
    )

    e_year_money_text: Union[EmptyStrToNone, float] = None  # '0'
    alarm_value: Union[EmptyStrToNone, int] = None  # 0
    alias: Union[EmptyStrToNone, str] = None  # 'Balkondach'
    children: List[Any]  # []
    city: Union[EmptyStrToNone, str] = None  # 'Shenzen'
    company_name: Union[EmptyStrToNone, str] = None  # ''
    country: Union[EmptyStrToNone, str] = None  # ''
    create_date: GrowattTime
    create_date_text: Union[EmptyStrToNone, datetime.date] = None  # '2024-11-29'
    create_date_text_a: Union[EmptyStrToNone, str] = None  # ''
    current_pac: Union[EmptyStrToNone, float] = None  # 0
    current_pac_str: Union[EmptyStrToNone, str] = None  # '0kW'
    current_pac_txt: Union[EmptyStrToNone, float] = None  # '0'
    data_log_list: List[Any]  # []
    default_plant: Union[EmptyStrToNone, bool] = None  # False
    design_company: Union[EmptyStrToNone, str] = None  # ''
    device_count: Union[EmptyStrToNone, int] = None  # 1
    e_today: Union[EmptyStrToNone, float] = None  # 0
    e_total: Union[EmptyStrToNone, float] = None  # 3.4000000953674316
    emonth_co2_text: Union[EmptyStrToNone, float] = None  # '0'
    emonth_coal_text: Union[EmptyStrToNone, float] = None  # '0'
    emonth_money_text: Union[EmptyStrToNone, float] = None  # '0'
    emonth_so2_text: Union[EmptyStrToNone, float] = None  # '0'
    energy_month: Union[EmptyStrToNone, float] = None  # 0
    energy_year: Union[EmptyStrToNone, float] = None  # 0
    env_temp: Union[EmptyStrToNone, float] = None  # 0
    etoday_co2_text: Union[EmptyStrToNone, float] = None  # '0'
    etoday_coal_text: Union[EmptyStrToNone, float] = None  # '0'
    etoday_money: Union[EmptyStrToNone, float] = None  # 0
    etoday_money_text: Union[EmptyStrToNone, float] = None  # '0'
    etoday_so2_text: Union[EmptyStrToNone, float] = None  # '0'
    etotal_co2_text: Union[EmptyStrToNone, float] = None  # '3.4'
    etotal_coal_text: Union[EmptyStrToNone, float] = None  # '1.4'
    etotal_formula_tree_text: Union[EmptyStrToNone, float] = None  # '0.19'
    etotal_money: Union[EmptyStrToNone, float] = None  # 1.0200001001358032
    etotal_money_text: Union[EmptyStrToNone, float] = None  # '1'
    etotal_so2_text: Union[EmptyStrToNone, float] = None  # '0.1'
    event_mess_bean_list: List[Any]  # []
    fixed_power_price: Union[EmptyStrToNone, float] = None  # 0
    flat_period_price: Union[EmptyStrToNone, float] = None  # 0
    formula_co2: Union[EmptyStrToNone, float] = None  # 0
    formula_coal: Union[EmptyStrToNone, float] = None  # 0
    formula_money: Union[EmptyStrToNone, float] = None  # 0.30000001192092896
    formula_money_str: Union[EmptyStrToNone, float] = None  # ''
    formula_money_unit_id: Union[EmptyStrToNone, str] = None  # 'EUR'
    formula_so2: Union[EmptyStrToNone, float] = None  # 0
    formula_tree: Union[EmptyStrToNone, float] = None  # 0
    grid_company: Union[EmptyStrToNone, str] = None  # ''
    grid_port: Union[EmptyStrToNone, str] = None  # ''
    grid_server_url: Union[EmptyStrToNone, str] = None  # ''
    has_device_on_line: Union[EmptyStrToNone, bool] = None  # 0
    has_storage: Union[EmptyStrToNone, bool] = None  # 0
    id: Union[EmptyStrToNone, int] = None  # Plant ID, e.g. 9900000
    img_path: Union[EmptyStrToNone, str] = None  # 'css/img/plant.gif'
    install_map_name: Union[EmptyStrToNone, str] = None  # ''
    irradiance: Union[EmptyStrToNone, float] = None  # 0
    is_share: Union[EmptyStrToNone, bool] = None  # False
    latitude_text: Union[EmptyStrToNone, str] = None  # 'null°null′null″'
    latitude_d: Union[EmptyStrToNone, str] = None  # ''
    latitude_f: Union[EmptyStrToNone, str] = None  # ''
    latitude_m: Union[EmptyStrToNone, str] = None  # ''
    level: Union[EmptyStrToNone, int] = None  # 1
    location_img_name: Union[EmptyStrToNone, str] = None  # ''
    logo_img_name: Union[EmptyStrToNone, str] = None  # ''
    longitude_text: Union[EmptyStrToNone, str] = None  # 'null°null′null″'
    longitude_d: Union[EmptyStrToNone, str] = None  # ''
    longitude_f: Union[EmptyStrToNone, str] = None  # ''
    longitude_m: Union[EmptyStrToNone, str] = None  # ''
    map_city: Union[EmptyStrToNone, str] = None  # ''
    map_lat: Union[EmptyStrToNone, str] = None  # ''
    map_lng: Union[EmptyStrToNone, str] = None  # ''
    map_area_id: Union[EmptyStrToNone, int] = None  # 0
    map_city_id: Union[EmptyStrToNone, int] = None  # 0
    map_country_id: Union[EmptyStrToNone, int] = None  # 0
    map_province_id: Union[EmptyStrToNone, int] = None  # 0
    money_unit_text: Union[EmptyStrToNone, str] = None  # '€'
    nominal_power: Union[EmptyStrToNone, int] = None  # peak power (Wp), e.g. 800
    nominal_power_str: Union[EmptyStrToNone, str] = None  # '0.8kWp'
    on_line_env_count: Union[EmptyStrToNone, int] = None  # 0
    pair_view_user_account: Union[EmptyStrToNone, str] = None  # ''
    panel_temp: Union[EmptyStrToNone, float] = None  # 0
    param_bean: Any  # None
    parent_id: Union[EmptyStrToNone, str] = None  # ''
    peak_period_price: Union[EmptyStrToNone, float] = None  # 0
    phone_num: Union[EmptyStrToNone, str] = None  # ''
    plant_address: Union[EmptyStrToNone, str] = None  # street, number
    plant_from_bean: Any  # None
    plant_img_name: Union[EmptyStrToNone, str] = None  # ''
    plant_name: Union[EmptyStrToNone, str] = None  # 'Balkondach'
    plant_nmi: Union[EmptyStrToNone, str] = None  # ''
    plant_type: Union[EmptyStrToNone, int] = None  # 0
    plant_lat: Union[EmptyStrToNone, float] = None  # ''
    plant_lng: Union[EmptyStrToNone, float] = None  # ''
    pr_month: Union[EmptyStrToNone, int] = None  # ''
    pr_today: Union[EmptyStrToNone, int] = None  # ''
    protocol_id: Union[EmptyStrToNone, str] = None  # ''
    remark: Union[EmptyStrToNone, str] = None  # ''
    status: Union[EmptyStrToNone, int] = None  # 0
    storage_battery_percentage: Union[EmptyStrToNone, float] = None  # 0
    storage_today_to_grid: Union[EmptyStrToNone, float] = None  # 0
    storage_today_to_user: Union[EmptyStrToNone, float] = None  # 0
    storage_total_to_grid: Union[EmptyStrToNone, float] = None  # 0
    storage_total_to_user: Union[EmptyStrToNone, float] = None  # 0
    storage_e_charge_today: Union[EmptyStrToNone, float] = None  # 0
    storage_e_discharge_today: Union[EmptyStrToNone, float] = None  # 0
    temp_type: Union[EmptyStrToNone, int] = None  # 0
    timezone: Union[EmptyStrToNone, float] = None  # 1
    timezone_text: Union[EmptyStrToNone, str] = None  # 'GMT 1'
    tree_id: Union[EmptyStrToNone, str] = None  # 'PLANT_0000000'
    tree_name: Union[EmptyStrToNone, str] = None  # 'Balkondach'
    unit_map: Union[EmptyStrToNone, Any] = None  # None
    user_account: Union[EmptyStrToNone, str] = None  # username
    user_bean: Union[EmptyStrToNone, Any] = None  # None
    valley_period_price: Union[EmptyStrToNone, float] = None  # 0
    wind_angle: Union[EmptyStrToNone, float] = None  # 0
    wind_speed: Union[EmptyStrToNone, float] = None  # 0


def _datalogger_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "sn",
    }
    return override.get(snake, to_camel(snake=snake))


class DataloggerData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_datalogger_data_to_camel,
        protected_namespaces=(),  # allow model_* keywords
    )

    last_update_time: Union[EmptyStrToNone, GrowattTime] = (
        None  # Last data received time, e.g. {'date': 25, 'day': 2, 'hours': 0, 'minutes': 32, 'month': 1, 'seconds': 1, 'time': 1740414721500, 'timezoneOffset': -480, 'year': 125}
    )
    lost: Union[EmptyStrToNone, bool] = None  # True
    manufacturer: Union[EmptyStrToNone, str] = None  # collector manufacturer, e.g. 'Growatt'
    model: Union[EmptyStrToNone, str] = None  # 'ShineWeFi'
    netmode: Union[EmptyStrToNone, str] = None  # NONE | WIFI | 4G | LAN, e.g. 'NONE'
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Collector SN, e.g. 'QMN000BZP0000000'
    type: Union[EmptyStrToNone, int] = None  # Collector type, e.g. 0


class DataloggerListData(ApiModel):
    count: int  # Total number of collectors
    dataloggers: List[DataloggerData]
    peak_power_actual: PlantTwo


class DataloggerList(ApiResponse):
    data: Union[EmptyStrToNone, DataloggerListData] = None


# #####################################################################################################################
# Device type info ####################################################################################################


class DeviceTypeInfo(ApiModel):
    device_type: Union[EmptyStrToNone, int] = (
        None  # 0=???, 16=inverter, 17=SPH, 18=MAX, 19=SPA, 22=MIN, 81=pcs, 82=HPS 83=PDB, 96=storage
    )
    dtc: Union[EmptyStrToNone, int] = None  # Device Code, e.g. 0
    have_meter: Union[EmptyStrToNone, bool] = None  # Default 0: no meter, 1: meter
    in_system: Union[EmptyStrToNone, bool] = None  # False
    model: Union[EmptyStrToNone, str] = None  # Device model, e.g. 'ShineWeFi'
    msg: Union[EmptyStrToNone, str] = None  # Return information, e.g. 'datalog'
    normal_power: Union[EmptyStrToNone, int] = (
        None  # Rated Power(Western Australia supports reading, others only partially), e.g. 0
    )
    obj: Union[EmptyStrToNone, int] = None  # 1=inverter, 2=storage, 3=collector, 4=other
    result: Union[EmptyStrToNone, int] = None  # 1=success, other=fail


# #####################################################################################################################
# Datalogger validation ###############################################################################################


class DataloggerValidationData(ApiModel):
    datalogger_sn: Union[EmptyStrToNone, str] = None  # SN of the collector (if exists), e.g. 'QMN0000000000000'
    plant_id: Union[EmptyStrToNone, int] = None  # plant ID to which the collector belongs (if exists), e.g. 9900000
    user_id: Union[EmptyStrToNone, int] = None  # user ID to which the collector belongs  (if exists), e.g. 3100000


class DataloggerValidation(ApiResponse):
    data: Union[EmptyStrToNone, DataloggerValidationData] = None


# #####################################################################################################################
# Datalogger validation ###############################################################################################


class DeviceEnergyDay(ApiResponse):
    data: Union[EmptyStrToNone, float] = None  # daily energy production,e.g. 168.89999389648438
    datalogger_sn: Union[EmptyStrToNone, str] = None  # SN of the collector, e.g. 'QMN0000000000000'
    device_sn: Union[EmptyStrToNone, str] = None  # SN of the inverter, e.g. 'BZP0000000'


# #####################################################################################################################
# Device (get) datalogger #############################################################################################


def _device_datalogger_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "datalogSN",
    }
    return override.get(snake, to_camel(snake=snake))


class DeviceDataloggerData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_device_datalogger_data_to_camel,
    )

    datalogger_sn: Union[EmptyStrToNone, str] = None  # SN of the collector, e.g. 'QMN0000000000000'


class DeviceDatalogger(ApiResponse):
    data: Union[EmptyStrToNone, DeviceDataloggerData] = None


# #####################################################################################################################
# Device create date ##################################################################################################


def _device_basic_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "datalogSn",
    }
    return override.get(snake, to_camel(snake=snake))


class DeviceBasicData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_device_basic_data_to_camel,
    )

    create_time: Union[EmptyStrToNone, datetime.datetime] = None  # create time, e.g. '2024-11-30 17:37:00'
    datalogger_sn: Union[EmptyStrToNone, str] = (
        None  # The SN of the collector to which the inverter belongs, e.g. 'QMN0000000000000'
    )
    device_name: Union[EmptyStrToNone, str] = None  # device name, e.g. 'MIN'
    device_sn: Union[EmptyStrToNone, str] = None  # Device SN, e.g. 'BZP0000000'
    device_type: Union[EmptyStrToNone, str] = None  # device type, e.g. 'CLOVE'
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. '2025-02-24 23:03:00'
    table_name: Union[EmptyStrToNone, str] = None


class DeviceCreateDate(ApiResponse):
    data: Union[EmptyStrToNone, Dict[str, DeviceBasicData]] = None  # key: device serial number


# #####################################################################################################################
# Device create date ##################################################################################################


class DeviceAdd(ApiResponse):
    data: Union[EmptyStrToNone, Any] = None
