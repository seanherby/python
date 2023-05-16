# Connects to a weather service and shows you the forecast for your requested area
import requests
import time

# Set up a request to fetch the weather
api_key = "your_code"
city = input("Choose your city!\n")
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=imperial"
request = requests.get(url)
json = request.json()

# Pretend to work
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')

# Display the weather
description = json.get("weather")[0].get("description")
print("Today's Weather Forecast is", description)
temp_min = json.get("main").get("temp_min")
temp_max = json.get("main").get("temp_max")
print("The range is", temp_min,"to", temp_max)
