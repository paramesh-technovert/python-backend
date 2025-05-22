from fastapi import APIRouter, HTTPException
from app.models.numbers import NumberInput, TwoNumberInput
from app.services.commonService import *

router = APIRouter()

@router.post("/add")
def add(data: NumberInput):
    return {"result": addition(data.numbers)}

@router.post("/subtract")
def subtract(data: TwoNumberInput):
    return {"result": subtraction(data.a, data.b)}

@router.post("/multiply")
def multiply(data: NumberInput):
    return {"result": multiplication(data.numbers)}

@router.post("/divide")
def divide(data: TwoNumberInput):
    try:
        result = division(data.a, data.b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
