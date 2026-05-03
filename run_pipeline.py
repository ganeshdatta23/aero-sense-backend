import sys
import os
import time
from datetime import datetime

# Add the project root to sys.path to allow absolute imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_pipeline.tasks.fetch_flight_data import fetch_flights
from data_pipeline.tasks.fetch_weather_data import fetch_weather
from data_pipeline.tasks.load_data_to_db import load_data

def run_ingestion():
    print(f"[{datetime.now()}] Starting ingestion cycle...")
    
    try:
        # 1. Fetch and Load Flights
        print("Fetching flights from OpenSky...")
        flights = fetch_flights()
        load_data("raw_flights", flights)
        print(f"Successfully loaded flight data.")

        # 2. Fetch and Load Weather (JFK as a sample point)
        lat, lon = "40.6413", "-73.7781"
        print(f"Fetching weather for JFK ({lat}, {lon})...")
        weather = fetch_weather(lat, lon)
        load_data("raw_weather", weather, lat=lat, lon=lon)
        print(f"Successfully loaded weather data.")

        print(f"[{datetime.now()}] Cycle complete!")
    
    except Exception as e:
        print(f"Error during ingestion: {e}")

if __name__ == "__main__":
    # Check if 'loop' argument is passed
    if len(sys.argv) > 1 and sys.argv[1] == "--loop":
        interval = 600  # 10 minutes
        print(f"Starting continuous ingestion every {interval} seconds...")
        while True:
            run_ingestion()
            print(f"Waiting {interval} seconds for next cycle...")
            time.sleep(interval)
    else:
        run_ingestion()
        print("\nTip: Run 'python run_pipeline.py --loop' to run this continuously.")
