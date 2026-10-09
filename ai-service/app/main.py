from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.analysis import router as analysis_router

app = FastAPI(title="FinSight AI Service", version="0.1.0")
app.include_router(health_router, prefix="/api/v1")
app.include_router(analysis_router, prefix="/api/v1")
