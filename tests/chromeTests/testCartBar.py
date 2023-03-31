from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.cartBarLcs import cart_bar_lcs
from src.locators.productPageLcs import product_lcs
import allure

class TestCartBar(ChromeDriverSetUp):
    @allure.description("test that verify if item was added to cart after user click on plus button")
    def test_add_item_to_cart(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
    @allure.description("test that verify if user can remove item from cart")
    def test_removing_item_from_cart(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        self.cart_bar.bucket_btn_click()
        sleep(0.06)
        assert self.common_actions.get_attribute_by_class(cart_bar_lcs["cart_is_empty"]) == "cart_emptyCart"

    @allure.description("test that verify if user can remove item from cart")
    def test_cart_clear_btn(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        self.cart_bar.cart_clear_btn_click()
        assert self.common_actions.get_attribute_by_class(cart_bar_lcs["cart_is_empty"]) == "cart_emptyCart"
    @allure.description("test that verify if added to cart item is the same item in the product page")
    def test_validation_of_item_in_the_cart(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_textcontent(cart_bar_lcs["item_name"]) == \
               self.common_actions.get_attribute_by_textcontent(product_lcs["product_name"])
    @allure.description("test that verify if user can add some count of items to cart")
    def test_appending_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        self.cart_bar.add_4items()
        sleep(0.06)
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "5"
    @allure.description("test that verify if user can decrease some count of items in the cart")
    def test_decreasing_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        self.cart_bar.add_4items()
        self.cart_bar.minus_2items()
        sleep(0.06)
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "3"



