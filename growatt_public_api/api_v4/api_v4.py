from typing import Optional, Literal, List, Union

import truststore

from pydantic_models.api_v4 import (
    DeviceListV4,
    InverterDetailsV4,
    StorageDetailsV4,
    MaxDetailsV4Max,
    SphDetailsV4,
    SpaDetailsV4,
    MinDetailsV4,
    WitDetailsV4,
    SphsDetailsV4,
    NoahDetailsV4,
)

truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


NEW_API_ERROR_CODES = {  # TODO use this for something?
    0: "Normal",
    1: "System Error",
    2: "Invalid Secret Token",
    3: "Device Permission Verification Failed",
    4: "Device Not Found",
    5: "Device Offline",
    6: "Failed to Set Parameters",
    7: "Device Type Error",
    8: "Device SN is Empty",
    9: "Date Cannot Be Empty",
    10: "Page Number Cannot Be Empty",
    11: "Device SN Exceeds Quantity Limit",
    12: "No Permission to Access Device",
    100: "API Access Interval",
    101: "No Permission to Access",
    102: "Access Frequency Limit, Different Interfaces Have Different Time Limits",
    -1: "Please Use the New Domain for Access",
}

DeviceType = Literal[
    "inv", "storage", "max", "sph", "spa", "min", "wit", "sph-s", "noah"
]


