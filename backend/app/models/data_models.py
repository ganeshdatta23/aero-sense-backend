from sqlalchemy import Column, Integer, DateTime, String, JSON
from sqlalchemy.sql import func
from backend.app.database.db import Base

class FlightRaw(Base):
    __tablename__ = "raw_flights"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    source = Column(String, default="opensky")
    payload = Column(JSON)  # Stores the full JSON response from OpenSky

class WeatherRaw(Base):
    __tablename__ = "raw_weather"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    latitude = Column(String)
    longitude = Column(String)
    payload = Column(JSON)  # Stores the full JSON response from Open-Meteo
