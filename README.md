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
    * `inverter.wifi_strength()` (using new API)
  * read alarms/notification `inverter.alarms()`
* device power/energy metrics
  * current
    * `inverter.power()` (using new API)
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
    * `max.wifi_strength()` (using new API)
  * read alarms/notification `max.alarms()`
* device power/energy metrics
  * current
    * `max.power()` (using new API)
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
    * `sph.wifi_strength()` (using new API)
  * read alarms/notification `sph.alarms()`
* device power/energy metrics
  * current
    * `sph.power()` (using new API)
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
      * `sph.setting_write_vpp_param_new()` (using new API)
      * `sph.setting_clear_vpp_time_period()` (using new API)

## SPA (DeviceType.SPA)
* general device data
  * read device data
    * `spa.details()`
    * `spa.details_v4()` (using new API)
    * `spa.wifi_strength()` (using new API)
  * read alarms/notification `spa.alarms()`
* device power/energy metrics
  * current
    * `spa.power()` (using new API)
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
      * `spa.setting_write_vpp_param_new()` (using new API)
      * `spa.setting_clear_vpp_time_period()` (using new API)

## MIN (DeviceType.MIN - TLX/MIN/MAC/MOD-XH/MID-XH/NEO)
* general device data
  * read device data
    * `min.details()`
    * `min.details_v4()` (using new API)
    * `min.wifi_strength()` (using new API)
  * read alarms/notification `min.alarms()`
* device power/energy metrics
  * current
    * `min.power()` (using new API)
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
      * `min.setting_write_vpp_param_new()` (using new API)
      * `min.setting_clear_vpp_time_period()` (using new API)

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
    * `wit.wifi_strength()` (using new API)
* device power/energy metrics
  * current
    * `wit.power()` (using new API)
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
      * `wit.setting_write_vpp_param_new()` (using new API)
      * `wit.setting_clear_vpp_time_period()` (using new API)

## SPH-S (DeviceType.SPHS)
*Note: SPH-S devices are not supported by APIv1 endpoints - only v4 endpoints available*
* general device data
  * read device data
    * `sphs.details_v4()` (using new API)
    * `sphs.wifi_strength()` (using new API)
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

## NOAH (DeviceType.NOAH - NOAH/NEXA)
*Note: Noah devices are not supported by APIv1 endpoints - only v4 endpoints available*
* general device data
  * read device data
    * `noah.details_v4()` (using new API)
    * `noah.wifi_strength()` (using new API)
* device power/energy metrics
  * current
    * `noah.status()` (using APP API)
    * `noah.power()` (using new API)
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
    * `noah.setting_write_grid_charging()` (using new API)
    * `noah.setting_write_off_grid()` (using new API)
    * `noah.setting_write_vpp_param()` (using new API)
  * assign inverter to noah system
    * `noah.setting_write_assign_inverter()` (using new API)
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
  * I have a NEO (=MIN) and NEXA (=NOAH) inverter for testing, and I found some devices on the test environments, but some device types remain untested.
  * just try to run the code for your inverter model and check the pydantic models are valid
* anything else you can think of


# Disclaimer
The developers & maintainers of this library accept no responsibility for any damage, problems or issues that arise with your Growatt systems as a result of its use.

The library contains functions that allow you to modify the configuration of your plant & inverter which carries the ability to set values outside of normal operating parameters, therefore, settings should only be modified if you understand the consequences.

To the best of our knowledge only the settings functions perform modifications to your system and all other operations are read only. Regardless of the operation:

***The library is used entirely at your own risk.***

