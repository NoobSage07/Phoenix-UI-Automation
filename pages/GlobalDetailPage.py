from pages.BasePage import BasePage


class GlobalDetailPage(BasePage):
    job_detail_table_XPATH = "(//mat-table)[1]"
    customer_detail_table_XPATH = "(//mat-table)[2]"
    serviceLocation_Details_XPATH = "(//mat-table)[3]"
    problemReported_Details_XPATH = "(//mat-table)[4]"
    actionStatus_Details_XPATH = "(//mat-table)[5]"
    row_tag_name = "mat-row"
    cell_tag_name = "mat-cell"

    def job_Details(self):
        self.get_table_values("job_detail_table_XPATH", self.job_detail_table_XPATH, self.row_tag_name,
                              self.cell_tag_name)
        return self

    def customer_Details(self):
        self.get_table_values("customer_detail_table_XPATH", self.customer_detail_table_XPATH, self.row_tag_name,
                              self.cell_tag_name)
        return self

    def serviceLocation_Details(self):
        self.get_table_values("serviceLocation_Details_XPATH", self.serviceLocation_Details_XPATH, self.row_tag_name,
                              self.cell_tag_name)
        return self

    def problemReported_Details(self):
        self.get_table_values("problemReported_Details_XPATH", self.problemReported_Details_XPATH, self.row_tag_name,
                              self.cell_tag_name)
        return self

    def actionStatus_Details(self):
        self.get_table_values("actionStatus_Details_XPATH", self.actionStatus_Details_XPATH, self.row_tag_name,
                              self.cell_tag_name)
        return self
