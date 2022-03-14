import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from utilities import configreader


# To check for failures in the tests
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# To take screenshot of failed test cases
@pytest.fixture()
def log_on_failure(request, setup):
    yield
    item = request.node
    driver = setup
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(scope="function", autouse=True)
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(configreader.readConfig("basic info", "testURL"))
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
