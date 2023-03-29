from selenium.webdriver.common.by import By
# cart_bar_lcs[""] = (By.CSS_SELECTOR, "")
cart_bar_lcs = dict()

cart_bar_lcs["cart_status"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]')
cart_bar_lcs["cart_clear"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]')
cart_bar_lcs["items_amount_fld"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.fullProduct_fullProduct > div > div.fullProduct_more_info > div.cart_cart.cart_cart_checkout.undefined.cart_open > div.cart_list.cart_list_fullProduct > div > a > div > div.inlineProduct_info > div.productBtn_productBtn > div > div > div > input[type=number]")
cart_bar_lcs["bucket_btn"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/a/div/div[3]/div[2]')
cart_bar_lcs["plus_btn"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/a/div/div[2]/div[3]/div/div/span[1]/i')
cart_bar_lcs["minus_btn"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/a/div/div[2]/div[3]/div/div/span[2]/i')
cart_bar_lcs["check_out_btn"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[3]/button')

# asserts
cart_bar_lcs["cart_is_empty"] = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div')
cart_bar_lcs["item_name"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.fullProduct_fullProduct > div > div.fullProduct_more_info > div.cart_cart.cart_cart_checkout.undefined.cart_open > div.cart_list.cart_list_fullProduct > div > a > div > div.inlineProduct_info > div.inlineProduct_name")
