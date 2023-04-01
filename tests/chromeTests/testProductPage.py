from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.productPageLcs import product_lcs
import allure


class TestProductPage(ChromeDriverSetUp):
    @allure.description("the test is verify, if product button work")
    def test_click_on_product(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.click_on_product()
        assert driver.current_url != "https://qa.trado.co.il/"
        assert "https://qa.trado.co.il/product/" in driver.current_url

    @allure.description("the test is verify, if user can add some count of items")
    def test_appending_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.click_on_product()
        self.product_page.add_5items()
        sleep(0.07)
        assert self.common_actions.get_attribute_by_value(product_lcs["product_amount_fld"]) == "5"

    @allure.description("the test is verify, if user can decrease some count of items")
    def test_decreasing_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.click_on_product()
        self.product_page.add_5items()
        self.product_page.minus_2items()
        sleep(0.06)
        assert self.common_actions.get_attribute_by_value(product_lcs["product_amount_fld"]) == "3"

    @allure.description("the test is verify, if title of product that user click on, "
                        "is the same title of product, that appear in the product page ")
    def test_product_verification(self, driver):
        self.welcome_to_modal.choose_coktails()
        assert self.common_actions.get_attribute_by_textcontent(product_lcs["product_name_in_hp"]) == "אקדיה"
        self.product_page.click_on_product()
        assert self.common_actions.get_attribute_by_textcontent(product_lcs["product_name"]) == "אקדיה"

    @allure.description("the test is verify, if the hebrew name of the product, "
                        "was changed to english name, after click on switch language button")
    def test_product_visability_in_eng(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.click_on_product()
        self.home_page.change_language_btn()
        assert self.common_actions.get_attribute_by_textcontent(product_lcs["product_name"]) == "acadia"
