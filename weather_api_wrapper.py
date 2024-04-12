import requests
import os

apikey = os.environ.get('k')
latitude = os.environ.get('lat')
longitude = os.environ.get('lon')

if not all([apikey, latitude, longitude]):
    print("Missing one of the required environment variables: k, lat, lon")
else:
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={apikey}"
    response = requests.get(url)
    weather_data = response.json()
    print(weather_data)
