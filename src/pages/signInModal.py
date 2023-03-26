from src.utils.commonActions import CommonActions
from src.locators.signInModalLcs import sign_in_lcs
class SignInModal(CommonActions):
    def sign_in_btn_click(self):
        CommonActions.click_on_locator(self, sign_in_lcs["sign_in_btn"])
    def set_phone_num(self, phonenum):
        CommonActions.set_locator(self, sign_in_lcs["phone_number_fld"]).send_keys(phonenum)
    def log_in_btn_click(self):
        CommonActions.click_on_locator(self, sign_in_lcs["log_in_btn"])
    def remember_me_btn_click(self):
        CommonActions.click_on_locator(self, sign_in_lcs["remember_me_btn"])
    def submit_btn(self):
        CommonActions.click_on_locator(self, sign_in_lcs["submit_btn"])