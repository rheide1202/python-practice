#api module
import requests

#informatie api
API_KEY = "31b982a2c2810668a92fb498be57fc56"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#stad uit de database kiezen, met een f string de url bepalen waar de request vandaan moet komen
city = "amsterdam"
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

#response code 200 is goed dit betekent geslaagd, daarna import hij de data van de stad in json formaat
if response.status_code == 200:
    data = response.json()
    #uit het json bestand definieer ik wat ik beschreven wil zien
    weather= data['weather'][0]['description']
    temperature= round(data["main"]["temp"] - 273.15, 2)
    min_degrees= round(data['main']['temp_min'] - 273.15, 2)
    max_degrees= round(data['main']['temp_max'] - 273.15, 2) 

    #print de gedifineerde data
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
    print("min_degrees:", min_degrees, "celsius")
    print("max_degrees:", max_degrees, "celcius")
#als de code niet 200 is krijg je deze melding, kan fout met api key of url zijn
else:
    print("An error occurred.")