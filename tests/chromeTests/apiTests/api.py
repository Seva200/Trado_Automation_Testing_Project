import requests

url = "https://widgetapi.purechat.com/api/visitorwidget/widgetversions/8d276de2-2c2b-4847-b8cc-936368f3844a"
response = requests.get(url)
if response.status_code != 200:
    print(response.json())
assert response.status_code == 200
