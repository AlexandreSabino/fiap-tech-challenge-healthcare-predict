from fastapi import FastAPI

from app.routers.healthcare_predictor_routes import healthcare_predictor_router

app = FastAPI(title="Healthcare Prediction API")

app.include_router(healthcare_predictor_router, prefix="/api")
