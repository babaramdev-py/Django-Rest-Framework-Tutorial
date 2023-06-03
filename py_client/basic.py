import requests

endpoint1 = "http://127.0.0.1:8000/"


response = requests.get(endpoint1)


print(response.text)


# HTTP Request -> HTML
# REST API HTTP request -> JSON(xml)
