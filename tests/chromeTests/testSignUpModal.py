from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.signUpModalLcs import sign_up_lcs

class TestSignUpModal(ChromeDriverSetUp):
    def test_sign_up_invalid_phone_num1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("546457")
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["invalid_number"]) == "מס׳ טלפון לא תקין"

    def test_sign_up_invalid_phone_num2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("euweuyquw")
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["invalid_number"]) == "מס׳ טלפון לא תקין"

    def test_sign_up_invalid_phone_num3(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("3" * 11)
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["invalid_number"]) == "מס׳ טלפון לא תקין"


    def test_sign_up_invalid_bn_number1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("1234567898")
        self.sign_up_modal.accept_policy()
        self.sign_up_modal.log_in_btn_click()
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["empty_bn_fld"]) == "שדה צריך להיות ייחודיי"

    def test_sign_up_invalid_bn_number2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_bn_number("sdqwdqw")
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["bnNum_fld"]) != "sdqwdqw"

    def test_sign_up_invalid_bn_number3(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_bn_number("1" * 9)
        assert "ח.פ לא תקין" in self.common_actions.get_attribute_by_textcontent(sign_up_lcs["bnnum_div"])

    def test_sign_up_with_no_policy_accept(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sign_in_click()
        self.sign_up_modal.sign_up_btn_click()
        self.sign_up_modal.set_phone_number("1234567898")
        self.sign_up_modal.log_in_btn_click()
        assert self.common_actions.get_attribute_by_textcontent(sign_up_lcs["no_accept_policy"]) == "please approve our policy "

    def test_sign_up(self, driver):
        self.sign_up_modal.set_sign_up()
        self.sign_up_modal.cocktails_btn_click()
        self.sign_up_modal.create_acc_btn_click()

