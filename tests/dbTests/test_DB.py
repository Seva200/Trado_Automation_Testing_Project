import time

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
    @allure.description("the test is verify, that invalid purchase didn't saved in db")
    def test_invalid_purchase_saved_in_db(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        self.delivery_details_section.complete_purchase_btn_click()
        self.payments_methods_section.purchase_btn_click()
        time.sleep(2)
        a = self.common_actions.get_attribute_by(payments_mthds_lcs["order_number"],
                                                            "textContent").encode('utf-8')
        a = str(a)
        order_number = a[-5] + a[-4] + a[-3] + a[-2]
        order_status = db.get_order_status(order_number)
        assert order_status != 'received'

