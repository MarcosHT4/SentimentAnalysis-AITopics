from src.schemas.analysis_output import AnalysisOutput
from src.schemas.score_output import ScoreOutput
from src.schemas.execution import Execution
from pydantic import BaseModel

class AnalysisAndSentimentOutput(BaseModel):
    analysis_output:AnalysisOutput
    score_output:ScoreOutput
    execution:Execution
