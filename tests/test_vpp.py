import datetime
import unittest
from unittest import skip
from unittest.mock import patch

from growatt_public_api import GrowattApiSession, Vpp
from growatt_public_api.pydantic_models import VppSoc


TEST_FILE = "growatt_public_api.vpp.vpp"


# noinspection DuplicatedCode
class TestVpp(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Vpp = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        return  # "Currently no SmartMeter device in test environment"

        # init API
        # noinspection PyUnreachableCode
        gas = GrowattApiSession.using_test_server_v1()
        # init DEVICE
        cls.api = Vpp(session=gas)
        cls.device_sn = ""  # "Currently no VPP device in test environment"

    @skip("No VPP device available on test environment (MIN device returns error)")
    def test_soc(self):
        with patch(f"{TEST_FILE}.VppSoc", wraps=VppSoc) as mock_pyd_model:
            self.api.soc(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in VppSoc.model_fields.items()} | set(
            VppSoc.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)

    @skip("No VPP device available on test environment (MIN device returns error)")
    def test_write(self):
        self.api.write(
            device_sn=self.device_sn,
            time_=datetime.time(12, 0),
            percentage=100,
        )
        raise NotImplementedError

    @skip("No VPP device available on test environment (MIN device returns error)")
    def test_write_multiple(self):
        self.api.write_multiple(
            device_sn=self.device_sn,
            time_percent=[
                (100, datetime.time(12, 0), datetime.time(13, 0)),
                (50, datetime.time(13, 0), datetime.time(14, 0)),
                (25, datetime.time(14, 0), datetime.time(15, 0)),
            ],
        )
        raise NotImplementedError
