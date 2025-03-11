from loguru import logger

from growatt_public_api import GrowattApi
from user.user import GrowattCountry

if __name__ == "__main__":
    logger.info("DEBUG")
    SERVER_URL = "https://test.growatt.com"
    # test token from official API docs https://www.showdoc.com.cn/262556420217021/1494053950115877
    API_TOKEN = "6eb6f069523055a339d71e5b1f6c88cc"  # gitleaks:allow

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

    # TODO API v4

    # user
    _user_list_ = ga.user.list(page=5, limit=100)
    _user_available_ = ga.user.check_username(username="DummyTestUser1")
    _user_available2_ = ga.user.check_username(username="DummyTestUser2")
    _user_modify_ = ga.user.modify(
        user_id=601,
        phone_number="01234567890123",
        installer_code="GWATT",
    )
    _user_register_ = ga.user.register(
        username="DummyTestUser1",
        password="DummyTestUser1pw",
        email="DummyTestUser1@example.com",
        country=GrowattCountry.JAPAN,
        user_type=1,
        installer_code="GWATT",
        phone_number="01234567890",
        time_zone="GMT+09:00",
    )
    # returned "c_user_id": 601

    logger.warning("DEBUG")
