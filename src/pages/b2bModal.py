from src.utils.commonActions import CommonActions
from src.locators.b2bModalLocs import b2b_lcs

class B2BModal(CommonActions):

    def x_btn_click(self):
        CommonActions.click_on_locator(self, b2b_lcs["x_btn"])

    def set_bn_num(self, bnnum):
        CommonActions.set_locator(self, b2b_lcs["bn_num_fld"]).send_keys(bnnum)

    def set_customer_id(self, custid):
        CommonActions.set_locator(self, b2b_lcs["b2b_customer_id_fld"]).send_keys(custid)

    def confirm_btn_click(self):
        CommonActions.click_on_locator(b2b_lcs["confirm_btn"])