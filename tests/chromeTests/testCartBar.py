from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.cartBarLcs import cart_bar_lcs
from src.locators.productPageLcs import product_lcs

class TestCartBar(ChromeDriverSetUp):

    def test_add_item_to_cart(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"

    def test_removing_item_from_cart(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        self.cart_bar.bucket_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(cart_bar_lcs["cart_is_empty"]) == "cart_emptyCart"

    def test_validation_of_item_in_the_cart(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_textcontent(cart_bar_lcs["item_name"]) == \
               self.common_actions.get_attribute_by_textcontent(product_lcs["product_name"])

    def test_appending_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "1"
        while self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) < "4":
            self.product_page.plus_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "4"

    def test_decreasing_count_of_items(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.product_page.add_1item()
        while self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) < "9":
            self.product_page.plus_btn_click()
        self.product_page.minus_btn_click()
        sleep(2)
        assert self.common_actions.get_attribute_by_value(cart_bar_lcs["items_amount_fld"]) == "8"


