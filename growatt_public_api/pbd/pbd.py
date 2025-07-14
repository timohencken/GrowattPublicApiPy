from datetime import date, timedelta
from typing import Optional
from ..pydantic_models.pbd import (
    PbdDetails,
    PbdEnergyOverview,
    PbdEnergyHistory,
    PbdAlarms,
)
from ..session.growatt_api_session import GrowattApiSession


class Pbd:
    """
    endpoints for PBD inverters
    https://www.showdoc.com.cn/262556420217021/6131307847776153

    Note:
        Only applicable to devices with device type 10 (pbd) returned by plant.list_devices()
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
    ) -> PbdDetails:
        """
        Get Pbd basic information
        Interface to get basic information of pbd
        https://www.showdoc.com.cn/262556420217021/6131307847776153

        Note:
            Only applicable to devices with device type 10 (pbd) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error

        Args:
            device_sn (str): PBD device SN

        Returns:
            PbdDetails
            {   'data': {   'address': 3,
                            'alias': 'PBD250',
                            'biout': 0.0,
                            'bms_enable': True,
                            'bvout': 0.0,
                            'charge_day_map': {},
                            'charge_month': 0,
                            'children': [],
                            'datalogger_sn': 'MONITOR003',
                            'discharge_day_map': {},
                            'discharge_month': 0.0,
                            'discharge_month_2': 0.0,
                            'discharge_month_text': '0',
                            'e_charge_today': 0.0,
                            'e_discharge_today': 0.0,
                            'e_discharge_total': 0.0,
                            'fw_version': 'AB02',
                            'grid_detection_time': 60.0,
                            'group_id': -1,
                            'i_out_max': 0.0,
                            'i_out_min': 500.0,
                            'i_pv_l_max': 500.0,
                            'i_pv_max': 500.0,
                            'icharge': 1.0,
                            'img_path': './css/img/status_gray.gif',
                            'inner_version': '2017',
                            'ipv': 0.0,
                            'ipv1': 0.0,
                            'ipv2': 0.0,
                            'last_update_time': {'date': 29, 'day': 3, 'hours': 18, 'minutes': 49, 'month': 6, 'seconds': 2, 'time': 1596019742000, 'timezone_offset': -480, 'year': 120},
                            'last_update_time_text': datetime.datetime(2020, 7, 29, 18, 49, 2),
                            'level': 6,
                            'location': None,
                            'lost': True,
                            'model': 1,
                            'model_text': 'A0B0D0T0P0U0M0S1',
                            'normalPower': 250000,
                            'on_off': True,
                            'out_power_max': 100.0,
                            'parent_id': 'LIST_MONITOR003_3',
                            'peak_clipping': 0.0,
                            'peak_clipping_total': 0.0,
                            'plant_id': 0,
                            'port_name': 'ShinePano-MONITOR003',
                            'power_start': 1.0,
                            'record': None,
                            'restore': 0.0,
                            'riso_enable': 0.0,
                            'riso_min': 33.0,
                            'rs_addr': 3.0,
                            'safety': 2.0,
                            'serial_num': 'HPS0000001',
                            'soc_max': 0.0,
                            'soc_min': 0.0,
                            'status': -1,
                            'status_lang': 'Lost',
                            'status_text': 'pbd.status.lost',
                            'tcp_server_ip': '47.107.154.111',
                            'timezone': 0,
                            'tree_id': 'HPS0000001',
                            'tree_name': 'PBD250',
                            'type': 1,
                            'updating': False,
                            'v_mppt_max': 844.7999877929688,
                            'v_mppt_min': 14.800000190734863,
                            'v_out_max': 450.0,
                            'v_out_min': 450.0,
                            'v_pv_max': 1000.0,
                            'v_start': 450.0,
                            'vpv': 0.0,
                            'vpv1': 0.0,
                            'vpv2': 545.5},
                'datalogger_sn': 'MONITOR003',
                'device_sn': 'HPS0000001',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/pbd/pbd_data_info",
            params={
                "device_sn": self._device_sn(device_sn),
            },
        )

        return PbdDetails.model_validate(response)

    def energy(
        self,
        device_sn: Optional[str] = None,
    ) -> PbdEnergyOverview:
        """
        Get the latest real-time data of Pbd
        Interface to get the latest real-time data of pbd
        https://www.showdoc.com.cn/262556420217021/6131312777930154

        Note:
            Only applicable to devices with device type 10 (pbd) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: Pbd does not exist
        * 10003: device SN error

        Args:
            device_sn (str): PBD serial number

        Returns:
            PbdEnergyOverview
            {   'data': {   'address': 0,
                            'again': False,
                            'alarm_code1': 0,
                            'alarm_code2': 0,
                            'alias': None,
                            'biout': 191.0,
                            'biout_buck1': 192.0,
                            'biout_buck2': 193.0,
                            'bipv_buck1': 157.0,
                            'bipv_buck2': 158.0,
                            'bipv_buck3': 211.0,
                            'bipv_buck4': 212.0,
                            'bipv_buck5': 213.0,
                            'bms_protection': 0,
                            'bms_status': 10,
                            'bms_volt_status': 2510,
                            'bvbus': 140.0,
                            'bvout': 190.0,
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 29, 'day': 3, 'hours': 18, 'minutes': 49, 'month': 6, 'seconds': 1, 'time': 1596019741000, 'timezone_offset': -480, 'year': 120},
                                            'time_in_millis': 1596019741000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2020,
                                            'weeks_in_week_year': 52},
                            'capacity': 1280.0,
                            'datalogger_sn': None,
                            'day': None,
                            'e_charge_time_today': 108.0,
                            'e_charge_time_total': 156.0,
                            'e_charge_today': 107.0,
                            'e_charge_total': 154.0,
                            'e_discharge_time_today': 106.0,
                            'e_discharge_time_total': 152.0,
                            'e_discharge_today': 105.0,
                            'e_discharge_total': 150.0,
                            'e_out_today': 201.0,
                            'e_out_total': 13238500.0,
                            'electric_state': -1,
                            'epv_time_today': 144.0,
                            'epv_time_total': 148.0,
                            'epv_today': 143.0,
                            'epv_total': 146.0,
                            'id': 0,
                            'ipv': 83.0,
                            'ipv1': 84.0,
                            'ipv2': 187.0,
                            'ipv3': 208.0,
                            'ipv4': 209.0,
                            'ipv5': 210.0,
                            'lost': True,
                            'max_charge_curr': 181.0,
                            'max_discharge_curr': 182.0,
                            'max_min_temp_cell': 9.0,
                            'max_temp': 9.0,
                            'max_temp_num': 9.0,
                            'max_volt': 2.0,
                            'max_volt_cell': 9.0,
                            'max_volt_num': 246.0,
                            'maxmin_volt_cell': 9.0,
                            'min_temp': 226.0,
                            'min_temp_group': 186.0,
                            'min_temp_num': 216.0,
                            'min_volt': 2.0,
                            'min_volt_cell': 9.0,
                            'min_volt_group': 196.0,
                            'min_volt_num': 236.0,
                            'mvpv': 12.699999809265137,
                            'pbd_bat_power': 98.0,
                            'pbd_bean': None,
                            'pbd_out_power': None,
                            'ppv': 189000.0,
                            'ppv1': 132.0,
                            'ppv2': 188.0,
                            'ppv3': 214.0,
                            'ppv4': 215.0,
                            'ppv5': 216.0,
                            'riso_bat_n': 122.0,
                            'riso_bat_p': 121.0,
                            'riso_bus_n': 200.0,
                            'riso_bus_p': 199.0,
                            'riso_pv_n': 120.0,
                            'riso_pv_p': 119.0,
                            'self_time': 1260.0,
                            'serial_num': 'HPS0000001',
                            'status': -1,
                            'status_lang': 'Lost',
                            'status_text': 'Lost',
                            'sys_fault_word1': -1,
                            'sys_fault_word2': -1,
                            'sys_fault_word3': -1,
                            'sys_fault_word4': -1,
                            'sys_fault_word5': -1,
                            'sys_fault_word6': -1,
                            'temp': 117.0,
                            'tempout_buck_l': 198.0,
                            'tempout_buck_module': 196.0,
                            'temppv_buck_l': 197.0,
                            'temppv_buck_module': 195.0,
                            'time': datetime.datetime(2020, 7, 29, 18, 49, 1),
                            'type_flag': 2250,
                            'vbat': None,
                            'vpv': 82.0,
                            'vpv1': 81.0,
                            'vpv2': 186.0,
                            'vpv3': 204.0,
                            'vpv4': 205.0,
                            'vpv5': 207.0,
                            'with_time': False},
                'datalogger_sn': 'MONITOR003',
                'device_sn': 'HPS0000001',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/pbd/pbd_last_data",
            data={
                "pbd_sn": self._device_sn(device_sn),
            },
        )

        return PbdEnergyOverview.model_validate(response)

    def energy_history(
        self,
        device_sn: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PbdEnergyHistory:
        """
        Get historical data of a Pbd
        An interface to obtain historical data of a pbd
        https://www.showdoc.com.cn/262556420217021/6131319527296946

        Note:
            Only applicable to devices with device type 10 (pbd) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: Pbd does not exist
        * 10003: device SN error

        Args:
            device_sn (str): PBD serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            PbdEnergyHistory
            {   'data': {   'count': 78,
                            'datalogger_sn': 'MONITOR003',
                            'datas': [   {   'address': 0,
                                             'again': False,
                                             'alarm_code1': 0,
                                             'alarm_code2': 0,
                                             'alias': None,
                                             'biout': 191.0,
                                             'biout_buck1': 192.0,
                                             'biout_buck2': 193.0,
                                             'bipv_buck1': 157.0,
                                             'bipv_buck2': 158.0,
                                             'bipv_buck3': 211.0,
                                             'bipv_buck4': 212.0,
                                             'bipv_buck5': 213.0,
                                             'bms_protection': 0,
                                             'bms_status': 10,
                                             'bms_volt_status': 2510,
                                             'bvbus': 140.0,
                                             'bvout': 190.0,
                                             'calendar': {   'first_day_of_week': 1,
                                                             'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                             'lenient': True,
                                                             'minimal_days_in_first_week': 1,
                                                             'time': {'date': 29, 'day': 3, 'hours': 18, 'minutes': 49, 'month': 6, 'seconds': 1, 'time': 1596019741000, 'timezone_offset': -480, 'year': 120},
                                                             'time_in_millis': 1596019741000,
                                                             'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                             'week_date_supported': True,
                                                             'week_year': 2020,
                                                             'weeks_in_week_year': 52},
                                             'capacity': 1280.0,
                                             'datalogger_sn': None,
                                             'day': None,
                                             'e_charge_time_today': 108.0,
                                             'e_charge_time_total': 156.0,
                                             'e_charge_today': 107.0,
                                             'e_charge_total': 154.0,
                                             'e_discharge_time_today': 106.0,
                                             'e_discharge_time_total': 152.0,
                                             'e_discharge_today': 105.0,
                                             'e_discharge_total': 150.0,
                                             'e_out_today': 201.0,
                                             'e_out_total': 13238500.0,
                                             'electric_state': -1,
                                             'epv_time_today': 144.0,
                                             'epv_time_total': 148.0,
                                             'epv_today': 143.0,
                                             'epv_total': 146.0,
                                             'id': 0,
                                             'ipv': 83.0,
                                             'ipv1': 84.0,
                                             'ipv2': 187.0,
                                             'ipv3': 208.0,
                                             'ipv4': 209.0,
                                             'ipv5': 210.0,
                                             'lost': True,
                                             'max_charge_curr': 181.0,
                                             'max_discharge_curr': 182.0,
                                             'max_min_temp_cell': 9.0,
                                             'max_temp': 9.0,
                                             'max_temp_num': 9.0,
                                             'max_volt': 2.0,
                                             'max_volt_cell': 9.0,
                                             'max_volt_num': 246.0,
                                             'maxmin_volt_cell': 9.0,
                                             'min_temp': 226.0,
                                             'min_temp_group': 186.0,
                                             'min_temp_num': 216.0,
                                             'min_volt': 2.0,
                                             'min_volt_cell': 9.0,
                                             'min_volt_group': 196.0,
                                             'min_volt_num': 236.0,
                                             'mvpv': 12.699999809265137,
                                             'pbd_bat_power': 98.0,
                                             'pbd_bean': None,
                                             'pbd_out_power': None,
                                             'ppv': 189000.0,
                                             'ppv1': 132.0,
                                             'ppv2': 188.0,
                                             'ppv3': 214.0,
                                             'ppv4': 215.0,
                                             'ppv5': 216.0,
                                             'riso_bat_n': 122.0,
                                             'riso_bat_p': 121.0,
                                             'riso_bus_n': 200.0,
                                             'riso_bus_p': 199.0,
                                             'riso_pv_n': 120.0,
                                             'riso_pv_p': 119.0,
                                             'self_time': 1260.0,
                                             'serial_num': 'HPS0000001',
                                             'status': -1,
                                             'status_lang': 'Lost',
                                             'status_text': 'Lost',
                                             'sys_fault_word1': -1,
                                             'sys_fault_word2': -1,
                                             'sys_fault_word3': -1,
                                             'sys_fault_word4': -1,
                                             'sys_fault_word5': -1,
                                             'sys_fault_word6': -1,
                                             'temp': 117.0,
                                             'tempout_buck_l': 198.0,
                                             'tempout_buck_module': 196.0,
                                             'temppv_buck_l': 197.0,
                                             'temppv_buck_module': 195.0,
                                             'time': datetime.datetime(2020, 7, 29, 18, 49, 1),
                                             'type_flag': 2250,
                                             'vbat': None,
                                             'vpv': 82.0,
                                             'vpv1': 81.0,
                                             'vpv2': 186.0,
                                             'vpv3': 204.0,
                                             'vpv4': 205.0,
                                             'vpv5': 207.0,
                                             'with_time': False}],
                            'device_sn': 'HPS0000001',
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
            endpoint="device/pbd/pbd_data",
            data={
                "pbd_sn": self._device_sn(device_sn),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return PbdEnergyHistory.model_validate(response)

    def alarms(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PbdAlarms:
        """
        Get the alarm data of a certain Pbd
        Interface to get the alarm data of a pbd
        https://www.showdoc.com.cn/262556420217021/6131327683011501

        Note:
            Only applicable to devices with device type 10 (pbd) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10005: Pbd does not exist

        Args:
            device_sn (str): PBD device serial number
            date_ (Optional[date]): Date - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            PbdAlarms
            {   'data': {   'alarms': [   {'alarm_code': '3-107-5', 'alarm_message': 'BYTE107_5', 'end_time': datetime.datetime(2019, 10, 16, 13, 51, 1), 'start_time': datetime.datetime(2019, 10, 16, 13, 51, 1), 'status': 1},
                                          {'alarm_code': '3-107-4', 'alarm_message': 'BYTE107_4', 'end_time': datetime.datetime(2019, 10, 16, 13, 51, 1), 'start_time': datetime.datetime(2019, 10, 16, 13, 51, 1), 'status': 1},
                                          {'alarm_code': '6-113-2', 'alarm_message': 'BYTE113_2', 'end_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'start_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'status': 1},
                                          {'alarm_code': '6-113-1', 'alarm_message': 'BYTE113_1', 'end_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'start_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'status': 1},
                                          {'alarm_code': '6-113-0', 'alarm_message': 'BYTE113_0', 'end_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'start_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'status': 1},
                                          {'alarm_code': '6-112-7', 'alarm_message': 'BYTE112_7', 'end_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'start_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'status': 1},
                                          {'alarm_code': '5-110-6', 'alarm_message': 'BYTE110_6', 'end_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'start_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'status': 1},
                                          {'alarm_code': '5-110-5', 'alarm_message': 'BYTE110_5', 'end_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'start_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'status': 1},
                                          {'alarm_code': '3-107-5', 'alarm_message': 'BYTE107_5', 'end_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'start_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'status': 1},
                                          {'alarm_code': '3-107-4', 'alarm_message': 'BYTE107_4', 'end_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'start_time': datetime.datetime(2019, 10, 15, 15, 20, 16), 'status': 1}],
                            'count': 10,
                            'device_sn': 'HPS0000001'},
                'error_code': 0,
                'error_msg': None}
        """

        if date_ is None:
            date_ = date.today()

        response = self.session.post(
            endpoint="device/pbd/alarm_data",
            data={
                "pbd_sn": self._device_sn(device_sn),
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return PbdAlarms.model_validate(response)
