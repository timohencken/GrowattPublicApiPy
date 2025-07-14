from datetime import date, timedelta
from typing import Optional, Literal, Union
from ..growatt_types import GrowattCountry, PlantType
from ..pydantic_models import DeviceAdd
from ..pydantic_models.device import (
    DataloggerAdd,
    DataloggerDelete,
    DataloggerList,
    DeviceList,
)
from ..pydantic_models.plant import (
    PlantList,
    PlantDetails,
    PlantEnergyOverview,
    PlantEnergyHistory,
    PlantPower,
    PlantAdd,
    PlantModify,
    PlantDelete,
)
from ..session.growatt_api_session import GrowattApiSession


class Plant:
    """
    endpoints for Plant (Power station) management
    https://www.showdoc.com.cn/262556420217021/1494063254831721
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def add(
        self,
        user_id: int,
        plant_name: str,
        peak_kw: float,
        country: Optional[Union[GrowattCountry, str]] = None,
        installer_code: Optional[str] = None,
        currency: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        timezone: Optional[float] = None,
        plant_type: Optional[Union[PlantType, int]] = None,
        create_date: Optional[date] = None,
        price_per_kwh: Optional[float] = None,
        city: Optional[str] = None,
        address: Optional[str] = None,
    ) -> PlantAdd:
        """
        2.1 Add power station
        Add the interface of the power station
        https://www.showdoc.com.cn/262556420217021/1494063254831721

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Username ID is empty
        * 10003: The power station name is empty
        * 10004: Peak power is empty
        * 10005: User does not exist
        * 10006: The power station name already exists under this user

        Args:
            user_id (int): User ID ("c_user_id" as returned in register()), e.g. 74
            plant_name (str): Power Station Name, e.g. "bole66"
            peak_kw (float): peak power (kWp), e.g. 20
            country (Optional[Union[GrowattCountry, str]]): Area country list, e.g. "Thailand"
            installer_code (Optional[str]): Installer code, e.g. "AFLF6"
            currency (Optional[str]): currency unit, e.g. "$"
            longitude (Optional[float]): longitude, e.g. 30
            latitude (Optional[float]): latitude, e.g. 20
            timezone (Optional[float]): time zone as hours from UTC (e.g. 9 for GMT+9)
            plant_type (Optional[Union[PlantType, int]]): Power station type: 0: Residential, 1: Commercial, 2: Ground-Mounted
            create_date (Optional[date]): Created time, e.g. "2022-10-13"
            price_per_kwh (Optional[float]): Electricity price, e.g. 1.4
            city (Optional[str]): City, e.g. "Shenzhen"
            address (Optional[str]): Plant location (street,...), e.g. "123 Main St."

        Returns:
            PlantAdd
            {   'data': {'plant_id': 24832},
                'error_code': 0,
                'error_msg': None}
        """

        if isinstance(country, GrowattCountry):
            country = country.value
        if isinstance(plant_type, PlantType):
            plant_type = plant_type.value
        if isinstance(create_date, date):
            create_date = create_date.isoformat()

        response = self.session.post(
            endpoint="plant/add",
            data={
                "c_user_id": user_id,
                "name": plant_name,
                "peak_power": peak_kw,
                "latitude_f": country,
                "latitude_d": installer_code,
                "currency": currency,
                "longitude": longitude,
                "latitude": latitude,
                "timezone_id": timezone,
                "plant_type": plant_type,
                "createDate": create_date,
                "formulaMoney": price_per_kwh,
                "city": city,
                "plantAddress": address,
            },
        )

        return PlantAdd.model_validate(response)

    def modify(
        self,
        user_id: int,
        plant_id: int,
        plant_name: str,
        peak_kw: Optional[float] = None,
        country: Optional[Union[GrowattCountry, str]] = None,
        installer_code: Optional[str] = None,
        currency: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        timezone: Optional[float] = None,
        plant_type: Optional[Union[PlantType, int]] = None,
    ) -> PlantModify:
        """
        2.2 Modifying the power station
        Modify the interface of the power station
        https://www.showdoc.com.cn/262556420217021/1494059609631488

        Rate limit(s):
        * This interface is only allowed to be called 10 times a day

        Specific error codes:
        * 10001: System error
        * 10002: Username ID is empty
        * 10003: The power station name is empty
        * 10004: Peak power is empty
        * 10005: User does not exist
        * 10006: The power station name already exists under this user
        * 10007: The power station does not exist

        Args:
            user_id (int): User ID ("c_user_id" as returned in register()), e.g. 74
            plant_id (int): Power Station ID ("plant_id" as returned in add()), e.g. 77
            plant_name (str): Power Station Name, e.g. "bole66"
            peak_kw (Optional[float]): peak power (kWp), e.g. 20
            country (Optional[Union[GrowattCountry, str]]): Area country list, e.g. "Thailand"
            installer_code (Optional[str]): Installer code, e.g. "AFLF6"
            currency (Optional[str]): currency unit, e.g. "$"
            longitude (Optional[float]): longitude, e.g. 30
            latitude (Optional[float]): latitude, e.g. 20
            timezone (Optional[float]): time zone as hours from UTC (e.g. 9 for GMT+9)
            plant_type (Optional[Union[PlantType, int]]): Power station type: 0: Residential, 1: Commercial, 2: Ground-Mounted

        Returns:
            PlantModify
            {'data': None, 'error_code': 0, 'error_msg': None}
        """

        if isinstance(country, GrowattCountry):
            country = country.value
        if isinstance(plant_type, PlantType):
            plant_type = plant_type.value

        response = self.session.post(
            endpoint="plant/modify",
            data={
                "c_user_id": user_id,
                "plant_id": plant_id,
                "name": plant_name,
                "latitude_f": country,
                "latitude_d": installer_code,
                "peak_power": peak_kw,
                "currency": currency,
                "longitude": longitude,
                "latitude": latitude,
                "timezone_id": timezone,
                "plant_type": plant_type,
            },
        )

        return PlantModify.model_validate(response)

    def delete(
        self,
        plant_id: int,
    ) -> PlantDelete:
        """
        2.3 Delete power station
        Delete the interface of the power station
        https://www.showdoc.com.cn/262556420217021/1494059771852057

        Specific error codes:
        * 10001: System error
        * 10002: The power plant ID is empty
        * 10004: The power station does not exist

        Args:
            plant_id (int): Power Station ID ("plant_id" as returned in add()), e.g. 77

        Returns:
            PlantDelete
            {'data': None, 'error_code': 0, 'error_msg': None}

        """

        response = self.session.post(
            endpoint="plant/delete",
            data={
                "plant_id": plant_id,
            },
        )

        return PlantDelete.model_validate(response)

    def list_by_user(
        self,
        username: str,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PlantList:
        """
        2.4 Get a list of power plants for a user
        Get the interface of a user's power station list
        https://www.showdoc.com.cn/262556420217021/1494064249382745

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes
        * This interface is only allowed to be called 10 times a day

        Specific error codes:
        * 10001: System error

        Args:
            username (str): 	User Account
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            PlantList
            e.g.
            {
                "data": {
                    "count": 1,
                    "plants": [
                        {
                            "status": 1,
                            "locale": "en-US",
                            "total_energy": 0,
                            "operator": "0",
                            "country": "China",
                            "city": "0",
                            "current_power": "",
                            "create_date": "2016-09-15",
                            "image_url": null,
                            "plant_id": 1185,
                            "name": "9",
                            "installer": "0",
                            "user_id": 31,
                            "longitude": "",
                            "latitude": "",
                            "peak_power": 0,
                            "latitude_d": null,
                            "latitude_f": null
                        }
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
        """

        response = self.session.post(
            endpoint="plant/user_plant_list",
            data={"user_name": username, "page": page, "perpage": limit},
        )

        return PlantList.model_validate(response)

    def list(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        search_type: Optional[str] = None,
        search_keyword: Optional[str] = None,
    ) -> PlantList:
        """
        2.5 Get a list of all user power stations
        Get the interface to all user power station lists
        https://www.showdoc.com.cn/262556420217021/1494058730404880

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes
        * This interface is only allowed to be called 10 times a day

        Specific error codes:
        * 10001: System error

        Args:
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100
            search_type (Optional[str]): search type
            search_keyword (Optional[str]): search keywords

        Returns:
            PlantList
            {   'data': {   'count': 1,
                            'plants': [   {   'city': '0',
                                              'country': 'China',
                                              'create_date': datetime.date(2016, 9, 15),
                                              'current_power': None,
                                              'image_url': None,
                                              'installer': '0',
                                              'latitude': None,
                                              'latitude_d': None,
                                              'latitude_f': None,
                                              'locale': 'en-US',
                                              'longitude': None,
                                              'name': '9',
                                              'operator': '0',
                                              'peak_power': 0.0,
                                              'plant_id': 1185,
                                              'status': 1,
                                              'total_energy': 0.0,
                                              'user_id': 31}]},
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="plant/list",
            params={
                "page": page,
                "perpage": limit,
                "search_type": search_type,
                "search_keyword": search_keyword,
            },
        )

        return PlantList.model_validate(response)

    def details(
        self,
        plant_id: int,
    ) -> PlantDetails:
        """
        2.6 Get basic information about a power station
        Interface to obtain basic information about a power station
        https://www.showdoc.com.cn/262556420217021/1494060394238679

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Power station does not exist
        * 10003: Power station ID is empty
        * 10004: User does not exist

        Args:
            plant_id (int): Power Station ID

        Returns:
            PlantDetails
            {   'data': {   'address1': None,
                            'address2': None,
                            'arrays': [{'module_man': 'Growatt', 'module_md': None, 'num_modules': 0}],
                            'city': 'Shenzhen',
                            'country': 'China',
                            'create_date': datetime.date(2018, 12, 12),
                            'currency': 'rmb',
                            'dataloggers': [{'datalogger_man': 'Growatt', 'datalogger_md': None, 'datalogger_num': 1}],
                            'description': None,
                            'designercontact': None,
                            'designerorganization': None,
                            'elevation': None,
                            'financiercontact': None,
                            'financierorganization': None,
                            'fixed_azimuth': None,
                            'fixed_tilt': None,
                            'grid_type': None,
                            'image_url': '2.png',
                            'installed_ac_capacity': None,
                            'installed_dc_capacity': None,
                            'installed_panel_area': None,
                            'installercontact': None,
                            'installerorganization': None,
                            'inverters': [{'inverter_man': 'Growatt', 'inverter_md': None, 'inverter_num': 1}],
                            'irradiationsensor_type': None,
                            'jurisdictioncontact': None,
                            'jurisdictionorganization': None,
                            'latitude': 22.6,
                            'locale': 'en_US',
                            'longitude': 113.9,
                            'maxs': [],
                            'name': 'API interface test power station',
                            'notes': None,
                            'offtakercontact': None,
                            'offtakerorganization': None,
                            'operatorcontact': None,
                            'operatororganization': None,
                            'ownercontact': 'rmb',
                            'ownerorganization': 'rmb',
                            'peak_power': 20.0,
                            'plant_type': None,
                            'postal': None,
                            'state': None,
                            'status': None,
                            'timezone': 'GMT+8',
                            'tracker_type': None,
                            'user_id': 33,
                            'weather_type': None,
                            'weathersensor_man': None,
                            'weathersensor_md': None,
                            'weathersensor_num': None},
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="plant/details",
            params={
                "plant_id": plant_id,
            },
        )

        return PlantDetails.model_validate(response)

    def energy_overview(
        self,
        plant_id: int,
    ) -> PlantEnergyOverview:
        """
        2.7 Get an overview of a plant data
        Interface to get an overview of a plant data
        https://www.showdoc.com.cn/262556420217021/1494061093808613

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Power station does not exist
        * 10003: Power station ID is empty

        Args:
            plant_id (int): Power Station ID

        Returns:
            PlantEnergyOverview
            {   'data': {   'carbon_offset': 9.4,
                            'current_power': 0.0,
                            'efficiency': None,
                            'last_update_time': datetime.datetime(2018, 12, 13, 11, 6, 34),
                            'monthly_energy': 15.7,
                            'peak_power_actual': 20.0,
                            'timezone': 'GMT+8',
                            'today_energy': 0.0,
                            'total_energy': 15.7,
                            'yearly_energy': 15.7},
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="plant/data",
            params={
                "plant_id": plant_id,
            },
        )

        return PlantEnergyOverview.model_validate(response)

    def energy_history(  # noqa: C901 'Plant.energy_history' is too complex (13)
        self,
        plant_id: int,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        date_interval: Optional[Literal["day", "month", "year"]] = "day",
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PlantEnergyHistory:
        """
        Retrieve plant energy data for multiple days/months/years.

        2.8 Historical power generation of the power station
        Obtain an interface for historical power generation of a power station
        https://www.showdoc.com.cn/262556420217021/1494061730868556

        Rate limit(s):
        * Get the frequency once every 5 minutes
        * This interface is only allowed to call 10 times a day

        Specific error codes:
        * 10001: System error
        * 10002: Power station does not exist
        * 10003: Power station ID is empty
        * 10004: Time format is incorrect

        Args:
            plant_id (int): Power Station ID
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            date_interval (Literal["day", "month", "year"]): Time unit - defaults to day
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            PlantEnergyHistory
            Note:
                In order to be able to return valid dates, months are repoarted as YYYY-MM-01 and years as YYYY-01-01

            e.g. "day"
            {   'data': {   'count': 6,
                            'energys': [   {   'date': datetime.date(2018, 12, 12),
                                               'energy': 0.0},
                                           {   'date': datetime.date(2018, 12, 13),
                                               'energy': 7.6},
                                           {   'date': datetime.date(2018, 12, 14),
                                               'energy': 0.0},
                                           {   'date': datetime.date(2018, 12, 15),
                                               'energy': 0.0},
                                           {   'date': datetime.date(2018, 12, 16),
                                               'energy': 0.0},
                                           {   'date': datetime.date(2018, 12, 17),
                                               'energy': 0.0}],
                            'time_unit': 'day'},
                'error_code': 0,
                'error_msg': None}
            e.g. "month"
            {   'data': {   'count': 2,
                            'energys': [   {   'date': datetime.date(2025, 2, 1),
                                               'energy': 19.3},
                                           {   'date': datetime.date(2025, 3, 1),
                                               'energy': 18.5}],
                            'time_unit': 'month'},
                'error_code': 0,
                'error_msg': None}
            e.g. "year"
            {   'data': {   'count': 2,
                            'energys': [   {   'date': datetime.date(2024, 1, 1),
                                               'energy': 9.1},
                                           {   'date': datetime.date(2025, 1, 1),
                                               'energy': 56.0}],
                            'time_unit': 'year'},
                'error_code': 0,
                'error_msg': None}
        """

        if start_date is None and end_date is None:
            start_date = date.today()
            end_date = date.today()
        elif start_date is None:
            start_date = end_date
        elif end_date is None:
            end_date = start_date

        # check interval validity
        if date_interval == "year":
            # max 20 years allowed
            if end_date.year - start_date.year >= 20:
                raise ValueError("date interval must not exceed 20 years in 'year' mode")
        elif date_interval == "month":
            if end_date.year - start_date.year > 1:
                raise ValueError("start date must be within same or previous year in 'month' mode")
        else:
            if end_date - start_date >= timedelta(days=7):
                raise ValueError("date interval must not exceed 7 days in 'day' mode")

        response = self.session.get(
            endpoint="plant/energy",
            params={
                "plant_id": plant_id,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "time_unit": date_interval,
                "page": page,
                "perpage": limit,
            },
        )

        # make month/year timestamps valid dates
        if "data" in response and "energys" in response["data"]:
            for date_energy in response["data"]["energys"]:
                if date_interval == "month":
                    date_energy["date"] = date.fromisoformat(f'{date_energy["date"]}-01')
                elif date_interval == "year":
                    date_energy["date"] = date.fromisoformat(f'{date_energy["date"]}-01-01')

        return PlantEnergyHistory.model_validate(response)

    def power(
        self,
        plant_id: int,
        date_: Optional[date] = None,
    ) -> PlantPower:
        """
        Retrieve plant power data for one day (in 5 minute intervals).

        2.9 Obtain power data of a certain power station
        Obtain an interface for power data of a certain power station
        https://www.showdoc.com.cn/262556420217021/1494062656174173

        Rate limit(s):
        * Get the frequency once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Power station does not exist
        * 10003: Power station ID is empty or time format is incorrect

        Args:
            plant_id (int): Power Station ID
            date_ (Optional[date]): Date - defaults to today

        Returns:
            PlantPower
            e.g.
            {   'data': {   'count': 2,
                            'powers': [   {   'power': 7903.39990234375,
                                              'time': datetime.datetime(2018, 12, 13, 10, 45)},
                                          {   'power': 7689.7001953125,
                                              'time': datetime.datetime(2018, 12, 13, 10, 40)}]},
                'error_code': 0,
                'error_msg': None}
        """

        if date_ is None:
            date_ = date.today()

        response = self.session.get(
            endpoint="plant/power",
            params={
                "plant_id": plant_id,
                "date": date_.strftime("%Y-%m-%d"),
            },
        )

        return PlantPower.model_validate(response)

    def add_datalogger(
        self,
        user_id: int,
        plant_id: int,
        datalogger_sn: str,
    ) -> DataloggerAdd:
        """
        3.1 Add collector
        Add the interface of the collector
        https://www.showdoc.com.cn/262556420217021/6117939786619819

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: power station ID is empty or collector serial number error
        * 10003: collector already exists
        * 10004: power station does not exist
        * 10005: user does not exist
        * 10006: user ID is empty

        Args:
            user_id (int): User ID ("c_user_id" as returned in register()), e.g. 74
            plant_id (int): Power Station ID
            datalogger_sn (str): Datalogger serial number

        Returns:
            DataloggerAdd
            {   'data': None,
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/datalogger/add",
            data={
                "plant_id": plant_id,
                "sn": datalogger_sn,
                "c_user_id": user_id,
            },
        )

        return DataloggerAdd.model_validate(response)

    def remove_datalogger(
        self,
        plant_id: int,
        datalogger_sn: str,
    ) -> DataloggerDelete:
        """
        3.2 Delete collector
        Delete the interface of the collector
        https://www.showdoc.com.cn/262556420217021/6117952419029888


        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: power station ID is empty or the collector serial number is wrong
        * 10003: power station does not exist
        * 10004: collector does not exist

        Args:
            plant_id (int): Power Station ID
            datalogger_sn (str): Datalogger serial number

        Returns:
            DataloggerDelete
            {   'data': None,
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.post(
            endpoint="device/datalogger/delete",
            data={
                "plant_id": plant_id,
                "sn": datalogger_sn,
            },
        )

        return DataloggerDelete.model_validate(response)

    def add_device(
        self,
        plant_id: int,
        device_sn: str,
        user_id: int,
    ) -> DeviceAdd:
        """
        Assign inverter to user account.
        If possible, please use device.datalogger_add() instead.

        Add device associated account interface
        The terminal account relationship associated with the device SN is used when the collector SN is not known,
         but the device SN is known, but there is a certain delay.
        The association relationship is not necessarily real-time, only when the device is online.
        It will be associated in real time.
        If the device is not online, it will be associated after the device is online.
        https://www.showdoc.com.cn/262556420217021/9462221142197198

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error

        Args:
            plant_id (int): Power Station ID
            device_sn (str): Inverter serial number
            user_id (int): User ID

        Returns:
            DeviceAdd
            e.g.
            {
                "error_code": 0,
                "error_msg": ""
            }
        """
        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/sn/add",
            data={
                "plant_id": plant_id,
                "sn": device_sn,
                "c_user_id": user_id,
            },
        )

        return DeviceAdd.model_validate(response)

    def list_dataloggers(
        self,
        plant_id: int,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> DataloggerList:
        """
        3.4 Get a list of power station collectors
        The interface to obtain the collector list of a certain power station
        https://www.showdoc.com.cn/262556420217021/6117971175828060

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: power station ID is empty
        * 10003: power station does not exist

        Args:
            plant_id (int): Power Station ID
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            DataloggerList
            e.g.
            {
                "data": {
                    "peak_power_actual": {
                        "treeID": "PLANT_24765",
                        "flatPeriodPrice": 0,
                        "longitudeText": "null°null′null″",
                        "storage_eChargeToday": 0,
                        "storage_BattoryPercentage": 0,
                        "dataLogList": [],
                        "designCompany": "API interface testing manufacturer",
                        "timezoneText": "GMT+8",
                        "defaultPlant": False,
                        "peakPeriodPrice": 0,
                        "formulaCoal": 0.4000000059604645,
                        "storage_eDisChargeToday": 0,
                        "city": "Shenzhen",
                        "nominalPower": 20000,
                        "unitMap": None,
                        "timezone": 8,
                        "level": 1,
                        "formulaMoneyUnitId": "rmb",
                        "currentPacTxt": "0",
                        "panelTemp": 0,
                        "fixedPowerPrice": 0,
                        "imgPath": "css/img/plant.gif",
                        "storage_TotalToGrid": 0,
                        "moneyUnitText": "￥",
                        "locationImgName": "1.png",
                        "prToday": "0",
                        "energyMonth": 0,
                        "deviceCount": 0,
                        "plantName": "API interface test plant",
                        "plantImgName": "2.png",
                        "eToday": 0,
                        "etodaySo2Text": "0",
                        "country": "China",
                        "emonthMoneyText": "0",
                        "longitude_d": "",
                        "longitude_f": "",
                        "formulaMoney": 1.2000000476837158,
                        "userAccount": "API interface test",
                        "mapLat": "",
                        "longitude_m": "",
                        "createDateText": "2018-12-12",
                        "formulaSo2": 0.800000011920929,
                        "valleyPeriodPrice": 0,
                        "mapLng": "",
                        "energyYear": 0,
                        "treeName": "API interface test power station",
                        "plant_lat": "22.6",
                        "onLineEnvCount": 0,
                        "etodayCo2Text": "0",
                        "latitudeText": "null°null′null″",
                        "etotalSo2Text": "0",
                        "children": [],
                        "hasDeviceOnLine": 0,
                        "id": 24765,
                        "etodayCoalText": "0",
                        "etodayMoney": 0,
                        "createDate": {"time": 1544544000000, "minutes": 0, "seconds": 0, "hours": 0, "month": 11, "year": 118, "timezoneOffset": -480, "day": 3, "date": 12 },
                        "prMonth": "0",
                        "mapCity": "",
                        "etotalMoney": 0,
                        "envTemp": 0,
                        "storage_TodayToGrid": 0,
                        "alias": "",
                        "etotalCo2Text": "0",
                        "emonthCo2Text": "0",
                        "eTotal": 0,
                        "etotalMoneyText": "0",
                        "formulaCo2": 0.6000000238418579,
                        "irradiance": 0,
                        "emonthSo2Text": "0",
                        "hasStorage": 0,
                        "windAngle": 0,
                        "etotalCoalText": "0",
                        "windSpeed": 0,
                        "emonthCoalText": "0",
                        "parentID": "",
                        "EYearMoneyText": "0",
                        "etodayMoneyText": "0",
                        "plant_lng": "113.9",
                        "pairViewUserAccount": "",
                        "latitude_m": "",
                        "userBean": None,
                        "storage_TotalToUser": 0,
                        "storage_TodayToUser": 0,
                        "isShare": False,
                        "currentPac": 0,
                        "latitude_d": "",
                        "latitude_f": ""
                    },
                    "count": 1,
                    "dataloggers": [
                        {
                            "last_update_time": {"time": 1544670394000, "minutes": 6, "seconds": 34, "hours": 11, "month": 11, "timezoneOffset": -480, "year": 118, "day": 4, "date": 13},
                            "model": "ShineWifiBox",
                            "sn": "CRAZT00001",
                            "lost": True,
                            "manufacturer": "Growatt",
                            "type": 0
                        }
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
        """

        response = self.session.get(
            endpoint="device/datalogger/list",
            params={
                "plant_id": plant_id,
                "page": page,
                "perpage": limit,
            },
        )

        return DataloggerList.model_validate(response)

    def list_devices(
        self,
        plant_id: int,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> DeviceList:
        """
        3.3 Obtain a power station equipment list
        Interface to get a list of power station equipment
        https://www.showdoc.com.cn/262556420217021/6117958613377445

        Rate limit(s):
        * The acquisition frequency is once every 5 minutes

        Specific error codes:
        * 10001: system error
        * 10002: power station ID is empty
        * 10003: power station does not exist

        Note:
            returned "device_type" mappings:
             1: inverter (including MAX)
             2: storage
             3: other (datalogger, smart meter, environmental sensor, ...)
             4: max (single MAX)
             5: sph
             6: spa
             7: min
             8: pcs
             9: hps
            10: pbd
            11: groboost

        Args:
            plant_id (int): Power Station ID
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            DeviceList
            e.g.
            {
                "data": {
                    "count": 3,
                    "devices": [
                        {
                            "device_sn": "ZT00100001",
                            "last_update_time": "2018-12-13 11:03:52",
                            "model": "A0B0D0T0PFU1M3S4",
                            "lost": True,
                            "status": 0,
                            "manufacturer": "Growatt",
                            "device_id": 116,
                            "datalogger_sn": "CRAZT00001",
                            "type": 1
                        },
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
        """

        response = self.session.get(
            endpoint="device/list",
            params={
                "plant_id": plant_id,
                "page": page,
                "perpage": limit,
            },
        )

        return DeviceList.model_validate(response)
