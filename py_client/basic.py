import requests

endpoint1 = "http://127.0.0.1:8000/api"


response = requests.get(endpoint1)


print(response.json()['Message'])


# HTTP Request -> HTML
# REST API HTTP request -> JSON(xml)
