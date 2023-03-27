from src.utils.commonActions import CommonActions
from src.locators.cartBarLcs import cart_bar_lcs
class CartBar(CommonActions):
    def cart_clear_btn_click(self):
        CommonActions.click_on_locator(self, cart_bar_lcs["cart_clear"])
    def bucket_btn_click(self):
        CommonActions.click_on_locator(self, cart_bar_lcs["bucket_btn"])
    def pluc_btn_click(self):
        CommonActions.click_on_locator(self, cart_bar_lcs["plus_btn"])
    def minus_btn_click(self):
        CommonActions.click_on_locator(self, cart_bar_lcs["minus_btn"])
    def check_out_btn_click(self):
        CommonActions.click_on_locator(self, cart_bar_lcs["check_out_btn"])
    def set_items_amount(self, amount):
        CommonActions.set_locator(self, cart_bar_lcs["items_amount_fld"]).send_keys(amount)