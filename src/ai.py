import math
from queue import Queue

from board import Board


def utility(board: Board, victory: bool, player: int, is_me: bool):
    if victory:
        return -1000 if is_me else 1000
    return board.eval(player)


def min_max_value(board: Board, initial_turn: int, turn: int, deepness: int, alpha: float, beta: float, is_max: bool):
    # Terminal state 🛑
    moves = board.get_possible_moves()
    victory = board.check_victory()
    if victory or len(moves) == 0 or turn - initial_turn >= deepness:
        return utility(board, victory, 2 - (turn % 2), turn % 2 == initial_turn % 2), None

    # Normal iteration 🔄
    v = -math.inf if is_max else math.inf
    current_move = None
    for move in moves:
        new_board = board.copy()
        new_board.add_disk(move, 2 - (turn % 2))
        new_v, _ = min_max_value(new_board, initial_turn, turn + 1, deepness, alpha, beta, not is_max)
        v = max(v, new_v) if is_max else min(v, new_v)
        if v == new_v or current_move is None:
            current_move = move

        # Alpha-Beta magic ✨
        if (is_max and v >= beta) or (not is_max and v >= alpha):
            return v, current_move
        if is_max:
            alpha = max(alpha, v)
        else:
            beta = max(beta, v)

    return v, current_move


def alpha_beta_decision(board: Board, turn: int, ai_level: int, queue: Queue, max_player):
    v, move = min_max_value(board, turn, turn, ai_level, -math.inf, math.inf, True)
    queue.put(move)
