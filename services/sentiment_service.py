from transformers import pipeline
from schemas.star_rating import StarRating
from schemas.star_rating import StarRatingList
class SentimentService:
    def __init__(self) -> None:
        self.pipe = pipeline("text-classification", model="karina-aquino/spanish-sentiment-model", top_k=None)
    def predict(self, text:str) -> StarRatingList:
        result = self.pipe(text)[0]
        temp_star_rating_list = []
        for item in result:
            label = item['label']
            score = item['score']
            star_rating = StarRating(label=label, score=score)
            temp_star_rating_list.append(star_rating)
        star_rating_list = StarRatingList(star_ratings=temp_star_rating_list) 
        return star_rating_list




        return result
