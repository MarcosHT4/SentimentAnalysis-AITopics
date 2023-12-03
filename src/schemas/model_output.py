from pydantic import BaseModel
from src.schemas.score_output import ScoreOutput
from src.schemas.execution import Execution
class ModelOutput(BaseModel):
    execution:Execution
    score_output:ScoreOutput