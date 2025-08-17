import os
from loguru import logger
from growatt_public_api import GrowattApi
import pandas as pd

"""
Example script to retrieve data from a NOAH/NEXA device (e.g. Growatt NEXA 2000)

Edit this code or set you own API key as environment variable "GROWATTAPITOKEN" to use your device.
"""


# init API
SERVER_URL = None  # default
API_TOKEN = os.environ.get("GROWATTAPITOKEN")
if API_TOKEN:
    api = GrowattApi(server_url=SERVER_URL, token=API_TOKEN)
else:
    # Unfortunately, there is no NOAH available on the test server
    raise RuntimeError(
        "No API token found. Please set environment variable 'GROWATTAPITOKEN' with your Growatt API token."
    )

logger.info(f"Retrieving devices...")
devices = api.device.list()
device_types = {}
for device in devices.data.data:
    # get device type
    device_types[device.device_sn] = api.device.get_device_type(device_sn=device.device_sn)
    logger.info(f"* device type: {device_types[device.device_sn].name}, device sn: {device.device_sn}")
# select first NOAH device
device = [d for d in devices.data.data if d.device_type == "noah"][0]

# get device details
logger.info(f"Retrieving details of '{device_types[device.device_sn].name}' device '{device.device_sn}'...")
my_device_api = api.api_for_device(device_sn=device.device_sn)
device_details = my_device_api.details_v4().data.devices[0]
logger.info(
    f"* alias: {device_details.alias}, firmware version: {device_details.fw_version}, model: {device_details.model or device_details.model_name}, default power: {device_details.default_power}W, updated: {device_details.last_update_time_text}"
)

logger.info(f"Retrieving latest energy of '{device_types[device.device_sn].name}' device '{device.device_sn}'...")
energy = my_device_api.energy_v4().data.devices[0]
logger.info(f"* Timestamp:   {energy.time_str}, Status: {energy.status}, work mode: {energy.work_mode}")
logger.info(f"* Heating:     {energy.heating_status}")
logger.info(f"* System-Temp: {energy.system_temp} °C")
logger.info(
    f"* Bat-Tempera: {', '.join([f'{energy.battery1_temp:2.0f} °C', f'{energy.battery2_temp:2.0f} °C', f'{energy.battery3_temp:2.0f} °C', f'{energy.battery4_temp:2.0f} °C'][:energy.battery_package_quantity])}"
)
logger.info(
    f"* PV-Temperat: {', '.join([f'{energy.pv1_temp:2.0f} °C', f'{energy.pv2_temp:2.0f} °C', f'{energy.pv3_temp:2.0f} °C', f'{energy.pv4_temp:2.0f} °C'])}"
)
_out_mode = {0: "On-Grid", 1: "Off-Grid", 2: "Hybrid"}[energy.on_off_grid]
logger.info(f"* Output mode: {_out_mode} ({energy.on_off_grid})")
logger.info(
    f"* SoC:         {energy.total_battery_pack_soc:5.0f} % ({', '.join([f'{energy.battery1_soc:5.0f} %', f'{energy.battery2_soc:5.0f} %', f'{energy.battery3_soc:5.0f} %', f'{energy.battery4_soc:5.0f} %'][:energy.battery_package_quantity])})"
)
ppv1 = energy.pv1_current * energy.pv1_voltage
ppv2 = energy.pv2_current * energy.pv2_voltage
ppv3 = energy.pv3_current * energy.pv3_voltage
ppv4 = energy.pv4_current * energy.pv4_voltage
logger.info(f"* PV power:    {energy.ppv:5.1f} W ({ppv1:5.1f} W, {ppv2:5.1f} W, {ppv3:5.1f} W, {ppv4:5.1f} W)")
logger.info(
    f"* PV voltage:  {energy.pv1_voltage:5.1f} V / {energy.pv2_voltage:4.1f} V / {energy.pv3_voltage:4.1f} V / {energy.pv4_voltage:4.1f} V"
)
logger.info(
    f"* PV current:  {energy.pv1_current:5.1f} A / {energy.pv2_current:4.1f} A / {energy.pv3_current:4.1f} A / {energy.pv4_current:4.1f} A"
)
logger.info(
    f"* PV current:  {energy.pv1_current:5.1f} A / {energy.pv2_current:4.1f} A / {energy.pv3_current:4.1f} A / {energy.pv4_current:4.1f} A"
)
logger.info(
    f"* Bat charge:  {energy.total_battery_pack_charging_power:5.1f} W, Status: {energy.total_battery_pack_charging_status}"
)
logger.info(f"* pAC:         {energy.pac:5.1f} W, (BUCK power)")
logger.info(f"* House load:  {energy.total_household_load:5.1f} W, (Total household load)")
logger.info(f"* w/o GroPlug: {energy.household_load_apart_from_groplug:5.1f} W, (Household load apart from GroPlug)")
logger.info(f"* Grid power:  {energy.on_grid_power:5.1f} W On-Grid, {energy.off_grid_power:5.1f} W Off-Grid")
logger.info(f"* CT power:    {energy.ct_self_power:5.1f} W (CT self power)")

logger.info(
    f"Retrieving latest energy history of '{device_types[device.device_sn].name}' device '{device.device_sn}'..."
)
power = my_device_api.energy_history_v4(date_=energy.time_str.date())
df = pd.DataFrame([x.model_dump() for x in power.data.datas])
df = df.set_index("time_str").sort_index().copy()
df["ppv1"] = df["pv1_current"] * df["pv1_voltage"]
df["ppv2"] = df["pv2_current"] * df["pv2_voltage"]
df["ppv3"] = df["pv3_current"] * df["pv3_voltage"]
df["ppv4"] = df["pv4_current"] * df["pv4_voltage"]
df = df[
    [
        "total_battery_pack_soc",  # SoC
        "on_grid_power",  # \__> output
        "off_grid_power",  # /
        "ct_self_power",  # ???
        "household_load_apart_from_groplug",  # ???
        "total_battery_pack_charging_power",  # load/unload battery power
        "total_household_load",
        "pac",
        "ppv",  # PV power
        "ppv1",
        "ppv2",
        "ppv3",
        "ppv4",  # PV power per string
    ]
]
logger.info(f"   Time |  SoC  |  Output   | Bat charge | PV power  | PV1 % | PV2 % | PV3 % | PV4 % ")
logger.info(f"--------+-------+-----------+------------+-----------+-------+-------+-------+-------")
for idx, row in df.iterrows():
    # logger.info(f"* 00:00 | 100 % | 10321.8 W |  -2000.0 W |  2000.0 W | 100 % | 100 % | 100 % | 100 %")
    logger.info(
        f"* {idx.strftime('%H:%M')} | {row['total_battery_pack_soc']:3.0f} % | {(row['on_grid_power'] + row['off_grid_power']):7.1f} W |  {row['total_battery_pack_charging_power']:7.1f} W |  {row['ppv']:6.1f} W | {((row['ppv1'] / row['ppv'] * 100) if row['ppv'] > 0 else 0.0):3.0f} % | {((row['ppv2'] / row['ppv'] * 100) if row['ppv'] > 0 else 0.0):3.0f} % | {((row['ppv3'] / row['ppv'] * 100) if row['ppv'] > 0 else 0.0):3.0f} % | {((row['ppv4'] / row['ppv'] * 100) if row['ppv'] > 0 else 0.0):3.0f} %"
    )

logger.success(f"DONE")
