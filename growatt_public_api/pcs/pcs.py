from datetime import date, timedelta
from typing import Optional
from ..pydantic_models.pcs import (
    PcsDetails,
    PcsEnergyOverview,
    PcsEnergyHistory,
    PcsAlarms,
)
from ..session.growatt_api_session import GrowattApiSession  # noqa: E402


class Pcs:
    """
    endpoints for PCS inverters
    https://www.showdoc.com.cn/262556420217021/6129831722860832

    Note:
        Only applicable to devices with device type 8 (pcs) returned by plant.list_devices()
    """

    session: GrowattApiSession
    device_sn: Optional[str] = None

    def __init__(self, session: GrowattApiSession, device_sn: Optional[str] = None) -> None:
        self.session = session
        self.device_sn = device_sn

    def _device_sn(self, device_sn: Optional[str]) -> str:
        """
        Use device_sn explicitly provided, fallback to the one from the instance
        """
        device_sn = device_sn or self.device_sn
        if device_sn is None:
            raise AttributeError("device_sn must be provided")
        return device_sn

    def details(
        self,
        device_sn: Optional[str] = None,
    ) -> PcsDetails:
        """
        Get Pcs basic information
        Interface to get basic information of pcs
        https://www.showdoc.com.cn/262556420217021/6129831722860832

        Note:
            Only applicable to devices with device type 8 (pcs) returned by plant.list_devices()

        Args:
            device_sn (str): PCS device SN

        Returns:
            PcsDetails
            {   'data': {   'address': 9,
                            'alias': 'PCS000001',
                            'charge_day_map': {},
                            'charge_month': 0,
                            'charge_month_text': '0',
                            'children': [],
                            'datalogger_sn': 'MONITOR002',
                            'discharge_day_map': {},
                            'discharge_month': 0.0,
                            'discharge_month_2': 0.0,
                            'discharge_month_text': '0',
                            'e_charge_today': 0.0,
                            'e_discharge_today': 0.0,
                            'e_discharge_total': 0.0,
                            'energy_day': None,
                            'energy_day_map': {},
                            'energy_month': 0.0,
                            'energy_month_text': '0',
                            'fw_version': 'AB02',
                            'group_id': -1,
                            'img_path': './css/img/status_gray.gif',
                            'inner_version': '2017',
                            'last_update_time': {'date': 27, 'day': 1, 'hours': 16, 'minutes': 26, 'month': 6, 'seconds': 14, 'time': 1595838374000, 'timezone_offset': -480, 'year': 120},
                            'last_update_time_text': datetime.datetime(2020, 7, 27, 16, 26, 14),
                            'level': 6,
                            'location': None,
                            'lost': False,
                            'model': 0,
                            'model_text': 'A0B0D0T0P0U0M0S0',
                            'normalPower': 500000,
                            'parent_id': 'LIST_MONITOR002_3',
                            'peak_clipping': 0.0,
                            'peak_clipping_total': 0.0,
                            'plant_id': 0,
                            'plant_name': None,
                            'port_name': 'ShinePano-MONITOR002',
                            'record': None,
                            'serial_num': 'PCS000001',
                            'status': 2,
                            'status_text': 'pcs.status.normal',
                            'tcp_server_ip': '47.107.154.111',
                            'tree_id': 'PCS000001',
                            'tree_name': 'PCS000001',
                            'updating': False,
                            'user_name': None},
                'datalogger_sn': 'MONITOR002',
                'device_sn': 'PCS000001',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/pcs/pcs_data_info",
            params={
                "device_sn": self._device_sn(device_sn),
            },
        )

        return PcsDetails.model_validate(response)

    def energy(
        self,
        device_sn: Optional[str] = None,
    ) -> PcsEnergyOverview:
        """
        Get the latest real-time data of Pcs
        Interface to get the latest real-time data of pcs
        https://www.showdoc.com.cn/262556420217021/6131235037123575

        Note:
            Only applicable to devices with device type 8 (pcs) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: Pcs does not exist
        * 10003: device SN error

        Args:
            device_sn (str): PCS serial number

        Returns:
            PcsEnergyOverview
            {   'data': {   'address': 0,
                            'again': False,
                            'alarm_code1': 0,
                            'alarm_code2': 0,
                            'alias': None,
                            'ats_bypass': 0,
                            'b_active_power': 19.0,
                            'b_apparent_power': 18.0,
                            'b_reactive_power': 20.0,
                            'bipv': 2.0,
                            'bipvu': 7.0,
                            'bipvv': 8.0,
                            'bipvw': 9.0,
                            'bms_protection': 0,
                            'bms_status': 6,
                            'bms_volt_status': 1690,
                            'bvbus': 59.0,
                            'bvbus_nega': 61.0,
                            'bvbus_posi': 60.0,
                            'bvpv': 1.0,
                            'bvpvuv': 13.0,
                            'bvpvvw': 14.0,
                            'bvpvwu': 15.0,
                            'bypass_freq': 8.100000381469727,
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 11, 'day': 4, 'hours': 17, 'minutes': 6, 'month': 5, 'seconds': 9, 'time': 1591866369000, 'timezone_offset': -480, 'year': 120},
                                            'time_in_millis': 1591866369000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2020,
                                            'weeks_in_week_year': 52},
                            'capacity': 470.0,
                            'datalogger_sn': None,
                            'day': None,
                            'dg_grid_power': 0.0,
                            'dg_grid_select': 0,
                            'e_charge_time_today': 27.0,
                            'e_charge_time_total': 1690932.0,
                            'e_charge_today': 26.0,
                            'e_charge_total': 1690930.0,
                            'e_discharge_time_today': 25.0,
                            'e_discharge_time_total': 1690932.0,
                            'e_discharge_today': 24.0,
                            'e_discharge_total': 1690930.0,
                            'electric_state': 5,
                            'gfdi1': 42.0,
                            'gfdi2': 43.0,
                            'grid_freq': 210.0,
                            'grid_time_today': 95.0,
                            'grid_time_total': 6422627.0,
                            'grid_today': 94.0,
                            'grid_total': 6291553.0,
                            'i1a': 10.0,
                            'i1b': 11.0,
                            'i1c': 12.0,
                            'load_active_power': 49.0,
                            'load_apparent_power': 48.0,
                            'load_ia': 53.0,
                            'load_ib': 54.0,
                            'load_ic': 55.0,
                            'load_pf': 52.0,
                            'load_reactive_power': 50.0,
                            'load_time_today': 83.0,
                            'load_time_total': 5636183.0,
                            'load_today': 82.0,
                            'load_total': 5505109.0,
                            'lost': True,
                            'max_charge_curr': 100.0,
                            'max_discharge_curr': 101.0,
                            'max_min_temp_cell': 6.0,
                            'max_temp': 6.0,
                            'max_temp_num': 6.0,
                            'max_volt': 1.0,
                            'max_volt_cell': 6.0,
                            'max_volt_num': 194.0,
                            'maxmin_volt_cell': 6.0,
                            'min_temp': 174.0,
                            'min_temp_group': 134.0,
                            'min_temp_num': 164.0,
                            'min_volt': 1.0,
                            'min_volt_cell': 6.0,
                            'min_volt_group': 144.0,
                            'min_volt_num': 184.0,
                            'mvpv': 0.46000000834465027,
                            'out_apparent_power': 78.0,
                            'out_reactive_power': 80.0,
                            'pac_to_battery': 17.0,
                            'pac_to_grid': 0.0,
                            'pcs_active_power': 79.0,
                            'pcs_bean': None,
                            'pf': 0.23000000417232513,
                            'pf_symbol': 220,
                            'power_grid': 0.0,
                            'ppv': 108000.0,
                            'pv_energy': 0.0,
                            'riso_batn': 41.0,
                            'riso_batp': 40.0,
                            'self_time': 450.0,
                            'serial_num': 'TND093000E',
                            'status': 2,
                            'status_lang': 'common_normal',
                            'status_text': 'OnGridState',
                            'sys_fault_word1': 8192,
                            'sys_fault_word2': 512,
                            'sys_fault_word3': 256,
                            'sys_fault_word4': 0,
                            'sys_fault_word5': 32816,
                            'sys_fault_word6': 160,
                            'sys_fault_word7': 0,
                            'sys_fault_word8': 0,
                            'temp1': 30.0,
                            'temp2': 31.0,
                            'temp3': 32.0,
                            'temp4': 33.0,
                            'temp5': 35.0,
                            'temp6': 36.0,
                            'time': datetime.datetime(2020, 6, 11, 17, 6, 9),
                            'to_grid_time_today': 89.0,
                            'to_grid_time_total': 6029405.0,
                            'to_grid_today': 88.0,
                            'to_grid_total': 5898331.0,
                            'to_power_grid': 0.0,
                            'type_flag': 1430,
                            'vac_frequency': 1.600000023841858,
                            'vacu': 135.0,
                            'vacuv': 4.0,
                            'vacv': 136.0,
                            'vacvw': 5.0,
                            'vacw': 137.0,
                            'vacwu': 6.0,
                            'vpvuv': 56.0,
                            'vpvvw': 57.0,
                            'vpvwu': 58.0,
                            'with_time': False},
                'datalogger_sn': 'WFD0947012',
                'device_sn': 'TND093000E',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/pcs/pcs_last_data",
            data={
                "pcs_sn": self._device_sn(device_sn),
            },
        )

        return PcsEnergyOverview.model_validate(response)

    def energy_history(
        self,
        device_sn: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PcsEnergyHistory:
        """
        Obtain historical data of a Pcs
        Interface to get historical data of a certain pcs
        https://www.showdoc.com.cn/262556420217021/6131245575367488

        Note:
            Only applicable to devices with device type 8 (pcs) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: Pcs does not exist
        * 10003: device SN error

        Args:
            device_sn (str): PCS serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            PcsEnergyHistory
            {   'data': {   'count': 479,
                            'datalogger_sn': 'MONITOR001',
                            'datas': [   {   'address': 0,
                                             'again': False,
                                             'alarm_code1': 0,
                                             'alarm_code2': 0,
                                             'alias': None,
                                             'ats_bypass': 0,
                                             'b_active_power': 0.0,
                                             'b_apparent_power': 0.0,
                                             'b_reactive_power': 0.0,
                                             'bipv': 3.0999999046325684,
                                             'bipvu': 0.0,
                                             'bipvv': 0.0,
                                             'bipvw': 0.0,
                                             'bms_protection': 0,
                                             'bms_status': 254,
                                             'bms_volt_status': 0,
                                             'bvbus': 0.0,
                                             'bvbus_nega': 0.0,
                                             'bvbus_posi': 0.0,
                                             'bvpv': -0.699999988079071,
                                             'bvpvuv': 4.099999904632568,
                                             'bvpvvw': 1.2000000476837158,
                                             'bvpvwu': 2.0,
                                             'bypass_freq': 0.0,
                                             'calendar': {   'first_day_of_week': 1,
                                                             'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                             'lenient': True,
                                                             'minimal_days_in_first_week': 1,
                                                             'time': {'date': 28, 'day': 2, 'hours': 13, 'minutes': 32, 'month': 6, 'seconds': 43, 'time': 1595914363000, 'timezone_offset': -480, 'year': 120},
                                                             'time_in_millis': 1595914363000,
                                                             'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                             'week_date_supported': True,
                                                             'week_year': 2020,
                                                             'weeks_in_week_year': 52},
                                             'capacity': 48130.0,
                                             'datalogger_sn': None,
                                             'day': None,
                                             'dg_grid_power': 0.0,
                                             'dg_grid_select': 0,
                                             'e_charge_time_today': 0.0,
                                             'e_charge_time_total': 0.0,
                                             'e_charge_today': 0.0,
                                             'e_charge_total': 0.0,
                                             'e_discharge_time_today': 0.0,
                                             'e_discharge_time_total': 0.0,
                                             'e_discharge_today': 0.0,
                                             'e_discharge_total': 0.0,
                                             'electric_state': -1,
                                             'gfdi1': 0.0,
                                             'gfdi2': 0.0,
                                             'grid_freq': 0.0,
                                             'grid_time_today': 0.0,
                                             'grid_time_total': 0.0,
                                             'grid_today': 0.0,
                                             'grid_total': 0.0,
                                             'i1a': 2.5999999046325684,
                                             'i1b': 2.700000047683716,
                                             'i1c': 5.199999809265137,
                                             'load_active_power': 0.0,
                                             'load_apparent_power': 0.0,
                                             'load_ia': 1.100000023841858,
                                             'load_ib': 0.20000000298023224,
                                             'load_ic': 0.20000000298023224,
                                             'load_pf': 0.0,
                                             'load_reactive_power': 0.0,
                                             'load_time_today': 0.0,
                                             'load_time_total': 0.0,
                                             'load_today': 0.0,
                                             'load_total': 0.0,
                                             'lost': True,
                                             'max_charge_curr': 0.0,
                                             'max_discharge_curr': 0.0,
                                             'max_min_temp_cell': 0.0,
                                             'max_temp': 157.0,
                                             'max_temp_num': 0.0,
                                             'max_volt': 65.0,
                                             'max_volt_cell': 0.0,
                                             'max_volt_num': 0.0,
                                             'maxmin_volt_cell': 0.0,
                                             'min_temp': 174.0,
                                             'min_temp_group': 0.0,
                                             'min_temp_num': 0.0,
                                             'min_volt': 8.0,
                                             'min_volt_cell': 0.0,
                                             'min_volt_group': 0.0,
                                             'min_volt_num': 0.0,
                                             'mvpv': 0.0,
                                             'out_apparent_power': 0.0,
                                             'out_reactive_power': 0.0,
                                             'pac_to_battery': 0.0,
                                             'pac_to_grid': 0.0,
                                             'pcs_active_power': 0.0,
                                             'pcs_bean': None,
                                             'pf': 1.0,
                                             'pf_symbol': 0,
                                             'power_grid': 0.0,
                                             'ppv': 0.0,
                                             'pv_energy': 0.0,
                                             'riso_batn': 1000.0,
                                             'riso_batp': 1000.0,
                                             'self_time': 60.0,
                                             'serial_num': 'PCS1234567',
                                             'status': 3,
                                             'status_lang': 'common_error',
                                             'status_text': 'FaultState',
                                             'sys_fault_word1': 0,
                                             'sys_fault_word2': 10240,
                                             'sys_fault_word3': 256,
                                             'sys_fault_word4': 0,
                                             'sys_fault_word5': 16,
                                             'sys_fault_word6': -1,
                                             'sys_fault_word7': 0,
                                             'sys_fault_word8': 0,
                                             'temp1': 6523.60009765625,
                                             'temp2': 6523.60009765625,
                                             'temp3': 6523.60009765625,
                                             'temp4': 6523.60009765625,
                                             'temp5': 0.0,
                                             'temp6': 160.0,
                                             'time': datetime.datetime(2020, 7, 28, 13, 32, 43),
                                             'to_grid_time_today': 0.0,
                                             'to_grid_time_total': 0.0,
                                             'to_grid_today': 0.0,
                                             'to_grid_total': 0.0,
                                             'to_power_grid': 0.0,
                                             'type_flag': 0,
                                             'vac_frequency': 41.27000045776367,
                                             'vacu': 2.299999952316284,
                                             'vacuv': 2.299999952316284,
                                             'vacv': 1.100000023841858,
                                             'vacvw': 0.4000000059604645,
                                             'vacw': 2.0999999046325684,
                                             'vacwu': 2.5999999046325684,
                                             'vpvuv': 1.7000000476837158,
                                             'vpvvw': 0.8999999761581421,
                                             'vpvwu': 0.800000011920929,
                                             'with_time': False}],
                            'device_sn': 'PCS1234567',
                            'next_page_start_id': 21},
                'error_code': 0,
                'error_msg': None}
        """

        if start_date is None and end_date is None:
            start_date = date.today()
            end_date = date.today()
        elif start_date is None:
            start_date = end_date
        elif end_date is None:
            end_date = start_date

        # check interval validity
        if end_date - start_date >= timedelta(days=7):
            raise ValueError("date interval must not exceed 7 days")

        response = self.session.post(
            endpoint="device/pcs/pcs_data",
            data={
                "pcs_sn": self._device_sn(device_sn),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return PcsEnergyHistory.model_validate(response)

    def alarms(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PcsAlarms:
        """
        Get the alarm data of a certain Pcs
        Interface to get the alarm data of a pcs
        https://www.showdoc.com.cn/262556420217021/6131258854397548

        Note:
            Only applicable to devices with device type 8 (pcs) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10005: pcs does not exist

        Args:
            device_sn (str): PCS device serial number
            date_ (Optional[date]): Date - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            SpaAlarms
            e.g.
            {
                'data': {
                    'alarms': [
                        {
                            'alarm_code': 2,
                            'alarm_message': '',
                            'end_time': datetime.datetime(2018, 12, 17, 14, 5, 54),
                            'start_time': datetime.datetime(2018, 12, 17, 14, 5, 54),
                            'status': 1
                        }
                    ],
                    'count': 1,
                    'device_sn': 'TLMAX00B01'
                },
                'error_code': 0,
                'error_msg': None
            }
        """

        if date_ is None:
            date_ = date.today()

        response = self.session.post(
            endpoint="device/pcs/alarm_data",
            data={
                "pcs_sn": self._device_sn(device_sn),
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return PcsAlarms.model_validate(response)
