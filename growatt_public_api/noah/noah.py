import datetime
from datetime import date, time
from typing import Union, List, Optional, Literal

from ..api_v4 import ApiV4
from ..growatt_types import DeviceType
from ..pydantic_models.noah import (
    NoahStatus,
    NoahBatteryStatus,
    NoahSettings,
    NoahPowerChart,
    NoahEnergyChart,
    NoahFirmwareInfo,
)
from ..pydantic_models.api_v4 import (
    NoahDetailsV4,
    NoahEnergyV4,
    NoahEnergyHistoryV4,
    NoahEnergyHistoryMultipleV4,
    SettingWriteV4,
    PowerV4,
    WifiStrengthV4,
)
from ..session.growatt_api_session import GrowattApiSession  # noqa: E402
from ..device import Device


class Noah:
    """
    endpoints for NOAH devices
    https://www.showdoc.com.cn/2540838290984246/11315140426110613
    """

    session: GrowattApiSession
    _api_v4: ApiV4
    device_sn: Optional[str] = None
    _noah_or_nexa_cache: dict = None

    def __init__(self, session: GrowattApiSession, device_sn: Optional[str] = None) -> None:
        self.session = session
        self._api_v4 = ApiV4(session)
        self.device_sn = device_sn
        self._noah_or_nexa_cache = {}

    def _device_sn(self, device_sn: Optional[Union[str, List[str]]]) -> Union[str, List[str]]:
        """
        Use device_sn explicitly provided, fallback to the one from the instance
        """
        device_sn = device_sn or self.device_sn
        if device_sn is None:
            raise AttributeError("device_sn must be provided")
        return device_sn

    def _noah_or_nexa(self, device_sn: Optional[str] = None):
        """
        determine if device is Noah or Nexa

        this is required to get the right URLs for some endpoints, e.g.
        * /noahDeviceApi/noah/getSystemStatus
        * /noahDeviceApi/nexa/getSystemStatus

        Web API uses /noahDeviceApi/noah/isPlantNoahSystem which is not available using token authentication

        returns
         "noah" | "nexa"
        """
        device_sn = self._device_sn(device_sn)
        if device_sn not in self._noah_or_nexa_cache:
            device_api = Device(session=self.session)
            device_type_info = device_api.type_info(device_sn=self._device_sn(device_sn))
            model_name = device_type_info.model or ""
            model_name = model_name.lower()
            model_name = model_name.split(" ")[0]
            if model_name in ["noah", "nexa"]:
                self._noah_or_nexa_cache[device_sn] = model_name
            else:
                raise ValueError(f"unknown model name '{model_name}' for device_sn '{device_sn}'")
        return self._noah_or_nexa_cache[device_sn]

    def status(
        self,
        device_sn: Optional[str] = None,
    ) -> NoahStatus:
        """
        Noah/Nexa status data
        Retrieve basic status/energy metrics by device SN.
        ! not part of official API documentation, but reverse-engineered from APP API calls
          * /noahDeviceApi/nexa/getSystemStatus
          * /noahDeviceApi/noah/getSystemStatus

        Rate limit(s):
        * There seems to be no rate limit for this endpoint, but do not call it too often to avoid being blocked
        * Mobile app calls this endpoint every 6 seconds

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            NoahStatus
            {'data': {'ac_couple_power_control': 1,
                      'alias': 'NEXA 2000',
                      'associated_inv_sn': None,
                      'battery_package_quantity': 2,
                      'total_battery_pack_charging_power': 112.0,  # (+)=charging, (-)=discharging
                      'eac_today': 1.4,
                      'eac_total': 118.2,
                      'eastron_status': -1,
                      'ct_self_power': 387.0,   # Power drawn from grid (measured by smart meter) (+)=from grid, (-)=to grid
                      'groplug_num': 0,
                      'groplug_power': 0.0,     # Probably power measured by groplug
                      'ct_flag': True,
                      'total_household_load': 387.0,  # Household power consumption
                      'currency': '€',
                      'on_off_grid': 0,
                      'other_power': 0.0,       # ??? during observation period always == pac
                      'pac': 0.0,               # AC in/output power (+)=AC-charging, (-)=Nexa/Noah power output
                      'plant_id': 12345678,
                      'ppv': 112.0,             # Photovoltaic power
                      'money_today': 0.56,
                      'money_total': 47.28,
                      'total_battery_pack_soc': 11,
                      'status': 6,
                      'work_mode': 2},
             'error_code': 0,
             'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        # noinspection DuplicatedCode
        device_sn = self._device_sn(device_sn)
        noah_or_nexa = self._noah_or_nexa(device_sn=device_sn)

        response = self.session.post(
            endpoint=f"noahDeviceApi/{noah_or_nexa}/getSystemStatus",
            data={
                "deviceSn": self._device_sn(device_sn),
            },
        )

        # transfer to data structure resembling v4 API
        _error_code = 0 if response.get("result") == 1 else 1
        _msg = response.get("msg")
        _msg = _msg or ("SUCCESSFUL_OPERATION" if _error_code == 0 else "SYSTEM_ERROR")
        _data = response.get("obj", {})
        # charge/discharge power is returned separately, but in v4 API it is a single value (positive=charging, negative=discharging)
        _data["total_battery_pack_charging_power"] = float(_data.get("chargePower") or 0.0) - float(
            _data.get("disChargePower") or 0.0
        )

        return NoahStatus.model_validate(
            {
                "data": _data,
                "error_code": _error_code,
                "error_msg": _msg,
            }
        )

    def battery_status(
        self,
        device_sn: Optional[str] = None,
    ) -> NoahBatteryStatus:
        """
        Noah/Nexa battery data
        Retrieve basic status/energy metrics by device SN.
        ! not part of official API documentation, but reverse-engineered from APP API calls
          * /noahDeviceApi/noah/getBatteryData
          * /noahDeviceApi/nexa/getBatteryData

        Rate limit(s):
        * There seems to be no rate limit for this endpoint, but do not call it too often to avoid being blocked

        Args:
            device_sn (Optional[str]): Inverter serial number

        Returns:
            NoahBatteryStatus
            {'data': {'battery1_serial_num': '0HVR...',
                      'battery1_soc': 9,
                      'battery1_temp': 15.0,
                      'battery1_temp_f': 59.0,
                      'battery2_serial_num': '0HYR...',
                      'battery2_soc': 12,
                      'battery2_temp': 11.0,
                      'battery2_temp_f': 51.8,
                      'battery3_serial_num': None,
                      'battery3_soc': None,
                      'battery3_temp': None,
                      'battery3_temp_f': None,
                      'battery4_serial_num': None,
                      'battery4_soc': None,
                      'battery4_temp': None,
                      'battery4_temp_f': None,
                      'battery_package_quantity': 2,
                      'time': datetime.datetime(2025, 10, 6, 18, 12, 44)},
             'error_code': 0,
             'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        # noinspection DuplicatedCode
        device_sn = self._device_sn(device_sn)
        noah_or_nexa = self._noah_or_nexa(device_sn=device_sn)

        response = self.session.post(
            endpoint=f"noahDeviceApi/{noah_or_nexa}/getBatteryData",
            data={
                "deviceSn": self._device_sn(device_sn),
            },
        )

        # transfer to data structure resembling v4 API
        _error_code = 0 if response.get("result") == 1 else 1
        _msg = response.get("msg")
        _msg = _msg or ("SUCCESSFUL_OPERATION" if _error_code == 0 else "SYSTEM_ERROR")
        _temp_type = response.get("obj", {}).get("tempType")  # e.g. "°C"
        _data = {
            "time": response.get("obj", {}).get("time"),
        }
        for _bat_num, _bat_data in enumerate(response.get("obj", {}).get("batter", []), start=1):
            _data[f"battery{_bat_num}_serial_num"] = _bat_data.get("serialNum")
            _data[f"battery{_bat_num}_soc"] = _bat_data.get("soc")
            _temp = _temp_c = _temp_f = _bat_data.get("temp")
            if "F" in _temp_type and _temp:
                # convert to celsius
                _temp_c = (float(_temp) - 32) / 1.8
            _data[f"battery{_bat_num}_temp"] = float(_temp_c) if _temp_c else None
            if "C" in _temp_type and _temp:
                # convert to fahrenheit
                _temp_f = (float(_temp) * 1.8) + 32
            _data[f"battery{_bat_num}_temp_f"] = float(_temp_f) if _temp_c else None
            _data["battery_package_quantity"] = _bat_num

        return NoahBatteryStatus.model_validate(
            {
                "data": _data,
                "error_code": _error_code,
                "error_msg": _msg,
            }
        )

    def settings(
        self,
        device_sn: Optional[str] = None,
    ) -> NoahSettings:
        """
        Noah/Nexa settings
        Retrieve basic settings by device SN.
        ! not part of official API documentation, but reverse-engineered from APP API calls
          * /noahDeviceApi/noah/getNoahInfoBySn
          * /noahDeviceApi/nexa/getNexaInfoBySn

        Rate limit(s):
        * There seems to be no rate limit for this endpoint, but do not call it too often to avoid being blocked

        Args:
            device_sn (Optional[str]): Inverter serial number

        Returns:
            NoahSettings
            {'data': {'ac_couple': True,
                      'ac_couple_enable': 1,
                      'ac_couple_power_control': 1,
                      'alias': 'NEXA 2000',
                      'allow_grid_charging': 1,
                      'ammeter_model': 'Shelly Pro 3EM',
                      'ammeter_sn': '123456789012345',
                      'anti_backflow_enable': 1,
                      'anti_backflow_power_percentage': 0,
                      'bat_sns': ['0HVR...', '0HYR...'],
                      'charging_soc_high_limit': 100.0,
                      'charging_soc_low_limit': 10.0,
                      'ct_type': 0,
                      'currency_list': ['RMB', 'EUR', 'GBP', 'USD', ...],
                      'default_ac_couple_power': 100,
                      'default_mode': 0,
                      'device_sn': '0HVR...',
                      'formula_money': 0.4,
                      'grid_connection_control': 0,
                      'grid_set': 1,
                      'model': 'NEXA 2000',
                      'currency': 'EUR',
                      'plant_id': 12345678,
                      'plant_name': 'Solar plant',
                      'plant_list': [{'plant_id': 12345678,
                                      'plant_img_name': None,
                                      'plant_name': 'Solar plant'}],
                      'safety': 1,
                      'safety_enable': True,
                      'safety_list': [{'country_and_area': 'German',
                                       'safety_correspond_num': 1},
                                      {'country_and_area': 'Netherlands',
                                       'safety_correspond_num': 2},
                                      {'country_and_area': 'Belgium',
                                       'safety_correspond_num': 3},
                                      {'country_and_area': 'French',
                                       'safety_correspond_num': 4},
                                      {'country_and_area': 'EN 50549-1',
                                       'safety_correspond_num': 5}],
                      'shelly_list': [],
                      'smart_plan': True,
                      'temp_type': 0,
                      'time_segments': {'time_segment1': None,
                                        'time_segment2': None,
                                        'time_segment3': {'work_mode': 2,
                                                          'start_time': datetime.time(0, 0),
                                                          'end_time': datetime.time(23, 59),
                                                          'power': 0,
                                                          'days': [0]},
                                        'time_segment4': None,
                                        'time_segment5': None,
                                        'time_segment6': None,
                                        'time_segment7': None,
                                        'time_segment8': None,
                                        'time_segment9': None},
                      'version': '11.10.09.07.9000.4017',
                      'work_mode': 2},
             'error_code': 0,
             'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        device_sn = self._device_sn(device_sn)
        noah_or_nexa = self._noah_or_nexa(device_sn=device_sn)

        response = self.session.post(
            endpoint=(
                # /noahDeviceApi/noah/getNoahInfoBySn
                # /noahDeviceApi/nexa/getNexaInfoBySn
                f"noahDeviceApi/{noah_or_nexa}/get{noah_or_nexa.capitalize()}InfoBySn"
            ),
            data={
                "deviceSn": self._device_sn(device_sn),
            },
        )

        # transfer to data structure resembling v4 API
        _error_code = 0 if response.get("result") == 1 else 1
        _msg = response.get("msg")
        _msg = _msg or ("SUCCESSFUL_OPERATION" if _error_code == 0 else "SYSTEM_ERROR")
        # add noah data
        _data = response.get("obj", {}).get("noah", {})
        # add top-level data
        _data["currency_list"] = response.get("obj", {}).get("unitKeyList", {})
        _data["plant_list"] = response.get("obj", {}).get("plantList", {})

        return NoahSettings.model_validate(
            {
                "data": _data,
                "error_code": _error_code,
                "error_msg": _msg,
            }
        )

    def power_chart(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
    ) -> NoahPowerChart:
        """
        Noah/Nexa power chart
        Retrieve power data for one day by device SN.
        ! not part of official API documentation, but reverse-engineered from APP API calls
          * /noahDeviceApi/noah/getNoahChartData
          * /noahDeviceApi/nexa/getNexaChartData

        Notes:
        * data is returned in 5-minute intervals
        * Nexa reports "pac" (load power) as 0.0 all the time, even when load is present
        * contains fix for Nexa has integer overflow on negative values for total_household_load

        Rate limit(s):
        * There seems to be no rate limit for this endpoint, but do not call it too often to avoid being blocked

        Args:
            device_sn (Optional[str]): Inverter serial number
            date_ (Optional[date]): date to retrieve - defaults to today

        Returns:
            NoahPowerChart
            {'data': [{'time': datetime.datetime(2025, 10, 4, 0, 0),
                       'pac': 0.0,
                       'ppv': 0.0,
                       'total_household_load': 0.0},
                      {'time': datetime.datetime(2025, 10, 4, 0, 5),
                       'pac': 0.0,
                       'ppv': 0.0,
                       'total_household_load': 0.0},
                        ...
                      {'time': datetime.datetime(2025, 10, 4, 16, 30),
                       'pac': 0.0,
                       'ppv': 165.5,
                       'total_household_load': 416.0},
                      {'time': datetime.datetime(2025, 10, 4, 16, 35),
                       'pac': 0.0,
                       'ppv': 191.0,
                       'total_household_load': 115.0},
                        ...
                      {'time': datetime.datetime(2025, 10, 4, 23, 55),
                       'pac': 0.0,
                       'ppv': 0.0,
                       'total_household_load': 0.0}],
             'error_code': 0,
             'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        device_sn = self._device_sn(device_sn)
        noah_or_nexa = self._noah_or_nexa(device_sn=device_sn)
        date_ = date_ or datetime.date.today()

        response = self.session.post(
            endpoint=(
                # /noahDeviceApi/noah/getNoahChartData
                # /noahDeviceApi/nexa/getNexaChartData
                f"noahDeviceApi/{noah_or_nexa}/get{noah_or_nexa.capitalize()}ChartData"
            ),
            data={
                "deviceSn": self._device_sn(device_sn),
                # endpoint retrieves data for yesterday, so in order to get data for the day requested, we add a day
                "date": (date_ + datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
            },
        )

        # transfer to data structure resembling v4 API
        _error_code = 0 if response.get("result") == 1 else 1
        _msg = response.get("msg")
        _msg = _msg or ("SUCCESSFUL_OPERATION" if _error_code == 0 else "SYSTEM_ERROR")
        _date_string = date_.strftime("%Y-%m-%d")
        _data = []
        for _time_string in sorted(response.get("obj", {}).keys()):
            _data_item = response.get("obj", {}).get(_time_string, {}).copy()
            _data_item["time"] = f"{_date_string} {_time_string}"  # make it datetime
            _data.append(_data_item)

        npc = NoahPowerChart.model_validate(
            {
                "data": _data,
                "error_code": _error_code,
                "error_msg": _msg,
            }
        )

        # nexa has integer overflow on negative values for total_household_load
        for entry in npc.data:
            if not entry.total_household_load:
                continue
            elif entry.total_household_load > 50000.0:
                # fix overflow by subtracting 65536.0
                entry.total_household_load -= 65536.0
            elif entry.total_household_load > 25000.0:
                # as chart data shows mean values, still values like 32755.5 can occur
                entry.total_household_load -= 65536.0 / 2.0

        return npc

    def energy_chart(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
        period: Optional[Literal["day", "month", "year"]] = None,
    ) -> NoahEnergyChart:
        """
        Noah/Nexa energy chart
        Retrieve energy data per day/month/year for one month/year/total by device SN.
        ! not part of official API documentation, but reverse-engineered from APP API calls
          * /noahDeviceApi/nexa/getDataChart
          * /noahDeviceApi/nexa/getDataChart

        Rate limit(s):
        * There seems to be no rate limit for this endpoint, but do not call it too often to avoid being blocked

        Args:
            device_sn (Optional[str]): Inverter serial number
            date_ (Optional[date]): date to retrieve - defaults to today
            period: ("day" | "month" | "year"): Get data per day (one month) / month (one year) / year - defaults to "day

        Returns:
            NoahEnergyChart
            period="day":
            {'data': [{'time': datetime.date(2025, 10, 1), 'epv': 5.1},
                      ...
                      {'time': datetime.date(2025, 10, 31), 'epv': 0.0}],
             'error_code': 0,
             'error_msg': 'SUCCESSFUL_OPERATION'}

            period="month":
            {'data': [{'time': datetime.date(2025, 1, 1), 'epv': 3.0},
                      ...
                      {'time': datetime.date(2025, 12, 1), 'epv': 0.0}],
             'error_code': 0,
             'error_msg': 'SUCCESSFUL_OPERATION'}

            period="year":
            {'data': [{'time': datetime.date(2020, 1, 1), 'epv': 0.0},
                      ...
                      {'time': datetime.date(2025, 1, 1), 'epv': 123.4}],
             'error_code': 0,
             'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        device_sn = self._device_sn(device_sn)
        noah_or_nexa = self._noah_or_nexa(device_sn=device_sn)
        date_ = date_ or datetime.date.today()
        period = period or "day"
        assert period in ["day", "month", "year"], f"invalid period {period}"
        if period == "year":
            date_type = 3
            date_string = date_.strftime("%Y-01-01")
        elif period == "month":
            date_type = 2
            date_string = date_.strftime("%Y-01-01")
        else:
            date_type = 1
            date_string = date_.strftime("%Y-%m-01")

        response = self.session.post(
            endpoint=(
                # /noahDeviceApi/noah/getDataChart
                # /noahDeviceApi/nexa/getDataChart
                f"noahDeviceApi/{noah_or_nexa}/getDataChart"
            ),
            data={
                "deviceSn": self._device_sn(device_sn),
                # endpoint retrieves data for yesterday, so in order to get data for the day requested, we add a day
                "dateTime": date_string,
                "dateType": date_type,
            },
        )

        # transfer to data structure resembling v4 API
        _error_code = 0 if response.get("result") == 1 else 1
        _msg = response.get("msg")
        _msg = _msg or ("SUCCESSFUL_OPERATION" if _error_code == 0 else "SYSTEM_ERROR")
        _data = []
        for _time_string in sorted(response.get("obj", {}).keys()):
            _data_item = {"epv": response.get("obj", {}).get(_time_string)}
            if period == "year":
                _data_item["time"] = f"{_time_string:>04}-01-01"  # make a date from "01"
            elif period == "month":
                _data_item["time"] = f"{date_.strftime('%Y')}-{_time_string:>02}-01"  # make a date from "01"
            else:
                _data_item["time"] = f"{date_.strftime('%Y-%m')}-{_time_string:>02}"  # make a date from "01"
            _data.append(_data_item)

        return NoahEnergyChart.model_validate(
            {
                "data": _data,
                "error_code": _error_code,
                "error_msg": _msg,
            }
        )

    def details_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> NoahDetailsV4:
        """
        Batch device information using "new-api" endpoint
        Retrieve basic information of devices in bulk based on device SN.
        https://www.showdoc.com.cn/2540838290984246/11292915673945114

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            NoahDetailsV4
            e.g.
            {   'data': {   'noah': [   {   'ac_couple_power_control': 1,
                                            'address': 1,
                                            'alias': None,
                                            'allow_grid_charging': 0,
                                            'ammeter_unbind': 0,
                                            'anti_backflow_enable': 0,
                                            'anti_backflow_power_percentage': 0,
                                            'associated_inv_man_and_model': 0,
                                            'associated_inv_sn': None,
                                            'bms_version': '213007',
                                            'charging_soc_high_limit': 100.0,
                                            'charging_soc_low_limit': 10.0,
                                            'component_power': 0.0,
                                            'datalogger_sn': None,
                                            'default_ac_couple_power': 100,
                                            'default_mode': 0,
                                            'default_power': 100.0,
                                            'device_sn': '0HVR...',
                                            'device_to_grid_power': 0,
                                            'eastron_ammeter_control_pair': 0,
                                            'ebm_order_num': 0,
                                            'fw_version': '230010',
                                            'grid_connection_control': 0,
                                            'grid_to_device_power': 826.0,
                                            'last_update_time': datetime.datetime(2025, 8, 16, 8, 29, 44, tzinfo=TzInfo(UTC)),
                                            'last_update_time_text': datetime.datetime(2025, 8, 16, 16, 29, 44),
                                            'location': None,
                                            'lost': True,
                                            'man_name': None,
                                            'model': None,
                                            'model_name': None,
                                            'mppt_version': '232010',
                                            'ota_device_type_code_high': 'PC',
                                            'ota_device_type_code_low': 'GU',
                                            'pd_version': '231007',
                                            'port_name': 'ShinePano-0HVR...',
                                            'shelly_flag': False,
                                            'smart_socket_power': 0.0,
                                            'status': -1,
                                            'sys_time': datetime.datetime(2025, 8, 16, 0, 33, 39, tzinfo=TzInfo(UTC)),
                                            'temp_type': 0,
                                            'time1_enable': True,
                                            'time1_end': datetime.time(23, 59),
                                            'time1_mode': 2,
                                            'time1_power': 0.0,
                                            'time1_start': datetime.time(0, 0),
                                            'time2_enable': False,
                                            'time2_end': datetime.time(0, 0),
                                            'time2_mode': 0,
                                            'time2_power': 200.0,
                                            'time2_start': datetime.time(0, 0),
                                            'time3_enable': False,
                                            'time3_end': datetime.time(0, 0),
                                            'time3_mode': 0,
                                            'time3_power': 200.0,
                                            'time3_start': datetime.time(0, 0),
                                            'time4_enable': False,
                                            'time4_end': datetime.time(0, 0),
                                            'time4_mode': 0,
                                            'time4_power': 200.0,
                                            'time4_start': datetime.time(0, 0),
                                            'time5_enable': False,
                                            'time5_end': datetime.time(0, 0),
                                            'time5_mode': 0,
                                            'time5_power': 200.0,
                                            'time5_start': datetime.time(0, 0),
                                            'time6_enable': False,
                                            'time6_end': datetime.time(0, 0),
                                            'time6_mode': 0,
                                            'time6_power': 200.0,
                                            'time6_start': datetime.time(0, 0),
                                            'time7_enable': False,
                                            'time7_end': datetime.time(0, 0),
                                            'time7_mode': 0,
                                            'time7_power': 200.0,
                                            'time7_start': datetime.time(0, 0),
                                            'time8_enable': False,
                                            'time8_end': datetime.time(0, 0),
                                            'time8_mode': 0,
                                            'time8_power': 200.0,
                                            'time8_start': datetime.time(0, 0),
                                            'time9_enable': False,
                                            'time9_end': datetime.time(0, 0),
                                            'time9_mode': 0,
                                            'time9_power': 200.0,
                                            'time9_start': datetime.time(0, 0),
                                            'timezone': 2}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.details(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.NOAH,
        )

    def energy_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> NoahEnergyV4:
        """
        Batch equipment data information using "new-api" endpoint
        Retrieve the last detailed data for multiple devices based on their SN and device type.
        https://www.showdoc.com.cn/2540838290984246/11292915898375566

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            {   'data': {   'devices': [   {   'ac_couple_protect_status': 4,
                                               'ac_couple_warn_status': 4,
                                               'battery1_protect_status': 0,
                                               'battery1_serial_num': '0HVR...',
                                               'battery1_soc': 10,
                                               'battery1_temp': 41.0,
                                               'battery1_temp_f': 105.8,
                                               'battery1_warn_status': 0,
                                               'battery2_protect_status': 0,
                                               'battery2_serial_num': None,
                                               'battery2_soc': 0,
                                               'battery2_temp': 0.0,
                                               'battery2_temp_f': 32.0,
                                               'battery2_warn_status': 0,
                                               'battery3_protect_status': 0,
                                               'battery3_serial_num': None,
                                               'battery3_soc': 0,
                                               'battery3_temp': 0.0,
                                               'battery3_temp_f': 32.0,
                                               'battery3_warn_status': 0,
                                               'battery4_protect_status': 0,
                                               'battery4_serial_num': None,
                                               'battery4_soc': 0,
                                               'battery4_temp': 0.0,
                                               'battery4_temp_f': 32.0,
                                               'battery4_warn_status': 0,
                                               'battery_cycles': 1,
                                               'battery_package_quantity': 1,
                                               'battery_soh': 100,
                                               'charge_soc_limit': 100,
                                               'ct_flag': 1,
                                               'ct_self_power': 270.0,
                                               'datalogger_sn': None,
                                               'device_sn': '0HVR...',
                                               'discharge_soc_limit': 10,
                                               'eac_month': 2.0,
                                               'eac_today': 1.1,
                                               'eac_total': 2.0,
                                               'eac_year': 2.0,
                                               'fault_status': 0,
                                               'heating_status': 0,
                                               'household_load_apart_from_groplug': 270.0,
                                               'is_again': 0,
                                               'max_cell_voltage': 3256.0,
                                               'min_cell_voltage': 3253.0,
                                               'mppt_protect_status': 0,
                                               'off_grid_current': 0.0,
                                               'off_grid_power': 0.0,
                                               'off_grid_voltage': 0.0,
                                               'on_grid_current': 0.0,
                                               'on_grid_power': 0.0,
                                               'on_grid_voltage': 1.1,
                                               'on_off_grid': 0,
                                               'pac': 0.0,
                                               'pd_warn_status': 0,
                                               'ppv': 0.0,
                                               'pv1_current': 0.0,
                                               'pv1_temp': 33.3,
                                               'pv1_voltage': 7.29,
                                               'pv2_current': 0.0,
                                               'pv2_temp': 33.3,
                                               'pv2_voltage': 7.23,
                                               'pv3_current': 0.17,
                                               'pv3_temp': 33.7,
                                               'pv3_voltage': 7.29,
                                               'pv4_current': 0.23,
                                               'pv4_temp': 33.7,
                                               'pv4_voltage': 16.73,
                                               'settable_time_period': 0,
                                               'status': 6,
                                               'system_temp': 33.4,
                                               'time': datetime.datetime(2025, 8, 16, 8, 31, 54, 234000, tzinfo=TzInfo(UTC)),
                                               'time_str': datetime.datetime(2025, 8, 16, 16, 31, 54),
                                               'total_battery_pack_charging_power': 0,
                                               'total_battery_pack_charging_status': 0,
                                               'total_battery_pack_soc': 10,
                                               'total_household_load': 270.0,
                                               'work_mode': 2}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy(device_sn=self._device_sn(device_sn), device_type=DeviceType.NOAH)

    def power(
        self,
        device_sn: Optional[str] = None,
    ) -> PowerV4:
        """
        Read power
        Read the active power percentage of the device based on the device type and SN of the device.
        https://www.showdoc.com.cn/2598832417617967/11558661383247816

        Note:
            returns output power (pac_on_grid) in W

        Rate limit(s):
        * The retrieval frequency is once every 5 seconds.

        Args:
            device_sn (Optional[str]): Inverter serial number

        Returns:
            PowerV4
            {   'data': 40,
                'error_code': 0,
                'error_msg': 'success'}
        """

        return self._api_v4.power(device_sn=self._device_sn(device_sn), device_type=DeviceType.NOAH)

    def energy_history_v4(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
    ) -> NoahEnergyHistoryV4:
        """
        One day data using "new-api" endpoint
        Retrieves all detailed data for a specific device on a particular day based on the device SN, device type, and date.
        https://www.showdoc.com.cn/2540838290984246/11292916022305414

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (str): Device unique serial number (SN)
            date_ (Optional[date]): Start Date - defaults to today

        Returns:
            NoahEnergyHistoryV4
            e.g.
            {   'data': {   'datas': [   {
                                             <see energy_v4() for attributes>
                                         }],
                            'have_next': False,
                            'start': 0},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy_history(
            device_sn=self._device_sn(device_sn), device_type=DeviceType.NOAH, date_=date_
        )

    def energy_history_multiple_v4(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        date_: Optional[date] = None,
    ) -> NoahEnergyHistoryMultipleV4:
        """
        One day data using "new-api" endpoint
        Retrieves all detailed data for a specific device on a particular day based on the device SN, device type, and date.
        https://www.showdoc.com.cn/2540838290984246/11292916022305414

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)
            date_ (Optional[date]): Start Date - defaults to today

        Returns:
            NoahEnergyHistoryMultipleV4
            e.g.
            {   'data': {   'NHB691514F': [   {
                                                  <see energy_v4() for attributes>
                                              }]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

        """

        return self._api_v4.energy_history_multiple(
            device_sn=self._device_sn(device_sn), device_type=DeviceType.NOAH, date_=date_
        )

    def setting_write_active_power(
        self,
        active_power_watt: int,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the active power using "new-api" endpoint
        Set the active power percentage of the device based on the device type and SN of the device.
        https://www.showdoc.com.cn/2540838290984246/11330751643769012

        Note:
        * NOAH devices can be configured to 0 ~ 800 W

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            active_power_watt (int): Active power in watt, range 0-800

        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_active_power(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.NOAH,
            active_power=active_power_watt,
        )

    def setting_write_soc_upper_limit(
        self,
        soc_limit: int,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the upper limit of the discharge SOC using "new-api" endpoint
        Set the upper limit of the discharge SOC of the device based on the device type noah and the SN of the device.
        https://www.showdoc.com.cn/2540838290984246/11330751643769012

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            soc_limit (int): discharge SOC upper limit, range 0-100, range 0-100 %

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}
        """

        return self._api_v4.setting_write_soc_upper_limit(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.NOAH,
            soc_limit=soc_limit,
        )

    def setting_write_soc_lower_limit(
        self,
        soc_limit: int,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the lower limit of the discharge SOC using "new-api" endpoint
        Set the lower limit of the discharge SOC of the device based on the device type noah and the SN of the device.
        https://www.showdoc.com.cn/2540838290984246/11330751643769012

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            soc_limit (int): discharge SOC lower limit, range 0-100, range 0-100 %

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}
        """

        return self._api_v4.setting_write_soc_lower_limit(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.NOAH,
            soc_limit=soc_limit,
        )

    def setting_write_time_period(
        self,
        time_period_nr: int,
        start_time: time,
        end_time: time,
        load_priority: bool,
        power_watt: int,
        enabled: bool,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the lower limit of the discharge SOC using "new-api" endpoint
        Set the lower limit of the discharge SOC of the device based on the device type noah and the SN of the device.
        https://www.showdoc.com.cn/2540838290984246/11330751643769012

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            time_period_nr (int): time period number - range 1 ~ 9
            start_time (datetime.time): period start time
            end_time (datetime.time): period end time
            load_priority (bool): priority setting - True = load priority, False = battery priority
            power_watt (int): output power - range 0 ~ 800 W
            enabled (bool): time period switch - True = on, False = off

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}
        """

        return self._api_v4.setting_write_time_period(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.NOAH,
            time_period_nr=time_period_nr,
            start_time=start_time,
            end_time=end_time,
            load_priority=load_priority,
            power_watt=power_watt,
            enabled=enabled,
        )

    def setting_write_assign_inverter(
        self,
        device_sn: str,
        inverter_sn: str,  # e.g. "NYR0N9W15U"
        inverter_model_id: str,  # e.g. "0x0105"
        inverter_brand_name: str,  # e.g. "Growatt"
        inverter_model_name: str,  # e.g. "NEO 2000M-X2"
        inverter_type: int = 0,  # e.g. # 0
    ) -> SettingWriteV4:
        """
        Set Noah Device
        Set the device's associated inverter and other third-party devices according to the device type noah and the device's SN.
        https://www.showdoc.com.cn/2598832417617967/11558661385169048

        Values to use for inverter_* parameters can be obtained from https://www.showdoc.com.cn/p/469a02fee3555b1661a25ecfed1cd821

        !!! WARNING !!! this endpoint was neither tried out, tested nor verified! Use at your own risk!

        Note:
        * This API is only applicable to NOAH device type

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            inverter_sn (str): Serial number of inverter to assign to NOAH device
            inverter_model_id (str): Model ID of inverter in hex format, e.g. "0x0105" - see https://www.showdoc.com.cn/p/469a02fee3555b1661a25ecfed1cd821
            inverter_brand_name (str): Manufacturer of inverter, e.g. "Growatt" - see https://www.showdoc.com.cn/p/469a02fee3555b1661a25ecfed1cd821
            inverter_model_name (str): Model name of inverter, e.g. "NEO 2000M-X2" - see https://www.showdoc.com.cn/p/469a02fee3555b1661a25ecfed1cd821
            inverter_type (int) = 0  # 0=inverter - see https://www.showdoc.com.cn/p/469a02fee3555b1661a25ecfed1cd821

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_assign_inverter(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.NOAH,
            inverter_sn=inverter_sn,
            inverter_model_id=inverter_model_id,
            inverter_brand_name=inverter_brand_name,
            inverter_model_name=inverter_model_name,
            inverter_type=inverter_type,
        )

    def setting_write_grid_charging(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        grid_charging: bool,
    ) -> SettingWriteV4:
        """
        Set whether to allow charging from the grid
        Set whether to allow charging from the grid of the device based on the device type noah and the SN of the device.
        https://www.showdoc.com.cn/2598832417617967/11558677502514466

        Note:
        * This API is only applicable to NOAH device type

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            grid_charging (bool): True=enabled, False=disabled

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_grid_charging(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.NOAH,
            grid_charging=grid_charging,
        )

    def setting_write_off_grid(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        off_grid: bool,
    ) -> SettingWriteV4:
        """
        Setting off-grid enable
        Setting off-grid enable of the device based on the device type noah and the SN of the device
        https://www.showdoc.com.cn/2598832417617967/11558677526814378

        Note:
        * This API is only applicable to NOAH device type

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            off_grid (bool): True=enabled, False=disabled

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_off_grid(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.NOAH,
            off_grid=off_grid,
        )

    def wifi_strength(  # noqa: C901 'ApiV4.power' is too complex (11)
        self,
        device_sn: str,
    ) -> WifiStrengthV4:
        """
        Get the collector signal value
        Get the network signal value of the collector through the SN of the device
        https://www.showdoc.com.cn/2598832417617967/11558704404033100

        Rate limit(s):
        * The retrieval frequency is once every 5 seconds.

        Args:
            device_sn (Optional[str]): Inverter serial number

        Returns:
            WifiStrengthV4
            {   'data': -46,
                'error_code': 0,
                'error_msg': 'success'}
        """

        return self._api_v4.wifi_strength(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.NOAH,
        )

    def firmware_info(
        self,
        device_sn: Optional[str] = None,
    ) -> NoahFirmwareInfo:
        """
        Noah/Nexa firmware version
        Retrieve current and latest firmware version
        ! not part of official API documentation, but reverse-engineered from APP API calls
          * /noahDeviceApi/noah/checkUpgradeNoah
          * /noahDeviceApi/nexa/checkUpgradeNexa

        Rate limit(s):
        * There seems to be no rate limit for this endpoint, but do not call it too often to avoid being blocked

        Args:
            device_sn (Optional[str]): Inverter serial number

        Returns:
            NoahFirmwareInfo
            {'data': {'update_available': False,
                      'current_version': '11.10.09.07.9000.4017',
                      'latest_version': '11.10.09.07.9000.4017',
                      'status': 6},
             'error_code': 0,
             'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        device_sn = self._device_sn(device_sn)
        noah_or_nexa = self._noah_or_nexa(device_sn=device_sn)
        response = self.session.post(
            endpoint=(
                # /noahDeviceApi/noah/checkUpgradeNoah
                # /noahDeviceApi/nexa/checkUpgradeNexa
                f"noahDeviceApi/{noah_or_nexa}/checkUpgrade{noah_or_nexa.capitalize()}"
            ),
            data={
                "deviceSn": device_sn,
            },
        )

        # transfer to data structure resembling v4 API
        _error_code = 0 if response.get("result") == 1 else 1
        _msg = response.get("msg")
        _msg = _msg or ("SUCCESSFUL_OPERATION" if _error_code == 0 else "SYSTEM_ERROR")
        _data = response.get("obj", {})

        return NoahFirmwareInfo.model_validate(
            {
                "data": _data,
                "error_code": _error_code,
                "error_msg": _msg,
            }
        )
