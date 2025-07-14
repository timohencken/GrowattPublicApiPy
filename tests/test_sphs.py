import unittest
from unittest.mock import patch

from growatt_public_api import GrowattApiSession, Device, Sphs
from growatt_public_api.pydantic_models.api_v4 import (
    SettingWriteV4,
    SphsDetailsV4,
    SphsDetailsDataV4,
    SphsDetailDataV4,
    SphsEnergyV4,
    SphsEnergyOverviewDataV4,
    SphsEnergyDataV4,
    SphsEnergyHistoryV4,
    SphsEnergyHistoryDataV4,
    SphsEnergyHistoryMultipleV4,
)

TEST_FILE = "growatt_public_api.sphs.sphs"
TEST_FILE_V4 = "growatt_public_api.api_v4.api_v4"


# noinspection DuplicatedCode
class TestSphs(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Sphs = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession.using_test_server_v4()
        # init
        cls.api = Sphs(session=gas)
        # get a device
        try:
            api_device = Device(session=gas)
            _devices = api_device.list()
            sn_list = [x.device_sn for x in _devices.data.data if x.device_type == "sph-s"]
            cls.device_sn = sn_list[0]
        except AttributeError:
            cls.device_sn = "QWL0DC3002"

    def test_details_v4(self):
        with patch(f"{TEST_FILE_V4}.SphsDetailsV4", wraps=SphsDetailsV4) as mock_pyd_model:
            self.api.details_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphsDetailsV4.model_fields.items()} | set(
            SphsDetailsV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in SphsDetailsDataV4.model_fields.items()} | set(
            SphsDetailsDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        pydantic_keys = {v.alias for k, v in SphsDetailDataV4.model_fields.items()} | set(
            SphsDetailDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["sph-s"][0].keys()).difference(pydantic_keys), "data_wit_0")

    def test_energy_v4(self):
        with patch(f"{TEST_FILE_V4}.SphsEnergyV4", wraps=SphsEnergyV4) as mock_pyd_model:
            self.api.energy_v4(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphsEnergyV4.model_fields.items()} | set(
            SphsEnergyV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in SphsEnergyOverviewDataV4.model_fields.items()} | set(
            SphsEnergyOverviewDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check device type specific data
        if raw_data["data"]["sph-s"]:
            pydantic_keys = {v.alias for k, v in SphsEnergyDataV4.model_fields.items()} | set(
                SphsEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["sph-s"][0].keys()).difference(pydantic_keys), "data_wit_0")
        else:
            self.assertEqual([], raw_data["data"]["sph-s"], "no data")

    def test_energy_history_v4(self):
        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.SphsEnergyHistoryV4", wraps=SphsEnergyHistoryV4) as mock_pyd_model:
            self.api.energy_history_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphsEnergyHistoryV4.model_fields.items()} | set(
            SphsEnergyHistoryV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in SphsEnergyHistoryDataV4.model_fields.items()} | set(
            SphsEnergyHistoryDataV4.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        if raw_data["data"]["datas"]:
            pydantic_keys = {v.alias for k, v in SphsEnergyDataV4.model_fields.items()} | set(
                SphsEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], raw_data["data"]["datas"], "no data")

    def test_energy_history_multiple_v4(self):
        # get date with data
        _details = self.api.details_v4(device_sn=self.device_sn)
        _last_ts = _details.data.devices[0].last_update_time

        with patch(f"{TEST_FILE_V4}.SphsEnergyHistoryMultipleV4", wraps=SphsEnergyHistoryMultipleV4) as mock_pyd_model:
            self.api.energy_history_multiple_v4(device_sn=self.device_sn, date_=_last_ts.date())

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in SphsEnergyHistoryMultipleV4.model_fields.items()} | set(
            SphsEnergyHistoryMultipleV4.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        self.assertEqual({self.device_sn}, set(raw_data["data"].keys()), "data")
        data_for_device = raw_data["data"][self.device_sn]
        # check datas
        if data_for_device:
            pydantic_keys = {v.alias for k, v in SphsEnergyDataV4.model_fields.items()} | set(
                SphsEnergyDataV4.model_fields.keys()
            )
            self.assertEqual(set(), set(data_for_device[0].keys()).difference(pydantic_keys), "data_datas_0")
        else:
            self.assertEqual([], data_for_device, "no data")

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
