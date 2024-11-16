# Application Programming Interface (give data or send request to it and modify some info)

import requests     # requests for data from an end point (url) that will give us some data
import json

API_KEY = ""    #then use documentation

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"    #contains query parameter (anything after ?), so looking for data assossiated with the city that the user types in

response = requests.get(request_url)    # will retrieve information

if response.status_code == 200:     # successful
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")