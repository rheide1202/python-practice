import json
import requests

#3f5cca07-f3e2-4a4b-aa4b-17ee033e716b
api_key = "3f5cca07f3e24a4baa4b17ee033e716b"
api_url = "https://eu.api.insight.rapid7.com/validate"


request_url = f"{api_url}?appid={api_key}"
response = requests.get(request_url)

print(response)

if response.status_code == 200:
    data = response.json()
    print(data)
