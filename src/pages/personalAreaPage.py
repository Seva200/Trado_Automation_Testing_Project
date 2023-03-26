from src.pages.commonActions import CommonActions
from src.locators.personalAreaPageLcs import personal_area_lcs
class PersonalAreaPage(CommonActions):
# Delivery Details
    def set_first_name(self, firstname):
        CommonActions.set_locator(self, personal_area_lcs["first_name_fld"]).send_keys(firstname)
    def set_last_name(self, lastname):
        CommonActions.set_locator(self, personal_area_lcs["last_name_fld"]).send_keys(lastname)
    def set_phone_num(self, phonenum):
        CommonActions.set_locator(self, personal_area_lcs["phone_fld"]).send_keys(phonenum)
    def set_email(self, email):
        CommonActions.set_locator(self, personal_area_lcs["email_fld"]).send_keys(email)
    def set_bn_id_num(self, bnid):
        CommonActions.set_locator(self, personal_area_lcs["bn_id_num"]).send_keys(bnid)

# Business Details
    def set_city_and_street(self, *args):
        CommonActions.set_locator(self, personal_area_lcs["city_&_street_fld"]).send_keys(*args)
    def set_number(self, num):
        CommonActions.set_locator(self, personal_area_lcs["num_fld"]).send_keys(num)
    def edit_btn_click(self):
        CommonActions.click_on_locator(self, personal_area_lcs["edit_btn"])

# My Wallet
    def withdraw_btn_click(self):
        CommonActions.click_on_locator(self, personal_area_lcs["withdraw_btn"])

# 4 Latest Orders
    def click_on_order(self):
        CommonActions.click_on_locator(self, personal_area_lcs["order_btn"])
    def support_link_click(self):
        CommonActions.click_on_locator(self, personal_area_lcs["support_link"])