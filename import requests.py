import requests
import json

API_KEY = "31b982a2c2810668a92fb498be57fc56"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    
    name= data["name"]
    weather= data['weather'][0]['description']
    temperature= round(data["main"]["temp"] - 273.15, 2)
    min_degrees= round(data['main']['temp_min'] - 273.15, 2)
    max_degrees= round(data['main']['temp_max'] - 273.15, 2)

    totaal = ("city", name), ("weather", weather), ("temperature", temperature), ("min_degrees", min_degrees), ("max_degrees", max_degrees)
    with open("graden.json", "w") as f:
        json.dump(totaal, f, indent=2)
    
    '''print("city:", name)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
    print("min_degrees:", min_degrees, "celsius")
    print("max_degrees:", max_degrees, "celcius")'''

else:
    print("An error occurred.")   

