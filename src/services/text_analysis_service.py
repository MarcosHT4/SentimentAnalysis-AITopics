import spacy
from src.config import get_settings, get_secret_settings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser


SETTINGS = get_settings()
SECRET_SETTINGS = get_secret_settings()

class TextAnalysisService:
    def __init__(self) -> None:
        self.nlp = spacy.load(SETTINGS.models_versions[0])
        self.llm = ChatOpenAI(model=SETTINGS.models_versions[2], openai_api_key=SECRET_SETTINGS.openai_key)

    def extract_part_of_speech(self, text:str) -> list:
        doc = self.nlp(text)
        pos = [(token.text, token.pos_) for token in doc]
        return pos
    def extract_named_entities(self, text:str) -> list:
        doc = self.nlp(text)
        ne = [(entity.text, entity.label_) for entity in doc.ents]
        return ne
    def extract_embeddings(self, text:str) -> list:
        doc = self.nlp(text)
        embeddings = doc.vector.tolist()
        return embeddings
    def generate_text(self, prompt:str) -> str:
        return self.llm.predict(prompt)
    
