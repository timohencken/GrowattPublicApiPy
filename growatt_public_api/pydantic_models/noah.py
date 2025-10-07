import datetime
from typing import Union, List, Any, Dict, Annotated

from loguru import logger
from pydantic import (
    ConfigDict,
    BeforeValidator,
)
from pydantic.alias_generators import to_camel

from .api_model import (
    EmptyStrToNone,
    ApiModel,
    NewApiResponse,
)


# #####################################################################################################################
# Noah status #########################################################################################################


def _noah_status_data_to_camel(snake: str) -> str:
    override = {
        "battery_package_quantity": "batteryNum",
        "ac_couple_power_control": "acCoupleEnable",
        "ct_flag": "isHaveCt",
        "currency": "moneyUnit",
        "money_today": "profitToday",
        "money_total": "profitTotal",
        "total_battery_pack_soc": "soc",
        "total_household_load": "loadPower",
        "ct_self_power": "gridPower",
    }
    return override.get(snake, to_camel(snake=snake))


class NoahStatusData(ApiModel):
    """
    data was gathered using Nexa device
    Noah data might differ in some fields
    - recheck when Noah is available on test server
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_noah_status_data_to_camel,
    )

    ac_couple_power_control: Union[EmptyStrToNone, int] = None  # e.g. '1'
    alias: Union[EmptyStrToNone, str] = None  # e.g. 'NEXA 2000'
    associated_inv_sn: Union[EmptyStrToNone, str] = None  # Associated Inverter, e.g. None
    battery_package_quantity: Union[EmptyStrToNone, int] = None  # Number of parallel battery packs, e.g. '2'
    total_battery_pack_charging_power: Union[EmptyStrToNone, float] = None  # Total battery charging power, e.g. '0'
    eac_today: Union[EmptyStrToNone, float] = None  # Daily power generation, e.g. '0.8'
    eac_total: Union[EmptyStrToNone, float] = None  # Total power generation, e.g. '116.7'
    eastron_status: Union[EmptyStrToNone, int] = None  # e.g. '-1'
    ct_self_power: Union[EmptyStrToNone, float] = (
        None  # power taken from grid measured by (shelly) smart meter e.g. '620'
    )
    groplug_num: Union[EmptyStrToNone, int] = None  # e.g. '0'
    groplug_power: Union[EmptyStrToNone, float] = None  # e.g. '0'
    ct_flag: Union[EmptyStrToNone, bool] = None  # e.g. 'true'
    total_household_load: Union[EmptyStrToNone, float] = (
        None  # Household consumption (minus third party inverter power) e.g. '620'
    )
    currency: Union[EmptyStrToNone, str] = None  # e.g. '€'
    on_off_grid: Union[EmptyStrToNone, int] = None  # e.g. '0'
    other_power: Union[EmptyStrToNone, float] = None  # e.g. '0'
    pac: Union[EmptyStrToNone, float] = (
        None  # BUCK (=step-down) output power - (-)=Output/(+)=AC-Charge - power in/output from Nexa, e.g. '0'
    )
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. '12345678'
    ppv: Union[EmptyStrToNone, float] = None  # Photovoltaic power (W), e.g. '0'
    money_today: Union[EmptyStrToNone, float] = None  # Income today in "currency", e.g. '0.32'
    money_total: Union[EmptyStrToNone, float] = None  # Income total in "currency", e.g. '46.68'
    total_battery_pack_soc: Union[EmptyStrToNone, int] = (
        None  # Total battery pack SOC (State of Charge) percentage, e.g. '11'
    )
    status: Union[EmptyStrToNone, int] = None  # 1: Normal, 4: Fault, 5: Heating, e.g. '6'
    work_mode: Union[EmptyStrToNone, int] = (
        None  # Current time period working mode (0=Load-First, 1=Battery-First, 2=Smart), e.g. '2'
    )


class NoahStatus(NewApiResponse):
    data: Union[EmptyStrToNone, NoahStatusData] = None


# #####################################################################################################################
# Noah battery status #################################################################################################


class NoahBatteryData(ApiModel):
    battery1_serial_num: Union[EmptyStrToNone, str] = None  # Battery pack 1—SN, e.g. '0HVR...'
    battery1_soc: Union[EmptyStrToNone, int] = None  # Battery pack 1 SOC, e.g. 47
    battery1_temp: Union[EmptyStrToNone, float] = None  # Battery pack 1 temperature, e.g. 36.0
    battery1_temp_f: Union[EmptyStrToNone, float] = None  # e.g. 96.8
    battery2_serial_num: Union[EmptyStrToNone, str] = None  # e.g. ''
    battery2_soc: Union[EmptyStrToNone, int] = None  # e.g. 0
    battery2_temp: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    battery2_temp_f: Union[EmptyStrToNone, float] = None  # e.g. 32.0
    battery3_serial_num: Union[EmptyStrToNone, str] = None  # e.g. ''
    battery3_soc: Union[EmptyStrToNone, int] = None  # e.g. 0
    battery3_temp: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    battery3_temp_f: Union[EmptyStrToNone, float] = None  # e.g. 32.0
    battery4_serial_num: Union[EmptyStrToNone, str] = None  # e.g. ''
    battery4_soc: Union[EmptyStrToNone, int] = None  # e.g. 0
    battery4_temp: Union[EmptyStrToNone, float] = None  # e.g. 0.0
    battery4_temp_f: Union[EmptyStrToNone, float] = None  # e.g. 32.0
    battery_package_quantity: Union[EmptyStrToNone, int] = None  # Number of parallel battery packs, e.g. 1
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-06-11 12:34:56'


class NoahBatteryStatus(NewApiResponse):
    data: Union[EmptyStrToNone, NoahBatteryData] = None


# #####################################################################################################################
# Noah settings #######################################################################################################


def parse_noah_time_segment(segment: str) -> Dict[str, str]:
    """
    time segments are provided by API as tring separated by underscores
    e.g. '0_0:2_0:3_200_1'
    which means:
    - work_mode: 0 (0=Load-First, 1=Battery-First, 2=Smart)
    - start_time: '0:2' (hh:mm)
    - end_time: '0:3' (hh:mm)
    - power: 200 (System output power in load-first mode, 0 for other modes)
    - days: '1' (0=every day, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat, 7=Sun)
    """
    if not segment:
        return {}

    parts = segment.split("_")
    if len(parts) != 5:
        logger.warning(f"Unexpected time segment format: {segment}")
        return {}

    try:
        return {
            "work_mode": parts[0],
            # time is missing leading zeroes and thus cannot be parsed by pydantic, e.g. '0:2' -> '00:02'
            "start_time": ":".join([f"{x:>02}" for x in parts[1].split(":")]),
            "end_time": ":".join([f"{x:>02}" for x in parts[2].split(":")]),
            "power": parts[3],
            "days": [day for day in parts[4].split(",")],
        }
    except Exception as e:
        logger.warning(f"Error parsing time segment: {segment}. Error: {e}")
        return {}


class NoahTimeSegment(ApiModel):
    work_mode: Union[EmptyStrToNone, int] = None  # e.g. '2'
    start_time: Union[EmptyStrToNone, datetime.time] = None  # e.g. '0:2'
    end_time: Union[EmptyStrToNone, datetime.time] = None  # e.g. '0:20'
    power: Union[EmptyStrToNone, int] = None  # System output power in load-first mode, 0 for other modes, e.g. '200'
    days: Union[EmptyStrToNone, List[int]] = (
        None  # 0=every day, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat, 7=Sun, e.g. [0]
    )


ParsedNoahTimeSegment = Annotated[NoahTimeSegment, BeforeValidator(parse_noah_time_segment)]


def time_segments_list_to_dict(segments: List[dict]) -> Dict[str, str]:
    """
    time segments are provided by API as list of dicts
        [{'time_segment1': '0_0:2_0:3_200_1'}, {'time_segment2': '1_0:5_0:6_0_1,2'}]
    but we want to have them as a single dict with known keys
        {'time_segment1': '0_0:2_0:3_200_1', 'time_segment2': '1_0:5_0:6_0_1,2'}
    """
    if segments is None:
        return {}

    segment_dict = {}
    try:
        for segment in segments:
            segment_dict.update(segment)
    except Exception as e:
        logger.warning(f"Unexpected time segments format: {segments}. Error: {e}")

    return segment_dict


class NoahTimeSegments(ApiModel):
    time_segment1: Union[EmptyStrToNone, ParsedNoahTimeSegment] = None  # e.g. '0_0:2_0:3_200_1'
    time_segment2: Union[EmptyStrToNone, ParsedNoahTimeSegment] = None  # e.g. '1_0:5_0:6_0_1,2'
    time_segment3: Union[EmptyStrToNone, ParsedNoahTimeSegment] = None  # e.g. '1_10:5_10:6_0_1,2'
    time_segment4: Union[EmptyStrToNone, ParsedNoahTimeSegment] = None  # e.g. '2_0:7_0:8_0_1,2,3,4,5,6,7'
    time_segment5: Union[EmptyStrToNone, ParsedNoahTimeSegment] = None  # e.g. '0_1:0_1:1_200_0'
    time_segment6: Union[EmptyStrToNone, ParsedNoahTimeSegment] = None  # e.g. '0_2:0_2:1_200_0'
    time_segment7: Union[EmptyStrToNone, ParsedNoahTimeSegment] = None  # e.g. '0_3:0_3:59_200_0'
    time_segment8: Union[EmptyStrToNone, ParsedNoahTimeSegment] = None  # e.g. '0_4:0_4:2_200_0'
    time_segment9: Union[EmptyStrToNone, ParsedNoahTimeSegment] = None  # e.g. '0_5:0_5:59_200_0'


class NoahSafetyListItem(ApiModel):
    country_and_area: Union[EmptyStrToNone, str] = None  # e.g. 'German'
    safety_correspond_num: Union[EmptyStrToNone, int] = None  # e.g. 1


class NoahPlantListItem(ApiModel):
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. '123456789'
    plant_img_name: Union[EmptyStrToNone, str] = None  # e.g. ''
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. 'My Solar Plant'


def _noah_settings_data_to_camel(snake: str) -> str:
    override = {
        "default_ac_couple_power": "defaultACCouplePower",
        "currency": "moneyUnitText",
        "time_segments": "time_segment",
    }
    return override.get(snake, to_camel(snake=snake))


class NoahSettingsData(ApiModel):
    """
    data was gathered using Nexa device
    Noah data might differ in some fields
    - recheck when Noah is available on test server
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_noah_settings_data_to_camel,
    )

    ac_couple: Union[EmptyStrToNone, bool] = None  # e.g. 'true'
    ac_couple_enable: Union[EmptyStrToNone, int] = None  # e.g. '1'
    ac_couple_power_control: Union[EmptyStrToNone, int] = None  # e.g. '1'
    alias: Union[EmptyStrToNone, str] = None  # e.g. 'NEXA 2000'
    allow_grid_charging: Union[EmptyStrToNone, int] = None  # e.g. '1'
    ammeter_model: Union[EmptyStrToNone, str] = None  # e.g. 'Shelly Pro 3EM'
    ammeter_sn: Union[EmptyStrToNone, str] = None  # e.g. '123456789012345',
    anti_backflow_enable: Union[EmptyStrToNone, int] = None  # e.g. '1',
    anti_backflow_power_percentage: Union[EmptyStrToNone, int] = None  # e.g. '0',
    bat_sns: Union[EmptyStrToNone, List[str]] = None  # e.g. ['0HVR...', '0HYR...'],
    charging_soc_high_limit: Union[EmptyStrToNone, float] = None  # e.g. '100',
    charging_soc_low_limit: Union[EmptyStrToNone, float] = None  # e.g. '10',
    ct_type: Union[EmptyStrToNone, int] = None  # e.g. '0',
    currency_list: Union[EmptyStrToNone, List[str]] = None  # e.g.
    # [ 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARP', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF',
    #   'BMD', 'BND', 'BOB', 'BRC', 'BSD', 'BTN', 'BUK', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'COP', 'CRC',
    #   'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS',
    #   'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'INR', 'IQD', 'IRR', 'ISK', 'JMD',
    #   'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL',
    #   'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN',
    #   'NIO', 'NIS', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RMB', 'RON',
    #   'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SVC',
    #   'SYP', 'SZL', 'THB', 'THP', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU',
    #   'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW']
    default_ac_couple_power: Union[EmptyStrToNone, int] = None  # e.g. '100'
    default_mode: Union[EmptyStrToNone, int] = None  # e.g. '0'
    device_sn: Union[EmptyStrToNone, str] = None  # e.g. '0HVR...'
    formula_money: Union[EmptyStrToNone, float] = None  # e.g. '0.4'
    grid_connection_control: Union[EmptyStrToNone, int] = None  # e.g. '0'
    grid_set: Union[EmptyStrToNone, int] = None  # e.g. '1'
    model: Union[EmptyStrToNone, str] = None  # Model, e.g. 'NEXA 2000',
    currency: Union[EmptyStrToNone, str] = None  # e.g. 'EUR'
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. '12345678'
    plant_name: Union[EmptyStrToNone, str] = None  # e.g. 'Solar plant',
    plant_list: Union[EmptyStrToNone, List[NoahPlantListItem]] = (
        None  # e.g. [{'plantId': 12345678, 'plantImgName': '', 'plantName': 'My Solar Plant'}]
    )
    safety: Union[EmptyStrToNone, int] = None  # e.g. 1
    safety_enable: Union[EmptyStrToNone, bool] = None  # e.g. 'true'
    safety_list: Union[EmptyStrToNone, List[NoahSafetyListItem]] = None  # e.g.
    # [ {'countryAndArea': 'German', 'safetyCorrespondNum': 1},
    #   {'countryAndArea': 'Netherlands', 'safetyCorrespondNum': 2},
    #   {'countryAndArea': 'Belgium', 'safetyCorrespondNum': 3},
    #   {'countryAndArea': 'French', 'safetyCorrespondNum': 4},
    #   {'countryAndArea': 'EN 50549-1', 'safetyCorrespondNum': 5}]
    shelly_list: Union[EmptyStrToNone, List[Any]] = None  # e.g. []
    smart_plan: Union[EmptyStrToNone, bool] = None  # e.g. 'true'
    temp_type: Union[EmptyStrToNone, int] = None  # 0=Celsius, 1=Fahrenheit, e.g. '0'
    time_segments: Union[EmptyStrToNone, Annotated[NoahTimeSegments, BeforeValidator(time_segments_list_to_dict)]] = (
        None  # Working mode time segments, e.g.
    )
    # [{'time_segment3': '2_0:0_0:1_0_0'}, {'time_segment1': '0_0:2_0:3_200_1'}, {'time_segment2': '1_0:5_0:6_0_1,2'},
    #  {'time_segment4': '2_0:7_0:8_0_1,2,3,4,5,6,7'}, {'time_segment5': '0_1:0_1:1_200_0'},
    #  {'time_segment6': '0_2:0_2:1_200_0'}, {'time_segment7': '0_3:0_3:59_200_0'}, {'time_segment8': '0_4:0_4:2_200_0'},
    #  {'time_segment9': '0_5:0_5:59_200_0'}]
    version: Union[EmptyStrToNone, str] = None  # e.g. '11.10.09.07.9000.4017'
    work_mode: Union[EmptyStrToNone, int] = None  # e.g. '2'


