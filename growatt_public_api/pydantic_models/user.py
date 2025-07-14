import datetime
from typing import Union, List

from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from .api_model import (
    ApiResponse,
    ApiModel,
    EmptyStrToNone,
)


# #####################################################################################################################
# User registration ###################################################################################################


class UserRegistrationData(ApiModel):
    c_user_id: int  # End User ID, e.g. 54


class UserRegistration(ApiResponse):
    data: Union[EmptyStrToNone, UserRegistrationData] = None


# #####################################################################################################################
# User modification ###################################################################################################


class UserModification(ApiResponse):
    data: Union[EmptyStrToNone, str] = None  # e.g. ""


# #####################################################################################################################
# Username availability check #########################################################################################


class UsernameAvailabilityCheck(ApiResponse):
    username_available: Union[EmptyStrToNone, bool] = None  # e.g. true
    data: Union[EmptyStrToNone, str] = None  # e.g. ""


# #####################################################################################################################
# User list ###########################################################################################################


def _user_info_to_camel(snake: str) -> str:
    override = {
        "id": "c_user_id",
        "name": "c_user_name",
        "email": "c_user_email",
        "phone_number": "c_user_tel",
        "registration_date": "c_user_regtime",
    }
    return override.get(snake, to_camel(snake=snake))


class UserInfo(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_user_info_to_camel,
    )

    id: Union[EmptyStrToNone, int] = None  # e.g. 1
    name: Union[EmptyStrToNone, str] = None  # e.g. "admin"
    email: Union[EmptyStrToNone, str] = None  # e.g. "imluobao@163.com"
    phone_number: Union[EmptyStrToNone, str] = None  # e.g. ""
    registration_date: Union[EmptyStrToNone, datetime.datetime] = None  # e.g. "2018-02-04 09:46:50"


def _user_list_data_to_camel(snake: str) -> str:
    override = {
        "users": "c_user",
    }
    return override.get(snake, to_camel(snake=snake))


class UserListData(ApiModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_user_list_data_to_camel,
    )
    count: Union[EmptyStrToNone, int] = None  # e.g. 2
    users: List[UserInfo]


class UserList(ApiResponse):
    data: Union[EmptyStrToNone, UserListData] = None
