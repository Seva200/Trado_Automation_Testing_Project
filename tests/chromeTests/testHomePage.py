import time
from time import sleep
from src.pages.commonActions import CommonActions
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from selenium.webdriver.common.by import By

class TestHomePage(ChromeDriverSetUp):
# Header
    def test_logo_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.logo_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/"

    def test_search_fld_valid1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.set_search_fld("milk")
        self.home_page.search_fld_click()
        assert "milk" in driver.find_element(By.XPATH, '/html/body/div/div/div[2]/header/div/div/div/div[1]/div/a[1]/div/div[2]/div[1]')\
            .get_attribute("textContent")

    def test_search_fld_valid2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.set_search_fld("אק")
        self.home_page.search_fld_click()
        assert "אק" in driver.find_element(By.XPATH, "/html/body/div/div/div[2]/header/div/div/div/div[1]/div/a[1]/div/div[2]/div[1]")\
            .get_attribute("textContent")

    def test_search_fld_invalid(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.set_search_fld("--")
        self.home_page.search_fld_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/header/div/div/div/div[1]/h3")\
                   .get_attribute("textContent") == "0 תוצאות"

    def test_dry_goods_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.dry_products_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/h1")\
                   .get_attribute("textContent") == "מוצרים יבשים"

    def test_beauty_products_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.beauty_products_click()
        assert driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/h1')\
                   .get_attribute("textContent") == "מוצרי טיפוח"

    def test_sweets_and_snacks_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.sweets_and_snacks_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/h1")\
                   .get_attribute("textContent") == "ממתקים וחטיפים"

    def test_frozen_btn(self, driver):
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/a[5]")\
            .get_attribute("textContent") == "קפואים"

    def test_drink_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.drinks_click()
        self.welcome_to_modal.x_btn_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/h1")\
                   .get_attribute("innerText") == "משקאות"

    
