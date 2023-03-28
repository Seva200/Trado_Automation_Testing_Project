from selenium.webdriver.common.by import By
# personal_area_lcs[""] = (By.CSS_SELECTOR, "")
personal_area_lcs = dict()

# Delivery Details
personal_area_lcs["first_name_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(1) > span > input")
personal_area_lcs["last_name_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(2) > span > input")
personal_area_lcs["phone_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(3) > span > input[type=tel]")
personal_area_lcs["email_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(4) > span > input[type=email]")
personal_area_lcs["bn_id_num"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(5) > span > input[type=number]")
# Business Details
personal_area_lcs["city_&_street_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(2) > div > div.form_formGroup.userAddressForm_addressBAF > div:nth-child(1) > input")
personal_area_lcs["num_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(2) > div > div.form_formGroup.userAddressForm_addressBAF > div:nth-child(2) > span > input[type=number]")
personal_area_lcs["edit_btn"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[4]')
personal_area_lcs["save_btn"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/input ')
# My Wallet
personal_area_lcs["withdraw_btn"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userPersonalArea_userPersonalAreaContainer > div.userWallet_userWallet > section > button")
# 4 Latest Orders
personal_area_lcs["order_btn"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userPersonalArea_userPersonalAreaContainer > div:nth-child(3) > div.userOrders_list > div:nth-child(1)")

personal_area_lcs["support_link"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userPersonalArea_userPersonalAreaContainer > div.userProducts_userProductsList > div.sectionFooter_sectionFooter > span")

# asserts
personal_area_lcs["user_product_list"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userPersonalArea_userPersonalAreaContainer > div.userProducts_userProductsList")
personal_area_lcs["street_num_inv_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(2) > div > div.form_formGroup.userAddressForm_addressBAF > div:nth-child(2) > div")
personal_area_lcs["invalid_email_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(4) > div")
personal_area_lcs["inv_phone_num_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(3) > div")
personal_area_lcs["fname_inv_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(1) > div")
personal_area_lcs["lname_inv_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(2) > div")
personal_area_lcs["inv_bn_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.userAddressForm_userAddressForm.userAddressForm_userAddressFormPersonal > form > div:nth-child(1) > div:nth-child(5) > div")
personal_area_lcs[""] = (By.CSS_SELECTOR, "")
personal_area_lcs[""] = (By.CSS_SELECTOR, "")