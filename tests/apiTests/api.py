import requests
import allure

# @allure.description("test api")
# def test_api1():
#     url = "https://widgetapi.purechat.com/api/visitorwidget/widgetversions/8d276de2-2c2b-4847-b8cc-936368f3844a"
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(response.json())
#     assert response.status_code == 200


# url = "https://qa.trado.co.il/api/product/filter"
# headers = {
#     "Content-Type": "application/json; charset=utf-8",
#     "Accept": "application/json, text/plain, */*",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Connection": "keep-alive"
#     }
#
# response = requests.post(url, headers=headers)
# print(response.json())