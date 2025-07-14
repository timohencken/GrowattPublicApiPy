from datetime import date, timedelta
from typing import Optional
from ..pydantic_models.smart_meter import (
    SmartMeterEnergyOverview,
    SmartMeterEnergyHistory,
)
from ..session import GrowattApiSession


class SmartMeter:
    """
    endpoints for Smart meters
    https://www.showdoc.com.cn/262556420217021/6131333103798986

    Note:
        Only applicable to devices with device type 3 (other) returned by plant.list_devices() - if device is a meter
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def energy(
        self,
        datalogger_sn: str,
        meter_address: int,
    ) -> SmartMeterEnergyOverview:
        """
        Obtain real-time data of smart meters according to
        Interface to obtain real-time data of smart meters according to the collector SN and smart meter addresses
        https://www.showdoc.com.cn/262556420217021/6131369504550249

        Note:
            Only applicable to devices with device type 3 (other) returned by plant.list_devices() - if device is a meter

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: collector SN error
        * 10003: device address is empty
        * 10004: collector does not exist

        Args:
            datalogger_sn (str): Serial number of the datalogger the meter is attached to
            meter_address (int): Address of the meter (see SmartMeter.list() output)

        Returns:
            SmartMeterEnergyOverview
            {   'data': {   'a_active_power': 0.0,
                            'a_current': 0.0,
                            'a_power_factor': 0.0,
                            'a_reactive_power': 0.0,
                            'a_voltage': 0.0,
                            'active_energy': 48.900001525878906,
                            'active_net_total_energy': None,
                            'active_power': 5589.60009765625,
                            'active_power_l1': 0.0,
                            'active_power_l2': 0.0,
                            'active_power_l3': 0.0,
                            'active_power_max_need': 0.0,
                            'active_power_max_need_one': 0.0,
                            'active_power_need': 0.0,
                            'active_power_need_one': 0.0,
                            'address': 1,
                            'again': None,
                            'alarm_Code': None,
                            'alias': None,
                            'apparent_energy': 0.0,
                            'apparent_energy_max_need': 0.0,
                            'apparent_energy_need': 0.0,
                            'apparent_power': 6025.5,
                            'apparent_power_l1': 0.0,
                            'apparent_power_l2': 0.0,
                            'apparent_power_l3': 0.0,
                            'b_active_power': 0.0,
                            'b_power_factor': 0.0,
                            'b_reactive_power': 0.0,
                            'c_active_power': 0.0,
                            'c_power_factor': 0.0,
                            'c_reactive_power': 0.0,
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 9, 'day': 3, 'hours': 15, 'minutes': 0, 'month': 0, 'seconds': 34, 'time': 1547017234000, 'timezone_offset': -480, 'year': 119},
                                            'time_in_millis': 1547017234000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2019,
                                            'weeks_in_week_year': 52},
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
                            'datalogger_sn': 'CRAZT00001',
                            'device_sn': None,
                            'ex_power_factor': None,
                            'fei_lv_bo_z_energy': 15.899999618530273,
                            'fei_lv_feng_z_energy': 10.199999809265137,
                            'fei_lv_gu_z_energy': 5.400000095367432,
                            'fei_lv_ping_z_energy': 6.5,
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
                            'lost': None,
                            'meter_dh': None,
                            'meter_ms': None,
                            'meter_ym': None,
                            'mode_status': None,
                            'month_energy': None,
                            'net_total_energy': None,
                            'posi_active_net_total_energy': None,
                            'posi_active_power': 0.0,
                            'posi_reactive_net_total_energy': None,
                            'posi_reactive_power': 0.0,
                            'positive_active_today_energy': None,
                            'positive_active_total_energy': 0.0,
                            'power_factor': 0.9991999864578247,
                            'power_factor_l1': 0.0,
                            'power_factor_l2': 0.0,
                            'power_factor_l3': 0.0,
                            'reactive_energy': 0.10000000149011612,
                            'reactive_net_total_energy': None,
                            'reactive_power': 168.89999389648438,
                            'reactive_power_l1': 0.0,
                            'reactive_power_l2': 0.0,
                            'reactive_power_l3': 0.0,
                            'reverse_active_energy': None,
                            'reverse_active_max_need': 0.0,
                            'reverse_active_need': 0.0,
                            'reverse_active_net_total_energy': None,
                            'reverse_active_power': 0.0,
                            'reverse_active_today_energy': None,
                            'reverse_active_total_energy': 0.0,
                            'reverse_apparent_energy': None,
                            'reverse_instant_total_active_power': None,
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
                            'time_text': datetime.datetime(2019, 1, 9, 15, 0, 34),
                            'today_energy': None,
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
                'datalogger_sn': 'CRAZT00001',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/ammeter/meter_last_data",
            params={
                "datalog_sn": datalogger_sn,
                "address": meter_address,
            },
        )

        return SmartMeterEnergyOverview.model_validate(response)

    def energy_history(
        self,
        datalogger_sn: str,
        meter_address: int,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> SmartMeterEnergyHistory:
        """
        Get historical data of a Pbd
        An interface to obtain historical data of a pbd
        https://www.showdoc.com.cn/262556420217021/6131319527296946

        Note:
            Only applicable to devices with device type 3 (other) returned by plant.list_devices() - if device is a meter

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: collector SN error
        * 10003: start date error
        * 10004: start date interval exceeds 7 days
        * 10005: device address is empty
        * 10006: collector does not exist

        Args:
            datalogger_sn (str): Serial number of the datalogger the meter is attached to
            meter_address (int): Address of the meter (see SmartMeter.list() output)
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            SmartMeterEnergyHistory
            {   'data': {   'count': 12,
                            'datalogger_sn': 'CRAZT00001',
                            'meter_data': [   {   'a_active_power': 0.0,
                                                  'a_current': 0.0,
                                                  'a_power_factor': 0.0,
                                                  'a_reactive_power': 0.0,
                                                  'a_voltage': 0.0,
                                                  'active_energy': 32.5,
                                                  'active_net_total_energy': None,
                                                  'active_power': 4886.5,
                                                  'active_power_l1': 0.0,
                                                  'active_power_l2': 0.0,
                                                  'active_power_l3': 0.0,
                                                  'active_power_max_need': 0.0,
                                                  'active_power_max_need_one': 0.0,
                                                  'active_power_need': 0.0,
                                                  'active_power_need_one': 0.0,
                                                  'address': 1,
                                                  'again': None,
                                                  'alarm_Code': None,
                                                  'alias': None,
                                                  'apparent_energy': 0.0,
                                                  'apparent_energy_max_need': 0.0,
                                                  'apparent_energy_need': 0.0,
                                                  'apparent_power': 5024.7998046875,
                                                  'apparent_power_l1': 0.0,
                                                  'apparent_power_l2': 0.0,
                                                  'apparent_power_l3': 0.0,
                                                  'b_active_power': 0.0,
                                                  'b_power_factor': 0.0,
                                                  'b_reactive_power': 0.0,
                                                  'c_active_power': 0.0,
                                                  'c_power_factor': 0.0,
                                                  'c_reactive_power': 0.0,
                                                  'calendar': {   'first_day_of_week': 1,
                                                                  'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                                  'lenient': True,
                                                                  'minimal_days_in_first_week': 1,
                                                                  'time': {'date': 13, 'day': 4, 'hours': 11, 'minutes': 3, 'month': 11, 'seconds': 52, 'time': 1544670232000, 'timezone_offset': -480, 'year': 118},
                                                                  'time_in_millis': 1544670232000,
                                                                  'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                                  'week_date_supported': True,
                                                                  'week_year': 2018,
                                                                  'weeks_in_week_year': 52},
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
                                                  'datalogger_sn': 'CRAZT00001',
                                                  'device_sn': None,
                                                  'ex_power_factor': None,
                                                  'fei_lv_bo_z_energy': 9.5,
                                                  'fei_lv_feng_z_energy': 6.800000190734863,
                                                  'fei_lv_gu_z_energy': 3.4000000953674316,
                                                  'fei_lv_ping_z_energy': 4.900000095367432,
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
                                                  'lost': None,
                                                  'meter_dh': None,
                                                  'meter_ms': None,
                                                  'meter_ym': None,
                                                  'mode_status': None,
                                                  'month_energy': None,
                                                  'net_total_energy': None,
                                                  'posi_active_net_total_energy': None,
                                                  'posi_active_power': 0.0,
                                                  'posi_reactive_net_total_energy': None,
                                                  'posi_reactive_power': 0.0,
                                                  'positive_active_today_energy': None,
                                                  'positive_active_total_energy': 0.0,
                                                  'power_factor': 0.9991999864578247,
                                                  'power_factor_l1': 0.0,
                                                  'power_factor_l2': 0.0,
                                                  'power_factor_l3': 0.0,
                                                  'reactive_energy': 0.10000000149011612,
                                                  'reactive_net_total_energy': None,
                                                  'reactive_power': 155.8000030517578,
                                                  'reactive_power_l1': 0.0,
                                                  'reactive_power_l2': 0.0,
                                                  'reactive_power_l3': 0.0,
                                                  'reverse_active_energy': None,
                                                  'reverse_active_max_need': 0.0,
                                                  'reverse_active_need': 0.0,
                                                  'reverse_active_net_total_energy': None,
                                                  'reverse_active_power': 0.0,
                                                  'reverse_active_today_energy': None,
                                                  'reverse_active_total_energy': 0.0,
                                                  'reverse_apparent_energy': None,
                                                  'reverse_instant_total_active_power': None,
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
                                                  'time_text': datetime.datetime(2018, 12, 13, 11, 3, 52),
                                                  'today_energy': None,
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
                                                  'zero_line_need': 0.0}]},
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

        response = self.session.get(
            endpoint="device/ammeter/meter_data",
            params={
                "datalog_sn": datalogger_sn,
                "address": meter_address,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return SmartMeterEnergyHistory.model_validate(response)
