import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ReadConfig

global driver


@pytest.fixture()
def setup_teardown(request):
    global driver
    browser = ReadConfig.read_configuration("basic info", "browser")
    url = ReadConfig.read_configuration("basic info", "url")

    if browser:
        if browser.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox()
        else:
            pytest.fail(f"Invalid browser specified in config: {browser}")
    else:
        pytest.fail("Browser not specified in config")

    if url:
        driver.get(url)
    else:
        pytest.fail("URL not specified in config")

    driver.maximize_window()
    implicit_wait_time = ReadConfig.read_configuration("basic info", "implicit_wait", default=3)
    driver.implicitly_wait(implicit_wait_time)

    request.cls.driver = driver

    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
