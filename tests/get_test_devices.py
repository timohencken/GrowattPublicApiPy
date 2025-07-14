"""
not a test
just enumerate available devices from test environment(s)

 device_type_v4 device_type_v1_txt device_type_txt       msg   obj_txt   device_sn                 server_url                     model     datalogger_sn  plant_id  device_type  obj  device_type_v1
            inv                NaN        Inverter  inverter  Inverter  NHB691514F  http://183.62.216.35:8081          Growatt 25000 UE        YYP0E3R00H       NaN           16    1             NaN
            max           Inverter             MAX  inverter  Inverter  SASF819012   https://test.growatt.com         Growatt 6000MTL-S        WLC082100F      23             18    1             1
            max                MAX             MAX  inverter  Inverter  SASF819012   https://test.growatt.com         Growatt 6000MTL-S        WLC082100F      23             18    1             4
            max                NaN             MAX     other     Other  QXHLD7F0C9  http://183.62.216.35:8081              MOD 10KTL3-X        BLE4BL40GS       NaN           18    4             NaN
            min                MIN             MIN     other     Other  GRT0010086   https://test.growatt.com                   default  VC51010223332257      29             22    4             7
            min                MIN             MIN     other     Other  RUK0CAE00J   https://test.growatt.com         MIN 10000TL-XH-US  VC50010621200118      29             22    4             7
            min                MIN             MIN     other     Other  TAG1234567   https://test.growatt.com         MIN 7600 TL-XH US  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1234001   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1235001   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1235002   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1235003   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1235004   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1235005   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1235006   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1235112   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  YYX1235112   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  YYX1235113   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1236601   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1236602   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1236603   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1236604   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  GRT1236605   https://test.growatt.com                   default  VC51010223062195      29             22    4             7
            min                MIN             MIN     other     Other  EVK0BHX111   https://test.growatt.com         MIN 11400TL-XH-US  VC51010223062195      29             22    4             7
            spa                NaN             SPA  inverter  Inverter  CHENYINSHU  http://183.62.216.35:8081             Growatt1000-S        BQC0733006       NaN           19    1             NaN
            sph                NaN             SPH   storage   Storage  AQM1234567  http://183.62.216.35:8081          SPH 5000TL BL-UP        XGD6E9K06M       NaN           17    2             NaN
          sph-s                NaN           SPH-S   storage   Storage  EFP0N1J023  http://183.62.216.35:8081                S10000H-48  VC41010123438079       NaN          260    2             NaN
        storage                NaN         Storage   storage   Storage  KHMOCM5688  http://183.62.216.35:8081  Growatt SPF 6000 ES PLUS        EAP0D9M006       NaN           96    2             NaN
            wit                NaN             WIT   storage   Storage  QWL0DC3002  http://183.62.216.35:8081            WIT 100K- HE L        XGD6E7C4S2       NaN          218    2             NaN
"""

import pandas as pd
from growatt_public_api.api_v4 import ApiV4
from growatt_public_api import GrowattApiSession, Device, Plant
from growatt_public_api.pydantic_models.api_v4 import DeviceListV4

# test environments
envs = [
    {
        "name": "test_v1",
        "gas": GrowattApiSession.using_test_server_v1(),
    },
    {
        "name": "test_v4",
        "gas": GrowattApiSession.using_test_server_v4(),
    },
]

device_overview = []
for env in envs:  # noqa C901 'Loop 25' is too complex (14)
    print(f"Checking env '{env.get('name')}'")
    # init API
    gas = env["gas"]
    # get devices
    api_device = Device(session=gas)
    apiv4 = ApiV4(session=gas)
    print("\rgetting device list")
    devices: DeviceListV4 = api_device.list()

    # get device type info
    print("\rgetting device type infos")
    device_type_infos = {}
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
        device_plant_info = api_device.get_plant(device_sn=device_sn)
        device_plant_infos[device_sn] = device_plant_info

    # we might have "hidden" devices only visible in v1 (e.g. MAX has two devices (type 1 & 4 with same sn)
    plant_devices = {}
    print("\rgetting plant devices")
    plant_ids = {x.data.plant.plant_id for x in device_plant_infos.values() if x.data}
    for idx, plant_id in enumerate(plant_ids):
        print(f"\r {idx + 1}/{len(plant_ids)}: {plant_id}      ", end="")
        plant_devices[plant_id] = api_plant.list_devices(plant_id=plant_id, limit=100)

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
        218: "WIT",
        260: "SPH-S",
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
