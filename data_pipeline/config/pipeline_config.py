OPENSKY_URL = "https://opensky-network.org/api/states/all"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

# India Bounding Box approx: 8.0 to 35.0 North, 68.0 to 97.0 East.
INDIA_BOUNDING_BOX = {
    "lamin": 8.0,
    "lomin": 68.0,
    "lamax": 35.0,
    "lomax": 97.0
}

# Major Indian Cities for weather data
INDIAN_CITIES = [
    {"name": "Delhi", "lat": "28.61", "lon": "77.20"},
    {"name": "Mumbai", "lat": "19.07", "lon": "72.87"},
    {"name": "Bengaluru", "lat": "12.97", "lon": "77.59"},
    {"name": "Chennai", "lat": "13.08", "lon": "80.27"},
    {"name": "Kolkata", "lat": "22.57", "lon": "88.36"},
    {"name": "Hyderabad", "lat": "17.38", "lon": "78.48"},
    {"name": "Guwahati", "lat": "26.14", "lon": "91.73"},
    {"name": "Ahmedabad", "lat": "23.02", "lon": "72.57"}
]
