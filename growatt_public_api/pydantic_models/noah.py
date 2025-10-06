from typing import Union

from pydantic import (
    ConfigDict,
)
from pydantic.alias_generators import to_camel

from .api_model import (
    EmptyStrToNone,
    ApiModel,
)


# #####################################################################################################################
# Noah status #########################################################################################################


def _noah_status_data_to_camel(snake: str) -> str:
    override = {
        "battery_package_quantity": "batteryNum",
        "ac_couple_power_control": "acCoupleEnable",
        "total_battery_pack_charging_power": "chargePower",
        "total_battery_pack_discharging_power": "disChargePower",
        "ct_flag": "isHaveCt",
        "currency": "moneyUnit",
        "money_today": "profitToday",
        "money_total": "profitTotal",
        "total_battery_pack_soc": "soc",
        # FIXME: assign
        # * "total_household_load"
        # * "household_load_apart_from_groplug"
        # * "ct_self_power"
        # to
        # * "loadPower"
        # * "groplugPower"
        # * "gridPower"
        # * "otherPower"
    }
    return override.get(snake, to_camel(snake=snake))


class NoahStatusData(ApiModel):
    """
    data was gathered using Nexa device
    Noah data might differ in some fields
    - recheck when Noah is available on test server
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_noah_status_data_to_camel,
    )

    ac_couple_power_control: Union[EmptyStrToNone, int] = None  # e.g. '1'
    alias: Union[EmptyStrToNone, str] = None  # e.g. 'NEXA 2000'
    associated_inv_sn: Union[EmptyStrToNone, str] = None  # Associated Inverter, e.g. None
    battery_package_quantity: Union[EmptyStrToNone, int] = None  # Number of parallel battery packs, e.g. '2'
    total_battery_pack_charging_power: Union[EmptyStrToNone, float] = None  # Total battery charging power, e.g. '0'
    total_battery_pack_discharging_power: Union[EmptyStrToNone, float] = (
        None  # Total battery discharging power, e.g. '0'
    )
    eac_today: Union[EmptyStrToNone, float] = None  # Daily power generation, e.g. '0.8'
    eac_total: Union[EmptyStrToNone, float] = None  # Total power generation, e.g. '116.7'
    eastron_status: Union[EmptyStrToNone, int] = None  # e.g. '-1'
    grid_power: Union[EmptyStrToNone, float] = None  # e.g. '620'  # FIXME assign (see above)
    groplug_num: Union[EmptyStrToNone, int] = None  # e.g. '0'
    groplug_power: Union[EmptyStrToNone, float] = None  # e.g. '0'  # FIXME assign (see above)
    ct_flag: Union[EmptyStrToNone, bool] = None  # e.g. 'true'
    load_power: Union[EmptyStrToNone, float] = None  # e.g. '620'  # FIXME assign (see above)
    currency: Union[EmptyStrToNone, str] = None  # e.g. '€'
    on_off_grid: Union[EmptyStrToNone, int] = None  # e.g. '0'
    other_power: Union[EmptyStrToNone, float] = None  # e.g. '0'  # FIXME assign (see above)
    pac: Union[EmptyStrToNone, float] = None  # BUCK (=step-down) output power, e.g. '0'
    plant_id: Union[EmptyStrToNone, int] = None  # e.g. '12345678'
    ppv: Union[EmptyStrToNone, float] = None  # Photovoltaic power (W), e.g. '0'
    money_today: Union[EmptyStrToNone, float] = None  # Income today in "currency", e.g. '0.32'
    money_total: Union[EmptyStrToNone, float] = None  # Income total in "currency", e.g. '46.68'
    total_battery_pack_soc: Union[EmptyStrToNone, int] = (
        None  # Total battery pack SOC (State of Charge) percentage, e.g. '11'
    )
    status: Union[EmptyStrToNone, int] = None  # 1: Normal, 4: Fault, 5: Heating, e.g. '6'
    work_mode: Union[EmptyStrToNone, int] = (
        None  # Current time period working mode (0=Load-First, 1=Battery-First, 2=Smart), e.g. '2'
    )


class NoahStatus(ApiModel):
    msg: Union[EmptyStrToNone, str] = None  # e.g. ''
    result: Union[EmptyStrToNone, int] = None  # 1=success, other=fail
    obj: Union[EmptyStrToNone, NoahStatusData] = (
        None  # {'acCoupleEnable': '1', 'alias': 'NEXA 2000', 'associatedInvSn': '', 'batteryNum': '2', 'chargePower': '0', 'disChargePower': '0', 'eacToday': '0.8', 'eacTotal': '116.7', 'eastronStatus': '-1', 'gridPower': '620', 'groplugNum': '0', 'groplugPower': '0', 'isHaveCt': 'true', 'loadPower': '620', 'moneyUnit': '€', 'onOffGrid': '0', 'otherPower': '0', 'pac': '0', 'plantId': '12345678', 'ppv': '0', 'profitToday': '0.32', 'profitTotal': '46.68', 'soc': '11', 'status': '6', 'workMode': '2'}
    )
