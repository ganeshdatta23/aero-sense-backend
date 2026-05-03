from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.app.database.db import get_db
from backend.app.services import analytics_service
from backend.app.schemas.data_schemas import Flight, DisruptionMetric

router = APIRouter()

@router.get("/current", response_model=List[Flight])
def read_current_flights(db: Session = Depends(get_db)):
    return analytics_service.get_latest_flights(db)

@router.get("/disruptions", response_model=List[DisruptionMetric])
def read_disruption_metrics(db: Session = Depends(get_db)):
    return analytics_service.calculate_disruption_metrics(db)
