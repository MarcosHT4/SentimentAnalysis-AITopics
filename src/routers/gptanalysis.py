from fastapi import (
    APIRouter,
    Body,
    Depends
)
from src.schemas.analysis_output import AnalysisOutput
from src.schemas.score_output import ScoreOutput
from src.schemas.analysis_and_sentiment_output import AnalysisAndSentimentOutput
from src.services.text_analysis_service import TextAnalysisService
from src.schemas.execution import Execution
from src.config import get_settings
import time
from functools import cache
text_analysis_service = TextAnalysisService()

@cache
def get_text_analysis_service():
    return text_analysis_service

router = APIRouter()
SETTINGS = get_settings()

@router.post("/gpt-analysis")
def analyze_text(text:str = Body(...), text_analysis = Depends(get_text_analysis_service)) -> AnalysisAndSentimentOutput:
    start_time = time.time()
    analysis_output = text_analysis.extract_analysis_by_gpt(text)
    score_output = text_analysis.extract_sentiment_by_gpt(text)
    execution = Execution(time_in_seconds=time.time()-start_time, original_text=text, text_char_length=len(text), version_number=SETTINGS.revision)
    analysis_and_sentiment_output = AnalysisAndSentimentOutput(analysis_output=analysis_output, score_output=score_output, execution=execution)
    return analysis_and_sentiment_output