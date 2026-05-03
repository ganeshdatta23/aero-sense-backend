from sqlalchemy.orm import Session
from backend.app.models.data_models import FlightRaw, WeatherRaw
from backend.app.schemas.data_schemas import DisruptionMetric
from datetime import datetime, timedelta

def get_latest_flights(db: Session, limit: int = 100):
    return db.query(FlightRaw).order_by(FlightRaw.timestamp.desc()).limit(limit).all()

def get_latest_weather(db: Session, limit: int = 10):
    return db.query(WeatherRaw).order_by(WeatherRaw.timestamp.desc()).limit(limit).all()

def calculate_disruption_metrics(db: Session):
    # This is a simplified placeholder for the dbt logic
    # In a real scenario, this would query the 'marts' tables created by dbt
    return [
        DisruptionMetric(
            hour=datetime.now() - timedelta(hours=i),
            flight_count=150 + i * 10,
            disrupted_count=10 + i * 2,
            avg_wind_speed=25.5 - i
        ) for i in range(5)
    ]
