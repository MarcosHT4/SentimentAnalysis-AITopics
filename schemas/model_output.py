from pydantic import BaseModel
from schemas.score_output import ScoreOutput
from schemas.execution import Execution
class ModelOutput(BaseModel):
    execution:Execution
    score_output:ScoreOutput