import datetime
from typing import List, Union, Literal

from .api_model import (
    ApiResponse,
    ApiModel,
    EmptyStrToNone,
)


# #####################################################################################################################
# Plant add ###########################################################################################################


class PlantAddData(ApiModel):
    plant_id: Union[EmptyStrToNone, int] = None  # Plant ID, e.g. 24832


class PlantAdd(ApiResponse):
    data: Union[EmptyStrToNone, PlantAddData] = None


# #####################################################################################################################
# Plant modify ########################################################################################################


class PlantModify(ApiResponse):
    data: Union[EmptyStrToNone, str] = None


# #####################################################################################################################
# Plant delete ########################################################################################################


class PlantDelete(ApiResponse):
    data: Union[EmptyStrToNone, str] = None


# #####################################################################################################################
# Plant list ##########################################################################################################


class PlantData(ApiModel):
    city: str  # 'Günzburg'
    country: str  # country name, e.g. 'Germany'
    create_date: Union[EmptyStrToNone, datetime.date]  # Website creation date, e.g. '2024-11-01'
    current_power: Union[EmptyStrToNone, float] = None  # Current power (W), e.g. '91.8'
    image_url: Union[EmptyStrToNone, str] = None  # Picture url
    installer: Union[EmptyStrToNone, str]  # Installer name, e.g. '0'
    latitude: Union[EmptyStrToNone, float] = None  # latitude, e.g. '48.12345'
    latitude_d: Union[EmptyStrToNone, str]  # Agent name
    latitude_f: Union[EmptyStrToNone, str]  # Agency area
    locale: Union[EmptyStrToNone, str] = None  # e.g. 'en-US'
    longitude: Union[EmptyStrToNone, float] = None  # longitude, e.g. '10.12345'
    name: str  # Power station name
    operator: Union[EmptyStrToNone, str]  # e.g. '0'
    peak_power: float  # Peak power (kWp), e.g. 0.8
    plant_id: int  # Plant ID
    status: int  # 1
    total_energy: Union[EmptyStrToNone, float] = None  # Cumulative power generation (kWh), e.g. '45'
    user_id: int  # User ID to which the power station belongs


class PlantListData(ApiModel):
    count: int  # Total number of power stations
    plants: List[PlantData]


class PlantList(ApiResponse):
    data: Union[EmptyStrToNone, PlantListData] = None


# #####################################################################################################################
# Plant details #######################################################################################################


class PlantDetailModule(ApiModel):
    module_man: Union[EmptyStrToNone, str] = None  # 'Growatt'
    module_md: Union[EmptyStrToNone, str] = None
    num_modules: Union[EmptyStrToNone, int] = None


class PlantDetailDatalogger(ApiModel):
    datalogger_man: Union[EmptyStrToNone, str] = None  # 'Growatt'
    datalogger_md: Union[EmptyStrToNone, str] = None
    datalogger_num: Union[EmptyStrToNone, int] = None


class PlantDetailInverter(ApiModel):
    inverter_man: Union[EmptyStrToNone, str] = None  # 'Growatt'
    inverter_md: Union[EmptyStrToNone, str] = None
    inverter_num: Union[EmptyStrToNone, int] = None


class PlantDetailMax(ApiModel):
    max_man: Union[EmptyStrToNone, str] = None  # 'Growatt'
    max_md: Union[EmptyStrToNone, str] = None
    max_num: Union[EmptyStrToNone, int] = None


