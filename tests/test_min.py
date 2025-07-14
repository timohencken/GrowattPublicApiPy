import unittest
from datetime import timedelta
from unittest.mock import patch

from growatt_public_api import GrowattApiSession, Device
from growatt_public_api.min import Min
from growatt_public_api.pydantic_models import MinDetails
from growatt_public_api.pydantic_models.api_v4 import (
    MinDetailsV4,
    MinDetailsDataV4,
    MinDetailDataV4,
    MinEnergyV4,
    MinEnergyOverviewDataV4,
    MinEnergyDataV4,
    MinEnergyHistoryDataV4,
    MinEnergyHistoryV4,
    MinEnergyHistoryMultipleV4,
    SettingWriteV4,
    SettingReadVppV4,
)
from growatt_public_api.pydantic_models.min import (
    MinDetailData,
    MinTlxSettingsData,
    MinEnergyOverview,
    MinEnergyHistory,
    MinEnergyHistoryData,
    MinEnergyOverviewData,
    MinEnergyOverviewMultiple,
    MinEnergyOverviewMultipleItem,
    MinSettingRead,
    MinSettingWrite,
    MinSettings,
    MinAlarms,
    MinAlarmsData,
    MinAlarm,
)


TEST_FILE = "growatt_public_api.min.min"
TEST_FILE_V4 = "growatt_public_api.api_v4.api_v4"


