class AgentEval:
    def __init__(self, sym, value_sym):
        self.sym = sym
        self.V = value_sym

    def take_action(self, env):
        best_value = -1
        next_move = None
        for i in range(3):
            for j in range(3):
                if env.is_empty(i, j):
                    env.board[i, j] = self.sym
                    state = env.get_state()
                    env.board[i, j] = 0
                    if self.V[state] > best_value:
                        best_value = self.V[state]
                        next_move = (i, j)
        if next_move:
            env.board[next_move[0], next_move[1]] = self.sym
        return next_move
