from fastapi import HTTPException, status, Request

from src.utils.jwt_handle import verify_token

# Función para verificar el token JWT en la sesión
def session_validator(request: Request):
    try:
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={
                    "status": 401,
                    "message": "No tiene autorización"
                }
            )
        
        token = auth_header.split(" ").pop()
        user = verify_token(token)

        return user
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail={
                "status": 401, 
                "message": "Error de autorización", 
                "error": str(e)
                }
            ) 


