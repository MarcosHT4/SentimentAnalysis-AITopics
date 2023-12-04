from pydantic import BaseModel
from typing import Optional
from src.schemas.part_of_speech_output import PartOfSpeechOutput
from src.schemas.named_entity_output import NamedEntityOutput

class AnalysisOutput(BaseModel):
    part_of_speech_tagging: list[PartOfSpeechOutput]
    named_entity_recognition: list[NamedEntityOutput]
    embeddings: Optional[list[float]] = None