import unittest
from datetime import timedelta
from unittest import skip
from unittest.mock import patch

from growatt_public_api import GrowattApiSession, Storage, Device
from growatt_public_api.pydantic_models import StorageAlarms
from growatt_public_api.pydantic_models.api_v4 import (
    StorageDetailsV4,
    StorageDetailDataV4,
    StorageDetailsDataV4,
    StorageEnergyV4,
    StorageEnergyOverviewDataV4,
    StorageEnergyDataV4,
    StorageEnergyHistoryV4,
    StorageEnergyHistoryDataV4,
    StorageEnergyHistoryMultipleV4,
    SettingWriteV4,
)
from growatt_public_api.pydantic_models.storage import (
    StorageAlarmsData,
    StorageAlarm,
    StorageDetails,
    StorageDetailData,
    StorageEnergyOverview,
    StorageEnergyOverviewData,
    StorageEnergyHistory,
    StorageEnergyHistoryData,
    StorageSettingRead,
    StorageSettingWrite,
)

TEST_FILE = "growatt_public_api.storage.storage"
TEST_FILE_V4 = "growatt_public_api.api_v4.api_v4"


class TestStorage(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Storage = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession.using_test_server_v4()
        # init
        cls.api = Storage(session=gas)
        # get a device
        try:
            api_device = Device(session=gas)
            _devices = api_device.list()
            sn_list = [x.device_sn for x in _devices.data.data if x.device_type == "storage"]
            cls.device_sn = sn_list[0]
        except AttributeError:
            cls.device_sn = "KHMOCM5688"

    @skip(
        "We have a STORAGE in v4 test env (sn=KHMOCM5688), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_alarms(self):
        with patch(f"{TEST_FILE}.StorageAlarms", wraps=StorageAlarms) as mock_pyd_model:
            self.api.alarms(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageAlarms.model_fields.items()} | set(
            StorageAlarms.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in StorageAlarmsData.model_fields.items()} | set(
            StorageAlarmsData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no alarms, there are no alarms
            self.assertEqual([], raw_data["data"]["alarms"])
        else:
            # check alarms
            pydantic_keys = {v.alias for k, v in StorageAlarm.model_fields.items()} | set(
                StorageAlarm.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["alarms"][0].keys()).difference(pydantic_keys), "data_alarms_0"
            )

    @skip(
        "We have a STORAGE in v4 test env (sn=KHMOCM5688), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_details(self):
        with patch(f"{TEST_FILE}.StorageDetails", wraps=StorageDetails) as mock_pyd_model:
            self.api.details(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageDetails.model_fields.items()} | set(
            StorageDetails.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in StorageDetailData.model_fields.items()} | set(
            StorageDetailData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    def test_details_v4(self):
        with patch(f"{TEST_FILE_V4}.StorageDetailsV4", wraps=StorageDetailsV4) as mock_pyd_model:
            self.api.details_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageDetailsV4.model_fields.items()} | set(
            StorageDetailsV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in StorageDetailsDataV4.model_fields.items()} | set(
            StorageDetailsDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        pydantic_keys = {v.alias for k, v in StorageDetailDataV4.model_fields.items()} | set(
            StorageDetailDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["storage"][0].keys()).difference(pydantic_keys), "data_storage_0")

    @skip(
        "We have a STORAGE in v4 test env (sn=KHMOCM5688), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_energy(self):
        with patch(f"{TEST_FILE}.StorageEnergyOverview", wraps=StorageEnergyOverview) as mock_pyd_model:
            self.api.energy(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageEnergyOverview.model_fields.items()} | set(
            StorageEnergyOverview.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in StorageEnergyOverviewData.model_fields.items()} | set(
            StorageEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    def test_energy_v4(self):
        with patch(f"{TEST_FILE_V4}.StorageEnergyV4", wraps=StorageEnergyV4) as mock_pyd_model:
            self.api.energy_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageEnergyV4.model_fields.items()} | set(
            StorageEnergyV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in StorageEnergyOverviewDataV4.model_fields.items()} | set(
            StorageEnergyOverviewDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        if raw_data["data"]["storage"]:
            pydantic_keys = {v.alias for k, v in StorageEnergyDataV4.model_fields.items()} | set(
                StorageEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["storage"][0].keys()).difference(pydantic_keys), "data_storage_0"
            )
        else:
            self.assertEqual([], raw_data["data"]["storage"], "no data")

    @skip(
        "We have a STORAGE in v4 test env (sn=KHMOCM5688), but it returns 'error_permission_denied' when using v1 API calls"
    )
    def test_energy_history(self):
        # get date with data
        _details = self.api.details(device_sn=self.device_sn)
        _last_ts = _details.data.last_update_time_text

        with patch(f"{TEST_FILE}.StorageEnergyHistory", wraps=StorageEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                device_sn=self.device_sn, start_date=_last_ts.date() - timedelta(days=6), end_date=_last_ts.date()
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageEnergyHistory.model_fields.items()} | set(
            StorageEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in StorageEnergyHistoryData.model_fields.items()} | set(
            StorageEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        pydantic_keys = {v.alias for k, v in StorageEnergyOverviewData.model_fields.items()} | set(
            StorageEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")

    def test_energy_history_v4(self):
        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.StorageEnergyHistoryV4", wraps=StorageEnergyHistoryV4) as mock_pyd_model:
            self.api.energy_history_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageEnergyHistoryV4.model_fields.items()} | set(
            StorageEnergyHistoryV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in StorageEnergyHistoryDataV4.model_fields.items()} | set(
            StorageEnergyHistoryDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        if raw_data["data"]["datas"]:
            pydantic_keys = {v.alias for k, v in StorageEnergyDataV4.model_fields.items()} | set(
                StorageEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], raw_data["data"]["datas"], "no data")

    def test_energy_history_multiple_v4(self):
        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(
            f"{TEST_FILE_V4}.StorageEnergyHistoryMultipleV4", wraps=StorageEnergyHistoryMultipleV4
        ) as mock_pyd_model:
            self.api.energy_history_multiple_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageEnergyHistoryMultipleV4.model_fields.items()} | set(
            StorageEnergyHistoryMultipleV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        self.assertEqual({self.device_sn}, set(raw_data["data"].keys()), "data")
        data_for_device = raw_data["data"][self.device_sn]
        # check datas
        if data_for_device:
            pydantic_keys = {v.alias for k, v in StorageEnergyDataV4.model_fields.items()} | set(
                StorageEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(data_for_device[0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], data_for_device, "no data")

    def test_setting_read__by_name(self):
        with patch(f"{TEST_FILE}.StorageSettingRead", wraps=StorageSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, parameter_id="storage_cmd_on_off")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageSettingRead.model_fields.items()} | set(
            StorageSettingRead.model_fields.keys()
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
        with patch(f"{TEST_FILE}.StorageSettingRead", wraps=StorageSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, start_address=0, end_address=0)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageSettingRead.model_fields.items()} | set(
            StorageSettingRead.model_fields.keys()
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
        with patch(f"{TEST_FILE}.StorageSettingWrite", wraps=StorageSettingWrite) as mock_pyd_model:
            self.api.setting_write(device_sn=self.device_sn, parameter_id="storage_cmd_on_off", parameter_value_1=1)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageSettingWrite.model_fields.items()} | set(
            StorageSettingWrite.model_fields.keys()
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
        with patch(f"{TEST_FILE}.StorageSettingWrite", wraps=StorageSettingWrite) as mock_pyd_model:
            self.api.setting_write(
                device_sn=self.device_sn, parameter_id="set_any_reg", parameter_value_1=0, parameter_value_2=1
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in StorageSettingWrite.model_fields.items()} | set(
            StorageSettingWrite.model_fields.keys()
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
