from pydantic import BaseModel
from typing import List

class NumberInput(BaseModel):
    numbers: List[float]

class TwoNumberInput(BaseModel):
    a: float
    b: float
