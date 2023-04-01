from time import sleep
import random
import allure
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.utils.pyMongoSetUp.signUpSetUp import phone_num, code
from src.locators.signUpModalLcs import sign_up_lcs
from src.locators.homePageLcs import home_lcs


class TestSignUpModal(ChromeDriverSetUp):
    @allure.description("the test is verify,if user can sign up with valid data")
    def test_valid_sign_up(self, driver):
        self.welcome_to_modal.choose_coktails()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["person_area_link"]) == " התחברות "
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number(phone_num)
        self.sign_up_modal.set_bn_number(f'4030{random.randint(0, 99999)}')
        self.sign_up_modal.accept_policy()
        self.sign_up_modal.log_in_btn_click()
        sleep(3)
        self.sign_up_modal.set_1_num(code())
        self.sign_up_modal.verify_btn_click()
        self.sign_up_modal.cocktails_btn_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["person_area_link"]) == " אזור אישי "

    @allure.description("the test is verify, that user can't sign up with invalid sms code")
    def test_sign_up_with_invalid_code(self, driver):
        self.welcome_to_modal.choose_coktails()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["person_area_link"]) == " התחברות "
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number(phone_num)
        self.sign_up_modal.set_bn_number(f'4030{random.randint(0, 99999)}')
        self.sign_up_modal.accept_policy()
        self.sign_up_modal.log_in_btn_click()
        sleep(3)
        self.sign_up_modal.set_code(1, 2, 3, 4, 5)
        self.sign_up_modal.verify_btn_click()
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["invalid_code_msg"]) == "failed to login "

    @allure.description("the test is verify, that user can't sign up with invalid phone number")
    def test_sign_up_invalid_phone_num1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("546457")
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["invalid_number"]) == "מס׳ טלפון לא תקין"

    @allure.description("the test is verify, that user can't sign up with invalid phone number")
    def test_sign_up_invalid_phone_num2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("euweuyquw")
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["invalid_number"]) == "מס׳ טלפון לא תקין"

    @allure.description("the test is verify, that user can't sign up with invalid phone number")
    def test_sign_up_invalid_phone_num3(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("3" * 11)
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["invalid_number"]) == "מס׳ טלפון לא תקין"

    @allure.description("the test is verify, that user can't sign up with invalid business number")
    def test_sign_up_invalid_bn_number1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("1234567898")
        self.sign_up_modal.accept_policy()
        self.sign_up_modal.log_in_btn_click()
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["empty_bn_fld"]) == "שדה צריך להיות ייחודיי"

    @allure.description("the test is verify, that user can't sign up with invalid business number")
    def test_sign_up_invalid_bn_number2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_bn_number("sdqwdqw")
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["bnNum_fld"]) != "sdqwdqw"

    @allure.description("the test is verify, that user can't sign up with invalid business number")
    def test_sign_up_invalid_bn_number3(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_bn_number("1" * 10)
        assert "ח.פ לא תקין" in self.common_actions.get_attribute_by_textcontent(sign_up_lcs["bnnum_div"])

    @allure.description("the test is verify, that user can't sign up without agree to terms and conditions")
    def test_sign_up_with_no_policy_accept(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("1234567898")
        self.sign_up_modal.log_in_btn_click()
        assert self.common_actions.get_attribute_by_textcontent(
            sign_up_lcs["no_accept_policy"]) == "please approve our policy "
