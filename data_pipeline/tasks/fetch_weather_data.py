import requests
from data_pipeline.config.pipeline_config import OPEN_METEO_URL

def fetch_weather(lat, lon):
    """
    Fetch real-time weather data for a given set of coordinates.
    """
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true",
        "windspeed_unit": "kmh"
    }
    response = requests.get(OPEN_METEO_URL, params=params)
    response.raise_for_status()
    return response.json()
