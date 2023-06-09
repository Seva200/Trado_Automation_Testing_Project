from selenium.webdriver.common.by import By
# deli_dtls_lcs[""] = (By.CSS_SELECTOR, "")
deli_dtls_lcs = dict()
# Invoice Details
deli_dtls_lcs["bn_name_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input")
deli_dtls_lcs["bn_num_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input[type=number]")
deli_dtls_lcs["email_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(2) > div:nth-child(3) > input[type=email]")
deli_dtls_lcs["city_inv_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(1) > input")
deli_dtls_lcs["street_inv_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(2) > input")
deli_dtls_lcs["num_inv_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(3) > input[type=number]")
deli_dtls_lcs["entrance_inv_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(4) > input")
deli_dtls_lcs["floor_inv_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(5) > input[type=number]")
# Delivery Address
deli_dtls_lcs["city_adrs_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input")
deli_dtls_lcs["street_adrs_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(2) > div:nth-child(2) > input")
deli_dtls_lcs["num_adrs_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(2) > div:nth-child(3) > input[type=number]")
deli_dtls_lcs["entrance_adrs_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(2) > div:nth-child(4) > input")
deli_dtls_lcs["floor_adrs_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(2) > div:nth-child(5) > input[type=number]")
deli_dtls_lcs["contact_name_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(3) > div:nth-child(1) > input")
deli_dtls_lcs["first_name_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(3) > div:nth-child(2) > input")
deli_dtls_lcs["last_name_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(3) > div:nth-child(3) > input")
deli_dtls_lcs["number_adrs_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(3) > div:nth-child(4) > input[type=tel]")
deli_dtls_lcs["complete_purchase"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div[3]/button/input')
deli_dtls_lcs["buy_more"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.checkout_checkout_back_step")

# asserts
deli_dtls_lcs["deliv_details_status"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.orderTimeline_orderTimeline.orderTimeline_checkoutTimeLineStyle > div.orderTimeline_time.orderTimeline_current.orderTimeline_current")
deli_dtls_lcs["payments_methods_status"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.orderTimeline_orderTimeline.orderTimeline_checkoutTimeLineStyle > div:nth-child(2)")
deli_dtls_lcs["invalid_bn_name_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3)")
deli_dtls_lcs["invalid_bn_num_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3)")
deli_dtls_lcs["invalid_email_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3)")
deli_dtls_lcs["invalid_city_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3)")
deli_dtls_lcs["invalid_street_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3)")
deli_dtls_lcs["invalid_house_num_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3)")
deli_dtls_lcs["invalid_entrance_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(4) > div:nth-child(3)")
deli_dtls_lcs["invalid_floor_msg"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(3) > div:nth-child(5) > div:nth-child(3)")
deli_dtls_lcs["order_summery_status"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.orderTimeline_orderTimeline.orderTimeline_checkoutTimeLineStyle > div:nth-child(3)")
deli_dtls_lcs["phone"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > label")
deli_dtls_lcs[""] = (By.CSS_SELECTOR, "")
deli_dtls_lcs[""] = (By.CSS_SELECTOR, "")
deli_dtls_lcs[""] = (By.CSS_SELECTOR, "")
