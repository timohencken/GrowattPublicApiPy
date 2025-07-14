from datetime import date, time
from typing import Union, List, Optional
from ..api_v4 import ApiV4
from ..growatt_types import DeviceType
from ..pydantic_models.api_v4 import (
    NoahDetailsV4,
    NoahEnergyV4,
    NoahEnergyHistoryV4,
    NoahEnergyHistoryMultipleV4,
    SettingWriteV4,
)
from ..session.growatt_api_session import GrowattApiSession  # noqa: E402


class Noah:
    """
    endpoints for NOAH devices
    https://www.showdoc.com.cn/2540838290984246/11315140426110613
    """

    session: GrowattApiSession
    _api_v4: ApiV4
    device_sn: Optional[str] = None

    def __init__(self, session: GrowattApiSession, device_sn: Optional[str] = None) -> None:
        self.session = session
        self._api_v4 = ApiV4(session)
        self.device_sn = device_sn

    def _device_sn(self, device_sn: Optional[Union[str, List[str]]]) -> Union[str, List[str]]:
        """
        Use device_sn explicitly provided, fallback to the one from the instance
        """
        device_sn = device_sn or self.device_sn
        if device_sn is None:
            raise AttributeError("device_sn must be provided")
        return device_sn

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
            {   'data': {   'noah': [   {   'address': 1,
                                            'alias': None,
                                            'associated_inv_sn': None,
                                            'bms_version': '213005',
                                            'charging_soc_high_limit': 100.0,
                                            'charging_soc_low_limit': 0.0,
                                            'component_power': 0.0,
                                            'datalogger_sn': None,
                                            'default_power': 200.0,
                                            'device_sn': '0PVPOXIEGENGHUI1',
                                            'ebm_order_num': 0,
                                            'fw_version': None,
                                            'last_update_time': 1720667148000,
                                            'last_update_time_text': datetime.datetime(2024, 7, 11, 11, 5, 48),
                                            'location': None,
                                            'lost': False,
                                            'model': 'Noah 2000',
                                            'mppt_version': '212004',
                                            'ota_device_type_code_high': 'PB',
                                            'ota_device_type_code_low': 'FU',
                                            'pd_version': '211005',
                                            'port_name': 'ShinePano-0PVPOXIEGENGHUI1',
                                            'smart_socket_power': 0.0,
                                            'status': 0,
                                            'sys_time': 1720660008000,
                                            'temp_type': 0,
                                            'time1_enable': True,
                                            'time1_end': datetime.time(23, 59),
                                            'time1_mode': 0,
                                            'time1_power': 400.0,
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
                                            'time9_start': datetime.time(0, 0)}]},
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
            Note: NOAH documentation is VERY incomplete
                  (see https://www.showdoc.com.cn/2540838290984246/11315141402697236 - json shows SPH-S instead).
                  Therefore, attributes listed here are possible not complete.
                  A real NOAH device would be required to find the correct attributes
            {   'data': {   'noah': [   {   'battery1_protect_status': None,
                                            'battery1_serial_num': None,
                                            'battery1_soc': None,
                                            'battery1_temp': None,
                                            'battery1_warn_status': None,
                                            'battery2_protect_status': None,
                                            'battery2_serial_num': None,
                                            'battery2_soc': None,
                                            'battery2_temp': None,
                                            'battery2_warn_status': None,
                                            'battery3_protect_status': None,
                                            'battery3_serial_num': None,
                                            'battery3_soc': None,
                                            'battery3_temp': None,
                                            'battery3_warn_status': None,
                                            'battery4_protect_status': None,
                                            'battery4_serial_num': None,
                                            'battery4_soc': None,
                                            'battery4_temp': None,
                                            'battery4_warn_status': None,
                                            'battery_package_quantity': None,
                                            'datalogger_sn': None,
                                            'device_sn': None,
                                            'eac_month': None,
                                            'eac_today': None,
                                            'eac_total': None,
                                            'eac_year': None,
                                            'fault_status': None,
                                            'heating_status': None,
                                            'is_Again': None,
                                            'mppt_protect_status': None,
                                            'pac': None,
                                            'pd_warn_status': None,
                                            'ppv': None,
                                            'status': None,
                                            'time': None,
                                            'total_battery_pack_charging_power': None,
                                            'total_battery_pack_charging_status': None,
                                            'total_battery_pack_soc': None,
                                            'work_mode': None}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy(device_sn=self._device_sn(device_sn), device_type=DeviceType.NOAH)

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
