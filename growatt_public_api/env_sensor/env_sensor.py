from datetime import date, timedelta
from typing import Optional
from ..pydantic_models.env_sensor import (
    EnvSensorMetricsOverview,
    EnvSensorMetricsHistory,
)
from ..session.growatt_api_session import GrowattApiSession


class EnvSensor:
    """
    endpoints for Environmental sensors (e.g. wind/temperature sensor)
    https://www.showdoc.com.cn/262556420217021/6131376900470247

    Note:
        Only applicable to devices with device type 3 (other) returned by plant.list_devices() - if device is an environmental sensor
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def metrics(
        self,
        datalogger_sn: str,
        sensor_address: int,
    ) -> EnvSensorMetricsOverview:
        """
        Acquire real-time data of the environmental detect
        According to the collector SN and the address of the environmental detector to obtain the real-time data interface of the environmental detector
        https://www.showdoc.com.cn/262556420217021/6131383465700984

        Note:
            Only applicable to devices with device type 3 (other) returned by plant.list_devices() - if device is an environmental sensor

        Rate limit(s):
        * The frequency of acquisition is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: collector SN error
        * 10003: device address is empty
        * 10004: collector does not exist

        Args:
            datalogger_sn (str): Serial number of the datalogger the meter is attached to
            sensor_address (int): Address of the sensor (see SmartMeter.list() output)

        Returns:
            EnvSensorMetricsOverview
            {   'data': {   'address': 2,
                            'air_pressure': None,
                            'alarm_code': None,
                            'calendar': {   'first_day_of_week': 1,
                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                            'lenient': True,
                                            'minimal_days_in_first_week': 1,
                                            'time': {'date': 9, 'day': 3, 'hours': 13, 'minutes': 37, 'month': 0, 'seconds': 33, 'time': 1547012253000, 'timezone_offset': -480, 'year': 119},
                                            'time_in_millis': 1547012253000,
                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                            'week_date_supported': True,
                                            'week_year': 2019,
                                            'weeks_in_week_year': 52},
                            'comm_status': None,
                            'daily_avg_soil_lvl_pct': None,
                            'datalogger_sn': 'CRAZT00001',
                            'device_status': None,
                            'efficiency': None,
                            'env_humidity': None,
                            'env_temp': 32.400001525878906,
                            'etoday_radiation': None,
                            'etotal_radiation': None,
                            'gas_concentration': None,
                            'internal_pressure': None,
                            'internal_relative_humidity': None,
                            'internal_temp_c': None,
                            'internal_temp_f': None,
                            'last_four_measurements_avg': None,
                            'panel_temp': 31.899999618530273,
                            'radiant': 170.0,
                            'rainfall_intensity': None,
                            'run_status': None,
                            'sensor_signal_gen': None,
                            'snow_depth': None,
                            'status_last_update_time': None,
                            'time_text': datetime.datetime(2019, 1, 9, 13, 37, 33),
                            'total_rainfall': None,
                            'wind_angle': 1.0,
                            'wind_speed': 0.10000000149011612},
                'datalogger_sn': 'CRAZT00001',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/env/env_last_data",
            params={
                "datalog_sn": datalogger_sn,
                "address": sensor_address,
            },
        )

        return EnvSensorMetricsOverview.model_validate(response)

    def metrics_history(
        self,
        datalogger_sn: str,
        sensor_address: int,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> EnvSensorMetricsHistory:
        """
        Obtain environmental detector data according to th
        According to the collector SN and the address of the environmental detector to obtain the interface of the environmental detector data
        https://www.showdoc.com.cn/262556420217021/6131378411575311

        Note:
            Only applicable to devices with device type 3 (other) returned by plant.list_devices() - if device is an environmental sensor

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
            sensor_address (int): Address of the sensor (see SmartMeter.list() output)
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            EnvSensorMetricsHistory
            {   'data': {   'count': 39,
                            'datalogger_sn': 'CRAZT00001',
                            'env_data': [   {   'address': 2,
                                                'air_pressure': None,
                                                'alarm_code': None,
                                                'calendar': {   'first_day_of_week': 1,
                                                                'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                                'lenient': True,
                                                                'minimal_days_in_first_week': 1,
                                                                'time': {'date': 9, 'day': 3, 'hours': 13, 'minutes': 37, 'month': 0, 'seconds': 33, 'time': 1547012253000, 'timezone_offset': -480, 'year': 119},
                                                                'time_in_millis': 1547012253000,
                                                                'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                                'week_date_supported': True,
                                                                'week_year': 2019,
                                                                'weeks_in_week_year': 52},
                                                'comm_status': None,
                                                'daily_avg_soil_lvl_pct': None,
                                                'datalogger_sn': 'CRAZT00001',
                                                'device_status': None,
                                                'efficiency': None,
                                                'env_humidity': None,
                                                'env_temp': 32.400001525878906,
                                                'etoday_radiation': None,
                                                'etotal_radiation': None,
                                                'gas_concentration': None,
                                                'internal_pressure': None,
                                                'internal_relative_humidity': None,
                                                'internal_temp_c': None,
                                                'internal_temp_f': None,
                                                'last_four_measurements_avg': None,
                                                'panel_temp': 31.899999618530273,
                                                'radiant': 170.0,
                                                'rainfall_intensity': None,
                                                'run_status': None,
                                                'sensor_signal_gen': None,
                                                'snow_depth': None,
                                                'status_last_update_time': None,
                                                'time_text': datetime.datetime(2019, 1, 9, 13, 37, 33),
                                                'total_rainfall': None,
                                                'wind_angle': 1.0,
                                                'wind_speed': 0.10000000149011612}]},
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
            endpoint="device/env/env_data",
            params={
                "datalog_sn": datalogger_sn,
                "address": sensor_address,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return EnvSensorMetricsHistory.model_validate(response)
