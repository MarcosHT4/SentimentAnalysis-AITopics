from fastapi import (
    APIRouter,
    Body,
    Depends
)
from src.schemas.score_output import ScoreOutput
from src.schemas.analysis_output import AnalysisOutput
from src.schemas.analysis_and_sentiment_output import AnalysisAndSentimentOutput
from src.schemas.execution import Execution
from src.services.text_analysis_service import TextAnalysisService
from src.services.sentiment_service import SentimentService
from src.services.score_conversion_service import ScoreConversionService
from src.config import get_settings
import time
from functools import cache

text_analysis_service = TextAnalysisService()
sentiment_service = SentimentService()
score_conversion_service = ScoreConversionService()
SETTINGS = get_settings()

@cache
def get_text_analysis_service():
    return text_analysis_service

@cache
def get_sentiment_service():
    return sentiment_service

@cache
def get_score_conversion_service():
    return score_conversion_service


router = APIRouter()

@router.post("/analysis")
def analyze_text(text:str = Body(...), text_analysis = Depends(get_text_analysis_service), sentiment = Depends(get_sentiment_service), score_conversion = Depends(get_score_conversion_service)) -> AnalysisAndSentimentOutput:
    start_time = time.time()
    pos = text_analysis.extract_part_of_speech(text)
    ne = text_analysis.extract_named_entities(text)
    embeddings = text_analysis.extract_embeddings(text)
    analysis_output = AnalysisOutput(part_of_speech_tagging=pos, named_entity_recognition=ne, embeddings=embeddings)
    sentiment_star_rating = sentiment.predict(text)
    score = score_conversion.convert_star_rating_to_score(sentiment_star_rating)
    label = score_conversion.map_score_to_sentiment(score)

    score_output = ScoreOutput(score=score, label=label)
    execution = Execution(time_in_seconds=time.time()-start_time, original_text=text, text_char_length=len(text), version_number=SETTINGS.revision)

    analysis_and_sentiment_output = AnalysisAndSentimentOutput(analysis_output=analysis_output, score_output=score_output, execution=execution)

    return analysis_and_sentiment_output
