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
    user: User
    plant: Plant
    datalogger: Datalogger
    device: Device
    inverter: Inverter
    storage: Storage
    min: Min
    max: Max
    sph: Sph
    spa: Spa
    pcs: Pcs
    hps: Hps
    pbd: Pbd
    smart_meter: SmartMeter
    env_sensor: EnvSensor
    groboost: Groboost
    wit: Wit
    sphs: Sphs
    noah: Noah

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
        self.user = User(self.session)
        self.plant = Plant(self.session)
        self.datalogger = Datalogger(self.session)
        self.device = Device(self.session)
        self.inverter = Inverter(self.session)
        self.storage = Storage(self.session)
        self.min = Min(self.session)
        self.max = Max(self.session)
        self.sph = Sph(self.session)
        self.spa = Spa(self.session)
        self.pcs = Pcs(self.session)
        self.hps = Hps(self.session)
        self.pbd = Pbd(self.session)
        self.smart_meter = SmartMeter(self.session)
        self.env_sensor = EnvSensor(self.session)
        self.groboost = Groboost(self.session)
        self.wit = Wit(self.session)
        self.sphs = Sphs(self.session)
        self.noah = Noah(self.session)

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
