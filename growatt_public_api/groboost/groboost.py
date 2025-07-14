from datetime import date, timedelta
from typing import Optional, Union, List
from ..pydantic_models.groboost import (
    GroboostDetails,
    GroboostMetricsOverview,
    GroboostMetricsHistory,
    GroboostMetricsOverviewMultiple,
    GroboostMetricsOverviewMultipleItem,
)
from ..session.growatt_api_session import GrowattApiSession


class Groboost:
    """
    endpoints for GROBOOST Energy management system
    https://www.showdoc.com.cn/262556420217021/7178727239710262

    Note:
        Only applicable to devices with device type 11 (groboost) returned by plant.list_devices()
    """

    session: GrowattApiSession
    device_sn: Optional[str] = None

    def __init__(self, session: GrowattApiSession, device_sn: Optional[str] = None) -> None:
        self.session = session
        self.device_sn = device_sn

    def _device_sn(self, device_sn: Optional[Union[str, List[str]]]) -> Union[str, List[str]]:
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
    ) -> GroboostDetails:
        """
        Interface to get basic information of GroBoost
        https://www.showdoc.com.cn/262556420217021/7178727239710262

        Note:
            Only applicable to devices with device type 11 (groboost) returned by plant.list_devices()

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
                "device_sn": self._device_sn(device_sn),
            },
        )

        return GroboostDetails.model_validate(response)

    def metrics(
        self,
        device_sn: Optional[str] = None,
    ) -> GroboostMetricsOverview:
        """
        Get the latest real-time data of GroBoost
        Interface to get the latest real-time data of GroBoost
        https://www.showdoc.com.cn/262556420217021/7178742217348819

        Note:
            Only applicable to devices with device type 11 (groboost) returned by plant.list_devices()

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
                "boost_sn": self._device_sn(device_sn),
            },
        )

        return GroboostMetricsOverview.model_validate(response)

    def metrics_multiple(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        page: Optional[int] = None,
    ) -> GroboostMetricsOverviewMultiple:
        """
        Get the latest real-time data of GroBoost in batch
        Interface to obtain the latest real-time data of GroBoost in batches
        https://www.showdoc.com.cn/262556420217021/7178802101296935

        Note:
            Only applicable to devices with device type 11 (groboost) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: Boost does not exist
        * 10003: device SN error
        * 10011: no permission

        Args:
            device_sn (Union[str, List[str]]): GROBOOST serial number or list of (multiple) GROBOOST serial numbers (max 100)
            page (Optional[int]): page number, default 1, max 2

        Returns:
            MinEnergyOverviewMultiple
            {   'data': [   {   'data': {   'a_freq': 0.0,
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
                                            'calendar': {   'first_day_of_week': 1, ...},
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
                                            'target_power': 2001.0,
                                            'temp': 0.0,
                                            'temp_enable': 0.0,
                                            'temperature': 0.0,
                                            'time_text': datetime.datetime(2021, 5, 11, 14, 32, 6),
                                            'total_energy': 2.4000000953674316,
                                            'total_number': 0,
                                            'tuning_state': 0,
                                            'v9420_status': 0,
                                            'version': '9.1.0.2',
                                            'voltage': 0.0,
                                            'water_heater_power': 0.0,
                                            'water_state': 0,
                                            'with_time': False},
                                'datalogger_sn': 'NACTEST128',
                                'device_sn': 'GVH0A47005'},
                            {   'data': {   'a_freq': 0.0,
                                            # ...
                                            'with_time': False},
                                'datalogger_sn': 'NACTEST128',
                                'device_sn': 'GRO2020102'}],
                'error_code': 0,
                'error_msg': None,
                'page_num': 1}
        """

        device_sn = self._device_sn(device_sn)
        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/boost/boosts_data",
            data={
                "boosts": device_sn,
                "pageNum": page or 1,
            },
        )

        # Unfortunately, the original response cannot be parsed by pydantic as the inverter_sn is used as key
        # To fix this, resulting data is restructured
        devices = [
            GroboostMetricsOverviewMultipleItem(
                device_sn=inverter_sn,
                datalogger_sn=response.get("data", {}).get(inverter_sn, {}).get("dataloggerSn", None),
                data=response.get("data", {}).get(inverter_sn, {}).get(inverter_sn, None),
            )
            for inverter_sn in response.get("boosts", [])
        ]
        response.pop("boosts", None)
        response["data"] = devices

        return GroboostMetricsOverviewMultiple.model_validate(response)

    def metrics_history(
        self,
        device_sn: Optional[str] = None,
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
            Only applicable to devices with device type 11 (groboost) returned by plant.list_devices()

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
            {   'data': {   'count': 254,
                            'datalogger_sn': 'NACTEST128',
                            'datas': [   {   'a_freq': 0.0,
                                             'a_ipv': 0.0,
                                             'a_jobs_model': 3,
                                             'a_load_normal_power': 360.0,
                                             'a_max_temp': 65.0,
                                             'a_min_temp': 40.0,
                                             'a_on_off': False,
                                             'a_ppv': 0.0,
                                             'a_set_power': 0.0,
                                             'a_start_power': 0.0,
                                             'a_temp': 127.0,
                                             'a_time': None,
                                             'a_total_energy': 0.0,
                                             'a_vpv': 0.0,
                                             'address': 84,
                                             'b_freq': 0.0,
                                             'b_ipv': 0.0,
                                             'b_load_normal_power': 360.0,
                                             'b_max_temp': 65.0,
                                             'b_min_temp': 40.0,
                                             'b_on_off': False,
                                             'b_ppv': 0.0,
                                             'b_start_power': 0.0,
                                             'b_temp': 0.0,
                                             'b_time': None,
                                             'b_total_energy': 0.0,
                                             'b_vpv': 0.0,
                                             'c_freq': 0.0,
                                             'c_ipv': 0.0,
                                             'c_load_normal_power': 360.0,
                                             'c_max_temp': 65.0,
                                             'c_min_temp': 40.0,
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
                                             'device_type': '69',
                                             'dry_contact_on_off': False,
                                             'dry_contact_status': 0,
                                             'dry_contact_time': None,
                                             'fw_version': '1.0.0.0',
                                             'jobs_model': 0,
                                             'load_device_type': 0,
                                             'load_priority': 0,
                                             'max_temp': 100.0,
                                             'min_time': 0.0,
                                             'power': 0.0,
                                             'power_factor': 0.0,
                                             'reset_factory': 255,
                                             'restart': 0,
                                             'rf_command': '014207',
                                             'rf_pair': 0.0,
                                             'rs485_addr': 1,
                                             'rs485_baudrate': 2,
                                             'serial_num': 'GRO2020102',
                                             'status': 0,
                                             'sys_time': '2021-05-11 14:41:34',
                                             'target_power': 3600.0,
                                             'temp': 0.0,
                                             'temp_enable': 1.0,
                                             'temperature': 0.0,
                                             'time_text': datetime.datetime(2021, 5, 11, 14, 29, 7),
                                             'total_energy': 0.0,
                                             'total_number': 0,
                                             'tuning_state': 0,
                                             'v9420_status': 0,
                                             'version': '9.1.0.2',
                                             'voltage': 0.0,
                                             'water_heater_power': 360.0,
                                             'water_state': 0,
                                             'with_time': False}],
                            'device_sn': 'GRO2020102',
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
            endpoint="device/boost/boost_data",
            data={
                "boost_sn": self._device_sn(device_sn),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return GroboostMetricsHistory.model_validate(response)