# noinspection DuplicatedCode
class TestMin(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Min = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession.using_test_server_v1()
        # init
        cls.api = Min(session=gas)
        # get a device
        try:
            api_device = Device(session=gas)
            _devices = api_device.list()
            sn_list = [x.device_sn for x in _devices.data.data if x.device_type == "min"]
            cls.device_sn = sn_list[0]
        except (AttributeError, IndexError):
            cls.device_sn = (
                "RUK0CAE00J"  # 'RUK0CAE00J', 'EVK0BHX111', 'GRT0010086', 'TAG1234567', 'YYX1235113', 'GRT1235003'
            )

    def test_alarms(self):
        with patch(f"{TEST_FILE}.MinAlarms", wraps=MinAlarms) as mock_pyd_model:
            self.api.alarms(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinAlarms.model_fields.items()} | set(
            MinAlarms.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in MinAlarmsData.model_fields.items()} | set(
            MinAlarmsData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no alarms, there are no alarms
            self.assertEqual([], raw_data["data"]["alarms"])
        else:
            # check alarms
            pydantic_keys = {v.alias for k, v in MinAlarm.model_fields.items()} | set(MinAlarm.model_fields.keys())
            self.assertEqual(
                set(), set(raw_data["data"]["alarms"][0].keys()).difference(pydantic_keys), "data_alarms_0"
            )

    def test_details(self):
        with patch(f"{TEST_FILE}.MinDetails", wraps=MinDetails) as mock_pyd_model:
            self.api.details(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinDetails.model_fields.items()} | set(
            MinDetails.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in MinDetailData.model_fields.items()} | set(
            MinDetailData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check SetBean
        pydantic_keys = {v.alias for k, v in MinTlxSettingsData.model_fields.items()} | set(
            MinTlxSettingsData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["tlxSetbean"].keys()).difference(pydantic_keys), "tlxSetbean")

    def test_details_v4(self):
        with patch(f"{TEST_FILE_V4}.MinDetailsV4", wraps=MinDetailsV4) as mock_pyd_model:
            self.api.details_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinDetailsV4.model_fields.items()} | set(
            MinDetailsV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in MinDetailsDataV4.model_fields.items()} | set(
            MinDetailsDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        pydantic_keys = {v.alias for k, v in MinDetailDataV4.model_fields.items()} | set(
            MinDetailDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["min"][0].keys()).difference(pydantic_keys), "data_min_0")

    def test_energy(self):
        with patch(f"{TEST_FILE}.MinEnergyOverview", wraps=MinEnergyOverview) as mock_pyd_model:
            self.api.energy(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinEnergyOverview.model_fields.items()} | set(
            MinEnergyOverview.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in MinEnergyOverviewData.model_fields.items()} | set(
            MinEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    def test_energy_v4(self):
        with patch(f"{TEST_FILE_V4}.MinEnergyV4", wraps=MinEnergyV4) as mock_pyd_model:
            self.api.energy_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinEnergyV4.model_fields.items()} | set(
            MinEnergyV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in MinEnergyOverviewDataV4.model_fields.items()} | set(
            MinEnergyOverviewDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        if raw_data["data"]["min"]:
            pydantic_keys = {v.alias for k, v in MinEnergyDataV4.model_fields.items()} | set(
                MinEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["min"][0].keys()).difference(pydantic_keys), "data_min_0")
        else:
            self.assertEqual([], raw_data["data"]["min"], "no data")

    def test_energy_history(self):
        # get date with data
        _details = self.api.details(device_sn=self.device_sn)
        _last_ts = _details.data.last_update_time_text

        with patch(f"{TEST_FILE}.MinEnergyHistory", wraps=MinEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                device_sn=self.device_sn, start_date=_last_ts.date() - timedelta(days=6), end_date=_last_ts.date()
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinEnergyHistory.model_fields.items()} | set(
            MinEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in MinEnergyHistoryData.model_fields.items()} | set(
            MinEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        pydantic_keys = {v.alias for k, v in MinEnergyOverviewData.model_fields.items()} | set(
            MinEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")

    def test_energy_history_v4(self):
        # get date with data
        _details = self.api.details(device_sn=self.device_sn)
        _last_ts = _details.data.last_update_time_text

        with patch(f"{TEST_FILE_V4}.MinEnergyHistoryV4", wraps=MinEnergyHistoryV4) as mock_pyd_model:
            self.api.energy_history_v4(device_sn=self.device_sn, date_=_last_ts.date() - timedelta(days=1))

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinEnergyHistoryV4.model_fields.items()} | set(
            MinEnergyHistoryV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in MinEnergyHistoryDataV4.model_fields.items()} | set(
            MinEnergyHistoryDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        if raw_data["data"]["datas"]:
            pydantic_keys = {v.alias for k, v in MinEnergyDataV4.model_fields.items()} | set(
                MinEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], raw_data["data"]["datas"], "no data")

    def test_energy_history_multiple_v4(self):
        # get date with data
        _details = self.api.details(device_sn=self.device_sn)
        _last_ts = _details.data.last_update_time_text

        with patch(f"{TEST_FILE_V4}.MinEnergyHistoryMultipleV4", wraps=MinEnergyHistoryMultipleV4) as mock_pyd_model:
            self.api.energy_history_multiple_v4(device_sn=self.device_sn, date_=_last_ts.date() - timedelta(days=1))

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinEnergyHistoryMultipleV4.model_fields.items()} | set(
            MinEnergyHistoryMultipleV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        self.assertEqual({self.device_sn}, set(raw_data["data"].keys()), "data")
        data_for_device = raw_data["data"][self.device_sn]
        # check datas
        if data_for_device:
            pydantic_keys = {v.alias for k, v in MinEnergyDataV4.model_fields.items()} | set(
                MinEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(data_for_device[0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], data_for_device, "no data")

    def test_energy_multiple(self):
        with (
            patch(f"{TEST_FILE}.MinEnergyOverviewMultiple", wraps=MinEnergyOverviewMultiple) as mock_pyd_model,
            patch(
                f"{TEST_FILE}.MinEnergyOverviewMultipleItem", wraps=MinEnergyOverviewMultipleItem
            ) as mock_pyd_model_multiple,
        ):
            self.api.energy_multiple(device_sn=self.device_sn)

        # check pre-parsed "multiple" data
        multiple_kwargs = mock_pyd_model_multiple.call_args.kwargs
        self.assertEqual({"data", "device_sn", "datalogger_sn"}, set(multiple_kwargs.keys()))
        self.assertEqual(self.device_sn, multiple_kwargs["device_sn"])
        self.assertIsNotNone(multiple_kwargs["datalogger_sn"])
        multiple_data = multiple_kwargs["data"]
        pydantic_keys = {v.alias for k, v in MinEnergyOverviewData.model_fields.items()} | set(
            MinEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(multiple_data.keys()).difference(pydantic_keys), "parsed_multiple_data")

        # check actual return value
        raw_data = mock_pyd_model.model_validate.call_args.args[0]
        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinEnergyOverviewMultiple.model_fields.items()} | set(
            MinEnergyOverviewMultiple.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)

    def test_setting_read__by_name(self):
        with patch(f"{TEST_FILE}.MinSettingRead", wraps=MinSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, parameter_id="tlx_on_off")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinSettingRead.model_fields.items()} | set(
            MinSettingRead.model_fields.keys()
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
        with patch(f"{TEST_FILE}.MinSettingRead", wraps=MinSettingRead) as mock_pyd_model:
            self.api.setting_read(device_sn=self.device_sn, start_address=0, end_address=0)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinSettingRead.model_fields.items()} | set(
            MinSettingRead.model_fields.keys()
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
        """
        This endpoint cannot be tested using the v1 test server (test.growatt.com), since it returns 404
        This endpoint is only available on the v4 test server (183.62.216.35:8081) and on the official server (openapi.growatt.com)
        """
        # use SPH device from v4 server
        api_server_v4 = Min(session=GrowattApiSession.using_test_server_v4())
        device_sn = "AQM1234567"  # actually not MIN but SPH -- but works fine

        # test it
        with patch(f"{TEST_FILE_V4}.SettingReadVppV4", wraps=SettingReadVppV4) as mock_pyd_model:
            api_server_v4.setting_read_vpp_param(device_sn=device_sn, parameter_id="set_param_1")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingReadVppV4.model_fields.items()} | set(
            SettingReadVppV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    def test_setting_write__by_name(self):
        with patch(f"{TEST_FILE}.MinSettingWrite", wraps=MinSettingWrite) as mock_pyd_model:
            self.api.setting_write(device_sn=self.device_sn, parameter_id="tlx_on_off", parameter_value_1=1)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinSettingWrite.model_fields.items()} | set(
            MinSettingWrite.model_fields.keys()
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
        with patch(f"{TEST_FILE}.MinSettingWrite", wraps=MinSettingWrite) as mock_pyd_model:
            self.api.setting_write(
                device_sn=self.device_sn, parameter_id="set_any_reg", parameter_value_1=0, parameter_value_2=1
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinSettingWrite.model_fields.items()} | set(
            MinSettingWrite.model_fields.keys()
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
        """
        This endpoint cannot be tested using the v1 test server (test.growatt.com), since it returns 404
        This endpoint is only available on the v4 test server (183.62.216.35:8081) and on the official server (openapi.growatt.com)
        """
        # use SPH device from v4 server
        api_server_v4 = Min(session=GrowattApiSession.using_test_server_v4())
        device_sn = "AQM1234567"  # actually not MIN but SPH -- but works fine

        # test it
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            api_server_v4.setting_write_vpp_param(
                device_sn=device_sn,
                parameter_id="set_param_2",  # On off command
                value=1,  # 1 = power on (default)
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    def test_settings(self):
        with patch(f"{TEST_FILE}.MinSettings", wraps=MinSettings) as mock_pyd_model:
            self.api.settings(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in MinSettings.model_fields.items()} | set(
            MinSettings.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in MinTlxSettingsData.model_fields.items()} | set(
            MinTlxSettingsData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
