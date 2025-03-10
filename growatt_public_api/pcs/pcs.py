from datetime import date, timedelta
from typing import Optional, Union, List

import truststore

from growatt_public_api.pydantic_models.pcs import (
    PcsDetails,
    PcsEnergyOverview,
    PcsEnergyHistory,
    PcsAlarms,
    PcsEnergyOverviewMultiple,
    PcsEnergyOverviewMultipleItem,
)

truststore.inject_into_ssl()
from growatt_public_api.session import GrowattApiSession  # noqa: E402


class Pcs:
    """
    endpoints for PCS inverters
    https://www.showdoc.com.cn/262556420217021/6129831722860832

    Note:
        Only applicable to devices with device type 8 (pcs) returned by device.list()
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def details(
        self,
        device_sn: str,
    ) -> PcsDetails:
        """
        Get Pcs basic information
        Interface to get basic information of pcs
        https://www.showdoc.com.cn/262556420217021/6129831722860832

        Note:
            Only applicable to devices with device type 8 (pcs) returned by device.list()

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
                "device_sn": device_sn,
            },
        )

        return PcsDetails.model_validate(response)

    def energy(
        self,
        device_sn: str,
    ) -> PcsEnergyOverview:
        """
        Get the latest real-time data of Pcs
        Interface to get the latest real-time data of pcs
        https://www.showdoc.com.cn/262556420217021/6131235037123575

        Note:
            Only applicable to devices with device type 8 (pcs) returned by device.list()

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
                "pcs_sn": device_sn,
            },
        )

        return PcsEnergyOverview.model_validate(response)

    # TODO
    def energy_multiple(
        self,
        device_sn: Union[str, List[str]],
        page: Optional[int] = None,
    ) -> PcsEnergyOverviewMultiple:
        """
        Get the latest real-time data of Spa in batches
        Interface to obtain the latest real-time data of inverters in batches
        https://www.showdoc.com.cn/262556420217021/6138369063488649

        Note:
            Only applicable to devices with device type 8 (pcs) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: System error
        * 10002: Device serial number error
        * 10003: Date format error
        * 10004: Date interval exceeds seven days
        * 10005: Spa does not exist

        Args:
            device_sn (Union[str, List[str]]): PCS serial number or list of (multiple) PCS serial numbers (max 100)
            page (Optional[int]): page number, default 1, max 2

        Returns:
            SpaEnergyOverviewMultiple
            {   'data': [   {   'data': {   'ac_charge_energy_today': 3.5999999046325684,
                                            'ac_charge_energy_total': 1305.5,
                                            'ac_charge_power': 0.0,
                                            'address': 0,
                                            'again': False,
                                            'alias': None,
                                            'battery_temperature': 36.900001525878906,
                                            'battery_type': 1,
                                            'bms_battery_curr': -9.390000343322754,
                                            'bms_battery_temp': 36.0,
                                            'bms_battery_volt': 53.099998474121094,
                                            'bms_cell10_volt': 3.316999912261963,
                                            'bms_cell11_volt': 3.315999984741211,
                                            'bms_cell12_volt': 3.315000057220459,
                                            'bms_cell13_volt': 3.316999912261963,
                                            'bms_cell14_volt': 3.316999912261963,
                                            'bms_cell15_volt': 3.315999984741211,
                                            'bms_cell16_volt': 3.318000078201294,
                                            'bms_cell1_volt': 3.318000078201294,
                                            'bms_cell2_volt': 0.0020000000949949026,
                                            'bms_cell3_volt': 3.315999984741211,
                                            'bms_cell4_volt': 3.316999912261963,
                                            'bms_cell5_volt': 3.316999912261963,
                                            'bms_cell6_volt': 3.316999912261963,
                                            'bms_cell7_volt': 3.318000078201294,
                                            'bms_cell8_volt': 3.315999984741211,
                                            'bms_cell9_volt': 3.316999912261963,
                                            'bms_constant_volt': 56.79999923706055,
                                            'bms_cycle_cnt': 100,
                                            'bms_delta_volt': 3.0,
                                            'bms_error': 0,
                                            'bms_error_old': 0,
                                            'bms_fw': 70,
                                            'bms_gauge_fcc': 232.0,
                                            'bms_gauge_rm': 243.27999877929688,
                                            'bms_info': 0,
                                            'bms_max_curr': 0.0,
                                            'bms_max_dischg_curr': 170.0,
                                            'bms_mcu_version': 70,
                                            'bms_pack_info': 0,
                                            'bms_soc': 98,
                                            'bms_soh': 100,
                                            'bms_status': 291,
                                            'bms_status_old': 0,
                                            'bms_using_cap': 0,
                                            'bms_warn_info': 0,
                                            'bms_warn_info_old': 0,
                                            'calendar': {   'first_day_of_week': 1,
                                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                            'lenient': True,
                                                            'minimal_days_in_first_week': 1,
                                                            'time': {'date': 11, 'day': 1, 'hours': 15, 'minutes': 43, 'month': 0, 'seconds': 42, 'time': 1610351022000, 'timezone_offset': -480, 'year': 121},
                                                            'time_in_millis': 1610351022000,
                                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                            'week_date_supported': True,
                                                            'week_year': 2021,
                                                            'weeks_in_week_year': 52},
                                            'datalogger_sn': None,
                                            'day': None,
                                            'day_map': None,
                                            'e_to_grid_today': 7.1,
                                            'e_to_grid_total': 1493.6,
                                            'e_to_user_today': 0.0,
                                            'e_to_user_total': 198.5,
                                            'eac_today': 1.5,
                                            'eac_total': 989.1,
                                            'echarge1_today': 3.3,
                                            'echarge1_total': 1195.9,
                                            'edischarge1_today': 1.8,
                                            'edischarge1_total': 1103.4,
                                            'elocal_load_today': 4.1,
                                            'elocal_load_total': 1972.2,
                                            'epv_inverter_today': 13.2,
                                            'epv_inverter_total': 3390.3,
                                            'error_code': -1,
                                            'error_text': 'Unknown',
                                            'fac': 50.029998779296875,
                                            'fault_bit_code': -1,
                                            'fault_code': -1,
                                            'lost': True,
                                            'pac': 430.4,
                                            'pac1': 418.3,
                                            'pac_to_grid_r': 21.5,
                                            'pac_to_grid_total': 21.5,
                                            'pac_to_user_r': 0.0,
                                            'pac_to_user_total': 0.0,
                                            'pcharge1': 0.0,
                                            'pdischarge1': 521.2,
                                            'plocal_load_r': 913.1,
                                            'plocal_load_total': 0.0,
                                            'ppv_inverter': 478.4,
                                            'priority_choose': 0.0,
                                            'serial_num': 'BKE4A02004',
                                            'soc': 98.0,
                                            'soc_text': '98%',
                                            'spa_bean': None,
                                            'status': 6,
                                            'status_text': 'Bat Online',
                                            'sys_en': -1,
                                            'sys_fault_word': 0,
                                            'sys_fault_word1': 0,
                                            'sys_fault_word2': 0,
                                            'sys_fault_word3': 0,
                                            'sys_fault_word4': 0,
                                            'sys_fault_word5': 0,
                                            'sys_fault_word6': 0,
                                            'sys_fault_word7': 256,
                                            'temp1': 37.0,
                                            'temp2': 35.0,
                                            'time': datetime.datetime(2021, 1, 11, 15, 43, 42),
                                            'time_total': -0.5,
                                            'ups_fac': 0.0,
                                            'ups_load_percent': 0.0,
                                            'ups_pac1': 0.0,
                                            'ups_pf': 1000.0,
                                            'ups_vac1': 0.0,
                                            'uw_sys_work_mode': 6,
                                            'v_bat_dsp': 53.20000076293945,
                                            'v_bus1': 393.0,
                                            'v_bus2': 300.0,
                                            'vac1': 243.0,
                                            'vbat': 52.79999923706055,
                                            'warn_code': -1,
                                            'warn_text': 'Unknown',
                                            'with_time': False},
                                'datalogger_sn': 'NAC591706C',
                                'device_sn': 'BKE4A02004'},
                            {   'data': {   'ac_charge_energy_today': 9.899999618530273,
                                            #...
                                            'with_time': False},
                                'datalogger_sn': 'NAC59170BA',
                                'device_sn': 'BKE192500D'}],
                'error_code': 0,
                'error_msg': None,
                'page_num': 1}
        """

        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/spa/spas_data",
            data={
                "spas": device_sn,
                "pageNum": page or 1,
            },
        )

        # Unfortunately, the original response cannot be parsed by pydantic as the inverter_sn is used as key
        # To fix this, resulting data is restructured
        devices = [
            PcsEnergyOverviewMultipleItem(
                device_sn=inverter_sn,
                datalogger_sn=response.get("data", {})
                .get(inverter_sn, {})
                .get("dataloggerSn", None),
                data=response.get("data", {})
                .get(inverter_sn, {})
                .get(inverter_sn, None),
            )
            for inverter_sn in response.get("spas", [])
        ]
        response.pop("spas", None)
        response["data"] = devices

        return PcsEnergyOverviewMultiple.model_validate(response)

    # TODO
    def energy_history(
        self,
        device_sn: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PcsEnergyHistory:
        """
        Get historical data of a SPH
        Interface to get historical data of a certain Mix
        https://www.showdoc.com.cn/262556420217021/6129765461123058

        Note:
            Only applicable to devices with device type 8 (pcs) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Device serial number error
        * 10003: Date format error
        * 10004: Date interval exceeds seven days
        * 10005: Mix does not exist

        Args:
            device_sn (str): PCS serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            SphEnergyHistory
            {   'data': {   'count': 9225,
                            'datalogger_sn': 'BQC0733010',
                            'datas': [   {   'ac_charge_energy_today': 0.0,
                                             'ac_charge_energy_total': 124.30000305175781,
                                             'ac_charge_power': 0.0,
                                             'address': 0,
                                             'again': False,
                                             'alias': None,
                                             'battery_temperature': 0.0,
                                             'battery_type': 1,
                                             'bms_battery_curr': 0.0,
                                             'bms_battery_temp': 28.0,
                                             'bms_battery_volt': 56.7400016784668,
                                             'bms_cell10_volt': 3.549999952316284,
                                             'bms_cell11_volt': 3.549999952316284,
                                             'bms_cell12_volt': 3.5510001182556152,
                                             'bms_cell13_volt': 3.5490000247955322,
                                             'bms_cell14_volt': 3.5490000247955322,
                                             'bms_cell15_volt': 3.5490000247955322,
                                             'bms_cell16_volt': 3.5480000972747803,
                                             'bms_cell1_volt': 3.5480000972747803,
                                             'bms_cell2_volt': 3.5480000972747803,
                                             'bms_cell3_volt': 3.549999952316284,
                                             'bms_cell4_volt': 3.549999952316284,
                                             'bms_cell5_volt': 3.549999952316284,
                                             'bms_cell6_volt': 3.5510001182556152,
                                             'bms_cell7_volt': 3.549999952316284,
                                             'bms_cell8_volt': 3.549999952316284,
                                             'bms_cell9_volt': 3.510999917984009,
                                             'bms_constant_volt': 56.79999923706055,
                                             'bms_cycle_cnt': 1331,
                                             'bms_delta_volt': 40.0,
                                             'bms_error': 0,
                                             'bms_error_old': 0,
                                             'bms_fw': 257,
                                             'bms_gauge_fcc': 100.0,
                                             'bms_gauge_rm': 49.97999954223633,
                                             'bms_info': 257,
                                             'bms_max_curr': 100.0,
                                             'bms_max_dischg_curr': 0.0,
                                             'bms_mcu_version': 512,
                                             'bms_pack_info': 257,
                                             'bms_soc': 100,
                                             'bms_soh': 47,
                                             'bms_status': 361,
                                             'bms_status_old': 361,
                                             'bms_using_cap': 5000,
                                             'bms_warn_info': 0,
                                             'bms_warn_info_old': 0,
                                             'calendar': {   'first_day_of_week': 1,
                                                             'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                             'lenient': True,
                                                             'minimal_days_in_first_week': 1,
                                                             'time': {'date': 5, 'day': 2, 'hours': 15, 'minutes': 51, 'month': 2, 'seconds': 22, 'time': 1551772282000, 'timezone_offset': -480, 'year': 119},
                                                             'time_in_millis': 1551772282000,
                                                             'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                             'week_date_supported': True,
                                                             'week_year': 2019,
                                                             'weeks_in_week_year': 52},
                                             'datalogger_sn': None,
                                             'day': None,
                                             'day_map': None,
                                             'e_to_grid_today': 0.3,
                                             'e_to_grid_total': 2293.4,
                                             'e_to_user_today': 0.0,
                                             'e_to_user_total': 11991.1,
                                             'eac_today': 0.0,
                                             'eac_total': 2015.9,
                                             'echarge1_today': 0.2,
                                             'echarge1_total': 6113.2,
                                             'edischarge1_today': 0.4,
                                             'edischarge1_total': 5540.6,
                                             'elocal_load_today': 0.4,
                                             'elocal_load_total': 26980.8,
                                             'eps_vac2': 0.0,
                                             'eps_vac3': 0.0,
                                             'epv1_today': 0.5,
                                             'epv1_total': 2352.3,
                                             'epv2_today': 0.0,
                                             'epv2_total': 0.0,
                                             'epv_total': 2352.3,
                                             'error_code': 0,
                                             'error_text': 'Unknown',
                                             'fac': 49.97999954223633,
                                             'fault_bit_code': 0,
                                             'fault_code': 0,
                                             'lost': True,
                                             'mix_bean': None,
                                             'pac': 0.0,
                                             'pac1': 0.0,
                                             'pac2': 0.0,
                                             'pac3': 0.0,
                                             'pac_to_grid_r': 37.7,
                                             'pac_to_grid_total': 37.7,
                                             'pac_to_user_r': 0.0,
                                             'pac_to_user_total': 0.0,
                                             'pcharge1': 0.0,
                                             'pdischarge1': 24.1,
                                             'plocal_load_r': 0.0,
                                             'plocal_load_total': 0.0,
                                             'ppv': 93.5,
                                             'ppv1': 93.5,
                                             'ppv2': 0.0,
                                             'ppv_text': '93.5 W',
                                             'priority_choose': 0.0,
                                             'serial_num': 'SARN744005',
                                             'soc': 100.0,
                                             'soc_text': '100%',
                                             'status': 5,
                                             'status_text': 'PV Bat Online',
                                             'sys_en': 8864,
                                             'sys_fault_word': 0,
                                             'sys_fault_word1': 0,
                                             'sys_fault_word2': 0,
                                             'sys_fault_word3': 0,
                                             'sys_fault_word4': 0,
                                             'sys_fault_word5': 0,
                                             'sys_fault_word6': 0,
                                             'sys_fault_word7': 256,
                                             'temp1': 34.0,
                                             'temp2': 33.0,
                                             'temp3': 33.0,
                                             'time': datetime.datetime(2019, 3, 5, 15, 51, 22),
                                             'time_total': 8513914.5,
                                             'ups_fac': 0.0,
                                             'ups_load_percent': 0.0,
                                             'ups_pac1': 0.0,
                                             'ups_pac2': 0.0,
                                             'ups_pac3': 0.0,
                                             'ups_pf': 1000.0,
                                             'ups_vac1': 0.0,
                                             'uw_sys_work_mode': 5,
                                             'v_bat_dsp': 56.70000076293945,
                                             'v_bus1': 391.0,
                                             'v_bus2': 322.0,
                                             'vac1': 219.10000610351562,
                                             'vac2': 0.0,
                                             'vac3': 0.0,
                                             'vbat': 56.70000076293945,
                                             'vpv1': 264.20001220703125,
                                             'vpv2': 0.0,
                                             'warn_code': 0,
                                             'warn_text': 'Unknown',
                                             'with_time': False}],
                            'device_sn': 'SARN744005',
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
        if end_date - start_date > timedelta(days=7):
            raise ValueError("date interval must not exceed 7 days")

        response = self.session.post(
            endpoint="device/mix/mix_data",
            data={
                "mix_sn": device_sn,
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
        device_sn: str,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PcsAlarms:
        """
        Get the alarm data of a certain Pcs
        Interface to get the alarm data of a pcs
        https://www.showdoc.com.cn/262556420217021/6131258854397548

        Note:
            Only applicable to devices with device type 8 (pcs) returned by device.list()

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
                "pcs_sn": device_sn,
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return PcsAlarms.model_validate(response)
