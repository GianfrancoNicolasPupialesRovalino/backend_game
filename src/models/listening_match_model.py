from pydantic import BaseModel
from datetime import datetime

class ListeningMatchModel(BaseModel):
    idMatch: int
    player: str
    score: int
    accuracy: int
    name_video: str
    difficulty: str
    time: int
    date: datetime

