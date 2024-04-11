import requests
import argparse

parser = argparse.ArgumentParser(description='Get weather data for a specific location.')

parser.add_argument('-k', '--apikey', help='OpenWeather API Key', required=True)
parser.add_argument('-lat', '--latitude', help='Latitude of the location', required=True)
parser.add_argument('-lon', '--longitude', help='Longitude of the location', required=True)

args = parser.parse_args()

url = f"http://api.openweathermap.org/data/2.5/weather?lat={args.latitude}&lon={args.longitude}&appid={args.apikey}"

response = requests.get(url)
weather_data = response.json()
print(weather_data)
