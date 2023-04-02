import random
from src.utils.commonActions import CommonActions
from src.locators.signUpModalLcs import sign_up_lcs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from src.utils.pyMongo.signUpSetUp import phone_num
from src.utils.pyMongo.signUpSetUp import code

class SignUpModal(CommonActions):
# Page 1
    def x_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["x_btn"])
    def sign_up_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["signUp_btn"])
    def facebook_link(self):
        CommonActions.click_on_visible_locator_ac(self, sign_up_lcs["facebook"])
    def google_link(self):
        CommonActions.click_on_visible_locator_ac(self, sign_up_lcs["google"])
    def twitter_link(self):
        CommonActions.click_on_visible_locator_ac(self, sign_up_lcs["twitter"])
    def set_phone_number(self, phonenumber):
        CommonActions.set_locator(self, sign_up_lcs["phone_fld"]).send_keys(phonenumber)
    def set_bn_number(self, bnnumber):
        CommonActions.set_locator(self, sign_up_lcs["bnNum_fld"]).send_keys(bnnumber)
    def accept_policy(self):
        CommonActions.click_on_visible_locator_ac(self, sign_up_lcs["accept_policy"])
    def accept_sent_emails(self):
        CommonActions.click_on_locator(self, sign_up_lcs["accept_sent_emails"])
    def log_in_btn_click(self):
        CommonActions.click_on_visible_locator_ac(self, sign_up_lcs["logIn_btn"])

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
    def set_code(self, num1, num2, num3, num4, num5):
        SignUpModal.set_1_num(self, num1)
        SignUpModal.set_2_num(self, num2)
        SignUpModal.set_3_num(self, num3)
        SignUpModal.set_4_num(self, num4)
        SignUpModal.set_5_num(self, num5)
    def verify_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["verify_btn"])
    def resent_msg_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["resent_msg_btn"])
    def create_acc_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["create_acc_btn"])
    def cocktails_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["choose_cocktail"])
        SignUpModal.create_acc_btn_click(self)
    def rest_btn_click(self):
        CommonActions.click_on_locator(self, sign_up_lcs["choose_rest"])
        SignUpModal.create_acc_btn_click(self)


    def set_sign_up(self):
        wdw(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[4]/div/div/div/button"))).click()
        wdw(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/a/span"))).click()
        SignUpModal.sign_up_btn_click(self)
        SignUpModal.set_phone_number(self, phone_num)
        SignUpModal.set_bn_number(self, f'3{random.randint(0,9)}1{random.randint(0,9)}'*2)
        SignUpModal.accept_policy(self)
        SignUpModal.log_in_btn_click(self)
        c = code()
        SignUpModal.set_1_num(self, c)
        SignUpModal.verify_btn_click(self)