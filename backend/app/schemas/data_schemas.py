from pydantic import BaseModel
from datetime import datetime
from typing import Any, List, Optional

class FlightBase(BaseModel):
    source: Optional[str] = "opensky"
    payload: Any

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class WeatherBase(BaseModel):
    latitude: str
    longitude: str
    payload: Any

class WeatherCreate(WeatherBase):
    pass

class Weather(WeatherBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class DisruptionMetric(BaseModel):
    hour: datetime
    flight_count: int
    disrupted_count: int
    avg_wind_speed: float
