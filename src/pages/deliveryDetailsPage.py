from src.pages.commonActions import CommonActions
from src.locators.deliveryDetailsPageLcs import deli_dtls_lcs
class DeliveryDetailsPage(CommonActions):
# Invoice Details
    def set_bn_name(self, bnname):
        CommonActions.set_locator(self, deli_dtls_lcs["bn_name_fld"]).send_keys(bnname)
    def set_bn_num(self, bnnum):
        CommonActions.set_locator(self, deli_dtls_lcs["bn_num_fld"]).send_keys(bnnum)
    def set_email(self, email):
        CommonActions.set_locator(self, deli_dtls_lcs["email_fld"]).send_keys(email)
    def set_city_inv(self, city):
        CommonActions.set_locator(self, deli_dtls_lcs["city_inv_fld"]).send_keys(city)
    def set_steet_inv(self, street):
        CommonActions.set_locator(self, deli_dtls_lcs["street_inv_fld"]).send_keys(street)
    def set_num_inv(self, num):
        CommonActions.set_locator(self, deli_dtls_lcs["num_inv_fld"]).send_keys(num)
    def set_entrance_inv(self, entrnsenum):
        CommonActions.set_locator(self, deli_dtls_lcs["entrance_inv_fld"]).send_keys(entrnsenum)
    def set_floor_inv(self, floornum):
        CommonActions.set_locator(self, deli_dtls_lcs["floor_inv_fld"]).send_keys(floornum)

# Delivery Address
    def set_city_adrs(self, city):
        CommonActions.set_locator(self, deli_dtls_lcs["city_adrs_fld"]).send_keys(city)
    def set_street_adrs(self, street):
        CommonActions.set_locator(self, deli_dtls_lcs["street_adrs_fld"]).send_keys(street)
    def set_num_adrs(self, num):
        CommonActions.set_locator(self, deli_dtls_lcs["num_adrs_fld"]).send_keys(num)
    def set_entrance_adrs(self, entrance):
        CommonActions.set_locator(self, deli_dtls_lcs["entrance_adrs_fld"]).send_keys(entrance)
    def set_floor_adrs(self, floor):
        CommonActions.set_locator(self, deli_dtls_lcs["floor_adrs_fld"]).send_keys(floor)
    def set_contact_name(self, contactname):
        CommonActions.set_locator(self, deli_dtls_lcs["contact_name_fld"]).send_keys(contactname)
    def set_first_name(self, firstname):
        CommonActions.set_locator(self, deli_dtls_lcs["first_name_fld"]).send_keys(firstname)
    def set_last_name(self, lastname):
        CommonActions.set_locator(self, deli_dtls_lcs["last_name_fld"]).send_keys(lastname)
    def set_number_adrs(self, number):
        CommonActions.set_locator(self, deli_dtls_lcs["number_adrs_fld"]).send_keys(number)
    def complete_purchase_btn_click(self):
        CommonActions.click_on_locator(self, deli_dtls_lcs["complete_purchase"])
    def buy_more_btn_click(self):
        CommonActions.click_on_locator(self, deli_dtls_lcs["buy_more"])