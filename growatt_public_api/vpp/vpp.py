import json
from datetime import time
from typing import List, Tuple
from ..pydantic_models.vpp import (
    VppSoc,
    VppWrite,
)
from ..session import GrowattApiSession


class Vpp:
    """
    endpoints for VPP SOC interface (MIN/SPA/SPH models)
    https://www.showdoc.com.cn/262556420217021/7178565721512898
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def soc(
        self,
        device_sn: str,
    ) -> VppSoc:
        """
        Get machine SOC value (VPP)
        Get machine SOC value interface (only supports MIN SPA SPH models)
        https://www.showdoc.com.cn/262556420217021/7178565721512898

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: read failure
        * 10002: device does not exist
        * 10003: device serial number is empty

        Args:
            device_sn (str): VPP SN

        Returns:
            MinSettings
            {
                'error_code': 0,
                'error_msg': None,
                'soc': 65.0,
                'datalogger_sn': 'JPC5A11700',
                'device_sn': 'MIXECN6000'
            }
        """

        response = self.session.post(
            endpoint="device/vpp/getSocData",
            data={
                "vppSn": device_sn,
            },
        )

        return VppSoc.model_validate(response)

    def write(
        self,
        device_sn: str,
        time_: time,
        percentage: int,
    ) -> VppWrite:
        """
        Read the machine to perform battery charging contr
        The reading machine immediately executes the battery charging control interface (only supports MIN SPA SPH models)
        https://www.showdoc.com.cn/262556420217021/7178602212464389

        Note: this endpoint is poorly documented

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 500: Set Parameter Failure
        * 10001: Reading failed
        * 10012: Device does not exist
        * 10004: Device serial number is empty
        * 10005: Collector offline
        * 10007: Setting parameter is null
        * 10008: Setting value is out of range Or abnormal
        * 10009: The type of the read setting parameter does not exist
        * 10011: No permission

        Args:
            device_sn (str): VPP SN
            time_ (time): Set time - 00:00 ~ 24:00 (hh:mm),
            percentage (int): Set the power positive number for charging - negative number for discharge -100 ~ 100

        Returns:
            VppWrite
            {
                'error_code': 0,
                'error_msg': None,
                'data': 0,
            }
        """

        time_int_min = time_.hour * 24 + time_.minute
        assert time_int_min <= 1440, f"Time range must not exceed 24 hours. You specified {time_}"

        percentage = int(round(percentage, 0))
        assert -100 <= percentage <= 100, f"Percentage must be between -100 and 100. You specified {percentage}"

        response = self.session.post(
            endpoint="vppRemoteSetNew",
            data={
                "vppSn": device_sn,
                "time": time_int_min,
                "percentage": percentage,
            },
        )

        return VppWrite.model_validate(response)

    def write_multiple(self, device_sn: str, schedules: List[Tuple[int, time, time]]) -> VppWrite:
        """
        Read and set VPP time period parameters (VPP)
        Read and set VPP time period parameter interface (only support MIN SPA SPH model)
        https://www.showdoc.com.cn/262556420217021/7178602212464389

        Note: this endpoint is poorly documented

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: Reading/Writing failed
        * 10012: Device does not exist
        * 10004: Device serial number is empty
        * 10005: Collector offline
        * 10007: Setting parameter is null
        * 10008: Setting value is out of range Or abnormal
        * 10009: The type of the read setting parameter does not exist
        * 10011: No permission

        Args:
            device_sn (str): VPP SN
            schedules (List[Tuple[int, time, time]]): Set time period
                Tuple with (power_percentage (int), start_time (time), end_time (time))
                percentage: positive number for charge 0 ~ 100, negative number for discharge -100 ~ 0
                e.g. [
                    (95, time(hour=0, minute=0), time(hour=5, minute=0)),    # 00:00 ~ 05:00 95% charge
                    (-60, time(hour=5, minute=1), time(hour=12, minute=0)),  # 05:01 ~ 12:00 60% discharge
                ]

        Returns:
            VppWrite
            {
                'error_code': 0,
                'error_msg': None,
                'data': 0,
            }
        """

        time_periods_parsed = []
        for percentage, start_time, end_time in schedules:
            percentage = int(round(percentage, 0))
            assert -100 <= percentage <= 100, f"Percentage must be between -100 and 100. You specified {percentage}"
            start_min = start_time.hour * 60 + start_time.minute
            end_min = end_time.hour * 60 + end_time.minute
            assert end_min > start_min, f"End time must be after start time. You specified {start_time} ~ {end_time}"
            time_periods_parsed.append(
                {
                    "percentage": percentage,
                    "startTime": start_min,
                    "endTime": end_min,
                }
            )

        response = self.session.post(
            endpoint="vppSetNew",
            data={
                "vppSn": device_sn,
                "timePeriods": json.dumps(time_periods_parsed),
            },
        )

        return VppWrite.model_validate(response)
