from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.productPageLcs import product_lcs

class TestProductPage(ChromeDriverSetUp):

    def test_click_on_product(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.click_on_product()
        assert driver.current_url != "https://qa.trado.co.il/"
        assert "https://qa.trado.co.il/product/" in driver.current_url

    def test_appending_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.click_on_product()
        self.product_page.add_5items()
        sleep(0.05)
        assert self.common_actions.get_attribute_by_value(product_lcs["product_amount_fld"]) == "5"

    def test_decreasing_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.click_on_product()
        self.product_page.add_5items()
        self.product_page.minus_2items()
        sleep(0.06)
        assert self.common_actions.get_attribute_by_value(product_lcs["product_amount_fld"]) == "3"

    def test_product_verification(self, driver):
        self.welcome_to_modal.choose_coktails()
        assert self.common_actions.get_attribute_by_textcontent(product_lcs["product_name_in_hp"]) == "גורילה גלו"
        self.product_page.click_on_product()
        assert self.common_actions.get_attribute_by_textcontent(product_lcs["product_name"]) == "גורילה גלו"

    def test_product_visability_in_eng(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.click_on_product()
        self.home_page.change_language_btn()
        assert self.common_actions.get_attribute_by_textcontent(product_lcs["product_name"]) == "gorilla glue"

