import pickle
from pathlib import Path
from loguru import logger
from growatt_public_api import GrowattApi


logger.info("Example using Growatt API v4 TEST server")
# test server from https://www.showdoc.com.cn/2540838290984246/11292913165257193
SERVER_URL = "http://183.62.216.35:8081"
# test token from official API docs https://www.showdoc.com.cn/2540838290984246/11292912972201443
API_TOKEN = "wa265d2h1og0873ml07142r81564hho6"  # gitleaks:allow

PICKLE_DIR = Path.home() / "growatt-api-pickle-v4"

"""
Note:
v4 API can also be tested using v1 test server & token,
but v1 server returns only max and min devices.

v1 API cannot be tested on v4 server, as it returns no plants.
"""

PICKLE_DIR.mkdir(parents=True, exist_ok=True)
ga = GrowattApi(token=API_TOKEN, server_url=SERVER_URL)
logger.debug("API initialized")

# get devices
devices_file = PICKLE_DIR / "devices.pickle"
if devices_file.exists():
    logger.debug(f"using devices from pickle {devices_file}")
    with devices_file.open("rb") as f:
        devices_ = pickle.load(f)
else:
    logger.debug(f"loading devices")
    devices_ = ga.v4.list()
    # {   'data': {   'count': 7,
    #                 'data': [   {'create_date': datetime.datetime(2024, 2, 5, 16, 1, 38), 'datalogger_sn': 'YYP0E3R00H', 'device_sn': 'NHB691514F', 'device_type': 'inv'},
    #                             {'create_date': datetime.datetime(2024, 2, 26, 15, 30, 59), 'datalogger_sn': 'EAP0D9M006', 'device_sn': 'KHMOCM5688', 'device_type': 'storage'},
    #                             {'create_date': datetime.datetime(2024, 1, 12, 17, 23, 47), 'datalogger_sn': 'BLE4BL40GS', 'device_sn': 'QXHLD7F0C9', 'device_type': 'max'},
    #                             {'create_date': datetime.datetime(2019, 1, 28, 15, 46, 31), 'datalogger_sn': 'BQC0733006', 'device_sn': 'CHENYINSHU', 'device_type': 'spa'},
    #                             {'create_date': datetime.datetime(2024, 4, 8, 16, 36, 41), 'datalogger_sn': 'VC41010123438079', 'device_sn': 'EFP0N1J023', 'device_type': 'sph-s'},
    #                             {'create_date': datetime.datetime(2023, 9, 15, 16, 28, 47), 'datalogger_sn': 'XGD6E7C4S2', 'device_sn': 'QWL0DC3002', 'device_type': 'wit'},
    #                             {'create_date': datetime.datetime(2024, 4, 24, 20, 33, 4), 'datalogger_sn': 'XGD6E9K06M', 'device_sn': 'AQM1234567', 'device_type': 'sph'}],
    #                 'last_pager': True,
    #                 'not_pager': False,
    #                 'other': None,
    #                 'page_size': 100,
    #                 'pages': 1,
    #                 'start_count': 0},
    #     'error_code': 0,
    #     'error_msg': 'SUCCESSFUL_OPERATION'}
    with devices_file.open("wb") as f:
        # noinspection PyTypeChecker
        pickle.dump(devices_, f)
devices = devices_.data.data
logger.debug(f"using {len(devices)} devices")

device_sn_inv = [d for d in devices if d.device_type == "inv"][0].device_sn
device_sn_storage = [d for d in devices if d.device_type == "storage"][0].device_sn
device_sn_max = [d for d in devices if d.device_type == "max"][0].device_sn
device_sn_sph = [d for d in devices if d.device_type == "sph"][0].device_sn
device_sn_spa = [d for d in devices if d.device_type == "spa"][0].device_sn
# no "min" :(
device_sn_wit = [d for d in devices if d.device_type == "wit"][0].device_sn
device_sn_sphs = [d for d in devices if d.device_type == "sph-s"][0].device_sn
# no "noah" :(

# _v4_details_inv_ = ga.v4.details(device_sn=device_sn_inv, device_type="inv")
# _v4_details_sto_ = ga.v4.details(device_sn=device_sn_storage, device_type="storage")
# _v4_details_sph_ = ga.v4.details(device_sn=device_sn_sph, device_type="sph")
# _v4_details_max_ = ga.v4.details(device_sn=device_sn_max, device_type="max")
# _v4_details_spa_ = ga.v4.details(device_sn=device_sn_spa, device_type="spa")
# _v4_details_min_ = ga.v4.details(device_sn=None, device_type="min")
# _v4_details_wit_ = ga.v4.details(device_sn=device_sn_wit, device_type="wit")
# _v4_details_sphs_ = ga.v4.details(device_sn=device_sn_sphs, device_type="sph-s")
# _v4_details_noah_ = ga.v4.details(device_sn=None, device_type="noah")

