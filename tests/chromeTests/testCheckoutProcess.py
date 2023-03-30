from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.deliveryDetailsPageLcs import deli_dtls_lcs
from src.locators.paymentsMethodsPageLcs import payments_mthds_lcs

class TestCheckoutProcess(ChromeDriverSetUp):

    def test_proceed_purchase_with_valid_data(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"])\
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "Paris", "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["city_adrs_fld"]) == "Paris"
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["street_adrs_fld"]) == "Baget"
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["num_adrs_fld"]) == "3"
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["entrance_adrs_fld"]) == "a"
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["floor_adrs_fld"]) == "2"
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"])\
               == "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_bn_name1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"])\
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        self.delivery_details_page.set_bn_name('')
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_bn_name_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_bn_name2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"])\
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        self.delivery_details_page.set_invoice_details("$3#--", "12345678987", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_bn_name_msg"]) == "שם בית העסק לא תקין"
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_bn_number1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_bn_num_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_bn_number2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "2" * 10, "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_bn_num_msg"]) == "ח.פ לא תקין"
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_email1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_email_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_email2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "wwqwed34", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_email_msg"]) == " דוא״ל לא תקין "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_city1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_city_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_street1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "Paris",
                                                       "", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_street_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_streetnum1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_house_num_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_streetnum2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "-4", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_house_num_msg"]) == " ספרות בלבד "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "



    def test_proceed_purchase_with_invalid_entrance1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_entrance_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "


    def test_proceed_purchase_with_invalid_floor1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_floor_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    def test_proceed_purchase_with_invalid_floor2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "-2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_floor_msg"]) == " ספרות בלבד "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    # def test_execute_valid_card_purchase(self, driver):
    #     self.sign_in_modal.sign_in()
    #     self.product_page.add_1item()
    #     self.cart_bar.check_out_btn_click()
    #     assert driver.current_url == "https://qa.trado.co.il/checkout"
    #     assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
    #            == "orderTimeline_time orderTimeline_current orderTimeline_current "
    #     assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
    #     self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "Paris",
    #                                                    "Baget", "3", "a", "2")
    #     self.delivery_details_page.complete_purchase_btn_click()
    #     self.payments_methods_page.credit_card_click()
    #     self.credit_card_modal.set_cvv("123")
    #     sleep(3)

    def test_execute_invalid_purchase1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678987"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678987", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        self.delivery_details_page.complete_purchase_btn_click()
        self.payments_methods_page.purchase_btn_click()
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["order_summery_status"]) != "orderTimeline_time orderTimeline_full orderTimeline_current "



