"""Write a python program to fetch current weather data from the JSON file"""

import json

with open('weather_data.json') as f:
    data = json.load(f)

current_temp = data['main']['temp']
humidity = data['main']['humidity']
weather_desc = data['main']['description']

print(f"Current temperature: {current_temp}°C")
print(f"Humidity: {humidity}%")
print(f"Weather description: {weather_desc}")
