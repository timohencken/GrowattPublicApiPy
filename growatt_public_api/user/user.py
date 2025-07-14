from typing import Optional, Union
from ..pydantic_models.user import (
    UserRegistration,
    UserModification,
    UsernameAvailabilityCheck,
    UserList,
)
from ..growatt_types import GrowattCountry
from ..session import GrowattApiSession


class User:
    """
    endpoints for User management
    https://www.showdoc.com.cn/262556420217021/1494056540800578
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def register(
        self,
        username: str,
        password: str,
        email: str,
        country: Union[GrowattCountry, str],
        installer_code: Optional[str] = None,
        phone_number: Optional[str] = None,
        time_zone: Optional[str] = None,
        user_type: int = 1,
    ) -> UserRegistration:
        """
        1.1 User registration
        User registered interface
        https://www.showdoc.com.cn/262556420217021/1494056540800578

        Specific error codes:
        * 10001: System error
        * 10002: Username or password is empty
        * 10003: Username already exists
        * 10004: User mailbox is empty
        * 10006: User type is empty
        * 10008: Token is empty
        * 10014: Installer coding error

        Args:
            username (str): username
            password (str): Password
            email (str): Register Email
            country (str): User Country
            user_type (int): User Type (1 for end customers)
            installer_code (Optional[str]): Installer code
            phone_number (Optional[str]): User Phone
            time_zone (Optional[str]): User Time Zone

        Returns:
            UserRegistration
            {   'data': {'c_user_id': 54},
                'error_code': 0,
                'error_msg': None}
        """
        if isinstance(country, GrowattCountry):
            country = country.value

        response = self.session.post(
            endpoint="user/user_register",
            data={
                "user_name": username,
                "user_password": password,
                "user_email": email,
                "user_type": user_type,
                "user_country": country,
                "agent_code": installer_code,
                "user_tel": phone_number,
                "time": time_zone,
            },
        )

        return UserRegistration.model_validate(response)

    def modify(
        self,
        user_id: int,
        phone_number: str,
        installer_code: Optional[str] = None,
    ) -> UserModification:
        """
        1.2 Modify user information
        Interface to modify user information
        https://www.showdoc.com.cn/262556420217021/1494057478651903

        Specific error codes:
        * 10001: System error
        * 10002: User ID is empty
        * 10003: User does not exist
        * 10004: User ID does not match token
        * 10014：Installer coding error

        Args:
            user_id (int): User ID ("c_user_id" as returned in register())
            phone_number (str): Phone number
            installer_code (Optional[str]): Installer code

        Returns:
            UserModification
            {   'data': None,
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="user/modify",
            data={
                "c_user_id": user_id,
                "mobile": phone_number,
                "agent_code": installer_code,
            },
        )

        return UserModification.model_validate(response)

    def check_username(
        self,
        username: str,
    ) -> UsernameAvailabilityCheck:
        """
        1.3 Verify that the username is duplicated
        Verify that the username is duplicated
        https://www.showdoc.com.cn/262556420217021/1494057808771611

        Specific error codes:
        * 10001: Server exception
        * 10002: Username is empty
        * 10003: Username already exists

        Args:
            username (str): username

        Returns:
            UserModification
            {   'data': None,
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="user/check_user",
            data={
                "user_name": username,
            },
        )
        if response["error_code"] == 10003:
            response["username_available"] = False
        elif response["error_code"] == 0:
            response["username_available"] = True

        return UsernameAvailabilityCheck.model_validate(response)

    def list(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> UserList:
        """
        1.4 Get a list of end users under the merchant
        Get the interface of the end user list under the merchant
        https://www.showdoc.com.cn/262556420217021/1494058357406324

        Rate limit(s):
        * Get the frequency once every 5 minutes
        * This interface is only allowed to call 10 times a day

        Specific error codes:
        * 10001: System error

        Args:
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            UserList
            {   'data': {   'c_user': [   {   'c_user_email': 'foobar@example.com',
                                              'c_user_id': 1,
                                              'c_user_name': 'admin',
                                              'c_user_regtime': datetime.datetime(2018, 2, 4, 9, 46, 50),
                                              'c_user_tel': None}],
                            'count': 2},
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="user/c_user_list",
            params={
                "page": page,
                "perpage": limit,
            },
        )

        return UserList.model_validate(response)
