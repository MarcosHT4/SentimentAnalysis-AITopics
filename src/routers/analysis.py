from fastapi import (
    APIRouter,
    Body,
    Depends
)
from src.schemas.analysis_output import AnalysisOutput
from src.services.text_analysis_service import TextAnalysisService
import time
from functools import cache
text_analysis_service = TextAnalysisService()

@cache
def get_text_analysis_service():
    return text_analysis_service

router = APIRouter()

@router.post("/analysis")
def analyze_text(text:str = Body(...), text_analysis = Depends(get_text_analysis_service)) -> AnalysisOutput:
    start_time = time.time()
    pos = text_analysis.extract_part_of_speech(text)
    ne = text_analysis.extract_named_entities(text)
    embeddings = text_analysis.extract_embeddings(text)
    analysis_output = AnalysisOutput(part_of_speech_tagging=pos, named_entity_recognition=ne, embeddings=embeddings)
    return analysis_output
