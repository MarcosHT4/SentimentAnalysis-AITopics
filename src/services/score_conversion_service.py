from src.schemas.star_rating import StarRatingList
class ScoreConversionService:
    def convert_star_rating_to_score(self, star_rating: StarRatingList) -> float:
        star_mapping = {
        '1 star': -1,
        '2 stars': -0.5,
        '3 stars': 0,
        '4 stars': 0.5,
        '5 stars': 1
        }

        weighted_sum = 0.0

        for item in star_rating.star_ratings:
            label = item.label
            score = item.score
            sentiment_value = star_mapping[label]
            weighted_sum += score * sentiment_value
        return weighted_sum    
    
    def map_score_to_sentiment(self, score: float) -> str:
        category_ranges = {
        'Muy Negativo': (-1, -0.75),
        'Negativo': (-0.75, -0.5),
        'Poco Negativo': (-0.5, -0.25),
        'Neutral': (-0.25, 0.25),
        'Poco Positivo': (0.25, 0.5),
        'Positivo': (0.5, 0.75),
        'Muy Positivo': (0.75, 1)
        }
        for category, (lower, upper) in category_ranges.items():
            if lower <= score < upper:
                return category