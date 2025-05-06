import unittest

from growatt_public_api import User

TEST_FILE = "user.user"


# noinspection DuplicatedCode
class TestUser(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: User = None

    def test_check_username(self):
        raise NotImplementedError

    def test_list(self):
        raise NotImplementedError

    def test_modify(self):
        raise NotImplementedError

    def test_register(self):
        raise NotImplementedError
