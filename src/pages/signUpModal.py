from src.pages.commonActions import CommonActions
from src.locators.signUpModalLcs import sign_up_lcs
class SignUpModal(CommonActions):
# Page 1
    def x_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["x_btn"])
    def sign_up_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["signUp_btn"])
    def facebook_link(self):
        CommonActions.click_on_locator(self, sign_up_lcs["facebook"])
    def google_link(self):
        CommonActions.click_on_locator(self, sign_up_lcs["google"])
    def twitter_link(self):
        CommonActions.click_on_locator(self, sign_up_lcs["twitter"])
    def set_phone_number(self, phonenumber):
        CommonActions.set_locator(self, sign_up_lcs["phone_fld"]).send_keys(phonenumber)
    def set_bn_number(self, bnnumber):
        CommonActions.set_locator(self, sign_up_lcs["bnNum_fld"]).send_keys(bnnumber)
    def accept_policy(self):
        CommonActions.click_on_locator(self, sign_up_lcs["accept_policy"])
    def accept_sent_emails(self):
        CommonActions.click_on_locator(self, sign_up_lcs["accept_sent_emails"])
    def log_in_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["logIn_btn"])
# Page 2
    def set_1_num(self, num):
        CommonActions.set_locator(self, sign_up_lcs["1input_number_fld"]).send_keys(num)
    def set_2_num(self, num):
        CommonActions.set_locator(self, sign_up_lcs["2input_number_fld"]).send_keys(num)
    def set_3_num(self, num):
        CommonActions.set_locator(self, sign_up_lcs["3input_number_fld"]).send_keys(num)
    def set_4_num(self, num):
        CommonActions.set_locator(self, sign_up_lcs["4input_number_fld"]).send_keys(num)
    def set_5_num(self, num):
        CommonActions.set_locator(self, sign_up_lcs["5input_number_fld"]).send_keys(num)
    def verify_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["verify_btn"])
    def resent_msg_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["resent_msg_btn"])