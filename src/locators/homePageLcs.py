from selenium.webdriver.common.by import By
# home_lcs[""] = (By.CSS_SELECTOR, "")
home_lcs = dict()

# Header
home_lcs["logo_btn"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > a.header_logoLink > div > a > img")
home_lcs["search_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > div > span > input")
home_lcs["sign_in_btn"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > header > div > div > a.header_userAreaLink > span:nth-child(2)")
home_lcs["section1"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div:nth-child(1) > div > div > div.verticalMenu_verticalMenuList > a.verticalMenu_active")
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
home_lcs["slide1"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(1)")
home_lcs["slide2"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(2)")
home_lcs["slide3"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(3)")
home_lcs["slide4"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(4)")
home_lcs["slide5"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(5)")
home_lcs["slide6"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(6)")
home_lcs["slide7"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(7)")
home_lcs["slide8"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(8)")
home_lcs["slide9"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(9)")
home_lcs["slide10"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.slider_slider > div > div > div > ul > li:nth-child(10)")

# Body
home_lcs["tell_me_more"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_sliderWrapper > div.addProductInfo_addProduct")
home_lcs["sort_select"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_sort > div > select")
home_lcs["popular_sort"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_sort > div > select > option:nth-child(1)")
home_lcs["low_to_high_price"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_sort > div > select > option:nth-child(2)")
home_lcs["high_to_low_price"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_sort > div > select > option:nth-child(3)")
home_lcs["list_view1"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_layout > span.icon_wrapper.productsList_active > i")
home_lcs["list_view2"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_btnsRow > div.productsList_layout > span:nth-child(1) > i")
home_lcs["max_card_link"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_moreInfo > div:nth-child(3) > div > a")
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
