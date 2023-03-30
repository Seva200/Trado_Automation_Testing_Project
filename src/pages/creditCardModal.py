from src.utils.commonActions import CommonActions
from src.locators.creditCardModalLcs import credit_card_lcs
class CreditCardModal(CommonActions):
    def x_btn_click(self):
        CommonActions.click_on_locator(self, credit_card_lcs["x_btn"])
    def set_card_num(self, cardnum):
        # CommonActions.click_on_visible_locator_ac(self, credit_card_lcs["card_num_fld"])
        # CommonActions.set_locator(self, credit_card_lcs["card_num_fld"]).clear()
        CommonActions.set_locator_invis(self, credit_card_lcs["card_num_fld"]).send_keys(cardnum)
    def set_id_num(self, idnum):
        CommonActions.set_locator(self, credit_card_lcs["id_num_fld"]).send_keys(idnum)
    def month_btn_click(self):
        CommonActions.click_on_locator(self, credit_card_lcs["month"])
    def choose_5_month(self):
        CreditCardModal.month_btn_click(self)
        CommonActions.click_on_locator(self, credit_card_lcs["month5"])
    def year_btn_click(self):
        CommonActions.click_on_locator(self, credit_card_lcs["year"])
    def choose_24_year(self):
        CreditCardModal.year_btn_click(self)
        CommonActions.click_on_locator(self, credit_card_lcs["year24"])
    def set_cvv(self, cvvnum):
        CommonActions.set_locator(self, credit_card_lcs["cvv"]).send_keys(cvvnum)
    def set_credit_card(self, cardnum, idnum, cvv):
        CreditCardModal.set_card_num(self, cardnum)
        CreditCardModal.set_id_num(self, idnum)
        CreditCardModal.set_cvv(self, cvv)
        CreditCardModal.choose_5_month(self)
        CreditCardModal.choose_24_year(self)

    def submit_btn_click(self):
        CommonActions.click_on_locator(self, credit_card_lcs["submit"])