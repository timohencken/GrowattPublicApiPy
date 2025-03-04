from datetime import date, timedelta
from typing import Optional, Literal

import truststore

from growatt_public_api.pydantic_models.plant import (
    PlantList,
    PlantDetails,
    PlantEnergyOverview,
    PlantEnergyHistory,
    PlantPower,
    PlantInfo,
)

truststore.inject_into_ssl()
from growatt_public_api.session import GrowattApiSession  # noqa: E402


class Plant:
    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session

    def add(self):
        """
        2.1 Add power station
        Add the interface of the power station

        https://www.showdoc.com.cn/262556420217021/1494063254831721
        """

        raise NotImplementedError  # TODO

    def modify(self):
        """
        2.2 Modifying the power station
        Modify the interface of the power station

        https://www.showdoc.com.cn/262556420217021/1494059609631488
        """

        raise NotImplementedError  # TODO

    def delete(self):
        """
        2.3 Delete power station
        Delete the interface of the power station
        https://www.showdoc.com.cn/262556420217021/1494059771852057
        """

        raise NotImplementedError  # TODO

    def list_by_user(
        self,
        username: str,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PlantList:
        """
        2.5 Get a list of all user power stations
        Get the interface to all user power station lists
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
            e.g.
            {
                "data": {
                    "address1": "",
                    "jurisdictionorganization": "",
                    "address2": "",
                    "installed_dc_capacity": "",
                    "city": "Shenzhen",
                    "timezone": "GMT+8",
                    "designerorganization": "",
                    "installercontact": "",
                    "create_date": "2018-12-12",
                    "image_url": "2.png",
                    "description": "",
                    "longitude": "113.9",
                    "fixed_azimuth": "",
                    "offtakercontact": "",
                    "status": "",
                    "postal": "",
                    "weathersensor_num": "",
                    "weathersensor_man": "",
                    "operatorcontact": "",
                    "country": "China",
                    "plant_type": "",
                    "fixed_tilt": "",
                    "inverters": [
                        {
                            "inverter_md": "",
                            "inverter_num": 1,
                            "inverter_man": "Growatt"
                        }
                    ],
                    "installerorganization": "",
                    "jurisdictioncontact": "",
                    "installed_ac_capacity": "",
                    "latitude": "22.6",
                    "financiercontact": "",
                    "ownerorganization": "rmb",
                    "locale": "en_US",
                    "designercontact": "",
                    "state": "",
                    "weather_type": "",
                    "currency": "rmb",
                    "installed_panel_area": "",
                    "name": "API interface test power station",
                    "user_id": 33,
                    "grid_type": "",
                    "operatororganization": "",
                    "elevation": "",
                    "irradiationsensor_type": "",
                    "ownercontact": "rmb",
                    "weathersensor_md": "",
                    "tracker_type": "",
                    "offtakerorganization": "",
                    "dataloggers": [
                        {
                            "datalogger_num": 1,
                            "datalogger_man": "Growatt",
                            "datalogger_md": ""
                        }
                    ],
                    "financierorganization": "",
                    "peak_power": 20,
                    "notes": "",
                    "arrays": [
                        {
                            "num_modules": 0,
                            "module_md": "",
                            "module_man": "Growatt"
                        }
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
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
            e.g.
            {
                "data": {
                    "peak_power_actual": 20,
                    "monthly_energy": "15.7",
                    "last_update_time": "2018-12-13 11:06:34",
                    "current_power": 0,
                    "timezone": "GMT+8",
                    "yearly_energy": "15.7",
                    "today_energy": "0",
                    "carbon_offset": "9.4",
                    "efficiency": "",
                    "total_energy": "15.7"
                },
                "error_code": 0,
                "error_msg": ""
            }
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
            {
                "data": {
                    "count": 1,
                    "time_unit": "day",
                    "energys": [
                        {"date": "2018-12-12", "energy": "0"}, # ...
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
            e.g. "month"
            {
                "data": {
                    "count": 1,
                    "time_unit": "month",
                    "energys": [
                        {'date': '2025-02-01', 'energy': '17.8'}, # ...
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
            e.g. "year"
            {
                "data": {
                    "count": 1,
                    "time_unit": "day",
                    "energys": [
                        {'date': 2025-01-01, 'energy': '36'}, # ...
                    ]
                },
                "error_code": 0,
                "error_msg": ""
            }
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
            if end_date.year - start_date.year > 20:
                raise ValueError(
                    "date interval must not exceed 20 years in 'year' mode"
                )
        elif date_interval == "month":
            if end_date.year - start_date.year > 1:
                raise ValueError(
                    "start date must be within same or previous year in 'month' mode"
                )
        else:
            if end_date - start_date > timedelta(days=7):
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
                    date_energy["date"] = date.fromisoformat(
                        date_energy["date"] + "-01"
                    )
                elif date_interval == "year":
                    date_energy["date"] = date.fromisoformat(
                        date_energy["date"] + "-01-01"
                    )

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
            {
                "data": {
                    "powers": [
                        {"time": "2018-12-13 10:45", "power": 7903.39990234375},
                        {"time": "2018-12-13 10:40", "power": 7689.7001953125}
                    ],
                    "count": 2
                },
                "error_code": 0,
                "error_msg": ""
            }
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

    def by_device(self, device_sn: str) -> PlantInfo:
        """
        Retrieve plant data (similar to list() by device_id (e.g. inverter id))

        2.10 Get the plant information of a device
        Obtain an interface for the plant information of a device
        https://www.showdoc.com.cn/262556420217021/1494064780850155

        Rate limit(s):
        * Get the frequency once every 5 minutes

        Specific error codes:
        * 10001: System error
        * 10002: Account does not exist
        * 10003: Device serial number is empty
        * 10004: Device type is empty
        * 10005: Device does not exist

        Args:
            device_sn (str): Device serial number (non-collector serial number)

        Returns:
            PlantInfo
        """

        response = self.session.post(
            endpoint="plant/sn_plant",
            data={
                "device_sn": device_sn,
            },
        )

        return PlantInfo.model_validate(response)
