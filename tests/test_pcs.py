import unittest
from datetime import timedelta
from unittest import skip
from unittest.mock import patch

from growatt_public_api import GrowattApiSession
from growatt_public_api.pcs import Pcs
from growatt_public_api.pydantic_models.pcs import (
    PcsAlarms,
    PcsAlarmsData,
    PcsAlarm,
    PcsDetails,
    PcsDetailData,
    PcsEnergyOverview,
    PcsEnergyOverviewData,
    PcsEnergyHistory,
    PcsEnergyHistoryData,
)

TEST_FILE = "growatt_public_api.pcs.pcs"


# noinspection DuplicatedCode
class TestPcs(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Pcs = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):  # noqa: C901 'TestEnvSensor.setUp' is too complex (11)
        return  # "Currently no PCS device in test environment"

        # init API
        # noinspection PyUnreachableCode
        gas = GrowattApiSession.using_test_server_v1()
        # init DEVICE
        cls.api = Pcs(session=gas)
        cls.device_sn = ""  # "Currently no PBD device in test environment"

    @skip("Currently no PCS devices on test environment")
    def test_alarms(self):
        with patch(f"{TEST_FILE}.PcsAlarms", wraps=PcsAlarms) as mock_pyd_model:
            self.api.alarms(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PcsAlarms.model_fields.items()} | set(
            PcsAlarms.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in PcsAlarmsData.model_fields.items()} | set(
            PcsAlarmsData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no alarms, there are no alarms
            self.assertEqual([], raw_data["data"]["alarms"])
        else:
            # check alarms
            pydantic_keys = {v.alias for k, v in PcsAlarm.model_fields.items()} | set(PcsAlarm.model_fields.keys())
            self.assertEqual(
                set(), set(raw_data["data"]["alarms"][0].keys()).difference(pydantic_keys), "data_alarms_0"
            )

    @skip("Currently no PCS devices on test environment")
    def test_details(self):
        with patch(f"{TEST_FILE}.PcsDetails", wraps=PcsDetails) as mock_pyd_model:
            self.api.details(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PcsDetails.model_fields.items()} | set(
            PcsDetails.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in PcsDetailData.model_fields.items()} | set(
            PcsDetailData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    @skip("Currently no PCS devices on test environment")
    def test_energy(self):
        with patch(f"{TEST_FILE}.PcsEnergyOverview", wraps=PcsEnergyOverview) as mock_pyd_model:
            self.api.energy(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PcsEnergyOverview.model_fields.items()} | set(
            PcsEnergyOverview.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in PcsEnergyOverviewData.model_fields.items()} | set(
            PcsEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    @skip("Currently no PCS devices on test environment")
    def test_energy_history(self):
        # get date with data
        _details = self.api.details(device_sn=self.device_sn)
        _last_ts = _details.data.last_update_time_text

        with patch(f"{TEST_FILE}.PcsEnergyHistory", wraps=PcsEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                device_sn=self.device_sn, start_date=_last_ts.date() - timedelta(days=6), end_date=_last_ts.date()
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PcsEnergyHistory.model_fields.items()} | set(
            PcsEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in PcsEnergyHistoryData.model_fields.items()} | set(
            PcsEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        pydantic_keys = {v.alias for k, v in PcsEnergyOverviewData.model_fields.items()} | set(
            PcsEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
