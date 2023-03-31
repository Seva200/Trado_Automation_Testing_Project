from src.utils.commonActions import CommonActions
from src.locators.finTradoModalLocs import fin_trado_lcs

class FinTradoModal(CommonActions):

    def x_btn_click(self):
        CommonActions.click_on_locator(self, fin_trado_lcs["x_btn"])
    def set_credit_amount(self, creditamount):
        CommonActions.set_locator(self, fin_trado_lcs["credit_amount_fld"]).send_keys(creditamount)
    def set_phone_num(self, phone):
        CommonActions.set_locator(self, fin_trado_lcs["x_btn"]).send_keys(phone)
    def continue_btn_click(self):
        CommonActions.click_on_locator(self, fin_trado_lcs["continue_btn"])

