from datetime import datetime, timedelta
from typing import Dict

from decouple import config
from jwt import ExpiredSignatureError, InvalidTokenError, decode, encode


JWT_SECRET = config("JWT_SECRET", default="myjwtsecret")

# Funcion para generar un token JWT
def generate_token(payload: Dict, expires_in: timedelta) -> str:
    expiration = datetime.now()+ expires_in
    payload["exp"] = expiration

    token = encode(payload, JWT_SECRET, algorithm="HS256")
    return token

def verify_token(token: str):
    try:
        user = decode(token, JWT_SECRET, algorithms=["HS256"])
        return user
    except ExpiredSignatureError:
        raise TokenExpiredError("El token ha expirado")
    except InvalidTokenError:
        raise InvalidTokenError("Token inválido")
    
class TokenExpiredError(Exception):
    """Excepción personalizada para manejar el caso de expiración del token."""
    pass

class InvalidTokenError(Exception):
    """Excepción personalizada para manejar el caso de token inválido."""
    pass
