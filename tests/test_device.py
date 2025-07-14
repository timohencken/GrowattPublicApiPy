import unittest
from typing import Union
from unittest import skip
from unittest.mock import patch

from growatt_public_api import (
    GrowattApiSession,
    Device,
    DeviceType,
)
from growatt_public_api.pydantic_models import PlantInfo
from growatt_public_api.pydantic_models.device import (
    DeviceCreateDate,
    DeviceBasicData,
    DataloggerValidation,
    DataloggerValidationData,
    DeviceEnergyDay,
    DeviceDatalogger,
    DeviceDataloggerData,
    DeviceTypeInfo,
)
from growatt_public_api.pydantic_models.plant import PlantInfoData

TEST_FILE = "growatt_public_api.device.device"


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
        gas = GrowattApiSession.using_test_server_v1()
        # init DEVICE
        cls.api = Device(session=gas)
        # get a device
        try:
            _devices = cls.api.list()
            sn_list = [x for x in _devices.data.data]  # select any type
            cls.device_sn = sn_list[0].device_sn
            cls.datalogger_sn = sn_list[0].datalogger_sn
        except AttributeError:
            cls.device_sn = "SASF819012"  # ['SASF819012', 'GRT0010086', 'RUK0CAE00J', 'TAG1234567', 'GRT1234001', 'GRT1235001', 'GRT1235002', 'GRT1235003', 'GRT1235004', 'GRT1235005', 'GRT1235006', 'GRT1235112', 'YYX1235112', 'YYX1235113', 'GRT1236601', 'GRT1236602', 'GRT1236603', 'GRT1236604', 'GRT1236605', 'EVK0BHX111']
            cls.datalogger_sn = "WLC082100F"

    def test_get_device_type(self):
        """test device type detection"""
        gas_v1 = GrowattApiSession.using_test_server_v1()
        device_api_v1 = Device(session=gas_v1)
        gas_v4 = GrowattApiSession.using_test_server_v4()
        device_api_v4 = Device(session=gas_v4)
        expected_devices = [
            # GROBOOST not available
            # HPS not available
            # INVERTER
            {"expected": DeviceType.INVERTER, "device_sn": "NHB691514F", "api": device_api_v4},
            # MAX
            {"expected": DeviceType.MAX, "device_sn": "SASF819012", "api": device_api_v1},
            {"expected": DeviceType.MAX, "device_sn": "QXHLD7F0C9", "api": device_api_v4},
            # MIN
            {"expected": DeviceType.MIN, "device_sn": "GRT0010086", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "RUK0CAE00J", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "TAG1234567", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1234001", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1235001", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1235002", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1235003", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1235004", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1235005", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1235006", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1235112", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "YYX1235112", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "YYX1235113", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1236601", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1236602", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1236603", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1236604", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "GRT1236605", "api": device_api_v1},
            # {"expected": DeviceType.MIN, "device_sn": "EVK0BHX111", "api": device_api_v1},
            # NOAH not available
            # PBD not available
            # PCS not available
            # SPA
            {"expected": DeviceType.SPA, "device_sn": "CHENYINSHU", "api": device_api_v4},
            # SPH
            {"expected": DeviceType.SPH, "device_sn": "AQM1234567", "api": device_api_v4},
            # SPH-S
            {"expected": DeviceType.SPHS, "device_sn": "EFP0N1J023", "api": device_api_v4},
            # STORAGE
            {"expected": DeviceType.STORAGE, "device_sn": "KHMOCM5688", "api": device_api_v4},
            # WIT
            {"expected": DeviceType.WIT, "device_sn": "QWL0DC3002", "api": device_api_v4},
            # Error cases
            {"expected": None, "device_sn": "NOTEXISTING", "api": device_api_v1},
            {"expected": None, "device_sn": "NOTEXISTING", "api": device_api_v4},
        ]
        for expected_device in expected_devices:
            expected_type = expected_device["expected"]
            device_sn = expected_device["device_sn"]
            api = expected_device["api"]
            print(f"checking {expected_type} {device_sn}")
            actual_type = api.get_device_type(device_sn=device_sn)
            self.assertEqual(expected_type, actual_type, f"unexpected type for device_sn: {device_sn}")

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
