import requests
import allure


class TestAPI:
    @allure.description('test api')
    def test_api1(self):
        url = "https://widgetapi.purechat.com/api/visitorwidget/widgetversions/8d276de2-2c2b-4847-b8cc-936368f3844a"
        response = requests.get(url)
        assert response.status_code == 200

    @allure.description('test language api')
    def test_language_api(self):
        url = "https://qa.trado.co.il/api/language/getLanguages"
        response = requests.post(url)
        x = response.json()
        assert response.status_code == 200
        assert x['payload'][0]['key'] == "hebrew"
        assert x['payload'][1]['key'] == "english"

    @allure.description('test product sections api')
    def test_product_sections_api(self):
        url = "https://qa.trado.co.il/api/tags/filter"
        response = requests.post(url)
        x = response.json()
        assert response.status_code == 200
        assert x['payload'][0]['sections'][1]['name'] == 'חטיפים'
