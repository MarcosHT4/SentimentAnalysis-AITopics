from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cache

class Settings(BaseSettings):
    api_name:str = "Sentiment Analysis Service"
    revision:str = "0.0.1"
    models_names:list[str] = [
        "Spanish Core News Medium - Spacy",
        "Spanish Sentiment Model - Karina Aquino",
        "GPT-4 - LangChain",
        "Text Embedding ADA-002 - LangChain"	
    ]
    csv_path:str = "src/outputs/predictions.csv"
    models_versions:list[str] = [
        "src/models/es_core_news_md-3.7.0",
        "./src/models/spanish-sentiment-model",
        "gpt-4",
        "text-embedding-ada-002"
    ]

class SecretSettings(BaseSettings):
    openai_key:str
    model_config = SettingsConfigDict(env_file=".env")
    

@cache
def get_secret_settings():
    return SecretSettings()

@cache
def get_settings():
    return Settings()
