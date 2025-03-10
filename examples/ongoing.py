import os
from datetime import timedelta, date, time
from loguru import logger

from growatt_public_api import GrowattApi


# ############################################################################################################
# MAIN - used just for checking the implementation during development
# expects following environment variables:
# GROWATTAPITOKEN
# GROWATTPLANTID
# GROWATTINVERTERID
# GROWATTINVERTERSN
# GROWATTDATALOGGERSN
# GROWATTDATALOGGERVALIDATIONCODE
# ############################################################################################################

if __name__ == "__main__":
    logger.info("DEBUG")
    # ############################################################################################################
    API_TOKEN = os.environ.get("GROWATTAPITOKEN")
    USERNAME = os.environ.get("GROWATTUSERNAME")
    PLANT_ID = int(os.environ.get("GROWATTPLANTID"))
    INVERTER_ID = int(os.environ.get("GROWATTINVERTERID"))
    INVERTER_SN = os.environ.get("GROWATTINVERTERSN")
    DATALOGGER_SN = os.environ.get("GROWATTDATALOGGERSN")
    DATALOGGER_VALIDATION_CODE = os.environ.get("GROWATTDATALOGGERVALIDATIONCODE")
    SERVER_URL = None  # default

    ga = GrowattApi(token=API_TOKEN, server_url=SERVER_URL)
    logger.debug("API initialized")

    # # FIXME DEBUG
    # sample_data = """"""
    # import json
    # import pprint
    # j = json.loads(sample_data)
    # pprint.pprint(j, indent=4, width=500)
    # k = MinEnergyHistory.model_validate(j)  # <-----------------------------
    # pprint.pprint(k.model_dump(), indent=4, width=500)
    # # FIXME DEBUG
    #
    # # FIXME DEBUG
    # import pprint
    # pprint.pprint(response, indent=4, width=500)
    # k2 = MinEnergyHistory.model_validate(response)  # <-----------------------------
    # pprint.pprint(k2.model_dump(), indent=4, width=500)
    # # FIXME DEBUG

    # TODO API v4
    # TODO user
    # TODO hps
    # TODO pbd
    # TODO Smart meter
    # TODO Environmental tester
    # TODO groBoost

    # pcs
    _pcs_energy_history_ = ga.pcs.energy_history(device_sn=INVERTER_SN)
    _pcs_energy_ = ga.pcs.energy(device_sn=INVERTER_SN)
    _pcs_details_ = ga.pcs.details(device_sn=INVERTER_SN)
    _pcs_alarms_ = ga.pcs.alarms(device_sn=INVERTER_SN)

    # spa
    _spa_energy_multiple_ = ga.spa.energy_multiple(device_sn=INVERTER_SN)
    _spa_energy_history_ = ga.spa.energy_history(device_sn=INVERTER_SN)
    _spa_energy_ = ga.spa.energy(device_sn=INVERTER_SN)
    _spa_details_ = ga.spa.details(device_sn=INVERTER_SN)
    _spa_setting_read_by_name_ = ga.spa.setting_read(
        device_sn=INVERTER_SN, parameter_id="pv_on_off"
    )
    _spa_alarms_ = ga.spa.alarms(device_sn=INVERTER_SN)

    # sph
    _sph_energy_history_ = ga.sph.energy_history(device_sn=INVERTER_SN)
    _sph_energy_multiple_ = ga.sph.energy_multiple(device_sn=INVERTER_SN)
    _sph_energy_ = ga.sph.energy(device_sn=INVERTER_SN)
    _sph_details_ = ga.sph.details(device_sn=INVERTER_SN)
    _sph_setting_read_by_name_ = ga.sph.setting_read(
        device_sn=INVERTER_SN, parameter_id="pv_on_off"
    )
    _sph_alarms_ = ga.sph.alarms(device_sn=INVERTER_SN)

    # max
    _max_setting_read_by_name_ = ga.max.setting_read(
        device_sn=INVERTER_SN, parameter_id="max_cmd_on_off"
    )
    _max_energy_multiple_ = ga.max.energy_multiple(device_sn=INVERTER_SN)
    _max_energy_history_ = ga.max.energy_history(device_sn=INVERTER_SN)
    _max_energy_ = ga.max.energy(device_sn=INVERTER_SN)
    _max_details_ = ga.max.details(device_sn=INVERTER_SN)
    _max_alarms_ = ga.max.alarms(device_sn=INVERTER_SN)

    # vpp
    _vpp_write_multiple_ = ga.vpp.write_multiple(
        device_sn=INVERTER_SN,
        time_percent=[
            (95, time(hour=0, minute=0), time(hour=5, minute=0)),
            (-60, time(hour=5, minute=1), time(hour=12, minute=0)),
        ],
    )
    _vpp_write_ = ga.vpp.write(
        device_sn=INVERTER_SN, time_=time(hour=12, minute=13), percentage=100
    )
    _vpp_soc_ = ga.vpp.soc(device_sn=INVERTER_SN)

    # min
    _min_settings_ = ga.min.settings(device_sn=INVERTER_SN)
    _min_energy_multiple_ = ga.min.energy_multiple(device_sn=INVERTER_SN)
    _min_setting_write_by_name_ = ga.min.setting_write(
        device_sn=INVERTER_SN,
        parameter_id="tlx_on_off",
        parameter_value_1="0001",
    )
    _min_setting_write_by_reg_ = ga.min.setting_write(
        device_sn=INVERTER_SN,
        parameter_id="set_any_reg",
        parameter_value_1="0",
        parameter_value_2="1",
    )
    _min_setting_by_name_dict_ = {}
    for named_setting in [
        "backflow_setting",
        "tlx_on_off",
        "pf_sys_year",
        "pv_grid_voltage_high",
        "pv_grid_voltage_low",
        "tlx_off_grid_enable",
        "tlx_ac_discharge_frequency",
        "tlx_ac_discharge_voltage",
        "pv_active_p_rate",
        "pv_reactive_p_rate",
        "pv_power_factor",
        "charge_power",
        "charge_stop_soc",
        "discharge_power",
        "discharge_stop_soc",
        "ac_charge",
        "time_segment1",
        "time_segment2",
        "time_segment3",
        "time_segment4",
        "time_segment5",
        "time_segment6",
        "time_segment7",
        "time_segment8",
        "time_segment9",
    ]:
        _min_setting_by_name_dict_[named_setting] = ga.min.setting_read(
            device_sn=INVERTER_SN, parameter_id=named_setting
        )
    _min_setting_read_by_name_single_ = ga.min.setting_read(
        device_sn=INVERTER_SN, parameter_id="tlx_on_off"
    )
    _min_setting_read_by_reg_ = ga.min.setting_read(
        device_sn=INVERTER_SN,
        start_address=0,
        end_address=10,
    )
    _min_alarms_ = ga.min.alarms(device_sn=INVERTER_SN)
    _min_energy_history_ = ga.min.energy_history(device_sn=INVERTER_SN)
    _min_energy_ = ga.min.energy(device_sn=INVERTER_SN)
    _min_details_ = ga.min.details(device_sn=INVERTER_SN)

    # storage
    _storage_alarms_ = ga.storage.alarms(device_sn=INVERTER_SN)
    _storage_energy_history_ = ga.storage.energy_history(device_sn=INVERTER_SN)
    _storage_energy_ = ga.storage.energy(device_sn=INVERTER_SN)
    _storage_details_ = ga.storage.details(device_sn=INVERTER_SN)
    _storage_setting_write_by_name_ = ga.storage.setting_write(
        device_sn=INVERTER_SN, parameter_id="storage_cmd_on_off", parameter_value_1="1"
    )
    _storage_setting_read_by_name_ = ga.storage.setting_read(
        device_sn=INVERTER_SN, parameter_id="storage_cmd_on_off"
    )

    # inverter
    _inverter_setting_read_by_name_ = ga.inverter.setting_read(
        device_sn=INVERTER_SN, parameter_id="pv_on_off"
    )
    _inverter_setting_read_by_reg_ = ga.inverter.setting_read(
        device_sn=INVERTER_SN, start_address=0
    )
    _inverter_setting_read_by_regs_ = ga.inverter.setting_read(
        device_sn=INVERTER_SN, start_address=0, end_address=10
    )
    _inverter_energy_multiple_ = ga.inverter.energy_multiple(device_sn=INVERTER_SN)
    _inverter_alarms_ = ga.inverter.alarms(device_sn=INVERTER_SN)
    _inverter_energy_history_ = ga.inverter.energy_history(device_sn=INVERTER_SN)
    _inverter_energy_ = ga.inverter.energy(device_sn=INVERTER_SN)
    _inverter_details_ = ga.inverter.details(device_sn=INVERTER_SN)
    _inverter_setting_write_by_reg_ = ga.inverter.setting_write(
        # will return failure as my inverter type is 7 (not 1)
        device_sn=INVERTER_SN,
        parameter_id="set_any_reg",
        parameter_value_1="0",
        parameter_value_2="1",
    )

    # device
    # TODO maybe split from device to inverter/datalogger?
    _device_create_date_ = ga.device.create_date(device_sn=INVERTER_SN)
    _device_get_datalogger_ = ga.device.get_datalogger(device_sn=INVERTER_SN)
    _device_energy_day_ = ga.device.energy_day(device_sn=INVERTER_SN)
    _datalogger_check_ = ga.device.datalogger_validate(
        datalogger_sn=DATALOGGER_SN, validation_code=DATALOGGER_VALIDATION_CODE
    )
    _device_type_dl_ = ga.device.type_info(device_sn=DATALOGGER_SN)
    _device_type_inv_ = ga.device.type_info(device_sn=INVERTER_SN)
    _device_list_ = ga.device.list(plant_id=PLANT_ID)

    # plant
    _plant_device_sn_ = ga.plant.by_device(device_sn=INVERTER_SN)
    _plant_power_ = ga.plant.power(plant_id=PLANT_ID, date_=date.today())
    _plant_energy_history_d_ = ga.plant.energy_history(
        plant_id=PLANT_ID,
        date_interval="day",
        start_date=date.today() - timedelta(days=7),
        end_date=date.today(),
    )
    _plant_energy_history_m_ = ga.plant.energy_history(
        plant_id=PLANT_ID,
        date_interval="month",
        start_date=date.today() - timedelta(days=30),
        end_date=date.today(),
    )
    _plant_energy_history_y_ = ga.plant.energy_history(
        plant_id=PLANT_ID,
        date_interval="month",
        start_date=date.today() - timedelta(days=365),
        end_date=date.today(),
    )
    _plant_energy_overview_ = ga.plant.energy_overview(plant_id=PLANT_ID)
    _plant_details_ = ga.plant.details(plant_id=PLANT_ID)
    _plant_list_by_user_ = ga.plant.list_by_user(username=USERNAME)
    _plant_list_ = ga.plant.list()

    logger.warning("DEBUG")
