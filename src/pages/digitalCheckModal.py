from src.utils.commonActions import CommonActions
from src.locators.diditalCheckModalLocs import digital_check_lcs

class DigitalCheckModal(CommonActions):

    def x_btn_click(self):
        CommonActions.click_on_locator(self, digital_check_lcs["x_btn"])

    def bank_name_btn_click(self):
        CommonActions.click_on_locator(self, digital_check_lcs["bank_name_btn"])

    def bank_12_click(self):
        DigitalCheckModal.bank_name_btn_click(self)
        CommonActions.click_on_locator(self, digital_check_lcs["bank_12"])

    def bank_10_click(self):
        DigitalCheckModal.bank_name_btn_click(self)
        CommonActions.click_on_locator(self, digital_check_lcs["bank_10"])

    def bank_11_click(self):
        DigitalCheckModal.bank_name_btn_click(self)
        CommonActions.click_on_locator(self, digital_check_lcs["bank11"])

    def set_bank_branch(self, branch):
        CommonActions.set_locator(self, digital_check_lcs["bank_branch_fld"]).send_keys(branch)

    def set_acc_num(self, accnum):
        CommonActions.set_locator(self, digital_check_lcs["acc_num_fld"] ).send_keys(accnum)

    def set_holder_name(self, holdername):
        CommonActions.set_locator(self, digital_check_lcs["acc_holder_name_fld"]).send_keys(holdername)

    def immediate_payment_btn_click(self):
        CommonActions.click_on_locator(self, digital_check_lcs["immediate_payment_btn"])

    def flowing_30_click(self):
        CommonActions.click_on_locator(self, digital_check_lcs["flowing_30"])

    def flowing_60_click(self):
        CommonActions.click_on_locator(self, digital_check_lcs["flowing_60"])

    def flowing_90_click(self):
        CommonActions.click_on_locator(self, digital_check_lcs["flowing_90"])

    def insert_the_check_btn_click(self):
        CommonActions.click_on_locator(self, digital_check_lcs["insert_the_check_btn"])




