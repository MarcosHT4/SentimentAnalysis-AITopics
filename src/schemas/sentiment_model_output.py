from pydantic import BaseModel
from src.schemas.score_output import ScoreOutput
from src.schemas.execution import Execution
class SentimentModelOutput(BaseModel):
    execution:Execution
    score_output:ScoreOutput