from fastapi import APIRouter

from app.domains.healthcare_customer_data import CustomerData
from app.domains.healthcare_predict_result import HealthcareValue
from app.services.healthcare_predictor import healthcare_value_predict_instance

healthcare_predictor_router = APIRouter()

@healthcare_predictor_router.post("/healthcare-value-predict")
async def healthcare_value_predict(customer_data: CustomerData):
    predict = healthcare_value_predict_instance.predict_value(customer_data)
    return HealthcareValue(value = predict)
