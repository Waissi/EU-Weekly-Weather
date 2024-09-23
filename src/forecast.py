import requests
import json
from geolocation import *
from PySide6.QtCore import *

url = "https://api.open-meteo.com/v1/forecast"


class DailyForecast():
    """
        date: QDateTime
        average_temp: float
    """

    def __init__(self, date: str, temp_min: float, temp_max: float):
        self.date = QDateTime()
        self.date.setDate(
            QDate(int(date[:4]), int(date[5:7]), int(date[8:10])))
        self.average_temp = (temp_min + temp_max) / 2


def get_city_forecast(city: str) -> list[DailyForecast]:
    city_forecast: list[DailyForecast] = []
    city_location = get_city_geolocation(city)
    if not city_location:
        return
    params = {
        "latitude": city_location.latitude,
        "longitude": city_location.longitude,
        "daily": "temperature_2m_max,temperature_2m_min"
    }
    result = requests.get(url, params=params)
    if not result.status_code == 200:
        return
    jsondata: dict = json.loads(result.text)
    data: dict = jsondata["daily"]
    for i in range(len(data["time"])):
        date: str = data["time"][i]
        temp_min: float = data["temperature_2m_min"][i]
        temp_max: float = data["temperature_2m_max"][i]
        city_forecast.append(DailyForecast(date, temp_min, temp_max))
    return city_forecast
