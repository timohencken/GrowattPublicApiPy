import unittest

from growatt_public_api import Plant

TEST_FILE = "plant.plant"


# noinspection DuplicatedCode
class TestPlant(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: Plant = None

    def test_add(self):
        raise NotImplementedError

    def test_by_device(self):
        raise NotImplementedError

    def test_delete(self):
        raise NotImplementedError

    def test_details(self):
        raise NotImplementedError

    def test_energy_history(self):
        raise NotImplementedError

    def test_energy_overview(self):
        raise NotImplementedError

    def test_list(self):
        raise NotImplementedError

    def test_list_by_user(self):
        raise NotImplementedError

    def test_modify(self):
        raise NotImplementedError

    def test_power(self):
        raise NotImplementedError
