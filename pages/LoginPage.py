from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage


class LoginPage(BasePage):
    username_ID = "username"
    password_ID = "password"
    signButton_XPATH = "//span[contains(text(), ' Sign in ')]/../.."

    def __init__(self, driver):
        super().__init__(driver)

    def fd_login(self, username_TEXT, password_TEXT):
        self.type_into_element(username_TEXT, "username_ID", self.username_ID)
        self.type_into_element(password_TEXT, "password_ID", self.password_ID)
        self.element_click("signButton_XPATH", self.signButton_XPATH)
        return DashboardPage(self.driver)

