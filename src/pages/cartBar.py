from src.utils.commonActions import CommonActions
from src.locators.cartBarLcs import cart_bar_lcs
class CartBar(CommonActions):
    def cart_clear_btn_click(self):
        CommonActions.click_on_locator(self, cart_bar_lcs["cart_status"])
        CommonActions.click_on_visible_locator_ac(self, cart_bar_lcs["cart_clear"])
    def bucket_btn_click(self):
        CommonActions.click_on_locator(self, cart_bar_lcs["bucket_btn"])
    def plus_btn_click(self):
        CommonActions.click_on_visible_locator_ac(self, cart_bar_lcs["plus_btn"])
    def minus_btn_click(self):
        CommonActions.click_on_visible_locator_ac(self, cart_bar_lcs["minus_btn"])
    def check_out_btn_click(self):
        CommonActions.click_on_visible_locator_ac(self, cart_bar_lcs["check_out_btn"])
    def set_items_amount(self, amount):
        CommonActions.set_locator(self, cart_bar_lcs["items_amount_fld"]).send_keys(amount)
    def add_4items(self):
        count = 0
        while count < 4:
            CartBar.plus_btn_click(self)
            count += 1
    def minus_2items(self):
        count = 2
        while count > 0:
            CartBar.minus_btn_click(self)
            count -= 1
