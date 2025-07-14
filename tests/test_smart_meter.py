import unittest
from unittest import skip
from growatt_public_api import GrowattApiSession
from growatt_public_api.smart_meter import SmartMeter

TEST_FILE = "growatt_public_api.smart_meter.smart_meter"


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
        gas = GrowattApiSession.using_test_server_v1()
        # init DEVICE
        cls.api = SmartMeter(session=gas)
        cls.device_sn = ""  # "Currently no SmartMeter device in test environment"

    @skip("Currently no SmartMeter devices on test environment")
    def test_energy(self):
        raise NotImplementedError

    @skip("Currently no SmartMeter devices on test environment")
    def test_energy_history(self):
        raise NotImplementedError
