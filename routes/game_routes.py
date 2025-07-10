from fastapi import APIRouter, HTTPException
from models.game_models import BoardState, GameResponse
from services.game_service import process_move, get_status, reset_board

router = APIRouter()

@router.post("/move", response_model=GameResponse)
def make_move(game_state: BoardState):
    try:
        return process_move(game_state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/game-state", response_model=GameResponse)
def get_game_state(board: str):
    try:
        return get_status(board)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/reset", response_model=GameResponse)
def reset_game():
    return reset_board()
