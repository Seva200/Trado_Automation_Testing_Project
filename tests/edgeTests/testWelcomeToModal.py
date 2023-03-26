from src.utils.drivers.edgeDriverSetUp import EdgeDriverSetUp
from selenium.webdriver.common.by import By

class TestWelcomeToModal(EdgeDriverSetUp):
    def test_X_btn(self, driver):
        assert driver.find_element(By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open").get_attribute("class") == "modal_modalWrapper false modal_open    "
        self.welcome_to_modal.x_btn_click()
        assert driver.find_element(By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_hide").get_attribute("class") == "modal_modalWrapper false   modal_hide  "
