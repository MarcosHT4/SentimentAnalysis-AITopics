from pydantic import BaseModel

class StarRating(BaseModel):
    label:str
    score:float
    
class StarRatingList(BaseModel):
    star_ratings: list[StarRating]

