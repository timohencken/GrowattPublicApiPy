from datetime import date, timedelta
from typing import Optional

import truststore

from pydantic_models.storage import (
    StorageSettingRead,
    StorageSettingWrite,
    StorageDetails,
    StorageEnergyOverview,
    StorageEnergyHistory,
    StorageAlarms,
)

truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


class Storage:
    """
    https://www.showdoc.com.cn/262556420217021/6119502268976860
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def setting_read(
        self,
        device_sn: str,
        parameter_id: Optional[str] = None,
        start_address: Optional[int] = None,
        end_address: Optional[int] = None,
    ) -> StorageSettingRead:
        """
        Read energy storage machine setting parameter interface
        https://www.showdoc.com.cn/262556420217021/6119793934974232

        Note:
            Only applicable to devices with device type 2 (storage) returned by device.list()

        This method allows to read
        * predefined settings
          * pass parameter_id, do not pass start_address or end_address
        * any register value
          * pass start_address and end_address, do not pass parameter_id
        see setting_write() for more details

        Specific error codes:
        * 10001: Reading failed
        * 10002: Device does not exist
        * 10003: Device offline
        * 10004: Collector serial number is empty
        * 10005: Collector offline
        * 10006: Collector type does not support reading Get function
        * 10007: The collector version does not support the reading function
        * 10008: The collector connects to the server error, please restart and try again
        * 10009: The read setting parameter type does not exist

        Args:
            device_sn (str): energy storage machine SN
            parameter_id (Optional[str]): parameter ID - specify either parameter_id ort start/end_address
            start_address (Optional[int]): register address to start reading from - specify either parameter_id ort start/end_address
            end_address (Optional[int]): register address to stop reading at

        Returns:
            StorageSettingRead
            e.g.
            {
                "data": "0",
                "error_code": 0,
                "error_msg": ""
            }
        """

        if parameter_id is None and start_address is None:
            raise ValueError("specify either parameter_id or start_address/end_address")
        elif parameter_id is not None and start_address is not None:
            raise ValueError("specify either parameter_id or start_address/end_address - not both.")
        elif parameter_id is not None:
            # named parameter
            start_address = 0
            end_address = 0
        else:
            # using register-number mode
            parameter_id = "set_any_reg"
            if start_address is None:
                start_address = end_address
            if end_address is None:
                end_address = start_address

        response = self.session.post(
            endpoint="readStorageParam",
            data={
                "device_sn": device_sn,
                "paramId": parameter_id,
                "startAddr": start_address,
                "endAddr": end_address,
            },
        )

        inv_setting_response = StorageSettingRead.model_validate(response)
        if inv_setting_response.error_code == 10002:
            inv_setting_response.error_msg += " (or type != 2 - check with device.list())"

        return inv_setting_response

    def setting_write(
        self,
        device_sn: str,
        parameter_id: str,
        parameter_value_1: str,
        parameter_value_2: Optional[str] = None,
        parameter_value_3: Optional[str] = None,
        parameter_value_4: Optional[str] = None,
    ) -> StorageSettingWrite:
        """
        Energy storage machine parameter setting
        Interface for parameter setting of energy storage machine
        https://www.showdoc.com.cn/262556420217021/6119502268976860

        Note:
            Only applicable to devices with device type 2 (storage) returned by device.list()

        This method allows to set
        * predefined settings (see table below)
        * any register value (see table below for most relevant settings, google for "Growatt Inverter Modbus RTU Protocol V1.20" for more)

        Predefined settings
        ========================+=======================================+=======================+============================================================================
        description             | parameter_id                          | parameter_value_[n]   | comment
        ========================+=======================================+=======================+============================================================================
        switch machine          | storage_cmd_on_off                    |[1]: 0000 or 0001      | 0 = Turn off and not automatically connect to the grid next time
                                |                                       |                       | 1 = Turn on and automatically connect to the grid next time
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------
        System mode             | storage_cmd_mode                      |[1]: 0 or 1            | 0 = Standard mode, 1 = Free mode
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------
        forced discharge enable | storage_cmd_forced_discharge_enable   |[1]: 0 or 1            | 0 = enable, 1 = disable
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------
        Lithium battery SOC     | storage_lithium_battery               |[1]: 0 ~ 10            |
         lower limit setting    |                                       |                       |
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------
        SP string voltage       | pv_power_factor                       |[1]: 300 ~ 500         | [1]: Open circuit voltage
                                |                                       |[2]: 0.55 ~ 0.9        | [2]: MPP voltage (fraction of open circuit voltage)
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------
        forced discharge        | storage_cmd_forced_discharge_time1    |[1]: 0 ~ 24            |
         time period            |                                       |[2]: 0 ~ 59            |
                                |                                       |[3]: 0 ~ 24            |
                                |                                       |[4]: 0 ~ 59            |
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------
        Set energy storage      | storage_cmd_sys_year                  |[1]: YYYYY-MM-DD hh:mm |
         machine time           |                                       |                       |
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------
        charge enable           | storage_ac_charge_enable_disenable    |[1]: 0 or 1            | 0 = disable, 1 = enable
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------
        Charging time period    | storage_ac_charge_hour_start          |[1]: 0 ~ 24            |
         time period            |                                       |[2]: 0 ~ 59            |
                                |                                       |[3]: 0 ~ 24            |
                                |                                       |[4]: 0 ~ 59            |
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------
        Rechargeable battery    | storage_ac_charge_soc_limit           |[1]: 10 ~ 80           | unit: %
         SOC setting            |                                       |                       |
        ------------------------+---------------------------------------+-----------------------+----------------------------------------------------------------------------

        Register settings
        =================
        google for "Growatt Inverter Modbus RTU Protocol V1.20" for more

        Specific error codes:
        * 10001: system error
        * 10002: energy storage machine server error
        * 10003: energy storage machine offline
        * 10004: energy storage machine serial number is empty
        * 10005: collector offline
        * 10006: The setting parameter type does not exist
        * 10007: the parameter value is empty
        * 10008: the parameter value is not within the range
        * 10009: the date and time format is wrong
        * 10012: the energy storage machine does not exist
        * 10013: the end time cannot be less than the start time

        Args:
            device_sn (str): energy storage machine SN
            parameter_id (str): parameter ID - pass "set_any_reg" to write register address
            parameter_value_1 (str): parameter value 1
            parameter_value_2 (Optional[str]): parameter value 2
            parameter_value_3 (Optional[str]): parameter value 3
            parameter_value_4 (Optional[str]): parameter value 4

        Returns:
            StorageSettingWrite
            e.g. (success)
            {
                "data": "",
                "error_code": 0,
                "error_msg": ""
            }
        """
        if parameter_id == "set_any_reg":
            assert parameter_value_1 is not None, "register address must be provided"
            assert parameter_value_2 is not None, "new value must be provided"
            assert parameter_value_3 is None, "parameter 3 must not be used for set_any_reg"
            assert parameter_value_4 is None, "parameter 4 must not be used for set_any_reg"
        else:
            assert parameter_value_1 is not None, "new value must be provided"

        # API docs: if there is no value, pass empty string ""
        if parameter_value_2 is None:
            parameter_value_2 = ""
        if parameter_value_3 is None:
            parameter_value_3 = ""
        if parameter_value_4 is None:
            parameter_value_4 = ""

        # parameter values must be string
        parameter_value_1 = str(parameter_value_1)
        parameter_value_2 = str(parameter_value_2)
        parameter_value_3 = str(parameter_value_3)
        parameter_value_4 = str(parameter_value_4)

        response = self.session.post(
            endpoint="storageSet",
            data={
                "storage_sn": device_sn,
                "type": parameter_id,
                "param1": parameter_value_1,
                "param2": parameter_value_2,
                "param3": parameter_value_3,
                "param4": parameter_value_4,
            },
        )

        inv_setting_response = StorageSettingWrite.model_validate(response)
        if inv_setting_response.error_code == 10012:
            inv_setting_response.error_msg += " (or type != 2 - check with device.list())"

        return inv_setting_response

    def details(
        self,
        device_sn: str,
    ) -> StorageDetails:
        """
        Get basic information of energy storage machine
        Get basic information interface of energy storage machine
        https://www.showdoc.com.cn/262556420217021/6119506364286651

        Note:
            Only applicable to devices with device type 2 (storage) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Args:
            device_sn (str): energy storage machine SN

        Returns:
            StorageDetails
            e.g.
            {'data': {'ac_in_model': 0.0,
                      'address': 1,
                      'alias': '2',
                      'b_light_en': 0,
                      'bat_low_to_uti_volt': 0.0,
                      'battery_type': 0,
                      'bulk_charge_volt': 0.0,
                      'buzzer_en': 0,
                      'charge_config': 0,
                      'children': [],
                      'communication_version': None,
                      'datalogger_sn': 'IUB38210F9',
                      'device_type': 1,
                      'float_charge_volt': 0.0,
                      'fw_version': 'FA1.0',
                      'group_id': -1,
                      'img_path': './css/img/status_yellow.gif',
                      'inner_version': 'fbaa1816',
                      'last_update_time': {'date': 14,
                                           'day': 1,
                                           'hours': 14,
                                           'minutes': 35,
                                           'month': 0,
                                           'seconds': 57,
                                           'time': 1547447757000,
                                           'timezone_offset': -480,
                                           'year': 119},
                      'last_update_time_text': datetime.datetime(2019, 1, 14, 14, 35, 57),
                      'level': 4,
                      'location': None,
                      'lost': False,
                      'manual_start_en': 0.0,
                      'max_charge_curr': 0.0,
                      'model': 1191936,
                      'model_text': 'A0B0D1T2P3U0M0S0',
                      'output_config': 0.0,
                      'output_freq_type': 0.0,
                      'output_volt_type': 0.0,
                      'over_load_restart': 0.0,
                      'over_temp_restart': 0.0,
                      'p_charge': 0.0,
                      'p_discharge': 0.0,
                      'parent_id': 'LIST_IUB38210F9_96',
                      'plant_id': 0,
                      'plant_name': None,
                      'port_name': None,
                      'pow_saving_en': 0.0,
                      'pv_model': 0.0,
                      'rate_va': 0.0,
                      'rate_watt': 0.0,
                      'record': None,
                      'sci_loss_chk_en': 0.0,
                      'serial_num': 'JZB674901B',
                      'status': 0,
                      'status_led1': False,
                      'status_led2': True,
                      'status_led3': True,
                      'status_led4': False,
                      'status_led5': False,
                      'status_led6': True,
                      'status_text': 'storage.status.operating',
                      'sys_time': None,
                      'tcp_server_ip': '47.254.154.60',
                      'tree_id': 'ST_JZB674901B',
                      'tree_name': '2',
                      'updating': False,
                      'user_name': None,
                      'uti_charge_end': 0.0,
                      'uti_charge_start': 0.0,
                      'uti_out_end': 0.0,
                      'uti_out_start': 0.0,
                      'uw_bat_type2': 0},
             'datalogger_sn': 'IUB38210F9',
             'device_sn': 'JZB674901B',
             'error_code': 0,
             'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/storage/storage_data_info",
            params={
                "device_sn": device_sn,
            },
        )

        return StorageDetails.model_validate(response)

    def energy(
        self,
        device_sn: str,
    ) -> StorageEnergyOverview:
        """
        Get the latest real-time data of the energy storag
        Interface to get the latest real-time data of energy storage machine
        https://www.showdoc.com.cn/262556420217021/6119678224369391

        Note:
            Only applicable to devices with device type 2 (storage) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Args:
            device_sn (str): Inverter serial number

        Returns:
            StorageEnergyOverview
            e.g.
            {   'data': {   'address': 0,
                            'again': False,
                            'alias': None,
                            'b_light_en': 0.0,
                            'bat_temp': 43.0,
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
                            'bms_soh': 0.0,
                            'bms_status': 0,
                            'bms_status2': 0,
                            'bms_temperature': 0.0,
                            'bms_temperature2': 0.0,
                            'bms_warn_info': 0,
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 14, 'day': 1, 'hours': 13, 'minutes': 20, 'month': 0, 'seconds': 57, 'time': 1547443257000, 'timezone_offset': -480, 'year': 119},
                                            'time_in_millis': 1547443257000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2019,
                                            'weeks_in_week_year': 52},
                            'capacity': 52.0,
                            'capacity_text': '52 %',
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
                            'charge_month': 0.0,
                            'charge_to_standby_reason': 5,
                            'charge_to_standby_reason_text': 'Reason of state change from charge to operating: Battery voltage high for charge',
                            'charge_way': 0,
                            'chg_curr': 0.0,
                            'constant_volt': 0.0,
                            'constant_volt2': 0.0,
                            'cycle_count': 0,
                            'cycle_count2': 0,
                            'datalogger_sn': None,
                            'day': None,
                            'day_map': None,
                            'delta_volt': 0.0,
                            'delta_volt2': 0.0,
                            'device_type': 0,
                            'discharge_curr': 0.0,
                            'discharge_month': 0.0,
                            'discharge_to_standby_reason': 5,
                            'discharge_to_standby_reason_text': 'Reason of state change from discharge to operating: Battery voltage low for discharge',
                            'e_bat_discharge_today': 0.0,
                            'e_bat_discharge_total': 0.0,
                            'e_charge_today': 0.0,
                            'e_charge_today2': 0.0,
                            'e_charge_today_text': '0.0 kWh',
                            'e_charge_total': 2.3,
                            'e_charge_total2': 2.6,
                            'e_charge_total_text': '2.3 kWh',
                            'e_discharge_today': 0.0,
                            'e_discharge_today2': 0.0,
                            'e_discharge_today_text': '0.0 kWh',
                            'e_discharge_total': 1.7,
                            'e_discharge_total2': 1.7,
                            'e_discharge_total_text': '1.7 kWh',
                            'e_to_grid_today': 0.0,
                            'e_to_grid_total': 7648481.6,
                            'e_to_user_today': 6.0,
                            'e_to_user_total': 24137119.8,
                            'e_today': 6.5,
                            'e_total': 1049.6000000000001,
                            'eac_charge_today': 0.0,
                            'eac_charge_total': 2.1,
                            'eac_discharge_today': 0.0,
                            'eac_discharge_total': 0.0,
                            'eop_discharge_today': 0.0,
                            'eop_discharge_total': 0.0,
                            'epv_today': 3.3,
                            'epv_today2': 3.2,
                            'epv_total': 539.6,
                            'epv_total2': 511.5,
                            'error_code': 0,
                            'error_text': 'Unknown',
                            'fault_code': 0,
                            'freq_grid': 0.0,
                            'freq_output': 0.0,
                            'gauge2_rm1': 0.0,
                            'gauge2_rm2': 0.0,
                            'gauge_battery_status': 0,
                            'gauge_ic_current': 0.0,
                            'gauge_operation_status': 0,
                            'gauge_pack_status': 0,
                            'gauge_rm1': 0.0,
                            'gauge_rm2': 0.0,
                            'i_ac_charge': 0.0,
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
                            'inner_cw_code': '0_0',
                            'ipm_temperature': 39.900001525878906,
                            'ipv': 0.0,
                            'ipv_text': '0.0 A',
                            'load_percent': 0.0,
                            'lost': True,
                            'manual_start_en': 0.0,
                            'max_charge_or_discharge_current': 0.0,
                            'max_charge_or_discharge_current2': 0.0,
                            'normal_power': 0,
                            'output_current': 0.0,
                            'output_power': 0.0,
                            'output_volt': 0.0,
                            'p_ac_charge': 0.0,
                            'p_ac_input': 0.0,
                            'p_bat': 0.0,
                            'p_charge': 0.0,
                            'p_charge2': 0.0,
                            'p_charge_text': '0.0 W',
                            'p_discharge': 0.0,
                            'p_discharge2': 0.0,
                            'p_discharge_text': '0.0 W',
                            'pac_to_grid': 0.0,
                            'pac_to_grid_text': '0.0 W',
                            'pac_to_user': 1922.9,
                            'pac_touser_text': None,
                            'pow_saving_en': 0.0,
                            'ppv': 1075.4,
                            'ppv2': 991.7,
                            'ppv_text': '1075.4 W',
                            'rate_va': 0.0,
                            'rate_watt': 0.0,
                            'remote_cntl_en': 0.0,
                            'remote_cntl_fail_reason': 0,
                            'sci_loss_chk_en': 0.0,
                            'serial_num': 'JZB674901B',
                            'soh': 0.0,
                            'soh2': 0.0,
                            'status': 0,
                            'status_text': 'Operating',
                            'storage_bean': None,
                            'sys_out': 2067.1000000000004,
                            'temperature': 39.79999923706055,
                            'time': datetime.datetime(2019, 1, 14, 13, 20, 57),
                            'uw_bat_type2': 0.0,
                            'v_bat': 50.20000076293945,
                            'v_bat_text': '50.2 V',
                            'v_buck': 161.39999389648438,
                            'v_buck2': 167.3000030517578,
                            'v_buck_text': '161.4 V',
                            'v_bus': 171.6999969482422,
                            'v_grid': 0.0,
                            'vac': 226.5,
                            'vac_Text': '226.5 V',
                            'vpv': 161.39999389648438,
                            'vpv2': 167.60000610351562,
                            'vpv_text': '161.4 V',
                            'warn_code': 0,
                            'warn_info': 0,
                            'warn_info2': 0,
                            'warn_text': 'Unknown',
                            'with_time': False},
                'datalogger_sn': 'IUB38210F9',
                'device_sn': 'JZB674901B',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/storage/storage_last_data",
            data={
                "storage_sn": device_sn,
            },
        )

        response_parsed = StorageEnergyOverview.model_validate(response)
        if response_parsed.error_code == 10002:
            response_parsed.error_msg += " (or type != 2 - check with device.list())"

        return response_parsed

    def energy_history(
        self,
        device_sn: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> StorageEnergyHistory:
        """
        Obtain historical data of an energy storage machin
        An interface for obtaining historical data of a certain energy storage machine
        https://www.showdoc.com.cn/262556420217021/6119692996848995

        Note:
            Only applicable to devices with device type 2 (storage) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10004: date interval exceeds seven days
        * 10005: energy storage machine does not exist

        Args:
            device_sn (str): Inverter serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            StorageEnergyHistory
            e.g.
            {   'data': {   'count': 289,
                            'datalogger_sn': 'IUB38210F9',
                            'datas': [   {   'address': 0,
                                             # ... see storage.energy() ...
                                             'with_time': False}],
                            'device_sn': 'JZB674901B',
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
            endpoint="device/storage/storage_data",
            data={
                "storage_sn": device_sn,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        response_parsed = StorageEnergyHistory.model_validate(response)
        if response_parsed.error_code == 10005:
            response_parsed.error_msg += " (or type != 2 - check with device.list())"

        return response_parsed

    def alarms(
        self,
        device_sn: str,
        date_: Optional[date] = None,
    ) -> StorageAlarms:
        """
        Get the alarm data of a certain energy storage mac
        Interface to obtain alarm data of a certain energy storage machine
        https://www.showdoc.com.cn/262556420217021/6119784080785951

        Note:
            Only applicable to devices with device type 2 (storage) returned by device.list()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10005: energy storage device does not exist

        Args:
            device_sn (str): Inverter serial number
            date_ (Optional[date]): Date - defaults to today

        Returns:
            StorageAlarms
            e.g.
            {
                'data': {
                    'alarms': [
                        {
                            'alarm_code': 3012,
                            'alarm_message': 'Battery temperature out of specified range for charge or discharge(range is settable),Check battery temperature',
                            'end_time': datetime.datetime(2019, 1, 13, 18, 18, 19),
                            'start_time': datetime.datetime(2019, 1, 13, 18, 18, 19),
                            'status': 1
                        }
                    ],
                    'count': 30,
                    'device_sn': None
                },
               'error_code': 0,
                'error_msg': None
            }
        """

        if date_ is None:
            date_ = date.today()

        response = self.session.post(
            endpoint="device/storage/alarm_data",
            data={
                "storage_sn": device_sn,
                "date": date_.strftime("%Y-%m-%d"),
            },
        )

        response_parsed = StorageAlarms.model_validate(response)
        if response_parsed.error_code == 10005:
            response_parsed.error_msg += " (or type != 2 - check with device.list())"

        return response_parsed
