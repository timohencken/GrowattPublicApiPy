import datetime
import unittest
from unittest import skip
from unittest.mock import patch


from growatt_public_api.api_v4 import ApiV4
from growatt_public_api import Plant, GrowattApiSession, User, GrowattCountry, PlantType, Device
from growatt_public_api.pydantic_models.device import (
    DataloggerList,
    DataloggerListData,
    DataloggerData,
    DeviceList,
    DeviceListData,
    DeviceData,
)
from growatt_public_api.pydantic_models.plant import (
    PlantList,
    PlantData,
    PlantListData,
    PlantPower,
    PlantPowerData,
    PlantPowerDate,
    PlantEnergyOverviewData,
    PlantEnergyOverview,
    PlantEnergyHistoryDate,
    PlantEnergyHistoryData,
    PlantEnergyHistory,
    PlantDetailData,
    PlantDetails,
    PlantDetailMax,
    PlantDetailInverter,
    PlantDetailDatalogger,
    PlantDetailModule,
)

TEST_FILE = "growatt_public_api.plant.plant"


# noinspection DuplicatedCode
class TestPlant(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Plant = None
    plant_id: int = None
    user_id: int = None
    user_name: str = None
    device_sn: str = None
    datalogger_sn: str = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession.using_test_server_v1()
        # init
        cls.api = Plant(session=gas)
        api_device = Device(session=gas)
        api_user = User(session=gas)
        api_v4 = ApiV4(session=gas)
        # get a plant with devices
        # 1. get a device
        try:
            print("lookup test device...")
            _device_list = api_v4.list()
            _device = _device_list.data.data[0]
            cls.device_sn = _device.device_sn
            cls.datalogger_sn = _device.datalogger_sn
        except AttributeError:
            cls.device_sn = "SASF819012"
            cls.datalogger_sn = "WLC082100F"
        # 2. get assigned plant
        try:
            print("lookup test plant...")
            _plant = api_device.get_plant(device_sn=cls.device_sn)
            cls.plant_id = _plant.data.plant.plant_id
            cls.user_id = _plant.data.plant.user_id
        except AttributeError:
            cls.plant_id = 23
            cls.user_id = 21
        # 3. get username for user_id
        try:
            print("lookup test user...")
            # noinspection PyTypeChecker
            cls.user_name = None
            _page = 0
            while cls.user_name is None and _page < 20:
                _page += 1
                _user_mapper = {x.id: x.name for x in api_user.list(limit=100, page=_page).data.users}
                cls.user_name = _user_mapper.get(cls.user_id)
            else:
                raise AttributeError("User name not found")
        except AttributeError:
            cls.user_name = "ceshi002"
        print("init done. running tests")

    def test_add_modify_delete(self):
        new_plant_id = None

        # add a plant
        try:
            add_plant_result = self.api.add(
                user_id=self.user_id,
                plant_name=f"Test Modify {datetime.datetime.now().isoformat()}",
                peak_kw=0.8,
                country=GrowattCountry.CANADA,
                installer_code="GWATT",
                currency="CAD",
                latitude=61.0666922,
                longitude=-107.991707,
                timezone=-4,
                plant_type=PlantType.RESIDENTIAL,
                create_date=datetime.datetime.now(),
                price_per_kwh=0.42,
                city="Calgary",
                address="1234 Test St",
            )
            new_plant_id = add_plant_result.data.plant_id
            add_plant_result_json = add_plant_result.model_dump()
            self.assertEqual(
                {"error_msg", "error_code", "data"},
                set(add_plant_result_json.keys()),
                f"Add plant result keys do not match expected keys. returned {add_plant_result}",
            )
            self.assertIsNotNone(new_plant_id, f"returned {add_plant_result}")
            self.assertEqual(0, add_plant_result.error_code, f"returned {add_plant_result}")
            self.assertIsNone(add_plant_result.error_msg, f"returned {add_plant_result}")
            print(f"Added plant {new_plant_id}")
        except (AssertionError, Exception) as e:
            print(f"Deleting plant {new_plant_id} after failed add")
            self.api.delete(plant_id=new_plant_id)
            raise e

        # modify the plant
        try:
            modify_plant_result = self.api.modify(
                user_id=self.user_id,
                plant_id=new_plant_id,
                plant_name=f"Test Modify {datetime.datetime.now().isoformat()} 2",
                peak_kw=0.6,
                country=GrowattCountry.JAPAN,
                installer_code="GWATT",
                currency="YEN",
                latitude=35.652832,
                longitude=139.839478,
                timezone=9.5,
                plant_type=PlantType.COMMERCIAL,
            )
            modify_plant_result_json = modify_plant_result.model_dump()
            self.assertEqual(
                {"error_msg", "error_code", "data"},
                set(modify_plant_result_json.keys()),
                f"Modify plant result keys do not match expected keys. returned {add_plant_result}",
            )
            self.assertEqual(0, modify_plant_result.error_code, f"returned {modify_plant_result}")
            self.assertIsNone(modify_plant_result.error_msg, f"returned {modify_plant_result}")
            self.assertIsNone(modify_plant_result.data, f"returned {modify_plant_result}")
            print(f"Modified plant {new_plant_id}")
        except (AssertionError, Exception) as e:
            print(f"Deleting plant {new_plant_id} after failed modify")
            self.api.delete(plant_id=new_plant_id)
            raise e

        # delete
        delete_plant_result = self.api.delete(plant_id=new_plant_id)
        delete_plant_result_json = delete_plant_result.model_dump()
        self.assertEqual(
            {"error_msg", "error_code", "data"},
            set(delete_plant_result_json.keys()),
            f"Delete plant result keys do not match expected keys. returned {add_plant_result}",
        )
        self.assertEqual(0, delete_plant_result.error_code, f"returned {delete_plant_result}")
        self.assertIsNone(delete_plant_result.error_msg, f"returned {delete_plant_result}")
        self.assertIsNone(delete_plant_result.data, f"returned {delete_plant_result}")
        print(f"Deleted plant {new_plant_id}")

    def test_details(self):
        with patch(f"{TEST_FILE}.PlantDetails", wraps=PlantDetails) as mock_pyd_model:
            self.api.details(plant_id=self.plant_id)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantDetails.model_fields.items()} | set(
            PlantDetails.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantDetailData.model_fields.items()} | set(
            PlantDetailData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check modules
        if raw_data["data"]["arrays"]:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantDetailModule.model_fields.items()} | set(
                PlantDetailModule.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["arrays"][0].keys()).difference(pydantic_keys), "data_arrays_0"
            )
        if raw_data["data"]["dataloggers"]:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantDetailDatalogger.model_fields.items()} | set(
                PlantDetailDatalogger.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["dataloggers"][0].keys()).difference(pydantic_keys), "data_dataloggers_0"
            )
        if raw_data["data"]["inverters"]:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantDetailInverter.model_fields.items()} | set(
                PlantDetailInverter.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["inverters"][0].keys()).difference(pydantic_keys), "data_inverters_0"
            )
        if raw_data["data"]["maxs"]:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantDetailMax.model_fields.items()} | set(
                PlantDetailMax.model_fields.keys()
            )
            self.assertEqual(set(), set(raw_data["data"]["maxs"][0].keys()).difference(pydantic_keys), "data_maxs_0")

    def test_energy_history__day(self):
        with patch(f"{TEST_FILE}.PlantEnergyHistory", wraps=PlantEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                plant_id=self.plant_id,
                start_date=datetime.date.today(),
                end_date=datetime.date.today() - datetime.timedelta(days=6),
                date_interval="day",
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantEnergyHistory.model_fields.items()} | set(
            PlantEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantEnergyHistoryData.model_fields.items()} | set(
            PlantEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no plants, there are no plants
            self.assertEqual([], raw_data["data"]["energys"])
        else:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantEnergyHistoryDate.model_fields.items()} | set(
                PlantEnergyHistoryDate.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["energys"][0].keys()).difference(pydantic_keys), "data_energys_0"
            )

    def test_energy_history__month(self):
        with patch(f"{TEST_FILE}.PlantEnergyHistory", wraps=PlantEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                plant_id=self.plant_id,
                start_date=datetime.date.today(),
                end_date=datetime.date.today() - datetime.timedelta(days=365),
                date_interval="month",
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantEnergyHistory.model_fields.items()} | set(
            PlantEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantEnergyHistoryData.model_fields.items()} | set(
            PlantEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no plants, there are no plants
            self.assertEqual([], raw_data["data"]["energys"])
        else:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantEnergyHistoryDate.model_fields.items()} | set(
                PlantEnergyHistoryDate.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["energys"][0].keys()).difference(pydantic_keys), "data_energys_0"
            )

    def test_energy_history__year(self):
        _today = datetime.date.today()
        with patch(f"{TEST_FILE}.PlantEnergyHistory", wraps=PlantEnergyHistory) as mock_pyd_model:
            self.api.energy_history(
                plant_id=self.plant_id,
                start_date=_today,
                end_date=_today.replace(year=_today.year - 10),
                date_interval="year",
            )

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantEnergyHistory.model_fields.items()} | set(
            PlantEnergyHistory.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantEnergyHistoryData.model_fields.items()} | set(
            PlantEnergyHistoryData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no plants, there are no plants
            self.assertEqual([], raw_data["data"]["energys"])
        else:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantEnergyHistoryDate.model_fields.items()} | set(
                PlantEnergyHistoryDate.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["energys"][0].keys()).difference(pydantic_keys), "data_energys_0"
            )

    def test_energy_overview(self):
        with patch(f"{TEST_FILE}.PlantEnergyOverview", wraps=PlantEnergyOverview) as mock_pyd_model:
            self.api.energy_overview(plant_id=self.plant_id)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantEnergyOverview.model_fields.items()} | set(
            PlantEnergyOverview.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantEnergyOverviewData.model_fields.items()} | set(
            PlantEnergyOverviewData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

    def test_list(self):
        with patch(f"{TEST_FILE}.PlantList", wraps=PlantList) as mock_pyd_model:
            self.api.list()

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantList.model_fields.items()} | set(
            PlantList.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantListData.model_fields.items()} | set(
            PlantListData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check
        if raw_data["data"]["count"] == 0:
            # if there are no plants, there are no plants
            self.assertEqual([], raw_data["data"]["plants"])
        else:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantData.model_fields.items()} | set(PlantData.model_fields.keys())
            self.assertEqual(
                set(), set(raw_data["data"]["plants"][0].keys()).difference(pydantic_keys), "data_plants_0"
            )

    def test_list_by_user(self):
        with patch(f"{TEST_FILE}.PlantList", wraps=PlantList) as mock_pyd_model:
            self.api.list_by_user(username=self.user_name)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantList.model_fields.items()} | set(
            PlantList.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantListData.model_fields.items()} | set(
            PlantListData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check alarms
        if raw_data["data"]["count"] == 0:
            # if there are no plants, there are no plants
            self.assertEqual([], raw_data["data"]["plants"])
        else:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantData.model_fields.items()} | set(PlantData.model_fields.keys())
            self.assertEqual(
                set(), set(raw_data["data"]["plants"][0].keys()).difference(pydantic_keys), "data_plants_0"
            )

    def test_power(self):
        with patch(f"{TEST_FILE}.PlantPower", wraps=PlantPower) as mock_pyd_model:
            self.api.power(plant_id=self.plant_id)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantPower.model_fields.items()} | set(
            PlantPower.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantPowerData.model_fields.items()} | set(
            PlantPowerData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check power
        if raw_data["data"]["count"] == 0:
            # if there are no powers, there are no powers
            self.assertEqual([], raw_data["data"]["powers"])
        else:
            # check plant
            pydantic_keys = {v.alias for k, v in PlantPowerDate.model_fields.items()} | set(
                PlantPowerDate.model_fields.keys()
            )
            self.assertEqual(
                set(), set(raw_data["data"]["powers"][0].keys()).difference(pydantic_keys), "data_powers_0"
            )

    @skip("Currently not testing endpoints writing data")
    def test_add_datalogger(self):
        self.api.add_datalogger(
            user_id=self.user_id,
            plant_id=self.plant_id,
            datalogger_sn=None,  # self.datalogger.sn,
        )
        raise NotImplementedError

    @skip("Currently not testing endpoints writing data")
    def test_remove_datalogger(self):
        self.api.remove_datalogger(
            plant_id=self.plant_id,
            datalogger_sn=None,  # self.datalogger.sn,
        )
        raise NotImplementedError

    @skip("Currently not testing endpoints writing data")
    def test_add_device(self):
        self.api.add_device(
            user_id=self.user_id,
            plant_id=self.plant_id,
            device_sn=None,  # self.device_sn,
        )
        raise NotImplementedError

    def test_list_dataloggers(self):
        with patch(f"{TEST_FILE}.DataloggerList", wraps=DataloggerList) as mock_pyd_model:
            self.api.list_dataloggers(plant_id=self.plant_id)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DataloggerList.model_fields.items()} | set(
            DataloggerList.model_fields.keys()
        )  # aliased and non-aliased params
        for param in set(raw_data.keys()):
            self.assertIn(param, pydantic_keys)
        # check data
        pydantic_keys = {v.alias for k, v in DataloggerListData.model_fields.items()} | set(
            DataloggerListData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check data item
        pydantic_keys = {v.alias for k, v in DataloggerData.model_fields.items()} | set(
            DataloggerData.model_fields.keys()
        )
        self.assertEqual(
            set(), set(raw_data["data"]["dataloggers"][0].keys()).difference(pydantic_keys), f"data_dataloggers_0"
        )

    def test_list_devices(self):
        with patch(f"{TEST_FILE}.DeviceList", wraps=DeviceList) as mock_pyd_model:
            self.api.list_devices(plant_id=self.plant_id)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in DeviceList.model_fields.items()} | set(
            DeviceList.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in DeviceListData.model_fields.items()} | set(
            DeviceListData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), f"data")
        # check data item
        pydantic_keys = {v.alias for k, v in DeviceData.model_fields.items()} | set(DeviceData.model_fields.keys())
        self.assertEqual(
            set(), set(raw_data["data"]["devices"][0].keys()).difference(pydantic_keys), f"data_dataloggers_0"
        )
