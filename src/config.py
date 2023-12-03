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
    csv_path:str = "src/outputs/predictions.csv"
    models_versions:list[str] = [
        "src/models/es_core_news_md-3.7.0",
        "",
        "gpt-4"
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
