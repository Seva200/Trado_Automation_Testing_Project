from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.paymentsMethodsSectionLcs import payments_mthds_lcs
from src.utils.pyMongo import db_actions as db
import allure

class TestDB(ChromeDriverSetUp):


    @allure.description("the test is verify, if the data hasn't been saved to the database"
                        " after the user has edited the business number")
    def test_invalid_bn_number_saved_in_db(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_btn_click()
        self.personal_area_page.set_bn_id_num("3" * 10)
        self.personal_area_page.save_btn_click()
        assert db.get_user_id() != '3' * 10


    @allure.description("the test is verify, if the data has been saved to the database"
                        " after the user has edited the email")
    def test_email_saved_in_db(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        self.personal_area_page.edit_btn_click()
        self.personal_area_page.set_email("green28@gmail.com")
        self.personal_area_page.save_btn_click()
        assert db.get_email() == 'green28@gmail.com'
        self.personal_area_page.edit_btn_click()
        self.personal_area_page.set_email("joshgrey89@mail.com")
        self.personal_area_page.set_bn_id_num("987654321")
        self.personal_area_page.save_btn_click()


