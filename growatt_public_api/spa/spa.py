from datetime import date, timedelta, time
from typing import Optional, Union, List, Tuple
from ..growatt_types import DeviceType
from ..pydantic_models import VppSoc, VppWrite
from ..pydantic_models.api_v4 import (
    SpaDetailsV4,
    SpaEnergyV4,
    SpaEnergyHistoryV4,
    SpaEnergyHistoryMultipleV4,
    SettingReadVppV4,
    SettingWriteV4,
)
from ..pydantic_models.spa import (
    SpaSettingRead,
    SpaSettingWrite,
    SpaDetails,
    SpaEnergyOverview,
    SpaEnergyHistory,
    SpaAlarms,
    SpaEnergyOverviewMultiple,
    SpaEnergyOverviewMultipleItem,
)
from ..session import GrowattApiSession
from ..api_v4.api_v4 import ApiV4
from ..vpp.vpp import Vpp


class Spa:
    """
    endpoints for SPA inverters
    https://www.showdoc.com.cn/262556420217021/6129790987434517

    Note:
        Only applicable to devices with device type 6 (spa) returned by plant.list_devices()
    """

    session: GrowattApiSession
    _api_v4: ApiV4
    _api_vpp: Vpp
    device_sn: Optional[str] = None

    def __init__(self, session: GrowattApiSession, device_sn: Optional[str] = None) -> None:
        self.session = session
        self._api_v4 = ApiV4(session)
        self._api_vpp = Vpp(session)
        self.device_sn = device_sn

    def _device_sn(self, device_sn: Optional[Union[str, List[str]]]) -> Union[str, List[str]]:
        """
        Use device_sn explicitly provided, fallback to the one from the instance
        """
        device_sn = device_sn or self.device_sn
        if device_sn is None:
            raise AttributeError("device_sn must be provided")
        return device_sn

    def setting_read(
        self,
        device_sn: Optional[str] = None,
        parameter_id: Optional[str] = None,
        start_address: Optional[int] = None,
        end_address: Optional[int] = None,
    ) -> SpaSettingRead:
        """
        Read Spa setting parameter interface
        Read Spa setting parameter interface
        https://www.showdoc.com.cn/262556420217021/6129809145198328

        Note:
            Only applicable to devices with device type 6 (spa) returned by plant.list_devices()

        This method allows to read
        * predefined settings
          * pass parameter_id, do not pass start_address or end_address
        * any register value
          * pass start_address and end_address, do not pass parameter_id
        see setting_write() for more details

        Specific error codes:
        * 10001: Reading failed
        * 10002: Device does not exist
        * 10003: Device offline
        * 10004: Collector serial number is empty
        * 10005: Collector offline
        * 10006: Collector type does not support reading Get function
        * 10007: The collector version does not support the reading function
        * 10008: The collector connects to the server error, please restart and try again
        * 10009: The read setting parameter type does not exist

        Args:
            device_sn (str): SPA SN
            parameter_id (Optional[str]): parameter ID - specify either parameter_id ort start/end_address
            start_address (Optional[int]): register address to start reading from - specify either parameter_id ort start/end_address
            end_address (Optional[int]): register address to stop reading at

        Returns:
            SpaSettingRead
            e.g.
            {
                "data": "0",
                "error_code": 0,
                "error_msg": ""
            }
        """

        if parameter_id is None and start_address is None:
            raise ValueError("specify either parameter_id or start_address/end_address")
        elif parameter_id is not None and start_address is not None:
            raise ValueError("specify either parameter_id or start_address/end_address - not both.")
        elif parameter_id is not None:
            # named parameter
            start_address = 0
            end_address = 0
        else:
            # using register-number mode
            parameter_id = "set_any_reg"
            if start_address is None:
                start_address = end_address
            if end_address is None:
                end_address = start_address

        response = self.session.post(
            endpoint="readSpaParam",
            data={
                "device_sn": self._device_sn(device_sn),
                "paramId": parameter_id,
                "startAddr": start_address,
                "endAddr": end_address,
            },
        )

        return SpaSettingRead.model_validate(response)

    def setting_read_vpp_param(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        parameter_id: str,
        device_sn: Optional[str] = None,
    ) -> SettingReadVppV4:
        """
        Read VPP parameters using "new-api" endpoint
        Read the VPP related parameters of the device according to the SN of the device.
        https://www.showdoc.com.cn/2598832417617967/11558629942271434

        Note:
        * The current interface only supports
          * SPA 1000-3000TL BL
          * SPA 4000-10000TL3 BH

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Allowed/known values for vpp_param:
          see self.setting_write_vpp_param()

        Args:
            device_sn (str): Inverter serial number
            parameter_id (str): Set parameter enumeration, example: set_param_1

        Returns:
            SettingReadVppV4
            e.g.
            {   'data': 0,
                'error_code': 0,
                'error_msg': 'success'}

        """

        return self._api_v4.setting_read_vpp_param(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.SPA,
            parameter_id=parameter_id,
        )

    # noinspection PyUnusedLocal
    def setting_write(
        self,
        parameter_id: str,
        parameter_value_1: Union[str, int],
        parameter_value_2: Optional[Union[str, int]] = None,
        parameter_value_3: Optional[Union[str, int]] = None,
        parameter_value_4: Optional[Union[str, int]] = None,
        parameter_value_5: Optional[Union[str, int]] = None,
        parameter_value_6: Optional[Union[str, int]] = None,
        parameter_value_7: Optional[Union[str, int]] = None,
        parameter_value_8: Optional[Union[str, int]] = None,
        parameter_value_9: Optional[Union[str, int]] = None,
        parameter_value_10: Optional[Union[str, int]] = None,
        parameter_value_11: Optional[Union[str, int]] = None,
        parameter_value_12: Optional[Union[str, int]] = None,
        parameter_value_13: Optional[Union[str, int]] = None,
        parameter_value_14: Optional[Union[str, int]] = None,
        parameter_value_15: Optional[Union[str, int]] = None,
        parameter_value_16: Optional[Union[str, int]] = None,
        parameter_value_17: Optional[Union[str, int]] = None,
        parameter_value_18: Optional[Union[str, int]] = None,
        device_sn: Optional[str] = None,
    ) -> SpaSettingWrite:
        """
        Spa parameter settings
        Spa parameter setting interface
        https://www.showdoc.com.cn/262556420217021/6129790987434517

        Note:
            Only applicable to devices with device type 6 (spa) returned by plant.list_devices()

        This method allows to set
        * predefined settings (see table below)
        * any register value (see table below for most relevant settings, google for "Growatt Inverter Modbus RTU Protocol V1.20" for more)

        Predefined settings
        ========================+=======================================+===========================+============================================================================
        description             | parameter_id                          | parameter_value_[n]       | comment
        ========================+=======================================+===========================+============================================================================
        Load priority           | spa_load_flast                        | [ 1]: 0 ~ 23              | [ 1]: hour
         discharge prohibition  |                                       | [ 2]: 0 ~ 59              | [ 2]: minute
                                |                                       | [ 3]: 0 ~ 23              | [ 3]: hour
                                |                                       | [ 4]: 0 ~ 59              | [ 4]: minute
                                |                                       | [ 5]: 0  or 1             | [ 5]: 0 = disable, 1 = enable
                                |                                       | [ 6]: 0 ~ 23              | [ 6]: hour
                                |                                       | [ 7]: 0 ~ 59              | [ 7]: minute
                                |                                       | [ 8]: 0 ~ 23              | [ 8]: hour
                                |                                       | [ 9]: 0 ~ 59              | [ 9]: minute
                                |                                       | [10]: 0  or 1             | [10]: 0 = disable, 1 = enable
                                |                                       | [11]: 0 ~ 23              | [11]: hour
                                |                                       | [12]: 0 ~ 59              | [12]: minute
                                |                                       | [13]: 0 ~ 23              | [13]: hour
                                |                                       | [14]: 0 ~ 59              | [14]: minute
                                |                                       | [15]: 0  or 1             | [15]: 0 = disable, 1 = enable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Grid priority           | spa_ac_charge_time_period             | [ 1]: 0 ~ 100             | [ 1]: discharge power
                                |                                       | [ 2]: 0 ~ 100             | [ 2]: discharge stop SOC
                                |                                       | [ 3]: 0 ~ 23              | [ 3]: hour
                                |                                       | [ 4]: 0 ~ 59              | [ 4]: minute
                                |                                       | [ 5]: 0 ~ 23              | [ 5]: hour
                                |                                       | [ 6]: 0 ~ 59              | [ 6]: minute
                                |                                       | [ 7]: 0  or 1             | [ 7]: 0 = disable, 1 = enable
                                |                                       | [ 8]: 0 ~ 23              | [ 8]: hour
                                |                                       | [ 9]: 0 ~ 59              | [ 9]: minute
                                |                                       | [10]: 0 ~ 23              | [10]: hour
                                |                                       | [11]: 0 ~ 59              | [11]: minute
                                |                                       | [12]: 0  or 1             | [12]: 0 = disable, 1 = enable
                                |                                       | [13]: 0 ~ 23              | [13]: hour
                                |                                       | [14]: 0 ~ 59              | [14]: minute
                                |                                       | [15]: 0 ~ 23              | [15]: hour
                                |                                       | [16]: 0 ~ 59              | [16]: minute
                                |                                       | [17]: 0  or 1             | [17]: 0 = disable, 1 = enable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Battery priority        | spa_ac_charge_time_period             | [ 1]: 0 ~ 100             | [ 1]: charging power
                                |                                       | [ 2]: 0 ~ 100             | [ 2]: charge stop SOC
                                |                                       | [ 3]: 0  or 1             | [ 3]: mains - 0 = disable, 1 = enable
                                |                                       | [ 4]: 0 ~ 23              | [ 4]: hour
                                |                                       | [ 5]: 0 ~ 59              | [ 5]: minute
                                |                                       | [ 6]: 0 ~ 23              | [ 6]: hour
                                |                                       | [ 7]: 0 ~ 59              | [ 7]: minute
                                |                                       | [ 8]: 0  or 1             | [ 8]: 0 = disable, 1 = enable
                                |                                       | [ 9]: 0 ~ 23              | [ 9]: hour
                                |                                       | [10]: 0 ~ 59              | [10]: minute
                                |                                       | [11]: 0 ~ 23              | [11]: hour
                                |                                       | [12]: 0 ~ 59              | [12]: minute
                                |                                       | [13]: 0  or 1             | [13]: 0 = disable, 1 = enable
                                |                                       | [14]: 0 ~ 23              | [14]: hour
                                |                                       | [15]: 0 ~ 59              | [15]: minute
                                |                                       | [16]: 0 ~ 23              | [16]: hour
                                |                                       | [17]: 0 ~ 59              | [17]: minute
                                |                                       | [18]: 0  or 1             | [18]: 0 = disable, 1 = enable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Power on and off        | pv_on_off                             | [1]: 0000 or 0001         | 0000 = off, 0001 = on
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Set time                | pf_sys_year                           | [1]: "00:00" ~ "23:59"    | HH:MM
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Upper limit             | pv_grid_voltage_high                  | [1]: e.g. 270             | V
         of mains voltage       |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Lower limit             | pv_grid_voltage_low                   | [1]: e.g. 180             | V
         of mains voltage       |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Off-grid                | spa_off_grid_enable                   | [1]: 0 or 1               | 0 = disabled, 1 = enable
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Off-grid frequency      | spa_ac_discharge_frequency            | [1]: 0 or 1               | 0 = 50Hz, 1 = 60Hz
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Off-grid voltage        | spa_ac_discharge_voltage              | [1]: 0 or 1 or 2          | 0 = 230V, 1 = 208V, 2 = 240V
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Whether to store the    | pv_pf_cmd_memory_state                | [1]: 0 or 1               | 0 = off, 1 = on
         following PF commands  |                                       |                           |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Active power            | pv_active_p_rate                      | [1]: 0 ~ 100              |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        Reactive power          | pv_reactive_p_rate                    | [1]: 0 ~ 100              |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------
        PF value                | pv_power_factor                       | [1]: -0.8 ~ -1            |
                                |                                       |   or  0.8 ~  1            |
        ------------------------+---------------------------------------+---------------------------+----------------------------------------------------------------------------

        Register settings
        =================
        google for "Growatt Inverter Modbus RTU Protocol V1.20" for more

        Specific error codes:
        * 10001: system error
        * 10002: AC energy storage machine server error
        * 10003: AC energy storage machine offline
        * 10004: AC energy storage machine serial number is empty
        * 10005: collector offline
        * 10006: Setting parameter type does not exist
        * 10007: parameter value is empty
        * 10008: parameter value is out of range
        * 10009: date and time format is wrong
        * 10012: AC energy storage machine does not exist
        * 10013: end time cannot be less than start time

        Args:
            device_sn (str): SPA SN
            parameter_id (str): parameter ID - pass "set_any_reg" to write register address
            parameter_value_1 (Union[str, int]): parameter value 1
            parameter_value_2 (Optional[Union[str, int]]): parameter value 2
            parameter_value_3 (Optional[Union[str, int]]): parameter value 3
            parameter_value_4 (Optional[Union[str, int]]): parameter value 4
            parameter_value_5 (Optional[Union[str, int]]): parameter value 5
            parameter_value_6 (Optional[Union[str, int]]): parameter value 6
            parameter_value_7 (Optional[Union[str, int]]): parameter value 7
            parameter_value_8 (Optional[Union[str, int]]): parameter value 8
            parameter_value_9 (Optional[Union[str, int]]): parameter value 9
            parameter_value_10 (Optional[Union[str, int]]): parameter value 10
            parameter_value_11 (Optional[Union[str, int]]): parameter value 11
            parameter_value_12 (Optional[Union[str, int]]): parameter value 12
            parameter_value_13 (Optional[Union[str, int]]): parameter value 13
            parameter_value_14 (Optional[Union[str, int]]): parameter value 14
            parameter_value_15 (Optional[Union[str, int]]): parameter value 15
            parameter_value_16 (Optional[Union[str, int]]): parameter value 16
            parameter_value_17 (Optional[Union[str, int]]): parameter value 17
            parameter_value_18 (Optional[Union[str, int]]): parameter value 18

        Returns:
            SpaSettingWrite
            e.g. (success)
            {
                "data": "",
                "error_code": 0,
                "error_msg": "Set Successful spa return"
            }
        """

        # put parameters to a dict to make handling easier
        parameters = {}
        for i in range(1, 19):
            parameters[i] = eval(f"parameter_value_{i}")

        if parameter_id == "set_any_reg":
            assert parameters[1] is not None, "register address must be provided"
            assert parameters[2] is not None, "new value must be provided"
            for i in range(3, 19):
                assert parameters[i] is None, f"parameter {i} must not be used for set_any_reg"
        else:
            assert parameters[1] is not None, "new value must be provided"

        # API docs: if there is no value, pass empty string ""
        for i in range(2, 19):
            if parameters[i] is None:
                parameters[i] = ""

        # parameter values must be string
        for i in range(1, 19):
            parameters[i] = str(parameters[i])

        response = self.session.post(
            endpoint="spaSet",
            data={
                "spa_sn": self._device_sn(device_sn),
                "type": parameter_id,
                **{f"param{i}": parameters[i] for i in range(1, 19)},
            },
        )

        return SpaSettingWrite.model_validate(response)

    def setting_write_on_off(
        self,
        power_on: bool,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the power on and off using "new-api" endpoint
        Turn device on/off
        https://www.showdoc.com.cn/2540838290984246/11330750679726415

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            power_on (bool): True = Power On, False = Power Off

        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}
        """

        return self._api_v4.setting_write_on_off(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.SPA,
            power_on=power_on,
        )

    def setting_write_active_power(
        self,
        active_power_percent: int,
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set the active power using "new-api" endpoint
        Set the active power percentage of the device based on the device type and SN of the device.
        https://www.showdoc.com.cn/2540838290984246/11330751643769012

        Note:
        * most devices can be configured to 0 ~ 100 %
        * NOAH devices can be configured to 0 ~ 800 W

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Args:
            device_sn (str): Inverter serial number
            active_power_percent (int): Percentage of active power, range 0-100

        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_active_power(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.SPA,
            active_power=active_power_percent,
        )

    def setting_write_vpp_param(  # noqa: C901 'ApiV4.energy' is too complex (11)
        self,
        parameter_id: str,
        value: Union[int, str],
        device_sn: Optional[str] = None,
    ) -> SettingWriteV4:
        """
        Set VPP parameters using "new-api" endpoint
        Set the VPP related parameters of the device according to the SN of the device.
        https://www.showdoc.com.cn/2598832417617967/11558385202215329

        Note:
        * The current interface only supports
          * SPA 1000-3000TL BL
          * SPA 4000-10000TL3 BH

        Rate limit(s):
        * The maximum frequency is once every 5 seconds.

        Allowed/known values for vpp_param:
        ========================+===============+===========================+============================================================================
        description             | parameter_id  | parameter_value           | comment
        ========================+===============+===========================+============================================================================
        Control authority       | set_param_1   | 0 ~ 1                     | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        On off command          | set_param_2   | 0 ~ 1                     | Not storage
                                |               |                           | 0 = power off
                                |               |                           | 1 = power on (default)
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        System time             | set_param_3   | yyyy-mm-dd HH:MM:SS       | Example: 2024-10-10 13:14:14
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        SYN enable              | set_param_4   | 0 ~ 1                     | Offline box enable
                                |               |                           | 0: not enabled (default)
                                |               |                           | 1: enable
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Active power            | set_param_5   | 0 ~ 100                   | Power limit percentage
         percentage derating    |               |                           | default value = 100
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Static active power     | set_param_6   | 0 ~ 100                   | Power limit percent
                                |               |                           | Actual active power is the less one between Active power percentage derating
                                |               |                           |  and Static active power limitation - Not storage
                                |               |                           | default value = 100
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EPS offline enable      | set_param_7   | 0 ~ 1                     | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EPS offline frequency   | set_param_8   | 0 ~ 1                     | 0 = 50 Hz (default)
                                |               |                           | 1 = 60 Hz
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EPS offline voltage(3)  | set_param_9   | 0 ~ 6                     | 0 = 230 V (default)
                                |               |                           | 1 = 208V
                                |               |                           | 2 = 240V
                                |               |                           | 3 = 220V
                                |               |                           | 4 = 127V
                                |               |                           | 5 = 277V
                                |               |                           | 6 = 254V
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Fix Q                   | set_param_10  | 0 ~ 60                    | Power limit percentage
                                |               |                           | default value = 60
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Reactive power mode     | set_param_11  | 0 ~ 5                     | 0: PF=1 (default)
                                |               |                           | 1: Pf value setting
                                |               |                           | 2: Default pf curve(reserve)
                                |               |                           | 3: User set pf curve(reserve)
                                |               |                           | 4: Lagging reactive power (+)
                                |               |                           | 5: Leading reactive power (-)
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Power factor            | set_param_12  | 0 ~ 20000                 | Actual power factor = (10000 - set_value) * 0.0001
                                |               |                           | default value = 10000
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Dynamic export          | set_param_13  | 0 ~ 1                     | 0 = disabled (default)
         limitation             |               |                           | 1 = single machine anti-back flow enable
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Export limitation power | set_param_14  | -100 ~ 100                | Positive value is backflow, negative value is fair current
                                |               |                           | default value = 0
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Failure value of        | set_param_15  | 0 ~ 100                   | When the communication with meter failed (30204 is 1), use this register
         anti-backflow limiting |               |                           |  to limit reactive power，for backflow control
         power                  |               |                           | default value = 0
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-back flow fail     | set_param_16  | 0 ~ 300                   | default value = 30
         time/EMS communicating |               |                           |
         fail time              |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        EMS communicating fail  | set_param_17  | 0 ~ 1                     | 0 = disabled (default)
         enable                 |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Super anti-backflow     | set_param_18  | 0 ~ 1                     | 0 = disabled (default)
         enable                 |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow feed      | set_param_19  | 0 ~ 20000                 | default value = 27
         power change slope     |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow single    | set_param_20  | 0 ~ 1                     | 0 = disabled (default)
         phase ctrl enable      |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Anti-backflow           | set_param_21  | 0 ~ 1                     | 0 = Default mode (default)
         protection mode（1）    |               |                           | 1 = software and hardware control mode
                                |               |                           | 2 = software control mode
                                |               |                           | 3 = hardware control mode
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Charging cut off SOC    | set_param_22  | 70 ~ 100                  | default value = 100
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Online discharge cut    | set_param_23  | 10 ~ 30                   | default value = 10
         off SOC                |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Load priority discharge | set_param_24  | 10 ~ 20                   | default value = 10
         cut off SOC (2)        |               |                           |
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Remote power control    | set_param_25  | 0 ~ 1                     | Not storage
         enable                 |               |                           | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Remote power control    | set_param_26  | 0 ~ 1440                  | Not storage
         charging time          |               |                           | 0: unlimited time (default)
                                |               |                           | 1 ~ 1440 min: control the power duration according to the set time
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Remote charge and       | set_param_27  | -100 ~ 100                | Not storage
         discharge power        |               |                           | negative value = discharge, positive value = charge
                                |               |                           | default value = 0
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        AC charging enable      | set_param_28  | 0 ~ 1                     | 0 = disabled (default)
                                |               |                           | 1 = enabled
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Offline discharge cut   | set_param_29  | 10 ~ 30                   | default value = 10
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery charge stop     | set_param_30  | 0 ~ 15000                 | Lead-acid battery used - Distinguished by voltage level
         voltage                |               |                           |  3800 = 127 V
                                |               |                           | 10000 = 227 V
                                |               |                           |  8000 = Others
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery discharge stop  | set_param_31  | 0 ~ 15000                 | Lead-acid battery used - Distinguished by voltage level
         voltage                |               |                           | 3800 = 127 V
                                |               |                           | 7500 = 227 V
                                |               |                           | 6500 = Others
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery max charge      | set_param_32  | 0 ~ 2000                  | Lead-acid battery used
         current                |               |                           | default value = 1500
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Battery max discharge   | set_param_33  | 0 ~ 2000                  | Lead-acid battery used
         current                |               |                           | default value = 1500
        ------------------------+---------------+---------------------------+----------------------------------------------------------------------------
        Charging and discharging| set_param_34  | 0 ~ 2000                  | Set time period (json format: [{percentage: power, startTime: start time, endTime: end time}]
         in different periods   |               |                           | time range: 0-1440
          (20 sections)         |               |                           | e.g.: [{"percentage":95,"startTime":0,"endTime":300},{"percentage":-60,"startTime":301,"endTime":720}]
        ========================+===============+===========================+============================================================================
        see https://www.showdoc.com.cn/2598832417617967/11558385130027995 or https://www.showdoc.com.cn/p/fc84c86facd79b3692f585fbd7a6e33b
        ========================+===============+===========================+============================================================================


        Args:
            device_sn (str): Inverter serial number
            parameter_id (str): Set parameter enumeration, example: set_param_1
            value (Union[int, str]): the parameter value set, example:value


        Returns:
            SettingWriteV4
            e.g.
            {   'data': None,
                'error_code': 0,
                'error_msg': 'PARAMETER_SETTING_SUCCESSFUL'}

        """

        return self._api_v4.setting_write_vpp_param(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.SPA,
            parameter_id=parameter_id,
            value=value,
        )

    def details(
        self,
        device_sn: Optional[str] = None,
    ) -> SpaDetails:
        """
        Get basic spa information
        Interface to get basic information of Spa
        https://www.showdoc.com.cn/262556420217021/6129791904178555

        Note:
            Only applicable to devices with device type 6 (spa) returned by plant.list_devices()

        Args:
            device_sn (str): SPA device SN

        Returns:
            SpaDetails
            e.g.
            {   'data': {   'active_p_rate': 100,
                            'address': 1,
                            'alias': 'LHD0847002',
                            'backflow_setting': None,
                            'bat_aging_test_step': 0,
                            'bat_first_switch1': 0,
                            'bat_first_switch2': 0,
                            'bat_first_switch3': 0,
                            'bat_temp_lower_limit_c': 0.0,
                            'bat_temp_lower_limit_d': 120.0,
                            'bat_temp_upper_limit_c': 40.0,
                            'bat_temp_upper_limit_d': 55.0,
                            'battery_type': 0,
                            'baudrate': 0,
                            'bct_adjust': 0,
                            'bct_mode': 0,
                            'buck_ups_fun_en': True,
                            'buck_ups_volt_set': 0.0,
                            'charge_power_command': 100,
                            'charge_time1': None,
                            'charge_time2': None,
                            'charge_time3': None,
                            'children': [],
                            'com_address': 1,
                            'communication_version': None,
                            'country_selected': 0,
                            'datalogger_sn': 'JPC2827188',
                            'discharge_power_command': 100,
                            'discharge_time1': None,
                            'discharge_time2': None,
                            'discharge_time3': None,
                            'dtc': 3701,
                            'energy_day': 0.0,
                            'energy_day_map': {},
                            'energy_month': 0.0,
                            'energy_month_text': '0',
                            'eps_freq_set': 0,
                            'eps_fun_en': False,
                            'eps_volt_set': 0,
                            'equipment_type': None,
                            'float_charge_current_limit': 650,
                            'forced_charge_time_start1': datetime.time(0, 0),
                            'forced_charge_time_start2': datetime.time(1, 30),
                            'forced_charge_time_start3': datetime.time(10, 30),
                            'forced_charge_time_stop1': datetime.time(23, 59),
                            'forced_charge_time_stop2': datetime.time(4, 29),
                            'forced_charge_time_stop3': datetime.time(13, 29),
                            'forced_discharge_time_start1': datetime.time(0, 0),
                            'forced_discharge_time_start2': datetime.time(7, 30),
                            'forced_discharge_time_start3': datetime.time(13, 30),
                            'forced_discharge_time_stop1': datetime.time(23, 59),
                            'forced_discharge_time_stop2': datetime.time(10, 29),
                            'forced_discharge_time_stop3': datetime.time(16, 29),
                            'fw_version': 'RH1.0',
                            'grid_first_switch1': True,
                            'grid_first_switch2': False,
                            'grid_first_switch3': False,
                            'group_id': -1,
                            'id': 0,
                            'img_path': './css/img/status_gray.gif',
                            'inner_version': 'rHAA020202',
                            'last_update_time': {'date': 19, 'day': 3, 'hours': 16, 'minutes': 3, 'month': 11, 'seconds': 4, 'time': 1545206584000, 'timezone_offset': -480, 'year': 118},
                            'last_update_time_text': datetime.datetime(2018, 12, 19, 16, 3, 4),
                            'lcd_language': 1,
                            'level': 4,
                            'load_first_start_time1': datetime.time(0, 0),
                            'load_first_start_time2': datetime.time(4, 30),
                            'load_first_start_time3': datetime.time(0, 0),
                            'load_first_stop_time1': datetime.time(23, 59),
                            'load_first_stop_time2': datetime.time(7, 29),
                            'load_first_stop_time3': datetime.time(0, 0),
                            'load_first_switch1': False,
                            'load_first_switch2': False,
                            'load_first_switch3': False,
                            'location': 'null',
                            'lost': True,
                            'manufacturer': 'New Energy ',
                            'modbus_version': 305,
                            'model': 29136100000,
                            'model_text': 'A0B0D0T4P7U2M2S1',
                            'on_off': True,
                            'p_charge': 0,
                            'p_discharge': 0,
                            'parent_id': 'LIST_JPC2827188_96',
                            'pf_cmd_memory_state': None,
                            'pf_sys_year': None,
                            'plant_id': 0,
                            'plant_name': None,
                            'pmax': 3000,
                            'port_name': 'port_name',
                            'power_factor': 10000.0,
                            'power_max': None,
                            'power_max_text': None,
                            'power_max_time': None,
                            'priority_choose': 2,
                            'pv_active_p_rate': None,
                            'pv_grid_voltage_high': None,
                            'pv_grid_voltage_low': None,
                            'pv_on_off': None,
                            'pv_pf_cmd_memory_state': None,
                            'pv_power_factor': None,
                            'pv_reactive_p_rate': None,
                            'pv_reactive_p_rate_two': None,
                            'reactive_p_rate': 100,
                            'record': None,
                            'serial_num': 'LHD0847002',
                            'spa_ac_discharge_frequency': None,
                            'spa_ac_discharge_voltage': None,
                            'spa_off_grid_enable': None,
                            'status': -1,
                            'status_text': 'spa.status.lost',
                            'sys_time': datetime.datetime(2018, 12, 19, 15, 59),
                            'tcp_server_ip': '192.168.3.35',
                            'tree_id': 'ST_LHD0847002',
                            'tree_name': 'LHD0847002',
                            'updating': False,
                            'user_name': None,
                            'usp_freq_set': None,
                            'vac_high': 264.5,
                            'vac_low': 184.0,
                            'vbat_start_for_charge': 58.0,
                            'vbat_start_for_discharge': 48.0,
                            'vbat_stop_for_charge': 5.880000114440918,
                            'vbat_stop_for_discharge': 4.699999809265137,
                            'vbat_warn_clr': 5.0,
                            'vbat_warning': 480.0,
                            'wcharge_soc_low_limit1': 100,
                            'wcharge_soc_low_limit2': 100,
                            'wdis_charge_soc_low_limit1': 100,
                            'wdis_charge_soc_low_limit2': 5},
                'datalogger_sn': 'JPC2827188',
                'device_sn': 'LHD0847002',
                'error_code': 0,
                'error_msg': None}
        """

        response = self.session.get(
            endpoint="device/spa/spa_data_info",
            params={
                "device_sn": self._device_sn(device_sn),
            },
        )

        return SpaDetails.model_validate(response)

    def details_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> SpaDetailsV4:
        """
        Batch device information using "new-api" endpoint
        Retrieve basic information of devices in bulk based on device SN.
        https://www.showdoc.com.cn/2540838290984246/11292915673945114

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            SpaDetailsV4
            e.g.
            {   'data': {   'spa': [   {   'ac_charge_enable': False,
                                           'active_p_rate': 100,
                                           'address': 1,
                                           'alias': 'CHENYINSHU',
                                           'backflow_setting': None,
                                           'bat_aging_test_step': 0,
                                           'bat_first_switch1': 0,
                                           'bat_first_switch2': 0,
                                           'bat_first_switch3': 0,
                                           'bat_pack_num': 0,
                                           'bat_serial_num': None,
                                           'bat_sys_rate_energy': 0.0,
                                           'bat_temp_lower_limit_c': 101.0,
                                           'bat_temp_lower_limit_d': 110.0,
                                           'bat_temp_upper_limit_c': 60.0,
                                           'bat_temp_upper_limit_d': 70.0,
                                           'battery_type': 1,
                                           'baudrate': 0,
                                           'bct_adjust': 0,
                                           'bct_mode': 0,
                                           'buck_ups_fun_en': True,
                                           'buck_ups_volt_set': 0.0,
                                           'charge_power_command': 100,
                                           'charge_time1': None,
                                           'charge_time2': None,
                                           'charge_time3': None,
                                           'children': None,
                                           'com_address': 1,
                                           'communication_version': None,
                                           'country_selected': 0,
                                           'datalogger_sn': 'BQC0733006',
                                           'device_type': 0,
                                           'discharge_power_command': 100,
                                           'discharge_time1': None,
                                           'discharge_time2': None,
                                           'discharge_time3': None,
                                           'dtc': 3701,
                                           'energy_day': 0.0,
                                           'energy_day_map': {},
                                           'energy_month': 0.0,
                                           'energy_month_text': '0',
                                           'eps_freq_set': 0,
                                           'eps_fun_en': False,
                                           'eps_volt_set': 0,
                                           'equipment_type': None,
                                           'export_limit': 0.0,
                                           'export_limit_power_rate': 0.0,
                                           'failsafe': 0,
                                           'float_charge_current_limit': 450.0,
                                           'forced_charge_stop_switch4': False,
                                           'forced_charge_stop_switch5': False,
                                           'forced_charge_stop_switch6': False,
                                           'forced_charge_time_start1': datetime.time(0, 0),
                                           'forced_charge_time_start2': datetime.time(0, 0),
                                           'forced_charge_time_start3': datetime.time(0, 0),
                                           'forced_charge_time_start4': None,
                                           'forced_charge_time_start5': None,
                                           'forced_charge_time_start6': None,
                                           'forced_charge_time_stop1': datetime.time(23, 59),
                                           'forced_charge_time_stop2': datetime.time(0, 0),
                                           'forced_charge_time_stop3': datetime.time(0, 0),
                                           'forced_charge_time_stop4': None,
                                           'forced_charge_time_stop5': None,
                                           'forced_charge_time_stop6': None,
                                           'forced_discharge_stop_switch4': False,
                                           'forced_discharge_stop_switch5': False,
                                           'forced_discharge_stop_switch6': False,
                                           'forced_discharge_time_start1': datetime.time(0, 0),
                                           'forced_discharge_time_start2': datetime.time(0, 0),
                                           'forced_discharge_time_start3': datetime.time(0, 0),
                                           'forced_discharge_time_start4': None,
                                           'forced_discharge_time_start5': None,
                                           'forced_discharge_time_start6': None,
                                           'forced_discharge_time_stop1': datetime.time(23, 59),
                                           'forced_discharge_time_stop2': datetime.time(0, 0),
                                           'forced_discharge_time_stop3': datetime.time(0, 0),
                                           'forced_discharge_time_stop4': None,
                                           'forced_discharge_time_stop5': None,
                                           'forced_discharge_time_stop6': None,
                                           'fw_version': 'RH1.0',
                                           'grid_first_switch1': True,
                                           'grid_first_switch2': False,
                                           'grid_first_switch3': False,
                                           'group_id': -1,
                                           'id': 0,
                                           'img_path': './css/img/status_gray.gif',
                                           'inner_version': 'rHBA020202',
                                           'inv_version': 0,
                                           'last_update_time': 1558437021000,
                                           'last_update_time_text': datetime.datetime(2019, 5, 21, 19, 10, 21),
                                           'lcd_language': 1,
                                           'level': 4,
                                           'load_first_start_time1': datetime.time(0, 40),
                                           'load_first_start_time2': datetime.time(0, 0),
                                           'load_first_start_time3': datetime.time(0, 30),
                                           'load_first_stop_time1': datetime.time(0, 49),
                                           'load_first_stop_time2': datetime.time(0, 9),
                                           'load_first_stop_time3': datetime.time(0, 39),
                                           'load_first_switch1': False,
                                           'load_first_switch2': False,
                                           'load_first_switch3': False,
                                           'location': None,
                                           'lost': True,
                                           'manufacturer': '   New Energy   ',
                                           'mc_version': None,
                                           'modbus_version': 305,
                                           'model': 1814994400000,
                                           'model_text': 'A0B1D1T4PFU2M3S8',
                                           'monitor_version': None,
                                           'new_sw_version_flag': 0,
                                           'off_grid_discharge_soc': 0.0,
                                           'old_error_flag': 0,
                                           'on_off': True,
                                           'p_charge': 0.0,
                                           'p_discharge': 0.0,
                                           'parent_id': 'LIST_BQC0733006_96',
                                           'pf_cmd_memory_state': 0,
                                           'pf_sys_year': None,
                                           'plant_id': 0,
                                           'plant_name': None,
                                           'pmax': 3680,
                                           'port_name': 'ShinePano - BQC0733006',
                                           'power_factor': 20000.0,
                                           'power_max': None,
                                           'power_max_text': None,
                                           'power_max_time': None,
                                           'priority_choose': 2,
                                           'pro_pto': 0.0,
                                           'pv_active_p_rate': None,
                                           'pv_grid_voltage_high': None,
                                           'pv_grid_voltage_low': None,
                                           'pv_on_off': None,
                                           'pv_pf_cmd_memory_state': None,
                                           'pv_power_factor': None,
                                           'pv_reactive_p_rate': None,
                                           'pv_reactive_p_rate_two': None,
                                           'reactive_p_rate': 100,
                                           'record': None,
                                           'region': 0,
                                           'safety_correspond_num': 0,
                                           'safety_version': 0,
                                           'serial_num': 'CHENYINSHU',
                                           'spa_ac_discharge_frequency': None,
                                           'spa_ac_discharge_voltage': None,
                                           'spa_off_grid_enable': None,
                                           'status': -1,
                                           'status_text': 'spa.status.lost',
                                           'sys_time': datetime.datetime(2019, 5, 21, 16, 19),
                                           'sys_time_text': datetime.datetime(2019, 5, 21, 16, 19, 22),
                                           'tcp_server_ip': '192.168.3.35',
                                           'timezone': 8.0,
                                           'tree_id': 'ST_CHENYINSHU',
                                           'tree_name': 'CHENYINSHU',
                                           'under_excited': 0,
                                           'updating': False,
                                           'ups_freq_set': 0.0,
                                           'user_name': None,
                                           'vac_high': 262.2,
                                           'vac_low': 184.0,
                                           'vbat_start_for_charge': 57.6,
                                           'vbat_start_for_discharge': 44.0,
                                           'vbat_stop_for_charge': 5.75,
                                           'vbat_stop_for_discharge': 4.7,
                                           'vbat_warn_clr': 5.0,
                                           'vbat_warning': 440.0,
                                           'vpp_open': 0.0,
                                           'w_charge_soc_low_limit1': 100,
                                           'w_charge_soc_low_limit2': 100,
                                           'w_discharge_soc_low_limit1': 100,
                                           'w_discharge_soc_low_limit2': 10,
                                           'w_load_soc_low_limit1': 0,
                                           'w_load_soc_low_limit2': 0}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.details(
            device_sn=self._device_sn(device_sn),
            device_type=DeviceType.SPA,
        )

    def energy(
        self,
        device_sn: Optional[str] = None,
    ) -> SpaEnergyOverview:
        """
        Get the latest real-time data from Spa
        Access to the latest real-time data of Spa
        https://www.showdoc.com.cn/262556420217021/6129794031492135

        Note:
            Only applicable to devices with device type 6 (spa) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: Mix does not exist
        * 10003: device SN error

        Args:
            device_sn (str): SPA serial number

        Returns:
            SpaEnergyOverview
        """

        response = self.session.post(
            endpoint="device/spa/spa_last_data",
            data={
                "spa_sn": self._device_sn(device_sn),
            },
        )

        return SpaEnergyOverview.model_validate(response)

    def energy_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
    ) -> SpaEnergyV4:
        """
        Batch equipment data information using "new-api" endpoint
        Retrieve the last detailed data for multiple devices based on their SN and device type.
        https://www.showdoc.com.cn/2540838290984246/11292915898375566

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)

        Returns:
            SpaEnergyV4
            e.g.
            {   'data': {   'spa': [   {   'ac_charge_energy_today': 0.0,
                                           'ac_charge_energy_total': 8.3,
                                           'ac_charge_power': 0.0,
                                           'acc_charge_pack_sn': 0,
                                           'acc_charge_power': 0.0,
                                           'acc_discharge_pack_sn': 0,
                                           'acc_discharge_power': 0.0,
                                           'address': 0,
                                           'again': False,
                                           'alias': None,
                                           'b_module_num': 0,
                                           'b_total_cell_num': 0,
                                           'batt_history_fault_code1': 0,
                                           'batt_history_fault_code2': 0,
                                           'batt_history_fault_code3': 0,
                                           'batt_history_fault_code4': 0,
                                           'batt_history_fault_code5': 0,
                                           'batt_history_fault_code6': 0,
                                           'batt_history_fault_code7': 0,
                                           'batt_history_fault_code8': 0,
                                           'battery_temperature': 0.0,
                                           'battery_type': 1,
                                           'bms_battery_curr': 0.0,
                                           'bms_battery_temp': 0.0,
                                           'bms_battery_volt': 0.0,
                                           'bms_cell10_volt': 0.0,
                                           'bms_cell11_volt': 0.0,
                                           'bms_cell12_volt': 0.0,
                                           'bms_cell13_volt': 0.0,
                                           'bms_cell14_volt': 0.0,
                                           'bms_cell15_volt': 0.0,
                                           'bms_cell16_volt': 0.0,
                                           'bms_cell1_volt': 0.0,
                                           'bms_cell2_volt': 0.0,
                                           'bms_cell3_volt': 0.0,
                                           'bms_cell4_volt': 0.0,
                                           'bms_cell5_volt': 0.0,
                                           'bms_cell6_volt': 0.0,
                                           'bms_cell7_volt': 0.0,
                                           'bms_cell8_volt': 0.0,
                                           'bms_cell9_volt': 0.0,
                                           'bms_constant_volt': 0.0,
                                           'bms_cycle_cnt': 0,
                                           'bms_delta_volt': 0.0,
                                           'bms_error': 0,
                                           'bms_error2': 0,
                                           'bms_error3': 0,
                                           'bms_error_old': 0,
                                           'bms_fw': 0,
                                           'bms_gauge_fcc': 0.0,
                                           'bms_gauge_rm': 0.0,
                                           'bms_hardware_version': 0,
                                           'bms_hardware_version2': 0,
                                           'bms_highest_soft_version': 0,
                                           'bms_info': 0,
                                           'bms_max_curr': 0.0,
                                           'bms_max_dischg_curr': 0.0,
                                           'bms_mcu_version': 0,
                                           'bms_pack_info': 0,
                                           'bms_request_type': 0,
                                           'bms_soc': 0,
                                           'bms_soh': 0,
                                           'bms_status': 0,
                                           'bms_status_old': 0,
                                           'bms_using_cap': 0,
                                           'bms_warn_info': 0,
                                           'bms_warn_info_old': 0,
                                           'calendar': 1716435473718,
                                           'datalogger_sn': 'XGD6CMM2VY',
                                           'day': None,
                                           'day_map': None,
                                           'device_sn': 'MTN0H6800E',
                                           'e_to_grid_today': 0.0,
                                           'e_to_grid_total': 1.0,
                                           'e_to_user_today': 0.0,
                                           'e_to_user_total': 0.0,
                                           'eac_today': 0.0,
                                           'eac_total': 6.5,
                                           'echarge1_today': 0.0,
                                           'echarge1_total': 7.6,
                                           'edischarge1_today': 0.0,
                                           'edischarge1_total': 6.8,
                                           'elocal_load_today': 0.0,
                                           'elocal_load_total': 0.0,
                                           'epv_inverter_today': 0.0,
                                           'epv_inverter_total': 0.0,
                                           'error_code': 0,
                                           'error_text': 'Unknown',
                                           'eself_today': 0.0,
                                           'eself_total': 5.9,
                                           'esystem_today': None,
                                           'esystem_total': None,
                                           'fac': 49.99,
                                           'fault_bit_code': 0,
                                           'fault_code': 0,
                                           'first_batt_fault_sn': 0,
                                           'fourth_batt_fault_sn': 0,
                                           'iac1': 0.0,
                                           'iac2': 0.0,
                                           'iac3': 0.0,
                                           'lost': True,
                                           'max_soc': 0.0,
                                           'min_soc': 0.0,
                                           'module_series_qty': 0,
                                           'monitor': 1,
                                           'number_of_batt_codes': 0,
                                           'pac': 0.3,
                                           'pac1': 0.0,
                                           'pac_r': 0.0,
                                           'pac_s': 0.0,
                                           'pac_t': 0.0,
                                           'pac_to_grid_r': 0.0,
                                           'pac_to_grid_total': 0.0,
                                           'pac_to_user_r': 0.0,
                                           'pac_to_user_total': 0.0,
                                           'pcharge1': 0.0,
                                           'pdischarge1': 0.0,
                                           'plocal_load_r': 0.0,
                                           'plocal_load_r2': 0.0,
                                           'plocal_load_s': 0.0,
                                           'plocal_load_t': 0.0,
                                           'plocal_load_total': 0.0,
                                           'pm_r': 0.0,
                                           'pm_s': 0.0,
                                           'pm_t': 0.0,
                                           'ppv_inverter': 0.0,
                                           'priority_choose': 2.0,
                                           'protect_pack_id': 0,
                                           'pself': 0.0,
                                           'psystem': 0.0,
                                           'second_batt_fault_sn': 0,
                                           'soc': 0.0,
                                           'soc_text': '0%',
                                           'spa_bean': None,
                                           'status': 9,
                                           'status_text': 'Bypass',
                                           'sys_en': 20992,
                                           'sys_fault_word': 0,
                                           'sys_fault_word1': 0,
                                           'sys_fault_word2': 0,
                                           'sys_fault_word3': 33280,
                                           'sys_fault_word4': 0,
                                           'sys_fault_word5': 0,
                                           'sys_fault_word6': 0,
                                           'sys_fault_word7': 4,
                                           'temp1': 28.300001,
                                           'temp2': 26.7,
                                           'temp3': 27.7,
                                           'third_batt_fault_sn': 0,
                                           'time': datetime.datetime(2024, 5, 23, 11, 37, 53),
                                           'time_total': 265549.0,
                                           'ups_fac': 0.0,
                                           'ups_iac1': 0.0,
                                           'ups_iac2': 0.0,
                                           'ups_iac3': 0.0,
                                           'ups_load_percent': 0.0,
                                           'ups_pac1': 0.0,
                                           'ups_pac2': 0.0,
                                           'ups_pac3': 0.0,
                                           'ups_pf': 1000.0,
                                           'ups_vac1': 225.4,
                                           'ups_vac2': 0.0,
                                           'ups_vac3': 0.0,
                                           'uw_dsp_dc_dc_debug_data': 0,
                                           'uw_dsp_dc_dc_debug_data1': 0,
                                           'uw_dsp_dc_dc_debug_data2': 0,
                                           'uw_dsp_dc_dc_debug_data3': 0,
                                           'uw_dsp_dc_dc_debug_data4': 0,
                                           'uw_dsp_inv_debug_data': 0,
                                           'uw_dsp_inv_debug_data1': 0,
                                           'uw_dsp_inv_debug_data2': 0,
                                           'uw_dsp_inv_debug_data3': 0,
                                           'uw_dsp_inv_debug_data4': 0,
                                           'uw_max_cell_vol': 0.0,
                                           'uw_max_tempr_cell': 0.0,
                                           'uw_max_tempr_cell_no': 0,
                                           'uw_max_volt_cell_no': 0,
                                           'uw_min_cell_vol': 0.0,
                                           'uw_min_tempr_cell': 0.0,
                                           'uw_min_tempr_cell_no': 0,
                                           'uw_min_volt_cell_no': 0,
                                           'uw_sys_work_mode': 9,
                                           'v_bat_dsp': 2.2,
                                           'v_bus1': 4.3,
                                           'v_bus2': 4.8,
                                           'vac1': 227.3,
                                           'vac2': 0.0,
                                           'vac3': 0.0,
                                           'vbat': 0.0,
                                           'warn_code': 0,
                                           'warn_text': 'Unknown',
                                           'with_time': False}]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy(device_sn=self._device_sn(device_sn), device_type=DeviceType.SPA)

    def energy_multiple(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        page: Optional[int] = None,
    ) -> SpaEnergyOverviewMultiple:
        """
        Get the latest real-time data of Spa in batches
        Interface to obtain the latest real-time data of inverters in batches
        https://www.showdoc.com.cn/262556420217021/6138369063488649

        Note:
            Only applicable to devices with device type 6 (spa) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: System error
        * 10002: Device serial number error
        * 10003: Date format error
        * 10004: Date interval exceeds seven days
        * 10005: Spa does not exist

        Args:
            device_sn (Union[str, List[str]]): SPA serial number or list of (multiple) SPA serial numbers (max 100)
            page (Optional[int]): page number, default 1, max 2

        Returns:
            SpaEnergyOverviewMultiple
            {   'data': [   {   'data': {   'ac_charge_energy_today': 3.5999999046325684,
                                            'ac_charge_energy_total': 1305.5,
                                            'ac_charge_power': 0.0,
                                            'address': 0,
                                            'again': False,
                                            'alias': None,
                                            'battery_temperature': 36.900001525878906,
                                            'battery_type': 1,
                                            'bms_battery_curr': -9.390000343322754,
                                            'bms_battery_temp': 36.0,
                                            'bms_battery_volt': 53.099998474121094,
                                            'bms_cell10_volt': 3.316999912261963,
                                            'bms_cell11_volt': 3.315999984741211,
                                            'bms_cell12_volt': 3.315000057220459,
                                            'bms_cell13_volt': 3.316999912261963,
                                            'bms_cell14_volt': 3.316999912261963,
                                            'bms_cell15_volt': 3.315999984741211,
                                            'bms_cell16_volt': 3.318000078201294,
                                            'bms_cell1_volt': 3.318000078201294,
                                            'bms_cell2_volt': 0.0020000000949949026,
                                            'bms_cell3_volt': 3.315999984741211,
                                            'bms_cell4_volt': 3.316999912261963,
                                            'bms_cell5_volt': 3.316999912261963,
                                            'bms_cell6_volt': 3.316999912261963,
                                            'bms_cell7_volt': 3.318000078201294,
                                            'bms_cell8_volt': 3.315999984741211,
                                            'bms_cell9_volt': 3.316999912261963,
                                            'bms_constant_volt': 56.79999923706055,
                                            'bms_cycle_cnt': 100,
                                            'bms_delta_volt': 3.0,
                                            'bms_error': 0,
                                            'bms_error_old': 0,
                                            'bms_fw': 70,
                                            'bms_gauge_fcc': 232.0,
                                            'bms_gauge_rm': 243.27999877929688,
                                            'bms_info': 0,
                                            'bms_max_curr': 0.0,
                                            'bms_max_dischg_curr': 170.0,
                                            'bms_mcu_version': 70,
                                            'bms_pack_info': 0,
                                            'bms_soc': 98,
                                            'bms_soh': 100,
                                            'bms_status': 291,
                                            'bms_status_old': 0,
                                            'bms_using_cap': 0,
                                            'bms_warn_info': 0,
                                            'bms_warn_info_old': 0,
                                            'calendar': {   'first_day_of_week': 1,
                                                            'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                            'lenient': True,
                                                            'minimal_days_in_first_week': 1,
                                                            'time': {'date': 11, 'day': 1, 'hours': 15, 'minutes': 43, 'month': 0, 'seconds': 42, 'time': 1610351022000, 'timezone_offset': -480, 'year': 121},
                                                            'time_in_millis': 1610351022000,
                                                            'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                            'week_date_supported': True,
                                                            'week_year': 2021,
                                                            'weeks_in_week_year': 52},
                                            'datalogger_sn': None,
                                            'day': None,
                                            'day_map': None,
                                            'e_to_grid_today': 7.1,
                                            'e_to_grid_total': 1493.6,
                                            'e_to_user_today': 0.0,
                                            'e_to_user_total': 198.5,
                                            'eac_today': 1.5,
                                            'eac_total': 989.1,
                                            'echarge1_today': 3.3,
                                            'echarge1_total': 1195.9,
                                            'edischarge1_today': 1.8,
                                            'edischarge1_total': 1103.4,
                                            'elocal_load_today': 4.1,
                                            'elocal_load_total': 1972.2,
                                            'epv_inverter_today': 13.2,
                                            'epv_inverter_total': 3390.3,
                                            'error_code': -1,
                                            'error_text': 'Unknown',
                                            'fac': 50.029998779296875,
                                            'fault_bit_code': -1,
                                            'fault_code': -1,
                                            'lost': True,
                                            'pac': 430.4,
                                            'pac1': 418.3,
                                            'pac_to_grid_r': 21.5,
                                            'pac_to_grid_total': 21.5,
                                            'pac_to_user_r': 0.0,
                                            'pac_to_user_total': 0.0,
                                            'pcharge1': 0.0,
                                            'pdischarge1': 521.2,
                                            'plocal_load_r': 913.1,
                                            'plocal_load_total': 0.0,
                                            'ppv_inverter': 478.4,
                                            'priority_choose': 0.0,
                                            'serial_num': 'BKE4A02004',
                                            'soc': 98.0,
                                            'soc_text': '98%',
                                            'spa_bean': None,
                                            'status': 6,
                                            'status_text': 'Bat Online',
                                            'sys_en': -1,
                                            'sys_fault_word': 0,
                                            'sys_fault_word1': 0,
                                            'sys_fault_word2': 0,
                                            'sys_fault_word3': 0,
                                            'sys_fault_word4': 0,
                                            'sys_fault_word5': 0,
                                            'sys_fault_word6': 0,
                                            'sys_fault_word7': 256,
                                            'temp1': 37.0,
                                            'temp2': 35.0,
                                            'time': datetime.datetime(2021, 1, 11, 15, 43, 42),
                                            'time_total': -0.5,
                                            'ups_fac': 0.0,
                                            'ups_load_percent': 0.0,
                                            'ups_pac1': 0.0,
                                            'ups_pf': 1000.0,
                                            'ups_vac1': 0.0,
                                            'uw_sys_work_mode': 6,
                                            'v_bat_dsp': 53.20000076293945,
                                            'v_bus1': 393.0,
                                            'v_bus2': 300.0,
                                            'vac1': 243.0,
                                            'vbat': 52.79999923706055,
                                            'warn_code': -1,
                                            'warn_text': 'Unknown',
                                            'with_time': False},
                                'datalogger_sn': 'NAC591706C',
                                'device_sn': 'BKE4A02004'},
                            {   'data': {   'ac_charge_energy_today': 9.899999618530273,
                                            #...
                                            'with_time': False},
                                'datalogger_sn': 'NAC59170BA',
                                'device_sn': 'BKE192500D'}],
                'error_code': 0,
                'error_msg': None,
                'page_num': 1}
        """

        device_sn = self._device_sn(device_sn)
        if isinstance(device_sn, list):
            assert len(device_sn) <= 100, "Max 100 devices per request"
            device_sn = ",".join(device_sn)

        response = self.session.post(
            endpoint="device/spa/spas_data",
            data={
                "spas": device_sn,
                "pageNum": page or 1,
            },
        )

        # Unfortunately, the original response cannot be parsed by pydantic as the inverter_sn is used as key
        # To fix this, resulting data is restructured
        devices = [
            SpaEnergyOverviewMultipleItem(
                device_sn=inverter_sn,
                datalogger_sn=response.get("data", {}).get(inverter_sn, {}).get("dataloggerSn", None),
                data=response.get("data", {}).get(inverter_sn, {}).get(inverter_sn, None),
            )
            for inverter_sn in response.get("spas", [])
        ]
        response.pop("spas", None)
        response["data"] = devices

        return SpaEnergyOverviewMultiple.model_validate(response)

    def energy_history(
        self,
        device_sn: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> SpaEnergyHistory:
        """
        Get historical data of a spa
        Interface to get historical data of a spa
        https://www.showdoc.com.cn/262556420217021/6129802729032136

        Note:
            Only applicable to devices with device type 6 (spa) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: System error
        * 10002: Device serial number error
        * 10003: Date format error
        * 10004: Date interval exceeds seven days
        * 10005: Spa does not exist

        Args:
            device_sn (str): SPA serial number
            start_date (Optional[date]): Start Date - defaults to today
            end_date (Optional[date]): End Date (date interval cannot exceed 7 days) - defaults to today
            timezone (Optional[str]): The time zone code of the data display, the default is UTC
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            SpaEnergyHistory
            {   'data': {   'count': 3662,
                            'datalogger_sn': 'JPC2827188',
                            'datas': [   {   'ac_charge_energy_today': 0.0,
                                             'ac_charge_energy_total': 35.900001525878906,
                                             'ac_charge_power': 0.0,
                                             'address': 0,
                                             'again': False,
                                             'alias': None,
                                             'battery_temperature': 26.299999237060547,
                                             'battery_type': 0,
                                             'bms_battery_curr': 0.0,
                                             'bms_battery_temp': 0.0,
                                             'bms_battery_volt': 0.0,
                                             'bms_cell10_volt': 0.0,
                                             'bms_cell11_volt': 0.0,
                                             'bms_cell12_volt': 0.0,
                                             'bms_cell13_volt': 0.0,
                                             'bms_cell14_volt': 0.0,
                                             'bms_cell15_volt': 0.0,
                                             'bms_cell16_volt': 0.0,
                                             'bms_cell1_volt': 0.0,
                                             'bms_cell2_volt': 0.0,
                                             'bms_cell3_volt': 0.0,
                                             'bms_cell4_volt': 0.0,
                                             'bms_cell5_volt': 0.0,
                                             'bms_cell6_volt': 0.0,
                                             'bms_cell7_volt': 0.0,
                                             'bms_cell8_volt': 0.0,
                                             'bms_cell9_volt': 0.0,
                                             'bms_constant_volt': 0.0,
                                             'bms_cycle_cnt': 0,
                                             'bms_delta_volt': 0.0,
                                             'bms_error': 0,
                                             'bms_error_old': 0,
                                             'bms_fw': 0,
                                             'bms_gauge_fcc': 0.0,
                                             'bms_gauge_rm': 0.0,
                                             'bms_info': 0,
                                             'bms_max_curr': 0.0,
                                             'bms_max_dischg_curr': 0.0,
                                             'bms_mcu_version': 0,
                                             'bms_pack_info': 0,
                                             'bms_soc': 0,
                                             'bms_soh': 0,
                                             'bms_status': 0,
                                             'bms_status_old': 0,
                                             'bms_using_cap': 0,
                                             'bms_warn_info': 0,
                                             'bms_warn_info_old': 0,
                                             'calendar': {   'first_day_of_week': 1,
                                                             'gregorian_change': {'date': 15, 'day': 5, 'hours': 8, 'minutes': 0, 'month': 9, 'seconds': 0, 'time': -12219292800000, 'timezone_offset': -480, 'year': -318},
                                                             'lenient': True,
                                                             'minimal_days_in_first_week': 1,
                                                             'time': {'date': 19, 'day': 3, 'hours': 16, 'minutes': 3, 'month': 11, 'seconds': 4, 'time': 1545206584000, 'timezone_offset': -480, 'year': 118},
                                                             'time_in_millis': 1545206584000,
                                                             'time_zone': {'dirty': False, 'display_name': 'China Standard Time', 'dst_savings': 0, 'id': 'Asia/Shanghai', 'last_rule_instance': None, 'raw_offset': 28800000},
                                                             'week_date_supported': True,
                                                             'week_year': 2018,
                                                             'weeks_in_week_year': 52},
                                             'datalogger_sn': None,
                                             'day': None,
                                             'day_map': None,
                                             'e_to_grid_today': 0.2,
                                             'e_to_grid_total': 104.7,
                                             'e_to_user_today': 0.0,
                                             'e_to_user_total': 104.8,
                                             'eac_today': 5.099999904632568,
                                             'eac_total': 156.6,
                                             'echarge1_today': 0.0,
                                             'echarge1_total': 32.9,
                                             'edischarge1_today': 6.0,
                                             'edischarge1_total': 167.1,
                                             'elocal_load_today': 5.6,
                                             'elocal_load_total': 77.9,
                                             'epv_inverter_today': 0.6,
                                             'epv_inverter_total': 0.6,
                                             'error_code': -1,
                                             'error_text': 'Unknown',
                                             'fac': 50.02000045776367,
                                             'fault_bit_code': -1,
                                             'fault_code': -1,
                                             'lost': True,
                                             'pac': 2976.3,
                                             'pac1': 2976.6,
                                             'pac_to_grid_r': 9.4,
                                             'pac_to_grid_total': 9.4,
                                             'pac_to_user_r': 0.0,
                                             'pac_to_user_total': 0.0,
                                             'pcharge1': 0.0,
                                             'pdischarge1': 3083.0,
                                             'plocal_load_r': 2946.4,
                                             'plocal_load_total': 0.0,
                                             'ppv_inverter': 6.8,
                                             'priority_choose': 2.0,
                                             'serial_num': 'LHD0847002',
                                             'soc': 88.0,
                                             'soc_text': '88%',
                                             'spa_bean': None,
                                             'status': 6,
                                             'status_text': 'Bat Online',
                                             'sys_en': -1,
                                             'sys_fault_word': 0,
                                             'sys_fault_word1': 0,
                                             'sys_fault_word2': 0,
                                             'sys_fault_word3': 0,
                                             'sys_fault_word4': 0,
                                             'sys_fault_word5': 0,
                                             'sys_fault_word6': 0,
                                             'sys_fault_word7': 256,
                                             'temp1': 72.0,
                                             'temp2': 40.0,
                                             'time': datetime.datetime(2018, 12, 19, 16, 3, 4),
                                             'time_total': -0.5,
                                             'ups_fac': 0.0,
                                             'ups_load_percent': 0.0,
                                             'ups_pac1': 0.0,
                                             'ups_pf': 1000.0,
                                             'ups_vac1': 0.0,
                                             'uw_sys_work_mode': 6,
                                             'v_bat_dsp': 51.400001525878906,
                                             'v_bus1': 378.0,
                                             'v_bus2': 283.0,
                                             'vac1': 230.6999969482422,
                                             'vbat': 51.400001525878906,
                                             'warn_code': -1,
                                             'warn_text': 'Unknown',
                                             'with_time': False}],
                            'device_sn': 'LHD0847002',
                            'next_page_start_id': 21},
                'error_code': 0,
                'error_msg': None}
        """

        if start_date is None and end_date is None:
            start_date = date.today()
            end_date = date.today()
        elif start_date is None:
            start_date = end_date
        elif end_date is None:
            end_date = start_date

        # check interval validity
        if end_date - start_date >= timedelta(days=7):
            raise ValueError("date interval must not exceed 7 days")

        response = self.session.post(
            endpoint="device/spa/spa_data",
            data={
                "spa_sn": self._device_sn(device_sn),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "timezone_id": timezone,
                "page": page,
                "perpage": limit,
            },
        )

        return SpaEnergyHistory.model_validate(response)

    def energy_history_v4(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
    ) -> SpaEnergyHistoryV4:
        """
        One day data using "new-api" endpoint
        Retrieves all detailed data for a specific device on a particular day based on the device SN, device type, and date.
        https://www.showdoc.com.cn/2540838290984246/11292916022305414

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (str): Device unique serial number (SN)
            date_ (Optional[date]): Start Date - defaults to today

        Returns:
            SpaEnergyHistoryV4
            e.g.
            {   'data': {   'datas': [   {
                                             <see energy_v4() for attributes>
                                         }],
                            'have_next': False,
                            'start': 0},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}
        """

        return self._api_v4.energy_history(
            device_sn=self._device_sn(device_sn), device_type=DeviceType.SPA, date_=date_
        )

    def energy_history_multiple_v4(
        self,
        device_sn: Optional[Union[str, List[str]]] = None,
        date_: Optional[date] = None,
    ) -> SpaEnergyHistoryMultipleV4:
        """
        One day data using "new-api" endpoint
        Retrieves all detailed data for a specific device on a particular day based on the device SN, device type, and date.
        https://www.showdoc.com.cn/2540838290984246/11292916022305414

        Rate limit(s):
        * The retrieval frequency is once every 5 minutes.

        Args:
            device_sn (Union[str, List[str]]): Inverter serial number or list of (multiple) inverter serial numbers (max 100)
            date_ (Optional[date]): Start Date - defaults to today

        Returns:
            SpaEnergyHistoryMultipleV4
            e.g.
            {   'data': {   'NHB691514F': [   {
                                                  <see energy_v4() for attributes>
                                              }]},
                'error_code': 0,
                'error_msg': 'SUCCESSFUL_OPERATION'}

        """

        return self._api_v4.energy_history_multiple(
            device_sn=self._device_sn(device_sn), device_type=DeviceType.SPA, date_=date_
        )

    def alarms(
        self,
        device_sn: Optional[str] = None,
        date_: Optional[date] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> SpaAlarms:
        """
        Get alarm data of a spa
        Interface to get alarm data of a certain Spa
        https://www.showdoc.com.cn/262556420217021/6129804467339594

        Note:
            Only applicable to devices with device type 6 (spa) returned by plant.list_devices()

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: system error
        * 10002: device serial number error
        * 10003: date format error
        * 10005: spa does not exist

        Args:
            device_sn (str): SPA device serial number
            date_ (Optional[date]): Date - defaults to today
            page (Optional[int]): page number, default 1
            limit (Optional[int]): Number of items per page, default 20, max 100

        Returns:
            SpaAlarms
            e.g.
            {
                'data': {
                    'alarms': [
                        {
                            'alarm_code': 3,
                            'alarm_message': '',
                            'end_time': datetime.datetime(2018, 12, 17, 14, 5, 54),
                            'start_time': datetime.datetime(2018, 12, 17, 14, 5, 54),
                            'status': 1
                        }
                    ],
                    'count': 1,
                    'device_sn': 'LHD0847002'
                },
                'error_code': 0,
                'error_msg': None
            }
        """

        if date_ is None:
            date_ = date.today()

        response = self.session.post(
            endpoint="device/spa/alarm_data",
            data={
                "spa_sn": self._device_sn(device_sn),
                "date": date_.strftime("%Y-%m-%d"),
                "page": page,
                "perpage": limit,
            },
        )

        return SpaAlarms.model_validate(response)

    def soc(
        self,
        device_sn: Optional[str] = None,
    ) -> VppSoc:
        """
        Get machine SOC value (VPP)
        Get machine SOC value interface (only supports MIN SPA SPH models)
        https://www.showdoc.com.cn/262556420217021/7178565721512898

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: read failure
        * 10002: device does not exist
        * 10003: device serial number is empty

        Args:
            device_sn (str): VPP SN

        Returns:
            VppSoc
            {
                'error_code': 0,
                'error_msg': None,
                'soc': 65.0,
                'datalogger_sn': 'JPC5A11700',
                'device_sn': 'MIXECN6000'
            }
        """

        return self._api_vpp.soc(device_sn=self._device_sn(device_sn))

    def settings_write_vpp_now(
        self,
        time_: time,
        percentage: int,
        device_sn: Optional[str] = None,
    ) -> VppWrite:
        """
        Read the machine to perform battery charging contr
        The reading machine immediately executes the battery charging control interface (only supports MIN SPA SPH models)
        https://www.showdoc.com.cn/262556420217021/7178602212464389

        Note: this endpoint is poorly documented

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 500: Set Parameter Failure
        * 10001: Reading failed
        * 10012: Device does not exist
        * 10004: Device serial number is empty
        * 10005: Collector offline
        * 10007: Setting parameter is null
        * 10008: Setting value is out of range Or abnormal
        * 10009: The type of the read setting parameter does not exist
        * 10011: No permission

        Args:
            device_sn (str): VPP SN
            time_ (time): Set time - 00:00 ~ 24:00 (hh:mm),
            percentage (int): Set the power positive number for charging - negative number for discharge -100 ~ 100

        Returns:
            VppWrite
            {
                'error_code': 0,
                'error_msg': None,
                'data': 0,
            }
        """

        return self._api_vpp.write(
            device_sn=self._device_sn(device_sn),
            time_=time_,
            percentage=percentage,
        )

    def settings_write_vpp_schedule(
        self, schedules: List[Tuple[int, time, time]], device_sn: Optional[str] = None
    ) -> VppWrite:
        """
        Read and set VPP time period parameters (VPP)
        Read and set VPP time period parameter interface (only support MIN SPA SPH model)
        https://www.showdoc.com.cn/262556420217021/7178602212464389

        Note: this endpoint is poorly documented

        Rate limit(s):
        * The frequency of acquisition is once every 10 seconds

        Specific error codes:
        * 10001: Reading/Writing failed
        * 10012: Device does not exist
        * 10004: Device serial number is empty
        * 10005: Collector offline
        * 10007: Setting parameter is null
        * 10008: Setting value is out of range Or abnormal
        * 10009: The type of the read setting parameter does not exist
        * 10011: No permission

        Args:
            device_sn (str): VPP SN
            schedules (List[Tuple[int, time, time]]): Set time period
                Tuple with (power_percentage (int), start_time (time), end_time (time))
                percentage: positive number for charge 0 ~ 100, negative number for discharge -100 ~ 0
                e.g. [
                    (95, time(hour=0, minute=0), time(hour=5, minute=0)),    # 00:00 ~ 05:00 95% charge
                    (-60, time(hour=5, minute=1), time(hour=12, minute=0)),  # 05:01 ~ 12:00 60% discharge
                ]

        Returns:
            VppWrite
            {
                'error_code': 0,
                'error_msg': None,
                'data': 0,
            }
        """

        return self._api_vpp.write_multiple(device_sn=self._device_sn(device_sn), schedules=schedules)
