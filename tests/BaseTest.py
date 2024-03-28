from datetime import datetime

import pytest

from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown", "log_on_failure")
class BaseTest:
    @staticmethod
    def generate_email_with_time_stamp():
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "test" + time_stamp + "@gmail.com"

