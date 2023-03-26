from selenium.webdriver.common.by import By
# payments_mthds_lcs[""] = (By.CSS_SELECTOR, "")
payments_mthds_lcs = dict()

payments_mthds_lcs["credit_card"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(4) > div > div > div")
payments_mthds_lcs["b2b"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(4) > div > div > div")
payments_mthds_lcs["digital_check"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(6) > div > label:nth-child(3) > div")
payments_mthds_lcs["bank_transfer"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(6) > div > label:nth-child(2) > div")
payments_mthds_lcs["fin_trado"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(1) > div:nth-child(6) > div > label:nth-child(1) > div")
payments_mthds_lcs["purchase"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.steps_steps.checkout_steps > form > section:nth-child(2) > div:nth-child(3) > button")
payments_mthds_lcs["go_back"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > div.checkout_checkout_back_step")
payments_mthds_lcs["thank_you_back_home"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div.checkout_checkout > div > button")
