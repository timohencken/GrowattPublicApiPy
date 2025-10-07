import os
import unittest
from datetime import time
from unittest import skip
from unittest.mock import patch

from growatt_public_api.growatt_api import GrowattApi
from loguru import logger

from growatt_public_api import GrowattApiSession, Device, Noah
from growatt_public_api.pydantic_models.api_v4 import (
    SettingWriteV4,
    NoahDetailsV4,
    NoahDetailsDataV4,
    NoahDetailDataV4,
    NoahEnergyV4,
    NoahEnergyOverviewDataV4,
    NoahEnergyDataV4,
    NoahEnergyHistoryV4,
    NoahEnergyHistoryDataV4,
    NoahEnergyHistoryMultipleV4,
    PowerV4,
    WifiStrengthV4,
)
from growatt_public_api.pydantic_models.noah import (
    NoahStatus,
    NoahBatteryStatus,
    NoahSettings,
    NoahPowerChart,
    NoahEnergyChart,
    NoahFirmwareInfo,
)


TEST_FILE = "growatt_public_api.noah.noah"
TEST_FILE_V4 = "growatt_public_api.api_v4.api_v4"


# noinspection DuplicatedCode
class TestNoah(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Noah = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        API_TOKEN = os.environ.get("GROWATTAPITOKEN")
        if API_TOKEN:
            api = GrowattApi(token=API_TOKEN)
            cls.api = api.noah
            devices = api.device.list()
            # get first NOAH device
            noah_device_sns = [d.device_sn for d in devices.data.data if d.device_type == "noah"]
            assert len(noah_device_sns) > 0, "No NOAH device found"
            cls.device_sn = noah_device_sns[0]
            print(f"Using NOAH device {cls.device_sn} from production server")
        else:
            # init API
            gas = GrowattApiSession.using_test_server_v4()
            # init
            cls.api = Noah(session=gas)
            # get a device
            try:
                api_device = Device(session=gas)
                _devices = api_device.list()
                sn_list = [x.device_sn for x in _devices.data.data if x.device_type == "noah"]
                cls.device_sn = sn_list[0]
                print(f"Using NOAH device {cls.device_sn} from test server")
            except (IndexError, AttributeError):
                # unfortunately, there is no NOAH device available at the test APIs :(
                logger.error("No NOAH device found in test API")
                cls.device_sn = ""

    def test_details_v4(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE_V4}.NoahDetailsV4", wraps=NoahDetailsV4) as mock_pyd_model:
            self.api.details_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahDetailsV4.model_fields.items()} | set(
            NoahDetailsV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in NoahDetailsDataV4.model_fields.items()} | set(
            NoahDetailsDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        pydantic_keys = {v.alias for k, v in NoahDetailDataV4.model_fields.items()} | set(
            NoahDetailDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["noah"][0].keys()).difference(pydantic_keys), "data_noah_0")

    def test_energy_v4(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE_V4}.NoahEnergyV4", wraps=NoahEnergyV4) as mock_pyd_model:
            self.api.energy_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahEnergyV4.model_fields.items()} | set(
            NoahEnergyV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in NoahEnergyOverviewDataV4.model_fields.items()} | set(
            NoahEnergyOverviewDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        if raw_data["data"]["noah"]:
            pydantic_keys = {v.alias for k, v in NoahEnergyDataV4.model_fields.items()} | set(
                NoahEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["noah"][0].keys()).difference(pydantic_keys), "data_noah_0")
        else:
            self.assertEqual([], raw_data["data"]["noah"], "no data")

    def test_power(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE_V4}.PowerV4", wraps=PowerV4) as mock_pyd_model:
            self.api.power(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PowerV4.model_fields.items()} | set(
            PowerV4.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        self.assertTrue(
            (raw_data["data"] is None) or (isinstance(raw_data["data"], int)) or (isinstance(raw_data["data"], float))
        )

    def test_energy_history_v4(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.NoahEnergyHistoryV4", wraps=NoahEnergyHistoryV4) as mock_pyd_model:
            self.api.energy_history_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahEnergyHistoryV4.model_fields.items()} | set(
            NoahEnergyHistoryV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in NoahEnergyHistoryDataV4.model_fields.items()} | set(
            NoahEnergyHistoryDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        if raw_data["data"]["datas"]:
            pydantic_keys = {v.alias for k, v in NoahEnergyDataV4.model_fields.items()} | set(
                NoahEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], raw_data["data"]["datas"], "no data")

    def test_energy_history_multiple_v4(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.NoahEnergyHistoryMultipleV4", wraps=NoahEnergyHistoryMultipleV4) as mock_pyd_model:
            self.api.energy_history_multiple_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahEnergyHistoryMultipleV4.model_fields.items()} | set(
            NoahEnergyHistoryMultipleV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        self.assertEqual({self.device_sn}, set(raw_data["data"].keys()), "data")
        data_for_device = raw_data["data"][self.device_sn]
        # check datas
        if data_for_device:
            pydantic_keys = {v.alias for k, v in NoahEnergyDataV4.model_fields.items()} | set(
                NoahEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(data_for_device[0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], data_for_device, "no data")

    @skip("no NOAH device available on test servers")  # do not test write functions on production server
    def test_setting_write_active_power(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_active_power(device_sn=self.device_sn, active_power_watt=800)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    @skip("no NOAH device available on test servers")  # do not test write functions on production server
    def test_setting_write_soc_upper_limit(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_soc_upper_limit(device_sn=self.device_sn, soc_limit=100)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    @skip("no NOAH device available on test servers")  # do not test write functions on production server
    def test_setting_write_soc_lower_limit(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_soc_lower_limit(device_sn=self.device_sn, soc_limit=100)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    @skip("no NOAH device available on test servers")  # do not test write functions on production server
    def test_setting_write_time_period(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_time_period(
                device_sn=self.device_sn,
                time_period_nr=1,
                start_time=time(8, 0),
                end_time=time(12, 0),
                load_priority=True,
                power_watt=800,
                enabled=False,
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    @skip("no NOAH device available on test servers")  # do not test write functions on production server
    def test_setting_write_assign_inverter(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_assign_inverter(
                device_sn=self.device_sn,
                inverter_sn="NYR0N9W15U",
                inverter_model_id="0x0105",
                inverter_brand_name="Growatt",
                inverter_model_name="NEO 2000M-X2",
                inverter_type=0,
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    @skip("no NOAH device available on test servers")  # do not test write functions on production server
    def test_setting_write_grid_charging(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_grid_charging(
                device_sn=self.device_sn,
                grid_charging=True,
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    @skip("no NOAH device available on test servers")  # do not test write functions on production server
    def test_setting_write_off_grid(self):
        with patch(f"{TEST_FILE_V4}.SettingWriteV4", wraps=SettingWriteV4) as mock_pyd_model:
            self.api.setting_write_off_grid(
                device_sn=self.device_sn,
                off_grid=True,
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingWriteV4.model_fields.items()} | set(
            SettingWriteV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    def test_wifi_strength(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE_V4}.WifiStrengthV4", wraps=WifiStrengthV4) as mock_pyd_model:
            self.api.wifi_strength(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PowerV4.model_fields.items()} | set(
            PowerV4.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check pydantic conversion works
        WifiStrengthV4.model_validate(raw_data)

    def test_status(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE}.NoahStatus", wraps=NoahStatus) as mock_pyd_model:
            self.api.status(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahStatus.model_fields.items()} | set(
            NoahStatus.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check pydantic conversion works
        NoahStatus.model_validate(raw_data)

    def test_battery_status(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE}.NoahBatteryStatus", wraps=NoahBatteryStatus) as mock_pyd_model:
            self.api.battery_status(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahBatteryStatus.model_fields.items()} | set(
            NoahBatteryStatus.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

        # check pydantic conversion works
        NoahBatteryStatus.model_validate(raw_data)

    def test_settings(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE}.NoahSettings", wraps=NoahSettings) as mock_pyd_model:
            self.api.settings(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahSettings.model_fields.items()} | set(
            NoahSettings.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

        # check pydantic conversion works
        NoahSettings.model_validate(raw_data)

    def test_power_chart(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE}.NoahPowerChart", wraps=NoahPowerChart) as mock_pyd_model:
            self.api.power_chart(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahPowerChart.model_fields.items()} | set(
            NoahPowerChart.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

        # check pydantic conversion works
        NoahPowerChart.model_validate(raw_data)

    def test_energy_chart(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE}.NoahEnergyChart", wraps=NoahEnergyChart) as mock_pyd_model:
            self.api.energy_chart(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahEnergyChart.model_fields.items()} | set(
            NoahEnergyChart.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

        # check pydantic conversion works
        NoahEnergyChart.model_validate(raw_data)

    def test_firmware_version(self):
        if self.device_sn is None:
            self.skipTest("no NOAH device available")

        with patch(f"{TEST_FILE}.NoahFirmwareInfo", wraps=NoahFirmwareInfo) as mock_pyd_model:
            self.api.firmware_info(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in NoahFirmwareInfo.model_fields.items()} | set(
            NoahFirmwareInfo.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

        # check pydantic conversion works
        NoahFirmwareInfo.model_validate(raw_data)
