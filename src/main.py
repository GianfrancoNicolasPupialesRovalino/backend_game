from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from src.routes.auth import auth_router
from src.routes.player import player_router
from src.utils.handle_response import send_error_response

app = FastAPI()

# Configuration for CORS
origins = [
    "http://localhost:5173",
]
# incluir la URL del juego en producción 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Orígenes permitidos
    allow_credentials=True,  # Permitir cookies y credenciales
    allow_methods=["*"],  # Métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Encabezados permitidos
)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Welcomer to Usability Games</h1>"

app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(player_router, prefix="/api/v1/player")




@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc: HTTPException):
    # Comprobamos si `exc.detail` es un dict, y lo formateamos.
    if isinstance(exc.detail, dict):
        return send_error_response(
            exc.status_code, exc.detail["message"], exc.detail["error"]
        )
    return send_error_response(exc.status_code, exc.detail)