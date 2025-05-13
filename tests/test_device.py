import unittest
from typing import Union
from unittest import skip
from unittest.mock import patch

from api_v4 import ApiV4
from growatt_public_api import (
    GrowattApiSession,
    Device,
)
from pydantic_models import PlantInfo
from pydantic_models.device import (
    DeviceCreateDate,
    DeviceBasicData,
    DataloggerValidation,
    DataloggerValidationData,
    DeviceEnergyDay,
    DeviceDatalogger,
    DeviceDataloggerData,
    DeviceTypeInfo,
)
from pydantic_models.plant import PlantInfoData

TEST_FILE = "device.device"


# noinspection DuplicatedCode
class TestDevice(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Device = None
    device_sn: str = None
    datalogger_sn: str = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession(
            # several min devices seen on v1 test server
            server_url="https://test.growatt.com",
            token="6eb6f069523055a339d71e5b1f6c88cc",  # gitleaks:allow
        )
        # init DEVICE
        cls.api = Device(session=gas)
        # get a device
        try:
            apiv4 = ApiV4(session=gas)
            _devices = apiv4.list()
            sn_list = [x for x in _devices.data.data]  # select any type
            cls.device_sn = sn_list[0].device_sn
            cls.datalogger_sn = sn_list[0].datalogger_sn
        except AttributeError:
            cls.device_sn = "SASF819012"  # ['SASF819012', 'GRT0010086', 'RUK0CAE00J', 'TAG1234567', 'GRT1234001', 'GRT1235001', 'GRT1235002', 'GRT1235003', 'GRT1235004', 'GRT1235005', 'GRT1235006', 'GRT1235112', 'YYX1235112', 'YYX1235113', 'GRT1236601', 'GRT1236602', 'GRT1236603', 'GRT1236604', 'GRT1236605', 'EVK0BHX111']
            cls.datalogger_sn = "WLC082100F"

    def test_create_date(self):
        with patch(f"{TEST_FILE}.DeviceCreateDate", wraps=DeviceCreateDate) as mock_pyd_model:
            self.api.create_date(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DeviceCreateDate.model_fields.items()} | set(
            DeviceCreateDate.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in DeviceBasicData.model_fields.items()} | set(
            DeviceBasicData.model_fields.keys()
        )
        self.assertEqual(
            set(), set(raw_data["data"][self.device_sn].keys()).difference(pydantic_keys), f"data_{self.device_sn}"
        )

    @skip("Cannot test without validation code")
    def test_datalogger_validate(self):
        with patch(f"{TEST_FILE}.DataloggerValidation", wraps=DataloggerValidation) as mock_pyd_model:
            self.api.datalogger_validate(datalogger_sn=self.datalogger_sn, validation_code="0000")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DataloggerValidation.model_fields.items()} | set(
            DataloggerValidation.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in DataloggerValidationData.model_fields.items()} | set(
            DataloggerValidationData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")

    def test_energy_day(self):
        with patch(f"{TEST_FILE}.DeviceEnergyDay", wraps=DeviceEnergyDay) as mock_pyd_model:
            actual = self.api.energy_day(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DeviceEnergyDay.model_fields.items()} | set(
            DeviceEnergyDay.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        self.assertIsInstance(raw_data["data"], Union[int, float], "source data is numeric")
        self.assertIsInstance(actual.data, float, "output is converted to float")

    def test_get_datalogger(self):
        with patch(f"{TEST_FILE}.DeviceDatalogger", wraps=DeviceDatalogger) as mock_pyd_model:
            actual = self.api.get_datalogger(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DeviceDatalogger.model_fields.items()} | set(
            DeviceDatalogger.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in DeviceDataloggerData.model_fields.items()} | set(
            DeviceDataloggerData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check correct data returned
        self.assertEqual(self.datalogger_sn, actual.data.datalogger_sn)

    def test_type_info(self):
        with patch(f"{TEST_FILE}.DeviceTypeInfo", wraps=DeviceTypeInfo) as mock_pyd_model:
            self.api.type_info(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DeviceTypeInfo.model_fields.items()} | set(
            DeviceTypeInfo.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    def test_get_plant(self):
        with patch(f"{TEST_FILE}.PlantInfo", wraps=PlantInfo) as mock_pyd_model:
            self.api.get_plant(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantInfo.model_fields.items()} | set(
            PlantInfo.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantInfoData.model_fields.items()} | set(
            PlantInfoData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
