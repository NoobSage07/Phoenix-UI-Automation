from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest

global driver


class Test_DeliveryNote(BaseTest):
    global driver

    def test_job_search(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login("iamfd", "password")
        dash_board = DashboardPage(self.driver)
        dash_board.gotoDownloadDeliveryNotePage().search_JOB("JOB_28957")

    def test_delivery_note(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login("iamfd", "password")
        dash_board = DashboardPage(self.driver)
        dash_board.gotoDownloadDeliveryNotePage().search_JOB("JOB_28957").delivery_status("tr", "td")
