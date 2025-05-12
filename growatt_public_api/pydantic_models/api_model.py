# Idea based on fastapi-restful which has a MIT License
# Fastapi-restful was deprecated in favor of fastapi-utils (which is MIT as well).
# This code is a rewritten and simplified version of the code from fastapi-restful and adjusted to work with pydantic V2.
from typing import Any, TypeAlias, Annotated, Union

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


EmptyStrToNone: TypeAlias = Annotated[None, BeforeValidator(_empty_str_to_none)]


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
    time: int  # timestamp, e.g. 1740414721500
    timezone_offset: int  # e.g. -480
