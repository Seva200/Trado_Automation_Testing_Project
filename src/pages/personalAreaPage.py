import time

from src.utils.commonActions import CommonActions
from src.locators.personalAreaPageLcs import personal_area_lcs
class PersonalAreaPage(CommonActions):
# Delivery Details
    def set_first_name(self, firstname):
        CommonActions.set_locator(self, personal_area_lcs["first_name_fld"]).clear()
        CommonActions.set_locator(self, personal_area_lcs["first_name_fld"]).send_keys(firstname)
    def set_last_name(self, lastname):
        CommonActions.set_locator(self, personal_area_lcs["last_name_fld"]).clear()
        CommonActions.set_locator(self, personal_area_lcs["last_name_fld"]).send_keys(lastname)
    def set_phone_num(self, phonenum):
        CommonActions.set_locator(self, personal_area_lcs["phone_fld"]).clear()
        CommonActions.set_locator(self, personal_area_lcs["phone_fld"]).send_keys(phonenum)
    def set_email(self, email):
        CommonActions.set_locator(self, personal_area_lcs["email_fld"]).clear()
        CommonActions.set_locator(self, personal_area_lcs["email_fld"]).send_keys(email)
    def set_bn_id_num(self, bnid):
        CommonActions.set_locator(self, personal_area_lcs["bn_id_num"]).clear()
        CommonActions.set_locator(self, personal_area_lcs["bn_id_num"]).send_keys(bnid)

# Business Details
    def set_city_and_street(self, city_and_street):
        CommonActions.set_locator(self, personal_area_lcs["city_&_street_fld"]).clear()
        CommonActions.set_locator(self, personal_area_lcs["city_&_street_fld"]).send_keys(city_and_street)
    def set_street_number(self, num):
        CommonActions.set_locator(self, personal_area_lcs["num_fld"]).clear()
        CommonActions.set_locator(self, personal_area_lcs["num_fld"]).send_keys(num)
    def edit_btn_click(self):
        CommonActions.click_on_visible_locator_ac(self, personal_area_lcs["edit_btn"])
    def save_btn_click(self):
        CommonActions.click_on_visible_locator_ac(self, personal_area_lcs["save_btn"])
    def edit_personal_area(self, fname, lname, phone, email, bnid, city_and_street, street_num):
        PersonalAreaPage.edit_btn_click(self)
        PersonalAreaPage.set_first_name(self, fname)
        PersonalAreaPage.set_last_name(self, lname)
        PersonalAreaPage.set_phone_num(self, phone)
        PersonalAreaPage.set_email(self, email)
        PersonalAreaPage.set_bn_id_num(self, bnid)
        PersonalAreaPage.set_city_and_street(self, city_and_street)
        PersonalAreaPage.set_street_number(self, street_num)
        PersonalAreaPage.save_btn_click(self)

# My Wallet
    def withdraw_btn_click(self):
        CommonActions.click_on_locator(self, personal_area_lcs["withdraw_btn"])

# 4 Latest Orders
    def click_on_order(self):
        CommonActions.click_on_locator(self, personal_area_lcs["order_btn"])
    def support_link_click(self):
        CommonActions.click_on_locator(self, personal_area_lcs["support_link"])