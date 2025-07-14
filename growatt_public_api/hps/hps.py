from datetime import date, timedelta
from typing import Optional
from ..pydantic_models.hps import (
    HpsDetails,
    HpsEnergyOverview,
    HpsEnergyHistory,
    HpsAlarms,
)
from ..session.growatt_api_session import GrowattApiSession


class Hps:
    """
    endpoints for HPS inverters
    https://www.showdoc.com.cn/262556420217021/6131272209142535

    Note:
        Only applicable to devices with device type 9 (hps) returned by plant.list_devices()
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
    ) -> HpsDetails:
        """
        Obtain basic Hps information
        Interface to get basic information of hps
        https://www.showdoc.com.cn/262556420217021/6131272209142535

        Note:
            Only applicable to devices with device type 9 (hps) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error

        Args:
            device_sn (str): HPS device SN

        Returns:
            HpsDetails
            {   'data': {   'address': 1,
                            'alias': 'UHD0918003',
                            'charge_day_map': {},
                            'charge_month': 0,
                            'children': [],
                            'datalogger_sn': 'WFD091500E',
                            'device_type': 0,
                            'discharge_day_map': {},
                            'discharge_month': 0.0,
                            'e_charge_today': 0.0,
                            'e_discharge_today': 0.0,
                            'e_discharge_total': 0.0,
                            'energy_day_map': {},
                            'energy_month': 0.0,
                            'energy_month_text': '0',
                            'fw_version': '1324',
                            'group_id': -1,
                            'hps_set_bean': None,
                            'id': 26,
                            'img_path': './css/img/status_gray.gif',
                            'inner_version': 'null',
                            'last_update_time': {   'first_day_of_week': 1,
                                                    'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                    'lenient': True,
                                                    'minimal_days_in_first_week': 1,
                                                    'time': {'date': 27, 'day': 1, 'hours': 13, 'minutes': 40, 'month': 6, 'seconds': 4, 'time': 1595828404000, 'timezone_offset': -480, 'year': 120},
                                                    'time_in_millis': 1595828404000,
                                                    'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                    'week_date_supported': True,
                                                    'week_year': 2020,
                                                    'weeks_in_week_year': 52},
                            'last_update_time_text': datetime.datetime(2020, 7, 27, 13, 40, 4),
                            'level': 4,
                            'location': None,
                            'lost': True,
                            'model': 0,
                            'model_text': 'A0B0D0T0P0U0M0S0',
                            'normalPower': 10000,
                            'parent_id': 'LIST_WFD091500E_82',
                            'plant_id': 0,
                            'plant_name': None,
                            'port_name': 'ShinePano-WFD091500E',
                            'power_max': None,
                            'power_max_text': None,
                            'power_max_time': None,
                            'pv_today': 0.0,
                            'record': None,
                            'serial_num': 'UHD0918003',
                            'status': -1,
                            'status_text': 'hps.status.lost',
                            'tcp_server_ip': '47.107.154.111',
                            'timezone': 8,
                            'tree_id': 'HPS_UHD0918003',
                            'tree_name': 'UHD0918003',
                            'updating': False,
                            'user_name': None},
                'datalogger_sn': 'WFD091500E',
                'device_sn': 'UHD0918003',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/hps/hps_data_info",
            params={
                "device_sn": self._device_sn(device_sn),
            },
        )

        return HpsDetails.model_validate(response)

    def energy(
        self,
        device_sn: Optional[str] = None,
    ) -> HpsEnergyOverview:
        """
        Get the latest real-time data of Hps
        Interface to get the latest real-time data of hps
        https://www.showdoc.com.cn/262556420217021/6131278907853302

        Note:
            Only applicable to devices with device type 9 (hps) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: Mix does not exist
        * 10003: device SN error

        Args:
            device_sn (str): HPS serial number

        Returns:
            HpsEnergyOverview
            {   'data': {   'address': 0,
                            'again': False,
                            'alarm_code1': 0,
                            'alarm_code2': 0,
                            'alias': None,
                            'ats_bypass': 0,
                            'b_active_power': 0.0,
                            'batcdct': 0.0,
                            'batldt': 0.0,
                            'batnir': 0.0,
                            'batpir': 0.0,
                            'bms_protection': 0,
                            'bms_show_status': 0,
                            'bms_status': 0,
                            'bms_volt_status': 0,
                            'bmstc': 0.0,
                            'bmstv': 0.0,
                            'bvbus': 0.0,
                            'bvbus_nega': 0.0,
                            'bvbus_posi': 0.0,
                            'bypass_freq': 0.0,
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 27, 'day': 1, 'hours': 13, 'minutes': 40, 'month': 6, 'seconds': 4, 'time': 1595828404000, 'timezone_offset': -480, 'year': 120},
                                            'time_in_millis': 1595828404000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2020,
                                            'weeks_in_week_year': 52},
                            'capacity': 0.0,
                            'cfdllc1': 0.0,
                            'cfdllc2': 0.0,
                            'datalogger_sn': None,
                            'day': None,
                            'dg_grid_power': 0.0,
                            'dg_grid_select': 0,
                            'e_bat_charge_time_total': 4.8,
                            'e_bat_charge_total': 12.0,
                            'e_bat_discharge_time_total': 0.6,
                            'e_bat_discharge_total': 0.3,
                            'e_charge_time_today': 318.1,
                            'e_charge_today': 12.0,
                            'e_discharge_time_today': 44.2,
                            'e_discharge_today': 2.0,
                            'e_grid_time_today': 573.5,
                            'e_grid_time_total': 8.90000057220459,
                            'e_grid_today': 1.899999976158142,
                            'e_grid_total': 1.899999976158142,
                            'e_load_time_today': 92.80000305175781,
                            'e_load_time_total': 1.2000000476837158,
                            'e_load_today': 4.800000190734863,
                            'e_load_total': 4.800000190734863,
                            'e_to_grid_time_today': 296.29998779296875,
                            'e_to_grid_time_total': 4.400000095367432,
                            'e_to_grid_today': 5.0,
                            'e_to_grid_total': 5.0,
                            'effectiveness': 99.0,
                            'epv_time_today': 358.1,
                            'epv_time_total': 5.5,
                            'epv_today': 0.0,
                            'epv_total': 21.8,
                            'fac': 0.0,
                            'grid_freq': 49.97999954223633,
                            'gvpvuv': 230.5,
                            'gvpvvw': 0.0,
                            'gvpvwu': 0.0,
                            'hps_bean': None,
                            'i_buck1': 0.10000000149011612,
                            'i_buck2': 0.10000000149011612,
                            'i_buck3': 0.0,
                            'i_buck4': 0.0,
                            'i_buck5': 0.0,
                            'ibat': -0.10000000149011612,
                            'iboard': -0.10000000149011612,
                            'id': 4,
                            'inductor_curr': 0.0,
                            'insul_detec_nega': 1000.0,
                            'insul_detec_posi': 1000.0,
                            'invuv': 0.0,
                            'invvw': 0.0,
                            'invwu': 0.0,
                            'ipv': 0.8999999761581421,
                            'ipv2': 0.800000011920929,
                            'ipva': 0.4000000059604645,
                            'ipvb': 0.0,
                            'ipvc': 0.0,
                            'ipvu': 0.10000000149011612,
                            'ipvv': 0.0,
                            'ipvw': 0.0,
                            'load_active_power': 0.0,
                            'load_ia': 0.30000001192092896,
                            'load_ib': 0.0,
                            'load_ic': 0.0,
                            'load_pf': 100.0,
                            'load_reactive_power': 0.0,
                            'lost': True,
                            'max_charge_curr': 0.0,
                            'max_discharge_curr': 0.0,
                            'max_min_temp_cell': 0.0,
                            'max_temp': 0.0,
                            'max_temp_num': 0.0,
                            'max_volt': 0.0,
                            'max_volt_cell': 0.0,
                            'max_volt_num': 0.0,
                            'maxmin_volt_cell': 0.0,
                            'min_temp': 0.0,
                            'min_temp_group': 0.0,
                            'min_temp_num': 0.0,
                            'min_volt': 0.0,
                            'min_volt_cell': 0.0,
                            'min_volt_group': 0.0,
                            'min_volt_num': 0.0,
                            'mvpv': 65.5260009765625,
                            'pac': 0.0,
                            'pac1': 0.0,
                            'pac2': 0.0,
                            'pf': 0.0010000000474974513,
                            'pf_symbol': 1,
                            'ppv': 0.0,
                            'ppv1': 0.0,
                            'ppv2': 0.0,
                            'pvnir1': 1000.0,
                            'pvpir1': 1000.0,
                            'rac': 0.0,
                            'run_model': 5,
                            'run_status': 0,
                            'scrtemp': 0.0,
                            'self_time': 10.0,
                            'serial_num': 'UHD0918003',
                            'status': 0,
                            'status_lang': 'common_wait',
                            'status_text': 'WaitState',
                            'sys_fault_word1': 0,
                            'sys_fault_word2': 0,
                            'sys_fault_word3': 0,
                            'sys_fault_word4': 0,
                            'sys_fault_word5': 1024,
                            'sys_fault_word6': 0,
                            'sys_fault_word7': 0,
                            'sys_fault_word8': 0,
                            'sys_fault_word9': 0,
                            'temp1': 35.0,
                            'temp2': 36.0,
                            'temp3': 0.0,
                            'temp4': 0.0,
                            'temp5': 0.0,
                            'temp6': 0.0,
                            'time': datetime.datetime(2020, 7, 27, 13, 40, 4),
                            'type_flag': 0,
                            'vbat': -1.5,
                            'vpv': 1.7000000476837158,
                            'vpv2': -0.5,
                            'vpvun': 1.0,
                            'vpvuv': 0.0,
                            'vpvvn': 0.0,
                            'vpvvw': 0.0,
                            'vpvwn': 0.0,
                            'vpvwu': 0.0,
                            'with_time': False},
                'datalogger_sn': 'WFD091500E',
                'device_sn': 'UHD0918003',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/hps/hps_last_data",
            data={
                "hps_sn": self._device_sn(device_sn),
            },
        )

        return HpsEnergyOverview.model_validate(response)

    def energy_history(
        self,
        device_sn: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> HpsEnergyHistory:
        """
        Get historical data of a certain Hps
        Interface to get historical data of a certain hps
        https://www.showdoc.com.cn/262556420217021/6131286861044579

        Note:
            Only applicable to devices with device type 9 (hps) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: Hps does not exist
        * 10003: device SN error

        Args:
            device_sn (str): HPS serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            HpsEnergyHistory
            {   'data': {   'count': 29,
                            'datalogger_sn': 'WFD091500E',
                            'datas': [   {   'address': 0,
                                             'again': False,
                                             'alarm_code1': 0,
                                             'alarm_code2': 0,
                                             'alias': None,
                                             'ats_bypass': 0,
                                             'b_active_power': 0.0,
                                             'batcdct': 0.0,
                                             'batldt': 0.0,
                                             'batnir': 0.0,
                                             'batpir': 0.0,
                                             'bms_protection': 0,
                                             'bms_show_status': 0,
                                             'bms_status': 0,
                                             'bms_volt_status': 0,
                                             'bmstc': 0.0,
                                             'bmstv': 0.0,
                                             'bvbus': 0.0,
                                             'bvbus_nega': 0.0,
                                             'bvbus_posi': 0.0,
                                             'bypass_freq': 0.0,
                                             'calendar': {   'first_day_of_week': 1,
                                                             'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                             'lenient': True,
                                                             'minimal_days_in_first_week': 1,
                                                             'time': {'date': 27, 'day': 1, 'hours': 13, 'minutes': 40, 'month': 6, 'seconds': 4, 'time': 1595828404000, 'timezone_offset': -480, 'year': 120},
                                                             'time_in_millis': 1595828404000,
                                                             'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                             'week_date_supported': True,
                                                             'week_year': 2020,
                                                             'weeks_in_week_year': 52},
                                             'capacity': 0.0,
                                             'cfdllc1': 0.0,
                                             'cfdllc2': 0.0,
                                             'datalogger_sn': None,
                                             'day': None,
                                             'dg_grid_power': 0.0,
                                             'dg_grid_select': 0,
                                             'e_bat_charge_time_total': 4.8,
                                             'e_bat_charge_total': 12.0,
                                             'e_bat_discharge_time_total': 0.6,
                                             'e_bat_discharge_total': 0.3,
                                             'e_charge_time_today': 318.1,
                                             'e_charge_today': 12.0,
                                             'e_discharge_time_today': 44.2,
                                             'e_discharge_today': 2.0,
                                             'e_grid_time_today': 573.5,
                                             'e_grid_time_total': 8.90000057220459,
                                             'e_grid_today': 1.899999976158142,
                                             'e_grid_total': 1.899999976158142,
                                             'e_load_time_today': 92.80000305175781,
                                             'e_load_time_total': 1.2000000476837158,
                                             'e_load_today': 4.800000190734863,
                                             'e_load_total': 4.800000190734863,
                                             'e_to_grid_time_today': 296.29998779296875,
                                             'e_to_grid_time_total': 4.400000095367432,
                                             'e_to_grid_today': 5.0,
                                             'e_to_grid_total': 5.0,
                                             'effectiveness': 99.0,
                                             'epv_time_today': 358.1,
                                             'epv_time_total': 5.5,
                                             'epv_today': 0.0,
                                             'epv_total': 21.8,
                                             'fac': 0.0,
                                             'grid_freq': 49.97999954223633,
                                             'gvpvuv': 230.5,
                                             'gvpvvw': 0.0,
                                             'gvpvwu': 0.0,
                                             'hps_bean': None,
                                             'i_buck1': 0.10000000149011612,
                                             'i_buck2': 0.10000000149011612,
                                             'i_buck3': 0.0,
                                             'i_buck4': 0.0,
                                             'i_buck5': 0.0,
                                             'ibat': -0.10000000149011612,
                                             'iboard': -0.10000000149011612,
                                             'id': 789,
                                             'inductor_curr': 0.0,
                                             'insul_detec_nega': 1000.0,
                                             'insul_detec_posi': 1000.0,
                                             'invuv': 0.0,
                                             'invvw': 0.0,
                                             'invwu': 0.0,
                                             'ipv': 0.8999999761581421,
                                             'ipv2': 0.800000011920929,
                                             'ipva': 0.4000000059604645,
                                             'ipvb': 0.0,
                                             'ipvc': 0.0,
                                             'ipvu': 0.10000000149011612,
                                             'ipvv': 0.0,
                                             'ipvw': 0.0,
                                             'load_active_power': 0.0,
                                             'load_ia': 0.30000001192092896,
                                             'load_ib': 0.0,
                                             'load_ic': 0.0,
                                             'load_pf': 100.0,
                                             'load_reactive_power': 0.0,
                                             'lost': True,
                                             'max_charge_curr': 0.0,
                                             'max_discharge_curr': 0.0,
                                             'max_min_temp_cell': 0.0,
                                             'max_temp': 0.0,
                                             'max_temp_num': 0.0,
                                             'max_volt': 0.0,
                                             'max_volt_cell': 0.0,
                                             'max_volt_num': 0.0,
                                             'maxmin_volt_cell': 0.0,
                                             'min_temp': 0.0,
                                             'min_temp_group': 0.0,
                                             'min_temp_num': 0.0,
                                             'min_volt': 0.0,
                                             'min_volt_cell': 0.0,
                                             'min_volt_group': 0.0,
                                             'min_volt_num': 0.0,
                                             'mvpv': 65.5260009765625,
                                             'pac': 0.0,
                                             'pac1': 0.0,
                                             'pac2': 0.0,
                                             'pf': 0.0010000000474974513,
                                             'pf_symbol': 1,
                                             'ppv': 0.0,
                                             'ppv1': 0.0,
                                             'ppv2': 0.0,
                                             'pvnir1': 1000.0,
                                             'pvpir1': 1000.0,
                                             'rac': 0.0,
                                             'run_model': 5,
                                             'run_status': 0,
                                             'scrtemp': 0.0,
                                             'self_time': 10.0,
                                             'serial_num': 'UHD0918003',
                                             'status': 0,
                                             'status_lang': 'common_wait',
                                             'status_text': 'WaitState',
                                             'sys_fault_word1': 0,
                                             'sys_fault_word2': 0,
                                             'sys_fault_word3': 0,
                                             'sys_fault_word4': 0,
                                             'sys_fault_word5': 1024,
                                             'sys_fault_word6': 0,
                                             'sys_fault_word7': 0,
                                             'sys_fault_word8': 0,
                                             'sys_fault_word9': 0,
                                             'temp1': 35.0,
                                             'temp2': 36.0,
                                             'temp3': 0.0,
                                             'temp4': 0.0,
                                             'temp5': 0.0,
                                             'temp6': 0.0,
                                             'time': datetime.datetime(2020, 7, 27, 13, 40, 4),
                                             'type_flag': 0,
                                             'vbat': -1.5,
                                             'vpv': 1.7000000476837158,
                                             'vpv2': -0.5,
                                             'vpvun': 1.0,
                                             'vpvuv': 0.0,
                                             'vpvvn': 0.0,
                                             'vpvvw': 0.0,
                                             'vpvwn': 0.0,
                                             'vpvwu': 0.0,
                                             'with_time': False}],
                            'device_sn': 'UHD0918003',
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
            endpoint="device/hps/hps_data",
            data={
                "hps_sn": self._device_sn(device_sn),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return HpsEnergyHistory.model_validate(response)

    def alarms(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> HpsAlarms:
        """
        Get the alarm data of a certain Hps
        Interface to get alarm data of a certain hps
        https://www.showdoc.com.cn/262556420217021/6131425592840458

        Note:
            Only applicable to devices with device type 9 (hps) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10005: Hps does not exist

        Args:
            device_sn (str): HPS device serial number
            date_ (Optional[date]): Date - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            HpsAlarms
            {   'data': {   'alarms': [   {'alarm_code': '7-114-5', 'alarm_message': 'BYTE114_5', 'end_time': datetime.datetime(2020, 7, 27, 11, 26, 10), 'start_time': datetime.datetime(2020, 7, 27, 11, 26, 10), 'status': 1},
                                          {'alarm_code': '6-113-5', 'alarm_message': 'BYTE113_5', 'end_time': datetime.datetime(2020, 7, 27, 11, 26, 10), 'start_time': datetime.datetime(2020, 7, 27, 11, 26, 10), 'status': 1},
                                          {'alarm_code': '2-104-3', 'alarm_message': 'BYTE104_3', 'end_time': datetime.datetime(2020, 7, 27, 11, 26, 10), 'start_time': datetime.datetime(2020, 7, 27, 11, 26, 10), 'status': 1},
                                          {'alarm_code': '5-110-2', 'alarm_message': 'BYTE110_2', 'end_time': datetime.datetime(2020, 7, 27, 11, 21, 10), 'start_time': datetime.datetime(2020, 7, 27, 11, 21, 10), 'status': 1},
                                          {'alarm_code': '5-110-2', 'alarm_message': 'BYTE110_2', 'end_time': datetime.datetime(2020, 7, 24, 18, 34, 21), 'start_time': datetime.datetime(2020, 7, 24, 18, 34, 21), 'status': 1},
                                          {'alarm_code': '6-113-5', 'alarm_message': 'BYTE113_5', 'end_time': datetime.datetime(2020, 7, 24, 18, 9, 26), 'start_time': datetime.datetime(2020, 7, 24, 18, 9, 26), 'status': 1},
                                          {'alarm_code': '2-104-3', 'alarm_message': 'BYTE104_3', 'end_time': datetime.datetime(2020, 7, 24, 18, 9, 26), 'start_time': datetime.datetime(2020, 7, 24, 18, 9, 26), 'status': 1},
                                          {'alarm_code': '5-110-2', 'alarm_message': 'BYTE110_2', 'end_time': datetime.datetime(2020, 7, 24, 16, 12, 39), 'start_time': datetime.datetime(2020, 7, 24, 16, 12, 39), 'status': 1},
                                          {'alarm_code': '5-110-2', 'alarm_message': 'BYTE110_2', 'end_time': datetime.datetime(2020, 7, 24, 15, 49, 20), 'start_time': datetime.datetime(2020, 7, 24, 15, 49, 20), 'status': 1},
                                          {'alarm_code': '7-114-5', 'alarm_message': 'BYTE114_5', 'end_time': datetime.datetime(2020, 7, 24, 15, 34, 22), 'start_time': datetime.datetime(2020, 7, 24, 15, 34, 22), 'status': 1},
                                          {'alarm_code': '6-113-5', 'alarm_message': 'BYTE113_5', 'end_time': datetime.datetime(2020, 7, 24, 15, 34, 22), 'start_time': datetime.datetime(2020, 7, 24, 15, 34, 22), 'status': 1},
                                          {'alarm_code': '5-110-2', 'alarm_message': 'BYTE110_2', 'end_time': datetime.datetime(2020, 7, 24, 15, 34, 22), 'start_time': datetime.datetime(2020, 7, 24, 15, 34, 22), 'status': 1},
                                          {'alarm_code': '5-110-2', 'alarm_message': 'BYTE110_2', 'end_time': datetime.datetime(2020, 7, 24, 15, 6, 42), 'start_time': datetime.datetime(2020, 7, 24, 15, 6, 42), 'status': 1},
                                          {'alarm_code': '7-114-5', 'alarm_message': 'BYTE114_5', 'end_time': datetime.datetime(2020, 7, 24, 11, 25, 14), 'start_time': datetime.datetime(2020, 7, 24, 11, 25, 14), 'status': 1},
                                          {'alarm_code': '6-113-5', 'alarm_message': 'BYTE113_5', 'end_time': datetime.datetime(2020, 7, 24, 11, 25, 14), 'start_time': datetime.datetime(2020, 7, 24, 11, 25, 14), 'status': 1},
                                          {'alarm_code': '7-114-5', 'alarm_message': 'BYTE114_5', 'end_time': datetime.datetime(2020, 7, 24, 10, 52, 59), 'start_time': datetime.datetime(2020, 7, 24, 10, 52, 59), 'status': 1},
                                          {'alarm_code': '6-113-5', 'alarm_message': 'BYTE113_5', 'end_time': datetime.datetime(2020, 7, 24, 10, 52, 59), 'start_time': datetime.datetime(2020, 7, 24, 10, 52, 59), 'status': 1},
                                          {'alarm_code': '5-110-2', 'alarm_message': 'BYTE110_2', 'end_time': datetime.datetime(2020, 7, 24, 10, 48, 1), 'start_time': datetime.datetime(2020, 7, 24, 10, 48, 1), 'status': 1},
                                          {'alarm_code': '5-110-2', 'alarm_message': 'BYTE110_2', 'end_time': datetime.datetime(2020, 7, 23, 17, 56), 'start_time': datetime.datetime(2020, 7, 23, 17, 56), 'status': 1},
                                          {'alarm_code': '5-110-2', 'alarm_message': 'BYTE110_2', 'end_time': datetime.datetime(2020, 7, 23, 16, 9, 41), 'start_time': datetime.datetime(2020, 7, 23, 16, 9, 41), 'status': 1}],
                            'count': 62,
                            'device_sn': 'UHD0918003'},
                'error_code': 0,
                'error_msg': None}
        """

        if date_ is None:
            date_ = date.today()

        response = self.session.post(
            endpoint="device/hps/alarm_data",
            data={
                "hps_sn": self._device_sn(device_sn),
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return HpsAlarms.model_validate(response)
