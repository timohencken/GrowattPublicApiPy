from typing import Optional, Literal
import truststore
from loguru import logger


truststore.inject_into_ssl()
import requests  # noqa: E402


class GrowattApiSession:
    server_url: str
    api_url: str
    token: str
    session: requests.Session
    """
    https://www.showdoc.com.cn/262556420217021/0
    """

    def __init__(
        self,
        token: str,
        server_url: str,
    ) -> None:
        self.server_url = server_url
        self.api_url = f"{self.server_url}/v1"  # API doccs specify v1
        # self.api_url = f"{self.server_url}/v4"  # but v4 works just the same
        self.token = token

        assert self.token, "No token provided"

        self.session = requests.Session()
        headers = {"token": self.token}
        self.session.headers.update(headers)

    @staticmethod
    def generic_error_message(code: int):
        error_codes = {
            # common error codes from v1 API
            0: "Normal",  # Success
            10011: "No privilege access",
            10012: "API rate limit exceeded (same request only once every 5 minutes)",
            10013: "The number per page cannot be greater than 100",
            10014: "The number of pages cannot be greater than 250 pages",
            -1: "Please use the new domain name to access",
        }
        error_message = error_codes.get(code, "")
        return error_message

    @staticmethod
    def generic_response_message(code: int):
        error_codes = {
            # common error codes from v4/new-api API
            0: "Normal",
            1: "System Error",
            2: "Invalid Secret Token",
            3: "Device Permission Verification Failed",
            4: "Device Not Found",
            5: "Device Offline",
            6: "Failed to Set Parameters",
            7: "Device Type Error",
            8: "Device SN is Empty",
            9: "Date Cannot Be Empty",
            10: "Page Number Cannot Be Empty",
            11: "Device SN Exceeds Quantity Limit",
            12: "No Permission to Access Device",
            100: "API Access Interval",
            101: "No Permission to Access",
            102: "Access Frequency Limit, Different Interfaces Have Different Time Limits (most allow 5 minute intervals)",
            -1: "Please Use the New Domain for Access",
        }
        error_message = error_codes.get(code, "")
        return error_message

    def get(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict] = None,
    ):
        return self.request(
            endpoint=endpoint,
            method="GET",
            params=params,
        )

    def post(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
    ):
        return self.request(
            endpoint=endpoint,
            method="POST",
            params=params,
            data=data,
        )

    def request(  # noqa: C901 'GrowattApiSession.request' is too complex (12)
        self,
        endpoint: Optional[str] = None,
        method: Literal["GET", "POST"] = "GET",
        params: Optional[dict] = None,
        data: Optional[dict] = None,
    ):
        """
        Perform a request to the Growatt API
        """
        url = f"{self.api_url}"
        if endpoint:
            url = f"{url}/{endpoint}"
        response = self.session.request(
            method,
            url=url,
            params=params,
            data=data,
        )

        if '<html data-name="login">' in response.text:
            logger.error("Login page shown")
        elif "Note: Dear user, you have not login to the system, skip login page login.." in response.text:
            logger.error("Forwarded to login page")

        try:
            json_data = response.json()
            # check error code
            error_code = json_data.get("error_code")
            if error_code:
                error_msg = json_data.get("error_msg")
                generic_error_msg = self.generic_error_message(error_code)
                if not error_msg:
                    json_data["error_msg"] = generic_error_msg
                error_log = f"request failed with error code {error_code}: {error_msg}"
                if generic_error_msg:
                    error_log += f" ({generic_error_msg})"
                logger.warning(error_log)
            error_code_new = json_data.get("code")
            if error_code_new:
                error_msg = json_data.get("message")
                generic_error_msg = self.generic_response_message(error_code_new)
                if not error_msg:
                    json_data["message"] = generic_error_msg
                error_log = f"request failed with error code {error_code_new}: {error_msg}"
                if generic_error_msg:
                    error_log += f" ({generic_error_msg})"
                logger.warning(error_log)

            return json_data
        except Exception as e:
            logger.error(f"JSON conversion failed: {e}\nResponse was:\n{response.text}")
            raise
