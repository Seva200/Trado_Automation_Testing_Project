from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.signInModalLcs import sign_in_lcs
from src.locators.homePageLcs import home_lcs
from src.utils.PymongoSetUp import sms_code

class TestSignInModal(ChromeDriverSetUp):

    def test_sign_in_valid(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("0552603210")
        self.sign_in_modal.log_in_btn_click()
        self.sign_in_modal.set_1_num(sms_code())
        self.sign_in_modal.submit_btn()
        assert "שלום" in self.common_actions.get_attribute_by_textcontent(home_lcs["hello_msg"])

    def test_sign_in_invalid_number1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("9876653022")
        self.sign_in_modal.log_in_btn_click()
        assert self.common_actions.get_attribute_by_textcontent(sign_in_lcs["no_register_number_msg"]) == "no such user please register "

    def test_sign_in_invalid_number2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("055728")
        assert self.common_actions.get_attribute_by_textcontent(sign_in_lcs["invalid_number"]) == "מס׳ טלפון לא תקין"

    def test_sign_in_invalid_number3(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("1" * 11)
        assert self.common_actions.get_attribute_by_textcontent(sign_in_lcs["invalid_number"]) == "מס׳ טלפון לא תקין"

    def test_resent_msg(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("0552992023")
        self.sign_in_modal.log_in_btn_click()
        code1 = sms_code()
        self.sign_in_modal.resent_msg_btn()
        code2 = sms_code()
        assert code1 != code2

    def test_sign_in_invalid_code(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("0552992023")
        self.sign_in_modal.log_in_btn_click()
        self.sign_in_modal.set_1_num("0" * 5)
        self.sign_in_modal.submit_btn()
        assert self.common_actions.get_attribute_by_textcontent(sign_in_lcs["invalid_code_msg"]) == "failed to login "

    def test_facebook_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.facebook_link()
        driver.switch_to.window(driver.window_handles[1])
        assert "https://www.facebook.com/" in driver.current_url

    def test_google_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.google_link()
        driver.switch_to.window(driver.window_handles[1])
        assert "https://accounts.google.com/" in driver.current_url

    def test_twitter_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.twitter_link()
        driver.switch_to.window(driver.window_handles[1])
        assert "https://twitter.com/" in driver.current_url





