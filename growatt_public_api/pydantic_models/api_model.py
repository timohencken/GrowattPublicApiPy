# Idea based on fastapi-restful which has a MIT License
# Fastapi-restful was deprecated in favor of fastapi-utils (which is MIT as well).
# This code is a rewritten and simplified version of the code from fastapi-restful and adjusted to work with pydantic V2.
import datetime
from typing import Any, TypeAlias, Annotated, Union, Optional

from loguru import logger

# LICENSE: https://github.com/dmontagu/fastapi-utils/blob/master/LICENSE
# Original Code: https://github.com/dmontagu/fastapi-utils/blob/master/fastapi_utils/api_model.py

from pydantic import (
    BaseModel,
    ConfigDict,
    BeforeValidator,
)
from pydantic.alias_generators import to_camel


def _empty_str_to_none(v: str | None) -> None:
    if v is None or v in ["", "null", "None"]:
        return None
    raise ValueError(
        "IGNORE (not a string - checking next type)"
    )  # Not str or None, Fall to next type. e.g. Decimal, or a non-empty str


def parse_forced_time(value: Optional[str] = None):
    """support 0:0 for 00:00"""
    if value and value.strip() and value != "null":
        # saw value "11:187" (="BBB") in test_min.test_details(), so we need to handle that
        try:
            return datetime.datetime.strptime(value, "%H:%M").time()
        except ValueError:
            logger.warning(f"Invalid time format: {value}. Returning None. Expected format is HH:MM.")
            return None
        except Exception as e:
            raise ValueError(str(e))
    else:
        return None


EmptyStrToNone: TypeAlias = Annotated[None, BeforeValidator(_empty_str_to_none)]


ForcedTime: TypeAlias = Annotated[Union[datetime.time, None], BeforeValidator(parse_forced_time)]


class ApiModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


class ApiResponse(ApiModel):
    """
    Generic API response. Base class for other responses
    """

    data: Union[EmptyStrToNone, Any] = None
    error_code: Union[EmptyStrToNone, int]
    error_msg: Union[EmptyStrToNone, str]


def _new_api_response_to_camel(snake: str) -> str:
    override = {
        "error_code": "code",
        "error_msg": "message",
    }
    return override.get(snake, to_camel(snake=snake))


class NewApiResponse(ApiModel):
    """
    Generic API response for v4/new-api.
    Base class for other responses
    renaming code->error_code and message->error_msg to be consistent with v1 API
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_new_api_response_to_camel,
    )

    data: Union[EmptyStrToNone, Any] = None
    error_code: Union[EmptyStrToNone, int]
    error_msg: Union[EmptyStrToNone, str]


class GrowattTime(ApiModel):
    """Api returns datetime in a special format"""

    year: int  # current year - 1900, e.g. 125 for 2025
    month: int  # month, e.g. 1
    date: int  # day, e.g. 25
    hours: int  # e.g. 0
    minutes: int  # e.g. 32
    seconds: int  # e.g. 1
    day: int  # weekday, e.g. 2
    time: datetime.datetime  # timestamp, e.g. 1740414721500
    timezone_offset: int  # e.g. -480


class GrowattTimeGregorianChange(GrowattTime):
    """'gregorianChange' has a negative timestamp, so we cannot use datetime directly."""

    time: int  # timestamp, e.g. -12219292800000


def _growatt_time_calendar_timezone_to_camel(snake: str) -> str:
    """
    define own to_camel function to support weird API naming
    """
    override = {
        "dst_savings": "DSTSavings",
        "id": "ID",
    }
    return override.get(snake, to_camel(snake=snake))


class GrowattTimeCalendarTimeZone(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_growatt_time_calendar_timezone_to_camel,
    )

    dirty: Union[EmptyStrToNone, bool] = None  # e.g. false
    display_name: Union[EmptyStrToNone, str] = None  # e.g. "China Standard Time"
    dst_savings: Union[EmptyStrToNone, int] = None  # e.g. 0
    id: Union[EmptyStrToNone, str] = None  # e.g. "Asia/Shanghai"
    last_rule_instance: Union[EmptyStrToNone, str] = None  # e.g. null
    raw_offset: Union[EmptyStrToNone, int] = None  # e.g. 28800000


class GrowattTimeCalendar(ApiModel):
    minimal_days_in_first_week: Union[EmptyStrToNone, int] = None  # e.g. 1
    week_year: Union[EmptyStrToNone, int] = None  # e.g. 2018
    time: Union[EmptyStrToNone, GrowattTime] = None
    weeks_in_week_year: Union[EmptyStrToNone, int] = None  # e.g. 52
    gregorian_change: Union[EmptyStrToNone, GrowattTimeGregorianChange] = None
    time_zone: Union[EmptyStrToNone, GrowattTimeCalendarTimeZone] = None
    time_in_millis: Union[EmptyStrToNone, int] = None  # e.g. 1544670232000
    lenient: Union[EmptyStrToNone, bool] = None  # e.g. true
    first_day_of_week: Union[EmptyStrToNone, int] = None  # e.g. 1
    week_date_supported: Union[EmptyStrToNone, bool] = None
