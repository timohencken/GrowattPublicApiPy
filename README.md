# GrowattApi
A python implementation of [Growatt](https://en.growatt.com/)'s public API.


# Motivation
There are already other libraries accessing Growatt's APIs, they all use reverse-engineered calls to internal, undocumented APIs.
* for example, see the faboulous work of [indykoning](https://github.com/indykoning) at [PyPi_GrowattServer](https://github.com/indykoning/PyPi_GrowattServer) used e.g. in HomeAssistant

This package aims to
* use Growatt's public API documented [here (v1)](https://www.showdoc.com.cn/262556420217021/0) and [here (v4)](https://www.showdoc.com.cn/2540838290984246/0)
* use type-aware pydantic objects as return values


# Implementation status
***Alpha***: The library is in an early stage of development and is not yet feature complete.

### API v1 (full featured API)
* User
  * ***Not*** implemented yet
* Plant
  * list plants
    * `plant.list()`
    * `plant.list_by_user()`
  * plant details
    * `plant.details()`
  * power/energy overview
    * `plant.energy_overview()`
  * energy history
    * `plant.energy_history()`
  * power metrics by day
    * `plant.power()`
  * ***Not*** implemented yet
    * add new plant
      * `plant.add()`
    * modify plant
      * `plant.modify()`
    * delete plant
      * `plant.delete()`
* Datalogger
  * list dataloggers
    * `device.datalogger_list()`
  * query device type
    * `device.type_info()`
    * *** this is NOT the same as the inverter type ***
  * verify datalogger's CC code
    * `device.datalogger_validate()`
  * ***Not*** implemented yet
    * add datalogger to plant
      * `device.datalogger_add()`
    * remove datalogger from plant
      * `device.datalogger_delete()`
* Generic - all inverter types
  * get inverters assigned to plant
    * `device.list()`
    * *** use this to query your inverter's "*TYPE*" for selecting the correct submodule ***
  * get datalogger for inverter
    * `device.get_datalogger()`
  * get device creation date
    * `device.create_date()`
  * add inverter to plant
    * `device.add()`
  * device power/energy metrics
    * get energy (sum) for specific day `device.energy_day()`
* Inverter (*TYPE=1* (including MAX))
  * general device data
    * read device data `inverter.details()`
    * read alarms/notification `inverter.alarms()`
  * device settings
    * read settings value `inverter.setting_read()`
    * write settings value `inverter.setting_write()` (***use with caution***)
  * device power/energy metrics
    * current `inverter.energy()`
    * current for multiple inverters `inverter.energy_multiple()`
    * historical data `inverter.energy_history()`
* Storage (*TYPE=2*)
  * general device data
    * read device data `storage.details()`
    * read alarms/notification `storage.alarms()`
  * device settings
    * read settings value `storage.setting_read()`
    * write settings value `storage.setting_write()` (***use with caution***)
  * device power/energy metrics
    * current `storage.energy()`
    * historical data `storage.energy_history()`
* Datalogger (*TYPE=3*)
  * ***Not*** implemented yet (TODO: refactor structure)
* MAX (*TYPE=4* - MAX)
  * general device data
    * read device data `max.details()`
    * read alarms/notification `max.alarms()`
  * device settings
    * read settings value `max.setting_read()`
    * write settings value `max.setting_write()` (***use with caution***)
  * device power/energy metrics
    * current `max.energy()`
    * current for multiple inverters `max.energy_multiple()`
    * historical data `max.energy_history()`
* SPH (*TYPE=5* - SPH/MIX) (TODO: refactor rename to MIX?)
  * general device data
    * read device data `sph.details()`
    * read alarms/notification `sph.alarms()`
  * device settings
    * read settings value `sph.setting_read()`
    * write settings value `sph.setting_write()` (***use with caution***)
  * device power/energy metrics
    * current `sph.energy()`
    * current for multiple inverters `sph.energy_multiple()`
    * historical data `sph.energy_history()`
* SPA (*TYPE=6* - SPA)
  * general device data
    * read device data `spa.details()`
    * read alarms/notification `spa.alarms()`
  * device settings
    * read settings value `spa.setting_read()`
    * write settings value `spa.setting_write()` (***use with caution***)
  * device power/energy metrics
    * current `spa.energy()`
    * current for multiple inverters `spa.energy_multiple()`
    * historical data `spa.energy_history()`
* MIN (*TYPE=7* - MIN/MAC/MOD-XH/MID-XH/NEO)
  * general device data
    * read device data `min.details()`
    * read alarms/notification `min.alarms()`
  * device settings
    * read settings overview `min.settings()`
    * read settings value `min.setting_read()`
    * write settings value `min.setting_write()` (***use with caution***)
  * device power/energy metrics
    * current `min.energy()`
    * current for multiple inverters `min.energy_multiple()`
    * historical data `min.energy_history()`
* PCS (*TYPE=8*)
  * general device data
    * read device data `pcs.details()`
    * read alarms/notification `pcs.alarms()`
  * device power/energy metrics
    * current `pcs.energy()`
    * historical data `pcs.energy_history()`
* HPS (*TYPE=9*)
  * general device data
    * read device data `hps.details()`
    * read alarms/notification `hps.alarms()`
  * device power/energy metrics
    * current `hps.energy()`
    * historical data `hps.energy_history()`
* PDB (*TYPE=10*)
  * ***Not*** implemented yet
* Smart meter (*TYPE=3*)
  * ***Not*** implemented yet
* Environment sensor (*TYPE=3*)
  * ***Not*** implemented yet
* VPP (*TYPE=3/5/6* MIN/SPH/SPA)
  * get current State-of-Charge (SOC) `vpp.soc()`
  * change time period settings
    * set current (dis)charge power `vpp.write()` (***use with caution***)
    * configure (dis)charge power for time periods `vpp.write_time_periods()` (***use with caution***)
* PDB (*TYPE=11* - GroBoost)
  * ***Not*** implemented yet

### API v4 (a few additional endpoints)
* ***Not*** implemented yet


# Usage
## Login
The API requires token authentication. The token can be retrieved via
* Growatt Android/iOS app "ShinePhone"
  * go to "Me" -> your username -> "API Token"
  * copy your token or request an new one
* Growatt web frontend at [openapi.growatt.com](http://openapi.growatt.com/)
  * login
  * click your username in the upper right corner
  * go to "Account Management" -> "API Token"
  * copy your token or request an new one

Pass the token when creating the API object
```python
from growatt_api import GrowattApi

api = GrowattApi(
    token="your_token",
    # for using a server other than "https://openapi.growatt.com", set the optional "server_url" parameter
    # server_url="https://openapi-cn.growatt.com",    # China
    # server_url="https://openapi-us.growatt.com",    # North America
    # server_url="http://openapi-au.growatt.com",     # Australia and New Zealand
    # server_url="https://openapi.growatt.com",       # Europe and rest of world
    # server_url="http://ess-server.atesspower.com",  # for ATESS users
)
```

## Examples

### get your plant ID
```python
plant_list = api.plant.list()
plant_id = plant_list.data.plants[0].plant_id
print(f"{plant_id=}")
# => plant_id=1234567
```

### get your devices
```python
from growatt_api import GrowattDeviceType

device_list = api.device.list(plant_id=plant_id)
device_sn = device_list.data.devices[0].device_sn
device_type = device_list.data.devices[0].type
print(f"{device_type=} ({GrowattDeviceType(device_type).name}), {device_sn=}")
# => device_type=7 (min), device_sn='BZP0000000'
```

### query device metrics
Use the submodule matching your device type to retrieve its metrics or settings
Note: Make sure to use `device.list()` for retrieving your device type - the internal type may differ form the marketing name.
```python
min_details = api.min.details(device_sn=device_sn)
print(min_details.data.model_dump_json())
# => {"alias":"BZP0000000","datalogger_sn":"QMN0000000000000","e_today":0.0,...}
```


# Contribution guidelines
If you see any bugs or improvement ideas, I would love to see a contribution from you.

Your options include
* Open an issue describing the bug or improvement idea
* Implement your changes and open a PR
  * run `flake8` and `black` on your code before committing
  * you can do this by using the pre-commit config of this rfepo
    ```shell
     pip install pre-commit
     cd GrowattPublicApiPy
     pre-commit install
     # git commit ...
     ```

# Contribution ideas
* add missing endpoints
  * I'm still working on adding endpoints, but any help is appreciated
* run code for different inverter types
  * I have a NEO (=MIN) inverter for testing, so I can't test the code for other inverter types.
  * just try to run the code for your inverter model and check the pydantic models are valid
* refactoring
  * while I like the idea of using single files for each inverter type, I think there might be a better way to do this ;)
* anything else you can think of


# Disclaimer
The developers & maintainers of this library accept no responsibility for any damage, problems or issues that arise with your Growatt systems as a result of its use.

The library contains functions that allow you to modify the configuration of your plant & inverter which carries the ability to set values outside of normal operating parameters, therefore, settings should only be modified if you understand the consequences.

To the best of our knowledge only the settings functions perform modifications to your system and all other operations are read only. Regardless of the operation:

***The library is used entirely at your own risk.***


# Changelog
* 2025.03.10 (pre-alpha)
  * endpoints implemented:
    * SPA
    * PCS
    * HPS
* 2025.03.05 (pre-alpha)
  * endpoints implemented:
    * MAX
    * SPH (MIX)
* 2025.03.04 (pre-alpha)
  * initial release
  * endpoints implemented:
    * Plant
    * Device
    * Datalogger
    * Inverter
    * Storage
    * MIN (MIN/MAC/MOD-XH/MID-XH/NEO)
    * VPP (MIN/SPH/SPA)
