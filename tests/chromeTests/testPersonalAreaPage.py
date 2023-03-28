from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.personalAreaPageLcs import personal_area_lcs

class TestPersonalAreaPage(ChromeDriverSetUp):

    def test_valid_personal_area(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', 'Gray', '0552603210', 'joshgrey89@mail.com', '123456789', 'Paris baget', '29')
        assert self.common_actions.get_attribute_by_value(personal_area_lcs["first_name_fld"]) == "Josh"
        assert self.common_actions.get_attribute_by_value(personal_area_lcs["city_&_street_fld"]) == "Paris baget 20"

    def test_invalid_street_number(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('יוני', 'וואיס', '0552992023', 'joshgrey89@mail.com', '123456789','Paris baget', '-')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["street_num_inv_msg"]) == "נא למלא שדה זה"

    def test_invalid_email(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', 'Gray', '0552992023', 'adaddem', '123456789', 'Paris baget', '29')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["invalid_email_msg"]) == "דוא״ל לא תקין"

    def test_inalid_first_name(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('', 'Gray', '0552603210', 'joshgrey89@mail.com', '123456789','Paris baget', '29')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["fname_inv_msg"]) == "נא למלא שדה זה"

    def test_invalid_last_name(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', '', '0552603210', 'joshgrey89@mail.com', '123456789','Paris baget', '29')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["lname_inv_msg"]) == "נא למלא שדה זה"

    def test_invalid_business_num1(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', 'Gray', '0552603210', 'joshgrey89@mail.com', '','Paris baget', '29')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["inv_bn_msg"]) == "נא למלא שדה זה"

    def test_invalid_business_num2(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', 'Gray', '0552603210', 'joshgrey89@mail.com', '12345678987', 'Paris baget', '29')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["inv_bn_msg"]) == "ח.פ לא תקין"

    def test_link_we_are_here(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.support_link_click()
        assert driver.current_url == "https://qa.trado.co.il/contact"

    def test_withdraw_btn(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.withdraw_btn_click()
        assert driver.current_url != "https://qa.trado.co.il/user/personalArea"