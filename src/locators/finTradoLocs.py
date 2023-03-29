from selenium.webdriver.common.by import By
# fin_trado_lcs[""] = (By.CSS_SELECTOR, "")
fin_trado_lcs = dict()

fin_trado_lcs["x_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > span")
fin_trado_lcs["loan_period_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > div > div:nth-child(3) > select")
fin_trado_lcs["chargeable_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > div > div:nth-child(3) > select")
fin_trado_lcs["total_interest_fld"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > div > div:nth-child(4) > input[type=number]")
fin_trado_lcs["next_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > div > div:nth-child(4) > input[type=number]")
fin_trado_lcs["verification_btn"] = (By.CSS_SELECTOR, "#BDI")
fin_trado_lcs["notice_btn"] = (By.XPATH, '//*[@id="BDI"]')
fin_trado_lcs["finish_order_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > form > div > div:nth-child(3) > button")
fin_trado_lcs[""] = (By.CSS_SELECTOR, "")
