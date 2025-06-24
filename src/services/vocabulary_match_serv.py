from src.database import VocabularyMatch
from src.models.vocabulary_match_model import VocabularyMatchModel


def create_vocabulary_match(data: VocabularyMatchModel):
    try:
        match = VocabularyMatch.create(
            idMatch=data.idMatch,
            player=data.player,
            num_words=data.num_words,
            difficulty=data.difficulty,
            score=data.score,
            time=data.time,
            date=data.date
        )
        return match
    except Exception as error:
        raise error

def get_vocabulary_matchs():
    try:
        matches = VocabularyMatch.select(
            VocabularyMatch.idMatch,
            VocabularyMatch.player,
            VocabularyMatch.num_words,
            VocabularyMatch.difficulty,
            VocabularyMatch.score,
            VocabularyMatch.time,
            VocabularyMatch.date
        )
        serialized_matches = [{
            "idMatch": match.idMatch,
            "player": match.player.email,
            "num_words": match.num_words,
            "difficulty": match.difficulty,
            "score": match.score,
            "time": match.time,
            "date": match.date.isoformat()
            } 
            for match in matches
        ]
        return serialized_matches
    except Exception as error:
        raise error
    
def get_vocabulary_match_player_serv(idMatch: int):
    try:
        match = VocabularyMatch.select(
            VocabularyMatch.idMatch,
            VocabularyMatch.player,
            VocabularyMatch.num_words,
            VocabularyMatch.difficulty,
            VocabularyMatch.score,
            VocabularyMatch.time,
            VocabularyMatch.date
        ).where(VocabularyMatch.idMatch == idMatch).first()
        
        if match:
            serialized_match = {
                "idMatch": match.idMatch,
                "player": match.player.email,
                "num_words": match.num_words,
                "difficulty": match.difficulty,
                "score": match.score,
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
        matches = VocabularyMatch.select(
            VocabularyMatch.idMatch,
            VocabularyMatch.player,
            VocabularyMatch.num_words,
            VocabularyMatch.difficulty,
            VocabularyMatch.score,
            VocabularyMatch.time,
            VocabularyMatch.date
        ).order_by(VocabularyMatch.score.desc()).limit(limit)

        serialized_matches = [{
            "idMatch": match.idMatch,
            "player": match.player.email,
            "num_words": match.num_words,
            "difficulty": match.difficulty,
            "score": match.score,
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
        matches = VocabularyMatch.select(
            VocabularyMatch.idMatch,
            VocabularyMatch.player,
            VocabularyMatch.num_words,
            VocabularyMatch.difficulty,
            VocabularyMatch.score,
            VocabularyMatch.time,
            VocabularyMatch.date
        ).where(VocabularyMatch.difficulty == difficulty).order_by(VocabularyMatch.score.desc()).limit(limit)

        serialized_matches = [{
            "idMatch": match.idMatch,
            "player": match.player.email,
            "num_words": match.num_words,
            "difficulty": match.difficulty,
            "score": match.score,
            "time": match.time,
            "date": match.date.isoformat()
            }
            for match in matches
        ]
        return serialized_matches
    except Exception as error:
        raise error