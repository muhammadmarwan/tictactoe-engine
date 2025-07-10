import os
import ast
import numpy as np
from models.game_models import GameResponse, BoardState, Environment
from utils.agent import AgentEval

def process_move(game_state: BoardState) -> GameResponse:
    env = Environment()
    env.set_state(game_state.board)

    if env.game_over():
        return build_response(env)

    vo_val = np.load(os.path.join(os.path.dirname(__file__), "..", "vo.npy"))
    agent = AgentEval(env.o, vo_val)
    move = agent.take_action(env)
    env.game_over(force_recalculate=True)
    return build_response(env, move)

def get_status(board: str) -> GameResponse:
    board_list = ast.literal_eval(board)
    env = Environment()
    env.set_state(board_list)
    env.game_over(force_recalculate=True)
    return build_response(env)

def reset_board() -> GameResponse:
    env = Environment()
    return build_response(env)

def build_response(env: Environment, move=None) -> GameResponse:
    return GameResponse(
        board=env.board.tolist(),
        move=move,
        status=env.get_status_enum(),
        winner="X" if env.winner == env.x else "O" if env.winner == env.o else None
    )
