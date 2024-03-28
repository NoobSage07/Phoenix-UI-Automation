from pages.BasePage import BasePage
from pages.GlobalDetailPage import GlobalDetailPage


class GlobalListPage(BasePage):
    table_XPATH = "//mat-table"
    row_tag_name = "mat-row"
    cell_tag_name = "mat-cell"
    existing_job_XPATH = "//button[contains(text(),'JOB_')]"

    def job_LIST(self):
        self.get_table_values("table_XPATH", self.table_XPATH, self.row_tag_name, self.cell_tag_name)
        return self

    def job_check(self):
        self.element_click("existing_job_XPATH", self.existing_job_XPATH)
        return GlobalDetailPage