# TODOs
* TODO: generate & publish docs
* add missing endpoints
  * Nexa endpoints from App
    * ```
      /noahDeviceApi/noah/getBatteryData
      "deviceSn": {serialNumber},
      ```
    * ```
      response = self.session.request(
          "POST",
          url='https://openapi.growatt.com/v4/noahDeviceApi/nexa/getNexaInfoBySn',
          #                                  /noahDeviceApi/noah/getNoahInfoBySn
          # see https://github.com/indykoning/PyPi_GrowattServer/blob/45e3fce44c32be16eec6cc049549a78b1e11233f/growattServer/base_api.py#L909
          params=None,
          data={'deviceSn': 'DEVICE_SN'},
      )
      print(response.text)
      print(response.status_code)
      # => {"msg":"","result":1,"obj":{"unitKeyList":["RMB","EUR","GBP","USD","AUD","BGN","BRC","CAD","CHF","CZK","DKK","HKD","HRK","HUF","IDR","NIS","INR","JPY","KRW","MXN","MYR","NOK","NZD","PHP","PLN","RON","RUB","SEK","SGD","THB","TRY","ZAR","AED","AFN","ALL","AMD","ANG","AOA","ARP","AWG","AZN","BAM","BBD","BDT","BHD","BIF","BND","BOB","BSD","BTN","BWP","BYN","BZD","CDF","CLP","COP","CRC","CUP","CVE","DJF","DOP","DZD","EGP","ERN","ETB","FJD","FKP","GEL","GHS","GIP","GMD","GNF","GTQ","GYD","HNL","HTG","IQD","IRR","ISK","JMD","JOD","KES","KGS","KHR","KMF","KPW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","BUK","MNT","MOP","MRU","MUR","MVR","MWK","MZN","NAD","NGN","NIO","NPR","OMR","PAB","PEN","PGK","PKR","PYG","QAR","RSD","RWF","SAR","SBD","SCR","SDG","SHP","SLL","SOS","SRD","SSP","STN","SVC","SYP","SZL","TJS","TMT","TND","TOP","TTD","TWD","TZS","UAH","UGX","UYU","UZS","VEF","VND","VUV","WST","XAF","XCD","XOF","XPF","YER","ZMW","BMD","THP"],"unitList":{"FJD":"FJD","MXN":"MXN","SCR":"SCR","CDF":"CDF","BBD":"BBD","GTQ":"GTQ","CLP":"CLP","HNL":"HNL","UGX":"UGX","ZAR":"ZAR","TND":"TND","STN":"STN","BSD":"BSD","SLL":"SLL","SDG":"SDG","IQD":"IQD","CUP":"CUP","GMD":"GMD","TWD":"TWD","RSD":"RSD","DOP":"DOP","KMF":"KMF","MYR":"MYR","FKP":"FKP","XOF":"XOF","GEL":"GEL","UYU":"UYU","MAD":"MAD","CVE":"CVE","TOP":"TOP","AZN":"AZN","OMR":"OMR","PGK":"PGK","SEK":"SEK","KES":"KES","BTN":"BTN","UAH":"UAH","GNF":"GNF","ARP":"ARP","ERN":"ERN","MZN":"MZN","SVC":"SVC","QAR":"QAR","IRR":"IRR","THB":"THB","UZS":"UZS","XPF":"XPF","MRU":"MRU","BDT":"BDT","LYD":"LYD","BMD":"BMD","PHP":"PHP","KWD":"KWD","BUK":"BUK","THP":"THP","RUB":"RUB","PYG":"PYG","ISK":"ISK","JMD":"JMD","COP":"COP","RMB":"RMB","USD":"USD","MKD":"MKD","DZD":"DZD","PAB":"PAB","SGD":"SGD","ETB":"ETB","KGS":"KGS","SOS":"SOS","VEF":"VEF","VUV":"VUV","LAK":"LAK","BND":"BND","XAF":"XAF","LRD":"LRD","CHF":"CHF","HRK":"HRK","ALL":"ALL","DJF":"DJF","ZMW":"ZMW","TZS":"TZS","VND":"VND","AUD":"AUD","GHS":"GHS","GYD":"GYD","KPW":"KPW","BOB":"BOB","KHR":"KHR","MDL":"MDL","IDR":"IDR","KYD":"KYD","AMD":"AMD","TRY":"TRY","BWP":"BWP","SHP":"SHP","LBP":"LBP","TJS":"TJS","JOD":"JOD","HKD":"HKD","AED":"AED","RWF":"RWF","EUR":"EUR","LSL":"LSL","DKK":"DKK","CAD":"CAD","BGN":"BGN","NOK":"NOK","MUR":"MUR","SYP":"SYP","GIP":"GIP","RON":"RON","LKR":"LKR","NGN":"NGN","CZK":"CZK","CRC":"CRC","PKR":"PKR","XCD":"XCD","ANG":"ANG","HTG":"HTG","BHD":"BHD","KZT":"KZT","SRD":"SRD","SZL":"SZL","SAR":"SAR","TTD":"TTD","YER":"YER","MVR":"MVR","AFN":"AFN","INR":"INR","KRW":"KRW","AWG":"AWG","NPR":"NPR","JPY":"JPY","MNT":"MNT","PLN":"PLN","AOA":"AOA","GBP":"GBP","SBD":"SBD","BYN":"BYN","HUF":"HUF","BIF":"BIF","MWK":"MWK","MGA":"MGA","BZD":"BZD","BAM":"BAM","EGP":"EGP","MOP":"MOP","NAD":"NAD","SSP":"SSP","BRC":"BRC","NIO":"NIO","PEN":"PEN","NIS":"NIS","NZD":"NZD","WST":"WST","TMT":"TMT"},"noah":{"acCouple":"true","time_segment":[{"time_segment3":"2_0:0_23:59_0_0"}],"workMode":"2","antiBackflowEnable":"1","acCouplePowerControl":"1","ammeterModel":"Shelly Pro 3EM","acCoupleEnable":"1","deviceSn":"DEVICE_SN","safety":1,"alias":"NEXA 2000","ammeterSn":"149618405023988","model":"NEXA 2000","shellyList":[],"gridSet":"1","antiBackflowPowerPercentage":"0","tempType":"0","batSns":["DEVICE_SN","0HYR40ZR23FT0007"],"safetyList":[{"safetyCorrespondNum":1,"countryAndArea":"German"},{"safetyCorrespondNum":2,"countryAndArea":"Netherlands"},{"safetyCorrespondNum":3,"countryAndArea":"Belgium"},{"safetyCorrespondNum":4,"countryAndArea":"French"},{"safetyCorrespondNum":5,"countryAndArea":"EN 50549-1"}],"plantId":"PLANT_ID","chargingSocHighLimit":"100","version":"11.10.09.07.9000.4017","chargingSocLowLimit":"10","formulaMoney":"0.4","ctType":"0","allowGridCharging":"1","defaultMode":"0","smartPlan":"true","safetyEnable":"true","defaultACCouplePower":"100","gridConnectionControl":"0","plantName":"Solarzaun","moneyUnitText":"EUR"},"plantList":[{"plantId":"PLANT_ID","plantImgName":"","plantName":"Solarzaun"}]}}
      # => 200
      ```
    * chart 5min data
      ```
      response = self.session.request(
          "POST",
          url='https://openapi.growatt.com/v4/noahDeviceApi/nexa/getNexaChartData',
          params=None,
          data={
              'deviceSn': 'DEVICE_SN',
              'date': '2025-10-01'
          },
      )
      print(response.text)
      print(response.status_code)
      # => {"msg":"","result":1,"obj":{"01:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"18:50":{"totalHouseholdLoad":"403","pac":"0","ppv":"0"},"02:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"08:05":{"totalHouseholdLoad":"557","pac":"0","ppv":"0"},"02:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"07:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"08:00":{"totalHouseholdLoad":"775","pac":"0","ppv":"0"},"20:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"07:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"01:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"14:15":{"totalHouseholdLoad":"216","pac":"0","ppv":"333.5"},"13:45":{"totalHouseholdLoad":"260","pac":"0","ppv":"220"},"20:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"19:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"14:10":{"totalHouseholdLoad":"65488","pac":"0","ppv":"341"},"19:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"13:40":{"totalHouseholdLoad":"301.5","pac":"0","ppv":"163.5"},"18:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"02:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"01:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"19:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"07:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"20:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"02:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"20:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"01:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"07:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"14:25":{"totalHouseholdLoad":"131","pac":"0","ppv":"291"},"06:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"13:55":{"totalHouseholdLoad":"138","pac":"0","ppv":"294"},"20:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"13:50":{"totalHouseholdLoad":"264.5","pac":"0","ppv":"280.5"},"19:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"14:20":{"totalHouseholdLoad":"65458.5","pac":"0","ppv":"337"},"02:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"02:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"08:25":{"totalHouseholdLoad":"412","pac":"0","ppv":"0"},"07:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"08:20":{"totalHouseholdLoad":"536","pac":"0","ppv":"36"},"07:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"13:25":{"totalHouseholdLoad":"156","pac":"0","ppv":"319.5"},"12:55":{"totalHouseholdLoad":"873.5","pac":"0","ppv":"257"},"18:35":{"totalHouseholdLoad":"1376","pac":"0","ppv":"0"},"19:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"13:20":{"totalHouseholdLoad":"242","pac":"0","ppv":"311.5"},"18:30":{"totalHouseholdLoad":"2446","pac":"0","ppv":"0"},"12:50":{"totalHouseholdLoad":"296.5","pac":"0","ppv":"258"},"19:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"18:40":{"totalHouseholdLoad":"373","pac":"0","ppv":"0"},"02:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"08:15":{"totalHouseholdLoad":"505.5","pac":"0","ppv":"30.5"},"02:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"07:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"20:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"08:10":{"totalHouseholdLoad":"552","pac":"0","ppv":"13.5"},"13:35":{"totalHouseholdLoad":"216.5","pac":"0","ppv":"275.5"},"07:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"14:05":{"totalHouseholdLoad":"65521.5","pac":"0","ppv":"336"},"18:45":{"totalHouseholdLoad":"456.5","pac":"0","ppv":"0"},"19:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"14:00":{"totalHouseholdLoad":"272.5","pac":"0","ppv":"356.5"},"19:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"13:30":{"totalHouseholdLoad":"137","pac":"0","ppv":"361"},"00:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"01:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"01:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"00:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"12:35":{"totalHouseholdLoad":"311","pac":"0","ppv":"232.5"},"13:00":{"totalHouseholdLoad":"237","pac":"0","ppv":"295"},"13:05":{"totalHouseholdLoad":"167.5","pac":"0","ppv":"290"},"17:45":{"totalHouseholdLoad":"4928","pac":"0","ppv":"0"},"18:15":{"totalHouseholdLoad":"336","pac":"0","ppv":"0"},"12:30":{"totalHouseholdLoad":"291","pac":"0","ppv":"245"},"17:40":{"totalHouseholdLoad":"2401.5","pac":"0","ppv":"21"},"18:10":{"totalHouseholdLoad":"1416.5","pac":"0","ppv":"28.5"},"23:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"01:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"17:50":{"totalHouseholdLoad":"1816.5","pac":"0","ppv":"0"},"01:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"00:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"00:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"12:45":{"totalHouseholdLoad":"307","pac":"0","ppv":"243"},"13:15":{"totalHouseholdLoad":"213","pac":"0","ppv":"294"},"17:55":{"totalHouseholdLoad":"2388","pac":"0","ppv":"47"},"18:25":{"totalHouseholdLoad":"411","pac":"0","ppv":"0"},"13:10":{"totalHouseholdLoad":"721.5","pac":"0","ppv":"298"},"18:20":{"totalHouseholdLoad":"1410.5","pac":"0","ppv":"0"},"12:40":{"totalHouseholdLoad":"333","pac":"0","ppv":"225.5"},"01:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"02:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"22:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"02:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"07:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"07:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"01:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"22:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"11:45":{"totalHouseholdLoad":"275.5","pac":"0","ppv":"149"},"12:10":{"totalHouseholdLoad":"376.5","pac":"0","ppv":"196.5"},"12:15":{"totalHouseholdLoad":"206","pac":"0","ppv":"246.5"},"16:50":{"totalHouseholdLoad":"291.5","pac":"0","ppv":"121"},"17:25":{"totalHouseholdLoad":"110","pac":"0","ppv":"76.5"},"16:55":{"totalHouseholdLoad":"341","pac":"0","ppv":"110.5"},"17:20":{"totalHouseholdLoad":"243.5","pac":"0","ppv":"81"},"11:40":{"totalHouseholdLoad":"279.5","pac":"0","ppv":"159"},"00:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"07:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"01:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"01:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"07:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"00:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"11:55":{"totalHouseholdLoad":"234.5","pac":"0","ppv":"201.5"},"18:05":{"totalHouseholdLoad":"2371","pac":"0","ppv":"21"},"12:25":{"totalHouseholdLoad":"219.5","pac":"0","ppv":"243"},"17:35":{"totalHouseholdLoad":"223","pac":"0","ppv":"54"},"11:50":{"totalHouseholdLoad":"328","pac":"0","ppv":"165"},"12:20":{"totalHouseholdLoad":"310","pac":"0","ppv":"244"},"17:30":{"totalHouseholdLoad":"285","pac":"0","ppv":"63"},"18:00":{"totalHouseholdLoad":"270","pac":"0","ppv":"47"},"00:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"00:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"22:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:55":{"totalHouseholdLoad":"153","pac":"0","ppv":"173"},"22:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"11:20":{"totalHouseholdLoad":"1980","pac":"0","ppv":"147"},"10:55":{"totalHouseholdLoad":"120","pac":"0","ppv":"290"},"09:50":{"totalHouseholdLoad":"184.5","pac":"0","ppv":"152.5"},"11:25":{"totalHouseholdLoad":"32814","pac":"0","ppv":"159.5"},"17:05":{"totalHouseholdLoad":"359","pac":"0","ppv":"108.5"},"17:00":{"totalHouseholdLoad":"367","pac":"0","ppv":"104"},"16:30":{"totalHouseholdLoad":"97","pac":"0","ppv":"211"},"16:35":{"totalHouseholdLoad":"32730.5","pac":"0","ppv":"182.5"},"10:50":{"totalHouseholdLoad":"115","pac":"0","ppv":"318"},"23:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"22:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"23:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:45":{"totalHouseholdLoad":"161","pac":"0","ppv":"148"},"22:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:40":{"totalHouseholdLoad":"132.5","pac":"0","ppv":"140.5"},"12:00":{"totalHouseholdLoad":"145.5","pac":"0","ppv":"246"},"12:05":{"totalHouseholdLoad":"259","pac":"0","ppv":"228"},"17:15":{"totalHouseholdLoad":"175","pac":"0","ppv":"88"},"11:35":{"totalHouseholdLoad":"239","pac":"0","ppv":"163"},"16:40":{"totalHouseholdLoad":"65473","pac":"0","ppv":"175"},"16:45":{"totalHouseholdLoad":"120","pac":"0","ppv":"176"},"11:30":{"totalHouseholdLoad":"149","pac":"0","ppv":"172"},"17:10":{"totalHouseholdLoad":"329.5","pac":"0","ppv":"100"},"21:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"22:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"00:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"00:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"22:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"06:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"21:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"10:30":{"totalHouseholdLoad":"204.5","pac":"0","ppv":"247"},"16:15":{"totalHouseholdLoad":"65396","pac":"0","ppv":"195.5"},"11:00":{"totalHouseholdLoad":"43","pac":"0","ppv":"331"},"10:35":{"totalHouseholdLoad":"164.5","pac":"0","ppv":"253"},"11:05":{"totalHouseholdLoad":"42","pac":"0","ppv":"369"},"15:40":{"totalHouseholdLoad":"1720","pac":"0","ppv":"226.5"},"15:45":{"totalHouseholdLoad":"499","pac":"0","ppv":"232.5"},"16:10":{"totalHouseholdLoad":"32637","pac":"0","ppv":"214.5"},"22:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"21:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"00:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"00:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"22:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"21:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"05:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"11:10":{"totalHouseholdLoad":"125","pac":"0","ppv":"265"},"16:25":{"totalHouseholdLoad":"65282.5","pac":"0","ppv":"193"},"10:45":{"totalHouseholdLoad":"234.5","pac":"0","ppv":"260"},"11:15":{"totalHouseholdLoad":"32409.5","pac":"0","ppv":"149.5"},"16:20":{"totalHouseholdLoad":"65278","pac":"0","ppv":"169"},"15:50":{"totalHouseholdLoad":"3540","pac":"0","ppv":"198"},"15:55":{"totalHouseholdLoad":"2181.5","pac":"0","ppv":"222"},"10:40":{"totalHouseholdLoad":"252","pac":"0","ppv":"248"},"20:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"10:05":{"totalHouseholdLoad":"95","pac":"0","ppv":"182.5"},"21:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:15":{"totalHouseholdLoad":"236","pac":"0","ppv":"59"},"20:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"08:45":{"totalHouseholdLoad":"197","pac":"0","ppv":"53.5"},"21:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:10":{"totalHouseholdLoad":"192","pac":"0","ppv":"71.5"},"08:40":{"totalHouseholdLoad":"196.5","pac":"0","ppv":"46"},"15:25":{"totalHouseholdLoad":"75","pac":"0","ppv":"273.5"},"10:10":{"totalHouseholdLoad":"113","pac":"0","ppv":"178"},"10:15":{"totalHouseholdLoad":"166.5","pac":"0","ppv":"201.5"},"14:50":{"totalHouseholdLoad":"400.5","pac":"0","ppv":"219"},"14:55":{"totalHouseholdLoad":"65420","pac":"0","ppv":"253"},"15:20":{"totalHouseholdLoad":"208","pac":"0","ppv":"267"},"22:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"02:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"22:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:05":{"totalHouseholdLoad":"164.5","pac":"0","ppv":"80"},"08:35":{"totalHouseholdLoad":"166","pac":"0","ppv":"45"},"21:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:00":{"totalHouseholdLoad":"242","pac":"0","ppv":"63"},"02:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"21:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"10:20":{"totalHouseholdLoad":"286.5","pac":"0","ppv":"229"},"08:30":{"totalHouseholdLoad":"373","pac":"0","ppv":"0"},"16:05":{"totalHouseholdLoad":"438","pac":"0","ppv":"230"},"15:35":{"totalHouseholdLoad":"172","pac":"0","ppv":"208"},"10:25":{"totalHouseholdLoad":"218","pac":"0","ppv":"243"},"15:30":{"totalHouseholdLoad":"167","pac":"0","ppv":"243"},"16:00":{"totalHouseholdLoad":"695.5","pac":"0","ppv":"222"},"19:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:25":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:20":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"20:35":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:35":{"totalHouseholdLoad":"127","pac":"0","ppv":"125"},"21:00":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"20:30":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"15:05":{"totalHouseholdLoad":"65402","pac":"0","ppv":"274"},"09:30":{"totalHouseholdLoad":"225","pac":"0","ppv":"112"},"14:35":{"totalHouseholdLoad":"169.5","pac":"0","ppv":"260"},"15:00":{"totalHouseholdLoad":"988.5","pac":"0","ppv":"260.5"},"19:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"14:30":{"totalHouseholdLoad":"161","pac":"0","ppv":"273"},"19:50":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"21:15":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"04:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"20:45":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:25":{"totalHouseholdLoad":"200","pac":"0","ppv":"97.5"},"08:55":{"totalHouseholdLoad":"213.5","pac":"0","ppv":"59"},"21:10":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"03:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"20:40":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"09:20":{"totalHouseholdLoad":"237.5","pac":"0","ppv":"69.5"},"15:15":{"totalHouseholdLoad":"32991","pac":"0","ppv":"266.5"},"10:00":{"totalHouseholdLoad":"153.5","pac":"0","ppv":"199"},"08:50":{"totalHouseholdLoad":"233","pac":"0","ppv":"58"},"14:45":{"totalHouseholdLoad":"609","pac":"0","ppv":"206.5"},"21:05":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"},"14:40":{"totalHouseholdLoad":"65492","pac":"0","ppv":"241"},"15:10":{"totalHouseholdLoad":"32802.5","pac":"0","ppv":"287"},"19:55":{"totalHouseholdLoad":"0","pac":"0","ppv":"0"}}}
      # => 200
      ```
      * seems to return previos day, so do request with date+1
      * daily data (other url and params!)
        ```
        response = self.session.request(
            "POST",
            url='https://openapi.growatt.com/v4/noahDeviceApi/nexa/getDataChart',
            params=None,
            data={
                'deviceSn': 'DEVICE_SN',
                'dateTime': '2025-10-01',
                'dateType': 1
            },
        )
        print(response.text)
        print(response.status_code)
        # => {"msg":"","result":1,"obj":{"22":"0","01":"0.2","23":"0","02":"0","24":"0","03":"0","25":"0","04":"0","26":"0","05":"0","27":"0","06":"0","28":"0","07":"0","29":"0","08":"0","09":"0","30":"0","31":"0","10":"0","11":"0","12":"0","13":"0","14":"0","15":"0","16":"0","17":"0","18":"0","19":"0","20":"0","21":"0"}}
        # => 200
        ```
      * monthly data: `'dateTime': '2025-10-01', 'dateType': 2`
      * yearly data: `'dateTime': '2025-10-01', 'dateType': 3`
    * ```
      response = self.session.request(
          "POST",
          url='https://openapi.growatt.com/v4/noahDeviceApi/nexa/checkUpgradeNexa',
          params=None,
          data={
              'deviceSn': 'DEVICE_SN',
          },
      )
      print(response.text)
      print(response.status_code)
      # => {"msg":"","result":1,"obj":{"checkUpgradeNoah":false,"currVersion":"11.10.09.07.9000.4017","newVersion":"11.10.09.07.9000.4017","status":"6"}}
      # => 200
      ```
    * for noah see
      * https://github.com/search?q=repo%3Amtrossbach%2Fnoah-mqtt%20noahDeviceApi&type=code
      * https://github.com/indykoning/PyPi_GrowattServer/blob/45e3fce44c32be16eec6cc049549a78b1e11233f/growattServer/base_api.py#L871
      *

# Changelog
* TBA
  * added `wifi_strength()` (new API) to inverter, noah, max, min, spa, sph, sph-s, wit
  * added `power()` (new API) to inverter, max, min, noah, spa, sph, wit
  * added `setting_write_assign_inverter()` (new API) to noah
  * added `setting_write_grid_charging()` (new API) to noah
  * added `setting_write_off_grid()` (new API) to noah
  * added `setting_write_vpp_param_new()` (new API) to min, spa, sph, wit
  * added `setting_clear_vpp_time_period()` (new API) to min, spa, sph, wit
  * added `status()` (APP API) to noah
* 2025.08.17 (alpha)
  * added NOAH/NEXA support (verified with real NEXA-2000 device)
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
