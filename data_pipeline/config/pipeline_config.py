OPENSKY_URL = "https://opensky-network.org/api/states/all"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

# India Bounding Box approx: 8.0 to 35.0 North, 68.0 to 97.0 East.
# INDIA_BOUNDING_BOX = {
#     "lamin": 8.0,
#     "lomin": 68.0,
#     "lamax": 35.0,
#     "lomax": 97.0
# }

# # Major Indian Cities for weather data
# INDIAN_CITIES = [
#     {"name": "Delhi", "lat": "28.61", "lon": "77.20"},
#     {"name": "Mumbai", "lat": "19.07", "lon": "72.87"},
#     {"name": "Bengaluru", "lat": "12.97", "lon": "77.59"},
#     {"name": "Chennai", "lat": "13.08", "lon": "80.27"},
#     {"name": "Kolkata", "lat": "22.57", "lon": "88.36"},
#     {"name": "Hyderabad", "lat": "17.38", "lon": "78.48"},
#     {"name": "Guwahati", "lat": "26.14", "lon": "91.73"},
#     {"name": "Ahmedabad", "lat": "23.02", "lon": "72.57"}
# ]

# Global Bounding Box (covers the entire world)
# Note: For global OpenSky data, you can simply omit the bounding box parameters in your API call.
INDIA_BOUNDING_BOX = {
    "lamin": -90.0,
    "lomin": -180.0,
    "lamax": 90.0,
    "lomax": 180.0
}

# Major Global Capitals for weather data
INDIAN_CITIES = [
    {"name": "Tokyo", "country": "Japan", "lat": "35.68", "lon": "139.69"},
    {"name": "London", "country": "UK", "lat": "51.51", "lon": "-0.13"},
    {"name": "Washington D.C.", "country": "USA", "lat": "38.90", "lon": "-77.04"},
    {"name": "Paris", "country": "France", "lat": "48.85", "lon": "2.35"},
    {"name": "Berlin", "country": "Germany", "lat": "52.52", "lon": "13.40"},
    {"name": "Beijing", "country": "China", "lat": "39.90", "lon": "116.40"},
    {"name": "Canberra", "country": "Australia", "lat": "-35.28", "lon": "149.13"},
    {"name": "Ottawa", "country": "Canada", "lat": "45.42", "lon": "-75.70"},
    {"name": "Brasilia", "country": "Brazil", "lat": "-15.83", "lon": "-47.86"},
    {"name": "New Delhi", "country": "India", "lat": "28.61", "lon": "77.20"}
]
