import unittest
from unittest import skip
from unittest.mock import patch

from growatt_public_api import (
    GrowattApiSession,
    Datalogger,
    Device,
)
from growatt_public_api.pydantic_models import EnvSensorList, SmartMeterList
from growatt_public_api.pydantic_models.device import (
    DataloggerValidation,
    DataloggerValidationData,
)
from growatt_public_api.pydantic_models.env_sensor import (
    EnvSensorListData,
    EnvSensorData,
)
from growatt_public_api.pydantic_models.smart_meter import SmartMeterListData, SmartMeterData

TEST_FILE = "growatt_public_api.datalogger.datalogger"


# noinspection DuplicatedCode
class TestDatalogger(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Datalogger = None
    datalogger_sn: str = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession.using_test_server_v1()
        # init DEVICE
        cls.api = Datalogger(session=gas)
        # get a device
        try:
            api_device = Device(session=gas)
            _devices = api_device.list()
            sn_list = [x for x in _devices.data.data]  # select any type
            cls.datalogger_sn = sn_list[0].datalogger_sn
        except AttributeError:
            cls.datalogger_sn = "WLC082100F"

    @skip("Cannot test without validation code")
    def test_validate(self):
        with patch(f"{TEST_FILE}.DataloggerValidation", wraps=DataloggerValidation) as mock_pyd_model:
            self.api.validate(datalogger_sn=self.datalogger_sn, validation_code="0000")

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

    def test_list_env_sensors(self):
        with patch(f"{TEST_FILE}.EnvSensorList", wraps=EnvSensorList) as mock_pyd_model:
            self.api.list_env_sensors(datalogger_sn=self.datalogger_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in EnvSensorList.model_fields.items()} | set(
            EnvSensorList.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in EnvSensorListData.model_fields.items()} | set(
            EnvSensorListData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check data item
        if raw_data["data"]["count"] == 0:
            self.assertEqual([], raw_data["data"]["envs"], f"data_envs empty")
        else:
            pydantic_keys = {v.alias for k, v in EnvSensorData.model_fields.items()} | set(
                EnvSensorData.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["envs"][0].keys()).difference(pydantic_keys), f"data_envs_0")

    def test_list_smart_meters(self):
        with patch(f"{TEST_FILE}.SmartMeterList", wraps=SmartMeterList) as mock_pyd_model:
            self.api.list_smart_meters(datalogger_sn=self.datalogger_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SmartMeterList.model_fields.items()} | set(
            SmartMeterList.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in SmartMeterListData.model_fields.items()} | set(
            SmartMeterListData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check data item
        if raw_data["data"]["count"] == 0:
            self.assertEqual([], raw_data["data"]["meters"], f"data_meters empty")
        else:
            pydantic_keys = {v.alias for k, v in SmartMeterData.model_fields.items()} | set(
                SmartMeterData.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["meters"][0].keys()).difference(pydantic_keys), f"data_meters_0"
            )
