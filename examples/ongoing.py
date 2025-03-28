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

    # API v4
    _v4_set_power_on_ = ga.v4.setting_write_on_off(device_sn=INVERTER_SN, device_type="min", power_on=True)
    _v4_energy_hist_min_ = ga.v4.energy_history(device_sn=INVERTER_SN, device_type="min")
    _v4_energy_hist2_min_ = ga.v4.energy_history_multiple(device_sn=INVERTER_SN, device_type="min")
    _v4_energy_min_ = ga.v4.energy(device_sn=INVERTER_SN, device_type="min")
    _v4_details_min_ = ga.v4.details(device_sn=INVERTER_SN, device_type="min")
    _v4_device_list_ = ga.v4.list(page=1)

    # user
    _user_list_ = ga.user.list()
    _user_available_ = ga.user.check_username(username="DummyTestUser1")
    # from user.user import GrowattCountry
    # _user_register_ = ga.user.register(
    #     username="DummyTestUser1",
    #     password="DummyTestUser1pw",
    #     email="DummyTestUser1@example.com",
    #     country=GrowattCountry.JAPAN,
    #     user_type=1,
    #     installer_code="GWATT",
    #     phone_number="01234567890",
    #     time_zone="GMT+09:00",
    # )
    # _user_modify_ = ga.user.modify(
    #     user_id=601,
    #     phone_number="01234567890123",
    #     installer_code="GWATT",
    # )

    # groBoost
    _groboost_metrics_multiple_ = ga.groboost.metrics_multiple(device_sn=INVERTER_SN)
    _groboost_metrics_history_ = ga.groboost.metrics_history(device_sn=INVERTER_SN)
    _groboost_metrics_ = ga.groboost.metrics(device_sn=INVERTER_SN)
    _groboost_details_ = ga.groboost.details(device_sn=INVERTER_SN)

    # Environmental sensor
    _env_metrics_history_ = ga.env_sensor.metrics_history(datalogger_sn=DATALOGGER_SN, sensor_address=1)
    _env_metrics_ = ga.env_sensor.metrics(datalogger_sn=DATALOGGER_SN, sensor_address=1)
    _env_list_ = ga.env_sensor.list(datalogger_sn=DATALOGGER_SN)

    # Smart meter
    _sm_energy_history_ = ga.smart_meter.energy_history(datalogger_sn=DATALOGGER_SN, meter_address=1)
    _sm_energy_ = ga.smart_meter.energy(datalogger_sn=DATALOGGER_SN, meter_address=1)
    _sm_list_ = ga.smart_meter.list(datalogger_sn=DATALOGGER_SN)

    # pbd
    _pbd_energy_history_ = ga.pbd.energy_history(device_sn=INVERTER_SN)
    _pbd_energy_ = ga.pbd.energy(device_sn=INVERTER_SN)
    _pbd_details_ = ga.pbd.details(device_sn=INVERTER_SN)
    _pbd_alarms_ = ga.pbd.alarms(device_sn=INVERTER_SN)

    # hps
    _hps_energy_history_ = ga.hps.energy_history(device_sn=INVERTER_SN)
    _hps_energy_ = ga.hps.energy(device_sn=INVERTER_SN)
    _hps_details_ = ga.hps.details(device_sn=INVERTER_SN)
    _hps_alarms_ = ga.hps.alarms(device_sn=INVERTER_SN)

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
    _spa_setting_read_by_name_ = ga.spa.setting_read(device_sn=INVERTER_SN, parameter_id="pv_on_off")
    _spa_alarms_ = ga.spa.alarms(device_sn=INVERTER_SN)

    # sph
    _sph_energy_history_ = ga.sph.energy_history(device_sn=INVERTER_SN)
    _sph_energy_multiple_ = ga.sph.energy_multiple(device_sn=INVERTER_SN)
    _sph_energy_ = ga.sph.energy(device_sn=INVERTER_SN)
    _sph_details_ = ga.sph.details(device_sn=INVERTER_SN)
    _sph_setting_read_by_name_ = ga.sph.setting_read(device_sn=INVERTER_SN, parameter_id="pv_on_off")
    _sph_alarms_ = ga.sph.alarms(device_sn=INVERTER_SN)

    # max
    _max_setting_read_by_name_ = ga.max.setting_read(device_sn=INVERTER_SN, parameter_id="max_cmd_on_off")
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
    _vpp_write_ = ga.vpp.write(device_sn=INVERTER_SN, time_=time(hour=12, minute=13), percentage=100)
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
    _min_setting_read_by_name_single_ = ga.min.setting_read(device_sn=INVERTER_SN, parameter_id="tlx_on_off")
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
    _storage_setting_read_by_name_ = ga.storage.setting_read(device_sn=INVERTER_SN, parameter_id="storage_cmd_on_off")

    # inverter
    _inverter_setting_read_by_name_ = ga.inverter.setting_read(device_sn=INVERTER_SN, parameter_id="pv_on_off")
    _inverter_setting_read_by_reg_ = ga.inverter.setting_read(device_sn=INVERTER_SN, start_address=0)
    _inverter_setting_read_by_regs_ = ga.inverter.setting_read(device_sn=INVERTER_SN, start_address=0, end_address=10)
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
    _datalogger_check_ = ga.device.datalogger_validate(
        datalogger_sn=DATALOGGER_SN, validation_code=DATALOGGER_VALIDATION_CODE
    )
    # _datalogger_add_ = ga.device.datalogger_add(
    #     user_id=601,
    #     plant_id=PLANT_ID,
    #     datalogger_sn="QMN000BZP0000000",
    # )
    _datalogger_list_ = ga.device.datalogger_list(
        plant_id=PLANT_ID,
    )
    # _datalogger_delete_ = ga.device.datalogger_delete(
    #     plant_id=PLANT_ID,
    #     datalogger_sn="QMN000BZP0000000",
    # )
    _device_create_date_ = ga.device.create_date(device_sn=INVERTER_SN)
    _device_get_datalogger_ = ga.device.get_datalogger(device_sn=INVERTER_SN)
    _device_energy_day_ = ga.device.energy_day(device_sn=INVERTER_SN)
    _device_type_dl_ = ga.device.type_info(device_sn=DATALOGGER_SN)
    _device_type_inv_ = ga.device.type_info(device_sn=INVERTER_SN)
    _device_list_ = ga.device.list(plant_id=PLANT_ID)

    # plant
    # from growatt_public_api import GrowattCountry, PlantType
    # _plant_add_ = ga.plant.add(
    #     user_id=601,
    #     plant_name="DummyTestPlant1",
    #     peak_kw=0.8,
    #     country=GrowattCountry.SWEDEN,
    #     installer_code="GWATT",
    #     currency="€",
    #     longitude=22.2,
    #     latitude=33.3,
    #     # timezone_id=8,
    #     plant_type=PlantType.RESIDENTIAL,
    #     create_date=date.today(),
    #     price_per_kwh=0.31,
    #     city="London",
    #     address="Westminster Abbey 1",
    # )
    # _plant_modify_ = ga.plant.modify(
    #     user_id=601,
    #     plant_id=730,  # id from _plant_add_
    #     plant_name="DummyTestPlant1renamed",  # rename plant
    # )
    # _plant_delete_ = ga.plant.delete(
    #     plant_id=730  # id from _plant_add_
    # )
    _plant_list_ = ga.plant.list()
    _plant_list_by_user_ = ga.plant.list_by_user(username=USERNAME)
    _plant_device_sn_ = ga.plant.by_device(device_sn=INVERTER_SN)
    _plant_details_ = ga.plant.details(plant_id=PLANT_ID)
    _plant_power_ = ga.plant.power(plant_id=PLANT_ID, date_=date.today())
    _plant_energy_overview_ = ga.plant.energy_overview(plant_id=PLANT_ID)
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

    logger.warning("DEBUG")
