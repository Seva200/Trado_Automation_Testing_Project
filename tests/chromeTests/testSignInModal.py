from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.signInModalLcs import sign_in_lcs
from src.locators.homePageLcs import home_lcs
import allure
from src.utils.pyMongoSetUp.signInSetUp import sms_code


class TestSignInModal(ChromeDriverSetUp):
    @allure.description("the test is verify, if user can sign in with valid data")
    def test_sign_in_valid(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("0552603210")
        self.sign_in_modal.log_in_btn_click()
        self.sign_in_modal.set_1_num(sms_code())
        self.sign_in_modal.submit_btn()
        sleep(1)
        assert "אורח" not in self.common_actions.get_attribute_by_textcontent(home_lcs["hello_user_msg"])

    @allure.description("the test is verify, if user can log out")
    def test_log_out_btn(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.log_out_btn_click()
        assert "שלום אורח" in self.common_actions.get_attribute_by_textcontent(home_lcs["hello_user_msg"])

    @allure.description("the test is verify, that user can't sign in with invalid number")
    def test_sign_in_invalid_number1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("9876653022")
        self.sign_in_modal.log_in_btn_click()
        assert self.common_actions.get_attribute_by_textcontent(
            sign_in_lcs["no_register_number_msg"]) == "no such user please register "

    @allure.description("the test is verify, that user can't sign in with invalid number")
    def test_sign_in_invalid_number2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("454545")
        assert self.common_actions.get_attribute_by_textcontent(
            sign_in_lcs["invalid_number_msg"]) == "מס׳ טלפון לא תקין"

    @allure.description("the test is verify, that user can't sign in with invalid number")
    def test_sign_in_invalid_number3(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("1" * 11)
        assert self.common_actions.get_attribute_by_textcontent(
            sign_in_lcs["invalid_number_msg"]) == "מס׳ טלפון לא תקין"

    @allure.description("the test that checks if the user can accept the new code by pressing the resend button")
    def test_resend_msg(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("0552603210")
        self.sign_in_modal.log_in_btn_click()
        code1 = sms_code()
        self.sign_in_modal.resent_msg_btn()
        code2 = sms_code()
        assert code1 != code2

    @allure.description("the test is verify, that user can't sign in with invalid sms code")
    def test_sign_in_invalid_code(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_in_modal.set_phone_num("0552603210")
        self.sign_in_modal.log_in_btn_click()
        self.sign_in_modal.set_1_num("0" * 5)
        self.sign_in_modal.submit_btn()
        assert self.common_actions.get_attribute_by_textcontent(sign_in_lcs["invalid_code_msg"]) == "failed to login "

    @allure.description("the test is verify, if facebook link is works")
    def test_facebook_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.facebook_link()
        driver.switch_to.window(driver.window_handles[1])
        assert "https://www.facebook.com/" in driver.current_url

    @allure.description("the test is verify, if google link is works")
    def test_google_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.google_link()
        sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        assert "https://accounts.google.com/" in driver.current_url
        assert self.common_actions.get_attribute_by_textcontent(
            sign_in_lcs["google_title"]) != "הגישה חסומה: הבקשה של האפליקציה הזו לא חוקית"

    @allure.description("the test is verify, if twitter link is works")
    def test_twitter_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.twitter_link()
        driver.switch_to.window(driver.window_handles[1])
        assert "https://twitter.com/" in driver.current_url
