from time import sleep
from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.homePageLcs import home_lcs
from src.locators.personalAreaPageLcs import personal_area_lcs
import allure


class TestHomePage(ChromeDriverSetUp):
    # Header
    @allure.description("the test is verify, if user can back into home page after click on logo buttton")
    def test_logo_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.logo_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/"

    @allure.description("test that verify if user can search valid item ")
    def test_search_fld_valid1(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.set_search_fld("milk")
        self.home_page.search_fld_click()
        assert "milk" in self.common_actions.get_attribute_by_textcontent(home_lcs["first_search_result"])

    @allure.description("the test is verify, if user can search valid item ")
    def test_search_fld_valid2(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.set_search_fld("אק")
        self.home_page.search_fld_click()
        assert "אק" in self.common_actions.get_attribute_by_textcontent(home_lcs["first_search_result"])

    @allure.description("the test is verify, that user can't search invalid item ")
    def test_search_fld_invalid(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.set_search_fld("--")
        self.home_page.search_fld_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["search_results_amount"]) == "0 תוצאות"

    @allure.description("the test is verify, that user can open the personal area page ")
    def test_personal_area_btn(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        assert driver.current_url == "https://qa.trado.co.il/user/personalArea"

    @allure.description("the test is verify, that user can open the personal area page,"
                        " after he click on the logo button ")
    def test2_personal_area_btn(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.personal_area_hdr_click()
        assert driver.current_url == "https://qa.trado.co.il/user/personalArea"
        assert self.common_actions.get_attribute_by_class(
            personal_area_lcs["user_product_list"]) == "userProducts_userProductsList "
        self.home_page.logo_btn_click()
        assert driver.current_url == "https://qa.trado.co.il/"
        self.home_page.personal_area_hdr_click()
        sleep(2)
        assert self.common_actions.get_attribute_by_class(
            personal_area_lcs["user_product_list"]) == "userProducts_userProductsList "

    @allure.description("the test is verify, if sales section button works"
                        " and button title is the same page title that he open")
    @allure.severity(severity_level='minor')
    def test_sales_btn(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.sales_btn_click()
        assert self.common_actions.get_attribute_by_innertext(home_lcs["page_title"]) == "מבצעים"

    @allure.description("the test is verify, if dry products section button works"
                        " and button title is the same page title that he open")
    @allure.severity(severity_level='minor')
    def test_dry_products_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.dry_products_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "מוצרים יבשים"

    @allure.description("the test is verify, if beauty section button works"
                        " and button title is the same page title that he open")
    @allure.severity(severity_level='minor')
    def test_beauty_products_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.beer_products_click()
        self.welcome_to_modal.x_btn_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "בירות "
        assert "beer" in self.common_actions.get_attribute_by_textcontent(home_lcs["product_from_beer_pg"])


    @allure.description("the test is verify, if sweet and snacks section button works"
                        " and button title is the same page title that he open")
    @allure.severity(severity_level='minor')
    def test_sweets_and_snacks_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.sweets_and_snacks_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "חטיפים "


    @allure.description("the test is verify, if frozen section button works"
                        " and button title is the same page title that he open")
    @allure.severity(severity_level='minor')
    def test_frozen_btn(self, driver):
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["cannabis_btn_title"]) == "קפואים"

    @allure.description("the test is verify, if cannabis section button works"
                        " and button title is the same page title that he open")
    @allure.severity(severity_level='minor')
    def test_cannabis_click(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.cannabis_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "קנאביס "

    @allure.description("the test is verify, if cleaners section button works"
                        " and button title is the same page title that he open")
    @allure.severity(severity_level='minor')
    def test_cleaners_btn_click(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.cleaners_click()
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["page_title"]) == "מוצרי ניקוי"

    @allure.description("the test is verify, if drinks section button works"
                        " and button title is the same page title that he open")
    @allure.severity(severity_level='minor')
    def test_drinks_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.drinks_click()
        assert self.common_actions.get_attribute_by_innertext(home_lcs["page_title"]) == "משקאות"

    @allure.description("the test is verify, if upload product button works"
                        " and button title is the same page title that he open")
    def test_upload_products_click(self, driver):
        self.sign_in_modal.sign_in()
        self.home_page.upload_prod_btn_click()
        assert self.common_actions.get_attribute_by_class(
            home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        assert self.common_actions.get_attribute_by_textcontent(home_lcs["upload_title"]) == " הוספת מוצר חדש "

    # Body
    # Slide Show
    @allure.description('the test is verify, if user can change slide by click on arrow in slide show')
    @allure.severity(severity_level='minor')
    def test_left_arrow_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["slide1"]) == "slide selected"
        self.home_page.left_arrow_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["slide8"]) == "slide selected"

    @allure.description('the test is verify, if user can change slide by click on arrow in slide show')
    @allure.severity(severity_level='minor')
    def test_right_arrow_btn(self, driver):
        self.welcome_to_modal.x_btn_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["slide1"]) == "slide selected"
        self.home_page.right_arrow_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["slide2"]) == "slide selected"

    @allure.description("the test is verify, if user can click on 1 slide from slide show")
    @allure.severity(severity_level='minor')
    def test_slideshow_1link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.slide1_click()
        assert self.common_actions.get_attribute_by_class(
            home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        assert "MAX" in self.common_actions.get_attribute_by_textcontent(home_lcs["max_card_modal"])

    @allure.description("the test is verify, if user can click on 3 slide from slide show")
    @allure.severity(severity_level='minor')
    def test_slideshow_3link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.right_arrow_click()
        self.home_page.right_arrow_click()
        sleep(1)
        self.home_page.slide3_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "

    @allure.description("the test is verify, if user can click on 8 slide from slide show")
    @allure.severity(severity_level='minor')
    def test_slideshow_8link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.left_arrow_click()
        sleep(1)
        self.home_page.slide8_click()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.max.co.il/cards/card/8649"

    @allure.description("the test is verify, if tell me more link is work")
    @allure.severity(severity_level='minor')
    def test_tell_me_more_link(self, driver):
        self.welcome_to_modal.x_btn_click()
        self.home_page.tell_me_more_click()
        assert self.common_actions.get_attribute_by_class(
            home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        assert self.common_actions.get_attribute_by_textcontent(
            home_lcs["sign_in_modal_title"]) == "ברוכים השבים! מתרגשים לראות אתכם כאן"

    @allure.description("the test is verify, if user can change the product list view")
    @allure.severity(severity_level='minor')
    def test_product_list_1view(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.list_view1_click()
        assert self.common_actions.get_attribute_by_class(
            home_lcs["product_list_actv"]) == "icon_wrapper productsList_active"

    @allure.description("the test is verify, if user can change the product list view")
    @allure.severity(severity_level='minor')
    def test_product_list_2view(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.list_view2_click()
        assert self.common_actions.get_attribute_by_class(
            home_lcs["product_list_actv"]) == "icon_wrapper productsList_active"

    @allure.description("the test is verify, if user can sort the product list by price from low to high")
    def test_sort_list_low_to_high(self, driver):
        self.welcome_to_modal.choose_coktails()
        sleep(2)
        self.home_page.low_to_high_price_click()
        sleep(2)
        a = "279"
        b = "269"
        assert a in self.common_actions.get_attribute_by(home_lcs["gorilla_prod"], "textContent")
        assert b in self.common_actions.get_attribute_by(home_lcs["alfa_oil_prod"], "textContent")
        assert int(a) < int(b)

    @allure.description("the test is verify, if max card link is work")
    @allure.severity(severity_level='minor')
    def test_max_card_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.max_card_link_click()
        assert driver.current_url == "https://www.max.co.il/cards/card/8649"

    @allure.description("the test is verify, if common questions link is work")
    @allure.severity(severity_level='minor')
    def test_common_questions_bd_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.common_questions_bd_link()
        assert driver.current_url == "https://qa.trado.co.il/questions"
        assert self.common_actions.get_attribute_by_textcontent(
            home_lcs["questions_pg_title"]) == "יש לכם שאלות ? הגעתם למקום הנכון"

    @allure.description("the test is verify, if contact us link is work")
    @allure.severity(severity_level='minor')
    def test_contact_us_bd_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.contact_us_bd_link()
        assert driver.current_url == "https://qa.trado.co.il/contact"
        assert self.common_actions.get_attribute_by_textcontent(
            home_lcs["contact_pg_title"]) == "נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה."

    @allure.description("the test is verify, if how shipment works link is work")
    @allure.severity(severity_level='minor')
    def test_shipment_works_bd_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.shipment_works_bd_link()
        assert driver.current_url == "https://qa.trado.co.il/shipment"
        assert self.common_actions.get_attribute_by_textcontent(
            home_lcs["shipment_pg_title"]) == "  שיטת השילוח שלנו נורא פשוטה.מהספק או מהמחסן הלוגיסטי,אליך עד 72 שעות."

    # Footer
    # Importants
    @allure.description("the test is verify, if who we are link is work")
    @allure.severity(severity_level='minor')
    def test_who_we_are_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.who_we_are_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.trado.co.il/page"

    @allure.description("the test is verify, if personal area link is work")
    @allure.severity(severity_level='minor')
    def test_personal_area_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        assert self.common_actions.set_locator(home_lcs["product_list_actv"])
        self.home_page.personal_area_link()
        assert self.common_actions.get_attribute_by_class(
            home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        self.sign_up_modal.x_btn_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_hide"]) == 'modal_modalWrapper false     '
        assert self.common_actions.set_locator(home_lcs["product_list_actv"])

    # Additionals
    @allure.description("the test is verify, if common questions link is work")
    @allure.severity(severity_level='minor')
    def test_common_questions_ftr_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.common_questions_ftr_link()
        assert driver.current_url == "https://qa.trado.co.il/questions"
        assert self.common_actions.get_attribute_by_textcontent(
            home_lcs["questions_pg_title"]) == "יש לכם שאלות ? הגעתם למקום הנכון"

    @allure.description("the test is verify, if max card link is work")
    @allure.severity(severity_level='minor')
    def test_max_for_business_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.max_for_business_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.max.co.il/cards/card/8649"

    # Stay in Touch
    @allure.description("the test is verify, if facebook link is work")
    @allure.severity(severity_level='minor')
    def test_facebook_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.facebook_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.facebook.com/"

    @allure.description("the test is verify, if instagram link is work")
    @allure.severity(severity_level='minor')
    def test_instagram_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.instagram_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://www.instagram.com/"

    @allure.description("the test is verify, if twitter link is work")
    def test_twitter_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.twitter_link()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://twitter.com/?lang=he"

    @allure.description("the test is verify, if term of use link is work")
    def test_term_of_use_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.term_of_use_link()
        assert driver.current_url == "https://qa.trado.co.il/info/%D7%AA%D7%A7%D7%A0%D7%95%D7%9F"

    @allure.description("the test is verify, if privacy policy link is work")
    def test_privacy_policy_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.privacy_policy_link()
        assert driver.current_url == "https://qa.trado.co.il/info/%D7%9E%D7%93%D7%99%D7%A0%D7%99%D7%95%D7%AA%20%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA"

    @allure.description("the test is verify, if accessibility statement link is work")
    def test_accessibility_statement_link(self, driver):
        self.welcome_to_modal.choose_coktails()
        self.home_page.accessibility_statement_link()
        assert driver.current_url == "https://qa.trado.co.il/info/%D7%94%D7%A6%D7%94%D7%A8%D7%AA%20%D7%A0%D7%92%D7%99%D7%A9%D7%95%D7%AA"
