from src.utils.commonActions import CommonActions
from src.locators.deliveryDetailsPageLcs import deli_dtls_lcs
class DeliveryDetailsPage(CommonActions):
# Invoice Details
    def set_bn_name(self, bnname):
        CommonActions.set_locator(self, deli_dtls_lcs["bn_name_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["bn_name_fld"]).send_keys(bnname)
    def set_bn_num(self, bnnum):
        CommonActions.set_locator(self, deli_dtls_lcs["bn_num_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["bn_num_fld"]).send_keys(bnnum)
    def set_email(self, email):
        CommonActions.set_locator(self, deli_dtls_lcs["email_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["email_fld"]).send_keys(email)
    def set_city_inv(self, city):
        CommonActions.set_locator(self, deli_dtls_lcs["city_inv_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["city_inv_fld"]).send_keys(city)
    def set_steet_inv(self, street):
        CommonActions.set_locator(self, deli_dtls_lcs["street_inv_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["street_inv_fld"]).send_keys(street)
    def set_house_num_inv(self, strnum):
        CommonActions.set_locator(self, deli_dtls_lcs["num_inv_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["num_inv_fld"]).send_keys(strnum)
    def set_entrance_inv(self, entrncenum):
        CommonActions.set_locator(self, deli_dtls_lcs["entrance_inv_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["entrance_inv_fld"]).send_keys(entrncenum)
    def set_floor_inv(self, floornum):
        CommonActions.set_locator(self, deli_dtls_lcs["floor_inv_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["floor_inv_fld"]).send_keys(floornum)
    def set_invoice_details(self, bnname, bnnum, email, city, street, strnum, entrancenum, floornum):
        DeliveryDetailsPage.set_bn_name(self, bnname)
        DeliveryDetailsPage.set_bn_num(self, bnnum)
        DeliveryDetailsPage.set_email(self, email)
        DeliveryDetailsPage.set_city_inv(self, city)
        DeliveryDetailsPage.set_steet_inv(self, street)
        DeliveryDetailsPage.set_house_num_inv(self, strnum)
        DeliveryDetailsPage.set_entrance_inv(self, entrancenum)
        DeliveryDetailsPage.set_floor_inv(self, floornum)

# Delivery Address
    def set_city_adrs(self, city):
        CommonActions.set_locator(self, deli_dtls_lcs["city_adrs_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["city_adrs_fld"]).send_keys(city)
    def set_street_adrs(self, street):
        CommonActions.set_locator(self, deli_dtls_lcs["street_adrs_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["street_adrs_fld"]).send_keys(street)
    def set_house_num_adrs(self, num):
        CommonActions.set_locator(self, deli_dtls_lcs["num_adrs_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["num_adrs_fld"]).send_keys(num)
    def set_entrance_adrs(self, entrance):
        CommonActions.set_locator(self, deli_dtls_lcs["entrance_adrs_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["entrance_adrs_fld"]).send_keys(entrance)
    def set_floor_adrs(self, floor):
        CommonActions.set_locator(self, deli_dtls_lcs["floor_adrs_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["floor_adrs_fld"]).send_keys(floor)
    def set_contact_name(self, contactname):
        CommonActions.set_locator(self, deli_dtls_lcs["contact_name_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["contact_name_fld"]).send_keys(contactname)
    def set_first_name(self, firstname):
        CommonActions.set_locator(self, deli_dtls_lcs["first_name_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["first_name_fld"]).send_keys(firstname)
    def set_last_name(self, lastname):
        CommonActions.set_locator(self, deli_dtls_lcs["last_name_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["last_name_fld"]).send_keys(lastname)
    def set_phone_adrs(self, number):
        CommonActions.set_locator(self, deli_dtls_lcs["number_adrs_fld"]).clear()
        CommonActions.set_locator(self, deli_dtls_lcs["number_adrs_fld"]).send_keys(number)
    def set_address_details(self, city, street, streetnum, entrance, floor, contactname, fname, lname, phone):
        DeliveryDetailsPage.set_city_adrs(self, city)
        DeliveryDetailsPage.set_street_adrs(self, street)
        DeliveryDetailsPage.set_house_num_adrs(self, streetnum)
        DeliveryDetailsPage.set_entrance_adrs(self, entrance)
        DeliveryDetailsPage.set_floor_adrs(self, floor)
        DeliveryDetailsPage.set_contact_name(self, contactname)
        DeliveryDetailsPage.set_first_name(self, fname)
        DeliveryDetailsPage.set_last_name(self, lname)
        DeliveryDetailsPage.set_phone_adrs(self, phone)

    def complete_purchase_btn_click(self):
        CommonActions.click_on_locator(self, deli_dtls_lcs["complete_purchase"])
    def buy_more_btn_click(self):
        CommonActions.click_on_locator(self, deli_dtls_lcs["buy_more"])