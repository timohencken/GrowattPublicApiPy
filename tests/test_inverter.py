import unittest
from datetime import timedelta
from unittest.mock import patch

from growatt_public_api import GrowattApiSession, Inverter
from growatt_public_api.pydantic_models import InverterAlarms
from growatt_public_api.pydantic_models.api_v4 import (
    InverterDetailDataV4,
    InverterDetailsDataV4,
    InverterDetailsV4,
    InverterEnergyV4,
    InverterEnergyOverviewDataV4,
    InverterEnergyDataV4,
    InverterEnergyHistoryV4,
    InverterEnergyHistoryDataV4,
    InverterEnergyHistoryMultipleV4,
    SettingWriteV4,
)
from growatt_public_api.pydantic_models.inverter import (
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


TEST_FILE = "growatt_public_api.inverter.inverter"
TEST_FILE_V4 = "growatt_public_api.api_v4.api_v4"


# noinspection DuplicatedCode
class TestInverter(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Inverter = None
    device_sn: str = None
    api_v4: Inverter = None
    device_sn_v4: str = None

    @classmethod
    def setUpClass(cls):
        cls.api = Inverter(session=GrowattApiSession.using_test_server_v1())
        cls.device_sn = "SASF819012"
        cls.api_v4 = Inverter(session=GrowattApiSession.using_test_server_v4())
        cls.device_sn_v4 = "NHB691514F"

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

    def test_details_v4(self):
        with patch(f"{TEST_FILE_V4}.InverterDetailsV4", wraps=InverterDetailsV4) as mock_pyd_model:
            self.api_v4.details_v4(device_sn=self.device_sn_v4)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterDetailsV4.model_fields.items()} | set(
            InverterDetailsV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in InverterDetailsDataV4.model_fields.items()} | set(
            InverterDetailsDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        pydantic_keys = {v.alias for k, v in InverterDetailDataV4.model_fields.items()} | set(
            InverterDetailDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["inv"][0].keys()).difference(pydantic_keys), "data_inv_0")

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

    def test_energy_v4(self):
        with patch(f"{TEST_FILE_V4}.InverterEnergyV4", wraps=InverterEnergyV4) as mock_pyd_model:
            self.api_v4.energy_v4(device_sn=self.device_sn_v4)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterEnergyV4.model_fields.items()} | set(
            InverterEnergyV4.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in InverterEnergyOverviewDataV4.model_fields.items()} | set(
            InverterEnergyOverviewDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        if raw_data["data"]["inv"]:
            pydantic_keys = {v.alias for k, v in InverterEnergyDataV4.model_fields.items()} | set(
                InverterEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["inv"][0].keys()).difference(pydantic_keys), "data_inv_0")
        else:
            self.assertEqual([], raw_data["data"]["inv"], "no data")

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

    def test_energy_history_v4(self):
        # get date with data
        _details = self.api_v4.details_v4(device_sn=self.device_sn_v4)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.InverterEnergyHistoryV4", wraps=InverterEnergyHistoryV4) as mock_pyd_model:
            self.api_v4.energy_history_v4(device_sn=self.device_sn_v4, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterEnergyHistoryV4.model_fields.items()} | set(
            InverterEnergyHistoryV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in InverterEnergyHistoryDataV4.model_fields.items()} | set(
            InverterEnergyHistoryDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        if raw_data["data"]["datas"]:
            pydantic_keys = {v.alias for k, v in InverterEnergyDataV4.model_fields.items()} | set(
                InverterEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], raw_data["data"]["datas"], "no data")

    def test_energy_history_multiple_v4(self):
        # get date with data
        _details = self.api_v4.details_v4(device_sn=self.device_sn_v4)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(
            f"{TEST_FILE_V4}.InverterEnergyHistoryMultipleV4", wraps=InverterEnergyHistoryMultipleV4
        ) as mock_pyd_model:
            self.api_v4.energy_history_multiple_v4(device_sn=self.device_sn_v4, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterEnergyHistoryMultipleV4.model_fields.items()} | set(
            InverterEnergyHistoryMultipleV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        self.assertEqual({self.device_sn_v4}, set(raw_data["data"].keys()), "data")
        data_for_device = raw_data["data"][self.device_sn_v4]
        # check datas
        if data_for_device:
            pydantic_keys = {v.alias for k, v in InverterEnergyDataV4.model_fields.items()} | set(
                InverterEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(data_for_device[0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], data_for_device, "no data")

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

    def test_setting_read__by_name(self):
        with patch(f"{TEST_FILE}.InverterSettingRead", wraps=InverterSettingRead) as mock_pyd_model:
            self.api_v4.setting_read(device_sn=self.device_sn_v4, parameter_id="pv_on_off")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterSettingRead.model_fields.items()} | set(
            InverterSettingRead.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # should return empty string if communication could not be established
        if raw_data["error_code"] > 0:
            self.assertEqual("", raw_data["data"])
        else:
            self.assertIsNotNone(raw_data["data"])
            self.assertNotEqual("", raw_data["data"])

    def test_setting_read__by_register(self):
        with patch(f"{TEST_FILE}.InverterSettingRead", wraps=InverterSettingRead) as mock_pyd_model:
            self.api_v4.setting_read(device_sn=self.device_sn_v4, start_address=0, end_address=0)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterSettingRead.model_fields.items()} | set(
            InverterSettingRead.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # should return empty string if communication could not be established
        if raw_data["error_code"] > 0:
            self.assertEqual("", raw_data["data"])
        else:
            self.assertIsNotNone(raw_data["data"])
            self.assertNotEqual("", raw_data["data"])

    def test_setting_write__by_name(self):
        with patch(f"{TEST_FILE}.InverterSettingWrite", wraps=InverterSettingWrite) as mock_pyd_model:
            self.api_v4.setting_write(device_sn=self.device_sn_v4, parameter_id="tlx_on_off", parameter_value_1=1)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterSettingWrite.model_fields.items()} | set(
            InverterSettingWrite.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        if raw_data["error_code"] > 0:
            # should return empty string if communication could not be established
            self.assertEqual("", raw_data["data"])
        else:
            # should anything but None if successful
            self.assertIsNotNone(raw_data["data"])

    def test_setting_write__by_register(self):
        with patch(f"{TEST_FILE}.InverterSettingWrite", wraps=InverterSettingWrite) as mock_pyd_model:
            self.api_v4.setting_write(
                device_sn=self.device_sn_v4, parameter_id="set_any_reg", parameter_value_1=0, parameter_value_2=1
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in InverterSettingWrite.model_fields.items()} | set(
            InverterSettingWrite.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        if raw_data["error_code"] > 0:
            # should return empty string if communication could not be established
            self.assertEqual("", raw_data["data"])
        else:
            # should anything but None if successful
            self.assertIsNotNone(raw_data["data"])

    def test_setting_write_on_off(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api_v4.setting_write_on_off(device_sn=self.device_sn_v4, power_on=True)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    def test_setting_write_active_power(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api_v4.setting_write_active_power(device_sn=self.device_sn_v4, active_power_percent=100)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