class ApiV4:
    """
    New API (v4)
    https://www.showdoc.com.cn/2540838290984246/11292912972201443
    """

    # TODO refactor - we do not want a v4 package (at least not external) - distribute to corresponding "device_type" packages

    # TODO v4 error codes
    # https://www.showdoc.com.cn/2540838290984246/11292913883034530

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session
        self.session.api_url = f"{self.session.server_url}/v4"  # FIXME - is this a good idea? or does it change the session object for v1 modules, too?

    def list(
        self,
        page: Optional[int] = None,
    ) -> DeviceListV4:
        """
        Device List
        Retrieve the list of devices associated with the distributor, installer, and terminal account of the secret token.
        The devices obtained through this interface are the only ones allowed to fetch data from.
        Devices not on the list are not permitted to retrieve data.
        https://www.showdoc.com.cn/2540838290984246/11292915113214428

        Returned "device_type" values are: (according to https://www.showdoc.com.cn/2540838290984246/11292914311318022 and https://www.showdoc.com.cn/p/b42ee029e131c68c4dbfdd89285c0ec1)
        * inv
        * storage
        * max
        * sph
        * spa
        * min
        * wit
        * sph-s
        * noah

        Rate limit(s):
        * Fetch frequency is limited to once every 5 seconds.

        Args:
            page (Optional[int]): Page number, default 1 (1~n)

        Returns:
            DeviceList
            {   'data': {   'count': 7,
                            'data': [   {'create_date': datetime.datetime(2021, 6, 29, 12, 2, 46), 'datalogger_sn': None, 'device_sn': 'HPJ0BF20FU', 'device_type': 'max'},
                                        {'create_date': datetime.datetime(2024, 11, 30, 17, 37, 26), 'datalogger_sn': 'QMN000BZP0000000', 'device_sn': 'BZP0000000', 'device_type': 'min'}
                                        {'create_date': datetime.datetime(2017, 1, 18, 14, 9, 53), 'datalogger_sn': None, 'device_sn': 'PR34211399', 'device_type': 'inv'}],
                            'last_pager': True,
                            'not_pager': False,
                            'other': None,
                            'page_size': 100,
                            'pages': 1,
                            'start_count': 0},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        response = self.session.post(
            endpoint="new-api/queryDeviceList",
            params={"page": page},
        )

        return DeviceListV4.model_validate(response)

    def details(  # noqa: C901 'ApiV4.details' is too complex (11)
        self,
        device_sn: Union[str, List[str]],
        device_type: DeviceType,
    ) -> Union[
        InverterDetailsV4,
        StorageDetailsV4,
        MaxDetailsV4Max,
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
            device_type (DeviceType): Device type (as returned by list())

        Returns:
            Union[InverterDetailsV4, StorageDetailsV4, MaxDetailsV4Max, SphDetailsV4, SpaDetailsV4, MinDetailsV4, WitDetailsV4, SphsDetailsV4, NoahDetailsV4]

            InverterDetailsV4:
            StorageDetailsV4:
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
                                               'ac_max_charge_curr': 30.0,
                                               'address': 1,
                                               'alias': '裁床照明+插座+大空调',
                                               'b_light_en': 0,
                                               'bat_low_to_uti_volt': 46.0,
                                               'battery_type': 0,
                                               'battery_undervoltage_cutoff_point': 42.0,
                                               'bulk_charge_volt': 56.4,
                                               'buzzer_en': 1,
                                               'charge_config': 0,
                                               'children': None,
                                               'communication_version': None,
                                               'datalogger_sn': 'DDD0CGA0CF',
                                               'device_type': 3,
                                               'dtc': 20105,
                                               'float_charge_volt': 54.0,
                                               'fw_version': '067.01/068.01',
                                               'group_id': -1,
                                               'img_path': './css/img/status_gray.gif',
                                               'inner_version': 'null',
                                               'last_update_time': 1716979679000,
                                               'last_update_time_text': datetime.datetime(2024, 5, 29, 18, 47, 59),
                                               'level': 4,
                                               'li_battery_protocol_type': 0,
                                               'location': None,
                                               'lost': True,
                                               'mains_to_battery_operat_point': 0.0,
                                               'manual_start_en': 0.0,
                                               'max_charge_curr': 1000.0,
                                               'model': 0,
                                               'model_text': 'A0B0D0T0P0U0M0S0',
                                               'output_config': 3.0,
                                               'output_freq_type': 0,
                                               'output_volt_type': 1,
                                               'over_load_restart': 1.0,
                                               'over_temp_restart': 1.0,
                                               'p_charge': 0.0,
                                               'p_discharge': 0.0,
                                               'parent_id': 'LIST_DDD0CGA0CF_96',
                                               'plant_id': 0,
                                               'plant_name': None,
                                               'port_name': None,
                                               'pow_saving_en': 0,
                                               'pv_model': 0,
                                               'rate_va': 5000.0,
                                               'rate_watt': 5000.0,
                                               'record': None,
                                               'sci_loss_chk_en': 0,
                                               'serial_num': 'JNK1CJM0GR',
                                               'status': 5,
                                               'status_led1': False,
                                               'status_led2': False,
                                               'status_led3': False,
                                               'status_led4': False,
                                               'status_led5': False,
                                               'status_led6': False,
                                               'status_text': 'inverter.status.lost',
                                               'sys_time': datetime.datetime(2024, 5, 29, 7, 57),
                                               'tcp_server_ip': '47.119.28.147',
                                               'timezone': 8.0,
                                               'tree_id': 'ST_JNK1CJM0GR',
                                               'tree_name': '裁床照明+插座+大空调',
                                               'updating': False,
                                               'user_name': None,
                                               'uti_charge_end': 0.0,
                                               'uti_charge_start': 0.0,
                                               'uti_out_end': 0.0,
                                               'uti_out_start': 0.0,
                                               'uw_bat_type2': 0,
                                               'uw_feed_en': 0,
                                               'uw_feed_range': 0.0,
                                               'uw_load_first': 0.0}]},
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

            MaxDetailsV4Max:

        """

        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="new-api/queryDeviceInfo",
            params={
                "deviceSn": device_sn,
                "deviceType": device_type,
            },
        )

        # FIXME DEBUG
        sample_data = """{
    "code": 0,
    "data": {
        "max": [
            {
                "id": 0,
                "serialNum": "HPJ0BF20FU",
                "bigDevice": false,
                "portName": "ShinePano - BLE4BEQ0BW",
                "dataLogSn": "BLE4BEQ0BW",
                "groupId": -1,
                "alias": "HPJ0BF20FU",
                "location": "",
                "addr": 1,
                "fwVersion": "TJ1.0",
                "model": 720575940631003386,
                "innerVersion": "TJAA08020002",
                "lost": false,
                "status": 1,
                "tcpServerIp": "47.119.22.101",
                "lastUpdateTime": 1716534733000,
                "normalPower": 25000,
                "power": 0.0,
                "communicationVersion": "ZBab-0002",
                "deviceType": 1,
                "eToday": 0.0,
                "eTotal": 0.0,
                "energyDayMap": {},
                "energyMonth": 0.0,
                "updating": false,
                "record": null,
                "energyDay": 0.0,
                "powerMax": null,
                "powerMaxTime": null,
                "userName": null,
                "plantId": 0,
                "plantname": null,
                "modelText": "S0AB00D00T00P0FU01M00FA",
                "timezone": 8.0,
                "sysTime": null,
                "onOff": 0,
                "activeRate": 0,
                "reactiveRate": 0,
                "pvPfCmdMemoryState": 0,
                "pf": 0.0,
                "exportLimit": 0,
                "exportLimitPowerRate": 0.0,
                "voltageHighLimit": 0.0,
                "voltageLowLimit": 0.0,
                "frequencyHighLimit": 0.0,
                "frequencyLowLimit": 0.0,
                "backflowDefaultPower": 0.0,
                "lcdLanguage": 0,
                "pfModel": 0,
                "pflinep1_lp": 0,
                "pflinep1_pf": 0.0,
                "pflinep2_lp": 0,
                "pflinep2_pf": 0.0,
                "pflinep3_lp": 0,
                "pflinep3_pf": 0.0,
                "pflinep4_lp": 0,
                "pflinep4_pf": 0.0,
                "strNum": 0,
                "vacLow": 0.0,
                "vacHigh": 0.0,
                "facLow": 0.0,
                "facHigh": 0.0,
                "maxSetBean": null,
                "dtc": 5001,
                "level": 6,
                "lastUpdateTimeText": "2024-05-24 15:12:13",
                "children": null,
                "treeName": "HPJ0BF20FU",
                "treeID": "HPJ0BF20FU",
                "parentID": "LIST_BLE4BEQ0BW_3",
                "imgPath": "./css/img/status_gray.gif",
                "statusText": "max.status.normal",
                "powerMaxText": "",
                "energyMonthText": "0"
            }
        ]
    },
    "message": "SUCCESSFUL_OPERATION"
}"""
        import json
        import pprint

        j = json.loads(sample_data)
        pprint.pprint(j, indent=4, width=500)
        k = SphDetailsV4.model_validate(j)  # <-----------------------------
        pprint.pprint(k.model_dump(), indent=4, width=500)
        # FIXME DEBUG

        device_type = device_type.lower()
        if device_type == "inv":
            return InverterDetailsV4.model_validate(response)
        elif device_type == "storage":
            return StorageDetailsV4.model_validate(response)
        elif device_type == "sph":
            return SphDetailsV4.model_validate(response)
        elif device_type == "max":  # TODO ongoing
            return MaxDetailsV4Max.model_validate(response)
        elif device_type == "spa":  # TODO
            return SpaDetailsV4.model_validate(response)
        elif device_type == "min":  # TODO
            return MinDetailsV4.model_validate(response)
        elif device_type == "wit":  # TODO
            return WitDetailsV4.model_validate(response)
        elif device_type == "sph-s":  # TODO
            return SphsDetailsV4.model_validate(response)
        elif device_type == "noah":  # TODO
            return NoahDetailsV4.model_validate(response)
        else:
            raise ValueError(f"Unknown device type: {device_type}")
