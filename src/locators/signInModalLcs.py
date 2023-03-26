from selenium.webdriver.common.by import By
# = (By.CSS_SELECTOR, "")
sign_in_lcs = dict()
# Page 1
sign_in_lcs["sign_in_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > div.login_loginregister > span.login_active")
sign_in_lcs["phone_number_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div:nth-child(1) > div:nth-child(1) > span > input[type=tel]")
sign_in_lcs["log_in_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > input")
sign_in_lcs["remember_me_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div > form > div:nth-child(1) > div.form_formItem.form_checkbox.undefined.false.undefined > span > span > span > i")