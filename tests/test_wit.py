import unittest
from unittest.mock import patch

from growatt_public_api import GrowattApiSession, Device, Wit
from growatt_public_api.pydantic_models.api_v4 import (
    SettingReadVppV4,
    SettingWriteV4,
    WitDetailsV4,
    WitDetailsDataV4,
    WitDetailDataV4,
    WitEnergyV4,
    WitEnergyOverviewDataV4,
    WitEnergyDataV4,
    WitEnergyHistoryV4,
    WitEnergyHistoryDataV4,
    WitEnergyHistoryMultipleV4,
)

TEST_FILE = "growatt_public_api.wit.wit"
TEST_FILE_V4 = "growatt_public_api.api_v4.api_v4"


# noinspection DuplicatedCode
class TestWit(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Wit = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession.using_test_server_v4()
        # init
        cls.api = Wit(session=gas)
        # get a device
        try:
            api_device = Device(session=gas)
            _devices = api_device.list()
            sn_list = [x.device_sn for x in _devices.data.data if x.device_type == "wit"]
            cls.device_sn = sn_list[0]
        except AttributeError:
            cls.device_sn = "QWL0DC3002"

    def test_details_v4(self):
        with patch(f"{TEST_FILE_V4}.WitDetailsV4", wraps=WitDetailsV4) as mock_pyd_model:
            self.api.details_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in WitDetailsV4.model_fields.items()} | set(
            WitDetailsV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in WitDetailsDataV4.model_fields.items()} | set(
            WitDetailsDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        pydantic_keys = {v.alias for k, v in WitDetailDataV4.model_fields.items()} | set(
            WitDetailDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["wit"][0].keys()).difference(pydantic_keys), "data_wit_0")

    def test_energy_v4(self):
        with patch(f"{TEST_FILE_V4}.WitEnergyV4", wraps=WitEnergyV4) as mock_pyd_model:
            self.api.energy_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in WitEnergyV4.model_fields.items()} | set(
            WitEnergyV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in WitEnergyOverviewDataV4.model_fields.items()} | set(
            WitEnergyOverviewDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        if raw_data["data"]["wit"]:
            pydantic_keys = {v.alias for k, v in WitEnergyDataV4.model_fields.items()} | set(
                WitEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["wit"][0].keys()).difference(pydantic_keys), "data_wit_0")
        else:
            self.assertEqual([], raw_data["data"]["wit"], "no data")

    def test_energy_history_v4(self):
        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.WitEnergyHistoryV4", wraps=WitEnergyHistoryV4) as mock_pyd_model:
            self.api.energy_history_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in WitEnergyHistoryV4.model_fields.items()} | set(
            WitEnergyHistoryV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in WitEnergyHistoryDataV4.model_fields.items()} | set(
            WitEnergyHistoryDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        if raw_data["data"]["datas"]:
            pydantic_keys = {v.alias for k, v in WitEnergyDataV4.model_fields.items()} | set(
                WitEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], raw_data["data"]["datas"], "no data")

    def test_energy_history_multiple_v4(self):
        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.WitEnergyHistoryMultipleV4", wraps=WitEnergyHistoryMultipleV4) as mock_pyd_model:
            self.api.energy_history_multiple_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in WitEnergyHistoryMultipleV4.model_fields.items()} | set(
            WitEnergyHistoryMultipleV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        self.assertEqual({self.device_sn}, set(raw_data["data"].keys()), "data")
        data_for_device = raw_data["data"][self.device_sn]
        # check datas
        if data_for_device:
            pydantic_keys = {v.alias for k, v in WitEnergyDataV4.model_fields.items()} | set(
                WitEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(data_for_device[0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], data_for_device, "no data")

    def test_setting_read_vpp_param(self):
        with patch(f"{TEST_FILE_V4}.SettingReadVppV4", wraps=SettingReadVppV4) as mock_pyd_model:
            self.api.setting_read_vpp_param(device_sn=self.device_sn, parameter_id="set_param_1")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SettingReadVppV4.model_fields.items()} | set(
            SettingReadVppV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

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
