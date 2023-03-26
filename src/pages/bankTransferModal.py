from src.utils.commonActions import CommonActions
from src.locators.bankTransferModalLcs import bank_transfer_lcs
class BankTransferModal(CommonActions):
    def x_btn_click(self):
        CommonActions.click_on_locator(self, bank_transfer_lcs["x_btn"])
    def bank_choose_click(self):
        CommonActions.click_on_locator(self, bank_transfer_lcs["bank_choose"])
    def set_bank_branch(self, branchnum):
        CommonActions.set_locator(self, bank_transfer_lcs["bank_branch_fld"]).send_keys(branchnum)
    def set_acc_num(self, accnum):
        CommonActions.set_locator(self, bank_transfer_lcs["acc_num_fld"]).send_keys(accnum)
    def set_acc_name(self, accname):
        CommonActions.set_locator(self, bank_transfer_lcs["acc_name_fld"]).send_keys(accname)
    def set_bn_num(self, bnnum):
        CommonActions.set_locator(self, bank_transfer_lcs["bn_num_fld"]).send_keys(bnnum)
    def confirm_transfer_btn_click(self):
        CommonActions.click_on_locator(self, bank_transfer_lcs["confirm_transfer"])