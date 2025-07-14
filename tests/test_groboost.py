import unittest
from unittest import skip
from unittest.mock import patch

from growatt_public_api.groboost import Groboost
from growatt_public_api import GrowattApiSession, Device, Plant
from growatt_public_api.pydantic_models import GroboostDetails
from growatt_public_api.pydantic_models.env_sensor import (
    EnvSensorMetricsOverviewData,
)
from growatt_public_api.pydantic_models.groboost import GroboostDetailData, SpctData, BoostData
from growatt_public_api.pydantic_models.smart_meter import SmartMeterEnergyOverviewData

TEST_FILE = "growatt_public_api.groboost.groboost"


class TestGroboost(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Groboost = None
    device_sn: str = None

    @classmethod
    def setUpClass(cls):  # noqa: C901 'TestEnvSensor.setUp' is too complex (11)
        return  # "Currently no environmental sensor found in test environment"

        # init API
        # noinspection PyUnreachableCode
        gas = GrowattApiSession.using_test_server_v1()
        # init DEVICE
        cls.api = Groboost(session=gas)
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
        # iterate plants, search for env (start with newest plant)
        api_device = Device(session=gas)
        print(f"searching plants for correct device")
        plant_devices = {}
        type_11_devices = []
        for idx, plant_id in enumerate(reversed(plant_ids)):
            print(f"\rscanning plant {idx+1}/{len(plant_ids)} with {plant_id=}", end="")
            devices = api_device.list(plant_id=plant_id)
            if devices.data.count == 0:
                continue
            print(f"\nfound {devices.data.count} devices in {plant_id=}")
            plant_devices[plant_id] = devices.data.devices
            for device in devices.data.devices:
                if device.type == 11:
                    device_sn = device.device_sn
                    print(f"\ndetected device of type=11 with {device_sn=} {plant_id=}")
                    type_11_devices.append(
                        {
                            "plant_id": plant_id,
                            "device_sn": device_sn,
                        }
                    )
        print(f"\rscanned {len(plant_ids)} plants")
        print(f"Found {len(type_11_devices)} devices with type='groboost'")
        if len(type_11_devices) > 0:
            # take the first one
            cls.device_sn = type_11_devices[0]["device_sn"]
            print(f"using {cls.device_sn=}")
        else:
            print("Could not find any environmental sensor in devices")
            print(plant_devices)
            raise AttributeError("No groboost devices found in test environment")

    @skip("Currently no groboost devices on test environment")
    def test_details(self):
        with patch(f"{TEST_FILE}.GroboostDetails", wraps=GroboostDetails) as mock_pyd_model:
            self.api.details(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in GroboostDetails.model_fields.items()} | set(
            GroboostDetails.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in GroboostDetailData.model_fields.items()} | set(
            GroboostDetailData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check SpctData
        pydantic_keys = {v.alias for k, v in SpctData.model_fields.items()} | set(SpctData.model_fields.keys())
        self.assertEqual(set(), set(raw_data["data"]["spct_data"].keys()).difference(pydantic_keys), f"spct_data")
        # check EnvSensorMetricsOverviewData
        pydantic_keys = {v.alias for k, v in EnvSensorMetricsOverviewData.model_fields.items()} | set(
            EnvSensorMetricsOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["env_data"].keys()).difference(pydantic_keys), f"env_data")
        # check BoostData
        pydantic_keys = {v.alias for k, v in BoostData.model_fields.items()} | set(BoostData.model_fields.keys())
        self.assertEqual(set(), set(raw_data["data"]["boost_data"].keys()).difference(pydantic_keys), f"boost_data")
        # check SmartMeterEnergyOverviewData
        pydantic_keys = {v.alias for k, v in SmartMeterEnergyOverviewData.model_fields.items()} | set(
            SmartMeterEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["ammeter_data"].keys()).difference(pydantic_keys), f"ammeter_data")

    @skip("Currently no groboost devices on test environment")
    def test_metrics(self):
        raise NotImplementedError

    @skip("Currently no groboost devices on test environment")
    def test_metrics_multiple(self):
        raise NotImplementedError

    @skip("Currently no groboost devices on test environment")
    def test_metrics_history(self):
        raise NotImplementedError
