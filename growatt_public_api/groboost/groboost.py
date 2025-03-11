from datetime import date, timedelta
from typing import Optional, Union, List

import truststore

from growatt_public_api.pydantic_models.groboost import (
    GroboostDetails,
    GroboostMetricsOverview,
    GroboostMetricsHistory,
    GroboostMetricsOverviewMultiple,
    GroboostMetricsOverviewMultipleItem,
)

truststore.inject_into_ssl()
from growatt_public_api.session import GrowattApiSession  # noqa: E402


class Groboost:
    """
    endpoints for GROBOOST Energy management system
    https://www.showdoc.com.cn/262556420217021/7178727239710262

    Note:
        Only applicable to devices with device type 11 (groboost) returned by device.list()
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def details(
        self,
        device_sn: str,
    ) -> GroboostDetails:
        """
        Interface to get basic information of GroBoost
        https://www.showdoc.com.cn/262556420217021/7178727239710262

        Note:
            Only applicable to devices with device type 11 (groboost) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10011: no permission

        Args:
            device_sn (str): GROBOOST device SN

        Returns:
            GroboostDetails
            {   'data': {   'address': 84,
                            'ammeter_data': {   'a_active_power': 0.0,
                                                'a_current': 0.0,
                                                'a_power_factor': 0.0,
                                                'a_reactive_power': 0.0,
                                                'a_voltage': 0.0,
                                                'active_energy': 0.0,
                                                'active_net_total_energy': None,
                                                'active_power': 0.0,
                                                'active_power_l1': 0.0,
                                                'active_power_l2': 0.0,
                                                'active_power_l3': 0.0,
                                                'active_power_max_need': 0.0,
                                                'active_power_max_need_one': 0.0,
                                                'active_power_need': 0.0,
                                                'active_power_need_one': 0.0,
                                                'address': 0,
                                                'again': None,
                                                'alarm_Code': None,
                                                'alias': None,
                                                'apparent_energy': 0.0,
                                                'apparent_energy_max_need': 0.0,
                                                'apparent_energy_need': 0.0,
                                                'apparent_power': 0.0,
                                                'apparent_power_l1': 0.0,
                                                'apparent_power_l2': 0.0,
                                                'apparent_power_l3': 0.0,
                                                'b_active_power': 0.0,
                                                'b_power_factor': 0.0,
                                                'b_reactive_power': 0.0,
                                                'c_active_power': 0.0,
                                                'c_power_factor': 0.0,
                                                'c_reactive_power': 0.0,
                                                'calendar': None,
                                                'com_address': None,
                                                'combined_reactive_power1': None,
                                                'combined_reactive_power2': None,
                                                'comm_status': None,
                                                'current': 0.0,
                                                'current_active_demand': None,
                                                'current_harmonic_avg': 0.0,
                                                'current_ia': 0.0,
                                                'current_ib': 0.0,
                                                'current_ic': 0.0,
                                                'current_l1': 0.0,
                                                'current_l1_max_need': 0.0,
                                                'current_l1_need': 0.0,
                                                'current_l2': 0.0,
                                                'current_l2_max_need': 0.0,
                                                'current_l2_need': 0.0,
                                                'current_l3': 0.0,
                                                'current_l3_max_need': 0.0,
                                                'current_l3_need': 0.0,
                                                'current_max_need': 0.0,
                                                'current_need': 0.0,
                                                'current_reactive_demand': None,
                                                'datalogger_sn': None,
                                                'device_sn': None,
                                                'ex_power_factor': None,
                                                'fei_lv_bo_z_energy': 0.0,
                                                'fei_lv_feng_z_energy': 0.0,
                                                'fei_lv_gu_z_energy': 0.0,
                                                'fei_lv_ping_z_energy': 0.0,
                                                'forward_active_max_need': 0.0,
                                                'forward_active_need': 0.0,
                                                'frequency': 0.0,
                                                'generic_meter': None,
                                                'grid_energy': 0.0,
                                                'grid_frequency': 0.0,
                                                'history_number': None,
                                                'instant_total_active_power': 0.0,
                                                'instant_total_apparent_power': 0.0,
                                                'instant_total_reactive_power': 0.0,
                                                'l1_current_harmonic': 0.0,
                                                'l1_voltage2': 0.0,
                                                'l1_voltage_harmonic': 0.0,
                                                'l1_voltage_harmonic2': 0.0,
                                                'l2_current_harmonic': 0.0,
                                                'l2_voltage3': 0.0,
                                                'l2_voltage_harmonic': 0.0,
                                                'l2_voltage_harmonic3': 0.0,
                                                'l3_current_harmonic': 0.0,
                                                'l3_voltage1': 0.0,
                                                'l3_voltage_harmonic': 0.0,
                                                'l3_voltage_harmonic1': 0.0,
                                                'line_voltage_harmonic_avg': 0.0,
                                                'lost': False,
                                                'meter_dh': None,
                                                'meter_ms': None,
                                                'meter_ym': None,
                                                'mode_status': None,
                                                'month_energy': 0.0,
                                                'net_total_energy': None,
                                                'posi_active_net_total_energy': None,
                                                'posi_active_power': 0.0,
                                                'posi_reactive_net_total_energy': None,
                                                'posi_reactive_power': 0.0,
                                                'positive_active_today_energy': 0.0,
                                                'positive_active_total_energy': 0.0,
                                                'power_factor': 0.0,
                                                'power_factor_l1': 0.0,
                                                'power_factor_l2': 0.0,
                                                'power_factor_l3': 0.0,
                                                'reactive_energy': 0.0,
                                                'reactive_net_total_energy': None,
                                                'reactive_power': 0.0,
                                                'reactive_power_l1': 0.0,
                                                'reactive_power_l2': 0.0,
                                                'reactive_power_l3': 0.0,
                                                'reverse_active_energy': 0.0,
                                                'reverse_active_max_need': 0.0,
                                                'reverse_active_need': 0.0,
                                                'reverse_active_net_total_energy': None,
                                                'reverse_active_power': 0.0,
                                                'reverse_active_today_energy': 0.0,
                                                'reverse_active_total_energy': 0.0,
                                                'reverse_apparent_energy': 0.0,
                                                'reverse_instant_total_active_power': 0.0,
                                                'reverse_reactive_net_total_energy': None,
                                                'reverse_reactive_power': 0.0,
                                                'run_status': None,
                                                'soft_code': None,
                                                'soft_version': None,
                                                'status_last_update_time': None,
                                                'thdi1': None,
                                                'thdi2': None,
                                                'thdi3': None,
                                                'thdv1': None,
                                                'thdv2': None,
                                                'thdv3': None,
                                                'time_text': None,
                                                'today_energy': 0.0,
                                                'total_active_energy_l1': 0.0,
                                                'total_active_energy_l2': 0.0,
                                                'total_active_energy_l3': 0.0,
                                                'total_energy': 0.0,
                                                'total_reactive_energy_l1': 0.0,
                                                'total_reactive_energy_l2': 0.0,
                                                'total_reactive_energy_l3': 0.0,
                                                'user_energy': 0.0,
                                                'voltage': 0.0,
                                                'voltage_harmonic_avg': 0.0,
                                                'voltage_l1': 0.0,
                                                'voltage_l2': 0.0,
                                                'voltage_l3': 0.0,
                                                'voltage_ua': 0.0,
                                                'voltage_uab': 0.0,
                                                'voltage_ub': 0.0,
                                                'voltage_ubc': 0.0,
                                                'voltage_uc': 0.0,
                                                'voltage_uca': 0.0,
                                                'with_time': None,
                                                'zero_line_max_need': 0.0,
                                                'zero_line_need': 0.0},
                            'boost_data': {   'a_freq': 0.0,
                                              'a_ipv': 0.0,
                                              'a_jobs_model': 0,
                                              'a_load_normal_power': 0.0,
                                              'a_max_temp': 0.0,
                                              'a_min_temp': 0.0,
                                              'a_on_off': False,
                                              'a_ppv': 0.0,
                                              'a_set_power': 0.0,
                                              'a_start_power': 0.0,
                                              'a_temp': 0.0,
                                              'a_time': None,
                                              'a_total_energy': 0.0,
                                              'a_vpv': 0.0,
                                              'address': 0,
                                              'b_freq': 0.0,
                                              'b_ipv': 0.0,
                                              'b_load_normal_power': 0.0,
                                              'b_max_temp': 0.0,
                                              'b_min_temp': 0.0,
                                              'b_on_off': False,
                                              'b_ppv': 0.0,
                                              'b_start_power': 0.0,
                                              'b_temp': 0.0,
                                              'b_time': None,
                                              'b_total_energy': 0.0,
                                              'b_vpv': 0.0,
                                              'c_freq': 0.0,
                                              'c_ipv': 0.0,
                                              'c_load_normal_power': 0.0,
                                              'c_max_temp': 0.0,
                                              'c_min_temp': 0.0,
                                              'c_on_off': False,
                                              'c_ppv': 0.0,
                                              'c_start_power': 0.0,
                                              'c_temp': 0.0,
                                              'c_time': None,
                                              'c_total_energy': 0.0,
                                              'c_vpv': 0.0,
                                              'calendar': {   'first_day_of_week': 1,
                                                              'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                              'lenient': True,
                                                              'minimal_days_in_first_week': 1,
                                                              'time': {'date': 11, 'day': 2, 'hours': 15, 'minutes': 39, 'month': 4, 'seconds': 48, 'time': 1620718788781, 'timezone_offset': -480, 'year': 121},
                                                              'time_in_millis': 1620718788781,
                                                              'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                              'week_date_supported': True,
                                                              'week_year': 2021,
                                                              'weeks_in_week_year': 52},
                                              'current': 0.0,
                                              'd_power': 0.0,
                                              'd_total_energy': 0.0,
                                              'datalogger_sn': None,
                                              'device_type': None,
                                              'dry_contact_on_off': False,
                                              'dry_contact_status': 0,
                                              'dry_contact_time': None,
                                              'fw_version': None,
                                              'jobs_model': 0,
                                              'load_device_type': 0,
                                              'load_priority': 0,
                                              'max_temp': 0.0,
                                              'min_time': 0.0,
                                              'power': 0.0,
                                              'power_factor': 0.0,
                                              'reset_factory': 0,
                                              'restart': 0,
                                              'rf_command': None,
                                              'rf_pair': 0.0,
                                              'rs485_addr': 0,
                                              'rs485_baudrate': 0,
                                              'serial_num': None,
                                              'status': 0,
                                              'sys_time': None,
                                              'target_power': 0.0,
                                              'temp': 0.0,
                                              'temp_enable': 0.0,
                                              'temperature': 0.0,
                                              'time_text': datetime.datetime(2021, 5, 11, 15, 39, 48),
                                              'total_energy': 0.0,
                                              'total_number': 0,
                                              'tuning_state': 0,
                                              'v9420_status': 0,
                                              'version': None,
                                              'voltage': 0.0,
                                              'water_heater_power': 0.0,
                                              'water_state': 0,
                                              'with_time': False},
                            'box_data': None,
                            'children': [],
                            'datalogger_sn': 'NACTEST128',
                            'device_name': 'GRO_BOOST',
                            'device_sn': 'GRO2020102',
                            'device_type': 'WIFI_METER',
                            'device_type_int': 69,
                            'env_data': {   'address': 0,
                                            'air_pressure': None,
                                            'alarm_code': None,
                                            'calendar': None,
                                            'comm_status': None,
                                            'daily_avg_soil_lvl_pct': None,
                                            'datalogger_sn': None,
                                            'device_status': None,
                                            'efficiency': None,
                                            'env_humidity': 0.0,
                                            'env_temp': 0.0,
                                            'etoday_radiation': None,
                                            'etotal_radiation': None,
                                            'gas_concentration': None,
                                            'internal_pressure': None,
                                            'internal_relative_humidity': None,
                                            'internal_temp_c': None,
                                            'internal_temp_f': None,
                                            'last_four_measurements_avg': None,
                                            'panel_temp': 0.0,
                                            'radiant': 0.0,
                                            'rainfall_intensity': None,
                                            'run_status': None,
                                            'sensor_signal_gen': None,
                                            'snow_depth': None,
                                            'status_last_update_time': None,
                                            'time_text': None,
                                            'total_rainfall': None,
                                            'wind_angle': 0.0,
                                            'wind_speed': 0.0},
                            'img_path': './css/img/status_green.gif',
                            'irradiantion': 0.0,
                            'jdameter_data': None,
                            'key': 'NACTEST128_69_addr84',    # gitleaks:allow
                            'last_update_time': {'date': 11, 'day': 2, 'hours': 15, 'minutes': 33, 'month': 4, 'seconds': 11, 'time': 1620718391000, 'timezone_offset': -480, 'year': 121},
                            'last_update_time_text': datetime.datetime(2021, 5, 11, 15, 33, 11),
                            'level': 4,
                            'location': None,
                            'lost': False,
                            'meter_ct': 0,
                            'parent_id': 'LIST_NACTEST128_69',
                            'parent_sn': None,
                            'pid_data': None,
                            'plant_id': 0,
                            'pr_month': 0.0,
                            'raillog': False,
                            'spct_data': {   'active_energy': 0.0,
                                             'active_power': 0.0,
                                             'address': 0,
                                             'apparent_power': 0.0,
                                             'calendar': None,
                                             'datalogger_sn': None,
                                             'device_sn': None,
                                             'fei_lv_bo_z_energy': 0.0,
                                             'fei_lv_feng_z_energy': 0.0,
                                             'fei_lv_gu_z_energy': 0.0,
                                             'fei_lv_ping_z_energy': 0.0,
                                             'grid_energy': 0.0,
                                             'grid_energy_today': 0.0,
                                             'install_location': 0.0,
                                             'lost': False,
                                             'power_factor': 0.0,
                                             'reactive_energy': 0.0,
                                             'reactive_power': 0.0,
                                             'time_text': None,
                                             'total_energy': 0.0,
                                             'user_energy': 0.0,
                                             'user_energy_today': 0.0},
                            'tcp_server_ip': '47.107.154.111',
                            'timezone': 0,
                            'tree_id': 'OD_NACTEST128_69_addr84',
                            'tree_name': 'GRO_BOOST#84'},
                'datalogger_sn': 'NACTEST128',
                'device_sn': 'GRO2020102',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/boost/boost_data_info",
            params={
                "device_sn": device_sn,
            },
        )

        return GroboostDetails.model_validate(response)

    def metrics(
        self,
        device_sn: str,
    ) -> GroboostMetricsOverview:
        """
        Get the latest real-time data of GroBoost
        Interface to get the latest real-time data of GroBoost
        https://www.showdoc.com.cn/262556420217021/7178742217348819

        Note:
            Only applicable to devices with device type 11 (groboost) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: Boost does not exist
        * 10003: device SN error
        * 10011: no permission

        Args:
            device_sn (str): GROBOOST serial number

        Returns:
            GroboostMetricsOverview
            {   'data': {   'a_freq': 0.0,
                            'a_ipv': 0.0,
                            'a_jobs_model': 0,
                            'a_load_normal_power': 0.0,
                            'a_max_temp': 0.0,
                            'a_min_temp': 0.0,
                            'a_on_off': False,
                            'a_ppv': 0.0,
                            'a_set_power': 0.0,
                            'a_start_power': 0.0,
                            'a_temp': 0.0,
                            'a_time': None,
                            'a_total_energy': 0.0,
                            'a_vpv': 0.0,
                            'address': 0,
                            'b_freq': 0.0,
                            'b_ipv': 0.0,
                            'b_load_normal_power': 0.0,
                            'b_max_temp': 0.0,
                            'b_min_temp': 0.0,
                            'b_on_off': False,
                            'b_ppv': 0.0,
                            'b_start_power': 0.0,
                            'b_temp': 0.0,
                            'b_time': None,
                            'b_total_energy': 0.0,
                            'b_vpv': 0.0,
                            'c_freq': 0.0,
                            'c_ipv': 0.0,
                            'c_load_normal_power': 0.0,
                            'c_max_temp': 0.0,
                            'c_min_temp': 0.0,
                            'c_on_off': False,
                            'c_ppv': 0.0,
                            'c_start_power': 0.0,
                            'c_temp': 0.0,
                            'c_time': None,
                            'c_total_energy': 0.0,
                            'c_vpv': 0.0,
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 11, 'day': 2, 'hours': 14, 'minutes': 29, 'month': 4, 'seconds': 7, 'time': 1620714547000, 'timezone_offset': -480, 'year': 121},
                                            'time_in_millis': 1620714547000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2021,
                                            'weeks_in_week_year': 52},
                            'current': 0.0,
                            'd_power': 0.0,
                            'd_total_energy': 0.0,
                            'datalogger_sn': None,
                            'device_type': None,
                            'dry_contact_on_off': False,
                            'dry_contact_status': 0,
                            'dry_contact_time': None,
                            'fw_version': None,
                            'jobs_model': 0,
                            'load_device_type': 0,
                            'load_priority': 0,
                            'max_temp': 0.0,
                            'min_time': 0.0,
                            'power': 0.0,
                            'power_factor': 0.0,
                            'reset_factory': 0,
                            'restart': 0,
                            'rf_command': None,
                            'rf_pair': 0.0,
                            'rs485_addr': 0,
                            'rs485_baudrate': 0,
                            'serial_num': None,
                            'status': 0,
                            'sys_time': None,
                            'target_power': 3600.0,
                            'temp': 0.0,
                            'temp_enable': 0.0,
                            'temperature': 0.0,
                            'time_text': datetime.datetime(2021, 5, 11, 14, 29, 7),
                            'total_energy': 0.0,
                            'total_number': 0,
                            'tuning_state': 0,
                            'v9420_status': 0,
                            'version': '9.1.0.2',
                            'voltage': 0.0,
                            'water_heater_power': 0.0,
                            'water_state': 0,
                            'with_time': False},
                'datalogger_sn': 'NACTEST128',
                'device_sn': 'GRO2020102',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/boost/boost_last_data",
            data={
                "boost_sn": device_sn,
            },
        )

        return GroboostMetricsOverview.model_validate(response)

    # TODO
    def metrics_multiple(
        self,
        device_sn: Union[str, List[str]],
        page: Optional[int] = None,
    ) -> GroboostMetricsOverviewMultiple:
        """
        Get the latest real-time data of min in batches
        Interface to obtain the latest real-time data of inverters in batches
        https://www.showdoc.com.cn/262556420217021/6129830403882881

        Note:
            Only applicable to devices with device type 11 (groboost) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: Min does not exist
        * 10003: device SN error

        Args:
            device_sn (Union[str, List[str]]): GROBOOST serial number or list of (multiple) GROBOOST serial numbers (max 100)
            page (Optional[int]): page number, default 1, max 2

        Returns:
            MinEnergyOverviewMultiple
            {   'data': [   {   'datalogger_sn': 'XGD4A371YB',
                                'device_sn': 'HMG2A3807H',
                                'data': {   'address': 0,
                                            'again': False,
                                            'alias': None,
                                            'b_merter_connect_flag': None,
                                            'bat_sn': None,
                                            'battery_no': None,
                                            'battery_sn': None,
                                            'bdc1_charge_power': 0.0,
                                            'bdc1_charge_total': 0.0,
                                            'bdc1_discharge_power': 0.0,
                                            'bdc1_discharge_total': 0.0,
                                            'bdc1_fault_type': 0,
                                            'bdc1_ibat': 0.0,
                                            'bdc1_ibb': 0.0,
                                            'bdc1_illc': 0.0,
                                            'bdc1_mode': 0,
                                            'bdc1_soc': 0.0,
                                            'bdc1_status': 0,
                                            'bdc1_temp1': 0.0,
                                            'bdc1_temp2': 0.0,
                                            'bdc1_vbat': 0.0,
                                            'bdc1_vbus1': 0.0,
                                            'bdc1_vbus2': 0.0,
                                            'bdc1_warn_code': 0,
                                            'bdc2_charge_power': 0.0,
                                            'bdc2_charge_total': 0.0,
                                            'bdc2_discharge_power': 0.0,
                                            'bdc2_discharge_total': 0.0,
                                            'bdc2_fault_type': 0,
                                            'bdc2_ibat': 0.0,
                                            'bdc2_ibb': 0.0,
                                            'bdc2_illc': 0.0,
                                            'bdc2_mode': 0,
                                            'bdc2_soc': 0.0,
                                            'bdc2_status': 0,
                                            'bdc2_temp1': 0.0,
                                            'bdc2_temp2': 0.0,
                                            'bdc2_vbat': 0.0,
                                            'bdc2_vbus1': 0.0,
                                            'bdc2_vbus2': 0.0,
                                            'bdc2_warn_code': 0,
                                            'bdc_bus_ref': 0,
                                            'bdc_derate_reason': 0,
                                            'bdc_fault_sub_code': 0,
                                            'bdc_status': 0,
                                            'bdc_vbus2_neg': 0.0,
                                            'bdc_warn_sub_code': 0,
                                            'bgrid_type': None,
                                            'bms_communication_type': 0,
                                            'bms_cv_volt': 0.0,
                                            'bms_error2': 0,
                                            'bms_error3': 0,
                                            'bms_error4': None,
                                            'bms_fault_type': 0,
                                            'bms_fw_version': '0',
                                            'bms_ibat': 0.0,
                                            'bms_icycle': 0.0,
                                            'bms_info': 0,
                                            'bms_ios_status': None,
                                            'bms_max_curr': 0.0,
                                            'bms_mcu_version': '0',
                                            'bms_pack_info': 0,
                                            'bms_soc': 0.0,
                                            'bms_soh': 0.0,
                                            'bms_status': 0,
                                            'bms_temp1_bat': 0.0,
                                            'bms_using_cap': 0,
                                            'bms_vbat': 0.0,
                                            'bms_vdelta': 0.0,
                                            'bms_warn2': 0,
                                            'bms_warn_code': 0.0,
                                            'bsystem_work_mode': None,
                                            'calendar': {   'first_day_of_week': 1,
                                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                            'lenient': True,
                                                            'minimal_days_in_first_week': 1,
                                                            'time': {'date': 7, 'day': 4, 'hours': 19, 'minutes': 29, 'month': 0, 'seconds': 10, 'time': 1610018950000, 'timezone_offset': -480, 'year': 121},
                                                            'time_in_millis': 1610018950000,
                                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                            'week_date_supported': True,
                                                            'week_year': 2021,
                                                            'weeks_in_week_year': 52},
                                            'datalogger_sn': None,
                                            'day': None,
                                            'dc_voltage': 0.0,
                                            'dci_r': 6.0,
                                            'dci_s': 0.0,
                                            'dci_t': 0.0,
                                            'debug1': '208, 15, 1, 2595, 2235, 3600, 0, 0',
                                            'debug2': '0, 106, 165, 0, 0, 0, 7, 0',
                                            'derating_mode': 15,
                                            'dry_contact_status': 0,
                                            'e_charge_today': 0.0,
                                            'e_charge_total': 0.0,
                                            'e_discharge_today': 0.0,
                                            'e_discharge_total': 0.0,
                                            'e_local_load_today': 0.0,
                                            'e_local_load_total': 0.0,
                                            'e_self_today': 0.0,
                                            'e_self_total': 0.0,
                                            'e_system_today': 0.0,
                                            'e_system_total': 0.0,
                                            'e_to_grid_today': 0.0,
                                            'e_to_grid_total': 0.0,
                                            'e_to_user_today': 0.0,
                                            'e_to_user_total': 0.0,
                                            'eac_charge_today': 0.0,
                                            'eac_charge_total': 0.0,
                                            'eac_today': 41.900001525878906,
                                            'eac_total': 668.4,
                                            'eex1_today': None,
                                            'eex1_total': None,
                                            'eex2_today': None,
                                            'eex2_total': None,
                                            'eps_fac': 0.0,
                                            'eps_iac1': 0.0,
                                            'eps_iac2': 0.0,
                                            'eps_iac3': 0.0,
                                            'eps_pac': 0.0,
                                            'eps_pac1': 0.0,
                                            'eps_pac2': 0.0,
                                            'eps_pac3': 0.0,
                                            'eps_pf': -1.0,
                                            'eps_vac1': 0.0,
                                            'eps_vac2': 0.0,
                                            'eps_vac3': 0.0,
                                            'epv1_today': 22.899999618530273,
                                            'epv1_total': 367.9,
                                            'epv2_today': 20.100000381469727,
                                            'epv2_total': 318.5,
                                            'epv3_today': 0.0,
                                            'epv3_total': 0.0,
                                            'epv4_today': None,
                                            'epv4_total': None,
                                            'epv_total': 686.4,
                                            'error_text': 'Unknown',
                                            'fac': 50.0099983215332,
                                            'fault_type': 0,
                                            'fault_type1': None,
                                            'gfci': 68.0,
                                            'iac1': 0.30000001192092896,
                                            'iac2': 0.0,
                                            'iac3': 0.0,
                                            'iacr': 0.0,
                                            'inv_delay_time': 0.0,
                                            'ipv1': 0.0,
                                            'ipv2': 0.0,
                                            'ipv3': 0.0,
                                            'ipv4': 0.0,
                                            'is_again': False,
                                            'iso': 23182.0,
                                            'load_percent': 0.0,
                                            'lost': True,
                                            'mtnc_mode': None,
                                            'mtnc_rqst': None,
                                            'n_bus_voltage': 0.0,
                                            'new_warn_code': None,
                                            'new_warn_sub_code': None,
                                            'op_fullwatt': 0.0,
                                            'operating_mode': 0,
                                            'p_bus_voltage': 358.29998779296875,
                                            'p_self': 0.0,
                                            'p_system': 0.0,
                                            'pac': 1.2,
                                            'pac1': 3.0999999046325684,
                                            'pac2': 0.0,
                                            'pac3': 0.0,
                                            'pac_to_grid_total': 0.0,
                                            'pac_to_local_load': 0.0,
                                            'pac_to_user_total': 0.0,
                                            'pacr': 0.0,
                                            'pex1': None,
                                            'pex2': None,
                                            'pf': 1.0,
                                            'ppv': 1.4,
                                            'ppv1': 1.0,
                                            'ppv2': 0.4,
                                            'ppv3': 0.0,
                                            'ppv4': 0.0,
                                            'real_op_percent': 0.0,
                                            'serial_num': 'HMG2A3807H',
                                            'soc1': None,
                                            'soc2': None,
                                            'status': 1,
                                            'status_text': 'Normal',
                                            'sys_fault_word': 0,
                                            'sys_fault_word1': 0,
                                            'sys_fault_word2': 0,
                                            'sys_fault_word3': 106,
                                            'sys_fault_word4': 165,
                                            'sys_fault_word5': 0,
                                            'sys_fault_word6': 0,
                                            'sys_fault_word7': 0,
                                            't_mtnc_strt': None,
                                            't_win_end': None,
                                            't_win_start': None,
                                            'temp1': 33.599998474121094,
                                            'temp2': 0.0,
                                            'temp3': 0.0,
                                            'temp4': 0.0,
                                            'temp5': 42.099998474121094,
                                            'time': datetime.datetime(2021, 1, 7, 19, 29, 10),
                                            'time_total': 169507.4,
                                            'tlx_bean': None,
                                            'total_working_time': None,
                                            'uw_sys_work_mode': 0,
                                            'vac1': 231.0,
                                            'vac2': 0.0,
                                            'vac3': 0.0,
                                            'vac_rs': 231.0,
                                            'vac_st': 0.0,
                                            'vac_tr': 0.0,
                                            'vacr': 0.0,
                                            'vacrs': 0.0,
                                            'vpv1': 257.0,
                                            'vpv2': 224.0,
                                            'vpv3': 0.0,
                                            'vpv4': 0.0,
                                            'warn_code': 0,
                                            'warn_code1': None,
                                            'warn_text': 'Unknown',
                                            'win_mode': None,
                                            'win_off_grid_soc': None,
                                            'win_on_grid_soc': None,
                                            'win_request': None,
                                            'with_time': False},
                            },
                            {   'datalogger_sn': 'XGD3A206CA',
                                'device_sn': 'XTD7A2562B',
                                'data': {   'address': 0,
                                            # ...
                                            'with_time': False},
                                }],
                'error_code': 0,
                'error_msg': None,
                'page_num': 1}
        """

        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/tlx/tlxs_data",
            data={
                "tlxs": device_sn,
                "pageNum": page or 1,
            },
        )

        # Unfortunately, the original response cannot be parsed by pydantic as the inverter_sn is used as key
        # To fix this, resulting data is restructured
        devices = [
            GroboostMetricsOverviewMultipleItem(
                device_sn=inverter_sn,
                datalogger_sn=response.get("data", {})
                .get(inverter_sn, {})
                .get("dataloggerSn", None),
                data=response.get("data", {})
                .get(inverter_sn, {})
                .get(inverter_sn, None),
            )
            for inverter_sn in response.get("tlxs", [])
        ]
        response.pop("tlxs", None)
        response["data"] = devices

        return GroboostMetricsOverviewMultiple.model_validate(response)

    # TODO
    def metrics_history(
        self,
        device_sn: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> GroboostMetricsHistory:
        """
        Get historical data of a GroBoost
        An interface to obtain historical data of a GroBoost
        https://www.showdoc.com.cn/262556420217021/7178779509746518

        Note:
            Only applicable to devices with device type 11 (groboost) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: Boost does not exist
        * 10003: device SN error
        * 10011: no permission

        Args:
            device_sn (str): GROBOOST serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            GroboostMetricsHistory

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
            endpoint="device/boost/boost_data",
            data={
                "boost_sn": device_sn,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        # FIXME DEBUG
        sample_data = """    {
    "data": {
        "datas": [
            {
                "fwVersion": "1.0.0.0",
                "bfreq": 0,
                "bonOff": 0,
                "addr": 84,
                "cloadNormalPower": 360,
                "bppv": 0,
                "temperature": 0,
                "aminTemp": 40,
                "cipv": 0,
                "powerFactor": 0,
                "loadPriority": 0,
                "btotalEnergy": 0,
                "totalNumber": 0,
                "power": 0,
                "rs485BaudRate": 2,
                "serialNum": "GRO2020102",
                "cppv": 0,
                "status": 0,
                "cminTemp": 40,
                "atotalEnergy": 0,
                "bmaxTemp": 65,
                "ctime": null,
                "cfreq": 0,
                "bminTemp": 40,
                "sysTime": "2021-05-11 14:41:34",
                "appv": 0,
                "targetPower": 3600,
                "voltage": 0,
                "dryContactStatus": 0,
                "temp": 0,
                "dpower": 0,
                "aipv": 0,
                "minTime": 0,
                "avpv": 0,
                "dtotalEnergy": 0,
                "loadDeviceType": 0,
                "btemp": 0,
                "atime": null,
                "afreq": 0,
                "ajobsModel": 3,
                "bipv": 0,
                "rfCommand": "014207",
                "astartPower": 0,
                "rs485Addr": 1,
                "version": "9.1.0.2",
                "tuningState": 0,
                "asetPower": 0,
                "totalEneny": 0,
                "waterState": 0,
                "ctotalEnergy": 0,
                "dryContactTime": null,
                "deviceType": "69",
                "current": 0,
                "cmaxTemp": 65,
                "withTime": false,
                "bloadNormalPower": 360,
                "timeText": "2021-05-11 14:29:07",
                "dataLogSn": "NACTEST128",
                "amaxTemp": 65,
                "calendar": {
                    "minimalDaysInFirstWeek": 1,
                    "time": {
                        "time": 1620714547000,
                        "minutes": 29,
                        "seconds": 7,
                        "hours": 14,
                        "month": 4,
                        "timezoneOffset": -480,
                        "year": 121,
                        "day": 2,
                        "date": 11
                    },
                    "weekYear": 2021,
                    "weeksInWeekYear": 52,
                    "gregorianChange": {
                        "time": -12219292800000,
                        "minutes": 0,
                        "seconds": 0,
                        "hours": 8,
                        "month": 9,
                        "timezoneOffset": -480,
                        "year": -318,
                        "day": 5,
                        "date": 15
                    },
                    "timeZone": {
                        "lastRuleInstance": null,
                        "DSTSavings": 0,
                        "rawOffset": 28800000,
                        "ID": "Asia/Shanghai",
                        "dirty": false,
                        "displayName": "China Standard Time"
                    },
                    "lenient": true,
                    "timeInMillis": 1620714547000,
                    "firstDayOfWeek": 1,
                    "weekDateSupported": true
                },
                "restart": 0,
                "rfPair": 0,
                "btime": null,
                "resetFactory": 255,
                "bvpv": 0,
                "aloadNormalPower": 360,
                "atemp": 127,
                "v9420Status": 0,
                "maxTemp": 100,
                "cstartPower": 0,
                "waterHeaterPower": 360,
                "cvpv": 0,
                "aonOff": 0,
                "tempEnable": 1,
                "dryContactOnOff": 0,
                "bstartPower": 0,
                "jobsModel": 0,
                "ctemp": 0,
                "conOff": 0
            }
        ],
        "next_page_start_id": 21,
        "count": 254,
        "boost_sn": "GRO2020102",
        "datalogger_sn": "NACTEST128"
    },
    "error_code": 0,
    "error_msg": ""
}"""
        import json
        import pprint

        j = json.loads(sample_data)
        pprint.pprint(j, indent=4, width=500)
        k = GroboostMetricsHistory.model_validate(j)  # <-----------------------------
        pprint.pprint(k.model_dump(), indent=4, width=500)
        # FIXME DEBUG

        return GroboostMetricsHistory.model_validate(response)
