import datetime
import unittest
from unittest.mock import patch


from api_v4 import ApiV4
from growatt_public_api import Plant, GrowattApiSession, User, GrowattCountry, PlantType
from pydantic_models.plant import (
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
    PlantInfo,
    PlantInfoData,
)

TEST_FILE = "plant.plant"


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

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession(
            server_url="https://test.growatt.com",
            token="6eb6f069523055a339d71e5b1f6c88cc",  # gitleaks:allow
        )
        # init
        cls.api = Plant(session=gas)
        api_user = User(session=gas)
        api_v4 = ApiV4(session=gas)
        # get a plant
        try:
            _plants = cls.api.list()
            plant_list = _plants.data.plants
            cls.plant_id = plant_list[0].plant_id
            # get username for user_id
            cls.user_id = plant_list[0].user_id
        except AttributeError:
            cls.plant_id = 51
            cls.user_id = 37
        # get username for user_id
        try:
            user_mapper = {x.id: x.name for x in api_user.list().data.users}
            cls.user_name = user_mapper.get(cls.user_id, None)
        except AttributeError:
            cls.user_name = "7177336xBs"
        # get a device for plant
        try:
            _devices = api_v4.list()
            cls.device_sn = _devices.data.data[0].device_sn
        except (AttributeError, IndexError):
            cls.device_sn = "SASF819012"

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

    def test_by_device(self):
        with patch(f"{TEST_FILE}.PlantInfo", wraps=PlantInfo) as mock_pyd_model:
            self.api.by_device(device_sn=self.device_sn)

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in PlantInfo.model_fields.items()} | set(
            PlantInfo.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in PlantInfoData.model_fields.items()} | set(
            PlantInfoData.model_fields.keys()
        )
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")

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

        # if raw_data["data"]["count"] == 0:
        #     # if there are no plants, there are no plants
        #     self.assertEqual([], raw_data["data"]["energys"])
        # else:
        #     # check plant
        #     pydantic_keys = {v.alias for k, v in PlantEnergyHistoryDate.model_fields.items()} | set(PlantEnergyHistoryDate.model_fields.keys())
        #     self.assertEqual(
        #         set(), set(raw_data["data"]["energys"][0].keys()).difference(pydantic_keys), "data_energys_0"
        #     )

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
