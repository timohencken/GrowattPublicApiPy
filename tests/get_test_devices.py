"""
not a test
just enumerate available devices from test environment(s)
"""

import pandas as pd
from api_v4 import ApiV4
from growatt_public_api import GrowattApiSession, Device, Plant
from pydantic_models.api_v4 import DeviceListV4

# test environments
envs = [
    {
        "name": "test_v1",
        "server_url": "https://test.growatt.com",
        "token": "6eb6f069523055a339d71e5b1f6c88cc",  # gitleaks:allow
    },
    {
        "name": "test_v4",
        "server_url": "http://183.62.216.35:8081",
        "token": "wa265d2h1og0873ml07142r81564hho6",  # gitleaks:allow
    },
]

device_overview = []
for env in envs:  # noqa C901 'Loop 25' is too complex (14)
    print(f"Checking env '{env.get('name')}'")
    # init API
    gas = GrowattApiSession(
        server_url=env.get("server_url"),
        token=env.get("token"),
    )
    # get devices
    apiv4 = ApiV4(session=gas)
    print("\rgetting device list")
    devices: DeviceListV4 = apiv4.list()

    # get device type info
    print("\rgetting device type infos")
    device_type_infos = {}
    api_device = Device(session=gas)
    for idx, device in enumerate(devices.data.data):
        print(f"\r {idx+1}/{len(devices.data.data)}: {device.device_sn}      ", end="")
        device_sn: str = device.device_sn
        device_type_info = api_device.type_info(device_sn=device_sn)
        device_type_infos[device_sn] = device_type_info

    # get plant info
    print("\rgetting device plant infos")
    device_plant_infos = {}
    api_plant = Plant(session=gas)
    for idx, device in enumerate(devices.data.data):
        print(f"\r {idx + 1}/{len(devices.data.data)}: {device.device_sn}      ", end="")
        device_sn: str = device.device_sn
        device_plant_info = api_plant.by_device(device_sn=device_sn)
        device_plant_infos[device_sn] = device_plant_info

    # we might have "hidden" devices only visible in v1 (e.g. MAX has two devices (type 1 & 4 with same sn)
    plant_devices = {}
    print("\rgetting plant devices")
    plant_ids = {x.data.plant.plant_id for x in device_plant_infos.values() if x.data}
    for idx, plant_id in enumerate(plant_ids):
        print(f"\r {idx + 1}/{len(plant_ids)}: {plant_id}      ", end="")
        plant_devices[plant_id] = api_device.list(plant_id=plant_id)

    # #################################################################################################################
    # collect and merge data
    print("\rmerging data")

    # from get devices
    for device in devices.data.data:
        device_overview.append(
            {
                "server_url": env.get("server_url"),
                "datalogger_sn": device.datalogger_sn,
                "device_sn": device.device_sn,
                "device_type_v4": device.device_type,
            }
        )

    # from get device type info
    map_obj = {
        1: "Inverter",
        2: "Storage",
        3: "Collector",
        4: "Other",
    }
    map_device_type = {
        16: "Inverter",
        17: "SPH",
        18: "MAX",
        19: "SPA",
        22: "MIN",
        81: "PCS",
        82: "HPS",
        83: "PDB",
        96: "Storage",
    }
    for device_sn, device_type_info in device_type_infos.items():
        if device_sn not in [x["device_sn"] for x in device_overview]:
            device_overview.append(
                {
                    "device_sn": device_sn,
                }
            )
        device_to_update = [x for x in device_overview if x["device_sn"] == device_sn][0]
        device_to_update["device_type"] = device_type_info.device_type
        device_to_update["model"] = device_type_info.model
        device_to_update["obj"] = device_type_info.obj
        device_to_update["msg"] = device_type_info.msg
        # add mapping
        device_to_update["device_type_txt"] = map_device_type.get(device_type_info.device_type)
        device_to_update["obj_txt"] = map_obj.get(device_type_info.obj)

    # from get plant info
    for device_sn, device_plant_info in device_plant_infos.items():
        if not device_plant_info.data:
            continue
        device_to_update = [x for x in device_overview if x["device_sn"] == device_sn][0]
        device_to_update["plant_id"] = device_plant_info.data.plant.plant_id

    # from we might have "hidden" devices only visible in v1 (e.g. MAX has two devices (type 1 & 4 with same sn)
    device_type_map = {
        1: "Inverter",
        2: "Storage",
        3: "Other",
        4: "MAX",
        5: "sph",
        6: "SPA",
        7: "MIN",
        8: "PCS",
        9: "HPS",
        10: "PBD",
        11: "groboost",
    }
    device_cnt = {}
    for plant_id, plant_device_list in plant_devices.items():
        for device in plant_device_list.data.devices:
            device_sn: str = device.device_sn
            device_type_v1: int = device.type
            # print(device_type_v1, device_sn)
            device_to_update = [x for x in device_overview if x["device_sn"] == device_sn][0]
            device_cnt[device_sn] = device_cnt.get(device_sn, 0) + 1
            if device_cnt[device_sn] > 1:
                # print(f"device {device_sn} has duplicates")
                append_ = True
                device_to_update = device_to_update.copy()
            else:
                append_ = False

            device_to_update["device_type_v1"] = device_type_v1
            device_to_update["device_type_v1_txt"] = device_type_map.get(device_type_v1)

            if append_:
                device_overview.append(device_to_update)


df = pd.DataFrame(device_overview)
df = df[
    [
        "device_type_v4",
        "device_type_v1_txt",
        "device_type_txt",
        "msg",
        "obj_txt",
        "device_sn",
        "server_url",
        "model",
        "datalogger_sn",
        "plant_id",
        "device_type",
        "obj",
        "device_type_v1",
    ]
]
df = df.sort_values(by=["device_type_v4", "device_type_v1"])
print(df.to_string())

print("\rDONE")
