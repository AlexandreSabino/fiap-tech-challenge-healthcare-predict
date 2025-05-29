import joblib
import pandas as pd
from pathlib import Path
import __main__

from sklearn.preprocessing import FunctionTransformer
from app.domains.healthcare_customer_data import CustomerData

MODEL_PATH = Path("model/fiap_tech_challenge_healthcare.joblib")

def _to_dataframe(customer_data: CustomerData):
    return pd.DataFrame([{
        "age": customer_data.age,
        "sex": customer_data.sex.value,
        "bmi": customer_data.bmi,
        "children": customer_data.children,
        "smoker": "yes" if customer_data.smoker else "no",
        "region": customer_data.region.value
    }])

def encode_smoker(X):
    X_np = X.to_numpy()
    return (X_np.ravel() == 'yes').astype(int).reshape(-1, 1)

__main__.encode_smoker = encode_smoker

class HealthcareValuePredict:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        print("Model loaded")

    def predict_value(self, customer_data: CustomerData):
        df = _to_dataframe(customer_data)
        return self.model.predict(df)[0]

healthcare_value_predict_instance = HealthcareValuePredict()