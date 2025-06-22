from pydantic import BaseModel
from datetime import datetime

class VocabularyMatchModel(BaseModel):
    idMatch: int
    player: str
    num_words: int
    difficulty: str
    score: int
    time: int
    date: datetime
