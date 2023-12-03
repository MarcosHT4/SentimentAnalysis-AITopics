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

@router.post("/gpt-analysis")
def analyze_text(text:str = Body(...), text_analysis = Depends(get_text_analysis_service)) -> str:
    start_time = time.time()
    output = text_analysis.generate_text(text)
    return output