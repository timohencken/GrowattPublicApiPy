import datetime
from typing import Union, List

from pydantic_models.api_model import (
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


class UserInfo(ApiModel):
    c_user_id: Union[EmptyStrToNone, int] = None  # e.g. 1
    c_user_name: Union[EmptyStrToNone, str] = None  # e.g. "admin"
    c_user_email: Union[EmptyStrToNone, str] = None  # e.g. "imluobao@163.com"
    c_user_tel: Union[EmptyStrToNone, str] = None  # e.g. ""
    c_user_regtime: Union[EmptyStrToNone, datetime.datetime] = (
        None  # e.g. "2018-02-04 09:46:50"
    )


class UserListData(ApiModel):
    count: Union[EmptyStrToNone, int] = None  # e.g. 2
    c_user: List[UserInfo]


class UserList(ApiResponse):
    data: Union[EmptyStrToNone, UserListData] = None
