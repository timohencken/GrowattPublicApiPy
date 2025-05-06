import unittest
from datetime import timedelta
from unittest import skip
from unittest.mock import patch

from api_v4 import ApiV4
from growatt_public_api import GrowattApiSession
from pydantic_models.spa import (
    SpaAlarm,
    SpaAlarmsData,
    SpaAlarms,
    SpaDetailData,
    SpaDetails,
    SpaEnergyOverviewData,
    SpaEnergyOverview,
    SpaEnergyHistory,
    SpaEnergyHistoryData,
    SpaEnergyOverviewMultiple,
    SpaEnergyOverviewMultipleItem,
    SpaSettingRead,
    SpaSettingWrite,
)
from spa import Spa

TEST_FILE = "spa.spa"


# noinspection DuplicatedCode
class TestSpa(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Spa = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession(
            server_url="http://183.62.216.35:8081",
            token="wa265d2h1og0873ml07142r81564hho6",  # gitleaks:allow
        )
        # init
        cls.api = Spa(session=gas)
        # get a device
        try:
            apiv4 = ApiV4(session=gas)
            _devices = apiv4.list()
            sn_list = [x.device_sn for x in _devices.data.data if x.device_type == "spa"]
            cls.device_sn = sn_list[0]
        except AttributeError:
            cls.device_sn = "CHENYINSHU"

    @skip(
        "We have a SPA in v4 test env (sn=CHENYINSHU), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_alarms(self):
        with patch(f"{TEST_FILE}.SpaAlarms", wraps=SpaAlarms) as mock_pyd_model:
            self.api.alarms(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SpaAlarms.model_fields.items()} | set(
            SpaAlarms.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in SpaAlarmsData.model_fields.items()} | set(
            SpaAlarmsData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no alarms, there are no alarms
            self.assertEqual([], raw_data["data"]["alarms"])
        else:
            # check alarms
            pydantic_keys = {v.alias for k, v in SpaAlarm.model_fields.items()} | set(SpaAlarm.model_fields.keys())
            self.assertEqual(
                set(), set(raw_data["data"]["alarms"][0].keys()).difference(pydantic_keys), "data_alarms_0"
            )

    @skip(
        "We have a SPA in v4 test env (sn=CHENYINSHU), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_details(self):
        with patch(f"{TEST_FILE}.SpaDetails", wraps=SpaDetails) as mock_pyd_model:
            self.api.details(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SpaDetails.model_fields.items()} | set(
            SpaDetails.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in SpaDetailData.model_fields.items()} | set(
            SpaDetailData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    @skip(
        "We have a SPA in v4 test env (sn=CHENYINSHU), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_energy(self):
        with patch(f"{TEST_FILE}.SpaEnergyOverview", wraps=SpaEnergyOverview) as mock_pyd_model:
            self.api.energy(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SpaEnergyOverview.model_fields.items()} | set(
            SpaEnergyOverview.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in SpaEnergyOverviewData.model_fields.items()} | set(
            SpaEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    @skip(
        "We have a SPA in v4 test env (sn=CHENYINSHU), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_energy_history(self):
        # get date with data
        _details = self.api.details(device_sn=self.device_sn)
        _last_ts = _details.data.last_update_time_text

        with patch(f"{TEST_FILE}.SpaEnergyHistory", wraps=SpaEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                device_sn=self.device_sn, start_date=_last_ts.date() - timedelta(days=6), end_date=_last_ts.date()
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SpaEnergyHistory.model_fields.items()} | set(
            SpaEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in SpaEnergyHistoryData.model_fields.items()} | set(
            SpaEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        pydantic_keys = {v.alias for k, v in SpaEnergyOverviewData.model_fields.items()} | set(
            SpaEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")

    @skip(
        "We have a SPA in v4 test env (sn=CHENYINSHU), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_energy_multiple(self):
        with (
            patch(f"{TEST_FILE}.SpaEnergyOverviewMultiple", wraps=SpaEnergyOverviewMultiple) as mock_pyd_model,
            patch(
                f"{TEST_FILE}.SpaEnergyOverviewMultipleItem", wraps=SpaEnergyOverviewMultipleItem
            ) as mock_pyd_model_multiple,
        ):
            self.api.energy_multiple(device_sn=self.device_sn)

        # check pre-parsed "multiple" data
        self.assertGreaterEqual(mock_pyd_model_multiple.call_count, 1, "check at least one SPA device returned")
        multiple_kwargs = mock_pyd_model_multiple.call_args.kwargs
        self.assertEqual({"data", "device_sn", "datalogger_sn"}, set(multiple_kwargs.keys()))
        self.assertEqual(self.device_sn, multiple_kwargs["device_sn"])
        self.assertIsNotNone(multiple_kwargs["datalogger_sn"])
        multiple_data = multiple_kwargs["data"]
        pydantic_keys = {v.alias for k, v in SpaEnergyOverviewData.model_fields.items()} | set(
            SpaEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(multiple_data.keys()).difference(pydantic_keys), "parsed_multiple_data")

        # check actual return value
        raw_data = mock_pyd_model.model_validate.call_args.args[0]
        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SpaEnergyOverviewMultiple.model_fields.items()} | set(
            SpaEnergyOverviewMultiple.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)

    def test_setting_read__by_name(self):
        with patch(f"{TEST_FILE}.SpaSettingRead", wraps=SpaSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, parameter_id="pv_on_off")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SpaSettingRead.model_fields.items()} | set(
            SpaSettingRead.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # should return empty string if communication could not be established
        if raw_data["error_code"] == 10003:
            self.assertEqual("", raw_data["data"])
        else:
            self.assertIsNotNone(raw_data["data"])
            self.assertNotEqual("", raw_data["data"])

    def test_setting_read__by_register(self):
        with patch(f"{TEST_FILE}.SpaSettingRead", wraps=SpaSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, start_address=0, end_address=0)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SpaSettingRead.model_fields.items()} | set(
            SpaSettingRead.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # should return empty string if communication could not be established
        if raw_data["error_code"] == 10003:
            self.assertEqual("", raw_data["data"])
        else:
            self.assertIsNotNone(raw_data["data"])
            self.assertNotEqual("", raw_data["data"])

    def test_setting_write__by_name(self):
        with patch(f"{TEST_FILE}.SpaSettingWrite", wraps=SpaSettingWrite) as mock_pyd_model:
            self.api.setting_write(device_sn=self.device_sn, parameter_id="pv_on_off", parameter_value_1=1)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SpaSettingWrite.model_fields.items()} | set(
            SpaSettingWrite.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        if raw_data["error_code"] == 10003:
            # should return empty string if communication could not be established
            self.assertEqual("", raw_data["data"])
        else:
            # should anything but None if successful
            self.assertIsNotNone(raw_data["data"])

    def test_setting_write__by_register(self):
        with patch(f"{TEST_FILE}.SpaSettingWrite", wraps=SpaSettingWrite) as mock_pyd_model:
            self.api.setting_write(
                device_sn=self.device_sn, parameter_id="set_any_reg", parameter_value_1=0, parameter_value_2=1
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SpaSettingWrite.model_fields.items()} | set(
            SpaSettingWrite.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        if raw_data["error_code"] == 10003:
            # should return empty string if communication could not be established
            self.assertEqual("", raw_data["data"])
        else:
            # should anything but None if successful
            self.assertIsNotNone(raw_data["data"])
