from pydantic import BaseModel

class input(BaseModel):
    input: str

class predictions(BaseModel):
    text: str
    category: str