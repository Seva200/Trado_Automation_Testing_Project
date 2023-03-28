from time import sleep
from src.utils.drivers.edgeDriverSetUp import EdgeDriverSetUp
from src.locators.homePageLcs import home_lcs
from src.locators.personalAreaPageLcs import personal_area_lcs


class TestHomePage(EdgeDriverSetUp):
# Header
    def test_logo_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.logo_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/"

    def test_search_fld_valid1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.set_search_fld("milk")
        self.home_page.search_fld_click()
        assert "milk" in self.common_actions.get_attribute_by_textcontent(home_lcs["first_search_result"])

    def test_search_fld_valid2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.set_search_fld("אק")
        self.home_page.search_fld_click()
        assert "אק" in self.common_actions.get_attribute_by_textcontent(home_lcs["first_search_result"])

    def test_search_fld_invalid(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.set_search_fld("--")
        self.home_page.search_fld_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["search_results_amount"]) == "0 תוצאות"
    def test_personal_area_btn(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_link()
        assert driver.current_url == "https://qa.trado.co.il/user/personalArea"
    def test2_personal_area_btn(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_link()
        assert driver.current_url == "https://qa.trado.co.il/user/personalArea"
        assert self.common_actions.get_attribute_by_class(personal_area_lcs["user_product_list"]) == "userProducts_userProductsList "
        self.home_page.logo_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/"
        self.home_page.personal_area_link()
        sleep(2)
        assert self.common_actions.get_attribute_by_class(personal_area_lcs["user_product_list"]) == "userProducts_userProductsList "

    def test_sales_btn(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sales_btn_click()
        assert self.common_actions.get_attribute_by_innertext(home_lcs["page_title"]) == "מבצעים"

    def test_dry_products_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.dry_products_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "מוצרים יבשים"

    def test_beauty_products_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.beauty_products_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "מוצרי טיפוח"

    def test_sweets_and_snacks_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.sweets_and_snacks_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "ממתקים וחטיפים"

    def test_frozen_btn(self, driver):
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "קפואים"

    def test_cannabis_click(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.cannabis_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "קנאביס "

    def test_cleaners_btn_click(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.cleaners_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "מוצרי ניקוי"

    def test_drinks_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.drinks_click()
        assert self.common_actions.get_attribute_by_innertext(home_lcs["page_title"]) == "משקאות"

    def test_upload_products_click(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.upload_prod_btn_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["upload_title"]) == " הוספת מוצר חדש "

# Body
    # Slide Show
    def test_left_arrow_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["slide1"]) == "slide selected"
        self.home_page.left_arrow_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["slide8"]) == "slide selected"

    def test_right_arrow_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["slide1"]) == "slide selected"
        self.home_page.right_arrow_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["slide2"]) == "slide selected"

    def test_slideshow_1link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.slide1_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        assert "MAX" in self.common_actions.get_attribute_by_textcontent(home_lcs["max_card_modal"])

    def test_slideshow_3link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.right_arrow_click()
        self.home_page.right_arrow_click()
        sleep(1)
        self.home_page.slide3_click()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url != "https://qa.trado.co.il/"

    def test_slideshow_8link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.left_arrow_click()
        sleep(1)
        self.home_page.slide8_click()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.max.co.il/cards/card/8649"

    def test_tell_me_more_link(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.tell_me_more_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["sign_in_modal_title"]) == "ברוכים השבים! מתרגשים לראות אתכם כאן"

    def test_product_list_1view(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.list_view1_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["product_list_actv"]) == "icon_wrapper productsList_active"

    def test_product_list_2view(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.list_view2_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["product_list_actv"]) == "icon_wrapper productsList_active"

    def test_max_card_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.max_card_link_click()
        assert driver.current_url == "https://www.max.co.il/cards/card/8649"

    def test_common_questions_bd_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.common_questions_bd_link()
        assert driver.current_url == "https://qa.trado.co.il/questions"
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["questions_pg_title"]) == "יש לכם שאלות ? הגעתם למקום הנכון"

    def test_contact_us_bd_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.contact_us_bd_link()
        assert driver.current_url == "https://qa.trado.co.il/contact"
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["contact_pg_title"]) == "נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה."

    def test_shipment_works_bd_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.shipment_works_bd_link()
        assert driver.current_url == "https://qa.trado.co.il/shipment"
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["shipment_pg_title"]) == "  שיטת השילוח שלנו נורא פשוטה.מהספק או מהמחסן הלוגיסטי,אליך עד 72 שעות."

# Footer
# Importants
    def test_who_we_are_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.who_we_are_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.trado.co.il/page"

    def test_personal_area_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        assert self.common_actions.set_locator(home_lcs["product_list_actv"])
        self.home_page.personal_area_link()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        self.sign_up_modal.x_btn_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_hide"]) == 'modal_modalWrapper false     '
        assert self.common_actions.set_locator(home_lcs["product_list_actv"])

# Additionals

    def test_common_questions_ftr_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.common_questions_ftr_link()
        assert driver.current_url == "https://qa.trado.co.il/questions"
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["questions_pg_title"]) == "יש לכם שאלות ? הגעתם למקום הנכון"

    def test_max_for_business_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.max_for_business_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.max.co.il/cards/card/8649"

# Stay in Touch
    def test_facebook_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.facebook_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.facebook.com/"

    def test_instagram_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.instagram_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.instagram.com/"

    def test_twitter_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.twitter_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://twitter.com/?lang=he"

    def test_term_of_use_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.term_of_use_link()
        assert driver.current_url == "https://qa.trado.co.il/info/%D7%AA%D7%A7%D7%A0%D7%95%D7%9F"

    def test_privacy_policy_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.privacy_policy_link()
        assert driver.current_url == "https://qa.trado.co.il/info/%D7%9E%D7%93%D7%99%D7%A0%D7%99%D7%95%D7%AA%20%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA"

    def test_accessibility_statement_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.accessibility_statement_link()
        assert driver.current_url == "https://qa.trado.co.il/info/%D7%94%D7%A6%D7%94%D7%A8%D7%AA%20%D7%A0%D7%92%D7%99%D7%A9%D7%95%D7%AA"



