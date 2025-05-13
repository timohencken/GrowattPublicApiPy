import unittest
from datetime import timedelta
from unittest import skip
from unittest.mock import patch

from growatt_public_api import GrowattApiSession, Inverter
from pydantic_models import InverterAlarms
from pydantic_models.inverter import (
    InverterAlarmsData,
    InverterAlarm,
    InverterDetails,
    InverterDetailData,
    InverterEnergyOverview,
    InverterEnergyOverviewData,
    InverterEnergyHistoryDataItem,
    InverterEnergyHistoryData,
    InverterEnergyHistory,
    InverterEnergyOverviewMultiple,
    InverterEnergyOverviewMultipleItem,
    InverterSettingRead,
    InverterSettingWrite,
)


TEST_FILE = "inverter.inverter"


# noinspection DuplicatedCode
class TestInverter(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Inverter = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        gas = GrowattApiSession.using_test_server_v1()
        cls.api = Inverter(session=gas)
        cls.device_sn = "SASF819012"

    def test_alarms(self):
        with patch(f"{TEST_FILE}.InverterAlarms", wraps=InverterAlarms) as mock_pyd_model:
            self.api.alarms(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterAlarms.model_fields.items()} | set(
            InverterAlarms.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in InverterAlarmsData.model_fields.items()} | set(
            InverterAlarmsData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no alarms, there are no alarms
            self.assertEqual([], raw_data["data"]["alarms"])
        else:
            # check alarms
            pydantic_keys = {v.alias for k, v in InverterAlarm.model_fields.items()} | set(
                InverterAlarm.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["alarms"][0].keys()).difference(pydantic_keys), "data_alarms_0"
            )

    def test_details(self):
        with patch(f"{TEST_FILE}.InverterDetails", wraps=InverterDetails) as mock_pyd_model:
            self.api.details(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterDetails.model_fields.items()} | set(
            InverterDetails.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in InverterDetailData.model_fields.items()} | set(
            InverterDetailData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    def test_energy(self):
        with patch(f"{TEST_FILE}.InverterEnergyOverview", wraps=InverterEnergyOverview) as mock_pyd_model:
            self.api.energy(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterEnergyOverview.model_fields.items()} | set(
            InverterEnergyOverview.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in InverterEnergyOverviewData.model_fields.items()} | set(
            InverterEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    def test_energy_history(self):
        # get date with data
        _details = self.api.details(device_sn=self.device_sn)
        _last_ts = _details.data.last_update_time_text

        with patch(f"{TEST_FILE}.InverterEnergyHistory", wraps=InverterEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                device_sn=self.device_sn, start_date=_last_ts.date() - timedelta(days=6), end_date=_last_ts.date()
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterEnergyHistory.model_fields.items()} | set(
            InverterEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in InverterEnergyHistoryData.model_fields.items()} | set(
            InverterEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        pydantic_keys = {v.alias for k, v in InverterEnergyHistoryDataItem.model_fields.items()} | set(
            InverterEnergyHistoryDataItem.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")

    def test_energy_multiple(self):
        with (
            patch(
                f"{TEST_FILE}.InverterEnergyOverviewMultiple", wraps=InverterEnergyOverviewMultiple
            ) as mock_pyd_model,
            patch(
                f"{TEST_FILE}.InverterEnergyOverviewMultipleItem", wraps=InverterEnergyOverviewMultipleItem
            ) as mock_pyd_model_multiple,
        ):
            self.api.energy_multiple(device_sn=self.device_sn)

        # check pre-parsed "multiple" data
        multiple_kwargs = mock_pyd_model_multiple.call_args.kwargs
        self.assertEqual({"data", "device_sn", "datalogger_sn"}, set(multiple_kwargs.keys()))
        self.assertEqual(self.device_sn, multiple_kwargs["device_sn"])
        self.assertIsNotNone(multiple_kwargs["datalogger_sn"])
        multiple_data = multiple_kwargs["data"]
        pydantic_keys = {v.alias for k, v in InverterEnergyOverviewData.model_fields.items()} | set(
            InverterEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(multiple_data.keys()).difference(pydantic_keys), "parsed_multiple_data")

        # check actual return value
        raw_data = mock_pyd_model.model_validate.call_args.args[0]
        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterEnergyOverviewMultiple.model_fields.items()} | set(
            InverterEnergyOverviewMultiple.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)

    @skip("Currently no type=1 inverter devices on test environment")
    def test_setting_read__by_name(self):
        with patch(f"{TEST_FILE}.InverterSettingRead", wraps=InverterSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, parameter_id="pv_on_off")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterSettingRead.model_fields.items()} | set(
            InverterSettingRead.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # should return empty string if communication could not be established
        if raw_data["error_code"] == 10003:
            self.assertEqual("", raw_data["data"])
        else:
            self.assertIsNotNone(raw_data["data"])
            self.assertNotEqual("", raw_data["data"])

    @skip("Currently no type=1 inverter devices on test environment")
    def test_setting_read__by_register(self):
        with patch(f"{TEST_FILE}.InverterSettingRead", wraps=InverterSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, start_address=0, end_address=0)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterSettingRead.model_fields.items()} | set(
            InverterSettingRead.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # should return empty string if communication could not be established
        if raw_data["error_code"] == 10003:
            self.assertEqual("", raw_data["data"])
        else:
            self.assertIsNotNone(raw_data["data"])
            self.assertNotEqual("", raw_data["data"])

    @skip("Currently no type=1 inverter devices on test environment")
    def test_setting_write__by_name(self):
        with patch(f"{TEST_FILE}.InverterSettingWrite", wraps=InverterSettingWrite) as mock_pyd_model:
            self.api.setting_write(device_sn=self.device_sn, parameter_id="tlx_on_off", parameter_value_1=1)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterSettingWrite.model_fields.items()} | set(
            InverterSettingWrite.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        if raw_data["error_code"] == 10003:
            # should return empty string if communication could not be established
            self.assertEqual("", raw_data["data"])
        else:
            # should anything but None if successful
            self.assertIsNotNone(raw_data["data"])

    @skip("Currently no type=1 inverter devices on test environment")
    def test_setting_write__by_register(self):
        with patch(f"{TEST_FILE}.InverterSettingWrite", wraps=InverterSettingWrite) as mock_pyd_model:
            self.api.setting_write(
                device_sn=self.device_sn, parameter_id="set_any_reg", parameter_value_1=0, parameter_value_2=1
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterSettingWrite.model_fields.items()} | set(
            InverterSettingWrite.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        if raw_data["error_code"] == 10003:
            # should return empty string if communication could not be established
            self.assertEqual("", raw_data["data"])
        else:
            # should anything but None if successful
            self.assertIsNotNone(raw_data["data"])
