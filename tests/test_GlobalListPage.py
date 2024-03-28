import time

from pages.DashboardPage import DashboardPage
from pages.GlobalListPage import GlobalListPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest

global driver


class TestGlobalListPage(BaseTest):
    global driver

    def test_searched_job_list(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login("iamfd", "password")
        dashboard = DashboardPage(self.driver)
        dashboard.search_existing_jobs("JOB_28957")

    def test_retrieve_list_element(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login("iamfd", "password")
        dashboard = DashboardPage(self.driver)
        dashboard.search_existing_jobs("JOB_28957")
        time.sleep(2)
        globalListPage = GlobalListPage(self.driver)
        globalListPage.job_LIST()
