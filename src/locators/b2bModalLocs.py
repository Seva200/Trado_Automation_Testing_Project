from selenium.webdriver.common.by import By
# b2b_lcs[""] = (By.CSS_SELECTOR, "")
b2b_lcs = dict()

b2b_lcs["x_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > span")
b2b_lcs["bn_num_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > section > div:nth-child(1) > input[type=number]")
b2b_lcs["b2b_customer_id_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > section > div:nth-child(2) > input[type=number]")
b2b_lcs["confirm_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > button")