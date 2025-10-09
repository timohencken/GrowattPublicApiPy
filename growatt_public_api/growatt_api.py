from typing import Optional, Self, Union
from loguru import logger
from .growatt_types import DeviceType
from .session.growatt_api_session import GrowattApiSession
from .user.user import User
from .plant.plant import Plant
from .datalogger.datalogger import Datalogger
from .device.device import Device
from .inverter.inverter import Inverter
from .storage.storage import Storage
from .min.min import Min
from .max.max import Max
from .sph.sph import Sph
from .spa.spa import Spa
from .pcs.pcs import Pcs
from .hps.hps import Hps
from .pbd.pbd import Pbd
from .smart_meter.smart_meter import SmartMeter
from .env_sensor.env_sensor import EnvSensor
from .groboost.groboost import Groboost
from .wit.wit import Wit
from .sphs.sphs import Sphs
from .noah.noah import Noah


class GrowattApi:
    session: GrowattApiSession
    _user: User = None
    _plant: Plant = None
    _datalogger: Datalogger = None
    _device: Device = None
    _inverter: Inverter = None
    _storage: Storage = None
    _min: Min = None
    _max: Max = None
    _sph: Sph = None
    _spa: Spa = None
    _pcs: Pcs = None
    _hps: Hps = None
    _pbd: Pbd = None
    _smart_meter: SmartMeter = None
    _env_sensor: EnvSensor = None
    _groboost: Groboost = None
    _wit: Wit = None
    _sphs: Sphs = None
    _noah: Noah = None

    """
    API documents:
    * v1 (full-featured API)
      https://www.showdoc.com.cn/262556420217021/0
    * v4 (new API with just a few endpoints)
      https://www.showdoc.com.cn/2540838290984246/0
    """

    def __init__(self, token: str, server_url: Optional[str] = None, use_cache: bool = True) -> None:
        """
        Initialize the GrowattApi with a session.

        :param token: The API token for authentication.
        :param server_url: The URL of the Growatt API server. If not provided, it defaults to the production server.
        :param use_cache: Cache requests to Growatt API to avoid 'API rate limit exceeded' errors.

        :raises AssertionError: If no token is provided.
        """
        assert token

        self.session = GrowattApiSession(token=token, server_url=server_url, use_cache=use_cache)

    @classmethod
    def using_test_server_v1(cls) -> Self:
        """
        Create a session using the test server
        """
        return cls(
            server_url="https://test.growatt.com",
            # test token from official API docs https://www.showdoc.com.cn/262556420217021/1494053950115877
            token="6eb6f069523055a339d71e5b1f6c88cc",  # gitleaks:allow
        )

    @classmethod
    def using_test_server_v4(cls) -> Self:
        """
        Create a session using the test server
        """
        return cls(
            server_url="http://183.62.216.35:8081",
            # test token from official API docs https://www.showdoc.com.cn/2540838290984246/11292912972201443
            token="wa265d2h1og0873ml07142r81564hho6",  # gitleaks:allow
        )

    # ##############################################################################
    # init specific apis on demand
    @property
    def user(self):
        if self._user is None:
            self._user = User(self.session)
        return self._user

    @property
    def plant(self):
        if self._plant is None:
            self._plant = Plant(self.session)
        return self._plant

    @property
    def datalogger(self):
        if self._datalogger is None:
            self._datalogger = Datalogger(self.session)
        return self._datalogger

    @property
    def device(self):
        if self._device is None:
            self._device = Device(self.session)
        return self._device

    @property
    def inverter(self):
        if self._inverter is None:
            self._inverter = Inverter(self.session)
        return self._inverter

    @property
    def storage(self):
        if self._storage is None:
            self._storage = Storage(self.session)
        return self._storage

    @property
    def min(self):
        if self._min is None:
            self._min = Min(self.session)
        return self._min

    @property
    def max(self):
        if self._max is None:
            self._max = Max(self.session)
        return self._max

    @property
    def sph(self):
        if self._sph is None:
            self._sph = Sph(self.session)
        return self._sph

    @property
    def spa(self):
        if self._spa is None:
            self._spa = Spa(self.session)
        return self._spa

    @property
    def pcs(self):
        if self._pcs is None:
            self._pcs = Pcs(self.session)
        return self._pcs

    @property
    def hps(self):
        if self._hps is None:
            self._hps = Hps(self.session)
        return self._hps

    @property
    def pbd(self):
        if self._pbd is None:
            self._pbd = Pbd(self.session)
        return self._pbd

    @property
    def smart_meter(self):
        if self._smart_meter is None:
            self._smart_meter = SmartMeter(self.session)
        return self._smart_meter

    @property
    def env_sensor(self):
        if self._env_sensor is None:
            self._env_sensor = EnvSensor(self.session)
        return self._env_sensor

    @property
    def groboost(self):
        if self._groboost is None:
            self._groboost = Groboost(self.session)
        return self._groboost

    @property
    def wit(self):
        if self._wit is None:
            self._wit = Wit(self.session)
        return self._wit

    @property
    def sphs(self):
        if self._sphs is None:
            self._sphs = Sphs(self.session)
        return self._sphs

    @property
    def noah(self):
        if self._noah is None:
            self._noah = Noah(self.session)
        return self._noah

    # ##############################################################################

    def api_for_device(  # noqa: C901 'GrowattApi.api_for_device' is too complex (14)
        self, device_sn: str, device_type: Optional[DeviceType] = None
    ) -> Optional[Union[Groboost, Hps, Inverter, Max, Min, Noah, Pbd, Pcs, Spa, Sph, Sphs, Storage, Wit]]:
        """
        Get the API for a specific device.

        :param device_sn: The serial number of the device.
        :param device_type: The type of the device. If not provided, it will be automatically determined from the device's serial number.
        """
        if device_type is None:
            device_type = self.device.get_device_type(device_sn)

        if device_type == DeviceType.GROBOOST:
            return Groboost(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.HPS:
            return Hps(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.INVERTER:
            return Inverter(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.MAX:
            return Max(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.MIN:
            return Min(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.NOAH:
            return Noah(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.PBD:
            return Pbd(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.PCS:
            return Pcs(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.SPA:
            return Spa(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.SPH:
            return Sph(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.SPHS:
            return Sphs(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.STORAGE:
            return Storage(session=self.session, device_sn=device_sn)
        elif device_type == DeviceType.WIT:
            return Wit(session=self.session, device_sn=device_sn)
        else:
            logger.error(f"Unknown device type: {device_type} for {device_sn=}")

        return None
