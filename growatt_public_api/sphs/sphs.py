from datetime import date
from typing import Union, List, Optional
from ..api_v4 import ApiV4
from ..growatt_types import DeviceType
from ..pydantic_models.api_v4 import (
    SphsEnergyHistoryV4,
    SphsEnergyHistoryMultipleV4,
    SettingWriteV4,
    SphsDetailsV4,
    SphsEnergyV4,
)
from ..session import GrowattApiSession


class Sphs:
    """
    endpoints for SPH-S devices
    https://www.showdoc.com.cn/2540838290984246/11292929153206911
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
    ) -> SphsDetailsV4:
        """
        Batch device information using "new-api" endpoint
        Retrieve basic information of devices in bulk based on device SN.
        https://www.showdoc.com.cn/2540838290984246/11292915673945114

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            SphsDetailsV4
            e.g.
            {   'data': {   'sphs': [   {   'active_rate': 100,
                                            'address': 1,
                                            'alias': 'EFP0N1J023',
                                            'baudrate': None,
                                            'children': None,
                                            'com_address': 1,
                                            'communication_version': 'SKaa-0001',
                                            'country_selected': 1,
                                            'datalogger_sn': 'VC41010123438079',
                                            'device_type': 280,
                                            'dtc': 21200,
                                            'e_today': 0.0,
                                            'e_total': 0.0,
                                            'energy_day': 0.0,
                                            'energy_day_map': {},
                                            'energy_month': 0.0,
                                            'energy_month_text': '0',
                                            'export_limit': 1,
                                            'export_limit_power_rate': 100.0,
                                            'failsafe': 0,
                                            'freq_high_limit': 60.5,
                                            'freq_low_limit': 59.3,
                                            'fw_version': 'UL2.1',
                                            'group_id': -1,
                                            'img_path': './css/img/status_gray.gif',
                                            'last_update_time': 1720838845000,
                                            'last_update_time_text': datetime.datetime(2024, 7, 13, 10, 47, 25),
                                            'lcd_language': 1,
                                            'level': 4,
                                            'location': None,
                                            'lost': True,
                                            'manufacturer': None,
                                            'modbus_version': 207,
                                            'model': 0,
                                            'model_text': 'S00B00D00T00P00U00M0000',
                                            'p_charge': 0.0,
                                            'p_discharge': 0.0,
                                            'parent_id': 'LIST_VC41010123438079_260',
                                            'plant_id': 0,
                                            'plant_name': None,
                                            'pmax': 15000,
                                            'port_name': 'ShinePano - VC41010123438079',
                                            'power': 0.0,
                                            'power_max': None,
                                            'power_max_text': None,
                                            'power_max_time': None,
                                            'pv_pf_cmd_memory_state': False,
                                            'reactive_output_priority': 1,
                                            'reactive_rate': 100,
                                            'reactive_value': 1000.0,
                                            'record': None,
                                            'serial_num': 'EFP0N1J023',
                                            'sph_set_bean': None,
                                            'status': -1,
                                            'status_text': 'sph.status.lost',
                                            'sys_time': datetime.datetime(2018, 1, 1, 0, 0),
                                            'sys_time_text': datetime.datetime(2018, 1, 1, 0, 0),
                                            'tcp_server_ip': '127.0.0.1',
                                            'timezone': 8.0,
                                            'tree_id': None,
                                            'tree_name': 'EFP0N1J023',
                                            'updating': False,
                                            'user_name': None,
                                            'uw_grid_watt_delay': 1000.0,
                                            'uw_nominal_grid_volt': 0.0,
                                            'uw_reconnect_start_slope': 10.0,
                                            'version': 'ULSP0101xx',
                                            'vnormal': 350.0,
                                            'voltage_high_limit': 264.0,
                                            'voltage_low_limit': 213.0}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.details(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.SPHS,
        )

    def energy_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> SphsEnergyV4:
        """
        Batch equipment data information using "new-api" endpoint
        Retrieve the last detailed data for multiple devices based on their SN and device type.
        https://www.showdoc.com.cn/2540838290984246/11292915898375566

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            SphsEnergyV4
            e.g.
            {   'code': 0,
                'data': {   'sph-s': [   {   'again': False,
                                             'batPower': 0.0,
                                             'bmsBatteryCurr': 0.0,
                                             'bmsBatteryTemp': 31.7,
                                             'bmsBatteryVolt': 5.31,
                                             'bmsConstantVolt': 5.68,
                                             'bmsSOC': 96,
                                             'bmsSOH': 0,
                                             'bmsUsingCap': 2000,
                                             'calendar': 1720838845025,
                                             'chipType': 0,
                                             'dataLogSn': 'VC41010123438079',
                                             'dayMap': None,
                                             'dcTemp': 58.7,
                                             'deviceType': 0,
                                             'eToGridHour': 0.0,
                                             'eToGridMonth': 0.1,
                                             'eToGridYear': 6.8,
                                             'eToUserHour': 0.0,
                                             'eToUserMonth': 160.9,
                                             'eToUserYear': 870.9,
                                             'eacToday': 0.0,
                                             'eacTotal': 1040.9,
                                             'echarge1Today': 0.0,
                                             'echarge1Total': 432.6,
                                             'edischarge1Today': 0.0,
                                             'edischarge1Total': 460.8,
                                             'elocalLoadHour': 0.2,
                                             'elocalLoadMonth': 433.0,
                                             'elocalLoadToday': 1.0,
                                             'elocalLoadTotal': 2024.8,
                                             'elocalLoadYear': 1741.8,
                                             'epsIac1': 8.4,
                                             'epsIac2': 0.0,
                                             'epsVac2': 0.0,
                                             'epv1Today': 0.0,
                                             'epv1Total': 0.0,
                                             'epv2Today': 0.0,
                                             'epv2Total': 0.0,
                                             'epv3Today': 0.800000011920929,
                                             'epv3Total': 0.0,
                                             'epvHour': 0.2,
                                             'epvMonth': 214.2,
                                             'epvToday': 0.8,
                                             'epvTotal': 1132.5,
                                             'epvYear': 1132.5,
                                             'errorText': 'Unknown',
                                             'eselfHour': 0.2,
                                             'eselfMonth': 272.1,
                                             'eselfYear': 1586.5,
                                             'eselftoday': 0.800000011920929,
                                             'eselftotal': 1586.5,
                                             'esystemHour': 0.2,
                                             'esystemMonth': 272.2,
                                             'esystemYear': 1593.3,
                                             'esystemtoday': 0.800000011920929,
                                             'esystemtotal': 1593.300048828125,
                                             'etoGridToday': 0.0,
                                             'etoGridTotal': 6.8,
                                             'etoUserToday': 0.2,
                                             'etoUserTotal': 870.9,
                                             'fac': 50.02,
                                             'faultBitCode': 0,
                                             'faultCode': 0,
                                             'genCurr': 0.0,
                                             'genEnergy': 0.0,
                                             'genEnergyToday': 0.0,
                                             'genFreq': 0.0,
                                             'genPower': 0.0,
                                             'genVol': 0.0,
                                             'gridStatus': 1,
                                             'hmiVersion': None,
                                             'iac1': 1.0,
                                             'iac2': 0.0,
                                             'ibat': 0.0,
                                             'invTemp': 48.0,
                                             'ipv1': 0.0,
                                             'ipv2': 0.0,
                                             'ipv3': 5.5,
                                             'loadPower1': 2169.0,
                                             'loadPower2': 0.0,
                                             'lost': True,
                                             'm1Version': None,
                                             'm2Version': None,
                                             'pac': 1871.0,
                                             'pac1': 138.0,
                                             'pac2': 0.0,
                                             'pacToGridR': 0.0,
                                             'pacToGridS': 0.0,
                                             'pacToGridTotal': 0.0,
                                             'pacToUserR': 138.0,
                                             'pacToUserTotal': 0.0,
                                             'pcharge1': 0.0,
                                             'pdischarge1': 0.0,
                                             'pex': 1871.0,
                                             'pf': -1.0,
                                             'plocalLoadR': 0.0,
                                             'plocalLoadS': 0.0,
                                             'plocalLoadTotal': 1871.0,
                                             'ppv': 1920.0,
                                             'ppv1': 0.0,
                                             'ppv2': 0.0,
                                             'ppv3': 1920.0,
                                             'ppvText': '1920.0 W',
                                             'priorityChoose': 0,
                                             'pself': 1920.0,
                                             'psystem': 1920.0,
                                             'rLoadVol': 230.6,
                                             'rLocalEnergy': 1820.7,
                                             'sLoadVol': 0.0,
                                             'sLocalEnergy': 0.0,
                                             'serialNum': 'EFP0N1J023',
                                             'soc': 96,
                                             'socText': '96%',
                                             'spStatus': 1,
                                             'sphBean': None,
                                             'status': 3,
                                             'statusText': 'Bat Online',
                                             'sysFaultWord': 12337,
                                             'sysFaultWord1': 12851,
                                             'sysFaultWord2': 13365,
                                             'sysFaultWord3': 13879,
                                             'sysFaultWord4': 14393,
                                             'sysFaultWord5': 16706,
                                             'sysFaultWord6': 17220,
                                             'sysFaultWord7': 17734,
                                             'sysStatus': 6,
                                             'systemFault': 0,
                                             'systemWarn': 0,
                                             'time': '2024-07-13 10:47:25',
                                             'timeTotal': 0.0,
                                             'upsFac': 50.0,
                                             'upsPac1': 1871.0,
                                             'upsPac2': 0.0,
                                             'upsVac1': 230.1999969482422,
                                             'uwSysWorkMode': 6,
                                             'vac1': 230.5,
                                             'vac2': 0.0,
                                             'vbat': 53.1,
                                             'vbat1': 53.0,
                                             'vpv1': 0.0,
                                             'vpv2': 0.0,
                                             'vpv3': 342.2,
                                             'warnCode': 0,
                                             'warnCode1': 0,
                                             'warnText': 'Unknown',
                                             'withTime': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy(device_sn=self._device_sn(device_sn), device_type=DeviceType.SPHS)

    def energy_history_v4(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
    ) -> SphsEnergyHistoryV4:
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
            SphsEnergyHistoryV4
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
            device_sn=self._device_sn(device_sn), device_type=DeviceType.SPHS, date_=date_
        )

    def energy_history_multiple_v4(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        date_: Optional[date] = None,
    ) -> SphsEnergyHistoryMultipleV4:
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
            SphsEnergyHistoryMultipleV4
            e.g.
            {   'data': {   'NHB691514F': [   {
                                                  <see energy_v4() for attributes>
                                              }]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

        """

        return self._api_v4.energy_history_multiple(
            device_sn=self._device_sn(device_sn), device_type=DeviceType.SPHS, date_=date_
        )

    def setting_write_on_off(
        self,
        power_on: bool,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the power on and off using "new-api" endpoint
        Turn device on/off
        https://www.showdoc.com.cn/2540838290984246/11330750679726415

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            power_on (bool): True = Power On, False = Power Off

        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}
        """

        return self._api_v4.setting_write_on_off(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.SPHS,
            power_on=power_on,
        )

    def setting_write_active_power(
        self,
        active_power_percent: int,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the active power using "new-api" endpoint
        Set the active power percentage of the device based on the device type and SN of the device.
        https://www.showdoc.com.cn/2540838290984246/11330751643769012

        Attention:
        not sure if this works for SPH-S. Test API returns "error code 7: WRONG_DEVICE_TYPE"

        Note:
        * most devices can be configured to 0 ~ 100 %
        * NOAH devices can be configured to 0 ~ 800 W

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            active_power_percent (int): Percentage of active power, range 0-100

        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_active_power(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.SPHS,
            active_power=active_power_percent,
        )
