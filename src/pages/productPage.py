from src.utils.commonActions import CommonActions
from src.locators.productPageLcs import product_lcs


class ProductPage(CommonActions):
    def click_on_product(self):
        CommonActions.click_on_locator(self, product_lcs["product_btn"])

    def plus_btn_click(self):
        CommonActions.click_on_visible_locator_ac(self, product_lcs["plus_btn"])

    def minus_btn_click(self):
        CommonActions.click_on_visible_locator_ac(self, product_lcs["minus_btn"])
    def set_product_amount(self, amount):
        CommonActions.set_locator(self, product_lcs["product_amount_fld"]).send_keys(amount)


    def add_1item(self):
        ProductPage.click_on_product(self)
        ProductPage.plus_btn_click(self)

    def add_5items(self):
        count = 0
        while count < 5:
            ProductPage.plus_btn_click(self)
            count += 1
    def minus_2items(self):
        count = 2
        while count > 0:
            ProductPage.minus_btn_click(self)
            count -= 1

