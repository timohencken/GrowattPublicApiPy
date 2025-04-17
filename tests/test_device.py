import unittest
from typing import Union
from unittest import skip
from unittest.mock import patch

from api_v4 import ApiV4
from growatt_public_api import GrowattApiSession, Device, Plant
from pydantic_models.device import (
    DeviceCreateDate,
    DeviceBasicData,
    DataloggerList,
    DataloggerListData,
    DataloggerData,
    DataloggerValidation,
    DataloggerValidationData,
    DeviceEnergyDay,
    DeviceDatalogger,
    DeviceDataloggerData,
    DeviceList,
    DeviceListData,
    DeviceData,
    DeviceTypeInfo,
)


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
    plant_id: int = None

    def setUp(self):
        # init API
        gas = GrowattApiSession(
            # several min devices seen on v1 test server
            server_url="https://test.growatt.com",
            token="6eb6f069523055a339d71e5b1f6c88cc",  # gitleaks:allow
        )
        # init DEVICE
        if self.api is None:
            self.api = Device(session=gas)
        # get a DEVICE device
        if self.device_sn is None:
            try:
                apiv4 = ApiV4(session=gas)
                _devices = apiv4.list()
                sn_list = [x for x in _devices.data.data]  # select any type
                self.device_sn = sn_list[0].device_sn
                self.datalogger_sn = sn_list[0].device_sn
                # get plant information
                api_plant = Plant(session=gas)
                _plant_info = api_plant.by_device(device_sn=self.device_sn)
                self.plant_id = _plant_info.data.plant.plant_id
            except AttributeError:
                # getting "FREQUENTLY_ACCESS" easily # TODO caching would be nice
                self.device_sn = "SASF819012"  # ['SASF819012', 'GRT0010086', 'RUK0CAE00J', 'TAG1234567', 'GRT1234001', 'GRT1235001', 'GRT1235002', 'GRT1235003', 'GRT1235004', 'GRT1235005', 'GRT1235006', 'GRT1235112', 'YYX1235112', 'YYX1235113', 'GRT1236601', 'GRT1236602', 'GRT1236603', 'GRT1236604', 'GRT1236605', 'EVK0BHX111']
                self.datalogger_sn = "WLC082100F"
                self.plant_id = 23

    @skip("Currently not testing endpoints writing data")
    def test_add(self):
        raise NotImplementedError

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

    @skip("Currently not testing endpoints writing data")
    def test_datalogger_add(self):
        raise NotImplementedError

    @skip("Currently not testing endpoints writing data")
    def test_datalogger_delete(self):
        raise NotImplementedError

    def test_datalogger_list(self):
        with patch(f"{TEST_FILE}.DataloggerList", wraps=DataloggerList) as mock_pyd_model:
            self.api.datalogger_list(plant_id=self.plant_id)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DataloggerList.model_fields.items()} | set(
            DataloggerList.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in DataloggerListData.model_fields.items()} | set(
            DataloggerListData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check data item
        pydantic_keys = {v.alias for k, v in DataloggerData.model_fields.items()} | set(
            DataloggerData.model_fields.keys()
        )
        self.assertEqual(
            set(), set(raw_data["data"]["dataloggers"][0].keys()).difference(pydantic_keys), f"data_dataloggers_0"
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

    def test_list(self):
        with patch(f"{TEST_FILE}.DeviceList", wraps=DeviceList) as mock_pyd_model:
            self.api.list(plant_id=self.plant_id)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DeviceList.model_fields.items()} | set(
            DeviceList.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in DeviceListData.model_fields.items()} | set(
            DeviceListData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check data item
        pydantic_keys = {v.alias for k, v in DeviceData.model_fields.items()} | set(DeviceData.model_fields.keys())
        self.assertEqual(
            set(), set(raw_data["data"]["devices"][0].keys()).difference(pydantic_keys), f"data_dataloggers_0"
        )

    def test_type_info(self):
        with patch(f"{TEST_FILE}.DeviceTypeInfo", wraps=DeviceTypeInfo) as mock_pyd_model:
            self.api.type_info(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DeviceTypeInfo.model_fields.items()} | set(
            DeviceTypeInfo.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