class NoahSettings(NewApiResponse):
    data: Union[EmptyStrToNone, NoahSettingsData] = None


# #####################################################################################################################
# Noah power chart ####################################################################################################


class NoahPowerChartData(ApiModel):
    time: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. '2024-06-11 00:00:00'
    pac: Union[EmptyStrToNone, float] = None  # e.g. 0
    ppv: Union[EmptyStrToNone, float] = None  # e.g. 0
    total_household_load: Union[EmptyStrToNone, float] = None  # e.g. 0


class NoahPowerChart(NewApiResponse):
    data: Union[EmptyStrToNone, List[NoahPowerChartData]] = None


# #####################################################################################################################
# Noah energy chart ####################################################################################################


class NoahEnergyChartData(ApiModel):
    time: Union[EmptyStrToNone, datetime.date] = None  # e.g. '2024-06-11 00:00:00'
    epv: Union[EmptyStrToNone, float] = None  # e.g. 0


class NoahEnergyChart(NewApiResponse):
    data: Union[EmptyStrToNone, List[NoahEnergyChartData]] = None


# #####################################################################################################################
# Noah firmware info ##################################################################################################


def _noah_firmware_info_data_to_camel(snake: str) -> str:
    override = {
        "update_available": "checkUpgradeNoah",
        "current_version": "currVersion",
        "latest_version": "newVersion",
    }
    return override.get(snake, to_camel(snake=snake))


class NoahFirmwareInfoData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_noah_firmware_info_data_to_camel,
    )

    current_version: Union[EmptyStrToNone, str] = None  # e.g. '11.10.09.07.9000.4017'
    latest_version: Union[EmptyStrToNone, str] = None  # e.g. '11.10.09.07.9000.4017'
    update_available: Union[EmptyStrToNone, bool] = None  # e.g. False
    status: Union[EmptyStrToNone, int] = None  # e.g. '6'


class NoahFirmwareInfo(NewApiResponse):
    data: Union[EmptyStrToNone, NoahFirmwareInfoData] = None
