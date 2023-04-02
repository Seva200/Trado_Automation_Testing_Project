from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
class CommonActions:
    def __init__(self, driver):
        self.driver = driver

    def set_locator(self, locator):
        return wdw(self.driver, 5).until(ec.visibility_of_element_located(locator))
    def set_locator_invis(self, locator):
        return wdw(self.driver, 5).until(ec.frame_to_be_available_and_switch_to_it(locator))

    def click_on_locator(self, locator):
        return wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).click()
    def click_on_visible_locator_ac(self, locator):
        element = wdw(self.driver, 5).until(ec.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        action.click(element)
        action.perform()
    def click_on_invis_locator_ac(self, locator):
        element = wdw(self.driver, 5).until(ec.invisibility_of_element(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        action.click(element)
        action.perform()

    def double_click(self, locator):
        element = wdw(self.driver, 5).until(ec.invisibility_of_element(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        action.double_click(element)
        action.perform()

    def get_attribute_by(self, locator, method):
        attribute = wdw(self.driver, 5).until(ec.visibility_of_element_located(locator)).get_attribute(method)
        return attribute

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
