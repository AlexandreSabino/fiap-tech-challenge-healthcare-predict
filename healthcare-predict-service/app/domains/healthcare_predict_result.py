from pydantic import BaseModel


class HealthcareValue(BaseModel):
    value: float

    def model_dump(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        data["value"] = float(f"{data['value']:.2f}")
        return data
