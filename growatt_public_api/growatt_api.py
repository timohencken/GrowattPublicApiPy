from enum import IntEnum
from typing import Optional

import truststore


truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402
from user import User  # noqa: E402
from plant import Plant  # noqa: E402
from device import Device  # noqa: E402
from inverter import Inverter  # noqa: E402
from storage import Storage  # noqa: E402
from min import Min  # noqa: E402
from max import Max  # noqa: E402
from vpp import Vpp  # noqa: E402
from sph import Sph  # noqa: E402
from spa import Spa  # noqa: E402


class GrowattDeviceType(IntEnum):
    inverter = 1  # (including MAX)
    storage = 2
    other = 3  # smart meter / environmental tester / vpp / groBoost
    max = 4
    sph = 5
    spa = 6  # MIX
    min = 7  # MIN / MAC / MOD-XH / MID-XH / NEO
    pcs = 8
    hps = 9
    pdb = 10
    gro_boost = 11
    # vpp: supported by min, spa, sph


class GrowattApi:
    session: GrowattApiSession
    user: User
    plant: Plant
    device: Device
    inverter: Inverter
    storage: Storage
    min: Min
    max: Max
    vpp: Vpp
    sph: Sph
    spa: Spa

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
        self.session = GrowattApiSession(
            token=token, server_url=server_url or "https://openapi.growatt.com"
        )
        self.user = User(self.session)
        self.plant = Plant(self.session)
        self.device = Device(self.session)
        self.inverter = Inverter(self.session)
        self.storage = Storage(self.session)
        self.min = Min(self.session)
        self.max = Max(self.session)
        self.vpp = Vpp(self.session)
        self.sph = Sph(self.session)
        self.spa = Spa(self.session)
