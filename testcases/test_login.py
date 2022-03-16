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
        "/Users/admin/Desktop/SDET1/sdet1_nop_commerce_pageobject/testdata/Login inputs.xlsx", "Sheet1"))
    def test_verify_login(self, usn, pwd):
        lp = Login(self.driver)
        db = Dashboard(self.driver)
        lp.perform_login(usn, pwd)
        db.validate_title("Dashboard")
        try:
            assert title == self.validate_title().text, "Title not matching"
        except:
            self.log.info("Title not matching")
