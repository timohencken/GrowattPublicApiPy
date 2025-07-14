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
## ***Alpha***: The library is roughly feature-complete, but not yet proven to be working for users other than me.
### Note:
Reading/writing settings seems not to work. All tries I did returned "error code 1: SYSTEM_ERROR" :(
(But still I was able to set my inverter to standby mode, so it seems to work despite the error message)


# Usage
## Installation
This package is available at [PiPy](https://pypi.org/project/growatt-public-api) and can be installed using pip:
```shell
pip install growatt-public-api
```

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
device_list = api.plant.list_devices(plant_id=plant_id)
device_sn = device_list.data.devices[0].device_sn
device_type = api.device.get_device_type(device_sn=device_sn)
print(f"{device_type=}, {device_sn=}")
# => device_type=DeviceType.MIN, device_sn='BZP0000000'
```

### query device metrics
#### Option 1: use device-specifc API explicitly
Use the submodule matching your device type to retrieve its metrics or settings
Note: Make sure to use `device.get_device_type()` for retrieving your device type - the internal type may differ form the marketing name.
```python
min_details = api.min.details(device_sn=device_sn)
print(min_details.data.model_dump_json())
# => {"alias":"BZP0000000","datalogger_sn":"QMN0000000000000","e_today":0.0,...}
```
#### Option 2: use the convenience API to automatically detect and use the correct device type
Here, retrieve the correct decive API's instance by using `api.api_for_device(device_sn=device_sn)`.
In following calls, the device_sn does not need to be supplied anymore.
```python
my_device = api.api_for_device(device_sn=device_sn)
# my_device will be of type `Min` for MIN devices with device_sn pre-set
min_details = my_device.details()
print(min_details.data.model_dump_json())
# => {"alias":"BZP0000000","datalogger_sn":"QMN0000000000000","e_today":0.0,...}
```

# Submodules and methods

## User
* list users
  * `user.list()`
* check username available
  * `user.check_username()`
* add user
  * `user.register()`
* modify user information
  * `user.modify()`

## Plant
* plant management
  * add new plant `plant.add()`
  * modify plant `plant.modify()`
  * delete plant `plant.delete()`
  * add inverter to plant `plant.add_device()`
  * add datalogger to plant `plant.add_datalogger()`
  * remove datalogger from plant `plant.remove_datalogger()`
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
* list devices assigned to plant
  * list dataloggers `plant.list_dataloggers()`
  * list inverters/storage `plant.list_devices()`

## Datalogger
* verify datalogger's CC code
  * `device.datalogger_validate()`
* get sensors attached to datalogger
  * get smart meters `datalogger.list_smart_meters()`
  * get environmental sensors `datalogger.list_env_sensors()`

## Device (*ALL* inverter types)
* get devices (inverters) assigned to current user
  * `device.list()`
  * see also
    * `plant.list_devices()`
    * `plant.list_dataloggers()`
    * `datalogger.list_smart_meters()`
    * `datalogger.list_env_sensors()`
* query device type
  * `device.get_device_type()`
    *** use this method to query your inverter's type ***
* get device creation date
  * `device.create_date()`
* device power/energy metrics
  * get energy (sum) for specific day `device.energy_day()`
* get device tree
  * get plant by device_sn `device.get_plant()`
  * get datalogger by device_sn `device.get_datalogger()`

## Inverter (DeviceType.INVERTER)
* general device data
  * read device data
    * `inverter.details()`
    * `inverter.details_v4()` (using new API)
  * read alarms/notification `inverter.alarms()`
* device power/energy metrics
  * current
    * `inverter.energy()`
    * `inverter.energy_v4()` (using new API)
    * `inverter.energy_multiple()`
  * historical data
    * `inverter.energy_history()`
    * `inverter.energy_history_v4()` (using new API)
    * `inverter.energy_history_multiple_v4()` (using new API)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings
  * read settings value `inverter.setting_read()`
  * write settings value
    * `inverter.setting_write()` (***use with caution***)
    * `inverter.setting_write_on_off()` (using new API)
    * `inverter.setting_write_active_power()` (using new API)

## Storage (DeviceType.STORAGE)
* general device data
  * read device data
    * `storage.details()`
    * `storage.details_v4()` (using new API)
  * read alarms/notification `storage.alarms()`
* device power/energy metrics
  * current
    * `storage.energy()`
    * `storage.energy_v4()` (using new API)
  * historical data
    * `storage.energy_history()`
    * `storage.energy_history_v4()` (using new API)
    * `storage.energy_history_multiple_v4()` (using new API)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings
  * read settings value `storage.setting_read()`
  * write settings value
    * `storage.setting_write()` (***use with caution***)
    * `storage.setting_write_on_off()` (using new API)
    * `storage.setting_write_active_power()` (using new API)

## MAX (DeviceType.MAX)
* general device data
  * read device data
    * `max.details()`
    * `max.details_v4()` (using new API)
  * read alarms/notification `max.alarms()`
* device power/energy metrics
  * current
    * `max.energy()`
    * `max.energy_multiple()`
    * `max.energy_v4()` (using new API)
  * historical data
    * `max.energy_history()`
    * `max.energy_history_v4()` (using new API)
    * `max.energy_history_multiple_v4()` (using new API)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings
  * read settings value `max.setting_read()`
  * write settings value
    * `max.setting_write()` (***use with caution***)
    * `max.setting_write_on_off()` (using new API)
    * `max.setting_write_active_power()` (using new API)

## SPH (DeviceType.SPH - (MIX))
* general device data
  * read device data
    * `sph.details()`
    * `sph.details_v4()` (using new API)
  * read alarms/notification `sph.alarms()`
* device power/energy metrics
  * current
    * `sph.energy()`
    * `sph.energy_multiple()`
    * `sph.energy_v4()` (using new API)
  * historical data
    * `sph.energy_history()`
    * `sph.energy_history_v4()` (using new API)
    * `sph.energy_history_multiple_v4()` (using new API)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings
  * read settings value
    * `sph.setting_read()`
    * `sph.setting_read_vpp_param()` (using new API)
  * write settings value
    * `sph.setting_write()` (***use with caution***)
    * `sph.setting_write_on_off()` (using new API)
    * `sph.setting_write_active_power()` (using new API)
    * `sph.setting_write_vpp_param()` (using new API)
  * VPP (VirtualPowerPlant) settings
    * get current State-of-Charge (SOC) `sph.soc()`
    * read vpp schedules
      * `sph.setting_read_vpp_param()` (using new API)
    * write vpp schedules
      * `sph.setting_write_vpp_now()`
      * `sph.setting_write_vpp_schedule()`
      * `sph.setting_write_vpp_param()` (using new API)

## SPA (DeviceType.SPA)
* general device data
  * read device data
    * `spa.details()`
    * `spa.details_v4()` (using new API)
  * read alarms/notification `spa.alarms()`
* device power/energy metrics
  * current
    * `spa.energy()`
    * `spa.energy_multiple()`
    * `spa.energy_v4()` (using new API)
  * historical data
    * `spa.energy_history()`
    * `spa.energy_history_v4()` (using new API)
    * `spa.energy_history_multiple_v4()` (using new API)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings
  * read settings value
    * `spa.setting_read()`
  * write settings value
    * `spa.setting_write()` (***use with caution***)
    * `spa.setting_write_on_off()` (using new API)
    * `spa.setting_write_active_power()` (using new API)
  * VPP (VirtualPowerPlant) settings
    * get current State-of-Charge (SOC) `spa.soc()`
    * read vpp schedules
      * `spa.setting_read_vpp_param()` (using new API)
    * write vpp schedules
      * `spa.setting_write_vpp_now()`
      * `spa.setting_write_vpp_schedule()`
      * `spa.setting_write_vpp_param()` (using new API)

## MIN (DeviceType.MIN - TLX/MIN/MAC/MOD-XH/MID-XH/NEO)
* general device data
  * read device data
    * `min.details()`
    * `min.details_v4()` (using new API)
  * read alarms/notification `min.alarms()`
* device power/energy metrics
  * current
    * `min.energy()`
    * `min.energy_v4()` (using new API)
    * `min.energy_multiple()`
  * historical data
    * `min.energy_history()`
    * `min.energy_history_v4()` (using new API)
    * `min.energy_history_multiple_v4()` (using new API)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings
  * read settings overview `min.settings()`
  * read settings value
    * `min.setting_read()`
  * write settings value
    * `min.setting_write()` (***use with caution***)
    * `min.setting_write_on_off()` (using new API)
    * `min.setting_write_active_power()` (using new API)
  * VPP (VirtualPowerPlant) settings
    * get current State-of-Charge (SOC) `min.soc()`
    * read vpp schedules
      * `min.setting_read_vpp_param()` (using new API)
    * write vpp schedules
      * `min.setting_write_vpp_now()`
      * `min.setting_write_vpp_schedule()`
      * `min.setting_write_vpp_param()` (using new API)

## PCS (DeviceType.PCS)
* general device data
  * read device data `pcs.details()`
  * read alarms/notification `pcs.alarms()`
* device power/energy metrics
  * current `pcs.energy()`
  * historical data `pcs.energy_history()`
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything

## HPS (DeviceType.HPS)
* general device data
  * read device data `hps.details()`
  * read alarms/notification `hps.alarms()`
* device power/energy metrics
  * current `hps.energy()`
  * historical data `hps.energy_history()`
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything

## PBD (DeviceType.PBD)
* general device data
  * read device data `pbd.details()`
  * read alarms/notification `pbd.alarms()`
* device power/energy metrics
  * current `pbd.energy()`
  * historical data `pbd.energy_history()`
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything

## WIT (DeviceType.WIT)
*Note: WIT devices are not supported by APIv1 endpoints - only v4 endpoints available*
* general device data
  * read device data
    * `wit.details_v4()` (using new API)
* device power/energy metrics
  * current
    * `wit.energy_v4()` (using new API)
  * historical data
    * `wit.energy_history_v4()` (using new API)
    * `wit.energy_history_multiple_v4()` (using new API)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings
  * write settings value
    * `wit.setting_write_on_off()` (using new API)
    * `wit.setting_write_active_power()` (using new API)
  * VPP (VirtualPowerPlant) settings
    * read vpp schedules
      * `wit.setting_read_vpp_param()` (using new API)
    * write vpp schedules
      * `wit.setting_write_vpp_param()` (using new API)

## SPH-S (DeviceType.SPHS)
*Note: SPH-S devices are not supported by APIv1 endpoints - only v4 endpoints available*
* general device data
  * read device data
    * `sphs.details_v4()` (using new API)
* device power/energy metrics
  * current
    * `sphs.energy_v4()` (using new API)
  * historical data
    * `sphs.energy_history_v4()` (using new API)
    * `sphs.energy_history_multiple_v4()` (using new API)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings
  * write settings value
    * `sphs.setting_write_on_off()` (using new API)
    * `sphs.setting_write_active_power()` (using new API)
  * VPP (VirtualPowerPlant) settings
    * read vpp schedules
      * `sphs.setting_read_vpp_param()` (using new API)
    * write vpp schedules
      * `sphs.setting_write_vpp_param()` (using new API)

## Noah (DeviceType.NOAH)
*Note: Noah devices are not supported by APIv1 endpoints - only v4 endpoints available*
* general device data
  * read device data
    * `noah.details_v4()` (using new API)
* device power/energy metrics
  * current
    * `noah.energy_v4()` (using new API)
  * historical data
    * `noah.energy_history_v4()` (using new API)
    * `noah.energy_history_multiple_v4()` (using new API)
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything
* device settings
  * read settings value
    * `noah.setting_read_vpp_param()` (using new API)
  * write settings value
    * `noah.setting_write_on_off()` (using new API)
    * `noah.setting_write_active_power()` (using new API)
    * `noah.setting_write_vpp_param()` (using new API)
  * VPP (VirtualPowerPlant) settings
    * read vpp schedules
      * `noah.setting_read_vpp_param()` (using new API)
    * write vpp schedules
      * `noah.setting_write_vpp_param()` (using new API)

## GroBoost (DeviceType.GROBOOST)
* general device data
  * read device data `groboost.details()`
* device metrics
  * current `groboost.metrics()`
  * current for multiple devices `groboost.metrics_multiple()`
  * historical data `groboost.metrics_history()`
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything

## Smart meter (DeviceType.OTHER - SmartMeter/SDM/CHNT)
* get meters attached to datalogger
  * `datalogger.list_smart_meters()`
* device power/energy metrics
  * current `smart_meter.energy()`
  * historical data `smart_meter.energy_history()`
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything

## Environmental sensor (DeviceType.OTHER - Temperature/Humidity/Wind/...)
* get sensors attached to datalogger
  * `datalogger.list_env_sensors()`
* device metrics
  * current `env_sensor.metrics()`
  * historical data `env_sensor.metrics_history()`
    * Note: historical data seems to be restricted to 95 days - for earlier dates, API does not return anything

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
* run code for different inverter types
  * I have a NEO (=MIN) inverter for testing, and I found some devices on the test environments, but some device types remain untested.
  * just try to run the code for your inverter model and check the pydantic models are valid
* anything else you can think of


# Disclaimer
The developers & maintainers of this library accept no responsibility for any damage, problems or issues that arise with your Growatt systems as a result of its use.

The library contains functions that allow you to modify the configuration of your plant & inverter which carries the ability to set values outside of normal operating parameters, therefore, settings should only be modified if you understand the consequences.

To the best of our knowledge only the settings functions perform modifications to your system and all other operations are read only. Regardless of the operation:

***The library is used entirely at your own risk.***

# TODOs
* TODO: generate & publish docs

# Changelog
* 2025.07.14 (alpha)
  * packaging & deploy to [PyPi](https://pypi.org/project/growatt-public-api)
  * removed truststore SSL certificate injection
* 2025.07.11 (pre-alpha)
  * moved common pydantic models (e.g. `GrowattTimeCalendar`) to common module
  * cache API requests (using TMP directory) to avoid 'API rate limit exceeded' errors
* 2025.06.03 (pre-alpha)
  * new [example for MIN](examples/min_data.py) devices (e.g. NEO)
  * convenience method `api_for_device()` for retrieving device-specific API
    ```python
    from growatt_api import GrowattApi
    api = GrowattApi(token="your_token")
    # now you can get your device-specifc api by
    my_device = api.api_for_device(device_sn="your_device_sn")
    # this returns e.g. `api.min` for MIN devices
    # arguments "device_sn" does not need to be supplied anymore, so you can do e.g.
    min_details = my_device.details()
    # instead of
    min_details = api.min.details(device_sn="your_device_sn")
    print(min_details.data.model_dump_json())
    ```
* 2025.05.22 (pre-alpha)
  * refactoring: moved some endpoints from/to plant/device/datalogger
  * refactoring: moved some endpoints from/to smart_meter/env_sensor/datalogger
  * common device type `growatt_public_api.DeviceType`
    * retrieve device type by `api.device.get_device_type()`
  * refactoring: integrate v4 endpoints in "normal" code (use submodule instead of device_type parameter)
  * refactoring: integrate VPP into MIN,SPA,SPH
* 2025.05.12 (pre-alpha)
  * add tests to verify returned parameters are same as expected parameters
* 2025.03.28 (pre-alpha)
  * v4/new-api endpoints implemented
* 2025.03.11 (pre-alpha)
  * all API v1 endpoints implemented
