from src.utils.commonActions import CommonActions
from src.locators.paymentsMethodsSectionLcs import payments_mthds_lcs
class PaymentsMethodsSection(CommonActions):
    def credit_card_click(self):
        CommonActions.click_on_locator(self, payments_mthds_lcs["credit_card"])
    def b2b_click(self):
        CommonActions.click_on_locator(self, payments_mthds_lcs["b2b"])
    def digital_check_click(self):
        CommonActions.click_on_locator(self, payments_mthds_lcs["digital_check"])
    def bank_transfer_click(self):
        CommonActions.click_on_locator(self, payments_mthds_lcs["bank_transfer"])
    def fin_trado_click(self):
        CommonActions.click_on_locator(self, payments_mthds_lcs["fin_trado"])
    def purchase_btn_click(self):
        CommonActions.click_on_visible_locator_ac(self, payments_mthds_lcs["purchase"])
    def go_back_btn_click(self):
        CommonActions.click_on_locator(self, payments_mthds_lcs["go_back"])
    def thank_you_back_home_btn_click(self):
        CommonActions.click_on_locator(self, payments_mthds_lcs["thank_you_back_home"])