from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.deliveryDetailsPageLcs import deli_dtls_lcs
from src.locators.paymentsMethodsPageLcs import payments_mthds_lcs
from src.locators.homePageLcs import home_lcs
from src.locators.creditCardModalLcs import credit_card_lcs
import allure

class TestCheckoutProcess(ChromeDriverSetUp):
    @allure.description("test that verify if user can proceed a purchase when he set valid delivery details data")
    def test_proceed_purchase_with_valid_data(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"])\
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris", "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["city_adrs_fld"]) == "Paris"
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["street_adrs_fld"]) == "Baget"
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["num_adrs_fld"]) == "3"
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["entrance_adrs_fld"]) == "a"
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["floor_adrs_fld"]) == "2"
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"])\
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
    @allure.description("test that verify if user can't proceed a purchase when he don't set a business name "
                        "in delivery details")
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

    @allure.description("test that verify if user can't proceed a purchase when he set invalid business name "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_bn_name2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"])\
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        self.delivery_details_page.set_invoice_details("$3#--", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_bn_name_msg"]) == "שם בית העסק לא תקין"
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he don't set a business number "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_bn_number1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_bn_num_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he set invalid business number "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_bn_number2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "2" * 10, "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_bn_num_msg"]) == "ח.פ לא תקין"
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he don't set an email "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_email1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_email_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he set invalid email "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_email2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "wwqwed34", "Paris",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_email_msg"]) == " דוא״ל לא תקין "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he don't set a city name "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_city1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "",
                                                       "Baget", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_city_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he don't set a street name "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_street1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "", "3", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_street_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he don't set a street number "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_streetnum1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_house_num_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he set invalid street number "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_streetnum2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "-4", "a", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_house_num_msg"]) == " ספרות בלבד "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he don't set an entrance "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_entrance1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "", "2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_entrance_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he don't set a floor number "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_floor1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_floor_msg"]) == " נא למלא שדה זה "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "

    @allure.description("test that verify if user can't proceed a purchase when he set invalid floor number "
                        "in delivery details")
    def test_proceed_purchase_with_invalid_floor2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "-2")
        assert self.common_actions.get_attribute_by_textcontent(deli_dtls_lcs["invalid_floor_msg"]) == " ספרות בלבד "
        self.delivery_details_page.complete_purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["payments_methods_status"]) \
               != "orderTimeline_time orderTimeline_current orderTimeline_current "
    @allure.description("test that verify if user can execute purchase with valid credit card")
    def test_execute_valid_credit_card_purchase(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        self.delivery_details_page.complete_purchase_btn_click()
        self.payments_methods_page.credit_card_click()
        driver.switch_to.frame("yaadFrame")
        self.credit_card_modal.set_card_num("4580000000000000")
        self.credit_card_modal.set_id_num("000000000")
        self.credit_card_modal.choose_5_month()
        self.credit_card_modal.choose_24_year()
        self.credit_card_modal.set_cvv('123')
        self.credit_card_modal.submit_btn_click()
        sleep(2)
        self.payments_methods_page.purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(
            deli_dtls_lcs["order_summery_status"]) != "orderTimeline_time orderTimeline_full orderTimeline_current "

    @allure.description("test, verify that user can't execute purchase with invalid credit card")
    def test_execute_invalid_credit_card_purchase(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        self.delivery_details_page.complete_purchase_btn_click()
        self.payments_methods_page.credit_card_click()
        driver.switch_to.frame("yaadFrame")
        self.credit_card_modal.set_card_num("ieifefnin")
        self.credit_card_modal.set_id_num("000000000")
        assert self.common_actions.get_attribute_by_textcontent(credit_card_lcs["invalid_card_number_msg"]) == "מספר כרטיס אשראי אינו תקין (418)"
        self.credit_card_modal.submit_btn_click()
        driver.switch_to.parent_frame()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
    @allure.description("test, verify that user can't execute a purchase without choose payment method ")
    def test_execute_invalid_purchase1(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        self.delivery_details_page.complete_purchase_btn_click()
        self.payments_methods_page.purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["order_summery_status"]) != "orderTimeline_time orderTimeline_full orderTimeline_current "
    @allure.description("test, verify that user can't execute a purchase with invalid bank transfer data ")
    def test_execute_invalid_purchase2(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        self.delivery_details_page.complete_purchase_btn_click()
        self.payments_methods_page.bank_transfer_click()
        self.bank_transfer_modal.set_bank_branch("dshdjsdjh")
        self.bank_transfer_modal.confirm_transfer_btn_click()
        self.payments_methods_page.purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["order_summery_status"]) != "orderTimeline_time orderTimeline_full orderTimeline_current "

    @allure.description("test, verify that user can't execute a purchase with invalid finTrado data ")
    def test_execute_invalid_purchase3(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        self.delivery_details_page.complete_purchase_btn_click()
        self.payments_methods_page.fin_trado_click()
        assert self.common_actions.get_attribute_by_class(payments_mthds_lcs["trado_modal_open"]) == "MuiDialog-container MuiDialog-scrollPaper css-ekeie0"
        self.fin_trado_modal.continue_btn_click()
        self.payments_methods_page.purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["order_summery_status"]) != "orderTimeline_time orderTimeline_full orderTimeline_current "

    @allure.description("test, verify that user can't execute a purchase with invalid digital check data ")
    def test_execute_invalid_purchase4(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        self.delivery_details_page.complete_purchase_btn_click()
        self.payments_methods_page.digital_check_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        self.digital_check_modal.insert_the_check_btn_click()
        self.digital_check_modal.set_bank_branch("efsdfsd")
        self.payments_methods_page.purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(
            deli_dtls_lcs["order_summery_status"]) != "orderTimeline_time orderTimeline_full orderTimeline_current "

    @allure.description("test, verify that user can't execute a purchase with invalid b2b data ")
    def test_execute_invalid_purchase5(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/checkout"
        assert self.common_actions.get_attribute_by_class(deli_dtls_lcs["deliv_details_status"]) \
               == "orderTimeline_time orderTimeline_current orderTimeline_current "
        assert self.common_actions.get_attribute_by_value(deli_dtls_lcs["bn_num_fld"]) == "12345678999"
        self.delivery_details_page.set_invoice_details("Pizza Jon", "12345678999", "jhongrey89@mail.com", "Paris",
                                                       "Baget", "3", "a", "2")
        self.delivery_details_page.complete_purchase_btn_click()
        self.payments_methods_page.b2b_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        self.b2b_modal.set_bn_num("sdqwdwef")
        self.b2b_modal.set_customer_id("licceencnec")
        self.b2b_modal.confirm_btn_click()
        self.payments_methods_page.purchase_btn_click()
        sleep(1)
        assert self.common_actions.get_attribute_by_class(
            deli_dtls_lcs["order_summery_status"]) != "orderTimeline_time orderTimeline_full orderTimeline_current "
