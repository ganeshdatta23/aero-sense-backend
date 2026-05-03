from fastapi import APIRouter
from backend.app.api.routes import flights, health

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(flights.router, prefix="/flights", tags=["flights"])
