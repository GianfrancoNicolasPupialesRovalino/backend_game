from src.database import GrammarMatch

from src.models.grammar_match_model import GrammarMatchModel
from src.utils.error_handle import get_details_error
from src.utils.handle_response import send_success_response

def create_grammar_match(data: GrammarMatchModel):
    try:
        match = GrammarMatch.create(
            idMatch=data.idMatch,
            player=data.player,
            session_name=data.session_name,
            difficulty=data.difficulty,
            time=data.time,
            score=data.score,
            completion=data.completion,
            date=data.date
        )
        return match
    except Exception as error:
        raise error
    
def get_grammar_matchs():
    try:
        matches = GrammarMatch.select(
            GrammarMatch.idMatch,
            GrammarMatch.player,
            GrammarMatch.session_name,
            GrammarMatch.difficulty,
            GrammarMatch.time,
            GrammarMatch.score,
            GrammarMatch.completion,
            GrammarMatch.date
        )
        serialized_matches = [{
            "idMatch": match.idMatch,
            "player": match.player.email,
            "session_name": match.session_name,
            "difficulty": match.difficulty,
            "time": match.time,
            "score": match.score,
            "completion": match.completion,
            "date": match.date.isoformat()
            } 
            for match in matches
        ]
        return serialized_matches
    except Exception as error:
        raise error
    
def get_grammar_match_player_serv(idMatch: int):
    try:
        match = GrammarMatch.select(
           GrammarMatch.idMatch,
            GrammarMatch.player,
            GrammarMatch.session_name,
            GrammarMatch.difficulty,
            GrammarMatch.time,
            GrammarMatch.score,
            GrammarMatch.completion,
            GrammarMatch.date
        ).where(GrammarMatch.idMatch == idMatch).first()
        if match:
            serialized_match = {
                "idMatch": match.idMatch,
                "player": match.player.email,
                "session_name": match.session_name,
                "difficulty": match.difficulty,
                "time": match.time,
                "score": match.score,
                "completion": match.completion,
                "date": match.date.isoformat()
            }
            return serialized_match
        else:
            return None
    except Exception as error:
        raise error

def get_top_scores_overall_serv(limit: int = 10):
    try:
        matches = GrammarMatch.select(
            GrammarMatch.idMatch,
            GrammarMatch.player,
            GrammarMatch.session_name,
            GrammarMatch.difficulty,
            GrammarMatch.time,
            GrammarMatch.score,
            GrammarMatch.completion,
            GrammarMatch.date
        ).order_by(GrammarMatch.score.desc()).limit(limit)

        serialized_matches = [{
            "idMatch": match.idMatch,
            "player": match.player.email,
            "session_name": match.session_name,
            "difficulty": match.difficulty,
            "time": match.time,
            "score": match.score,
            "completion": match.completion,
            "date": match.date.isoformat()
            } 
            for match in matches
        ]
        return serialized_matches
    except Exception as error:
        raise error

def get_top_scores_by_difficulty_serv(difficulty: str, limit: int = 10):
    try:
        matches = GrammarMatch.select(
            GrammarMatch.idMatch,
            GrammarMatch.player,
            GrammarMatch.session_name,
            GrammarMatch.difficulty,
            GrammarMatch.time,
            GrammarMatch.score,
            GrammarMatch.completion,
            GrammarMatch.date
        ).where(GrammarMatch.difficulty == difficulty).order_by(GrammarMatch.score.desc()).limit(limit)

        serialized_matches = [{
            "idMatch": match.idMatch,
            "player": match.player.email,
            "session_name": match.session_name,
            "difficulty": match.difficulty,
            "time": match.time,
            "score": match.score,
            "completion": match.completion,
            "date": match.date.isoformat()
            } 
            for match in matches
        ]
        return serialized_matches
    except Exception as error:
        raise error