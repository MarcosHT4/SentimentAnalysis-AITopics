from pydantic import BaseModel
from typing import Optional

class AnalysisOutput(BaseModel):
    part_of_speech_tagging: list[list[str]]
    named_entity_recognition: list[list[str]]
    embeddings: Optional[list[float]] = None