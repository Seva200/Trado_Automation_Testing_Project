from selenium.webdriver.common.by import By
# home_lcs[""] = (By.CSS_SELECTOR, "")
home_lcs = dict()

# Header
home_lcs["logo_btn"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > a.header_logoLink > div > a > img")
home_lcs["search_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > div > span > input")
home_lcs["sign_in_btn"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > a.header_userAreaLink > span:nth-child(2)")
home_lcs["log_out_btn"] = (By.CLASS_NAME, 'header_logOut')
home_lcs["personal_area_hdr"] = (By.CSS_SELECTOR, '#root > div > div.pages_pages > header > div > div > a.header_userAreaLink > span:nth-child(2)')
home_lcs["section1"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a:nth-child(1)")
home_lcs["section2"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a:nth-child(2)")
home_lcs["section3"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a:nth-child(3)")
home_lcs["section4"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a:nth-child(4)")
home_lcs["section5"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a:nth-child(5)")
home_lcs["section6"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a:nth-child(6)")
home_lcs["section7"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a:nth-child(7)")
home_lcs["upload_prod"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a.verticalMenu_addProduct > span")

# Body
    # Slide Show
home_lcs["left_arrow"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > button.control-arrow.control-prev")
home_lcs["right_arrow"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > button.control-arrow.control-next")
home_lcs["slide1"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div > div > div > div > ul > li:nth-child(2)")
home_lcs["slide2"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div > div > div > div > ul > li:nth-child(3)")
home_lcs["slide3"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[4]/a')
home_lcs["slide4"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div > div > div > div > ul > li:nth-child(5)")
home_lcs["slide5"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div > div > div > div > ul > li:nth-child(6)")
home_lcs["slide6"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div > div > div > div > ul > li:nth-child(7)")
home_lcs["slide7"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div > div > div > div > ul > li:nth-child(8)")
home_lcs["slide8"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div > div > div > div > ul > li:nth-child(9)")
# Body
home_lcs["tell_me_more"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.addProductInfo_addProduct")
home_lcs["sort_select"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_sort > div > select")
home_lcs["popular_sort"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_sort > div > select > option:nth-child(1)")
home_lcs["low_to_high_price"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_sort > div > select > option:nth-child(2)")
home_lcs["high_to_low_price"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_sort > div > select > option:nth-child(3)")
home_lcs["list_view1"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_layout > span.icon_wrapper.productsList_active > i")
home_lcs["list_view2"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_layout > span:nth-child(1) > i")
home_lcs["max_card_link"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_moreInfo > div.maxInfo_maxInfo > div:nth-child(3) > div > a")
home_lcs["common_questions_bd"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_moreInfo > div:nth-child(3) > div > a")
home_lcs["contact_us_bd"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_moreInfo > div:nth-child(4) > div > a")
home_lcs["shipment_works_bd"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_moreInfo > div:nth-child(5) > div > a")
home_lcs["change_language"] = (By.CSS_SELECTOR, "#root > div > div.languageChooser_languageChooser > div > span")

# Footer
# Importants
home_lcs["who_we_are"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div:nth-child(1) > a:nth-child(2)")
home_lcs["personal_area"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div:nth-child(1) > a:nth-child(3)")
home_lcs["eTrado"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div:nth-child(1) > a:nth-child(4)")
home_lcs["contact_us_ftr"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div:nth-child(1) > a:nth-child(5)")
home_lcs["business interface"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div:nth-child(1) > a:nth-child(6)")
# Additionals
home_lcs["common_questions_ftr"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div:nth-child(2) > a:nth-child(2)")
home_lcs["shipment_works_ftr"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div:nth-child(2) > a:nth-child(3)")
home_lcs["payment_solutions"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div:nth-child(2) > a:nth-child(4)")
home_lcs["max_for_business"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div:nth-child(2) > a:nth-child(5)")
# Stay In Touch
home_lcs["facebook"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div.footer_contact > a:nth-child(2)")
home_lcs["instagram"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div.footer_contact > a:nth-child(3)")
home_lcs["twitter"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div.footer_contact > a:nth-child(4)")
home_lcs["terms_of_use"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div.footer_copyrightsContainer > div > a:nth-child(1)")
home_lcs["privacy_policy"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div.footer_copyrightsContainer > div > a:nth-child(2)")
home_lcs["accessibility_statement"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.footer_footerWrapper > div > div.footer_copyrightsContainer > div > a:nth-child(3)")

# assert locators
home_lcs["first_search_result"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > div > div.mainSearch_results > div > a:nth-child(1) > div > div.productDesc_productDesc.inlineProduct_desc > div.productDesc_name")
home_lcs["search_results_amount"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > div > div.mainSearch_results > h3")
home_lcs["page_title"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div:nth-child(1) > h1")
home_lcs["cannabis_btn_title"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a:nth-child(3) > div:nth-child(1) > div")
home_lcs["modal_open"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open")
home_lcs["modal_hide"] = (By.XPATH, '//*[@id="root"]/div/div[4]')
home_lcs["upload_title"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div.addProduct_modal_container > div.addProduct_header > h2")
home_lcs["max_card_modal"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > h3")
home_lcs["product_price1"] = (By.CSS_SELECTOR, '#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list > a:nth-child(5) > div > div.product_top > div.productDesc_productDesc.undefined > div:nth-child(2) > div > div > span > span')
home_lcs["product_price2"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list > a:nth-child(4) > div > div.product_top > div.productDesc_productDesc.undefined > div:nth-child(2) > div > div > span")
home_lcs["sign_in_modal_title"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > div.login_titleContainer > h2")
home_lcs["product_list_actv"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_layout > span.icon_wrapper.productsList_active")
home_lcs["questions_pg_title"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.questions_header > div > h4")
home_lcs["contact_pg_title"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div:nth-child(1) > h4")
home_lcs["shipment_pg_title"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.shipment_header > div")
home_lcs["hello_user_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > a.header_userAreaLink")
home_lcs["person_area_link"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > a.header_userAreaLink > span:nth-child(2)")
home_lcs["gorilla_prod_price"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list > a:nth-child(5) > div > div.product_top > div.productDesc_productDesc.undefined > div:nth-child(2) > div > div > span > span")
home_lcs["alfa_oil_prod_price"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list > a:nth-child(4) > div > div.product_top > div.productDesc_productDesc.undefined > div:nth-child(2) > div > div > span > span")
home_lcs["product_from_beer_pg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list > a > div > div.product_top > div.productDesc_productDesc.undefined > div.productDesc_name")
home_lcs["dog_prod_price"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list > a:nth-child(5) > div > div.product_top > div.productDesc_productDesc.undefined > div:nth-child(2) > div > div > span")
home_lcs["goats_milk_prod_price"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list > a:nth-child(4) > div > div.product_top > div.productDesc_productDesc.undefined > div:nth-child(2) > div > div > span > span")
home_lcs["accessibility_statement_title"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.topImage_topImage.undefined > h1")
