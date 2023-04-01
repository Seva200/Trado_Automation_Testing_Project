import time
from src.utils.commonActions import CommonActions
from src.locators.homePageLcs import home_lcs
from selenium.webdriver.common.keys import Keys
class HomePage(CommonActions):

# Header
    def logo_btn_click(self):
        CommonActions.click_on_locator(self, home_lcs["logo_btn"])
    def set_search_fld(self, msg):
        CommonActions.set_locator(self, home_lcs["search_fld"]).send_keys(msg)
    def log_out_btn_click(self):
        CommonActions.click_on_invis_locator_ac(self, home_lcs["log_out_btn"])
    def personal_area_hdr_click(self):
        CommonActions.click_on_visible_locator_ac(self, home_lcs["personal_area_hdr"])

    def search_fld_click(self):
        HomePage.logo_btn_click(self)
        time.sleep(1)
        CommonActions.click_on_locator(self, home_lcs["search_fld"])

    def sign_in_click(self):
        CommonActions.click_on_locator(self, home_lcs["sign_in_btn"])
    def sales_btn_click(self):
        CommonActions.click_on_locator(self, home_lcs["section1"])
    def dry_products_click(self):
        CommonActions.click_on_locator(self, home_lcs["section2"])
    def beauty_products_click(self):
        CommonActions.click_on_locator(self, home_lcs["section3"])
    def sweets_and_snacks_click(self):
        CommonActions.click_on_locator(self, home_lcs["section4"])
    def cannabis_click(self):
        CommonActions.click_on_locator(self, home_lcs["section5"])
    def cleaners_click(self):
        CommonActions.click_on_locator(self, home_lcs["section6"])
    def drinks_click(self):
        CommonActions.click_on_locator(self, home_lcs["section7"])
    def upload_prod_btn_click(self):
        CommonActions.click_on_locator(self, home_lcs["upload_prod"])

# Body
    # Slide Show
    def left_arrow_click(self):
        CommonActions.click_on_locator(self, home_lcs["left_arrow"])
    def right_arrow_click(self):
        CommonActions.click_on_locator(self, home_lcs["right_arrow"])
    def slide1_click(self):
        CommonActions.click_on_locator(self, home_lcs["slide1"])
    def slide2_click(self):
        CommonActions.click_on_locator(self, home_lcs["slide2"])
    def slide3_click(self):
        CommonActions.click_on_locator(self, home_lcs["slide3"])
    def slide4_click(self):
        CommonActions.click_on_locator(self, home_lcs["slide4"])
    def slide5_click(self):
        CommonActions.click_on_locator(self, home_lcs["slide5"])
    def slide6_click(self):
        CommonActions.click_on_locator(self, home_lcs["slide6"])
    def slide7_click(self):
        CommonActions.click_on_locator(self, home_lcs["slide7"])
    def slide8_click(self):
        CommonActions.click_on_locator(self, home_lcs["slide8"])
    def tell_me_more_click(self):
        CommonActions.click_on_locator(self, home_lcs["tell_me_more"])
    def sort_btn_click(self):
        CommonActions.click_on_locator(self, home_lcs["sort_select"])
    def sort_by_popularity_click(self):
        CommonActions.click_on_locator(self, home_lcs["popular_sort"])
    def low_to_high_price_click(self):
        CommonActions.click_on_locator(self, home_lcs["low_to_high_price"])
    def high_to_low_price_click(self):
        CommonActions.click_on_locator(self, home_lcs["high_to_low_price"])
    def list_view1_click(self):
        CommonActions.click_on_locator(self, home_lcs["list_view1"])
    def list_view2_click(self):
        CommonActions.click_on_locator(self, home_lcs["list_view2"])
    def max_card_link_click(self):
        CommonActions.click_on_locator(self, home_lcs["max_card_link"])
    def common_questions_bd_link(self):
        CommonActions.click_on_locator(self, home_lcs["common_questions_bd"])
    def contact_us_bd_link(self):
        CommonActions.click_on_locator(self, home_lcs["contact_us_bd"])
    def shipment_works_bd_link(self):
        CommonActions.click_on_locator(self, home_lcs["shipment_works_bd"])
    def change_language_btn(self):
        CommonActions.click_on_visible_locator_ac(self, home_lcs["change_language"])

# Footer
# Importants
    def who_we_are_link(self):
        CommonActions.click_on_locator(self, home_lcs["who_we_are"])
    def personal_area_link(self):
        CommonActions.click_on_locator(self, home_lcs["personal_area"])
    def eTrado_link(self):
        CommonActions.click_on_locator(self, home_lcs["eTrado"])
    def contact_us_ftr_link(self):
        CommonActions.click_on_locator(self, home_lcs["contact_us_ftr"])
    def business_interface_link(self):
        CommonActions.click_on_locator(self, home_lcs["business interface"])
# Additionals
    def common_questions_ftr_link(self):
        CommonActions.click_on_locator(self, home_lcs["common_questions_ftr"])
    def shipment_works_ftr_link(self):
        CommonActions.click_on_locator(self, home_lcs["shipment_works_ftr"])
    def payment_solutions_link(self):
        CommonActions.click_on_locator(self, home_lcs["payment_solutions"])
    def max_for_business_link(self):
        CommonActions.click_on_locator(self, home_lcs["max_for_business"])
# Stay in Touch
    def facebook_link(self):
        CommonActions.click_on_locator(self, home_lcs["facebook"])
    def instagram_link(self):
        CommonActions.click_on_locator(self, home_lcs["instagram"])
    def twitter_link(self):
        CommonActions.click_on_locator(self, home_lcs["twitter"])
    def term_of_use_link(self):
        CommonActions.click_on_locator(self, home_lcs["terms_of_use"])
    def privacy_policy_link(self):
        CommonActions.click_on_locator(self, home_lcs["privacy_policy"])
    def accessibility_statement_link(self):
        CommonActions.click_on_locator(self, home_lcs["accessibility_statement"])

