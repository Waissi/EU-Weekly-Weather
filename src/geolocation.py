import requests
import json

url = "https://geocoding-api.open-meteo.com/v1/search"


class CityLocation():
    """
        latitude: float
        longitude: float
    """

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


def get_city_geolocation(city) -> CityLocation:
    params = {
        "name": city,
        "count": "1",
        "language": "en",
        "format": "json"
    }
    result = requests.get(url, params=params)
    if not result.status_code == 200:
        return
    data = json.loads(result.text)
    return CityLocation(data["results"][0]["latitude"], data["results"][0]["longitude"])
