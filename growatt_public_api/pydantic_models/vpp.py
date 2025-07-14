from typing import Union

from pydantic import (
    ConfigDict,
)
from pydantic.alias_generators import to_camel

from .api_model import (
    ApiResponse,
    EmptyStrToNone,
)


# #####################################################################################################################
# Vpp SOC #############################################################################################################


def _vpp_soc_to_camel(snake: str) -> str:
    override = {"device_sn": "sn", "datalogger_sn": "dataLogSn"}
    return override.get(snake, to_camel(snake=snake))


class VppSoc(ApiResponse):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_vpp_soc_to_camel,
    )
    soc: Union[EmptyStrToNone, float] = None  # SOC value, e.g. 65
    datalogger_sn: Union[EmptyStrToNone, str] = None  # Device collector serial number, e.g. "ZT00100001"
    device_sn: Union[EmptyStrToNone, str] = None  # Device serial number, e.g. "CRAZT00001"


# #####################################################################################################################
# Vpp write ###########################################################################################################


class VppWrite(ApiResponse):
    data: Union[EmptyStrToNone, int] = None


# #####################################################################################################################
