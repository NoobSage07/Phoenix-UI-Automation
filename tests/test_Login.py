import time
import pytest
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils

global driver


class Test_Login(BaseTest):
    global driver

    @pytest.mark.parametrize("username,password",
                             ExcelUtils.get_data_from_excel("..//ExcelFiles/TutorialsNinja.xlsx", "LoginTest"))
    def test_valid_Login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.fd_login(username, password)
        time.sleep(2)

        # assertions

    def test_invalid_Login(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login("iamfd", "blabala")
        time.sleep(2)
        # assertions

    def test_blank_Login(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login(" ", " ")
        time.sleep(2)
        assert 1 == 2
        # assertions
