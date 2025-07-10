from fastapi import FastAPI
from routes.game_routes import router as game_router
from middleware.auth_key_middleware import verify_internal_api_key

app = FastAPI()

app.middleware("http")(verify_internal_api_key)

app.include_router(game_router, prefix="/game")