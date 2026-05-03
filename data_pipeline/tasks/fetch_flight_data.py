import requests
from data_pipeline.config.pipeline_config import OPENSKY_URL, INDIA_BOUNDING_BOX

def fetch_flights():
    """
    Fetch live flight state vectors for the India region from OpenSky Network.
    """
    response = requests.get(OPENSKY_URL, params=INDIA_BOUNDING_BOX)
    response.raise_for_status()
    data = response.json()
    return data
