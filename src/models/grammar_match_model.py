from pydantic import BaseModel
from datetime import datetime

class GrammarMatchModel(BaseModel):
    idMatch: int
    player: str
    session_name: str
    difficulty: str
    time: int
    score: int
    completion: int
    date: datetime
