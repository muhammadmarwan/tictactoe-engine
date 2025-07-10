from pydantic import BaseModel
from typing import List, Optional
import numpy as np

LENGTH = 3

class BoardState(BaseModel):
    board: List[List[int]]
    player: str

class GameResponse(BaseModel):
    board: List[List[int]]
    move: Optional[tuple]
    status: str
    winner: Optional[str]

class Environment:
    def __init__(self):
        self.board = np.zeros((LENGTH, LENGTH))
        self.x = -1
        self.o = 1
        self.winner = None
        self.ended = False

    def is_empty(self, i, j):
        return self.board[i, j] == 0

    def set_state(self, state):
        self.board = np.array(state)
        self.game_over()

    def get_state(self):
        h = 0
        k = 0
        for i in range(LENGTH):
            for j in range(LENGTH):
                cell = self.board[i, j]
                v = 0 if cell == 0 else 1 if cell == self.x else 2
                h += (3 ** k) * v
                k += 1
        return h

    def game_over(self, force_recalculate=False):
        if not force_recalculate and self.ended:
            return self.ended

        for i in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[i].sum() == player * LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        for j in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[:, j].sum() == player * LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        for player in (self.x, self.o):
            if self.board.trace() == player * LENGTH or np.fliplr(self.board).trace() == player * LENGTH:
                self.winner = player
                self.ended = True
                return True

        if np.all(self.board != 0):
            self.winner = None
            self.ended = True
            return True

        return False

    def get_status_enum(self):
        if not self.ended:
            return "ONGOING"
        if self.winner == self.x:
            return "WIN"
        if self.winner == self.o:
            return "LOSS"
        return "DRAW"
