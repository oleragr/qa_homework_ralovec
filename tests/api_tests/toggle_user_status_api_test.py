import pytest
from api.toggle_user_status_API import ToggleUserStatusAPI
from hamcrest import *

ACCOUNT_NR = '233223432432432'
MSISDN = '919825098250'


@pytest.mark.usefixtures("setUp")
class TestToggleUserStatusAPI:

    @pytest.fixture(autouse=True)
    def function_setup(self):
        print("Setting up test")
        self.toggle_user_status_api = ToggleUserStatusAPI()
        self.toggle_user_status_api.login("admin", "admin")
        self.toggle_user_status_api.toggle_user_status(ACCOUNT_NR, MSISDN, True)

    @pytest.mark.api
    def test_assign_limited_rights(self):
        self.toggle_user_status_api.login("admin", "admin")
        resp = self.toggle_user_status_api.toggle_user_status(ACCOUNT_NR, MSISDN, False)
        assert_that(resp.status_code == 200, 'User was not modified!')

        self.toggle_user_status_api.login('233223432432432', "233223432432432")
        resp = self.toggle_user_status_api.toggle_user_status(ACCOUNT_NR, MSISDN, True)
        assert_that(resp.status_code == 403, 'Status modified by user without permissions!')

    @pytest.mark.api
    def test_assign_admin_rights(self):
        self.toggle_user_status_api.login("admin", "admin")
        resp = self.toggle_user_status_api.toggle_user_status(ACCOUNT_NR, MSISDN, True)
        assert_that(resp.status_code == 200, 'User was not modified!')

        self.toggle_user_status_api.login('233223432432432', "233223432432432")
        resp = self.toggle_user_status_api.toggle_user_status(ACCOUNT_NR, MSISDN, False)
        assert_that(resp.status_code == 200, 'User was not modified!')

    @pytest.mark.api
    def test_assign_wrong_rights(self):
        self.toggle_user_status_api.login("admin", "admin")
        resp = self.toggle_user_status_api.toggle_user_status(ACCOUNT_NR, MSISDN, "WrongValue")
        assert_that(resp.status_code == 422, 'User was not modified!')
