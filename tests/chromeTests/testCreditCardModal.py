from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.creditCardModalLcs import credit_card_lcs

class TestCreditCardModal(ChromeDriverSetUp):

    def test_valid_data(self, driver):
        self.sign_in_modal.sign_in()
        self.product_page.add_1item()
        self.cart_bar.check_out_btn_click()
        self.delivery_details_page.complete_purchase_btn_click()
        self.payments_methods_page.credit_card_click()
        self.credit_card_modal.set_card_num("4500000000000000")
        sleep(3)