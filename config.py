from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cache

class Settings(BaseSettings):
    api_name:str = "Sentiment Analysis Service"
    revision:str = "0.0.1"
    models_names:list[str] = [
        "Spanish Core News Small - Spacy",
        "Spanish Sentiment Model - Karina Aquino",
        "GPT-4 - LangChain"
    ]
    csv_path:str = "outputs/predictions.csv"

@cache
def get_settings():
    return Settings()
