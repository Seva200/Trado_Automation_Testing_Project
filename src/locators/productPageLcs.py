from selenium.webdriver.common.by import By
# = (By.CSS_SELECTOR, "")
product_lcs = dict()

product_lcs["product_btn"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list > a:nth-child(1) > div > div.product_top > div.productDesc_productDesc.undefined > div.productDesc_name")
product_lcs["plus_btn"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.fullProduct_fullProduct > div > div:nth-child(1) > div.fullProduct_side1 > div > div.fullProduct_top > div.fullProduct_productsHedaer > div.productBtn_productBtn.fullProduct_btn > div > div > span:nth-child(1) > i")
product_lcs["minus_btn"] = (By.CSS_SELECTOR, "#root > div > div.pages_pages > div.pages_children.false > div > div > div.fullProduct_fullProduct > div > div:nth-child(1) > div.fullProduct_side1 > div > div.fullProduct_top > div.fullProduct_productsHedaer > div.productBtn_productBtn.fullProduct_btn > div > div > span:nth-child(3) > i")