import requests
from data_pipeline.config.pipeline_config import OPENSKY_URL

def fetch_flights():
    """
    Fetch live flight state vectors from OpenSky Network.
    """
    response = requests.get(OPENSKY_URL)
    response.raise_for_status()
    data = response.json()
    # The 'states' key contains a list of state vectors
    return data
