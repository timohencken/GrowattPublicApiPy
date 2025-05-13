from typing import Optional

import truststore

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
from vpp import Vpp  # noqa: E402
from sph import Sph  # noqa: E402
from spa import Spa  # noqa: E402
from pcs import Pcs  # noqa: E402
from hps import Hps  # noqa: E402
from pbd import Pbd  # noqa: E402
from smart_meter import SmartMeter  # noqa: E402
from env_sensor import EnvSensor  # noqa: E402
from groboost import Groboost  # noqa: E402
from api_v4 import ApiV4  # noqa: E402
from wit import Wit  # noqa: E402
from sphs import Sphs  # noqa: E402


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
    vpp: Vpp
    sph: Sph
    spa: Spa
    pcs: Pcs
    hps: Hps
    pbd: Pbd
    smart_meter: SmartMeter
    env_sensor: EnvSensor
    groboost: Groboost
    v4: ApiV4
    wit: Wit
    sphs: Sphs

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
        self.session = GrowattApiSession(token=token, server_url=server_url or "https://openapi.growatt.com")
        self.user = User(self.session)
        self.plant = Plant(self.session)
        self.datalogger = Datalogger(self.session)
        self.device = Device(self.session)
        self.inverter = Inverter(self.session)
        self.storage = Storage(self.session)
        self.min = Min(self.session)
        self.max = Max(self.session)
        self.vpp = Vpp(self.session)
        self.sph = Sph(self.session)
        self.spa = Spa(self.session)
        self.pcs = Pcs(self.session)
        self.hps = Hps(self.session)
        self.pbd = Pbd(self.session)
        self.smart_meter = SmartMeter(self.session)
        self.env_sensor = EnvSensor(self.session)
        self.groboost = Groboost(self.session)
        self.v4 = ApiV4(self.session)
        self.wit = Wit(self.session)
        self.sphs = Sphs(self.session)
