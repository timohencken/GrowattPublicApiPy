from typing import Optional, Self, Union

import truststore
from loguru import logger

from growatt_public_api import DeviceType

truststore.inject_into_ssl()

from session import GrowattApiSession  # noqa: E402
from user import User  # noqa: E402
from plant import Plant  # noqa: E402
from datalogger import Datalogger  # noqa: E402
from device import Device  # noqa: E402
from inverter import Inverter  # noqa: E402
from storage import Storage  # noqa: E402
from min import Min  # noqa: E402
from max import Max  # noqa: E402
from sph import Sph  # noqa: E402
from spa import Spa  # noqa: E402
from pcs import Pcs  # noqa: E402
from hps import Hps  # noqa: E402
from pbd import Pbd  # noqa: E402
from smart_meter import SmartMeter  # noqa: E402
from env_sensor import EnvSensor  # noqa: E402
from groboost import Groboost  # noqa: E402
from wit import Wit  # noqa: E402
from sphs import Sphs  # noqa: E402
from noah import Noah  # noqa: E402


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

    def __init__(
        self,
        token: str = None,
        server_url: Optional[str] = None,
    ) -> None:
        self.session = GrowattApiSession(token=token, server_url=server_url)
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
        self, device_sn: str
    ) -> Optional[Union[Groboost, Hps, Inverter, Max, Min, Noah, Pbd, Pcs, Spa, Sph, Sphs, Storage, Wit]]:
        """
        Get the API for a specific device.
        """
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
