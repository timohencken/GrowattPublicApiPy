import datetime
from typing import Optional, Literal, List, Union
from loguru import logger
from ..growatt_types import DeviceType
from ..pydantic_models.api_v4 import (
    InverterDetailsV4,
    StorageDetailsV4,
    SphDetailsV4,
    SpaDetailsV4,
    MinDetailsV4,
    WitDetailsV4,
    SphsDetailsV4,
    NoahDetailsV4,
    MaxDetailsV4,
    InverterEnergyV4,
    StorageEnergyV4,
    MaxEnergyV4,
    SphEnergyV4,
    SpaEnergyV4,
    MinEnergyV4,
    WitEnergyV4,
    NoahEnergyV4,
    SphsEnergyV4,
    InverterEnergyHistoryV4,
    InverterEnergyHistoryMultipleV4,
    StorageEnergyHistoryV4,
    SphEnergyHistoryV4,
    MaxEnergyHistoryV4,
    SpaEnergyHistoryV4,
    MinEnergyHistoryV4,
    WitEnergyHistoryV4,
    SphsEnergyHistoryV4,
    NoahEnergyHistoryV4,
    StorageEnergyHistoryMultipleV4,
    SphEnergyHistoryMultipleV4,
    MaxEnergyHistoryMultipleV4,
    SpaEnergyHistoryMultipleV4,
    MinEnergyHistoryMultipleV4,
    WitEnergyHistoryMultipleV4,
    SphsEnergyHistoryMultipleV4,
    NoahEnergyHistoryMultipleV4,
    SettingWriteV4,
    SettingReadVppV4,
)
from ..session.growatt_api_session import GrowattApiSession


DeviceTypeStr = Literal["inv", "storage", "max", "sph", "spa", "min", "wit", "sph-s", "noah"]


