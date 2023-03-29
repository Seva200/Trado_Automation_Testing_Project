from selenium.webdriver.common.by import By
# = (By.CSS_SELECTOR, "")
sign_in_lcs = dict()
# Page 1
sign_in_lcs["sign_in_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > div.login_loginregister > span.login_active")
sign_in_lcs["phone_number_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div:nth-child(1) > div:nth-child(1) > span > input[type=tel]")
sign_in_lcs["log_in_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > input")
sign_in_lcs["remember_me_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div:nth-child(1) > div.form_formItem.form_checkbox.undefined.false.undefined > span > span > span > i")
sign_in_lcs["submit_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > input")
# Page 2
sign_in_lcs["1input_number_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div.form_loginCode > div:nth-child(1) > span > input")
sign_in_lcs["2input_number_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div.form_loginCode > div:nth-child(2) > span > input")
sign_in_lcs["3input_number_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div.form_loginCode > div:nth-child(3) > span > input")
sign_in_lcs["4input_number_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div.form_loginCode > div:nth-child(4) > span > input")
sign_in_lcs["5input_number_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div.form_loginCode > div:nth-child(5) > span > input")
sign_in_lcs["verify_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > input")
sign_in_lcs["resent_msg_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > div.login_sms")

# asserts
sign_in_lcs["no_register_number_msg"] = (By.CSS_SELECTOR, '#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div.form_message')
sign_in_lcs["invalid_number_msg"] = (By.CSS_SELECTOR, '#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div:nth-child(1) > div:nth-child(1) > div')
sign_in_lcs["invalid_code_msg"] = (By.CSS_SELECTOR, '#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div.form_message')
sign_in_lcs["google_title"] = (By.CSS_SELECTOR, '#headingText > span')
sign_in_lcs[""] = (By.CSS_SELECTOR, '')