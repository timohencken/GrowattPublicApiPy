import os
from datetime import date
from loguru import logger
from growatt_public_api import GrowattApi


"""
Example script to retrieve data from a MIN device (e.g. Growatt NEO)

Edit this code or set you own API key as environment variable "GROWATTAPITOKEN" to use your device.
If nothing is set, test server will be used instead.
"""


# init API
SERVER_URL = None  # default
API_TOKEN = os.environ.get("GROWATTAPITOKEN")
if API_TOKEN:
    api = GrowattApi(server_url=SERVER_URL, token=API_TOKEN)
else:
    api = GrowattApi.using_test_server_v1()

# show user information
logger.info("Retrieving user information...")
users = api.user.list()
for user in users.data.users:
    logger.info(f"* user id: {user.id}, name: {user.name}, email: {user.email}, phone: {user.phone_number}")
# select first user
user = users.data.users[0]

# show plant information
# logger.info("Retrieving plants...")
# plants = api.plant.list()
logger.info(f"Retrieving plants for user '{user.name}'...")
plants = api.plant.list_by_user(username=user.name)
for plant in plants.data.plants:
    logger.info(
        f"* plant id: {plant.plant_id}, user id: {plant.user_id}, name: {plant.name}, kW peak: {plant.peak_power}, location: {plant.city} {plant.country} {plant.latitude}°/{plant.longitude}°"
    )
# select first plant
plant = plants.data.plants[0]

logger.info(f"Retrieving energy for plant '{plant.name}'...")
energy = api.plant.energy_overview(plant_id=plant.plant_id).data
logger.info(
    f"* current: {energy.current_power} kW, today: {energy.today_energy} kWh, month: {energy.monthly_energy} kWh, year: {energy.yearly_energy} kWh, total: {energy.total_energy} kWh"
)

logger.info(f"Retrieving today's energy history for plant '{plant.name}'...")
power = api.plant.power(plant_id=plant.plant_id)
for ts, watt in sorted([(x.time, x.power) for x in power.data.powers if x.power is not None]):
    logger.info(f"* {ts.isoformat(sep=' ', timespec='minutes')}: {watt:6.1f} W")

# get plant devices
# logger.info(f"Retrieving devices...")
# devices = api.device.list()
logger.info(f"Retrieving devices of plant '{plant.name}'...")
devices = api.plant.list_devices(plant_id=plant.plant_id)
device_types = {}
for device in devices.data.devices:
    # get device type
    device_types[device.device_sn] = api.device.get_device_type(device_sn=device.device_sn)
    logger.info(
        f"* device type: {device_types[device.device_sn].name}, device sn: {device.device_sn}, last update: {device.last_update_time}, online: {not(device.lost)}"
    )
# select first device (this example assumes it is 'MIN'
device = devices.data.devices[0]

# skipped assert as we use api_for_device() to get device-independent API instance
# from growatt_public_api import GrowattApi, DeviceType
# assert device_types[device.device_sn] == DeviceType.MIN

# get device details
logger.info(f"Retrieving details of '{device_types[device.device_sn].name}' device '{device.device_sn}'...")
# device_details = api.min.details(device_sn=device.device_sn).data
my_device_api = api.api_for_device(device_sn=device.device_sn)
device_details = my_device_api.details().data
logger.info(
    f"* alias: {device_details.alias}, firmware version: {device_details.fw_version} {device_details.inner_version}, model: {device_details.model_text}, W peak: {device_details.pmax}"
)

logger.info(f"Retrieving energy of '{device_types[device.device_sn].name}' device '{device.device_sn}'...")
# energy = api.min.energy_v4(device_sn=device.device_sn).data.devices[0]
energy = my_device_api.energy_v4().data.devices[0]
logger.info(f"* Timestamp:   {energy.time}, Status: {energy.status_text}")
logger.info(f"* AC power:    {energy.pac:5.1f} W ({energy.pac1:5.1f} + {energy.pac2:5.1f} + {energy.pac3:5.1f})")
logger.info(f"* AC voltage:  {energy.vac1:5.1f} V / {energy.vac2:5.1f} V / {energy.vac3:5.1f} V")
logger.info(f"* AC current:  {energy.iac1:5.1f} A / {energy.iac2:5.1f} A / {energy.iac3:5.1f} A")
logger.info(
    f"* PV power:    {energy.ppv:5.1f} W ({energy.ppv1:5.1f} + {energy.ppv2:5.1f} + {energy.ppv3:5.1f} + {energy.ppv4:5.1f})"
)
logger.info(f"* PV voltage:  {energy.vpv1:5.1f} V / {energy.vpv2:5.1f} V / {energy.vpv3:5.1f} V / {energy.vpv4:5.1f} V")
logger.info(f"* PV current:  {energy.vpv1:5.1f} A / {energy.vpv2:5.1f} A / {energy.vpv3:5.1f} A / {energy.vpv4:5.1f} A")
logger.info(
    f"* Temperature: {energy.temp1:4.1f} °C / {energy.temp2:4.1f} °C / {energy.temp3:4.1f} °C / {energy.temp4:4.1f} °C / {energy.temp5:4.1f} °C"
)

logger.info(
    f"Retrieving today's energy history of '{device_types[device.device_sn].name}' device '{device.device_sn}'..."
)
# power = api.min.energy_history(device_sn=device.device_sn, limit=100)  # ! this endpoint uses paging - in real life, multiple requests are required to retrieve full day
power = my_device_api.energy_history_v4(date_=date.today())
for ts, pac, ppv, ppv1, ppv2, ppv3, ppv4 in sorted(
    [(x.time, x.pac, x.ppv, x.ppv1, x.ppv2, x.ppv3, x.ppv4) for x in power.data.datas]
):
    if ppv > 0:
        ppv1 = ppv1 / ppv * 100
        ppv2 = ppv2 / ppv * 100
        ppv3 = ppv3 / ppv * 100
        ppv4 = ppv4 / ppv * 100
    else:
        ppv1 = ppv2 = ppv3 = ppv4 = 0
    logger.info(
        f"* {ts.isoformat(sep=' ', timespec='minutes')}: {pac:6.1f} W (AC), {ppv:5.1f} W (PV) - PV1 {ppv1:2.0f}%, PV2 {ppv2:2.0f}%, PV3 {ppv3:2.0f}%, PV4 {ppv4:2.0f}%"
    )

if hasattr(my_device_api, "settings"):
    logger.info(
        f"Retrieving configured settings of '{device_types[device.device_sn].name}' device '{device.device_sn}'..."
    )
    # settings = api.min.settings(device_sn=device.device_sn).data
    settings = my_device_api.settings().data
    logger.info(
        f"* On/Off: {'On' if settings.on_off else 'Off'}, Limits: {settings.active_rate:5.1f}% = {(settings.active_rate/100 * device_details.pmax):5.1f} W / {settings.voltage_low_limit:0.1f}~{settings.voltage_high_limit:0.1f} V / {settings.frequency_low_limit:0.1f}~{settings.frequency_high_limit:0.1f} Hz"
    )
else:
    logger.warning(f"method 'settings()' not available for '{device_types[device.device_sn].name}' device")

logger.success(f"DONE")
