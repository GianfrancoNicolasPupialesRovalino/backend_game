from src.database import Player

def get_auth_player_serv(email: str):
    try:
        player = Player.select().where(Player.email == email)
        return player.dicts().first()
    except Exception as error:
        raise error