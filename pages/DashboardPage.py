from pages.CreateJobPage import CreateJobPage
from pages.BasePage import BasePage
from pages.DownloadDeliveryNotesPage import DownloadDeliveryNotesPage
from pages.GlobalListPage import GlobalListPage


class DashboardPage(BasePage):
    # Menu
    dashboard_menu_XPATH = "//span[contains(text(), \" Dashboard \")]"
    createJob_menu_XPATH = "//span[contains(text(), 'Create Job')]"
    downloadDeliveryNotesPage_XPATH = "//a[@href='/frontdesk/download-delivery-note']"

    # Dashboard Count
    pending_4_delivery_XPATH = "//div[contains(text(), 'Pending for delivery')]/../div/button"
    created_today_XPATH = "//div[contains(text(),'Created today')]/../div/button"
    pending_4_FST_assignment_XPATH = "//div[contains(text(),'Pending for FST assignment')]/../div/button"
    table_XPATH = "//mat-table"
    row_tag_name = "mat-row"
    cell_tag_name = "mat-cell"

    # Search
    search_box_XPATH = "//input[@placeholder='Search for a Job or IMEI']"

    # user Info Button
    user_ICON = "(//button)[2]"
    user_NAME = "//span[contains(text(),'iamfd')]"

    def __init__(self, driver):
        super().__init__(driver)

    def pendingForDelivery_Status(self):
        self.element_click("pending_4_delivery_XPATH", self.pending_4_delivery_XPATH)
        # Printing Table
        self.get_table_values("table_XPATH", self.table_XPATH, self.row_tag_name, self.cell_tag_name)
        return self

    def createdToday_Status(self):
        self.element_click("created_today_XPATH", self.created_today_XPATH)
        # Printing Table
        self.get_table_values("table_XPATH", self.table_XPATH, self.row_tag_name, self.cell_tag_name)
        return self

    def gotoCreateJobPage(self):
        self.element_click("createJob_menu_XPATH", self.createJob_menu_XPATH)
        return CreateJobPage(self.driver)

    def gotoDownloadDeliveryNotePage(self):
        self.element_click("downloadDeliveryNotesPage_XPATH", self.downloadDeliveryNotesPage_XPATH)
        return DownloadDeliveryNotesPage(self.driver)

    def search_existing_jobs(self, jobNo_TEXT):
        self.type_into_element(jobNo_TEXT, "search_box_XPATH", self.search_box_XPATH)
        self.press_enter_key("search_box_XPATH", self.search_box_XPATH)
        return GlobalListPage

    def user_info(self):
        self.element_click("user_ICON", self.user_ICON)
        self.retrieve_element_text("user_NAME", self.user_NAME)
        print(self.retrieve_element_text("user_NAME", self.user_NAME))
