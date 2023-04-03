import allure
from src.locators.personalAreaPageLcs import personal_area_lcs
from src.utils.drivers.edgeDriverSetUp import EdgeDriverSetUp


class TestPersonalAreaPage(EdgeDriverSetUp):

    @allure.description("the test is verify, that user can't edit his profile with invalid street number")
    def test_invalid_street_number(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', 'Gray', '0552603210', 'joshgrey89@mail.com', '987654321',
                                                   'Paris Baget', '-')
        assert self.common_actions.get_attribute_by_textcontent(
            personal_area_lcs["street_num_inv_msg"]) == "נא למלא שדה זה"

    @allure.description("the test is verify, that user can't edit his profile with invalid email")
    def test_invalid_email(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', 'Gray', '0552992023', 'adaddem', '987654321', 'Paris Baget',
                                                   '29')
        assert self.common_actions.get_attribute_by_textcontent(
            personal_area_lcs["invalid_email_msg"]) == "דוא״ל לא תקין"

    @allure.description("the test is verify, that user can't edit his profile with invalid first name")
    def test_invalid_first_name(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('', 'Gray', '0552603210', 'joshgrey89@mail.com', '987654321',
                                                   'Paris Baget', '29')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["fname_inv_msg"]) == "נא למלא שדה זה"

    @allure.description("the test is verify, that user can't edit his profile with invalid business number")
    def test_invalid_business_num1(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', 'Gray', '0552603210', 'joshgrey89@mail.com', '',
                                                   'Paris Baget', '29')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["inv_bn_msg"]) == "נא למלא שדה זה"

    @allure.description("the test is verify, that user can't edit his profile with invalid business number")
    def test_invalid_business_num2(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', 'Gray', '0552603210', 'joshgrey89@mail.com', '12345678999',
                                                   'Paris Baget', '29')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["inv_bn_msg"]) == "ח.פ לא תקין"

    @allure.description("the test is verify, that user can't edit his profile with invalid last name")
    def test_invalid_last_name(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', '', '0552603210', 'joshgrey89@mail.com', '987654321',
                                                   'Paris Baget', '29')
        assert self.common_actions.get_attribute_by_textcontent(personal_area_lcs["lname_inv_msg"]) == "נא למלא שדה זה"

    @allure.description("the test is verify, if user can edit his profile with valid data")
    def test_valid_personal_area(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_personal_area('Josh', 'Gray', '0552603210', 'joshgrey89@mail.com', '987654321',
                                                   'Paris Baget', '29')
        assert self.common_actions.get_attribute_by_value(personal_area_lcs["first_name_fld"]) == "Josh"
        assert self.common_actions.get_attribute_by_value(
            personal_area_lcs["city_&_street_fld"]) == "Paris baget street"

    @allure.description("the test is verify, verify if we are here link is work")
    @allure.severity(severity_level='minor')
    def test_link_we_are_here(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.support_link_click()
        assert driver.current_url == "https://qa.trado.co.il/contact"

    @allure.description("the test is verify, verify if withdraw button is works")
    def test_withdraw_btn(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.withdraw_btn_click()
        assert driver.current_url != "https://qa.trado.co.il/user/personalArea"
