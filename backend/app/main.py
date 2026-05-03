from fastapi import FastAPI
from backend.app.api.api_router import api_router
from backend.app.core.config import settings
from backend.app.database.db import engine, Base

# Create tables if they don't exist (Simple approach for prototype)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to AeroSense API", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
