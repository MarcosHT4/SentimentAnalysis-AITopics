from fastapi import (
    APIRouter,
    Body,
    Depends
)
from src.schemas.execution import Execution
from src.schemas.sentiment_model_output import SentimentModelOutput
from src.schemas.score_output import ScoreOutput
from src.config import get_settings
import time
from src.services.csv_filler import CSVFillerService
from src.services.sentiment_service import SentimentService
from src.services.score_conversion_service import ScoreConversionService
from functools import cache

router = APIRouter()
csv_filler_service = CSVFillerService()
sentiment_service = SentimentService()
score_conversion_service = ScoreConversionService()
SETTINGS = get_settings()


@cache
def get_csv_filler():
    return csv_filler_service
@cache
def get_sentiment_service():
    return sentiment_service
@cache
def get_score_conversion_service():
    return score_conversion_service


@router.post("/sentiment")
def analyze_sentiment(text:str = Body(...), csv_filler = Depends(get_csv_filler), sentiment = Depends(get_sentiment_service), score_conversion = Depends(get_score_conversion_service))-> SentimentModelOutput:
    start = time.time()
    star_rating_list = sentiment.predict(text)
        
    score = score_conversion.convert_star_rating_to_score(star_rating_list)
    label = score_conversion.map_score_to_sentiment(score)

    score_output = ScoreOutput(score=score, label=label)
    execution = Execution(time_in_seconds=time.time()-start, original_text=text, text_char_length=len(text), version_number=SETTINGS.revision)

    model_output = SentimentModelOutput(execution=execution, score_output=score_output)
    csv_filler.add_csv_prediction_sentiment_analysis(score_output, execution)
    return model_output


    