from selenium.webdriver.common.by import By

welcome_to_lcs = dict()

welcome_to_lcs["x_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > span > i")
welcome_to_lcs["cocktail"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div.store_interests > div:nth-child(1)")
welcome_to_lcs["restaurants"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > div.store_interests > div:nth-child(2)")
welcome_to_lcs["save_btn"] = (By.CSS_SELECTOR, "#root > div > div.modal_modalWrapper.false.modal_open > div > div > div > button")
