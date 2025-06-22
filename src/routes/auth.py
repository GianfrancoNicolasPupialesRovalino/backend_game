from datetime import timedelta

from fastapi import APIRouter

from src.models.auth_model import AuthModel
from src.models.player_model import PlayerModel
from src.services.auth_serv import get_auth_player_serv
from src.services.player_serv import create_player_serv
from src.utils.jwt_handle import generate_token
from src.utils.error_handle import get_details_error
from src.utils.handle_response import send_success_response
from src.utils.bcrypt_handle import verified


auth_router = APIRouter()


@auth_router.post("/login")
def login_player_ctrl(data: AuthModel):
    try: 
        
        player = get_auth_player_serv(data.email)
        if not player:
            return send_success_response(404, "Player not found")
        if not verified(data.password, player["password"]):
            return send_success_response(401, "Invalid credentials")

        token = generate_token(player, expires_in=timedelta(minutes=960))


        return send_success_response(
            200,
            "Login user",
            {
                "token": token,
                "player": {
                    "email": player.get("email"),
                    "name": player.get("name"),
                    "lastname": player.get("lastname"),
                },
            },
        )
    except Exception as error:    
        return get_details_error(error)
    

@auth_router.post("/register")
def create_player_ctrl(data: PlayerModel):
    try:
        player = create_player_serv(data)
        print(f"Usuario creado: {player.email}")
        return send_success_response(201, "Player created successfully")
    except Exception as error:
        return get_details_error(error)
    

@auth_router.get("/logout")
def logout_player_ctrl():
        return send_success_response(200, "Logout successful")