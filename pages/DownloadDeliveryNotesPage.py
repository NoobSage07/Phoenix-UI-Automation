import time

from pages.BasePage import BasePage


class DownloadDeliveryNotesPage(BasePage):
    search_field_XPATH = "//input[@data-placeholder='Search Job']"
    submit_button_XPATH = "//span[contains(text(),' Submit ')]/.."
    signButton_XPATH = "//span[contains(text(), ' Submit ')]/../."
    table_XPATH = "//table"
    row_tag_name = "tr"
    cell_tag_name = "td"

    def __init__(self, driver):
        super().__init__(driver)

    def search_JOB(self, job_number_TEXT):
        self.type_into_element(job_number_TEXT, "search_field_XPATH", self.search_field_XPATH)
        self.element_click("submit_button_XPATH", self.submit_button_XPATH)
        time.sleep(2)
        return self

    def delivery_status(self, row_tag_name, cell_tag_name):
        self.get_table_values("table_XPATH", self.table_XPATH, row_tag_name, cell_tag_name)
        return self
