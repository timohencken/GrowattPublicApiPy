from datetime import date
from typing import Union, List, Optional

from ..api_v4 import ApiV4
from ..growatt_types import DeviceType
from ..pydantic_models.api_v4 import (
    WitDetailsV4,
    WitEnergyV4,
    WitEnergyHistoryV4,
    WitEnergyHistoryMultipleV4,
    SettingReadVppV4,
    SettingWriteV4,
)

from ..session import GrowattApiSession


class Wit:
    """
    endpoints for WIT devices
    https://www.showdoc.com.cn/2540838290984246/11292927244927496
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
    ) -> WitDetailsV4:
        """
        Batch device information using "new-api" endpoint
        Retrieve basic information of devices in bulk based on device SN.
        https://www.showdoc.com.cn/2540838290984246/11292915673945114

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            WitDetailsV4
            e.g.
            {   'data': {   'wit': [   {   'ac_stop_charging_soc': 0.0,
                                           'active_rate': 100.0,
                                           'address': 1,
                                           'alias': 'QWL0DC3002',
                                           'anti_backflow_failure_power_percent': -0.1,
                                           'anti_backflow_failure_time': -1.0,
                                           'anti_backflow_flag': False,
                                           'ats_version': None,
                                           'b_bak_bat2_soc': -1.0,
                                           'b_bak_bat3_soc': -1.0,
                                           'b_bak_soc': 0.0,
                                           'bat_connection_type': 1,
                                           'bat_connection_type2': 0,
                                           'bat_connection_type3': 0,
                                           'bat_serial_num1': None,
                                           'bat_serial_num2': None,
                                           'bat_serial_num3': None,
                                           'bat_serial_num4': None,
                                           'bat_serial_num5': None,
                                           'bat_sleep_wake_up1': 0,
                                           'bat_sleep_wake_up2': 0,
                                           'bat_sleep_wake_up3': 0,
                                           'baudrate': 64,
                                           'bms1_enable': True,
                                           'bms2_enable': False,
                                           'bms3_enable': False,
                                           'charge_soc_limit': 0.0,
                                           'children': None,
                                           'com_address': 1,
                                           'com_name': None,
                                           'communication_version': 'ZBea-0042',
                                           'country_selected': 0,
                                           'datalogger_sn': 'XGD6E7C4S2',
                                           'device_type': 218,
                                           'discharge_soc_limit': 0.0,
                                           'drms_enable': False,
                                           'drms_mode': 0,
                                           'dtc': 5600,
                                           'energy_day': 0.0,
                                           'energy_day_map': {},
                                           'energy_month': 0.0,
                                           'energy_month_text': '0',
                                           'fac_high': 505.0,
                                           'fac_high2': 50.5,
                                           'fac_high3': 50.5,
                                           'fac_low': 475.0,
                                           'fac_low2': 47.5,
                                           'fac_low3': 47.5,
                                           'forced_stop_switch1': False,
                                           'forced_stop_switch2': False,
                                           'forced_stop_switch3': False,
                                           'forced_stop_switch4': False,
                                           'forced_stop_switch5': False,
                                           'forced_stop_switch6': False,
                                           'forced_time_start1': datetime.time(0, 0),
                                           'forced_time_start2': datetime.time(0, 0),
                                           'forced_time_start3': datetime.time(0, 0),
                                           'forced_time_start4': datetime.time(0, 0),
                                           'forced_time_start5': datetime.time(0, 0),
                                           'forced_time_start6': datetime.time(0, 0),
                                           'forced_time_stop1': datetime.time(0, 0),
                                           'forced_time_stop2': datetime.time(0, 0),
                                           'forced_time_stop3': datetime.time(0, 0),
                                           'forced_time_stop4': datetime.time(0, 0),
                                           'forced_time_stop5': datetime.time(0, 0),
                                           'forced_time_stop6': datetime.time(0, 0),
                                           'freq_change_enable': -1,
                                           'freq_high_limit': 50.2,
                                           'freq_low_limit': 49.5,
                                           'fw_version': 'TO1.0',
                                           'grid_meter_enable': True,
                                           'grid_reconnection_time': 300,
                                           'group_id': -1,
                                           'heat_up_time': -1.0,
                                           'hl_voltage_enable': False,
                                           'id': 0,
                                           'img_path': './css/img/status_gray.gif',
                                           'last_update_time': 1728205322000,
                                           'last_update_time_text': datetime.datetime(2024, 10, 6, 17, 2, 2),
                                           'lcd_language': 1,
                                           'level': 4,
                                           'line_n_disconnect_enable': False,
                                           'load_red_rate': -0.1,
                                           'location': None,
                                           'lost': True,
                                           'max_spontaneous_selfuse': 0.0,
                                           'modbus_version': 307,
                                           'model': 2378182293228422120,
                                           'model_text': 'S21B01D00T32P0FU01M03E8',
                                           'module1': 0,
                                           'module2': 0,
                                           'module3': 0,
                                           'module4': 0,
                                           'oil_charge_power_limit': -0.1,
                                           'oil_enable': False,
                                           'oil_rated_power': 0.0,
                                           'on_off': True,
                                           'over_fre_drop_point': 50.3,
                                           'over_fre_lo_red_delay_time': 0.0,
                                           'over_fre_lo_red_res_time': 0.0,
                                           'over_fre_lo_red_slope': 50.0,
                                           'parallel_enable': True,
                                           'param_protect_enable': False,
                                           'parent_id': 'LIST_XGD6E7C4S2_218',
                                           'pf_level1': 0.0,
                                           'pf_level2': 0.0,
                                           'pf_level3': 0.0,
                                           'pf_level4': 0.0,
                                           'pf_level5': 0.0,
                                           'pf_level6': 0.0,
                                           'pf_level7': 0.0,
                                           'pf_level8': 0.0,
                                           'pf_model': 0.0,
                                           'pflinep1_lp': 0.0,
                                           'pflinep1_pf': -1.0,
                                           'pflinep2_lp': 0.0,
                                           'pflinep2_pf': -1.0,
                                           'pflinep3_lp': 0.0,
                                           'pflinep3_pf': -1.0,
                                           'pflinep4_lp': 0.0,
                                           'pflinep4_pf': -1.0,
                                           'plant_id': 0,
                                           'plant_name': None,
                                           'pmax': 100000,
                                           'pmax_level1': 0.0,
                                           'pmax_level2': 0.0,
                                           'pmax_level3': 0.0,
                                           'pmax_level4': 0.0,
                                           'pmax_level5': 0.0,
                                           'pmax_level6': 0.0,
                                           'pmax_level7': 0.0,
                                           'pmax_level8': 0.0,
                                           'port_name': 'ShinePano - XGD6E7C4S2',
                                           'power_factor': 0.5,
                                           'power_imbalance_control_enable': False,
                                           'power_max': None,
                                           'power_max_text': None,
                                           'power_max_time': None,
                                           'power_ud_forced_enable': False,
                                           'pu_enable': 0,
                                           'pv_num': 0,
                                           'pv_pf_cmd_memory_state': False,
                                           'reactive_output_priority': 0,
                                           'reactive_rate': 0.0,
                                           'reactive_value': 0.0,
                                           'record': None,
                                           'restart_time': 30,
                                           'rrcr_enable': 0.0,
                                           'safety_correspond_num': 0.0,
                                           'safety_function': 0,
                                           'safety_version': 0,
                                           'serial_num': 'QWL0DC3002',
                                           'single_export': 1,
                                           'status': -1,
                                           'status_text': 'wit.status.lost',
                                           'str_num': 0,
                                           'svg_function': 0,
                                           'sys_optical_storage_mode': 0,
                                           'sys_time': '2024-10-06 16:27:29',
                                           'sys_time_text': datetime.datetime(2024, 10, 6, 16, 27, 29),
                                           'tcp_server_ip': '127.0.0.1',
                                           'time1_mode': 0,
                                           'time1_power': 0.0,
                                           'time2_mode': 0,
                                           'time2_power': 0.0,
                                           'time3_mode': 0,
                                           'time3_power': 0.0,
                                           'time4_mode': 0,
                                           'time4_power': 0.0,
                                           'time5_mode': 0,
                                           'time5_power': 0.0,
                                           'time6_mode': 0,
                                           'time6_power': 0.0,
                                           'time_start': 30,
                                           'timezone': 8.0,
                                           'tree_id': 'ST_QWL0DC3002',
                                           'tree_name': 'QWL0DC3002',
                                           'underfreq_load_delay_time': 0.0,
                                           'underfreq_load_enable': -1,
                                           'underfreq_load_point': 49.8,
                                           'underfreq_load_res_time': 0.0,
                                           'underfreq_load_slope': 400,
                                           'updating': False,
                                           'user_name': None,
                                           'uw_1th_bat_charge_limit': 100.0,
                                           'uw_1th_bat_discharge_limit': 100.0,
                                           'uw_2th_bat_cap': 9947.0,
                                           'uw_2th_bat_charge_limit': 993.4,
                                           'uw_2th_bat_discharge_limit': 1000.0,
                                           'uw_2th_bat_end_of_vol': 1017.3,
                                           'uw_2th_bat_max_charge_curr': 1021.6,
                                           'uw_2th_bat_max_charge_vol': 1006.9,
                                           'uw_2th_bat_max_discharge_curr': 994.7,
                                           'uw_3th_bat_cap': 10000.0,
                                           'uw_3th_bat_charge_limit': 1000.0,
                                           'uw_3th_bat_discharge_limit': 1000.0,
                                           'uw_3th_bat_end_of_vol': 1000.0,
                                           'uw_3th_bat_max_charge_curr': 1000.0,
                                           'uw_3th_bat_max_charge_vol': 1000.0,
                                           'uw_3th_bat_max_discharge_curr': 1000.0,
                                           'uw_a_couple_enable': -1,
                                           'uw_a_couple_end_soc': -1.0,
                                           'uw_a_couple_start_soc': -1.0,
                                           'uw_ac_charge_enable': True,
                                           'uw_ac_charge_power_rate': 100.0,
                                           'uw_anti_backflow': 1,
                                           'uw_bat_cap': 100.0,
                                           'uw_bat_charge_stop_soc': 100.0,
                                           'uw_bat_charge_stop_soc2': -1.0,
                                           'uw_bat_charge_stop_soc3': -1.0,
                                           'uw_bat_cnn_way': 10000.0,
                                           'uw_bat_discharge_stop_soc': 10.0,
                                           'uw_bat_discharge_stop_soc2': -1.0,
                                           'uw_bat_discharge_stop_soc3': -1.0,
                                           'uw_bat_enable1': False,
                                           'uw_bat_enable2': False,
                                           'uw_bat_enable3': False,
                                           'uw_bat_max_charge_current': 100.0,
                                           'uw_bat_max_discharge_current': 100.0,
                                           'uw_batt_eod_vol': 620.0,
                                           'uw_batt_max_charge_vol': 800.0,
                                           'uw_batt_type1': 0,
                                           'uw_batt_type2': 0,
                                           'uw_batt_type3': 0,
                                           'uw_connect_phase_mode': 1,
                                           'uw_demand_mange_charge_power_limit': 0.0,
                                           'uw_demand_mange_discharge_power_limit': 0.0,
                                           'uw_demand_mange_enable': False,
                                           'uw_dg_start_soc': 60.0,
                                           'uw_dg_stop_soc': 30.0,
                                           'uw_disconnect_phase_mode': 1,
                                           'uw_gen_port_dev_type': 0,
                                           'uw_gen_power': 0.0,
                                           'uw_load_pv_inverter': 0,
                                           'uw_off_grid_enable': False,
                                           'uw_off_grid_freq': 0.0,
                                           'uw_off_grid_soc1': 5.0,
                                           'uw_off_grid_soc2': -1.0,
                                           'uw_off_grid_soc3': -1.0,
                                           'uw_off_grid_vol': 1.0,
                                           'uw_on_off_change_manual_mode': 0,
                                           'uw_on_off_change_mode': 2,
                                           'uw_on_off_grid_set': 0,
                                           'uw_pcs_type': 0,
                                           'v_bak_soc_enable': False,
                                           'vac_high': 438.2,
                                           'vac_high2': 537.8,
                                           'vac_high3': 537.8,
                                           'vac_low': 338.6,
                                           'vac_low2': 199.1,
                                           'vac_low3': 199.1,
                                           'version': 'TOaa211689',
                                           'vnormal': 1.0,
                                           'voltage_high_limit': 438.2,
                                           'voltage_low_limit': 338.6,
                                           'vpv_start': 195.0,
                                           'w_anti_backflow_meter_power_limit': 0.0,
                                           'w_power_restart_slope_ee': 5000.0,
                                           'w_power_start_slope': 5000.0,
                                           'wide_voltage_enable': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.details(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.WIT,
        )

    def energy_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> WitEnergyV4:
        """
        Batch equipment data information using "new-api" endpoint
        Retrieve the last detailed data for multiple devices based on their SN and device type.
        https://www.showdoc.com.cn/2540838290984246/11292915898375566

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            WitEnergyV4
            e.g.
            {   'data': {   'wit': [   {   'ac_charge_energy_today': 0.0,
                                           'ac_charge_energy_total': 7843.2001953125,
                                           'again': False,
                                           'b_afci_status': 0,
                                           'b_alarm_sub_code': -1,
                                           'b_bat_bus_target': 0.0,
                                           'b_bms_sta': -1,
                                           'b_cluster_cnt': -1,
                                           'b_fault_sub_code': -1,
                                           'b_flag_chg_dis': -1,
                                           'b_packs_cnt': -1,
                                           'b_sig_mode_cell_cnt': -1,
                                           'b_sig_pack_mode_cnt': -1,
                                           'b_soc': -1.0,
                                           'b_soh': -1.0,
                                           'b_status_first': -1,
                                           'b_status_sec': -1,
                                           'b_sys_avg_soc': -1.0,
                                           'b_sys_max_soc': -1.0,
                                           'b_sys_max_soc_pack_num': -0.1,
                                           'b_sys_min_soc': -1.0,
                                           'b_sys_min_soc_pack_num': -0.1,
                                           'bat_curr_first': -0.1,
                                           'bat_curr_sec': -0.1,
                                           'bat_power': 0.0,
                                           'bat_power2': 0.0,
                                           'bat_power3': 0.0,
                                           'bat_type': 6513.6,
                                           'bat_volt_first': -0.1,
                                           'bat_volt_sec': -0.1,
                                           'battery_type': 0,
                                           'bms_bat_vol2': 0.0,
                                           'bms_bat_vol3': 0.0,
                                           'bms_battery_volt': 48.0,
                                           'bms_max_temp2': 0.0,
                                           'bms_max_temp3': 0.0,
                                           'bms_min_temp2': 0.0,
                                           'bms_min_temp3': 0.0,
                                           'bms_sell_max_vol2': 0.0,
                                           'bms_sell_max_vol3': 0.0,
                                           'bms_sell_min_vol2': 0.0,
                                           'bms_sell_min_vol3': 0.0,
                                           'bus_cap_using': 414.0,
                                           'calendar': 1728205321768,
                                           'cbat': 0.0,
                                           'cbat2': 0.0,
                                           'cbat3': 0.0,
                                           'current_string1': 0.0,
                                           'current_string10': 0.0,
                                           'current_string11': 0.0,
                                           'current_string12': 0.0,
                                           'current_string13': 0.0,
                                           'current_string14': 0.0,
                                           'current_string15': 0.0,
                                           'current_string16': 0.0,
                                           'current_string17': 0.0,
                                           'current_string18': 0.0,
                                           'current_string19': 0.0,
                                           'current_string2': 0.0,
                                           'current_string20': 0.0,
                                           'current_string3': 0.0,
                                           'current_string4': 0.0,
                                           'current_string5': 0.0,
                                           'current_string6': 0.0,
                                           'current_string7': 0.0,
                                           'current_string8': 0.0,
                                           'current_string9': 0.0,
                                           'datalogger_sn': 'XGD6E7C4S2',
                                           'day_map': None,
                                           'delay_time': 30.0,
                                           'derating_mode': 14,
                                           'device_sn': 'QWL0DC3002',
                                           'e_charge1_today': 2.6,
                                           'e_charge1_total': 8131.7,
                                           'e_charge2_today': 0.0,
                                           'e_charge2_total': 0.0,
                                           'e_charge3_today': 0.0,
                                           'e_charge3_total': 0.0,
                                           'e_discharge1_today': None,
                                           'e_discharge1_total': None,
                                           'e_discharge2_today': 0.0,
                                           'e_discharge2_total': 0.0,
                                           'e_discharge3_today': 0.0,
                                           'e_discharge3_total': 0.0,
                                           'e_local_load_today': 2.5,
                                           'e_local_load_total': 2906.4,
                                           'e_self_today': 2.299999952316284,
                                           'e_self_total': 326.70001220703125,
                                           'e_system_today': 2.299999952316284,
                                           'e_system_total': 6368.89990234375,
                                           'e_to_grid_today': 0.0,
                                           'e_to_grid_total': None,
                                           'e_to_user_today': 0.1,
                                           'e_to_user_total': 8813.6,
                                           'eac_today': 2.2,
                                           'eac_total': 6209.6,
                                           'eex_today': 14644.4,
                                           'eex_total': 78610.9,
                                           'epv10_today': 2.5,
                                           'epv10_total': 24.399999618530273,
                                           'epv1_today': 0.0,
                                           'epv1_total': 7.8,
                                           'epv2_today': 0.0,
                                           'epv2_total': 0.0,
                                           'epv3_today': 0.0,
                                           'epv3_total': 29.399999618530273,
                                           'epv4_today': 0.0,
                                           'epv4_total': 0.0,
                                           'epv5_today': 0.0,
                                           'epv5_total': 0.0,
                                           'epv6_today': 0.0,
                                           'epv6_total': 0.0,
                                           'epv7_today': 0.0,
                                           'epv7_total': 0.0,
                                           'epv8_today': 0.0,
                                           'epv8_total': 0.0,
                                           'epv9_today': 2.299999952316284,
                                           'epv9_total': 23.5,
                                           'epv_today': 4.799999952316284,
                                           'epv_total': 85.1,
                                           'error_code': 0,
                                           'error_text': 'Unknown',
                                           'fac': 0.0,
                                           'fan_fault_bit': 0.0,
                                           'fault_bit_code': 1,
                                           'fault_code': 501,
                                           'fault_value': 0,
                                           'flash_erase_aging_ok_flag': False,
                                           'gen_port1_volt': 0.0,
                                           'gen_port2_volt': 0.0,
                                           'gen_port3_volt': 0.0,
                                           'gen_power': 0.0,
                                           'gfci': 0.0,
                                           'hcpc_low_volt_num': -0.1,
                                           'hcpc_max_volt_num': -0.1,
                                           'hcpc_single_low_temp_num': -0.1,
                                           'hcpc_single_low_volt_num': -0.1,
                                           'hcpc_single_max_temp_num': -0.1,
                                           'hcpc_single_max_volt_num': -0.1,
                                           'hcpc_temp_num': -0.1,
                                           'hcpc_temp_num1': -0.1,
                                           'iac1': 0.0,
                                           'iac2': 0.0,
                                           'iac3': 0.0,
                                           'iac_load': 0.3,
                                           'iacs_load': 0.3,
                                           'iact_load': 0.3,
                                           'inv_r_volt_first': -0.1,
                                           'inv_r_volt_sec': -0.1,
                                           'inv_s_volt_first': -0.1,
                                           'inv_s_volt_sec': -0.1,
                                           'inv_t_volt_first': -0.1,
                                           'inv_t_volt_sec': -0.1,
                                           'ipv1': 0.0,
                                           'ipv10': 0.0,
                                           'ipv2': 0.0,
                                           'ipv3': 0.0,
                                           'ipv4': 0.0,
                                           'ipv5': 0.0,
                                           'ipv6': 0.0,
                                           'ipv7': 0.0,
                                           'ipv8': 0.0,
                                           'ipv9': 0.0,
                                           'off_grid_status': 0,
                                           'on_off_grid_state': 0,
                                           'on_off_grid_state_first': 0,
                                           'on_off_grid_state_sec': 0,
                                           'op_fullwatt': 0.0,
                                           'p_self': 0.0,
                                           'p_system': 0.0,
                                           'pac': 0.0,
                                           'pac1': 0.0,
                                           'pac2': 0.0,
                                           'pac3': 0.0,
                                           'pac_to_grid_total': 0.0,
                                           'pac_to_user_total': 0.0,
                                           'pex': 0.0,
                                           'pf': 1.0,
                                           'pid_bus': 0.0,
                                           'pid_fault_code': 0,
                                           'pid_status': 0,
                                           'plocal_load_total': 0.0,
                                           'pm_derate': 0.0,
                                           'ppv': 0.0,
                                           'ppv1': 0.0,
                                           'ppv10': 0.0,
                                           'ppv2': 0.0,
                                           'ppv3': 0.0,
                                           'ppv4': 0.0,
                                           'ppv5': 0.0,
                                           'ppv6': 0.0,
                                           'ppv7': 0.0,
                                           'ppv8': 0.0,
                                           'ppv9': 0.0,
                                           'priority_choose': 0.0,
                                           'pv_iso': 65530.0,
                                           'r_dci': 0.0,
                                           'react_power': 0.0,
                                           'react_power_max': 48437.5,
                                           'react_power_total': 1325.6,
                                           'reactive_power_real_value_first': 0.0,
                                           'reactive_power_real_value_sec': 0.0,
                                           'real_op_percent': 0.0,
                                           'real_power': 0.0,
                                           'reverse_curr1': 0.0,
                                           'reverse_curr2': 0.0,
                                           'reverse_curr3': 0.0,
                                           'run_time': 414.0,
                                           's_dci': 0.0,
                                           'sac': 0.0,
                                           'soc': 13.0,
                                           'soc2': 0.0,
                                           'soc3': 0.0,
                                           'soh': 100.0,
                                           'soh2': 0.0,
                                           'soh3': 0.0,
                                           'status': 1,
                                           'status_text': 'Operating',
                                           'str_break': 0,
                                           'str_break2': 0,
                                           'str_unbalance': 0,
                                           'str_unbalance2': 0,
                                           'str_unmatch': 0,
                                           'str_unmatch2': 0,
                                           'str_warning_value1': 0,
                                           'str_warning_value2': 0,
                                           'string_prompt': 0,
                                           'sys_on_pack_cnt': 0.0,
                                           't_dci': 0.0,
                                           'temp1': 34.600002,
                                           'temp2': 43.5,
                                           'temp3': 28.4,
                                           'time': datetime.datetime(2024, 10, 6, 17, 2, 1),
                                           'time_total': 4226661.5,
                                           'u_ac_power': -0.1,
                                           'u_bat_chg_p': -0.1,
                                           'u_bat_dsg_p': -0.1,
                                           'ud_acc_chg_soe': -0.1,
                                           'ud_acc_dis_soe': -0.1,
                                           'ud_calib_apparent_power_first': -0.1,
                                           'ud_calib_apparent_power_sec': -0.1,
                                           'ud_fault_bit_high': False,
                                           'ud_fault_bit_low': False,
                                           'ud_op_r_watt_first': -0.1,
                                           'ud_op_r_watt_sec': -0.1,
                                           'ud_op_rst_watt_first': -0.1,
                                           'ud_op_rst_watt_sec': -0.1,
                                           'ud_op_s_watt_first': -0.1,
                                           'ud_op_s_watt_sec': -0.1,
                                           'ud_op_t_watt_first': -0.1,
                                           'ud_op_t_watt_sec': -0.1,
                                           'usb_aging_test_ok_flag': False,
                                           'uw_alarm_code': -1,
                                           'uw_ambient_first': -0.1,
                                           'uw_ambient_sec': -0.1,
                                           'uw_bat_enable1': False,
                                           'uw_bat_enable2': False,
                                           'uw_bat_enable3': False,
                                           'uw_cell_max_v_chg': -1.0,
                                           'uw_cell_min_v_dis': -1.0,
                                           'uw_cell_tavg_value': -0.1,
                                           'uw_cell_tmax_value': -0.1,
                                           'uw_cell_tmin_value': -0.1,
                                           'uw_cell_uavg_value': -1.0,
                                           'uw_cell_umax_value': -1.0,
                                           'uw_cell_umin_value': -0.1,
                                           'uw_charge_max_vol': -0.1,
                                           'uw_fault_code': -1,
                                           'uw_freq_first': -0.01,
                                           'uw_freq_sec': -0.01,
                                           'uw_full_charge_capacity': -0.1,
                                           'uw_gen_port_dev_type': 0,
                                           'uw_inv_first': -0.1,
                                           'uw_inv_sec': -0.1,
                                           'uw_inv_warn_value': 0,
                                           'uw_load_per_first': -1,
                                           'uw_load_per_sec': -1,
                                           'uw_main_code_first': -1,
                                           'uw_main_code_sec': -1,
                                           'uw_main_warn_first': -1,
                                           'uw_main_warn_sec': -1,
                                           'uw_mod_max_bla_temp_value': -0.1,
                                           'uw_mod_max_vol_value': -0.01,
                                           'uw_mod_min_bla_temp_value': -0.1,
                                           'uw_mode_avg_vol_value': -0.01,
                                           'uw_mode_min_vol_value': -0.01,
                                           'uw_mode_rated_cap': -0.1,
                                           'uw_mode_rated_vol': -0.01,
                                           'uw_n_bus_volt_first': -0.1,
                                           'uw_n_bus_volt_sec': -0.1,
                                           'uw_op_line_rs_first': -0.1,
                                           'uw_op_line_rs_sec': -0.1,
                                           'uw_op_line_st_first': -0.1,
                                           'uw_op_line_st_sec': -0.1,
                                           'uw_op_line_tr_first': -0.1,
                                           'uw_op_line_tr_sec': -0.1,
                                           'uw_op_phase_r_curr_first': -0.1,
                                           'uw_op_phase_r_curr_sec': -0.1,
                                           'uw_op_phase_r_volt_first': -0.1,
                                           'uw_op_phase_r_volt_sec': -0.1,
                                           'uw_op_phase_s_curr_first': -0.1,
                                           'uw_op_phase_s_curr_sec': -0.1,
                                           'uw_op_phase_s_volt_first': -0.1,
                                           'uw_op_phase_s_volt_sec': -0.1,
                                           'uw_op_phase_t_curr_first': -0.1,
                                           'uw_op_phase_t_curr_sec': -0.1,
                                           'uw_op_phase_t_volt_first': -0.1,
                                           'uw_op_phase_t_volt_sec': -0.1,
                                           'uw_output_first': -0.1,
                                           'uw_output_sec': -0.1,
                                           'uw_p_bus_volt_first': -0.1,
                                           'uw_p_bus_volt_sec': -0.1,
                                           'uw_rated_battery_capacity': -0.1,
                                           'uw_rated_battery_power_energy': -0.1,
                                           'uw_rdci_curr_first': -0.1,
                                           'uw_rdci_curr_sec': -0.1,
                                           'uw_sdci_curr_first': -0.1,
                                           'uw_sdci_curr_sec': -0.1,
                                           'uw_sub_code_first': -1,
                                           'uw_sub_code_sec': -1,
                                           'uw_sub_warn_first': -1,
                                           'uw_sub_warn_sec': -1,
                                           'uw_sys_load_vol_value': -0.1,
                                           'uw_sys_max_allow_ichg': -0.1,
                                           'uw_sys_max_allow_idis': -0.1,
                                           'uw_sys_max_vtotalchg': -0.1,
                                           'uw_sys_min_vtotaldis': -0.1,
                                           'uw_sys_tota_vol_value': -0.1,
                                           'uw_sys_total_i_value': -0.1,
                                           'uw_tdci_curr_first': -0.1,
                                           'uw_tdci_curr_sec': -0.1,
                                           'uw_upack_rated': -0.1,
                                           'v_bat_dsp': 661.0,
                                           'v_bus_n': 328.2,
                                           'v_bus_p': 330.5,
                                           'v_string1': 88.7,
                                           'v_string10': 89.0,
                                           'v_string11': 89.1,
                                           'v_string12': 89.1,
                                           'v_string13': 88.5,
                                           'v_string14': 88.5,
                                           'v_string15': 88.9,
                                           'v_string16': 88.9,
                                           'v_string17': 4.6,
                                           'v_string18': 4.6,
                                           'v_string19': 2.5,
                                           'v_string2': 88.7,
                                           'v_string20': 2.5,
                                           'v_string3': 87.8,
                                           'v_string4': 87.8,
                                           'v_string5': 89.3,
                                           'v_string6': 89.3,
                                           'v_string7': 86.2,
                                           'v_string8': 86.2,
                                           'v_string9': 89.0,
                                           'vac': 1.4,
                                           'vac1': 1.4,
                                           'vac2': 0.9,
                                           'vac3': 1.7,
                                           'vac_rs': 1.4,
                                           'vac_rs1': 0.0,
                                           'vac_st': 1.3,
                                           'vac_st1': 0.0,
                                           'vac_tr': 1.2,
                                           'vac_tr1': 0.0,
                                           'vacs': 0.9,
                                           'vact': 1.7,
                                           'vbat': 48.0,
                                           'vbat2': 0.0,
                                           'vbat3': 0.0,
                                           'vpp_work_status': 0,
                                           'vpv1': 88.7,
                                           'vpv10': 2.5,
                                           'vpv2': 87.8,
                                           'vpv3': 89.3,
                                           'vpv4': 86.2,
                                           'vpv5': 89.0,
                                           'vpv6': 89.1,
                                           'vpv7': 88.5,
                                           'vpv8': 88.9,
                                           'vpv9': 4.6,
                                           'warn_code': 400,
                                           'warn_code1': 25,
                                           'warn_text': 'Unknown',
                                           'warning_value1': 0,
                                           'warning_value2': 0,
                                           'warning_value3': 0,
                                           'wit_bean': None,
                                           'with_time': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy(device_sn=self._device_sn(device_sn), device_type=DeviceType.WIT)

    def energy_history_v4(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
    ) -> WitEnergyHistoryV4:
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
            WitEnergyHistoryV4
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
            device_sn=self._device_sn(device_sn), device_type=DeviceType.WIT, date_=date_
        )

    def energy_history_multiple_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        date_: Optional[date] = None,
    ) -> WitEnergyHistoryMultipleV4:
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
            WitEnergyHistoryMultipleV4
            e.g.
            {   'data': {   'NHB691514F': [   {
                                                  <see energy_v4() for attributes>
                                              }]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

        """

        return self._api_v4.energy_history_multiple(
            device_sn=self._device_sn(device_sn), device_type=DeviceType.WIT, date_=date_
        )

    def setting_read_vpp_param(
        self,
        parameter_id: str,
        device_sn: Optional[str] = None,
    ) -> SettingReadVppV4:
        """
        Read VPP parameters using "new-api" endpoint
        Read the VPP related parameters of the device according to the SN of the device.
        https://www.showdoc.com.cn/2598832417617967/11558629942271434

        Note:
        * The current interface only supports
          * WIT 100KTL3-H
          * WIS 215KTL3

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Allowed/known values for vpp_param:
          see self.setting_write_vpp_param()

        Args:
            device_sn (str): Inverter serial number
            parameter_id (str): Set parameter enumeration, example: set_param_1

        Returns:
            SettingReadVppV4
            e.g.
            {   'data': 0,
                'error_code': 0,
                'error_msg': 'success'}

        """

        return self._api_v4.setting_read_vpp_param(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.WIT,
            parameter_id=parameter_id,
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
            device_type=DeviceType.WIT,
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
            device_type=DeviceType.WIT,
            active_power=active_power_percent,
        )

    def setting_write_vpp_param(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        parameter_id: str,
        value: Union[int, str],
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set VPP parameters using "new-api" endpoint
        Set the VPP related parameters of the device according to the SN of the device.
        https://www.showdoc.com.cn/2598832417617967/11558385202215329

        Note:
        * The current interface only supports
          * WIT 100KTL3-H
          * WIS 215KTL3

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Allowed/known values for vpp_param:
        ========================+===============+===========================+============================================================================
        description             | parameter_id  | parameter_value           | comment
        ========================+===============+===========================+============================================================================
        Control authority       | set_param_1   | 0 ~ 1                     | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        On off command          | set_param_2   | 0 ~ 1                     | Not storage
                                |               |                           | 0 = power off
                                |               |                           | 1 = power on (default)
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        System time             | set_param_3   | yyyy-mm-dd HH:MM:SS       | Example: 2024-10-10 13:14:14
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        SYN enable              | set_param_4   | 0 ~ 1                     | Offline box enable
                                |               |                           | 0: not enabled (default)
                                |               |                           | 1: enable
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Active power            | set_param_5   | 0 ~ 100                   | Power limit percentage
         percentage derating    |               |                           | default value = 100
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Static active power     | set_param_6   | 0 ~ 100                   | Power limit percent
                                |               |                           | Actual active power is the less one between Active power percentage derating
                                |               |                           |  and Static active power limitation - Not storage
                                |               |                           | default value = 100
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EPS offline enable      | set_param_7   | 0 ~ 1                     | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EPS offline frequency   | set_param_8   | 0 ~ 1                     | 0 = 50 Hz (default)
                                |               |                           | 1 = 60 Hz
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EPS offline voltage(3)  | set_param_9   | 0 ~ 6                     | 0 = 230 V (default)
                                |               |                           | 1 = 208V
                                |               |                           | 2 = 240V
                                |               |                           | 3 = 220V
                                |               |                           | 4 = 127V
                                |               |                           | 5 = 277V
                                |               |                           | 6 = 254V
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Fix Q                   | set_param_10  | 0 ~ 60                    | Power limit percentage
                                |               |                           | default value = 60
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Reactive power mode     | set_param_11  | 0 ~ 5                     | 0: PF=1 (default)
                                |               |                           | 1: Pf value setting
                                |               |                           | 2: Default pf curve(reserve)
                                |               |                           | 3: User set pf curve(reserve)
                                |               |                           | 4: Lagging reactive power (+)
                                |               |                           | 5: Leading reactive power (-)
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Power factor            | set_param_12  | 0 ~ 20000                 | Actual power factor = (10000 - set_value) * 0.0001
                                |               |                           | default value = 10000
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Dynamic export          | set_param_13  | 0 ~ 1                     | 0 = disabled (default)
         limitation             |               |                           | 1 = single machine anti-back flow enable
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Export limitation power | set_param_14  | -100 ~ 100                | Positive value is backflow, negative value is fair current
                                |               |                           | default value = 0
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Failure value of        | set_param_15  | 0 ~ 100                   | When the communication with meter failed (30204 is 1), use this register
         anti-backflow limiting |               |                           |  to limit reactive power，for backflow control
         power                  |               |                           | default value = 0
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-back flow fail     | set_param_16  | 0 ~ 300                   | default value = 30
         time/EMS communicating |               |                           |
         fail time              |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EMS communicating fail  | set_param_17  | 0 ~ 1                     | 0 = disabled (default)
         enable                 |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Super anti-backflow     | set_param_18  | 0 ~ 1                     | 0 = disabled (default)
         enable                 |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow feed      | set_param_19  | 0 ~ 20000                 | default value = 27
         power change slope     |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow single    | set_param_20  | 0 ~ 1                     | 0 = disabled (default)
         phase ctrl enable      |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow           | set_param_21  | 0 ~ 1                     | 0 = Default mode (default)
         protection mode（1）    |               |                           | 1 = software and hardware control mode
                                |               |                           | 2 = software control mode
                                |               |                           | 3 = hardware control mode
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Charging cut off SOC    | set_param_22  | 70 ~ 100                  | default value = 100
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Online discharge cut    | set_param_23  | 10 ~ 30                   | default value = 10
         off SOC                |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Load priority discharge | set_param_24  | 10 ~ 20                   | default value = 10
         cut off SOC (2)        |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Remote power control    | set_param_25  | 0 ~ 1                     | Not storage
         enable                 |               |                           | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Remote power control    | set_param_26  | 0 ~ 1440                  | Not storage
         charging time          |               |                           | 0: unlimited time (default)
                                |               |                           | 1 ~ 1440 min: control the power duration according to the set time
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Remote charge and       | set_param_27  | -100 ~ 100                | Not storage
         discharge power        |               |                           | negative value = discharge, positive value = charge
                                |               |                           | default value = 0
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        AC charging enable      | set_param_28  | 0 ~ 1                     | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Offline discharge cut   | set_param_29  | 10 ~ 30                   | default value = 10
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery charge stop     | set_param_30  | 0 ~ 15000                 | Lead-acid battery used - Distinguished by voltage level
         voltage                |               |                           |  3800 = 127 V
                                |               |                           | 10000 = 227 V
                                |               |                           |  8000 = Others
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery discharge stop  | set_param_31  | 0 ~ 15000                 | Lead-acid battery used - Distinguished by voltage level
         voltage                |               |                           | 3800 = 127 V
                                |               |                           | 7500 = 227 V
                                |               |                           | 6500 = Others
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery max charge      | set_param_32  | 0 ~ 2000                  | Lead-acid battery used
         current                |               |                           | default value = 1500
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery max discharge   | set_param_33  | 0 ~ 2000                  | Lead-acid battery used
         current                |               |                           | default value = 1500
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Charging and discharging| set_param_34  | 0 ~ 2000                  | Set time period (json format: [{percentage: power, startTime: start time, endTime: end time}]
         in different periods   |               |                           | time range: 0-1440
          (20 sections)         |               |                           | e.g.: [{"percentage":95,"startTime":0,"endTime":300},{"percentage":-60,"startTime":301,"endTime":720}]
        ========================+===============+===========================+============================================================================
        see https://www.showdoc.com.cn/2598832417617967/11558385130027995 or https://www.showdoc.com.cn/p/fc84c86facd79b3692f585fbd7a6e33b
        ========================+===============+===========================+============================================================================


        Args:
            device_sn (str): Inverter serial number
            parameter_id (str): Set parameter enumeration, example: set_param_1
            value (Union[int, str]): the parameter value set, example:value


        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_vpp_param(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.WIT,
            parameter_id=parameter_id,
            value=value,
        )
