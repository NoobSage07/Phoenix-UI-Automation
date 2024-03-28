import time
from pages.DashboardPage import DashboardPage
from pages.GlobalDetailPage import GlobalDetailPage
from pages.GlobalListPage import GlobalListPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest

global driver


class Test_GlobalDetailPage(BaseTest):
    global driver

    def test_retrieve_list_element(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login("iamfd", "password")
        dashboard = DashboardPage(self.driver)
        dashboard.search_existing_jobs("JOB_28957")
        time.sleep(2)
        globalListPage = GlobalListPage(self.driver)
        globalListPage.job_check()
        time.sleep(2)
        globalDetailPage = GlobalDetailPage(self.driver)
        globalDetailPage.actionStatus_Details()
