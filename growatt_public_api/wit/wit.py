import truststore


truststore.inject_into_ssl()
from session import GrowattApiSession  # noqa: E402


class Wit:
    """
    endpoints for WIT devices
    https://www.showdoc.com.cn/2540838290984246/11292927244927496
    """

    session: GrowattApiSession

    def __init__(self, session: GrowattApiSession) -> None:
        self.session = session
