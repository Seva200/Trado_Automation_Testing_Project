from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.cartBarLcs import cart_bar_lcs
from src.locators.productPageLcs import product_lcs
import allure


class TestCartBar(ChromeDriverSetUp):
    @allure.description("the test is verify, if item was added to cart after user click on plus button")
    def test_add_item_to_cart(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"

    @allure.description("the test is verify, if user can remove item from cart")
    def test_removing_item_from_cart(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        self.cart_bar.bucket_btn_click()
        sleep(0.06)
        assert self.common_actions.get_attribute_by_class(cart_bar_lcs["cart_is_empty"]) == "cart_emptyCart"

    @allure.description("the test, that verify if user can remove item from cart")
    def test_cart_clear_btn(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        self.cart_bar.cart_clear_btn_click()
        assert self.common_actions.get_attribute_by_class(cart_bar_lcs["cart_is_empty"]) == "cart_emptyCart"

    @allure.description("the test is verify, if added to cart item has the same name as the item in the product page")
    def test_validation_of_item_in_the_cart1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_textcontent(cart_bar_lcs["item_name"]) == \
               self.common_actions.get_attribute_by_textcontent(product_lcs["product_name"])

    @allure.description("the test is verify, if added to cart item has the same price as a price to purchase")
    def test_validation_of_item_in_the_cart2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        sleep(2)
        assert self.common_actions.get_attribute_by_textcontent(cart_bar_lcs["product_price_in_div"]) == \
               self.common_actions.get_attribute_by_textcontent(cart_bar_lcs["product_price_in_footer"])


    @allure.description("the test is verify, if user can add some amount of items to cart")
    def test_appending_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        self.cart_bar.add_4items()
        sleep(0.06)
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "5"

    @allure.description("the test is verify, if user can decrease some amount of items in the cart")
    def test_decreasing_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        self.cart_bar.add_4items()
        self.cart_bar.minus_2items()
        sleep(0.08)
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "3"


