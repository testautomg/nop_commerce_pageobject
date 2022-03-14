import logging

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities import logger


class Login:
    log = logger.custom_logger(loglevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # locators
    USERNAME_FIELD_ID = "Email"
    PASSWORD_FIELD_ID = "Password"
    LOGIN_BUTTON_XPATH = "//button[@type='submit']"

    # locators return function
    def get_username_field(self):
        return self.driver.find_element(By.ID, self.USERNAME_FIELD_ID)

    def get_password_field(self):
        return self.driver.find_element(By.ID, self.PASSWORD_FIELD_ID)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.LOGIN_BUTTON_XPATH)

    def enter_username(self, username):
        self.get_username_field().clear()
        self.get_username_field().send_keys(username)
        self.log.info("Entered username")

    def enter_password(self, password):
        self.get_password_field().clear()
        self.get_password_field().send_keys(password)
        self.log.info("Entered password")

    def click_login_button(self):
        self.get_login_button().click()
        self.log.info("clicked login button")

    # main func
    def perform_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        # allure.attach(self.driver.get_screenshot_as_png(), name="Login_test", attachment_type=AttachmentType.PNG)
        self.click_login_button()
