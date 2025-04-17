import unittest
from unittest import skip
from unittest.mock import patch

from env_sensor import EnvSensor
from growatt_public_api import GrowattApiSession, Device, Plant
from pydantic_models.env_sensor import (
    EnvSensorList,
    EnvSensorListData,
    EnvSensorData,
    EnvSensorMetricsOverview,
    EnvSensorMetricsOverviewData,
    EnvSensorMetricsHistory,
    EnvSensorMetricsHistoryData,
)

TEST_FILE = "env_sensor.env_sensor"


class TestEnvSensor(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: EnvSensor = None
    datalogger_sn: str = None
    sensor_address: int = None

    def setUp(self):  # noqa: C901 'TestEnvSensor.setUp' is too complex (11)
        # init API
        gas = GrowattApiSession(
            # several min devices seen on v1 test server
            server_url="https://test.growatt.com",
            token="6eb6f069523055a339d71e5b1f6c88cc",  # gitleaks:allow
        )
        # init DEVICE
        if self.api is None:
            self.api = EnvSensor(session=gas)
        # get a DEVICE device
        if self.datalogger_sn is None:
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
            type_3_devices = []
            for idx, plant_id in enumerate(reversed(plant_ids)):
                print(f"\rscanning plant {idx+1}/{len(plant_ids)} with {plant_id=}", end="")
                devices = api_device.list(plant_id=plant_id)
                if devices.data.count == 0:
                    continue
                print(f"\nfound {devices.data.count} devices in {plant_id=}")
                plant_devices[plant_id] = devices.data.devices
                for device in devices.data.devices:
                    if device.type == 3:
                        datalogger_sn = device.datalogger_sn
                        device_id = device.device_id
                        device_sn = device.device_sn
                        print(
                            f"\ndetected device of type=3 with {device_id=} {device_sn=} {datalogger_sn=} {plant_id=}"
                        )
                        type_3_devices.append(
                            {
                                "plant_id": plant_id,
                                "datalogger_sn": datalogger_sn,
                                "device_id": device_id,
                                "device_sn": device_sn,
                            }
                        )
            print(f"\rscanned {len(plant_ids)} plants")
            print(f"Found {len(type_3_devices)} devices with type='other' - assuming these are env sensors")
            if len(type_3_devices) > 0:
                # take the first one
                self.datalogger_sn = type_3_devices[0]["datalogger_sn"]
                self.sensor_address = type_3_devices[0]["device_id"]
                print(f"using {self.datalogger_sn=} {self.sensor_address=}")
            else:
                print("Could not find any environmental sensor in devices")
                print(plant_devices)
                self.datalogger_sn = "NO DEVICE FOUND"
        if self.datalogger_sn == "NO DEVICE FOUND":
            raise AttributeError("No environmental sensor found in test environment")

    @skip("Currently no env sensors on test environment")
    def test_list(self):
        with patch(f"{TEST_FILE}.EnvSensorList", wraps=EnvSensorList) as mock_pyd_model:
            self.api.list(datalogger_sn=self.datalogger_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in EnvSensorList.model_fields.items()} | set(
            EnvSensorList.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in EnvSensorListData.model_fields.items()} | set(
            EnvSensorListData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check data item
        pydantic_keys = {v.alias for k, v in EnvSensorData.model_fields.items()} | set(
            EnvSensorData.model_fields.keys()
        )
        self.assertEqual(
            set(), set(raw_data["data"]["envs"][0].keys()).difference(pydantic_keys), f"data_dataloggers_0"
        )

    @skip("Currently no env sensors on test environment")
    def test_metrics(self):
        with patch(f"{TEST_FILE}.EnvSensorMetricsOverview", wraps=EnvSensorMetricsOverview) as mock_pyd_model:
            self.api.metrics(datalogger_sn=self.datalogger_sn, sensor_address=self.sensor_address)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in EnvSensorMetricsOverview.model_fields.items()} | set(
            EnvSensorMetricsOverview.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in EnvSensorMetricsOverviewData.model_fields.items()} | set(
            EnvSensorMetricsOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")

    @skip("Currently no env sensors on test environment")
    def test_metrics_history(self):
        with patch(f"{TEST_FILE}.EnvSensorMetricsHistory", wraps=EnvSensorMetricsHistory) as mock_pyd_model:
            self.api.metrics_history(datalogger_sn=self.datalogger_sn, sensor_address=self.sensor_address)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in EnvSensorMetricsHistory.model_fields.items()} | set(
            EnvSensorMetricsHistory.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in EnvSensorMetricsHistoryData.model_fields.items()} | set(
            EnvSensorMetricsHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check data item
        pydantic_keys = {v.alias for k, v in EnvSensorMetricsOverviewData.model_fields.items()} | set(
            EnvSensorMetricsOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"]["env_data"][0].keys()).difference(pydantic_keys), f"data_env_0")
