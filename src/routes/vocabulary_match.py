from fastapi import APIRouter

from src.services.vocabulary_match_serv import create_vocabulary_match, get_vocabulary_matchs, get_vocabulary_match_player_serv, get_top_scores_overall_serv, get_top_scores_by_difficulty_serv
from src.services.player_serv import get_player_by_email_serv
from src.utils.handle_response import send_success_response 
from src.utils.error_handle import get_details_error
from src.models.vocabulary_match_model import VocabularyMatchModel

vocabulary_match_router = APIRouter()

@vocabulary_match_router.post("/register")
def post_vocabulary_match_ctrl(data: VocabularyMatchModel):
    try:
        print(f"Datos recibidos en el backend: {data.dict()}")
        player = get_player_by_email_serv(email=data.player)
        if not player:
            return send_success_response(404, "Player not found")
        existing_match = get_vocabulary_match_player_serv(idMatch=data.idMatch)
        if existing_match:
            return send_success_response(409, "Match already exists")
        
        match = create_vocabulary_match(data)
        print(f"Partida creada: {match.idMatch}")
        return send_success_response(201, "Match created successfully")
    except Exception as error:
        return get_details_error(error)
        
@vocabulary_match_router.get("/all")
def get_vocabulary_matchs_ctrl():
    try:
        matches = get_vocabulary_matchs()

        if not matches:
            return send_success_response(404, "No matches found")
        
        return send_success_response(200, "Matches retrieved successfully",matches)
    except Exception as error:
        return get_details_error(error)

@vocabulary_match_router.get("/top-scores/overall")
def get_top_scores_overall_ctrl():
    try:
        matches = get_top_scores_overall_serv()

        if not matches:
            return send_success_response(404, "No top scores found.")

        return send_success_response(200, "Top scores retrieved successfully (overall).", matches)
    except Exception as error:
        return get_details_error(error)

@vocabulary_match_router.get("/top-scores/by-difficulty/{difficulty}")
def get_top_scores_by_difficulty_ctrl(difficulty: str):
    try:
        matches = get_top_scores_by_difficulty_serv(difficulty)

        if not matches:
            return send_success_response(404, f"No top scores found for difficulty: {difficulty}.")

        return send_success_response(200, f"Top scores retrieved successfully for difficulty: {difficulty}.", matches)
    except Exception as error:
        return get_details_error(error)