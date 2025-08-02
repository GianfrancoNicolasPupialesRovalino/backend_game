from database import ListeningMatch
from models.listening_match_model import ListeningMatchModel


def create_listening_match(data: ListeningMatchModel):
    try:
        match = ListeningMatch.create(
            idMatch=data.idMatch,
            player=data.player,
            score=data.score,
            accuracy=data.accuracy,
            name_video=data.name_video,
            difficulty=data.difficulty,
            time=data.time,
            date=data.date
        )
        return match
    except Exception as error:
        raise error

def get_listening_matchs():
    try:
        matches = ListeningMatch.select(
            ListeningMatch.idMatch,
            ListeningMatch.player,
            ListeningMatch.score,
            ListeningMatch.accuracy,
            ListeningMatch.name_video,
            ListeningMatch.difficulty,
            ListeningMatch.time,
            ListeningMatch.date
        )
        serialized_matches = [{
            "idMatch": match.idMatch,
            "player": match.player.email,
            "score": match.score,
            "accuracy": match.accuracy,
            "name_video": match.name_video,
            "difficulty": match.difficulty,
            "time": match.time,
            "date": match.date.isoformat()
            } 
            for match in matches
        ]
        return serialized_matches
    except Exception as error:
        raise error

def get_listening_match_player_serv(idMatch: int):
    try:
        match = ListeningMatch.select(
            ListeningMatch.idMatch,
            ListeningMatch.player,
            ListeningMatch.score,
            ListeningMatch.accuracy,
            ListeningMatch.name_video,
            ListeningMatch.difficulty,
            ListeningMatch.time,
            ListeningMatch.date
        ).where(ListeningMatch.idMatch == idMatch).first()

        if match:
            serialized_match = {
                "idMatch": match.idMatch,
                "player": match.player.email,
                "score": match.score,
                "accuracy": match.accuracy,
                "name_video": match.name_video,
                "difficulty": match.difficulty,
                "time": match.time,
                "date": match.date.isoformat()
            }
            return serialized_match
        else:
            return None
    except Exception as error:
        raise error
    
def get_top_scores_overall_serv(limit: int = 10):
    try:
        matches = ListeningMatch.select(
                ListeningMatch.idMatch,
                ListeningMatch.player,
                ListeningMatch.score,
                ListeningMatch.accuracy,
                ListeningMatch.name_video,
                ListeningMatch.difficulty,
                ListeningMatch.time,
                ListeningMatch.date
            ).order_by(ListeningMatch.score.desc()).limit(limit)
        serialized_matches = [{
            "idMatch": match.idMatch,
            "player": match.player.email,
            "score": match.score,
            "accuracy": match.accuracy,
            "name_video": match.name_video,
            "difficulty": match.difficulty,
            "time": match.time,
            "date": match.date.isoformat()
            }
            for match in matches
        ]
        return serialized_matches
    except Exception as error:
        raise error
    

def get_top_scores_by_difficulty_serv(difficulty: str, limit: int = 10):
    try:
        matches = ListeningMatch.select(
                ListeningMatch.idMatch,
                ListeningMatch.player,
                ListeningMatch.score,
                ListeningMatch.accuracy,
                ListeningMatch.name_video,
                ListeningMatch.difficulty,
                ListeningMatch.time,
                ListeningMatch.date
            ).where(ListeningMatch.difficulty == difficulty).order_by(ListeningMatch.score.desc()).limit(limit)
        serialized_matches = [{
            "idMatch": match.idMatch,
            "player": match.player.email,
            "score": match.score,
            "accuracy": match.accuracy,
            "name_video": match.name_video,
            "difficulty": match.difficulty,
            "time": match.time,
            "date": match.date.isoformat()
            }
            for match in matches
        ]
        return serialized_matches
    except Exception as error:
        raise error
