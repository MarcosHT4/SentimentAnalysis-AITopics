from pydantic import BaseModel

class NamedEntityOutput(BaseModel):
    entity: str
    named_entity_tag: str
