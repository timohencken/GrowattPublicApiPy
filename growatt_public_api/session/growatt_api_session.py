import hashlib
import json
import pickle
import tempfile
from datetime import timedelta, datetime
from pathlib import Path
from typing import Optional, Literal, Self
from loguru import logger
import requests


class GrowattApiSession:
    server_url: str
    api_url: str
    token: str
    session: requests.Session
    cache_folder: Path = None
    max_cache_age: timedelta = timedelta(days=1)
    """
    https://www.showdoc.com.cn/262556420217021/0
    """

    def __init__(
        self,
        token: str,
        server_url: Optional[str] = None,
        use_cache: bool = True,
    ) -> None:
        self.server_url = server_url or "https://openapi.growatt.com"
        # API docs specify /v1/ for some endpoints and /v4/ for other ("new-api") endpoints
        # anyway, both (v1 and v4) work for all endpoints
        # so we just use v4 for simplicity
        self.api_url = f"{self.server_url}/v4"
        self.token = token

        assert self.token, "No token provided"

        self.session = requests.Session()
        headers = {"token": self.token}
        self.session.headers.update(headers)

        # setup cache
        if use_cache:
            # set cache folder to TMP/growatt_public_api_cache
            self.cache_folder = Path(tempfile.gettempdir()) / "growatt_public_api_cache"
            self.cache_folder.mkdir(parents=True, exist_ok=True)
            # clean outdated pickle files
            cache_expires = datetime.now() - self.max_cache_age
            for pickle_file in self.cache_folder.glob("*.pickle"):
                mtime = datetime.fromtimestamp(pickle_file.stat().st_mtime)
                if mtime < cache_expires:
                    # Deleting outdated cache file
                    try:
                        pickle_file.unlink()
                    except OSError:
                        logger.debug(f"Failed to delete outdated cache file: {pickle_file}")

    @classmethod
    def using_test_server_v1(cls) -> Self:
        """
        Create a session using the test server
        """
        return cls(
            server_url="https://test.growatt.com",
            # test token from official API docs https://www.showdoc.com.cn/262556420217021/1494053950115877
            token="6eb6f069523055a339d71e5b1f6c88cc",  # gitleaks:allow
        )

    @classmethod
    def using_test_server_v4(cls) -> Self:
        """
        Create a session using the test server
        """
        return cls(
            server_url="http://183.62.216.35:8081",
            # test token from official API docs https://www.showdoc.com.cn/2540838290984246/11292912972201443
            token="wa265d2h1og0873ml07142r81564hho6",  # gitleaks:allow
        )

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
        use_cache: bool = True,
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
        elif ("Note: Dear user, you have not login to the system, skip login page login.." in response.text) or (
            '<a href="/login" target="_top" id="login">' in response.text
        ):
            logger.error("Forwarded to login page")

        try:
            json_data = response.json()
            # check error code
            error_code = json_data.get("error_code")
            error_code_new = json_data.get("code")
            if self.cache_folder and use_cache:
                # create hash from request params
                args_ = {"base_url": url, "endpoint": endpoint, "method": method, "params": params, "data": data}
                hash_ = hashlib.md5(json.dumps(args_).encode()).hexdigest()
                pickle_file = self.cache_folder / f"{hash_}.pickle"
                pickle_file.parent.mkdir(parents=True, exist_ok=True)

                if error_code == 10012 or error_code_new == 102:
                    # check if we have a cached version of this request and return it
                    if pickle_file.exists():
                        logger.warning(f"API limit exceeded. Using cached version of request to {endpoint}")
                        with pickle_file.open("rb") as f:
                            json_data = pickle.load(f)
                else:
                    # cache the response
                    with pickle_file.open("wb") as f:
                        pickle.dump(json_data, f)

                # recalculate as data might have been loaded from cache
                error_code = json_data.get("error_code")
                error_code_new = json_data.get("code")

            if error_code:
                error_msg = json_data.get("error_msg")
                generic_error_msg = self.generic_error_message(error_code)
                if not error_msg:
                    json_data["error_msg"] = generic_error_msg
                error_log = f"request failed with error code {error_code}: {error_msg}"
                if generic_error_msg:
                    error_log += f" ({generic_error_msg})"
                logger.warning(error_log)

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
