from transformers import pipeline
class SentimentService:
    def __init__(self) -> None:
        self.pipe = pipeline("text-classification", model="karina-aquino/spanish-sentiment-model", top_k=None)
    def predict(self, text:str) -> list:
        result = self.pipe(text)
        return result
