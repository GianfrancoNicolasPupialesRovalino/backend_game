from fastapi import APIRouter


from services.player_serv import get_players_serv, get_player_by_email_serv
from utils.error_handle import get_details_error
from utils.handle_response import send_success_response

player_router = APIRouter()

@player_router.get("/all")
def get_players_ctrl():
    try:
        players = get_players_serv()

        if not players:
            return send_success_response(404, "No players found")
        
        return send_success_response(200, "Players retrieved successfully", players)
    except Exception as error:
        return get_details_error(error)
    

@player_router.get("/{email}")
def get_player_by_email_ctrl(email: str):
    try:
        player = get_player_by_email_serv(email=email)

        if not player:
            return send_success_response(404, "Player not found")
        
        return send_success_response(200, "Player found", player)
    except Exception as error:
        return get_details_error(error)