import random
import string
import unittest
from unittest import skip
from unittest.mock import patch

from growatt_public_api import User, GrowattApiSession
from growatt_public_api.pydantic_models import UserList
from growatt_public_api.pydantic_models.user import UserListData, UserInfo, UsernameAvailabilityCheck, UserModification

TEST_FILE = "growatt_public_api.user.user"


# noinspection DuplicatedCode
class TestUser(unittest.TestCase):
    """
    retrieve from API
    compare to pydantic models
    """

    api: User = None

    @classmethod
    def setUpClass(cls):
        # init API
        gas = GrowattApiSession.using_test_server_v1()
        # init
        cls.api = User(session=gas)

    def test_check_username(self):
        # get list of users to determine a (non-)existing username
        existing_usernames = [x.name for x in self.api.list().data.users]

        # check for existing username
        with patch(f"{TEST_FILE}.UsernameAvailabilityCheck", wraps=UsernameAvailabilityCheck) as mock_pyd_model:
            result_exist = self.api.check_username(existing_usernames[0])
        self.assertFalse(result_exist.username_available, "username should not be available")

        # check non-existing username
        username = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        while username in existing_usernames:
            username = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        result_not_exist = self.api.check_username(username)
        self.assertTrue(result_not_exist.username_available, "username should be available")

        # check parameters are included in pydantic model
        raw_data = mock_pyd_model.model_validate.call_args.args[0]
        pydantic_keys = {v.alias for k, v in UsernameAvailabilityCheck.model_fields.items()} | set(
            UsernameAvailabilityCheck.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    def test_list(self):
        with patch(f"{TEST_FILE}.UserList", wraps=UserList) as mock_pyd_model:
            api_response = self.api.list()

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in UserList.model_fields.items()} | set(
            UserList.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")
        # check data
        pydantic_keys = {v.alias for k, v in UserListData.model_fields.items()} | set(UserListData.model_fields.keys())
        self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
        # check UserInfo
        if api_response.data.count == 0:
            # if there are no users, there are no users
            self.assertEqual([], raw_data["data"]["c_user"])
        else:
            # check alarms
            pydantic_keys = {v.alias for k, v in UserInfo.model_fields.items()} | set(UserInfo.model_fields.keys())
            self.assertEqual(set(), set(raw_data["data"]["c_user"][0].keys()).difference(pydantic_keys), "data_users_0")

    def test_modify(self):
        # get list of users
        existing_user_ids = [x.id for x in self.api.list().data.users]

        with patch(f"{TEST_FILE}.UserModification", wraps=UserModification) as mock_pyd_model:
            self.api.modify(user_id=existing_user_ids[0], phone_number="01234567890", installer_code="GWATT")

        raw_data = mock_pyd_model.model_validate.call_args.args[0]

        # check parameters are included in pydantic model
        pydantic_keys = {v.alias for k, v in UserModification.model_fields.items()} | set(
            UserModification.model_fields.keys()
        )  # aliased and non-aliased params
        self.assertEqual(set(), set(raw_data.keys()).difference(pydantic_keys), "root")

    @skip("Not tested as users cannot be deleted")
    def test_register(self):
        raise NotImplementedError
