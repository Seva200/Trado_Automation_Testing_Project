from selenium.webdriver.common.by import By
# bank_transfer_lcs[""] = (By.CSS_SELECTOR, "")
bank_transfer_lcs = dict()

bank_transfer_lcs["x_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > span > i")
bank_transfer_lcs["bank_choose"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > section > div:nth-child(2) > select")
bank_transfer_lcs["bank_branch_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > section > div:nth-child(3) > input[type=text]")
bank_transfer_lcs["acc_num_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > section > div:nth-child(4) > input[type=text]")
bank_transfer_lcs["acc_name_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > section > div:nth-child(5) > input[type=text]")
bank_transfer_lcs["bn_num_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > section > div:nth-child(6) > input[type=number]")
bank_transfer_lcs["confirm_transfer"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > button")