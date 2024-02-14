from flask import Flask, jsonify, request
from flask_cors import CORS
from forecastitService import ForecastitService

app = Flask(__name__)
CORS(app)
serviceLayer = ForecastitService()

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', default=None)

    if city:
        weatherData = serviceLayer.getWeatherData(city)
        response_data = weatherData
    else:
        return jsonify({"status": "error", "message": "Please provide city"}), 400

    return jsonify(response_data), 200

@app.route('/past/weather', methods=['GET'])
def get_past_weather():
    city = request.args.get('city', default=None)

    if city:
            pastWeatherData = serviceLayer.getPastWeatherData(city)
            response_data = pastWeatherData
    else:
        return jsonify({"status": "error", "message": "Please provide city"}), 400

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)