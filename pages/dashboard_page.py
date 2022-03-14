import time

from selenium.webdriver.common.by import By

from pages.base_page import Base_page


class Dashboard(Base_page):
    def __init__(self, driver):
        self.driver = driver

    # locators
    TITLE_TEXT_XPATH = "//h1[normalize-space()='Dashboard']"

    # locator return function
    def get_title(self):
        return self.driver.find_element(By.XPATH, self.TITLE_TEXT_XPATH).text

    def validate_title(self, title):
        self.scroll_by_pixel()
        time.sleep(3)
        assert self.get_title() == title
