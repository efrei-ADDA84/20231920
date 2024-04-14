from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_weather():
    api_key = os.environ.get('API_KEY')  # Get the API key from an environment variable
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if not api_key:
        return jsonify({"error": "API key is missing"}), 401  # Return an error if the API key isn't provided
    
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=8081)
