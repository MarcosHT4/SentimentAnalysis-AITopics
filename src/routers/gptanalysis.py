from fastapi import (
    APIRouter,
    Body,
    Depends
)
from src.schemas.analysis_output import AnalysisOutput
from src.schemas.score_output import ScoreOutput
from src.schemas.analysis_and_sentiment_output import AnalysisAndSentimentOutput
from src.services.text_analysis_service import TextAnalysisService
from src.services.csv_filler import CSVFillerService
from src.schemas.execution import Execution
from src.config import get_settings
import time
from functools import cache
text_analysis_service = TextAnalysisService()
csv_filler_service = CSVFillerService()

@cache
def get_text_analysis_service():
    return text_analysis_service
@cache
def get_csv_filler_service():
    return csv_filler_service
router = APIRouter()
SETTINGS = get_settings()

@router.post("/analysis_v2")
def analyze_text(text:str = Body(...), text_analysis = Depends(get_text_analysis_service), csv_filler = Depends(get_csv_filler_service)) -> AnalysisAndSentimentOutput:
    start_time = time.time()
    analysis_output = text_analysis.extract_analysis_by_gpt(text)
    embeddings = text_analysis.extract_embeddings_by_gpt(text)
    analysis_output.embeddings = embeddings
    score_output = text_analysis.extract_sentiment_by_gpt(text)
    execution = Execution(time_in_seconds=time.time()-start_time, original_text=text, text_char_length=len(text), version_number=SETTINGS.revision)
    csv_filler_service.add_csv_prediction_sentiment_analysis(score_output, execution, True,analysis_output)
    analysis_and_sentiment_output = AnalysisAndSentimentOutput(analysis_output=analysis_output, score_output=score_output, execution=execution)
    return analysis_and_sentiment_output