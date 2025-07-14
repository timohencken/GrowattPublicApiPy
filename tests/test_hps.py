import unittest
from datetime import timedelta
from unittest import skip
from unittest.mock import patch

from growatt_public_api import GrowattApiSession, Plant, Device
from growatt_public_api.hps import Hps
from growatt_public_api.pydantic_models import HpsAlarms
from growatt_public_api.pydantic_models.hps import (
    HpsAlarmsData,
    HpsAlarm,
    HpsDetails,
    HpsDetailData,
    HpsEnergyOverview,
    HpsEnergyOverviewData,
    HpsEnergyHistoryData,
    HpsEnergyHistory,
)


TEST_FILE = "growatt_public_api.hps.hps"


# noinspection DuplicatedCode
class TestMin(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Hps = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):  # noqa: C901 'TestEnvSensor.setUp' is too complex (11)
        return  # "Currently no environmental sensor found in test environment"

        # init API
        # noinspection PyUnreachableCode
        gas = GrowattApiSession.using_test_server_v1()
        # init DEVICE
        cls.api = Hps(session=gas)
        # get a DEVICE device
        # ENV sensors are only available on the old API
        # so we need to get all plants and then iterate its devices until we find an environmental sensor
        api_plant = Plant(session=gas)
        plant_ids = []
        for page in range(1, 100):
            plants = api_plant.list(limit=100, page=page)
            plant_count = plants.data.count
            # noinspection PyUnresolvedReferences
            plant_ids.extend([x.plant_id for x in plants.data.plants])
            print(f"retrieved {len(plant_ids)} plants")
            if len(plant_ids) >= plant_count:
                break
        # iterate plants, search for env (start with the newest plant)
        api_device = Device(session=gas)
        print(f"searching plants for correct device")
        plant_devices = {}
        type_9_devices = []
        for idx, plant_id in enumerate(reversed(plant_ids)):
            print(f"\rscanning plant {idx+1}/{len(plant_ids)} with {plant_id=}", end="")
            devices = api_device.list(plant_id=plant_id)
            if devices.data.count == 0:
                continue
            print(f"\nfound {devices.data.count} devices in {plant_id=}")
            plant_devices[plant_id] = devices.data.devices
            for device in devices.data.devices:
                if device.type == 9:
                    device_sn = device.device_sn
                    print(f"\ndetected device of type=9 with {device_sn=} {plant_id=}")
                    type_9_devices.append(
                        {
                            "plant_id": plant_id,
                            "device_sn": device_sn,
                        }
                    )
        print(f"\rscanned {len(plant_ids)} plants")
        print(f"Found {len(type_9_devices)} devices with type='HPS'")
        if len(type_9_devices) > 0:
            # take the first one
            cls.device_sn = type_9_devices[0]["device_sn"]
            print(f"using {cls.device_sn=}")
        else:
            print("Could not find any HPS in devices")
            print(plant_devices)
            raise AttributeError("No HPS devices found in test environment")

    @skip("Currently no HPS devices on test environment")
    def test_alarms(self):
        with patch(f"{TEST_FILE}.HpsAlarms", wraps=HpsAlarms) as mock_pyd_model:
            self.api.alarms(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in HpsAlarms.model_fields.items()} | set(
            HpsAlarms.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in HpsAlarmsData.model_fields.items()} | set(
            HpsAlarmsData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no alarms, there are no alarms
            self.assertEqual([], raw_data["data"]["alarms"])
        else:
            # check alarms
            pydantic_keys = {v.alias for k, v in HpsAlarm.model_fields.items()} | set(HpsAlarm.model_fields.keys())
            self.assertEqual(
                set(), set(raw_data["data"]["alarms"][0].keys()).difference(pydantic_keys), "data_alarms_0"
            )

    @skip("Currently no HPS devices on test environment")
    def test_details(self):
        with patch(f"{TEST_FILE}.HpsDetails", wraps=HpsDetails) as mock_pyd_model:
            self.api.details(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in HpsDetails.model_fields.items()} | set(
            HpsDetails.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in HpsDetailData.model_fields.items()} | set(
            HpsDetailData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    @skip("Currently no HPS devices on test environment")
    def test_energy(self):
        with patch(f"{TEST_FILE}.HpsEnergyOverview", wraps=HpsEnergyOverview) as mock_pyd_model:
            self.api.energy(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in HpsEnergyOverview.model_fields.items()} | set(
            HpsEnergyOverview.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in HpsEnergyOverviewData.model_fields.items()} | set(
            HpsEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    @skip("Currently no HPS devices on test environment")
    def test_energy_history(self):
        # get date with data
        _details = self.api.details(device_sn=self.device_sn)
        _last_ts = _details.data.last_update_time_text

        with patch(f"{TEST_FILE}.HpsEnergyHistory", wraps=HpsEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                device_sn=self.device_sn, start_date=_last_ts.date() - timedelta(days=6), end_date=_last_ts.date()
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in HpsEnergyHistory.model_fields.items()} | set(
            HpsEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in HpsEnergyHistoryData.model_fields.items()} | set(
            HpsEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check datas
        pydantic_keys = {v.alias for k, v in HpsEnergyOverviewData.model_fields.items()} | set(
            HpsEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
        # FAILS often as api.details() is called too frequently
