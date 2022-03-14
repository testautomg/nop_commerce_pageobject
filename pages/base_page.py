from selenium.webdriver.common.by import By


class Base_page:
    def __init__(self, driver):
        self.driver = driver

    def scroll_by_pixel(self):
        self.driver.execute_script("window.scrollBy(0,1000)")

