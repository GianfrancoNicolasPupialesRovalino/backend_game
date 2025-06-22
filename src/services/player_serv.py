from src.database import Player
from src.models.player_model import PlayerModel
from src.utils.bcrypt_handle import encrypt



def get_players_serv():
    try:
        player = Player.select(
            Player.email,
            Player.name,
            Player.last_name,
        )
        return list(player.dicts())
    except Exception as error:
        raise error

def get_player_by_email_serv(email: str):
    try:
        player = Player.select(
            Player.email,
            Player.name,
            Player.last_name,
        ).where(Player.email == email)

        return player.dicts().first()
    except Exception as error:
        raise error
    

def create_player_serv(data: PlayerModel):
    try:
        print(data)
        password_hashed = encrypt(data.password)

        user = Player.create(
            email=data.email,
            name=data.name,
            last_name=data.last_name,
            password=password_hashed
        )

        return user
    except Exception as error:
        raise error