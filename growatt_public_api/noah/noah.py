import truststore


truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


class Noah:
    """
    endpoints for SPH-S devices
    https://www.showdoc.com.cn/2540838290984246/11292929153206911
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session
