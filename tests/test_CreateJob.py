import time
from pages.CreateJobPage import CreateJobPage
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest

global driver


class Test_CreateJob(BaseTest):
    global driver

    def test_create_job(self):
        login_page = LoginPage(self.driver)
        login_page.fd_login("iamfd", "password")
        dash_board = DashboardPage(self.driver)
        dash_board.gotoCreateJobPage()
        time.sleep(1)
        create_job = CreateJobPage(self.driver)
        (create_job.selectOEM("Google").selectProductName("Nexus 2")
         .selectModelName(
            "Nexus 2 blue")
         .selectInWarrantyStatus("In Warrenty").selectProblem("Poor battery life")
         .enterIMEI(
            "12345431234567").enterDateOfPurchase("3/6/2024")
         .enterRemarks("Blabla").enterFirstName(
            "Mister")
         .enterLastName("Twister").enterContactNo("98097687777")
         .enterEmail("gucci@gang.com").enterFlatNo(
            "420")
         .enterApartmentNo("Earth").enterLandmark("land")
         .enterStreetName("Street").enterArea(
            "Area")
         .selectState("Delhi").enterPincode("110043")).submitJob()
        time.sleep(4)
