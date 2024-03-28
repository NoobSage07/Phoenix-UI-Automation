from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest

global driver


class Test_Dashboard(BaseTest):
    global driver

    def test_pendingForDelivery_Status(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login("iamfd", "password")
        dash_board = DashboardPage(self.driver)
        dash_board.pendingForDelivery_Status()

    def test_createdToday_Status(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login("iamfd", "password")
        dash_board = DashboardPage(self.driver)
        dash_board.createdToday_Status()
