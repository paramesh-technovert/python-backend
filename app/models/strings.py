from pydantic import BaseModel

class StringInput(BaseModel):
    text: str

class ConcatInput(BaseModel):
    first: str
    second: str

class AnagramInput(BaseModel):
    first: str
    second: str
