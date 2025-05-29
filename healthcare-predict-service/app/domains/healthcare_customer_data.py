import enum

from pydantic import BaseModel

class Gender(enum.Enum):
    MALE = "male"
    FEMALE = "female"

class Region(enum.Enum):
    SOUTHWEST = "southwest"
    SOUTHEAST = "southeast"
    NORTHEAST = "northeast"
    NORTHWEST = "northwest"

class CustomerData(BaseModel):
    age: int
    sex: Gender
    bmi: float
    children: int
    smoker: bool
    region: Region