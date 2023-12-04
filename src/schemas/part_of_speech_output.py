from pydantic import BaseModel

class PartOfSpeechOutput(BaseModel):
    word: str
    part_of_speech_tag: str