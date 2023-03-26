import time

from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from selenium.webdriver.common.by import By
from src.utils.PymongoSetUp import sms

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
    def test_personal_area_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.personal_area_link()
        assert wdw(driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]"))) \
                   .get_attribute("class") == "modal_modalWrapper false modal_open    "

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
    def test_cannabis_click(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.cannabis_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/a[5]") \
                   .get_attribute("textContent") == "קנאביס"
    def test_cleaners_btn_click(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.cleaners_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/h1") \
                   .get_attribute("textContent") == "מוצרי ניקוי"
    def test_drink_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.drinks_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/h1")\
                   .get_attribute("innerText") == "משקאות"
    def test_uppload_products_click(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.upload_prod_btn_click()
        assert wdw(driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]"))) \
                   .get_attribute("class") == "modal_modalWrapper false modal_open    "
# Body
    # Slide Show
    def test_left_arrow_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[2]")\
                   .get_attribute("class") == "slide selected"
        self.home_page.left_arrow_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[9]") \
                   .get_attribute("class") == "slide selected"
    def test_right_arrow_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        assert driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[2]") \
               .get_attribute("class") == "slide selected"
        self.home_page.right_arrow_click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[3]") \
                   .get_attribute("class") == "slide selected"

    def test_login(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.upload_prod_btn_click()
        self.sign_in_modal.set_phone_num("0552992023")
        self.sign_in_modal.log_in_btn_click()
        y = sms()
        self.sign_up_modal.set_1_num(y)
        self.sign_in_modal.submit_btn()
        time.sleep(2)


    
