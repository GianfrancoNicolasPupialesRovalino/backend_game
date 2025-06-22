from pydantic import BaseModel

class PlayerModel(BaseModel):
    email: str
    name: str
    last_name: str
    password: str
