from src.utils.commonActions import CommonActions
from src.locators.signInModalLcs import sign_in_lcs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from src.utils.PymongoSetUp import sms_code
class SignInModal(CommonActions):
    def sign_in_btn_click(self):
        CommonActions.click_on_locator(self, sign_in_lcs["sign_in_btn"])
    def set_phone_num(self, phonenum):
        CommonActions.set_locator(self, sign_in_lcs["phone_number_fld"]).send_keys(phonenum)
    def log_in_btn_click(self):
        CommonActions.click_on_locator(self, sign_in_lcs["log_in_btn"])
    def remember_me_btn_click(self):
        CommonActions.click_on_locator(self, sign_in_lcs["remember_me_btn"])


        # Page 2
    def set_1_num(self, num):
        CommonActions.set_locator(self, sign_in_lcs["1input_number_fld"]).send_keys(num)

    def set_2_num(self, num):
        CommonActions.set_locator(self, sign_in_lcs["2input_number_fld"]).send_keys(num)

    def set_3_num(self, num):
        CommonActions.set_locator(self, sign_in_lcs["3input_number_fld"]).send_keys(num)

    def set_4_num(self, num):
        CommonActions.set_locator(self, sign_in_lcs["4input_number_fld"]).send_keys(num)

    def set_5_num(self, num):
        CommonActions.set_locator(self, sign_in_lcs["5input_number_fld"]).send_keys(num)

    def verify_btn_click(self):
        CommonActions.click_on_locator(self, sign_in_lcs["verify_btn"])

    def submit_btn(self):
        CommonActions.click_on_locator(self, sign_in_lcs["submit_btn"])
    def log_in(self):
        wdw(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[4]/div/div/div/button"))).click()
        wdw(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/a/span"))).click()
        SignInModal.set_phone_num(self, "0552992023")
        SignInModal.log_in_btn_click(self)
        y = sms_code()
        SignInModal.set_1_num(self, y)
        SignInModal.submit_btn(self)


