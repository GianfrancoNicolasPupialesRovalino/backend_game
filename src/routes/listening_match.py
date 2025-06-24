from fastapi import APIRouter

from src.services.listening_match_serv import create_listening_match, get_listening_matchs, get_listening_match_player_serv, get_top_scores_overall_serv, get_top_scores_by_difficulty_serv
from src.services.player_serv import get_player_by_email_serv
from src.utils.handle_response import send_success_response
from src.utils.error_handle import get_details_error
from src.models.listening_match_model import ListeningMatchModel

listening_match_router = APIRouter()

@listening_match_router.post("/register")
def post_listening_match_ctrl(data: ListeningMatchModel):
    try:
        print(f"Datos recibidos en el backend: {data.dict()}")
        player = get_player_by_email_serv(email=data.player)
        if not player:
            return send_success_response(404, "Player not found")
        existing_match = get_listening_match_player_serv(idMatch=data.idMatch)
        if existing_match:
            return send_success_response(409, "Match already exists")
        
        match = create_listening_match(data)
        print(f"Partida creada: {match.idMatch}")
        return send_success_response(201, "Match created successfully")
    except Exception as error:
        return get_details_error(error)
    
@listening_match_router.get("/all")
def get_listening_matchs_ctrl():
    try:
        matches = get_listening_matchs()

        if not matches:
            return send_success_response(404, "No matches found")
        
        return send_success_response(200, "Matches retrieved successfully", matches)
    except Exception as error:
        return get_details_error(error)
    

@listening_match_router.get("/top-scores/overall")
def get_top_scores_overall_ctrl(limit: int = 10):
    try:
        matches = get_top_scores_overall_serv(limit)

        if not matches:
            return send_success_response(404, "No top scores found.")

        return send_success_response(200, "Top scores retrieved successfully (overall).", matches)
    except Exception as error:
        return get_details_error(error)

@listening_match_router.get("/top-scores/by-difficulty/{difficulty}")
def get_top_scores_by_difficulty_ctrl(difficulty: str, limit: int = 10):
    try:
        matches = get_top_scores_by_difficulty_serv(difficulty, limit)

        if not matches:
            return send_success_response(404, f"No top scores found for difficulty: {difficulty}.")

        return send_success_response(200, f"Top scores retrieved successfully for difficulty: {difficulty}.", matches)
    except Exception as error:
        return get_details_error(error)
