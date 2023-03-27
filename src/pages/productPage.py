from src.utils.commonActions import CommonActions
from src.locators.productPageLcs import product_lcs


class ProductPage(CommonActions):
    def click_on_product(self):
        CommonActions.click_on_locator(self, product_lcs["product_btn"])

    def plus_btn_click(self):
        CommonActions.click_on_locator(self, product_lcs["plus_btn"])

    def minus_btn_click(self):
        CommonActions.click_on_locator(self, product_lcs["minus_btn"])

    def add_1item(self):
        ProductPage.click_on_product(self)
        ProductPage.plus_btn_click(self)


