# import unittest
# from datetime import timedelta
# from unittest.mock import patch
#
# from api_v4 import ApiV4
# from growatt_public_api import GrowattApiSession
# from hps import Hps
# from min import Min
# from pydantic_models import MinDetails
# from pydantic_models.min import (
#     MinDetailData,
#     MinTlxSettingsData,
#     MinEnergyOverview,
#     MinEnergyHistory,
#     MinEnergyHistoryData,
#     MinEnergyOverviewData,
#     MinEnergyOverviewMultiple,
#     MinEnergyOverviewMultipleItem,
#     MinSettingRead,
#     MinSettingWrite,
#     MinSettings,
#     MinAlarms,
#     MinAlarmsData,
#     MinAlarm,
# )
#
#
# TEST_FILE = "hps.hps"
#
#
# # noinspection DuplicatedCode
# class TestMin(unittest.TestCase):
#     """
#     retrieve from API
#     compare to pydantic models
#     """
#
#     api: Hps = None
#     device_sn: str = None
#
#     @classmethod
#     def setUpClass(cls):
#         # init API
#         gas = GrowattApiSession(
#             # several min devices seen on v1 test server
#             # server_url="https://test.growatt.com",
#             # token="6eb6f069523055a339d71e5b1f6c88cc",  # gitleaks:allow
#             server_url="http://183.62.216.35:8081",
#             token="wa265d2h1og0873ml07142r81564hho6",  # gitleaks:allow
#         )
#         # init MIN
#         cls.api = Hps(session=gas)
#         # get a MIN device
#         try:
#             apiv4 = ApiV4(session=gas)
#             _devices = apiv4.list()
#             sn_list = [x.device_sn for x in _devices.data.data if x.device_type == "min"]
#             cls.device_sn = sn_list[0]
#         except AttributeError:
#             cls.device_sn = (
#                 "RUK0CAE00J"  # 'RUK0CAE00J', 'EVK0BHX111', 'GRT0010086', 'TAG1234567', 'YYX1235113', 'GRT1235003'
#             )
#
#     def test_alarms(self):
#         with patch(f"{TEST_FILE}.MinAlarms", wraps=MinAlarms) as mock_pyd_model:
#             self.api.alarms(device_sn=self.device_sn)
#
#         raw_data = mock_pyd_model.model_validate.call_args.args[0]
#
#         # check parameters are included in pydantic model
#         pydantic_keys = {v.alias for k, v in MinAlarms.model_fields.items()} | set(
#             MinAlarms.model_fields.keys()
#         )  # aliased and non-aliased params
#         for param in set(raw_data.keys()):
#             self.assertIn(param, pydantic_keys)
#         # check data
#         pydantic_keys = {v.alias for k, v in MinAlarmsData.model_fields.items()} | set(
#             MinAlarmsData.model_fields.keys()
#         )
#         self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
#         # check alarms
#         if raw_data["data"]["count"] == 0:
#             # if there are no alarms, there are no alarms
#             self.assertEqual([], raw_data["data"]["alarms"])
#         else:
#             # check alarms
#             pydantic_keys = {v.alias for k, v in MinAlarm.model_fields.items()} | set(MinAlarm.model_fields.keys())
#             self.assertEqual(
#                 set(), set(raw_data["data"]["alarms"][0].keys()).difference(pydantic_keys), "data_alarms_0"
#             )
#
#     def test_details(self):
#         with patch(f"{TEST_FILE}.MinDetails", wraps=MinDetails) as mock_pyd_model:
#             self.api.details(device_sn=self.device_sn)
#
#         raw_data = mock_pyd_model.model_validate.call_args.args[0]
#
#         # check parameters are included in pydantic model
#         pydantic_keys = {v.alias for k, v in MinDetails.model_fields.items()} | set(
#             MinDetails.model_fields.keys()
#         )  # aliased and non-aliased params
#         for param in set(raw_data.keys()):
#             self.assertIn(param, pydantic_keys)
#         # check data
#         pydantic_keys = {v.alias for k, v in MinDetailData.model_fields.items()} | set(
#             MinDetailData.model_fields.keys()
#         )
#         self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
#         # check SetBean
#         pydantic_keys = {v.alias for k, v in MinTlxSettingsData.model_fields.items()} | set(
#             MinTlxSettingsData.model_fields.keys()
#         )
#         self.assertEqual(set(), set(raw_data["data"]["tlxSetbean"].keys()).difference(pydantic_keys), "tlxSetbean")
#
#     def test_energy(self):
#         with patch(f"{TEST_FILE}.MinEnergyOverview", wraps=MinEnergyOverview) as mock_pyd_model:
#             self.api.energy(device_sn=self.device_sn)
#
#         raw_data = mock_pyd_model.model_validate.call_args.args[0]
#
#         # check parameters are included in pydantic model
#         pydantic_keys = {v.alias for k, v in MinEnergyOverview.model_fields.items()} | set(
#             MinEnergyOverview.model_fields.keys()
#         )  # aliased and non-aliased params
#         for param in set(raw_data.keys()):
#             self.assertIn(param, pydantic_keys)
#         # check data
#         pydantic_keys = {v.alias for k, v in MinEnergyOverviewData.model_fields.items()} | set(
#             MinEnergyOverviewData.model_fields.keys()
#         )
#         self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
#
#     def test_energy_history(self):
#         # get date with data
#         _details = self.api.details(device_sn=self.device_sn)
#         _last_ts = _details.data.last_update_time_text
#
#         with patch(f"{TEST_FILE}.MinEnergyHistory", wraps=MinEnergyHistory) as mock_pyd_model:
#             self.api.energy_history(
#                 device_sn=self.device_sn, start_date=_last_ts.date() - timedelta(days=6), end_date=_last_ts.date()
#             )
#
#         raw_data = mock_pyd_model.model_validate.call_args.args[0]
#
#         # check parameters are included in pydantic model
#         pydantic_keys = {v.alias for k, v in MinEnergyHistory.model_fields.items()} | set(
#             MinEnergyHistory.model_fields.keys()
#         )  # aliased and non-aliased params
#         for param in set(raw_data.keys()):
#             self.assertIn(param, pydantic_keys)
#         # check data
#         pydantic_keys = {v.alias for k, v in MinEnergyHistoryData.model_fields.items()} | set(
#             MinEnergyHistoryData.model_fields.keys()
#         )
#         self.assertEqual(set(), set(raw_data["data"].keys()).difference(pydantic_keys), "data")
#         # check datas
#         pydantic_keys = {v.alias for k, v in MinEnergyOverviewData.model_fields.items()} | set(
#             MinEnergyOverviewData.model_fields.keys()
#         )
#         self.assertEqual(set(), set(raw_data["data"]["datas"][0].keys()).difference(pydantic_keys), "data_datas_0")
#         # FAILS often as api.details() is called too frequently
