import unittest
from datetime import timedelta
from unittest import skip
from unittest.mock import patch

from growatt_public_api import GrowattApiSession, Device
from growatt_public_api.pydantic_models.api_v4 import (
    SphDetailsV4,
    SphDetailsDataV4,
    SphDetailDataV4,
    SphEnergyV4,
    SphEnergyOverviewDataV4,
    SphEnergyDataV4,
    SphEnergyHistoryV4,
    SphEnergyHistoryDataV4,
    SphEnergyHistoryMultipleV4,
    SettingReadVppV4,
    SettingWriteV4,
)
from growatt_public_api.pydantic_models.sph import (
    SphAlarmsData,
    SphAlarms,
    SphAlarm,
    SphDetails,
    SphDetailData,
    SphSettingWrite,
    SphSettingRead,
    SphEnergyOverviewMultiple,
    SphEnergyOverviewData,
    SphEnergyOverviewMultipleItem,
    SphEnergyHistoryData,
    SphEnergyHistory,
    SphEnergyOverview,
)
from growatt_public_api.sph import Sph

TEST_FILE = "growatt_public_api.sph.sph"
TEST_FILE_V4 = "growatt_public_api.api_v4.api_v4"


# noinspection DuplicatedCode
class TestSph(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Sph = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession.using_test_server_v4()
        # init
        cls.api = Sph(session=gas)
        # get a device
        try:
            api_device = Device(session=gas)
            _devices = api_device.list()
            sn_list = [x.device_sn for x in _devices.data.data if x.device_type == "sph"]
            cls.device_sn = sn_list[0]
        except AttributeError:
            cls.device_sn = "AQM1234567"

    @skip(
        "We have a SPH in v4 test env (sn=AQM1234567), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_alarms(self):
        with patch(f"{TEST_FILE}.SphAlarms", wraps=SphAlarms) as mock_pyd_model:
            self.api.alarms(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphAlarms.model_fields.items()} | set(
            SphAlarms.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in SphAlarmsData.model_fields.items()} | set(
            SphAlarmsData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no alarms, there are no alarms
            self.assertEqual([], raw_data["data"]["alarms"])
        else:
            # check alarms
            pydantic_keys = {v.alias for k, v in SphAlarm.model_fields.items()} | set(SphAlarm.model_fields.keys())
            self.assertEqual(
                set(), set(raw_data["data"]["alarms"][0].keys()).difference(pydantic_keys), "data_alarms_0"
            )

    @skip(
        "We have a SPH in v4 test env (sn=AQM1234567), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_details(self):
        with patch(f"{TEST_FILE}.SphDetails", wraps=SphDetails) as mock_pyd_model:
            self.api.details(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphDetails.model_fields.items()} | set(
            SphDetails.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in SphDetailData.model_fields.items()} | set(
            SphDetailData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    def test_details_v4(self):
        with patch(f"{TEST_FILE_V4}.SphDetailsV4", wraps=SphDetailsV4) as mock_pyd_model:
            self.api.details_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphDetailsV4.model_fields.items()} | set(
            SphDetailsV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in SphDetailsDataV4.model_fields.items()} | set(
            SphDetailsDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        pydantic_keys = {v.alias for k, v in SphDetailDataV4.model_fields.items()} | set(
            SphDetailDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["sph"][0].keys()).difference(pydantic_keys), "data_sph_0")

    @skip(
        "We have a SPH in v4 test env (sn=AQM1234567), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_energy(self):
        with patch(f"{TEST_FILE}.SphEnergyOverview", wraps=SphEnergyOverview) as mock_pyd_model:
            self.api.energy(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphEnergyOverview.model_fields.items()} | set(
            SphEnergyOverview.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in SphEnergyOverviewData.model_fields.items()} | set(
            SphEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    def test_energy_v4(self):
        with patch(f"{TEST_FILE_V4}.SphEnergyV4", wraps=SphEnergyV4) as mock_pyd_model:
            self.api.energy_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphEnergyV4.model_fields.items()} | set(
            SphEnergyV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in SphEnergyOverviewDataV4.model_fields.items()} | set(
            SphEnergyOverviewDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        if raw_data["data"]["sph"]:
            pydantic_keys = {v.alias for k, v in SphEnergyDataV4.model_fields.items()} | set(
                SphEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["sph"][0].keys()).difference(pydantic_keys), "data_sph_0")
        else:
            self.assertEqual([], raw_data["data"]["sph"], "no data")

    @skip(
        "We have a SPH in v4 test env (sn=AQM1234567), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_energy_history(self):
        # get date with data
        _details = self.api.details(device_sn=self.device_sn)
        _last_ts = _details.data.last_update_time_text

        with patch(f"{TEST_FILE}.SphEnergyHistory", wraps=SphEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                device_sn=self.device_sn, start_date=_last_ts.date() - timedelta(days=6), end_date=_last_ts.date()
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphEnergyHistory.model_fields.items()} | set(
            SphEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in SphEnergyHistoryData.model_fields.items()} | set(
            SphEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        pydantic_keys = {v.alias for k, v in SphEnergyOverviewData.model_fields.items()} | set(
            SphEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")

    def test_energy_history_v4(self):
        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.SphEnergyHistoryV4", wraps=SphEnergyHistoryV4) as mock_pyd_model:
            self.api.energy_history_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphEnergyHistoryV4.model_fields.items()} | set(
            SphEnergyHistoryV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in SphEnergyHistoryDataV4.model_fields.items()} | set(
            SphEnergyHistoryDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        if raw_data["data"]["datas"]:
            pydantic_keys = {v.alias for k, v in SphEnergyDataV4.model_fields.items()} | set(
                SphEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], raw_data["data"]["datas"], "no data")

    @skip(
        "We have a SPH in v4 test env (sn=AQM1234567), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_energy_multiple(self):
        with (
            patch(f"{TEST_FILE}.SphEnergyOverviewMultiple", wraps=SphEnergyOverviewMultiple) as mock_pyd_model,
            patch(
                f"{TEST_FILE}.SphEnergyOverviewMultipleItem", wraps=SphEnergyOverviewMultipleItem
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
        pydantic_keys = {v.alias for k, v in SphEnergyOverviewData.model_fields.items()} | set(
            SphEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(multiple_data.keys()).difference(pydantic_keys), "parsed_multiple_data")

        # check actual return value
        raw_data = mock_pyd_model.model_validate.call_args.args[0]
        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphEnergyOverviewMultiple.model_fields.items()} | set(
            SphEnergyOverviewMultiple.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)

    def test_energy_history_multiple_v4(self):
        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.SphEnergyHistoryMultipleV4", wraps=SphEnergyHistoryMultipleV4) as mock_pyd_model:
            self.api.energy_history_multiple_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphEnergyHistoryMultipleV4.model_fields.items()} | set(
            SphEnergyHistoryMultipleV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        self.assertEqual({self.device_sn}, set(raw_data["data"].keys()), "data")
        data_for_device = raw_data["data"][self.device_sn]
        # check datas
        if data_for_device:
            pydantic_keys = {v.alias for k, v in SphEnergyDataV4.model_fields.items()} | set(
                SphEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(data_for_device[0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], data_for_device, "no data")

    def test_setting_read__by_name(self):
        with patch(f"{TEST_FILE}.SphSettingRead", wraps=SphSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, parameter_id="pv_on_off")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphSettingRead.model_fields.items()} | set(
            SphSettingRead.model_fields.keys()
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
        with patch(f"{TEST_FILE}.SphSettingRead", wraps=SphSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, start_address=0, end_address=0)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphSettingRead.model_fields.items()} | set(
            SphSettingRead.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # should return empty string if communication could not be established
        if raw_data["error_code"] == 10003:
            self.assertEqual("", raw_data["data"])
        else:
            self.assertIsNotNone(raw_data["data"])
            self.assertNotEqual("", raw_data["data"])

    def test_setting_read_vpp_param(self):
        with patch(f"{TEST_FILE_V4}.SettingReadVppV4", wraps=SettingReadVppV4) as mock_pyd_model:
            self.api.setting_read_vpp_param(device_sn=self.device_sn, parameter_id="set_param_1")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingReadVppV4.model_fields.items()} | set(
            SettingReadVppV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    def test_setting_write__by_name(self):
        with patch(f"{TEST_FILE}.SphSettingWrite", wraps=SphSettingWrite) as mock_pyd_model:
            self.api.setting_write(device_sn=self.device_sn, parameter_id="pv_on_off", parameter_value_1=1)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphSettingWrite.model_fields.items()} | set(
            SphSettingWrite.model_fields.keys()
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
        with patch(f"{TEST_FILE}.SphSettingWrite", wraps=SphSettingWrite) as mock_pyd_model:
            self.api.setting_write(
                device_sn=self.device_sn, parameter_id="set_any_reg", parameter_value_1=0, parameter_value_2=1
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphSettingWrite.model_fields.items()} | set(
            SphSettingWrite.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        if raw_data["error_code"] == 10003:
            # should return empty string if communication could not be established
            self.assertEqual("", raw_data["data"])
        else:
            # should anything but None if successful
            self.assertIsNotNone(raw_data["data"])

    def test_setting_write_on_off(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_on_off(device_sn=self.device_sn, power_on=True)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    def test_setting_write_active_power(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_active_power(device_sn=self.device_sn, active_power_percent=100)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    def test_setting_write_vpp_param(self):
        # test it
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_vpp_param(
                device_sn=self.device_sn,
                parameter_id="set_param_2",  # On off command
                value=1,  # 1 = power on (default)
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
