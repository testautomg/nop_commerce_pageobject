import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.dashboard_page import Dashboard
from pages.login_page import Login
from utilities import excel


class Test_NopCommerce:

    @pytest.mark.usefixtures("log_on_failure")
    # @pytest.mark.parametrize("usn,pwd", [("admin@yourstore.com", "admin"), ("test@youstore.com", "testing")])
    @pytest.mark.parametrize("usn,pwd", excel.get_data(
        "./testdata/Login inputs.xlsx", "Sheet1"))
    def test_verify_login(self, usn, pwd):
        lp = Login(self.driver)
        db = Dashboard(self.driver)
        lp.perform_login(usn, pwd)
        db.validate_title("Dashboard")

        # Added something from SDET1
        # added something to branch2