class ApiV4:
    """
    New API (v4)
    https://www.showdoc.com.cn/2540838290984246/11292912972201443

    v4 error codes
    https://www.showdoc.com.cn/2540838290984246/11292913883034530

    Do not use this module directly, use the device-specific implementation instead.
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    @staticmethod
    def _device_type(device_type: Union[DeviceType, DeviceTypeStr]) -> DeviceType:
        if isinstance(device_type, DeviceType):
            return device_type

        try:
            return DeviceType(device_type)
        except ValueError:
            raise ValueError(
                f"device type '{device_type}' cannot be mapped to any known device type ({', '.join([x.name for x in DeviceType])})"
            )

    def details(  # noqa: C901 'ApiV4.details' is too complex (11)
        self,
        device_sn: Union[str, List[str]],
        device_type: Union[DeviceType, DeviceTypeStr],
    ) -> Union[
        InverterDetailsV4,
        StorageDetailsV4,
        MaxDetailsV4,
        SphDetailsV4,
        SpaDetailsV4,
        MinDetailsV4,
        WitDetailsV4,
        SphsDetailsV4,
        NoahDetailsV4,
    ]:
        """
        Batch device information
        Retrieve basic information of devices in bulk based on device type and device SN.
        The data returned by the interface will only include devices that the key token has permission to access.
        Information about devices without permission will not be returned.
        https://www.showdoc.com.cn/2540838290984246/11292915673945114

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list())

        Returns:
            Union[InverterDetailsV4, StorageDetailsV4, MaxDetailsV4, SphDetailsV4, SpaDetailsV4, MinDetailsV4, WitDetailsV4, SphsDetailsV4, NoahDetailsV4]

            InverterDetailsV4:
            {   'data': {   'inv': [   {   'address': 1,
                                           'alias': 'HPB3744071',
                                           'big_device': False,
                                           'children': None,
                                           'communication_version': None,
                                           'create_date': None,
                                           'datalogger_sn': 'JPC2101182',
                                           'device_type': 0,
                                           'e_today': 0.0,
                                           'e_total': 0.0,
                                           'energy_day': 0.0,
                                           'energy_day_map': {},
                                           'energy_month': 0.0,
                                           'energy_month_text': '0',
                                           'fw_version': 'AH1.0',
                                           'group_id': 0,
                                           'id': 7,
                                           'img_path': './css/img/status_gray.gif',
                                           'inner_version': 'ahbb1916',
                                           'inv_set_bean': None,
                                           'inverter_info_status_css': 'vsts_table_ash',
                                           'ipm_temperature': 0.0,
                                           'last_update_time': 1613805596000,
                                           'last_update_time_text': datetime.datetime(2021, 2, 20, 15, 19, 56),
                                           'level': 4,
                                           'load_text': '0%',
                                           'location': '在这',
                                           'lost': True,
                                           'model': 269545841,
                                           'model_text': 'A1B0D1T0PFU1M7S1',
                                           'nominal_power': 6000,
                                           'optimizer_list': None,
                                           'parent_id': 'LIST_JPC2101182_0',
                                           'plant_id': 0,
                                           'plant_name': None,
                                           'power': 0.0,
                                           'power_max': None,
                                           'power_max_text': None,
                                           'power_max_time': None,
                                           'record': None,
                                           'rf_stick': None,
                                           'serial_num': 'HPB3744071',
                                           'status': -1,
                                           'status_text': 'inverter.status.lost',
                                           'tcp_server_ip': '192.168.3.35',
                                           'temperature': 0.0,
                                           'tree_id': 'HPB3744071',
                                           'tree_name': 'HPB3744071',
                                           'update_exist': False,
                                           'updating': False,
                                           'user_id': 0,
                                           'user_name': None}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            StorageDetailsV4:
            {   'data': {   'storage': [   {   'ac_in_model': 1.0,
                                               'ac_max_charge_curr': 60.0,
                                               'address': 0,
                                               'alias': None,
                                               'b_light_en': 1,
                                               'bat_low_to_uti_volt': 46.0,
                                               'battery_type': 0,
                                               'battery_undervoltage_cutoff_point': 42.0,
                                               'bulk_charge_volt': 56.4,
                                               'buzzer_en': 1,
                                               'charge_config': 1,
                                               'children': None,
                                               'communication_version': None,
                                               'datalogger_sn': 'EAP0D9M006',
                                               'device_type': 6,
                                               'dtc': 20806,
                                               'float_charge_volt': 54.0,
                                               'fw_version': '141.00/142.00',
                                               'group_id': -1,
                                               'img_path': './css/img/status_gray.gif',
                                               'inner_version': 'null',
                                               'last_update_time': 1718612986000,
                                               'last_update_time_text': datetime.datetime(2024, 6, 17, 16, 29, 46),
                                               'level': 4,
                                               'li_battery_protocol_type': 1,
                                               'location': None,
                                               'lost': True,
                                               'mains_to_battery_operat_point': 54.0,
                                               'manual_start_en': 0.0,
                                               'max_charge_curr': 0.0,
                                               'model': 120,
                                               'model_text': 'A0B0D0T0P0U0M7S8',
                                               'output_config': 3.0,
                                               'output_freq_type': 0,
                                               'output_volt_type': 1,
                                               'over_load_restart': 1.0,
                                               'over_temp_restart': 1.0,
                                               'p_charge': 0.0,
                                               'p_discharge': 0.0,
                                               'parent_id': 'LIST_EAP0D9M006_96',
                                               'plant_id': 0,
                                               'plant_name': None,
                                               'port_name': None,
                                               'pow_saving_en': 0,
                                               'pv_model': 0,
                                               'rate_va': 12000.0,
                                               'rate_watt': 12000.0,
                                               'record': None,
                                               'sci_loss_chk_en': 0,
                                               'serial_num': 'KHMOCM5688',
                                               'status': -1,
                                               'status_led1': False,
                                               'status_led2': False,
                                               'status_led3': False,
                                               'status_led4': False,
                                               'status_led5': False,
                                               'status_led6': False,
                                               'status_text': 'inverter.status.lost',
                                               'sys_time': datetime.datetime(2024, 6, 17, 16, 17),
                                               'tcp_server_ip': '127.0.0.1',
                                               'timezone': 8.0,
                                               'tree_id': 'ST_KHMOCM5688',
                                               'tree_name': None,
                                               'updating': False,
                                               'user_name': None,
                                               'uti_charge_end': 0.0,
                                               'uti_charge_start': 0.0,
                                               'uti_out_end': 0.0,
                                               'uti_out_start': 0.0,
                                               'uw_bat_type2': 1,
                                               'uw_feed_en': 0,
                                               'uw_feed_range': 0.0,
                                               'uw_load_first': 0.0}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            MaxDetailsV4:
            {   'data': {   'max': [   {   'active_rate': 0.0,
                                           'address': 1,
                                           'alias': 'HPJ0BF20FU',
                                           'backflow_default_power': 0.0,
                                           'big_device': False,
                                           'children': None,
                                           'communication_version': 'ZBab-0002',
                                           'datalogger_sn': 'BLE4BEQ0BW',
                                           'device_type': 1,
                                           'dtc': 5001,
                                           'e_today': 0.0,
                                           'e_total': 0.0,
                                           'energy_day': 0.0,
                                           'energy_day_map': {},
                                           'energy_month': 0.0,
                                           'energy_month_text': '0',
                                           'export_limit': 0.0,
                                           'export_limit_power_rate': 0.0,
                                           'fac_high': 0.0,
                                           'fac_low': 0.0,
                                           'frequency_high_limit': 0.0,
                                           'frequency_low_limit': 0.0,
                                           'fw_version': 'TJ1.0',
                                           'group_id': -1,
                                           'id': 0,
                                           'img_path': './css/img/status_gray.gif',
                                           'inner_version': 'TJAA08020002',
                                           'last_update_time': 1716534733000,
                                           'last_update_time_text': datetime.datetime(2024, 5, 24, 15, 12, 13),
                                           'lcd_language': 0,
                                           'level': 6,
                                           'location': None,
                                           'lost': False,
                                           'max_set_bean': None,
                                           'model': 720575940631003386,
                                           'model_text': 'S0AB00D00T00P0FU01M00FA',
                                           'normal_power': 25000.0,
                                           'on_off': False,
                                           'parent_id': 'LIST_BLE4BEQ0BW_3',
                                           'pf': 0.0,
                                           'pf_model': 0,
                                           'pflinep1_lp': 0.0,
                                           'pflinep1_pf': 0.0,
                                           'pflinep2_lp': 0.0,
                                           'pflinep2_pf': 0.0,
                                           'pflinep3_lp': 0.0,
                                           'pflinep3_pf': 0.0,
                                           'pflinep4_lp': 0.0,
                                           'pflinep4_pf': 0.0,
                                           'plant_id': 0,
                                           'plant_name': None,
                                           'port_name': 'ShinePano - BLE4BEQ0BW',
                                           'power': 0.0,
                                           'power_max': None,
                                           'power_max_text': None,
                                           'power_max_time': None,
                                           'pv_pf_cmd_memory_state': 0,
                                           'reactive_rate': 0.0,
                                           'record': None,
                                           'serial_num': 'HPJ0BF20FU',
                                           'status': 1,
                                           'status_text': 'max.status.normal',
                                           'str_num': 0,
                                           'sys_time': None,
                                           'tcp_server_ip': '47.119.22.101',
                                           'timezone': 8.0,
                                           'tree_id': 'HPJ0BF20FU',
                                           'tree_name': 'HPJ0BF20FU',
                                           'updating': False,
                                           'user_name': None,
                                           'vac_high': 0.0,
                                           'vac_low': 0.0,
                                           'voltage_high_limit': 0.0,
                                           'voltage_low_limit': 0.0}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            SphDetailsV4:
            {   'data': {   'sph': [   {   'ac_charge_enable': False,
                                           'active_rate': 100,
                                           'address': 1,
                                           'alias': 'OZD0849010',
                                           'back_up_en': 0,
                                           'backflow_setting': None,
                                           'bat_aging_test_step': 0,
                                           'bat_first_switch1': 0,
                                           'bat_first_switch2': 0,
                                           'bat_first_switch3': 0,
                                           'bat_parallel_num': 0,
                                           'bat_series_num': 0,
                                           'bat_sys_rate_energy': -0.1,
                                           'bat_temp_lower_limit_c': 110.0,
                                           'bat_temp_lower_limit_d': 110.0,
                                           'bat_temp_upper_limit_c': 60.0,
                                           'bat_temp_upper_limit_d': 70.0,
                                           'battery_type': 0,
                                           'baudrate': 0,
                                           'bct_adjust': 0,
                                           'bct_mode': 0,
                                           'buck_ups_fun_en': False,
                                           'buck_ups_volt_set': 0.0,
                                           'cc_current': 0.0,
                                           'charge_power_command': 100,
                                           'charge_time1': None,
                                           'charge_time2': None,
                                           'charge_time3': None,
                                           'children': None,
                                           'com_address': 1,
                                           'communication_version': None,
                                           'country_selected': 0,
                                           'cv_voltage': 0.0,
                                           'datalogger_sn': 'JAD084800B',
                                           'device_type': 0,
                                           'discharge_power_command': 100,
                                           'discharge_time1': None,
                                           'discharge_time2': None,
                                           'discharge_time3': None,
                                           'dtc': 3501,
                                           'energy_day': 0.0,
                                           'energy_day_map': {},
                                           'energy_month': 0.0,
                                           'energy_month_text': '0',
                                           'eps_freq_set': 0,
                                           'eps_fun_en': True,
                                           'eps_volt_set': 0,
                                           'export_limit': 0,
                                           'export_limit_power_rate': 0.0,
                                           'failsafe': 0,
                                           'float_charge_current_limit': 660.0,
                                           'forced_charge_stop_switch1': True,
                                           'forced_charge_stop_switch2': False,
                                           'forced_charge_stop_switch3': False,
                                           'forced_charge_stop_switch4': False,
                                           'forced_charge_stop_switch5': False,
                                           'forced_charge_stop_switch6': False,
                                           'forced_charge_time_start1': datetime.time(0, 0),
                                           'forced_charge_time_start2': datetime.time(0, 0),
                                           'forced_charge_time_start3': datetime.time(0, 0),
                                           'forced_charge_time_start4': datetime.time(0, 0),
                                           'forced_charge_time_start5': datetime.time(0, 0),
                                           'forced_charge_time_start6': datetime.time(0, 0),
                                           'forced_charge_time_stop1': datetime.time(0, 0),
                                           'forced_charge_time_stop2': datetime.time(0, 0),
                                           'forced_charge_time_stop3': datetime.time(0, 0),
                                           'forced_charge_time_stop4': datetime.time(0, 0),
                                           'forced_charge_time_stop5': datetime.time(0, 0),
                                           'forced_charge_time_stop6': datetime.time(0, 0),
                                           'forced_discharge_stop_switch1': False,
                                           'forced_discharge_stop_switch2': False,
                                           'forced_discharge_stop_switch3': False,
                                           'forced_discharge_stop_switch4': False,
                                           'forced_discharge_stop_switch5': False,
                                           'forced_discharge_stop_switch6': False,
                                           'forced_discharge_time_start1': datetime.time(0, 0),
                                           'forced_discharge_time_start2': datetime.time(0, 0),
                                           'forced_discharge_time_start3': datetime.time(0, 0),
                                           'forced_discharge_time_start4': datetime.time(0, 0),
                                           'forced_discharge_time_start5': datetime.time(0, 0),
                                           'forced_discharge_time_start6': datetime.time(0, 0),
                                           'forced_discharge_time_stop1': datetime.time(0, 0),
                                           'forced_discharge_time_stop2': datetime.time(0, 0),
                                           'forced_discharge_time_stop3': datetime.time(0, 0),
                                           'forced_discharge_time_stop4': datetime.time(0, 0),
                                           'forced_discharge_time_stop5': datetime.time(0, 0),
                                           'forced_discharge_time_stop6': datetime.time(0, 0),
                                           'fw_version': 'RA1.0',
                                           'grid_first_switch1': False,
                                           'grid_first_switch2': False,
                                           'grid_first_switch3': False,
                                           'group_id': -1,
                                           'id': 0,
                                           'img_path': './css/img/status_green.gif',
                                           'in_power': 20.0,
                                           'inner_version': 'raab010101',
                                           'inv_version': 0,
                                           'last_update_time': 1716535653000,
                                           'last_update_time_text': datetime.datetime(2024, 5, 24, 15, 27, 33),
                                           'lcd_language': 1,
                                           'level': 4,
                                           'load_first_control': 0,
                                           'load_first_stop_soc_set': 0,
                                           'location': None,
                                           'lost': False,
                                           'lv_voltage': 0.0,
                                           'manufacturer': '   New Energy   ',
                                           'mc_version': 'null',
                                           'mix_ac_discharge_frequency': None,
                                           'mix_ac_discharge_voltage': None,
                                           'mix_off_grid_enable': None,
                                           'modbus_version': 305,
                                           'model': 1159635200000,
                                           'model_text': 'A0B0DBT0PFU2M4S0',
                                           'monitor_version': 'null',
                                           'new_sw_version_flag': 0,
                                           'off_grid_discharge_soc': -1,
                                           'old_error_flag': 0,
                                           'on_off': False,
                                           'out_power': 20.0,
                                           'p_charge': 0,
                                           'p_discharge': 0,
                                           'parent_id': 'LIST_JAD084800B_96',
                                           'pf_sys_year': None,
                                           'plant_id': 0,
                                           'plant_name': None,
                                           'pmax': 0,
                                           'port_name': 'ShinePano - JAD084800B',
                                           'power_factor': 0.0,
                                           'power_max': None,
                                           'power_max_text': None,
                                           'power_max_time': None,
                                           'priority_choose': 1,
                                           'pv_active_p_rate': None,
                                           'pv_grid_voltage_high': None,
                                           'pv_grid_voltage_low': None,
                                           'pv_on_off': None,
                                           'pv_pf_cmd_memory_state': None,
                                           'pv_pf_cmd_memory_state_mix': None,
                                           'pv_pf_cmd_memory_state_sph': False,
                                           'pv_power_factor': None,
                                           'pv_reactive_p_rate': None,
                                           'pv_reactive_p_rate_two': None,
                                           'reactive_delay': 150.0,
                                           'reactive_power_limit': 48.0,
                                           'reactive_rate': 100,
                                           'record': None,
                                           'region': -1,
                                           'safety': '00',
                                           'safety_num': '4E',
                                           'serial_num': 'OZD0849010',
                                           'sgip_en': False,
                                           'single_export': 0,
                                           'status': 5,
                                           'status_text': 'mix.status.normal',
                                           'sys_time': datetime.datetime(2024, 5, 24, 5, 20, 52),
                                           'sys_time_text': datetime.datetime(2024, 5, 24, 5, 20, 52),
                                           'tcp_server_ip': '47.119.173.58',
                                           'timezone': 8.0,
                                           'tree_id': 'ST_OZD0849010',
                                           'tree_name': 'OZD0849010',
                                           'under_excited': 0,
                                           'updating': False,
                                           'user_name': None,
                                           'usp_freq_set': 0,
                                           'uw_grid_watt_delay': 0.0,
                                           'uw_hf_rt2_ee': 0.0,
                                           'uw_hf_rt_ee': 0.0,
                                           'uw_hf_rt_time2_ee': 0.0,
                                           'uw_hf_rt_time_ee': 0.0,
                                           'uw_hv_rt2_ee': 0.0,
                                           'uw_hv_rt_ee': 0.0,
                                           'uw_hv_rt_time2_ee': 0.0,
                                           'uw_hv_rt_time_ee': 0.0,
                                           'uw_lf_rt2_ee': 0.0,
                                           'uw_lf_rt_ee': 0.0,
                                           'uw_lf_rt_time2_ee': 0.0,
                                           'uw_lf_rt_time_ee': 0.0,
                                           'uw_lv_rt2_ee': 0.0,
                                           'uw_lv_rt3_ee': 0.0,
                                           'uw_lv_rt_ee': 0.0,
                                           'uw_lv_rt_time2_ee': 0.0,
                                           'uw_lv_rt_time3_ee': 0.0,
                                           'uw_lv_rt_time_ee': 0.0,
                                           'uw_nominal_grid_volt': 0.0,
                                           'uw_reconnect_start_slope': 0.0,
                                           'v1': 122.0,
                                           'v2': 119.0,
                                           'v3': 146.0,
                                           'v4': 143.0,
                                           'vbat_start_for_charge': 54.4,
                                           'vbat_start_for_discharge': 44.0,
                                           'vbat_stop_for_charge': 5.75,
                                           'vbat_stop_for_discharge': 4.7,
                                           'vbat_warn_clr': 5.0,
                                           'vbat_warning': 440.0,
                                           'vnormal': 360.0,
                                           'voltage_high_limit': 263.0,
                                           'voltage_low_limit': 186.0,
                                           'vpp_open': 0.0,
                                           'wcharge_soc_low_limit1': 100,
                                           'wcharge_soc_low_limit2': 100,
                                           'wdis_charge_soc_low_limit1': 100,
                                           'wdis_charge_soc_low_limit2': 5}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            SpaDetailsV4:
            {   'data': {   'spa': [   {   'ac_charge_enable': False,
                                           'active_p_rate': 100,
                                           'address': 1,
                                           'alias': 'CHENYINSHU',
                                           'backflow_setting': None,
                                           'bat_aging_test_step': 0,
                                           'bat_first_switch1': 0,
                                           'bat_first_switch2': 0,
                                           'bat_first_switch3': 0,
                                           'bat_pack_num': 0,
                                           'bat_serial_num': None,
                                           'bat_sys_rate_energy': 0.0,
                                           'bat_temp_lower_limit_c': 101.0,
                                           'bat_temp_lower_limit_d': 110.0,
                                           'bat_temp_upper_limit_c': 60.0,
                                           'bat_temp_upper_limit_d': 70.0,
                                           'battery_type': 1,
                                           'baudrate': 0,
                                           'bct_adjust': 0,
                                           'bct_mode': 0,
                                           'buck_ups_fun_en': True,
                                           'buck_ups_volt_set': 0.0,
                                           'charge_power_command': 100,
                                           'charge_time1': None,
                                           'charge_time2': None,
                                           'charge_time3': None,
                                           'children': None,
                                           'com_address': 1,
                                           'communication_version': None,
                                           'country_selected': 0,
                                           'datalogger_sn': 'BQC0733006',
                                           'device_type': 0,
                                           'discharge_power_command': 100,
                                           'discharge_time1': None,
                                           'discharge_time2': None,
                                           'discharge_time3': None,
                                           'dtc': 3701,
                                           'energy_day': 0.0,
                                           'energy_day_map': {},
                                           'energy_month': 0.0,
                                           'energy_month_text': '0',
                                           'eps_freq_set': 0,
                                           'eps_fun_en': False,
                                           'eps_volt_set': 0,
                                           'equipment_type': None,
                                           'export_limit': 0.0,
                                           'export_limit_power_rate': 0.0,
                                           'failsafe': 0,
                                           'float_charge_current_limit': 450.0,
                                           'forced_charge_stop_switch4': False,
                                           'forced_charge_stop_switch5': False,
                                           'forced_charge_stop_switch6': False,
                                           'forced_charge_time_start1': datetime.time(0, 0),
                                           'forced_charge_time_start2': datetime.time(0, 0),
                                           'forced_charge_time_start3': datetime.time(0, 0),
                                           'forced_charge_time_start4': None,
                                           'forced_charge_time_start5': None,
                                           'forced_charge_time_start6': None,
                                           'forced_charge_time_stop1': datetime.time(23, 59),
                                           'forced_charge_time_stop2': datetime.time(0, 0),
                                           'forced_charge_time_stop3': datetime.time(0, 0),
                                           'forced_charge_time_stop4': None,
                                           'forced_charge_time_stop5': None,
                                           'forced_charge_time_stop6': None,
                                           'forced_discharge_stop_switch4': False,
                                           'forced_discharge_stop_switch5': False,
                                           'forced_discharge_stop_switch6': False,
                                           'forced_discharge_time_start1': datetime.time(0, 0),
                                           'forced_discharge_time_start2': datetime.time(0, 0),
                                           'forced_discharge_time_start3': datetime.time(0, 0),
                                           'forced_discharge_time_start4': None,
                                           'forced_discharge_time_start5': None,
                                           'forced_discharge_time_start6': None,
                                           'forced_discharge_time_stop1': datetime.time(23, 59),
                                           'forced_discharge_time_stop2': datetime.time(0, 0),
                                           'forced_discharge_time_stop3': datetime.time(0, 0),
                                           'forced_discharge_time_stop4': None,
                                           'forced_discharge_time_stop5': None,
                                           'forced_discharge_time_stop6': None,
                                           'fw_version': 'RH1.0',
                                           'grid_first_switch1': True,
                                           'grid_first_switch2': False,
                                           'grid_first_switch3': False,
                                           'group_id': -1,
                                           'id': 0,
                                           'img_path': './css/img/status_gray.gif',
                                           'inner_version': 'rHBA020202',
                                           'inv_version': 0,
                                           'last_update_time': 1558437021000,
                                           'last_update_time_text': datetime.datetime(2019, 5, 21, 19, 10, 21),
                                           'lcd_language': 1,
                                           'level': 4,
                                           'load_first_start_time1': datetime.time(0, 40),
                                           'load_first_start_time2': datetime.time(0, 0),
                                           'load_first_start_time3': datetime.time(0, 30),
                                           'load_first_stop_time1': datetime.time(0, 49),
                                           'load_first_stop_time2': datetime.time(0, 9),
                                           'load_first_stop_time3': datetime.time(0, 39),
                                           'load_first_switch1': False,
                                           'load_first_switch2': False,
                                           'load_first_switch3': False,
                                           'location': None,
                                           'lost': True,
                                           'manufacturer': '   New Energy   ',
                                           'mc_version': None,
                                           'modbus_version': 305,
                                           'model': 1814994400000,
                                           'model_text': 'A0B1D1T4PFU2M3S8',
                                           'monitor_version': None,
                                           'new_sw_version_flag': 0,
                                           'off_grid_discharge_soc': 0.0,
                                           'old_error_flag': 0,
                                           'on_off': True,
                                           'p_charge': 0.0,
                                           'p_discharge': 0.0,
                                           'parent_id': 'LIST_BQC0733006_96',
                                           'pf_cmd_memory_state': 0,
                                           'pf_sys_year': None,
                                           'plant_id': 0,
                                           'plant_name': None,
                                           'pmax': 3680,
                                           'port_name': 'ShinePano - BQC0733006',
                                           'power_factor': 20000.0,
                                           'power_max': None,
                                           'power_max_text': None,
                                           'power_max_time': None,
                                           'priority_choose': 2,
                                           'pro_pto': 0.0,
                                           'pv_active_p_rate': None,
                                           'pv_grid_voltage_high': None,
                                           'pv_grid_voltage_low': None,
                                           'pv_on_off': None,
                                           'pv_pf_cmd_memory_state': None,
                                           'pv_power_factor': None,
                                           'pv_reactive_p_rate': None,
                                           'pv_reactive_p_rate_two': None,
                                           'reactive_p_rate': 100,
                                           'record': None,
                                           'region': 0,
                                           'safety_correspond_num': 0,
                                           'safety_version': 0,
                                           'serial_num': 'CHENYINSHU',
                                           'spa_ac_discharge_frequency': None,
                                           'spa_ac_discharge_voltage': None,
                                           'spa_off_grid_enable': None,
                                           'status': -1,
                                           'status_text': 'spa.status.lost',
                                           'sys_time': datetime.datetime(2019, 5, 21, 16, 19),
                                           'sys_time_text': datetime.datetime(2019, 5, 21, 16, 19, 22),
                                           'tcp_server_ip': '192.168.3.35',
                                           'timezone': 8.0,
                                           'tree_id': 'ST_CHENYINSHU',
                                           'tree_name': 'CHENYINSHU',
                                           'under_excited': 0,
                                           'updating': False,
                                           'ups_freq_set': 0.0,
                                           'user_name': None,
                                           'vac_high': 262.2,
                                           'vac_low': 184.0,
                                           'vbat_start_for_charge': 57.6,
                                           'vbat_start_for_discharge': 44.0,
                                           'vbat_stop_for_charge': 5.75,
                                           'vbat_stop_for_discharge': 4.7,
                                           'vbat_warn_clr': 5.0,
                                           'vbat_warning': 440.0,
                                           'vpp_open': 0.0,
                                           'w_charge_soc_low_limit1': 100,
                                           'w_charge_soc_low_limit2': 100,
                                           'w_discharge_soc_low_limit1': 100,
                                           'w_discharge_soc_low_limit2': 10,
                                           'w_load_soc_low_limit1': 0,
                                           'w_load_soc_low_limit2': 0}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            MinDetailsV4:
            {   'data': {   'min': [   {   'address': 1,
                                           'alias': 'BZP3N6U09K',
                                           'bat_aging_test_step': 0,
                                           'bat_parallel_num': 0,
                                           'bat_series_num': 0,
                                           'bat_sys_energy': 0.0,
                                           'bat_temp_lower_limit_c': 0.0,
                                           'bat_temp_lower_limit_d': 0.0,
                                           'bat_temp_upper_limit_c': 0.0,
                                           'bat_temp_upper_limit_d': 0.0,
                                           'battery_type': 0,
                                           'baudrate': 0,
                                           'bct_adjust': 0,
                                           'bct_mode': 0,
                                           'bcu_version': None,
                                           'bdc1_model': '0',
                                           'bdc1_sn': None,
                                           'bdc1_version': '\x00\x00\x00\x00-0',
                                           'bdc_auth_version': 0,
                                           'bdc_mode': 0,
                                           'bms_communication_type': 0,
                                           'bms_software_version': None,
                                           'children': None,
                                           'com_address': 1,
                                           'communication_version': 'GJAA-0004',
                                           'country_selected': 1,
                                           'datalogger_sn': 'QMN000BZP3N6U09K',
                                           'device_type': 5,
                                           'dtc': 5203,
                                           'e_today': 0.0,
                                           'e_total': 0.0,
                                           'energy_day_map': {},
                                           'energy_month': 0.0,
                                           'energy_month_text': '0',
                                           'fw_version': 'GJ1.0',
                                           'group_id': -1,
                                           'hw_version': '0',
                                           'id': 1404608,
                                           'img_path': './css/img/status_gray.gif',
                                           'inner_version': 'GJAA04xx',
                                           'last_update_time': 1742876493000,
                                           'last_update_time_text': datetime.datetime(2025, 3, 25, 12, 21, 33),
                                           'level': 4,
                                           'li_battery_fw_version': None,
                                           'li_battery_manufacturers': None,
                                           'location': None,
                                           'lost': False,
                                           'manufacturer': '   PV Inverter  ',
                                           'modbus_version': 0,
                                           'model': 504403158517219338,
                                           'model_text': 'S07B00D00T00P0FU01M000A',
                                           'monitor_version': None,
                                           'mppt': 513.0,
                                           'optimizer_list': None,
                                           'p_charge': 0.0,
                                           'p_discharge': 0.0,
                                           'parent_id': 'LIST_QMN000BZP3N6U09K_22',
                                           'plant_id': 0,
                                           'plantname': None,
                                           'pmax': 1000,
                                           'port_name': 'ShinePano-QMN000BZP3N6U09K',
                                           'power': 0.0,
                                           'power_max': None,
                                           'power_max_text': None,
                                           'power_max_time': None,
                                           'priority_choose': 0,
                                           'pv_num': 0,
                                           'record': None,
                                           'restart_time': 65,
                                           'safety_version': 0,
                                           'serial_num': 'BZP3N6U09K',
                                           'start_time': 65,
                                           'status': 1,
                                           'status_text': 'tlx.status.checking',
                                           'str_num': -1,
                                           'sys_time': None,
                                           'tcp_server_ip': '47.254.132.50',
                                           'timezone': 1.0,
                                           'tlx_set_bean': None,
                                           'tracker_model': 0,
                                           'tree_id': 'ST_BZP3N6U09K',
                                           'tree_name': 'BZP3N6U09K',
                                           'updating': False,
                                           'user_name': None,
                                           'vbat_start_for_discharge': 0.0,
                                           'vbat_stop_for_charge': 0.0,
                                           'vbat_stop_for_discharge': 0.0,
                                           'vbat_warn_clr': 0.0,
                                           'vbat_warning': 0.0,
                                           'vnormal': 280.0,
                                           'vpp_open': 0.0}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            WitDetailsV4:
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

            SphsDetailsV4:
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

            NoahDetailsV4:
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

        device_type = self._device_type(device_type=device_type)

        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="new-api/queryDeviceInfo",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
            },
        )

        if device_type == DeviceType.INVERTER:
            return InverterDetailsV4.model_validate(response)
        elif device_type == DeviceType.STORAGE:
            return StorageDetailsV4.model_validate(response)
        elif device_type == DeviceType.MAX:
            return MaxDetailsV4.model_validate(response)
        elif device_type == DeviceType.SPH:
            return SphDetailsV4.model_validate(response)
        elif device_type == DeviceType.SPA:
            return SpaDetailsV4.model_validate(response)
        elif device_type == DeviceType.MIN:
            return MinDetailsV4.model_validate(response)
        elif device_type == DeviceType.WIT:
            return WitDetailsV4.model_validate(response)
        elif device_type == DeviceType.SPHS:
            return SphsDetailsV4.model_validate(response)
        elif device_type == DeviceType.NOAH:
            return NoahDetailsV4.model_validate(response)
        else:
            raise ValueError(f"Unknown device type: {device_type}")

    def energy(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: Union[str, List[str]],
        device_type: Union[DeviceType, DeviceTypeStr],
    ) -> Union[
        InverterEnergyV4,
        StorageEnergyV4,
        MaxEnergyV4,
        SphEnergyV4,
        SpaEnergyV4,
        MinEnergyV4,
        WitEnergyV4,
        SphsEnergyV4,
        NoahEnergyV4,
    ]:
        """
        Batch equipment data information
        Retrieve the last detailed data for multiple devices based on their SN and device type.
        The interface returns data only for devices that the secret token has permission to access.
        Information for devices without permission will not be returned.
        https://www.showdoc.com.cn/2540838290984246/11292915898375566

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.
        * NOAH devices have a frequency of once every minute.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list())

        Returns:
            Union[InverterEnergyV4, StorageEnergyV4, MaxEnergyV4, SphEnergyV4, SpaEnergyV4, MinEnergyV4, WitEnergyV4, SphsEnergyV4, NoahEnergyV4,]

            InverterEnergyV4
            {   'data': {   'inv': [   {   'again': False,
                                           'big_device': False,
                                           'current_string1': 0.0,
                                           'current_string2': 0.0,
                                           'current_string3': 0.0,
                                           'current_string4': 0.0,
                                           'current_string5': 0.0,
                                           'current_string6': 0.0,
                                           'current_string7': 0.0,
                                           'current_string8': 0.0,
                                           'device_sn': 'NHB691514F',
                                           'dw_string_warning_value1': 0,
                                           'e_rac_today': 0.0,
                                           'e_rac_total': 308.0,
                                           'epv1_today': 0.0,
                                           'epv1_total': 120.8,
                                           'epv2_today': 0.0,
                                           'epv2_total': 0.0,
                                           'epv_total': 120.8,
                                           'fac': 0.0,
                                           'fault_type': 30,
                                           'i_pid_pvape': 0.0,
                                           'i_pid_pvbpe': 0.0,
                                           'iacr': 0.0,
                                           'iacs': 0.0,
                                           'iact': 0.0,
                                           'id': 0,
                                           'ipm_temperature': 28.7,
                                           'ipv1': 0.0,
                                           'ipv2': 0.0,
                                           'ipv3': 0.0,
                                           'n_bus_voltage': 149.2,
                                           'op_fullwatt': 0.0,
                                           'p_bus_voltage': 151.2,
                                           'pac': 0.0,
                                           'pacr': 0.0,
                                           'pacs': 0.0,
                                           'pact': 0.0,
                                           'pf': 1.0,
                                           'pid_status': 0,
                                           'power_today': 0.0,
                                           'power_total': 115.7,
                                           'ppv': 0.0,
                                           'ppv1': 0.0,
                                           'ppv2': 0.0,
                                           'ppv3': 0.0,
                                           'rac': 0.0,
                                           'real_op_percent': 0.0,
                                           'status': 3,
                                           'status_text': 'Fault',
                                           'str_fault': 0.0,
                                           'temperature': 27.9,
                                           'time': datetime.datetime(2024, 11, 13, 11, 4, 59),
                                           'time_calendar': 1731467099997,
                                           'time_total': 244.66666666666666,
                                           'time_total_text': '244.7',
                                           'v_pid_pvape': 0.0,
                                           'v_pid_pvbpe': 0.0,
                                           'v_string1': 0.0,
                                           'v_string2': 0.0,
                                           'v_string3': 0.0,
                                           'v_string4': 0.0,
                                           'v_string5': 0.0,
                                           'v_string6': 0.0,
                                           'v_string7': 0.0,
                                           'v_string8': 0.0,
                                           'vacr': 2.0,
                                           'vacs': 3.5,
                                           'vact': 1.4,
                                           'vpv1': 299.5,
                                           'vpv2': 21.6,
                                           'vpv3': 0.0,
                                           'w_pid_fault_value': 0,
                                           'w_string_status_value': 0,
                                           'warn_code': 0,
                                           'warning_value1': 0,
                                           'warning_value2': 0}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            StorageEnergyV4
            {   'data': {   'storage': [   {   'address': 0,
                                               'again': False,
                                               'alias': None,
                                               'b_light_en': 0.0,
                                               'bat_depower_reason': 0,
                                               'bat_protect1': 0,
                                               'bat_protect2': 0,
                                               'bat_protect3': 0,
                                               'bat_serial_num_id': 0,
                                               'bat_serial_number': None,
                                               'bat_temp': 0.0,
                                               'bat_warn_info1': 0,
                                               'bat_warn_info2': 0,
                                               'bms_battery_curr': 0.0,
                                               'bms_battery_temp': 0.0,
                                               'bms_battery_volt': 0.0,
                                               'bms_c_volt': 0.0,
                                               'bms_cell_volt1': 0.0,
                                               'bms_cell_volt10': 0.0,
                                               'bms_cell_volt11': 0.0,
                                               'bms_cell_volt12': 0.0,
                                               'bms_cell_volt13': 0.0,
                                               'bms_cell_volt14': 0.0,
                                               'bms_cell_volt15': 0.0,
                                               'bms_cell_volt16': 0.0,
                                               'bms_cell_volt2': 0.0,
                                               'bms_cell_volt3': 0.0,
                                               'bms_cell_volt4': 0.0,
                                               'bms_cell_volt5': 0.0,
                                               'bms_cell_volt6': 0.0,
                                               'bms_cell_volt7': 0.0,
                                               'bms_cell_volt8': 0.0,
                                               'bms_cell_volt9': 0.0,
                                               'bms_cell_voltage1': 0.0,
                                               'bms_cell_voltage10': 0.0,
                                               'bms_cell_voltage11': 0.0,
                                               'bms_cell_voltage12': 0.0,
                                               'bms_cell_voltage13': 0.0,
                                               'bms_cell_voltage14': 0.0,
                                               'bms_cell_voltage15': 0.0,
                                               'bms_cell_voltage16': 0.0,
                                               'bms_cell_voltage2': 0.0,
                                               'bms_cell_voltage3': 0.0,
                                               'bms_cell_voltage4': 0.0,
                                               'bms_cell_voltage5': 0.0,
                                               'bms_cell_voltage6': 0.0,
                                               'bms_cell_voltage7': 0.0,
                                               'bms_cell_voltage8': 0.0,
                                               'bms_cell_voltage9': 0.0,
                                               'bms_constant_volt': 0.0,
                                               'bms_current': 0.0,
                                               'bms_current2': 0.0,
                                               'bms_delta_volt': 0.0,
                                               'bms_error': 0,
                                               'bms_error2': 0,
                                               'bms_info': 0,
                                               'bms_max_current_charge': 0.0,
                                               'bms_pack_info': 0,
                                               'bms_soc': 0.0,
                                               'bms_soh': 0.0,
                                               'bms_status': 0,
                                               'bms_status2': 0,
                                               'bms_temperature': 0.0,
                                               'bms_temperature2': 0.0,
                                               'bms_using_cap': 0,
                                               'bms_warn_info': 0,
                                               'buck1_ntc_temperature': 25.2,
                                               'buck2_ntc_temperature': 25.3,
                                               'calendar': 1718612986554,
                                               'capacity': 100.0,
                                               'capacity_text': '100 %',
                                               'cell2_voltage1': 0.0,
                                               'cell2_voltage10': 0.0,
                                               'cell2_voltage11': 0.0,
                                               'cell2_voltage12': 0.0,
                                               'cell2_voltage13': 0.0,
                                               'cell2_voltage14': 0.0,
                                               'cell2_voltage15': 0.0,
                                               'cell2_voltage16': 0.0,
                                               'cell2_voltage2': 0.0,
                                               'cell2_voltage3': 0.0,
                                               'cell2_voltage4': 0.0,
                                               'cell2_voltage5': 0.0,
                                               'cell2_voltage6': 0.0,
                                               'cell2_voltage7': 0.0,
                                               'cell2_voltage8': 0.0,
                                               'cell2_voltage9': 0.0,
                                               'cell_voltage1': 0.0,
                                               'cell_voltage10': 0.0,
                                               'cell_voltage11': 0.0,
                                               'cell_voltage12': 0.0,
                                               'cell_voltage13': 0.0,
                                               'cell_voltage14': 0.0,
                                               'cell_voltage15': 0.0,
                                               'cell_voltage16': 0.0,
                                               'cell_voltage2': 0.0,
                                               'cell_voltage3': 0.0,
                                               'cell_voltage4': 0.0,
                                               'cell_voltage5': 0.0,
                                               'cell_voltage6': 0.0,
                                               'cell_voltage7': 0.0,
                                               'cell_voltage8': 0.0,
                                               'cell_voltage9': 0.0,
                                               'charge_bat_num': 0,
                                               'charge_current': 0.0,
                                               'charge_day_map': {},
                                               'charge_energy': 0.0,
                                               'charge_map': {},
                                               'charge_month': 0.0,
                                               'charge_month_text': '0',
                                               'charge_to_standby_reason': 0,
                                               'charge_to_standby_reason_text': 'Unknown',
                                               'charge_way': 0,
                                               'constant_volt': 0.0,
                                               'constant_volt2': 0.0,
                                               'cycle_count': 0,
                                               'cycle_count2': 0,
                                               'datalogger_sn': 'EAP0D9M006',
                                               'day': None,
                                               'day_map': None,
                                               'dc_dc_temperature': 28.6,
                                               'delta_volt': 0.0,
                                               'delta_volt2': 0.0,
                                               'device_sn': 'KHMOCM5688',
                                               'device_type': 6,
                                               'discharge_current': 0.0,
                                               'discharge_map': {},
                                               'discharge_map_map': {},
                                               'discharge_month': 0.0,
                                               'discharge_month_2': 0.0,
                                               'discharge_month_text': '0',
                                               'discharge_to_standby_reason': 0,
                                               'discharge_to_standby_reason_text': 'Unknown',
                                               'do_status': 0,
                                               'dsg_bat_num': 0,
                                               'dsg_energy': 0.0,
                                               'e_bat_charge_today': 0.0,
                                               'e_bat_charge_total': 0.0,
                                               'e_bat_discharge_today': 0.7,
                                               'e_bat_discharge_total': 0.7,
                                               'e_charge_today': 0.0,
                                               'e_charge_today2': 0.0,
                                               'e_charge_today_text': '0.0 kWh',
                                               'e_charge_total': 0.0,
                                               'e_charge_total2': 0.0,
                                               'e_charge_total_text': '0.0 kWh',
                                               'e_discharge_today': 0.0,
                                               'e_discharge_today2': 0.0,
                                               'e_discharge_today_text': '0.0 kWh',
                                               'e_discharge_total': 0.0,
                                               'e_discharge_total2': 0.0,
                                               'e_discharge_total_text': '0.0 kWh',
                                               'e_gen_discharge_power': 0.0,
                                               'e_gen_discharge_power1': 0.0,
                                               'e_gen_discharge_power2': 0.0,
                                               'e_gen_discharge_today': 0.0,
                                               'e_gen_discharge_total': 0.0,
                                               'e_to_grid_today': 5.4,
                                               'e_to_grid_total': 5.1,
                                               'e_to_user_today': 0.0,
                                               'e_to_user_total': 0.0,
                                               'e_today': 6.0,
                                               'e_total': 5.4,
                                               'eac_charge_today': 0.0,
                                               'eac_charge_total': 0.0,
                                               'eac_discharge_today': 0.0,
                                               'eac_discharge_total': 0.0,
                                               'env_temperature': 0.0,
                                               'eop_discharge_today': 0.0,
                                               'eop_discharge_total': 0.0,
                                               'epv_today': 6.0,
                                               'epv_today2': 0.0,
                                               'epv_total': 5.4,
                                               'epv_total2': 0.0,
                                               'error_code': 0,
                                               'error_text': 'Unknown',
                                               'fault_code': 0,
                                               'float_charge_volt': 0.0,
                                               'freq_grid': 0.0,
                                               'freq_output': 50.0,
                                               'gauge2_rm1': 0.0,
                                               'gauge2_rm2': 0.0,
                                               'gauge_battery_status': 0,
                                               'gauge_fcc': 0.0,
                                               'gauge_ic_current': 0.0,
                                               'gauge_operation_status': 0,
                                               'gauge_pack_status': 0,
                                               'gauge_rm': 0.0,
                                               'gauge_rm1': 0.0,
                                               'gauge_rm2': 0.0,
                                               'gen_current': 0.0,
                                               'gen_current1': 0.0,
                                               'gen_current2': 0.0,
                                               'gen_volt': 0.0,
                                               'gen_volt2': 0.0,
                                               'hardware_version': 0,
                                               'i_ac_charge': 0.0,
                                               'i_ac_charge1': 0.0,
                                               'i_ac_charge2': 0.0,
                                               'i_charge': 0.0,
                                               'i_charge_pv1': 0.0,
                                               'i_charge_pv2': 0.0,
                                               'i_charge_text': '0.0 A',
                                               'i_discharge': 0.0,
                                               'i_discharge_text': '0.0 A',
                                               'iac_to_grid': 0.0,
                                               'iac_to_grid_text': '0.0 A',
                                               'iac_to_user': 0.0,
                                               'iac_to_user_text': '0.0 A',
                                               'inner_cw_code': None,
                                               'inv_temperature': 31.8,
                                               'ipm_temperature': 0.0,
                                               'ipv': 0.0,
                                               'ipv_text': '0.0 A',
                                               'llc_temperature': 0.0,
                                               'load_percent': 0.0,
                                               'load_percent1': 0.0,
                                               'load_percent2': 0.0,
                                               'lost': True,
                                               'manual_start_en': 0.0,
                                               'manufacture': 0,
                                               'max_cell_temp': 0.0,
                                               'max_cell_volt': 0.0,
                                               'max_charge_or_discharge_current': 0.0,
                                               'max_charge_or_discharge_current2': 0.0,
                                               'max_min_cell_temp_serial_num': 0,
                                               'max_min_cell_volt_num': 0,
                                               'max_min_soc': 0.0,
                                               'min_cell_temp': 0.0,
                                               'min_cell_volt': 0.0,
                                               'module2_max_temp': 0.0,
                                               'module2_max_volt': 0.0,
                                               'module2_min_temp': 0.0,
                                               'module2_min_volt': 0.0,
                                               'module_id': 0,
                                               'module_id2': 0,
                                               'module_soc': 0.0,
                                               'module_status': 0,
                                               'module_total_curr': 0.0,
                                               'module_total_volt': 0.0,
                                               'normal_power': 0,
                                               'output_current': 0.2,
                                               'output_current2': 0.0,
                                               'output_power': 0.0,
                                               'output_power1': 0.0,
                                               'output_power2': 0.0,
                                               'output_volt': 229.9,
                                               'output_volt2': 0.0,
                                               'p_ac_charge': 0.0,
                                               'p_ac_input': 0.0,
                                               'p_ac_input1': 0.0,
                                               'p_ac_input2': 0.0,
                                               'p_ac_output': 0.0,
                                               'p_bat': 0.0,
                                               'p_charge': 0.0,
                                               'p_charge2': 0.0,
                                               'p_charge_text': '0.0 W',
                                               'p_discharge': 0.0,
                                               'p_discharge2': 0.0,
                                               'p_discharge_text': '0.0 W',
                                               'pac_to_grid': 0.0,
                                               'pac_to_grid_text': '0.0 W',
                                               'pac_to_user': 0.0,
                                               'pac_to_user_text': '0.0 W',
                                               'pack_num': 0,
                                               'parallel_hight_softwar_ver': 0,
                                               'pow_saving_en': 0.0,
                                               'ppv': 0.0,
                                               'ppv2': 0.0,
                                               'ppv_text': '0.0 W',
                                               'protect_pack_id': 0,
                                               'q_bat': 0.0,
                                               'rate_va': 0.0,
                                               'rate_watt': 0.0,
                                               'remote_cntl_en': 0.0,
                                               'remote_cntl_fail_reason': 0,
                                               'request_battery_type': 0,
                                               'sci_loss_chk_en': 0.0,
                                               'software_version1': None,
                                               'software_version2': None,
                                               'software_version3': None,
                                               'soh': 0.0,
                                               'soh2': 0.0,
                                               'spf5000_status_text': 'Battery Discharging',
                                               'status': 2,
                                               'status_text': 'Discharge',
                                               'storage_bean': None,
                                               'sys_out': 0.0,
                                               'temperature': 0.0,
                                               'time': datetime.datetime(2024, 6, 17, 16, 29, 46),
                                               'total_cell_num': 0,
                                               'update_status': 0,
                                               'uw_bat_type2': 0.0,
                                               'v_bat': 53.14,
                                               'v_bat_text': '53.14 V',
                                               'v_buck': 0.0,
                                               'v_buck2': 0.0,
                                               'v_buck_text': '0.0 V',
                                               'v_bus': 468.6,
                                               'v_grid': 0.0,
                                               'v_grid2': 0.0,
                                               'vac': 0.0,
                                               'vac_Text': '0.0 V',
                                               'vpv': 0.0,
                                               'vpv2': 0.0,
                                               'vpv_text': '0.0 V',
                                               'warn_code': 0,
                                               'warn_code2': 0,
                                               'warn_code3': 0,
                                               'warn_info': 0,
                                               'warn_info2': 0,
                                               'warn_text': 'Unknown',
                                               'with_time': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            MaxEnergyV4
            {   'data': {   'max': [   {   'address': 0,
                                           'afci_pv1': 0,
                                           'afci_pv2': 0,
                                           'afci_status': 0,
                                           'again': False,
                                           'alias': None,
                                           'apf_status': 0.0,
                                           'apf_status_text': None,
                                           'calendar': 1714113885020,
                                           'comp_har_ir': 0.0,
                                           'comp_har_is': 0.0,
                                           'comp_har_it': 0.0,
                                           'comp_qr': 0.0,
                                           'comp_qs': 0.0,
                                           'comp_qt': 0.0,
                                           'ct_har_ir': 0.0,
                                           'ct_har_is': 0.0,
                                           'ct_har_it': 0.0,
                                           'ct_ir': 0.0,
                                           'ct_is': 0.0,
                                           'ct_it': 0.0,
                                           'ct_qr': 0.0,
                                           'ct_qs': 0.0,
                                           'ct_qt': 0.0,
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
                                           'current_string21': 0.0,
                                           'current_string22': 0.0,
                                           'current_string23': 0.0,
                                           'current_string24': 0.0,
                                           'current_string25': 0.0,
                                           'current_string26': 0.0,
                                           'current_string27': 0.0,
                                           'current_string28': 0.0,
                                           'current_string29': 0.0,
                                           'current_string3': 0.0,
                                           'current_string30': 0.0,
                                           'current_string31': 0.0,
                                           'current_string32': 0.0,
                                           'current_string4': 0.0,
                                           'current_string5': 0.0,
                                           'current_string6': 0.0,
                                           'current_string7': 0.0,
                                           'current_string8': 0.0,
                                           'current_string9': 0.0,
                                           'datalogger_sn': 'BLE4BL40GS',
                                           'day': None,
                                           'debug1': '0，0，0，30200，7，55，0，8200',
                                           'debug2': '0，24，3，20，24，4，26，0',
                                           'debug3': '0，0，0，0，0，0，0，0',
                                           'derating_mode': 7,
                                           'device_sn': 'QXHLD7F0C9',
                                           'dw_string_warning_value1': 0,
                                           'e_rac_today': 0.0,
                                           'e_rac_total': 0.0,
                                           'eac_today': 0.0,
                                           'eac_total': 225.9,
                                           'epv10_today': 0.0,
                                           'epv10_total': 0.0,
                                           'epv11_today': 0.0,
                                           'epv11_total': 0.0,
                                           'epv12_today': 0.0,
                                           'epv12_total': 0.0,
                                           'epv13_today': 0.0,
                                           'epv13_total': 0.0,
                                           'epv14_today': 0.0,
                                           'epv14_total': 0.0,
                                           'epv15_today': 0.0,
                                           'epv15_total': 0.0,
                                           'epv16_today': 0.0,
                                           'epv16_total': 0.0,
                                           'epv1_today': 0.0,
                                           'epv1_total': 140.3,
                                           'epv2_today': 0.0,
                                           'epv2_total': 83.6,
                                           'epv3_today': 0.0,
                                           'epv3_total': 0.0,
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
                                           'epv9_today': 0.0,
                                           'epv9_total': 0.0,
                                           'epv_total': 223.9,
                                           'fac': 46.0,
                                           'fault_code1': 0,
                                           'fault_code2': 0,
                                           'fault_type': 302,
                                           'fault_value': 0,
                                           'gfci': 2.0,
                                           'i_pid_pvape': 0.0,
                                           'i_pid_pvbpe': 0.0,
                                           'i_pid_pvcpe': 0.0,
                                           'i_pid_pvdpe': 0.0,
                                           'i_pid_pvepe': 0.0,
                                           'i_pid_pvfpe': 0.0,
                                           'i_pid_pvgpe': 0.0,
                                           'i_pid_pvhpe': 0.0,
                                           'i_pid_pvpe10': 0.0,
                                           'i_pid_pvpe11': 0.0,
                                           'i_pid_pvpe12': 0.0,
                                           'i_pid_pvpe13': 0.0,
                                           'i_pid_pvpe14': 0.0,
                                           'i_pid_pvpe15': 0.0,
                                           'i_pid_pvpe16': 0.0,
                                           'i_pid_pvpe9': 0.0,
                                           'iacr': 0.0,
                                           'iacs': 0.0,
                                           'iact': 0.0,
                                           'id': 0,
                                           'ipm_temperature': 0.0,
                                           'ipv1': 0.0,
                                           'ipv10': 0.0,
                                           'ipv11': 0.0,
                                           'ipv12': 0.0,
                                           'ipv13': 0.0,
                                           'ipv14': 0.0,
                                           'ipv15': 0.0,
                                           'ipv16': 0.0,
                                           'ipv2': 0.0,
                                           'ipv3': 0.0,
                                           'ipv4': 0.0,
                                           'ipv5': 0.0,
                                           'ipv6': 0.0,
                                           'ipv7': 0.0,
                                           'ipv8': 0.0,
                                           'ipv9': 0.0,
                                           'lost': True,
                                           'max_bean': None,
                                           'n_bus_voltage': 292.9,
                                           'op_fullwatt': 555.5,
                                           'p_bus_voltage': 300.4,
                                           'pac': 0.0,
                                           'pacr': 0.0,
                                           'pacs': 0.0,
                                           'pact': 0.0,
                                           'pf': 1.0,
                                           'pid_bus': 0.0,
                                           'pid_fault_code': 0,
                                           'pid_status': 0,
                                           'pid_status_text': 'Lost',
                                           'power_today': 0.0,
                                           'power_total': 0.0,
                                           'ppv': 0.0,
                                           'ppv1': 0.0,
                                           'ppv10': 0.0,
                                           'ppv11': 0.0,
                                           'ppv12': 0.0,
                                           'ppv13': 0.0,
                                           'ppv14': 0.0,
                                           'ppv15': 0.0,
                                           'ppv16': 0.0,
                                           'ppv2': 0.0,
                                           'ppv3': 0.0,
                                           'ppv4': 0.0,
                                           'ppv5': 0.0,
                                           'ppv6': 0.0,
                                           'ppv7': 0.0,
                                           'ppv8': 0.0,
                                           'ppv9': 0.0,
                                           'pv_iso': 0.0,
                                           'r_dci': 0.0,
                                           'rac': 0.0,
                                           'react_power': 0.0,
                                           'react_power_max': 0.0,
                                           'react_power_total': 0.0,
                                           'real_op_percent': 0.0,
                                           's_dci': 0.0,
                                           'status': 3,
                                           'status_text': 'Fault',
                                           'str_break': 0,
                                           'str_fault': 0,
                                           'str_unbalance': 0,
                                           'str_unmatch': 0,
                                           't_dci': 0.0,
                                           'temperature': 55.100002,
                                           'temperature2': 25.7,
                                           'temperature3': 25.7,
                                           'temperature4': 0.0,
                                           'temperature5': 0.0,
                                           'time': datetime.datetime(2024, 4, 26, 14, 44, 45),
                                           'time_calendar': 1714113885020,
                                           'time_total': 808233.0,
                                           'v_pid_pvape': 0.0,
                                           'v_pid_pvbpe': 0.0,
                                           'v_pid_pvcpe': 0.0,
                                           'v_pid_pvdpe': 0.0,
                                           'v_pid_pvepe': 0.0,
                                           'v_pid_pvfpe': 0.0,
                                           'v_pid_pvgpe': 0.0,
                                           'v_pid_pvhpe': 0.0,
                                           'v_pid_pvpe10': 0.0,
                                           'v_pid_pvpe11': 0.0,
                                           'v_pid_pvpe12': 0.0,
                                           'v_pid_pvpe13': 0.0,
                                           'v_pid_pvpe14': 0.0,
                                           'v_pid_pvpe15': 0.0,
                                           'v_pid_pvpe16': 0.0,
                                           'v_pid_pvpe9': 0.0,
                                           'v_string1': 0.0,
                                           'v_string10': 0.0,
                                           'v_string11': 0.0,
                                           'v_string12': 0.0,
                                           'v_string13': 0.0,
                                           'v_string14': 0.0,
                                           'v_string15': 0.0,
                                           'v_string16': 0.0,
                                           'v_string17': 0.0,
                                           'v_string18': 0.0,
                                           'v_string19': 0.0,
                                           'v_string2': 0.0,
                                           'v_string20': 0.0,
                                           'v_string21': 0.0,
                                           'v_string22': 0.0,
                                           'v_string23': 0.0,
                                           'v_string24': 0.0,
                                           'v_string25': 0.0,
                                           'v_string26': 0.0,
                                           'v_string27': 0.0,
                                           'v_string28': 0.0,
                                           'v_string29': 0.0,
                                           'v_string3': 0.0,
                                           'v_string30': 0.0,
                                           'v_string31': 0.0,
                                           'v_string32': 0.0,
                                           'v_string4': 0.0,
                                           'v_string5': 0.0,
                                           'v_string6': 0.0,
                                           'v_string7': 0.0,
                                           'v_string8': 0.0,
                                           'v_string9': 0.0,
                                           'vac_rs': 0.3,
                                           'vac_st': 2.5,
                                           'vac_tr': 2.3,
                                           'vacr': 0.7,
                                           'vacs': 0.90000004,
                                           'vact': 1.6,
                                           'vpv1': 599.8,
                                           'vpv10': 0.0,
                                           'vpv11': 0.0,
                                           'vpv12': 0.0,
                                           'vpv13': 0.0,
                                           'vpv14': 0.0,
                                           'vpv15': 0.0,
                                           'vpv16': 0.0,
                                           'vpv2': 292.7,
                                           'vpv3': 0.0,
                                           'vpv4': 0.0,
                                           'vpv5': 0.0,
                                           'vpv6': 0.0,
                                           'vpv7': 0.0,
                                           'vpv8': 0.0,
                                           'vpv9': 0.0,
                                           'w_pid_fault_value': 0,
                                           'w_string_status_value': 0,
                                           'warn_bit': 0,
                                           'warn_code': 0,
                                           'warning_value1': 0,
                                           'warning_value2': 0,
                                           'warning_value3': 0,
                                           'with_time': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            SphEnergyV4
            {   'data': {   'sph': [   {   'ac_charge_energy_today': 0.0,
                                           'ac_charge_energy_total': 39.900001525878906,
                                           'ac_charge_power': 0.0,
                                           'acc_charge_pack_sn': 0,
                                           'acc_charge_power': 0.0,
                                           'acc_discharge_pack_sn': 0,
                                           'acc_discharge_power': 0.0,
                                           'address': 0,
                                           'again': False,
                                           'alias': None,
                                           'b_module_num': 0,
                                           'b_total_cell_num': 0,
                                           'backup_warning': 0,
                                           'bat_error_union': 0,
                                           'batt_history_fault_code1': 0,
                                           'batt_history_fault_code2': 0,
                                           'batt_history_fault_code3': 0,
                                           'batt_history_fault_code4': 0,
                                           'batt_history_fault_code5': 0,
                                           'batt_history_fault_code6': 0,
                                           'batt_history_fault_code7': 0,
                                           'batt_history_fault_code8': 0,
                                           'battery_temperature': 0.0,
                                           'battery_type': 1,
                                           'bms_battery_curr': 0.0,
                                           'bms_battery_temp': 0.0,
                                           'bms_battery_volt': 0.0,
                                           'bms_cell10_volt': 0.0,
                                           'bms_cell11_volt': 0.0,
                                           'bms_cell12_volt': 0.0,
                                           'bms_cell13_volt': 0.0,
                                           'bms_cell14_volt': 0.0,
                                           'bms_cell15_volt': 0.0,
                                           'bms_cell16_volt': 0.0,
                                           'bms_cell1_volt': 0.0,
                                           'bms_cell2_volt': 0.0,
                                           'bms_cell3_volt': 0.0,
                                           'bms_cell4_volt': 0.0,
                                           'bms_cell5_volt': 0.0,
                                           'bms_cell6_volt': 0.0,
                                           'bms_cell7_volt': 0.0,
                                           'bms_cell8_volt': 0.0,
                                           'bms_cell9_volt': 0.0,
                                           'bms_constant_volt': 0.0,
                                           'bms_cycle_cnt': 0,
                                           'bms_delta_volt': 0.0,
                                           'bms_error': 0,
                                           'bms_error2': 0,
                                           'bms_error3': 0,
                                           'bms_error_expansion': 0,
                                           'bms_error_old': 0,
                                           'bms_fw': 0,
                                           'bms_gauge_fcc': 0.0,
                                           'bms_gauge_rm': 0.0,
                                           'bms_hardware_version': 0,
                                           'bms_hardware_version2': 0,
                                           'bms_highest_soft_version': 0,
                                           'bms_info': 0,
                                           'bms_max_curr': 0.0,
                                           'bms_max_dischg_curr': 0.0,
                                           'bms_mcu_version': 0,
                                           'bms_pack_info': 0,
                                           'bms_protection': 0,
                                           'bms_request_type': 0,
                                           'bms_soc': 0,
                                           'bms_soh': 0,
                                           'bms_status': 0,
                                           'bms_status_old': 0,
                                           'bms_using_cap': 0,
                                           'bms_warn_info': 0,
                                           'bms_warn_info2': 0,
                                           'bms_warn_info_old': 0,
                                           'calendar': 1736416511922,
                                           'capacity_add': 0.0,
                                           'charge_cutoff_volt': 0.0,
                                           'charge_forbidden_mark': 0,
                                           'datalogger_sn': 'XGD6E9K06M',
                                           'day': None,
                                           'day_map': None,
                                           'device_sn': 'AQM1234567',
                                           'discharge_cutoff_volt': 0.0,
                                           'discharge_forbidden_mark': 0,
                                           'dsgip_start_date_time': None,
                                           'e_to_grid_today': 1.0,
                                           'e_to_grid_total': 103.9,
                                           'e_to_user_today': 0.0,
                                           'e_to_user_total': 23.5,
                                           'eac_today': 0.0,
                                           'eac_total': 128.3,
                                           'echarge1_today': 0.0,
                                           'echarge1_total': 64.5,
                                           'edischarge1_today': 0.0,
                                           'edischarge1_total': 59.6,
                                           'eex_today': 0.0,
                                           'eex_total': 0.9,
                                           'elocal_load_today': 0.0,
                                           'elocal_load_total': 41.0,
                                           'eps_vac2': 0.0,
                                           'eps_vac3': 0.0,
                                           'epv1_today': 0.0,
                                           'epv1_total': 54.7,
                                           'epv2_today': 0.0,
                                           'epv2_total': 40.7,
                                           'epv_today': 0.0,
                                           'epv_total': 95.4,
                                           'error_code': 0,
                                           'error_text': 'Unknown',
                                           'eself_today': 0.0,
                                           'eself_total': 26.299999237060547,
                                           'esystem_today': 0.0,
                                           'esystem_total': 119.69999694824219,
                                           'fac': 49.98,
                                           'fault_bit_code': 0,
                                           'fault_code': 0,
                                           'first_batt_fault_sn': None,
                                           'fourth_batt_fault_sn': 0,
                                           'iac1': 0.0,
                                           'iac2': 0.0,
                                           'iac3': 0.0,
                                           'lost': True,
                                           'max_single_cell_tem': 0.0,
                                           'max_single_cell_tem_no': 0,
                                           'max_single_cell_volt': 0.0,
                                           'max_single_cell_volt_no': 0,
                                           'max_soc': 0.0,
                                           'min_single_cell_tem': 0.0,
                                           'min_single_cell_tem_no': 0,
                                           'min_single_cell_volt': 0.0,
                                           'min_single_cell_volt_no': 0,
                                           'min_soc': 0.0,
                                           'mix_bean': None,
                                           'module_qty': 0,
                                           'module_series_qty': 0,
                                           'number_of_batt_codes': 0,
                                           'pac': 0.3,
                                           'pac1': 0.0,
                                           'pac2': 0.0,
                                           'pac3': 0.0,
                                           'pac_r': 0.0,
                                           'pac_s': 0.0,
                                           'pac_t': 0.0,
                                           'pac_to_grid_r': 50.0,
                                           'pac_to_grid_total': 50.0,
                                           'pac_to_user_r': 0.0,
                                           'pac_to_user_total': 0.0,
                                           'pcharge1': 0.0,
                                           'pdischarge1': 0.0,
                                           'pex': 0.0,
                                           'plocal_load_r': 0.0,
                                           'plocal_load_r2': 0.0,
                                           'plocal_load_s': 0.0,
                                           'plocal_load_t': 0.0,
                                           'plocal_load_total': 0.0,
                                           'pm_r': 0.0,
                                           'pm_s': 0.0,
                                           'pm_t': 0.0,
                                           'ppv': 0.0,
                                           'ppv1': 0.0,
                                           'ppv2': 0.0,
                                           'ppv_text': '0.0 W',
                                           'priority_choose': 0.0,
                                           'protect_pack_id': 0,
                                           'pself': 0.0,
                                           'psystem': 0.0,
                                           'second_batt_fault_sn': 0,
                                           'sgip_cycl_cnt': 0,
                                           'sgip_start_cycl_cnt': 0,
                                           'soc': 0.0,
                                           'soc_text': '0%',
                                           'software_develop_major_version': 0,
                                           'software_develop_minor_version': 0,
                                           'software_major_version': 0,
                                           'software_minor_version': 0,
                                           'status': 9,
                                           'status_text': 'Bypass',
                                           'sys_en': 20992,
                                           'sys_fault_word': 0,
                                           'sys_fault_word1': 0,
                                           'sys_fault_word2': 0,
                                           'sys_fault_word3': 33280,
                                           'sys_fault_word4': 32,
                                           'sys_fault_word5': 0,
                                           'sys_fault_word6': 0,
                                           'sys_fault_word7': 0,
                                           'temp1': 29.6,
                                           'temp2': 27.4,
                                           'temp3': 28.800001,
                                           'third_batt_fault_sn': 0,
                                           'time': datetime.datetime(2025, 1, 9, 17, 55, 11),
                                           'time_total': 577485.5,
                                           'ups_fac': 0.0,
                                           'ups_load_percent': 0.0,
                                           'ups_pac1': 0.0,
                                           'ups_pac2': 0.0,
                                           'ups_pac3': 0.0,
                                           'ups_pf': 1000.0,
                                           'ups_vac1': 234.0,
                                           'uw_bat_cycle_cnt_pr': None,
                                           'uw_dsp_dc_dc_debug_data': 0,
                                           'uw_dsp_dc_dc_debug_data1': 0,
                                           'uw_dsp_dc_dc_debug_data2': 0,
                                           'uw_dsp_dc_dc_debug_data3': 0,
                                           'uw_dsp_dc_dc_debug_data4': 0,
                                           'uw_dsp_inv_debug_data': 0,
                                           'uw_dsp_inv_debug_data1': 0,
                                           'uw_dsp_inv_debug_data2': 0,
                                           'uw_dsp_inv_debug_data3': 0,
                                           'uw_dsp_inv_debug_data4': 0,
                                           'uw_max_cell_vol': 0.0,
                                           'uw_max_tempr_cell': 0.0,
                                           'uw_max_tempr_cell_no': 0,
                                           'uw_max_volt_cell_no': 0,
                                           'uw_min_cell_vol': 0.0,
                                           'uw_min_tempr_cell': 0.0,
                                           'uw_min_tempr_cell_no': 0,
                                           'uw_min_volt_cell_no': 0,
                                           'uw_sys_work_mode': 9,
                                           'v_bat_dsp': 2.1000001,
                                           'v_bus1': 2.5,
                                           'v_bus2': 4.3,
                                           'vac1': 236.4,
                                           'vac2': 0.0,
                                           'vac3': 0.0,
                                           'vbat': 0.0,
                                           'vpv1': 0.0,
                                           'vpv2': 0.0,
                                           'warn_code': 0,
                                           'warn_text': 'Unknown',
                                           'with_time': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            SpaEnergyV4
            {   'data': {   'spa': [   {   'ac_charge_energy_today': 0.0,
                                           'ac_charge_energy_total': 8.3,
                                           'ac_charge_power': 0.0,
                                           'acc_charge_pack_sn': 0,
                                           'acc_charge_power': 0.0,
                                           'acc_discharge_pack_sn': 0,
                                           'acc_discharge_power': 0.0,
                                           'address': 0,
                                           'again': False,
                                           'alias': None,
                                           'b_module_num': 0,
                                           'b_total_cell_num': 0,
                                           'batt_history_fault_code1': 0,
                                           'batt_history_fault_code2': 0,
                                           'batt_history_fault_code3': 0,
                                           'batt_history_fault_code4': 0,
                                           'batt_history_fault_code5': 0,
                                           'batt_history_fault_code6': 0,
                                           'batt_history_fault_code7': 0,
                                           'batt_history_fault_code8': 0,
                                           'battery_temperature': 0.0,
                                           'battery_type': 1,
                                           'bms_battery_curr': 0.0,
                                           'bms_battery_temp': 0.0,
                                           'bms_battery_volt': 0.0,
                                           'bms_cell10_volt': 0.0,
                                           'bms_cell11_volt': 0.0,
                                           'bms_cell12_volt': 0.0,
                                           'bms_cell13_volt': 0.0,
                                           'bms_cell14_volt': 0.0,
                                           'bms_cell15_volt': 0.0,
                                           'bms_cell16_volt': 0.0,
                                           'bms_cell1_volt': 0.0,
                                           'bms_cell2_volt': 0.0,
                                           'bms_cell3_volt': 0.0,
                                           'bms_cell4_volt': 0.0,
                                           'bms_cell5_volt': 0.0,
                                           'bms_cell6_volt': 0.0,
                                           'bms_cell7_volt': 0.0,
                                           'bms_cell8_volt': 0.0,
                                           'bms_cell9_volt': 0.0,
                                           'bms_constant_volt': 0.0,
                                           'bms_cycle_cnt': 0,
                                           'bms_delta_volt': 0.0,
                                           'bms_error': 0,
                                           'bms_error2': 0,
                                           'bms_error3': 0,
                                           'bms_error_old': 0,
                                           'bms_fw': 0,
                                           'bms_gauge_fcc': 0.0,
                                           'bms_gauge_rm': 0.0,
                                           'bms_hardware_version': 0,
                                           'bms_hardware_version2': 0,
                                           'bms_highest_soft_version': 0,
                                           'bms_info': 0,
                                           'bms_max_curr': 0.0,
                                           'bms_max_dischg_curr': 0.0,
                                           'bms_mcu_version': 0,
                                           'bms_pack_info': 0,
                                           'bms_request_type': 0,
                                           'bms_soc': 0,
                                           'bms_soh': 0,
                                           'bms_status': 0,
                                           'bms_status_old': 0,
                                           'bms_using_cap': 0,
                                           'bms_warn_info': 0,
                                           'bms_warn_info_old': 0,
                                           'calendar': 1716435473718,
                                           'datalogger_sn': 'XGD6CMM2VY',
                                           'day': None,
                                           'day_map': None,
                                           'device_sn': 'MTN0H6800E',
                                           'e_to_grid_today': 0.0,
                                           'e_to_grid_total': 1.0,
                                           'e_to_user_today': 0.0,
                                           'e_to_user_total': 0.0,
                                           'eac_today': 0.0,
                                           'eac_total': 6.5,
                                           'echarge1_today': 0.0,
                                           'echarge1_total': 7.6,
                                           'edischarge1_today': 0.0,
                                           'edischarge1_total': 6.8,
                                           'elocal_load_today': 0.0,
                                           'elocal_load_total': 0.0,
                                           'epv_inverter_today': 0.0,
                                           'epv_inverter_total': 0.0,
                                           'error_code': 0,
                                           'error_text': 'Unknown',
                                           'eself_today': 0.0,
                                           'eself_total': 5.9,
                                           'esystem_today': None,
                                           'esystem_total': None,
                                           'fac': 49.99,
                                           'fault_bit_code': 0,
                                           'fault_code': 0,
                                           'first_batt_fault_sn': 0,
                                           'fourth_batt_fault_sn': 0,
                                           'iac1': 0.0,
                                           'iac2': 0.0,
                                           'iac3': 0.0,
                                           'lost': True,
                                           'max_soc': 0.0,
                                           'min_soc': 0.0,
                                           'module_series_qty': 0,
                                           'monitor': 1,
                                           'number_of_batt_codes': 0,
                                           'pac': 0.3,
                                           'pac1': 0.0,
                                           'pac_r': 0.0,
                                           'pac_s': 0.0,
                                           'pac_t': 0.0,
                                           'pac_to_grid_r': 0.0,
                                           'pac_to_grid_total': 0.0,
                                           'pac_to_user_r': 0.0,
                                           'pac_to_user_total': 0.0,
                                           'pcharge1': 0.0,
                                           'pdischarge1': 0.0,
                                           'plocal_load_r': 0.0,
                                           'plocal_load_r2': 0.0,
                                           'plocal_load_s': 0.0,
                                           'plocal_load_t': 0.0,
                                           'plocal_load_total': 0.0,
                                           'pm_r': 0.0,
                                           'pm_s': 0.0,
                                           'pm_t': 0.0,
                                           'ppv_inverter': 0.0,
                                           'priority_choose': 2.0,
                                           'protect_pack_id': 0,
                                           'pself': 0.0,
                                           'psystem': 0.0,
                                           'second_batt_fault_sn': 0,
                                           'soc': 0.0,
                                           'soc_text': '0%',
                                           'spa_bean': None,
                                           'status': 9,
                                           'status_text': 'Bypass',
                                           'sys_en': 20992,
                                           'sys_fault_word': 0,
                                           'sys_fault_word1': 0,
                                           'sys_fault_word2': 0,
                                           'sys_fault_word3': 33280,
                                           'sys_fault_word4': 0,
                                           'sys_fault_word5': 0,
                                           'sys_fault_word6': 0,
                                           'sys_fault_word7': 4,
                                           'temp1': 28.300001,
                                           'temp2': 26.7,
                                           'temp3': 27.7,
                                           'third_batt_fault_sn': 0,
                                           'time': datetime.datetime(2024, 5, 23, 11, 37, 53),
                                           'time_total': 265549.0,
                                           'ups_fac': 0.0,
                                           'ups_iac1': 0.0,
                                           'ups_iac2': 0.0,
                                           'ups_iac3': 0.0,
                                           'ups_load_percent': 0.0,
                                           'ups_pac1': 0.0,
                                           'ups_pac2': 0.0,
                                           'ups_pac3': 0.0,
                                           'ups_pf': 1000.0,
                                           'ups_vac1': 225.4,
                                           'ups_vac2': 0.0,
                                           'ups_vac3': 0.0,
                                           'uw_dsp_dc_dc_debug_data': 0,
                                           'uw_dsp_dc_dc_debug_data1': 0,
                                           'uw_dsp_dc_dc_debug_data2': 0,
                                           'uw_dsp_dc_dc_debug_data3': 0,
                                           'uw_dsp_dc_dc_debug_data4': 0,
                                           'uw_dsp_inv_debug_data': 0,
                                           'uw_dsp_inv_debug_data1': 0,
                                           'uw_dsp_inv_debug_data2': 0,
                                           'uw_dsp_inv_debug_data3': 0,
                                           'uw_dsp_inv_debug_data4': 0,
                                           'uw_max_cell_vol': 0.0,
                                           'uw_max_tempr_cell': 0.0,
                                           'uw_max_tempr_cell_no': 0,
                                           'uw_max_volt_cell_no': 0,
                                           'uw_min_cell_vol': 0.0,
                                           'uw_min_tempr_cell': 0.0,
                                           'uw_min_tempr_cell_no': 0,
                                           'uw_min_volt_cell_no': 0,
                                           'uw_sys_work_mode': 9,
                                           'v_bat_dsp': 2.2,
                                           'v_bus1': 4.3,
                                           'v_bus2': 4.8,
                                           'vac1': 227.3,
                                           'vac2': 0.0,
                                           'vac3': 0.0,
                                           'vbat': 0.0,
                                           'warn_code': 0,
                                           'warn_text': 'Unknown',
                                           'with_time': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            MinEnergyV4
            {   'data': {   'min': [   {   'address': 0,
                                           'again': False,
                                           'alias': None,
                                           'b_merter_connect_flag': False,
                                           'bat_sn': None,
                                           'battery_no': -1,
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
                                           'bgrid_type': 0,
                                           'bms_communication_type': 0,
                                           'bms_cv_volt': 0.0,
                                           'bms_error2': 0,
                                           'bms_error3': 0,
                                           'bms_error4': 0,
                                           'bms_fault_type': 0,
                                           'bms_fw_version': '0',
                                           'bms_ibat': 0.0,
                                           'bms_icycle': 0.0,
                                           'bms_info': 0.0,
                                           'bms_ios_status': 0,
                                           'bms_max_curr': 0.0,
                                           'bms_mcu_version': '0',
                                           'bms_pack_info': 0.0,
                                           'bms_soc': 0.0,
                                           'bms_soh': 0.0,
                                           'bms_status': 0,
                                           'bms_temp1_bat': 0.0,
                                           'bms_using_cap': 0.0,
                                           'bms_vbat': 0.0,
                                           'bms_vdelta': 0.0,
                                           'bms_warn2': 0,
                                           'bms_warn_code': 0.0,
                                           'bsystem_work_mode': 0,
                                           'calendar': 1742974615711,
                                           'datalogger_sn': 'QMN000BZP3N6U09K',
                                           'day': None,
                                           'dc_voltage': 0.0,
                                           'dci_r': 0.0,
                                           'dci_s': 0.0,
                                           'dci_t': 0.0,
                                           'debug1': '0，0，0，0，0，2，2，0',
                                           'debug2': '0，1，9，5660，0，12260，1，0',
                                           'derating_mode': 0,
                                           'device_sn': 'BZP3N6U09K',
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
                                           'eac_today': 0.2,
                                           'eac_total': 76.8,
                                           'eex1_today': -0.1,
                                           'eex1_total': -0.1,
                                           'eex2_today': -0.1,
                                           'eex2_total': -0.1,
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
                                           'epv1_today': 0.3,
                                           'epv1_total': 83.5,
                                           'epv2_today': 0.0,
                                           'epv2_total': 0.0,
                                           'epv3_today': 0.0,
                                           'epv3_total': 0.0,
                                           'epv4_today': 0.0,
                                           'epv4_total': 0.0,
                                           'epv_total': 83.5,
                                           'error_text': 'Unknown',
                                           'fac': 50.0,
                                           'fault_type': 0,
                                           'fault_type1': 0,
                                           'gfci': 0.0,
                                           'iac1': 0.1,
                                           'iac2': 0.0,
                                           'iac3': 0.0,
                                           'iacr': 0.0,
                                           'inv_delay_time': 65.0,
                                           'ipv1': 0.7,
                                           'ipv2': 0.0,
                                           'ipv3': 0.0,
                                           'ipv4': 0.0,
                                           'is_again': False,
                                           'iso': 2648.0,
                                           'load_percent': 0.0,
                                           'lost': True,
                                           'mtnc_mode': 0,
                                           'mtnc_rqst': 0.0,
                                           'n_bus_voltage': 0.0,
                                           'new_warn_code': 0,
                                           'new_warn_sub_code': 0,
                                           'op_fullwatt': 0.0,
                                           'operating_mode': 0,
                                           'p_bus_voltage': 447.8,
                                           'p_self': 0.0,
                                           'p_system': 0.0,
                                           'pac': 10.6,
                                           'pac1': 17.2,
                                           'pac2': 0.0,
                                           'pac3': 0.0,
                                           'pac_to_grid_total': 0.0,
                                           'pac_to_local_load': 0.0,
                                           'pac_to_user_total': 0.0,
                                           'pacr': 0.0,
                                           'pex1': -0.1,
                                           'pex2': -0.1,
                                           'pf': 1.0,
                                           'ppv': 21.6,
                                           'ppv1': 21.6,
                                           'ppv2': 0.0,
                                           'ppv3': 0.0,
                                           'ppv4': 0.0,
                                           'real_op_percent': 1.0,
                                           'soc1': 0.0,
                                           'soc2': 0.0,
                                           'status': 1,
                                           'status_text': 'Normal',
                                           'sys_fault_word': 0,
                                           'sys_fault_word1': 2,
                                           'sys_fault_word2': 0,
                                           'sys_fault_word3': 0,
                                           'sys_fault_word4': 0,
                                           'sys_fault_word5': 0,
                                           'sys_fault_word6': 0,
                                           'sys_fault_word7': 0,
                                           't_mtnc_strt': None,
                                           't_win_end': None,
                                           't_win_start': None,
                                           'temp1': 21.2,
                                           'temp2': 21.2,
                                           'temp3': 21.2,
                                           'temp4': 21.2,
                                           'temp5': 0.0,
                                           'time': datetime.datetime(2025, 3, 26, 15, 36, 55),
                                           'time_total': 3055520.5,
                                           'tlx_bean': None,
                                           'total_working_time': 0.0,
                                           'uw_sys_work_mode': 0,
                                           'vac1': 233.4,
                                           'vac2': 0.0,
                                           'vac3': 0.0,
                                           'vac_rs': 233.4,
                                           'vac_st': 0.0,
                                           'vac_tr': 0.0,
                                           'vacr': 0.0,
                                           'vacrs': 0.0,
                                           'vpv1': 28.8,
                                           'vpv2': 10.1,
                                           'vpv3': 0.0,
                                           'vpv4': 0.0,
                                           'warn_code': 220,
                                           'warn_code1': 2,
                                           'warn_text': 'Unknown',
                                           'win_mode': 0,
                                           'win_off_grid_soc': 0.0,
                                           'win_on_grid_soc': 0.0,
                                           'win_request': 0,
                                           'with_time': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

            WitEnergyV4
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

            SphsEnergyV4
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

            NoahEnergyV4
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

        device_type = self._device_type(device_type=device_type)

        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="new-api/queryLastData",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
            },
        )

        if device_type == DeviceType.INVERTER:
            return InverterEnergyV4.model_validate(response)
        elif device_type == DeviceType.STORAGE:
            return StorageEnergyV4.model_validate(response)
        elif device_type == DeviceType.MAX:
            return MaxEnergyV4.model_validate(response)
        elif device_type == DeviceType.SPH:
            return SphEnergyV4.model_validate(response)
        elif device_type == DeviceType.SPA:
            return SpaEnergyV4.model_validate(response)
        elif device_type == DeviceType.MIN:
            return MinEnergyV4.model_validate(response)
        elif device_type == DeviceType.WIT:
            return WitEnergyV4.model_validate(response)
        elif device_type == DeviceType.SPHS:
            return SphsEnergyV4.model_validate(response)
        elif device_type == DeviceType.NOAH:
            logger.warning(
                "NOAH documentation in missing/incomplete in API docs. A real device would be needed for finding correct attributes"
            )
            logger.warning("please send following output to a developer:")
            logger.warning(f"NOAH energy dump:\n{response}")
            return NoahEnergyV4.model_validate(response)
        else:
            raise ValueError(f"Unknown device type: {device_type}")

    def energy_history(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        device_type: Union[DeviceType, DeviceTypeStr],
        date_: Optional[datetime.date] = None,
    ) -> Union[
        InverterEnergyHistoryV4,
        StorageEnergyHistoryV4,
        SphEnergyHistoryV4,
        MaxEnergyHistoryV4,
        SpaEnergyHistoryV4,
        MinEnergyHistoryV4,
        WitEnergyHistoryV4,
        SphsEnergyHistoryV4,
        NoahEnergyHistoryV4,
    ]:
        """
        One day data
        Retrieves all detailed data for a specific device on a particular day based on the device SN, device type, and date.
        The interface returns data only for devices that the secret token has permission to access.
        Information for devices without permission will not be returned.
        https://www.showdoc.com.cn/2540838290984246/11292916022305414

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (str): Device unique serial number (SN)
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list())
            date_ (Optional[date]): Start Date - defaults to today

        Returns:
            Union[InverterEnergyHistoryV4, StorageEnergyHistoryV4, SphEnergyHistoryV4, MaxEnergyHistoryV4, SpaEnergyHistoryV4, MinEnergyHistoryV4, WitEnergyHistoryV4, SphsEnergyHistoryV4, NoahEnergyHistoryV4]

            {   'data': {   'datas': [   {
                                             <see energy() for attributes>
                                         }],
                            'have_next': False,
                            'start': 0},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

        """

        device_type = self._device_type(device_type=device_type)

        date_ = date_ or datetime.date.today()

        response = self.session.post(
            endpoint="new-api/queryHistoricalData",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
                "date": date_.strftime("%Y-%m-%d"),
            },
        )

        if device_type == DeviceType.INVERTER:
            return InverterEnergyHistoryV4.model_validate(response)
        elif device_type == DeviceType.STORAGE:
            return StorageEnergyHistoryV4.model_validate(response)
        elif device_type == DeviceType.MAX:
            return MaxEnergyHistoryV4.model_validate(response)
        elif device_type == DeviceType.SPH:
            return SphEnergyHistoryV4.model_validate(response)
        elif device_type == DeviceType.SPA:
            return SpaEnergyHistoryV4.model_validate(response)
        elif device_type == DeviceType.MIN:
            return MinEnergyHistoryV4.model_validate(response)
        elif device_type == DeviceType.WIT:
            return WitEnergyHistoryV4.model_validate(response)
        elif device_type == DeviceType.SPHS:
            return SphsEnergyHistoryV4.model_validate(response)
        elif device_type == DeviceType.NOAH:
            logger.warning(
                "NOAH documentation in missing/incomplete in API docs. A real device would be needed for finding correct attributes"
            )
            logger.warning("please send following output to a developer:")
            logger.warning(f"NOAH energy history dump:\n{response}")
            return NoahEnergyHistoryV4.model_validate(response)
        else:
            raise ValueError(f"Unknown device type: {device_type}")

    def energy_history_multiple(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: Union[str, List[str]],
        device_type: Union[DeviceType, DeviceTypeStr],
        date_: Optional[datetime.date] = None,
    ) -> Union[
        InverterEnergyHistoryMultipleV4,
        StorageEnergyHistoryMultipleV4,
        SphEnergyHistoryMultipleV4,
        MaxEnergyHistoryMultipleV4,
        SpaEnergyHistoryMultipleV4,
        MinEnergyHistoryMultipleV4,
        WitEnergyHistoryMultipleV4,
        SphsEnergyHistoryMultipleV4,
        NoahEnergyHistoryMultipleV4,
    ]:
        """
        One day data
        Retrieves all detailed data for a specific device on a particular day based on the device SN, device type, and date.
        The interface returns data only for devices that the secret token has permission to access.
        Information for devices without permission will not be returned.
        https://www.showdoc.com.cn/2540838290984246/11292916022305414

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list())
            date_ (Optional[date]): Start Date - defaults to today

        Returns:
            Union[InverterEnergyHistoryMultipleV4, ...]

            {   'data': {   'NHB691514F': [   {
                                                  <see energy() for attributes>
                                              }]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

        """

        device_type = self._device_type(device_type=device_type)

        date_ = date_ or datetime.date.today()

        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="new-api/queryDevicesHistoricalData",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
                "date": date_.strftime("%Y-%m-%d"),
            },
        )

        if device_type == DeviceType.INVERTER:
            return InverterEnergyHistoryMultipleV4.model_validate(response)
        elif device_type == DeviceType.STORAGE:
            return StorageEnergyHistoryMultipleV4.model_validate(response)
        elif device_type == DeviceType.MAX:
            return MaxEnergyHistoryMultipleV4.model_validate(response)
        elif device_type == DeviceType.SPH:
            return SphEnergyHistoryMultipleV4.model_validate(response)
        elif device_type == DeviceType.SPA:
            return SpaEnergyHistoryMultipleV4.model_validate(response)
        elif device_type == DeviceType.MIN:
            return MinEnergyHistoryMultipleV4.model_validate(response)
        elif device_type == DeviceType.WIT:
            return WitEnergyHistoryMultipleV4.model_validate(response)
        elif device_type == DeviceType.SPHS:
            return SphsEnergyHistoryMultipleV4.model_validate(response)
        elif device_type == DeviceType.NOAH:
            logger.warning(
                "NOAH documentation in missing/incomplete in API docs. A real device would be needed for finding correct attributes"
            )
            logger.warning("please send following output to a developer:")
            logger.warning(f"NOAH energy history dump:\n{response}")
            return NoahEnergyHistoryMultipleV4.model_validate(response)
        else:
            raise ValueError(f"Unknown device type: {device_type}")

    def setting_write_on_off(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        device_type: Union[DeviceType, DeviceTypeStr],
        power_on: bool,
    ) -> SettingWriteV4:
        """
        Set the power on and off
        Turn device on/off
        The interface returns data only for devices that the secret token has permission to access.
        Information for devices without permission will not be returned.
        https://www.showdoc.com.cn/2540838290984246/11330750679726415

        Note:
        * Noah type devices do not support power on/off settings

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list())
            power_on (bool): True = Power On, False = Power Off

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        device_type = self._device_type(device_type=device_type)

        if device_type == DeviceType.NOAH:
            raise AttributeError("NOAH devices do not support power on/off setting")

        if power_on:
            value = 1
            log_txt = "on"
        else:
            value = 0
            log_txt = "off"

        logger.info(f"Turning {device_type.name} device '{device_sn}' {log_txt}")
        response = self.session.post(
            endpoint="new-api/setOnOrOff",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
                "value": value,
            },
        )

        return SettingWriteV4.model_validate(response)

    def setting_write_active_power(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        device_type: Union[DeviceType, DeviceTypeStr],
        active_power: int,
    ) -> SettingWriteV4:
        """
        Set the active power
        Set the active power percentage of the device based on the device type and SN of the device.
        The interface returns data only for devices that the secret token has permission to access.
        Information for devices without permission will not be returned.
        https://www.showdoc.com.cn/2540838290984246/11330751643769012

        Note:
        * most devices can be configured to 0 ~ 100 %
        * NOAH devices can be configured to 0 ~ 800 W

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list())
            active_power (int): Percentage of active power, range 0-100 --- NOAH device is set to power (range 0-800W, unit W)

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        device_type = self._device_type(device_type=device_type)

        active_power = int(active_power)
        if device_type == DeviceType.NOAH:
            assert 0 <= active_power <= 800, "NOAH devices can be configured to 0 ~ 800 W"
            logger.info(f"Setting {device_type} device '{device_sn}' power to {active_power} W")
        else:
            assert 0 <= active_power <= 100, "active power must be in range 0 ~ 100 %"
            logger.info(f"Setting {device_type} device '{device_sn}' active power to {active_power} %")

        response = self.session.post(
            endpoint="new-api/setPower",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
                "value": active_power,
            },
        )

        return SettingWriteV4.model_validate(response)

    def setting_write_soc_upper_limit(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        device_type: Union[DeviceType, DeviceTypeStr],
        soc_limit: int,
    ) -> SettingWriteV4:
        """
        Set the upper limit of the discharge SOC
        Set the upper limit of the discharge SOC of the device based on the device type noah and the SN of the device.
        The interface returns data only for devices that the secret token has permission to access.
        Information for devices without permission will not be returned.
        https://www.showdoc.com.cn/2540838290984246/11330751904512654

        Note:
        * This API is only applicable to NOAH device type

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list()) -- This API is only applicable to NOAH device type
            soc_limit (int): discharge SOC upper limit, range 0-100, range 0-100 %

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        device_type = self._device_type(device_type=device_type)

        soc_limit = int(soc_limit)
        if device_type != DeviceType.NOAH:
            raise AttributeError("This API is only applicable to NOAH device type")

        logger.info(f"Setting {device_type} device '{device_sn}' SOC discharge upper limit to {soc_limit} %")

        response = self.session.post(
            endpoint="new-api/setHighLimitSoc",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
                "value": soc_limit,
            },
        )

        return SettingWriteV4.model_validate(response)

    def setting_write_soc_lower_limit(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        device_type: Union[DeviceType, DeviceTypeStr],
        soc_limit: int,
    ) -> SettingWriteV4:
        """
        Set the lower discharge SOC limit
        Set the lower discharge SOC limit of the device based on the device type noah and the SN of the device.
        The interface returns data only for devices that the secret token has permission to access.
        Information for devices without permission will not be returned.
        https://www.showdoc.com.cn/2540838290984246/11330752473301776

        Note:
        * This API is only applicable to NOAH device type

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list()) -- This API is only applicable to NOAH device type
            soc_limit (int): discharge SOC lower limit, range 0-100, range 0-100 %

        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        device_type = self._device_type(device_type=device_type)

        if device_type != DeviceType.NOAH:
            raise AttributeError("This API is only applicable to NOAH device type")

        soc_limit = int(soc_limit)

        logger.info(f"Setting {device_type} device '{device_sn}' SOC discharge lower limit to {soc_limit} %")

        response = self.session.post(
            endpoint="new-api/setLowLimitSoc",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
                "value": soc_limit,
            },
        )

        return SettingWriteV4.model_validate(response)

    def setting_write_time_period(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        device_type: Union[DeviceType, DeviceTypeStr],
        time_period_nr: int,
        start_time: datetime.time,
        end_time: datetime.time,
        load_priority: bool,
        power_watt: int,
        enabled: bool,
    ) -> SettingWriteV4:
        """
        Set the time period and mode
        Set the time period and machine mode of the device based on the device type noah and the SN of the device.
        The interface returns data only for devices that the secret token has permission to access.
        Information for devices without permission will not be returned.
        https://www.showdoc.com.cn/2540838290984246/11330752683972660

        Note:
        * This API is only applicable to NOAH device type

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list()) -- This API is only applicable to NOAH device type
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

        device_type = self._device_type(device_type=device_type)

        if device_type != DeviceType.NOAH:
            raise AttributeError("This API is only applicable to NOAH device type")

        time_period_nr = int(time_period_nr)
        assert 1 <= time_period_nr <= 9, "Time period number must be in range 1 ~ 9"
        assert start_time <= end_time, "Start time must be before end time"
        assert 0 <= power_watt <= 800, "Output power must be in range 0 ~ 800 W"

        if enabled:
            enable = 1
            log_txt = "Enabling"
        else:
            enable = 0
            log_txt = "Disabling"
        log_txt += f" {device_type} device '{device_sn}' time period {time_period_nr} from {start_time} to {end_time} with {power_watt} W"
        if load_priority:
            mode = 1
            log_txt += " (load priority)"
        else:
            mode = 0
            log_txt += " (battery priority)"

        response = self.session.post(
            endpoint="new-api/setTimeSegment",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
                "type": time_period_nr,
                "startTime": start_time.strftime("%H:%M"),
                "endTime": end_time.strftime("%H:%M"),
                "mode": mode,
                "power": power_watt,
                "enable": enable,
            },
        )

        return SettingWriteV4.model_validate(response)

    def setting_read_vpp_param(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        device_type: Union[DeviceType, DeviceTypeStr],
        parameter_id: str,
    ) -> SettingReadVppV4:
        """
        Read VPP parameters
        Read the VPP related parameters of the device according to the SN of the device.
        The interface returns data only for devices that the secret token has permission to access.
        The device without permission will not be read and the results will not be returned.
        https://www.showdoc.com.cn/2598832417617967/11558629942271434

        Note:
        * The current interface only supports sph, spa, min, wit device types.
          The specific models are as follows:
          * SPH 3000-6000TL BL
          * SPH 3000-6000TL BL US
          * SPH 4000-10000TL3 BH
          * SPA 1000-3000TL BL
          * SPA 4000-10000TL3 BH
          * MIN 2500-6000TL-XH US
          * MIN 2500-6000TL-XH
          * MOD-XH/MID-XH
          * WIT 100KTL3-H
          * WIS 215KTL3

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Allowed/known values for parameter_id:
          see self.setting_write_vpp_param()

        Args:
            device_sn (str): Inverter serial number
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list())
            parameter_id (str): Set parameter enumeration, example: set_param_1


        Returns:
            SettingReadVppV4

            {   'data': 0,
                'error_code': 0,
                'error_msg': 'success'}

        """

        device_type = self._device_type(device_type=device_type)

        assert parameter_id.startswith("set_param_"), "parameter_id must start with 'set_param_'"
        assert parameter_id[10:].isdigit(), "parameter_id must be followed by a number"

        response = self.session.post(
            endpoint="new-api/readVppParameter",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
                "setType": parameter_id,
            },
        )

        return SettingReadVppV4.model_validate(response)

    def setting_write_vpp_param(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        device_sn: str,
        device_type: Union[DeviceType, DeviceTypeStr],
        parameter_id: str,
        value: Union[int, str],
    ) -> SettingWriteV4:
        """
        VPP related parameter settings
        Set the VPP related parameters of the device according to the SN of the device.
        The interface returns data only for devices that the secret token has permission to access.
        The device without permission will not be read and the results will not be returned.
        https://www.showdoc.com.cn/2598832417617967/11558385202215329

        Note:
        * The current interface only supports sph, spa, min, wit device types.
          The specific models are as follows:
          * SPH 3000-6000TL BL
          * SPA 1000-3000TL BL
          * SPH 3000-6000TL BL US
          * SPH 4000-10000TL3 BH
          * SPA 4000-10000TL3 BH
          * MIN 2500-6000TL-XH US
          * MIN 2500-6000TL-XH
          * MOD-XH/MID-XH
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
            device_type (Union[DeviceType, DeviceTypeStr]): Device type (as returned by list())
            parameter_id (str): Set parameter enumeration, example: set_param_1
            value (Union[int, str]): the parameter value set, example:value


        Returns:
            SettingWriteV4

            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        device_type = self._device_type(device_type=device_type)

        assert parameter_id.startswith("set_param_"), "parameter_id must start with 'set_param_'"
        assert parameter_id[10:].isdigit(), "parameter_id must be followed by a number"

        response = self.session.post(
            endpoint="new-api/setVppParameter",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type.value,
                "setType": parameter_id,
                "value": str(value),
            },
        )

        return SettingWriteV4.model_validate(response)
