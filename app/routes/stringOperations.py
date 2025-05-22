from fastapi import APIRouter
from app.models.strings import StringInput, ConcatInput, AnagramInput
from app.services.commonService import reverse_string, concat_strings, is_anagram

router = APIRouter()

@router.post("/reverse")
def reverse(data: StringInput):
    return {"result": reverse_string(data.text)}

@router.post("/concat")
def concat(data: ConcatInput):
    return {"result": concat_strings(data.first, data.second)}

@router.post("/isanagram")
def anagram(data: AnagramInput):
    return {"result": is_anagram(data.first, data.second)}
