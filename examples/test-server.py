import pickle
from datetime import date, timedelta
from pathlib import Path
from typing import Optional, Dict, Any
from loguru import logger
from growatt_public_api import GrowattApi


logger.info("Example using Growatt API v1 TEST server")
SERVER_URL = "https://test.growatt.com"
# test token from official API docs https://www.showdoc.com.cn/262556420217021/1494053950115877
API_TOKEN = "6eb6f069523055a339d71e5b1f6c88cc"  # gitleaks:allow
PICKLE_DIR = Path.home() / "growatt-api-pickle"

"""
Note:
v4 API can also be tested using v1 test server & token,
but v1 server returns only max and min devices.

v1 API cannot be tested on v4 server, as it returns no plants.
"""

PICKLE_DIR.mkdir(parents=True, exist_ok=True)
ga = GrowattApi(token=API_TOKEN, server_url=SERVER_URL)
logger.debug("API initialized")

# get list of plants associated to the test account
# pickle results for later use
plants_file = PICKLE_DIR / "all_plants.pickle"
if plants_file.exists():
    logger.debug(f"using plants from pickle {plants_file}")
    with plants_file.open("rb") as f:
        all_plants = pickle.load(f)
else:
    all_plants = []
    chunksize = 20
    plant_total_count: Optional[int] = None

    while plant_total_count is None or len(all_plants) < plant_total_count:
        page = len(all_plants) // chunksize + 1
        logger.debug(f"loading plant list page {page}")
        plant_list = ga.plant.list(page=page, limit=chunksize)
        plant_total_count = plant_list.data.count  # plant count known after first request
        # remember all plants
        all_plants.extend(plant_list.data.plants)
    with plants_file.open("wb") as f:
        # noinspection PyTypeChecker
        pickle.dump(all_plants, f)
    logger.debug(f"using {len(all_plants)} plants")

# get devices for each plant
plant_devices_file = PICKLE_DIR / "all_plant_devices.pickle"
if plant_devices_file.exists():
    logger.debug(f"using devices from pickle {plant_devices_file}")
    with plant_devices_file.open("rb") as f:
        plant_devices = pickle.load(f)
else:
    plant_devices: Dict[int, Any] = {}
    for idx, plant in enumerate(all_plants):
        page = 1
        logger.debug(f"loading devices for plant {plant.plant_id} ({idx+1}/{len(all_plants)})")
        while True:
            device_list = ga.device.list(
                plant_id=plant.plant_id,
                page=page,  # first page
                limit=100,  # max limit
            )
            plant_devices[plant.plant_id] = plant_devices.get(plant.plant_id, []) + device_list.data.devices
            if len(plant_devices[plant.plant_id]) >= device_list.data.count:
                break  # all devices retrieved
            else:
                page += 1
    with plant_devices_file.open("wb") as f:
        # noinspection PyTypeChecker
        pickle.dump(plant_devices, f)

plants_with_devices = {k: v for k, v in plant_devices.items() if v}
logger.debug(f"using {len(plants_with_devices)} plants with devices")

# get details for each device
device_details_file = PICKLE_DIR / "all_device_details.pickle"
if device_details_file.exists():
    logger.debug(f"using device details from pickle {device_details_file}")
    with device_details_file.open("rb") as f:
        device_details = pickle.load(f)
else:
    device_details = []
    datalogger_details_cache = {}  # same datalogger may be used by multiple devices
    device_details_cache = {}  # MAX reports as two device. One of type 1 (inverter) and one of type 4 (max)
    for plant_id, devices in plants_with_devices.items():
        for idx, device in enumerate(devices):
            logger.debug(f"loading details for device {device.device_id} of plant {plant_id}")
            if device.device_sn:
                if device.device_sn not in device_details_cache:
                    device_details_cache[device.device_sn] = ga.device.type_info(device_sn=device.device_sn)
                inverter_details = device_details_cache.get(device.device_sn)
            else:
                inverter_details = {}
            if device.datalogger_sn:
                if device.datalogger_sn not in datalogger_details_cache:
                    datalogger_details_cache[device.datalogger_sn] = ga.device.type_info(device_sn=device.datalogger_sn)
                datalogger_details = datalogger_details_cache.get(device.datalogger_sn)
            else:
                datalogger_details = {}
            device_details.append(
                {
                    "plant_id": plant_id,
                    "device_sn": device.device_sn,
                    "datalogger_sn": device.datalogger_sn,
                    "device_details": inverter_details,
                    "device_type": device.type,
                    "datalogger_details": datalogger_details,
                }
            )
    with device_details_file.open("wb") as f:
        # noinspection PyTypeChecker
        pickle.dump(device_details, f)
logger.debug(f"using {len(device_details)} devices")

# Now you could
# e.g. try to find a device supporting VPP commands

for device in device_details:
    vpp_result = ga.vpp.soc(device_sn=device["device_sn"])
    logger.debug(f'sn: {device["device_sn"]}, type={device["device_type"]}, {vpp_result}')
    if vpp_result.error_code == 0:
        logger.info(f"Device {device['device_sn']} supports VPP commands")
        break

# Now you could
# e.g. filter for a specific type to try its endpoints
inverter = next((d for d in device_details if d["device_type"] == 1), None)
if inverter:
    inverter_sn = inverter["device_sn"]
    logger.debug(f"Found inverter {inverter_sn} for plant {inverter['plant_id']}")

    logger.debug(f"alarms:\n{ga.inverter.alarms(device_sn=inverter_sn).model_dump()}")
    logger.debug(f"details:\n{ga.inverter.details(device_sn=inverter_sn).model_dump()}")
    logger.debug(f"energy:\n{ga.inverter.energy(device_sn=inverter_sn).model_dump()}")
    logger.debug(f"energy_history:\n{ga.inverter.energy_history(device_sn=inverter_sn).model_dump()}")
    logger.debug(f"energy_multiple:\n{ga.inverter.energy_multiple(device_sn=inverter_sn).model_dump()}")

# try a MAX device
max_device = next((d for d in device_details if d["device_type"] == 4), None)
if inverter:
    max_sn = max_device["device_sn"]

    logger.debug(f"Found 'MAX' device {max_sn} for plant {max_device['plant_id']}")

    logger.debug(f"alarms:\n{ga.max.alarms(device_sn=max_sn).model_dump()}")
    logger.debug(f"details:\n{ga.max.details(device_sn=max_sn).model_dump()}")
    max_energy = ga.max.energy(device_sn=max_sn)
    logger.debug(f"energy:\n{max_energy.model_dump()}")
    try:
        last_data_ts = max_energy.data.time.date()
    except AttributeError:
        last_data_ts = date(2024, 12, 20)
    max_history = ga.max.energy_history(
        device_sn=max_sn,
        # ensure we see some data (will probably have no data for "today"
        start_date=last_data_ts - timedelta(days=1),
        end_date=last_data_ts + timedelta(days=1),
    )
    logger.debug(f"energy_history:\n{max_history.model_dump()}")
    logger.debug(f"energy_multiple:\n{ga.max.energy_multiple(device_sn=max_sn).model_dump()}")
    logger.debug(
        f"settings read 'max_cmd_on_off':\n{ga.max.setting_read(device_sn=max_sn, parameter_id='max_cmd_on_off').model_dump()}"
    )

logger.success("DONE")
