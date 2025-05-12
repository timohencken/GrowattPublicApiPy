import unittest
from unittest import skip
from growatt_public_api import GrowattApiSession
from smart_meter import SmartMeter

TEST_FILE = "smart_meter.smart_meter"


class TestSmartMeter(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: SmartMeter = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        return  # "Currently no SmartMeter device in test environment"

        # init API
        # noinspection PyUnreachableCode
        gas = GrowattApiSession(
            # several min devices seen on v1 test server
            server_url="https://test.growatt.com",
            token="6eb6f069523055a339d71e5b1f6c88cc",  # gitleaks:allow
        )
        # init DEVICE
        cls.api = SmartMeter(session=gas)
        cls.device_sn = ""  # "Currently no SmartMeter device in test environment"

    @skip("Currently no SmartMeter devices on test environment")
    def test_energy(self):
        raise NotImplementedError

    @skip("Currently no SmartMeter devices on test environment")
    def test_energy_history(self):
        raise NotImplementedError

    @skip("Currently no SmartMeter devices on test environment")
    def test_list(self):
        raise NotImplementedError
