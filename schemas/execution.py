from pydantic import BaseModel
from schemas.detection import Detection

class Execution(BaseModel):
    time_in_seconds:float
    original_text:str
    text_char_length:int
    version_number:str