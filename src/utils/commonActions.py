import time

from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
class CommonActions:
    def __init__(self, driver):
        self.driver = driver

    def set_locator(self, locator):
        return wdw(self.driver, 5).until(ec.visibility_of_element_located(locator))

    def click_on_locator(self, locator):
        return wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).click()
    def click_on_locator_ac(self, locator):
        element = wdw(self.driver, 5).until(ec.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click(on_element=element)
        action.perform()

    def get_attribute_by_innertext(self, locator):
        attribute = wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).get_attribute("innerText")
        return attribute
    def get_attribute_by_class(self, locator):
        attribute = wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).get_attribute("class")
        return attribute
    def get_attribute_by_id(self, locator):
        attribute = wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).get_attribute("id")
        return attribute
    def get_attribute_by_textcontent(self, locator):
        attribute = wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).get_attribute("textContent")
        return attribute

    def get_attribute_by_title(self, locator):
        attribute = wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).get_attribute("title")
        return attribute
    def get_attribute_by_value(self, locator):
        attribute = wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).get_attribute("value")
        return attribute
