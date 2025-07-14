import datetime
from typing import Union, List

from pydantic import (
    ConfigDict,
)
from pydantic.alias_generators import to_camel

from .api_model import (
    ApiResponse,
    EmptyStrToNone,
    ApiModel,
    GrowattTimeCalendar,
)


# #####################################################################################################################
# Environmental sensor list ###########################################################################################


def _env_sensor_data_to_camel(snake: str) -> str:
    override = {
        "datalogger_sn": "datalog_sn",
    }
    return override.get(snake, to_camel(snake=snake))


class EnvSensorData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_env_sensor_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # device address, e.g. '1'
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the smart meter, e.g. 'CRAZT00001'
    device_name: Union[EmptyStrToNone, str] = None  # device name, e.g. 'ENV_DEVICE'
    device_type: Union[EmptyStrToNone, str] = None  # Device type (48: environmental tester), e.g. '48'
    last_update_time: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. '2019-01-09 10:33:06'
    lost: Union[EmptyStrToNone, bool] = None  # The online status of the device (0: online, 1: disconnected), e.g. 0


class EnvSensorListData(ApiModel):
    count: int  # Total number of devices
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The serial number of the collector, e.g. 'CRAZT00001'
    envs: List[EnvSensorData]


class EnvSensorList(ApiResponse):
    data: Union[EmptyStrToNone, EnvSensorListData] = None


# #####################################################################################################################
# Environmental sensor data overview ##################################################################################


def _env_sensor_metrics_overview_data_to_camel(snake: str) -> str:
    override = {
        "address": "addr",
        "datalogger_sn": "dataLogSn",
        "sensor_signal_gen": "sensorSingnalGen",
    }
    return override.get(snake, to_camel(snake=snake))


class EnvSensorMetricsOverviewData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_env_sensor_metrics_overview_data_to_camel,
    )

    address: Union[EmptyStrToNone, int] = None  # device address, e.g. 2
    air_pressure: Union[EmptyStrToNone, float] = None  # e.g. 0
    alarm_code: Union[EmptyStrToNone, str] = None  # e.g. ''
    calendar: Union[EmptyStrToNone, GrowattTimeCalendar] = None  # e.g. {'firstDayOfWeek: 1,...}
    comm_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    daily_avg_soil_lvl_pct: Union[EmptyStrToNone, float] = None  # e.g. 0
    datalogger_sn: Union[EmptyStrToNone, str] = None  # e.g. 'CRAZT00001'
    device_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    efficiency: Union[EmptyStrToNone, float] = None  # e.g. 0
    env_humidity: Union[EmptyStrToNone, float] = None  # e.g. 0
    env_temp: Union[EmptyStrToNone, float] = None  # Ambient temperature, e.g. 32.400001525878906
    etoday_radiation: Union[EmptyStrToNone, float] = None  # Etoday Radiation, e.g. 0
    etotal_radiation: Union[EmptyStrToNone, float] = None  # e.g. 0
    gas_concentration: Union[EmptyStrToNone, float] = None  # e.g. 0
    internal_pressure: Union[EmptyStrToNone, float] = None  # e.g. 0
    internal_relative_humidity: Union[EmptyStrToNone, float] = None  # e.g. 0
    internal_temp_c: Union[EmptyStrToNone, float] = None  # e.g. 0
    internal_temp_f: Union[EmptyStrToNone, float] = None  # e.g. 0
    last_four_measurements_avg: Union[EmptyStrToNone, float] = None  # e.g. 0
    panel_temp: Union[EmptyStrToNone, float] = None  # Panel temperature, e.g. 31.899999618530273
    radiant: Union[EmptyStrToNone, float] = None  # Irradiation intensity, e.g. 170
    rainfall_intensity: Union[EmptyStrToNone, float] = None  # e.g. 0
    run_status: Union[EmptyStrToNone, int] = None  # e.g. 0
    sensor_signal_gen: Union[EmptyStrToNone, float] = None  # e.g. 0
    snow_depth: Union[EmptyStrToNone, float] = None  # e.g. 0
    status_last_update_time: Union[EmptyStrToNone, str] = None  # e.g. ''
    time_text: Union[EmptyStrToNone, datetime.datetime] = None  # Last update time, e.g. '2019-01-09 13:37:33'
    total_rainfall: Union[EmptyStrToNone, float] = None  # e.g. 0
    wind_angle: Union[EmptyStrToNone, float] = None  # Wind direction, e.g. 1
    wind_speed: Union[EmptyStrToNone, float] = None  # wind speed, e.g. 0.10000000149011612


class EnvSensorMetricsOverview(ApiResponse):
    data: Union[EmptyStrToNone, EnvSensorMetricsOverviewData] = None
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "MONITOR003"


# #####################################################################################################################
# Environmental sensor data history ###################################################################################


class EnvSensorMetricsHistoryData(ApiModel):
    count: int  # Total Records
    datalogger_sn: Union[EmptyStrToNone, str] = None  # The collector SN of the inverter, e.g. "CRAZT00001"
    env_data: List[EnvSensorMetricsOverviewData]


class EnvSensorMetricsHistory(ApiResponse):
    data: Union[EmptyStrToNone, EnvSensorMetricsHistoryData] = None
