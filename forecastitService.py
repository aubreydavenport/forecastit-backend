import requests
from datetime import datetime, timedelta

class ForecastitService:
    def __init__(self):
        pass

    def getWeatherData(self, cityName):
        params = {
            "lat": 0.0,
            "lon": 0.0,
            "appid": "c4a286328b3d2bbf20a28a17ddab0bd6",
            "units": "imperial",
            "exclude": "minutely,hourly,daily,alerts"
            }

        #Set lat/lon from city
        if cityName == "Boston":
            params["lat"] = 42.36
            params["lon"] = -71.06

        if cityName == "Chicago":
            params["lat"] = 41.88
            params["lon"] = -87.63

        if cityName == "Dallas":
            params["lat"] = 32.78
            params["lon"] = -96.80

        if cityName == "New York":
            params["lat"] = 40.71
            params["lon"] = -74.01

        if cityName == "London":
            params["lat"] = 51.51
            params["lon"] = -0.13

        url = "https://api.openweathermap.org/data/3.0/onecall?"
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()

    def getPastWeatherData(self, cityName):
        time = datetime.utcnow()
        unix = time.timestamp()
        params = {
            "lat": 0.0,
            "lon": 0.0,
            "units": "imperial",
            "appid": "c4a286328b3d2bbf20a28a17ddab0bd6",
            "dt": unix
            }

        #Set lat/lon from city
        if cityName == "Boston":
            params["lat"] = 42.36
            params["lon"] = -71.06

        if cityName == "Chicago":
            params["lat"] = 41.88
            params["lon"] = -87.63

        if cityName == "Dallas":
            params["lat"] = 32.78
            params["lon"] = -96.80

        if cityName == "New York":
            params["lat"] = 40.71
            params["lon"] = -74.01

        if cityName == "London":
            params["lat"] = 51.51
            params["lon"] = -0.13

        url = "https://api.openweathermap.org/data/3.0/onecall/timemachine?"
        weatherHistory = []

        for i in range(1, 8):
            time = time - timedelta(hours=24)
            unix = int(time.timestamp())
            params["dt"] = unix
            response = requests.get(url, params=params)
            if response.status_code == 200:
                jsonData = response.json()
                data = jsonData["data"][0]
                weather = data["weather"][0]
                weatherHistory.append({
                    "daysAgo": i,
                    "temp": data["temp"],
                    "main": weather["main"],
                    "desc": weather["description"]
                })

        print(weatherHistory)


        return weatherHistory

if __name__ == "__main__":
    service = ForecastitService()