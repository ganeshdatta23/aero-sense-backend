from backend.app.database.db import SessionLocal
from backend.app.models.data_models import FlightRaw, WeatherRaw

def load_data(table_name, payload, **kwargs):
    """
    Loads raw JSON data into the specified PostgreSQL table using SQLAlchemy ORM.
    """
    db = SessionLocal()
    try:
        if table_name == "raw_flights":
            new_record = FlightRaw(
                source=kwargs.get("source", "opensky"),
                payload=payload
            )
            db.add(new_record)
        elif table_name == "raw_weather":
            new_record = WeatherRaw(
                latitude=str(kwargs.get("lat")),
                longitude=str(kwargs.get("lon")),
                payload=payload
            )
            db.add(new_record)
        
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error loading data into {table_name}: {e}")
        raise e
    finally:
        db.close()
