from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from selenium.webdriver.common.by import By
class TestWelcomeToModal(ChromeDriverSetUp):
    def test_X_btn(self, driver):
        assert driver.find_element(By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open").get_attribute("class") == "modal_modalWrapper false modal_open    "
        self.welcome_to_modal.x_btn_click()
        assert driver.find_element(By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_hide").get_attribute("class") == "modal_modalWrapper false   modal_hide  "

    def test_choose_interest(self, driver):
        assert driver.find_element(By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open").get_attribute("class") == "modal_modalWrapper false modal_open    "
        self.welcome_to_modal.choose_coktails()
        self.welcome_to_modal.save_btn_click()
        assert driver.find_element(By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_hide").get_attribute("class") == "modal_modalWrapper false   modal_hide  "


