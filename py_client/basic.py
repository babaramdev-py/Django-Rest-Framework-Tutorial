import requests

endpoint1 = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"


response = requests.get(endpoint, json={"query":"Hello world!"})


print(response.json())


# HTTP Request -> HTML
# REST API HTTP request -> JSON(xml)