class PlantDetailData(ApiModel):
    address1: Union[EmptyStrToNone, str] = None  # Plant address
    address2: Union[EmptyStrToNone, str] = None
    arrays: List[PlantDetailModule] = []  # e.g. [{'module_man': 'Growatt', 'module_md': '', 'num_modules': 0}]
    city: Union[EmptyStrToNone, str] = None  # e.g. 'Günzburg'
    country: Union[EmptyStrToNone, str] = None  # country name, e.g. 'Germany'
    create_date: Union[EmptyStrToNone, datetime.date] = None  # Building date, e.g. '2024-11-29'
    currency: Union[EmptyStrToNone, str] = None  # currency unit, e.g. 'EUR'
    dataloggers: List[PlantDetailDatalogger] = (
        []
    )  # e.g. [{'datalogger_man': 'Growatt', 'datalogger_md': '', 'datalogger_num': 1}]
    description: Union[EmptyStrToNone, str] = None
    designercontact: Union[EmptyStrToNone, str] = None
    designerorganization: Union[EmptyStrToNone, str] = None
    elevation: Union[EmptyStrToNone, float] = None
    financiercontact: Union[EmptyStrToNone, str] = None
    financierorganization: Union[EmptyStrToNone, str] = None
    fixed_azimuth: Union[EmptyStrToNone, float] = None
    fixed_tilt: Union[EmptyStrToNone, float] = None
    grid_type: Union[EmptyStrToNone, str] = None
    image_url: Union[EmptyStrToNone, str] = None  # Picture url, e.g. None
    installed_ac_capacity: Union[EmptyStrToNone, float] = None
    installed_dc_capacity: Union[EmptyStrToNone, float] = None
    installed_panel_area: Union[EmptyStrToNone, float] = None
    installercontact: Union[EmptyStrToNone, str] = None
    installerorganization: Union[EmptyStrToNone, str] = None
    inverters: List[PlantDetailInverter] = (
        []
    )  # e.g. [{'inverter_man': 'Growatt', 'inverter_md': '', 'inverter_num': 0}]
    irradiationsensor_type: Union[EmptyStrToNone, str] = None
    jurisdictioncontact: Union[EmptyStrToNone, str] = None
    jurisdictionorganization: Union[EmptyStrToNone, str] = None
    latitude: Union[EmptyStrToNone, float] = None  # Latitude, e.g. '48.424232364163'
    locale: Union[EmptyStrToNone, str] = None  # , e.g. 'en_US'
    longitude: Union[EmptyStrToNone, float] = None  # Longitude, e.g. '10.298493652343'
    maxs: List[PlantDetailMax] = []  # e.g. [{'max_man': 'Growatt', 'max_md': '', 'max_num': 0}]
    name: Union[EmptyStrToNone, str] = None  # power station name, e.g. 'Balkondach'
    notes: Union[EmptyStrToNone, str] = None
    offtakercontact: Union[EmptyStrToNone, str] = None
    offtakerorganization: Union[EmptyStrToNone, str] = None
    operatorcontact: Union[EmptyStrToNone, str] = None
    operatororganization: Union[EmptyStrToNone, str] = None
    ownercontact: Union[EmptyStrToNone, str] = None
    ownerorganization: Union[EmptyStrToNone, str] = None
    peak_power: Union[EmptyStrToNone, float] = None  # peak power (kWp), e.g. 1
    plant_type: Union[EmptyStrToNone, int] = (
        None  # Plant type (0=Residential Plant, 1=Commercial Plant, 2=Ground-Mounted Plants), e.g. 0
    )
    postal: Union[EmptyStrToNone, str] = None
    state: Union[EmptyStrToNone, str] = None
    status: Union[EmptyStrToNone, str] = None
    timezone: Union[EmptyStrToNone, str] = None  # Time Zone, e.g. 'GMT+1'
    tracker_type: Union[EmptyStrToNone, str] = None
    user_id: Union[EmptyStrToNone, int] = None  # User ID to which the plant belongs, e.g. 3127501
    weather_type: Union[EmptyStrToNone, str] = None
    weathersensor_man: Union[EmptyStrToNone, str] = None
    weathersensor_md: Union[EmptyStrToNone, str] = None
    weathersensor_num: Union[EmptyStrToNone, str] = None


class PlantDetails(ApiResponse):
    data: Union[EmptyStrToNone, PlantDetailData] = None


# #####################################################################################################################
# Plant energy overview ###############################################################################################


class PlantEnergyOverviewData(ApiModel):
    current_power: Union[EmptyStrToNone, float] = None  # current power (kW), 0
    today_energy: Union[EmptyStrToNone, float] = None  # Power Generation (kWh), '0.2'
    monthly_energy: Union[EmptyStrToNone, float] = None  # Power Generation in the Month (kWh), '17.8'
    yearly_energy: Union[EmptyStrToNone, float] = None  # Power generation in the current year (kWh), '36'
    total_energy: Union[EmptyStrToNone, float] = None  # Cumulative power generation (kWh), '45.1'
    peak_power_actual: Union[EmptyStrToNone, float] = None  # Actual Peak Power (kW), 1
    efficiency: Union[EmptyStrToNone, float] = None
    carbon_offset: Union[EmptyStrToNone, float] = None  # Equivalent reduction of CO2 emissions, '7.1'
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last received data, '2025-02-24 15:34:56'
    timezone: Union[EmptyStrToNone, str] = None  # Time Zone, 'GMT+1'


class PlantEnergyOverview(ApiResponse):
    data: Union[EmptyStrToNone, PlantEnergyOverviewData] = None


# #####################################################################################################################
# Plant energy history ################################################################################################


class PlantEnergyHistoryDate(ApiModel):
    date: datetime.date  # '2018-12-13' | '2018-12' | '2018'
    energy: Union[EmptyStrToNone, float] = None


class PlantEnergyHistoryData(ApiModel):
    count: int  # Total Records
    time_unit: Literal["day", "month", "year"]  # time_unit on request
    energys: List[PlantEnergyHistoryDate]


class PlantEnergyHistory(ApiResponse):
    data: Union[EmptyStrToNone, PlantEnergyHistoryData] = None


# #####################################################################################################################
# Plant power #########################################################################################################


class PlantPowerDate(ApiModel):
    time: datetime.datetime  # '2018-12-13 10:45'
    power: Union[EmptyStrToNone, float] = None


class PlantPowerData(ApiModel):
    count: int  # Total Records
    powers: List[PlantPowerDate]


class PlantPower(ApiResponse):
    data: Union[EmptyStrToNone, PlantPowerData] = None


# #####################################################################################################################
# Plant info ##########################################################################################################


class PlantInfoData(ApiModel):
    plant: PlantData


class PlantInfo(ApiResponse):
    data: Union[EmptyStrToNone, PlantInfoData] = None