# _v4_energy_inv_ = ga.v4.energy(device_sn=device_sn_inv, device_type="inv")
# _v4_energy_sto_ = ga.v4.energy(device_sn=device_sn_storage, device_type="storage")
# _v4_energy_max_ = ga.v4.energy(device_sn=device_sn_max, device_type="max")
# _v4_energy_sph_ = ga.v4.energy(device_sn=device_sn_sph, device_type="sph")
# _v4_energy_spa_ = ga.v4.energy(device_sn=device_sn_spa, device_type="spa")
# _v4_energy_min_ = ga.v4.energy(device_sn="AFE494403F", device_type="min")
# _v4_energy_wit_ = ga.v4.energy(device_sn=device_sn_wit, device_type="wit")
# _v4_energy_sphs_ = ga.v4.energy(device_sn=device_sn_sphs, device_type="sph-s")
# _v4_energy_noah_ = ga.v4.energy(device_sn='EFP0N1J023', device_type="noah")

# _last_date = date(2024, 11, 13)  # _v4_details_inv_.data.inv[0].last_update_time_text.date()
# _v4_energy_hist_inv_ = ga.v4.energy_history(device_sn=device_sn_inv, device_type="inv", date_=_last_date)
# _v4_energy_hist2_inv_ = ga.v4.energy_history_multiple(device_sn=device_sn_inv, device_type="inv", date_=_last_date)
# _last_date = date(2024, 6, 17)  # _v4_details_sto_.data.storage[0].last_update_time_text.date()
# _v4_energy_hist_sto_ = ga.v4.energy_history(device_sn=device_sn_storage, device_type="storage", date_=_last_date)
# _v4_energy_hist2_sto_ = ga.v4.energy_history_multiple(device_sn=device_sn_storage, device_type="storage", date_=_last_date)
# _last_date = date(2025, 1, 9)  # _v4_details_sph_.data.sph[0].last_update_time_text.date()
# _v4_energy_hist_sph_ = ga.v4.energy_history(device_sn=device_sn_sph, device_type="sph", date_=_last_date)
# _v4_energy_hist2_sph_ = ga.v4.energy_history_multiple(device_sn=device_sn_sph, device_type="sph", date_=_last_date)
# _last_date = date(2024, 4, 26)  # _v4_details_max_.data.max[0].last_update_time_text.date()
# _v4_energy_hist_max_ = ga.v4.energy_history(device_sn=device_sn_max, device_type="max", date_=_last_date)
# _v4_energy_hist2_max_ = ga.v4.energy_history_multiple(device_sn=device_sn_max, device_type="max", date_=_last_date)
# _last_date = date(2019, 5, 21)  # _v4_details_spa_.data.spa[0].last_update_time_text.date()
# _v4_energy_hist_spa_ = ga.v4.energy_history(device_sn=device_sn_spa, device_type="spa", date_=_last_date)
# _v4_energy_hist2_spa_ = ga.v4.energy_history_multiple(device_sn=device_sn_spa, device_type="spa", date_=_last_date)
# _v4_energy_hist_min_ = ga.v4.energy_history(device_sn=None, device_type="min")
# _v4_energy_hist2_min_ = ga.v4.energy_history_multiple(device_sn=None, device_type="min")
# _last_date = date(2024, 10, 6)  # _v4_details_wit_.data.wit[0].last_update_time_text.date()
# _v4_energy_hist_wit_ = ga.v4.energy_history(device_sn=device_sn_wit, device_type="wit", date_=_last_date)
# _v4_energy_hist2_wit_ = ga.v4.energy_history_multiple(device_sn=device_sn_wit, device_type="wit", date_=_last_date)
# _last_date = date(2024, 7, 13)  # _v4_details_sphs_.data.sphs[0].last_update_time_text.date()
# _v4_energy_hist_sphs_ = ga.v4.energy_history(device_sn=device_sn_sphs, device_type="sph-s", date_=_last_date)
# _v4_energy_hist2_sphs_ = ga.v4.energy_history_multiple(device_sn=device_sn_sphs, device_type="sph-s", date_=_last_date)
# _v4_energy_hist_noah_ = ga.v4.energy_history(device_sn=None, device_type="noah")
# _v4_energy_hist2_noah_ = ga.v4.energy_history_multiple(device_sn=None, device_type="noah")

# _v4_set_power_on_ = ga.v4.setting_write_on_off(device_sn=device_sn_inv, device_type="inv", power_on=True)
# _v4_set_active_power_ = ga.v4.setting_write_active_power(device_sn=device_sn_inv, device_type="inv", active_power=100)
# _v4_set_soc_upper_ = ga.v4.setting_write_soc_upper_limit(device_sn=device_sn_inv, device_type="noah", soc_limit=100)
# _v4_set_soc_lower_ = ga.v4.setting_write_soc_lower_limit(device_sn=device_sn_inv, device_type="noah", soc_limit=0)
# _v4_set_period_ = ga.v4.setting_write_time_period(
#     device_sn=device_sn_inv,
#     device_type="noah",
#     time_period_nr=1,
#     start_time=time(9, 0),
#     end_time=time(12, 0),
#     load_priority=True,
#     power_watt=800,
#     enabled=False,
# )

_vpp_setting_ = ga.v4.setting_read_vpp_param(
    device_sn=device_sn_storage, device_type="noah", parameter_id="set_param_2"
)

logger.success("DONE")
