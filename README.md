# GrowattApi
A python implementation of [Growatt](https://en.growatt.com/)'s public API.


# Motivation
There are already other libraries accessing Growatt's APIs, they all use reverse-engineered calls to internal, undocumented APIs.
* for example, see the faboulous work of [indykoning](https://github.com/indykoning) at [PyPi_GrowattServer](https://github.com/indykoning/PyPi_GrowattServer) used e.g. in HomeAssistant

This package aims to
* use type-aware pydantic objects as return values
* use Growatt's public API documented
  * [here (v1)](https://www.showdoc.com.cn/262556420217021/0)
    * /v1/ endpoints
    * user/plant management
    * metrics
    * settings read/write
    * inv/storage/max/sph/spa/min/pcs/hps/pbd/smart_meter/env_sensor/vpp/groboost (no wit/sph-s/noah)
  * [here (v4)](https://www.showdoc.com.cn/2540838290984246/0)
    * /v4/new-api endpoints
    * no user/plant management
    * new endpoints for metrics
    * settings write only on/off and NOAH time periods
    * inv/storage/sph/max/spa/min/wit/sph-s/noah (no pcs/hps/pbd/smart_meter/env_sensor/vpp/groboost)
  * [here (v1/v4 mixed)](https://www.showdoc.com.cn/2598832417617967/0)
    * mixed documentation - different sorting
    * vpp settings (in addition to other /v4/ docs)
  * [here (/v1/v4 postman)](https://www.postman.com/gold-water-163355/growatt-public/collection/fw8cldm/shineserver-public)
    * postman collection implementing some (known) endpoints


# Implementation status
## ***Alpha***: The library is in an early stage of development and is not yet feature complete.

### API v1 (full featured API)
* User
  * list users
    * `user.list()`
  * check username available
    * `user.check_username()`
  * add user
    * `user.register()`
  * modify user information
    * `user.modify()`
* Plant
  * plant management
    * add new plant `plant.add()`
    * modify plant `plant.modify()`
    * delete plant `plant.delete()`
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
* Datalogger
  * datalogger management
    * add datalogger to plant `device.datalogger_add()`
    * remove datalogger from plant `device.datalogger_delete()`
  * list dataloggers
    * `device.datalogger_list()`
  * query device type
    * `device.type_info()`
    * *** this is NOT the same as the inverter type ***
  * verify datalogger's CC code
    * `device.datalogger_validate()`
* Generic - all inverter types
  * get inverters assigned to plant
    * `device.list()`
    * ***use this to query your inverter's*** "*TYPE*" ***for selecting the correct submodule***
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
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
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
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
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
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
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
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
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
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
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
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* PCS (*TYPE=8*)
  * general device data
    * read device data `pcs.details()`
    * read alarms/notification `pcs.alarms()`
  * device power/energy metrics
    * current `pcs.energy()`
    * historical data `pcs.energy_history()`
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* HPS (*TYPE=9*)
  * general device data
    * read device data `hps.details()`
    * read alarms/notification `hps.alarms()`
  * device power/energy metrics
    * current `hps.energy()`
    * historical data `hps.energy_history()`
* PBD (*TYPE=10*)
  * general device data
    * read device data `pbd.details()`
    * read alarms/notification `pbd.alarms()`
  * device power/energy metrics
    * current `pbd.energy()`
    * historical data `pbd.energy_history()`
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* Smart meter (*TYPE=3* - SmartMeter/SDM/CHNT)
  * get meters attached to datalogger
    * `smart_meter.list()`
  * device power/energy metrics
    * current `smart_meter.energy()`
    * historical data `smart_meter.energy_history()`
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* Environmental sensor (*TYPE=3* - Temperature/Humidity/Wind/...)
  * get sensors attached to datalogger
    * `env_sensor.list()`
  * device metrics
    * current `env_sensor.metrics()`
    * historical data `env_sensor.metrics_history()`
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* VPP (VirtualPowerPlant *TYPE=3/5/6* - MIN/SPH/SPA)
  * get current State-of-Charge (SOC) `vpp.soc()`
  * change time period settings
    * set current (dis)charge power `vpp.write()` (***use with caution***)
    * configure (dis)charge power for time periods `vpp.write_time_periods()` (***use with caution***)
* GroBoost (*TYPE=11* - GroBoost)
  * general device data
    * read device data `groboost.details()`
  * device metrics
    * current `groboost.metrics()`
    * current for multiple devices `groboost.metrics_multiple()`
    * historical data `groboost.metrics_history()`
      * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything

### API v4 (a few additional endpoints)
* get devices (inverters) assigned to current user
  * `v4.list()`
    ***use this to query your inverter's*** "*TYPE*" ***required for subsequent requests***
* general device data
  * read device data `v4.details()`
* device metrics
  * current `v4.energy()`
    * Note for NOAH: API docs are incomplete. I would be happy if you dump NOAHs output and create a github issue.
  * historical data `v4.energy_history()`
  * historical data `v4.energy_history_multiple()` (query multiple devices at once)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings (***use with caution***)
  * power on/off: `v4.setting_write_on_off()`
  * configure active power percentage: `v4.setting_write_active_power()`
    * Note: for NOAH devices, pass 0~800W instead of 0~100%
  * configure SOC limits: `v4.setting_write_soc_upper_limit()` / `v4.setting_write_soc_lower_limit()`
    * Note: only for NOAH devices
  * configure time period `v4.setting_write_time_period()`
    * Note: only for NOAH devices
  * configure VPP parameters: `v4.setting_write_vpp_param()` / `v4.setting_write_vpp_param()`
    * Note: The current interface only supports sph, spa, min, wit device types.
      The specific models are as follows: SPH 3000-6000TL BL, SPA 1000-3000TL BL, SPH 3000-6000TL BL US, SPH 4000-10000TL3 BH, SPA 4000-10000TL3 BH, MIN 2500-6000TL-XH US, MIN 2500-6000TL-XH, MOD-XH\MID-XH, WIT 100KTL3-H, WIS 215KTL3


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
  * copy your token or request a new one

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

# TODOs
* TODO: refactor to integrate v4 endpoints in "normal" code (use submodule instead of device_type parameter)
* TODO: add caching to 5-minute-interval endpoints
  * ongoing - still some TODOs
* TODO: common device type
* TODO: generate & publish docs

# Changelog
* ONGOING (pre-alpha)
  * add tests to verify returned parameters are same as expected parameters
* 2025.03.28 (pre-alpha)
  * v4/new-api endpoints implemented
* 2025.03.11 (pre-alpha)
  * all API v1 endpoints implemented
