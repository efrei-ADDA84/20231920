from flask import Flask, request, jsonify
import requests
import os
import argparse

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    api_key = request.args.get('apikey')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    print(api_key, lat, lon)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
