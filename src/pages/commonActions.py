from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec

class CommonActions:
    def __init__(self, driver):
        self.driver = driver

    def set_locator(self, locator):
        return wdw(self.driver, 5).until(ec.visibility_of_element_located(locator))

    def click_on_locator(self, locator):
        return wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).click()

