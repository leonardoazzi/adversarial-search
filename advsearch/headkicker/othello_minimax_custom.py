import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, 5, evaluate_custom)


def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    board = state.board.tiles
    opponent = Board.opponent(player)
    player_score = 0
    opponent_score = 0
    for row_idx, row in enumerate(board):
        for (col_idx, node) in enumerate(row):
            score = EVAL_TEMPLATE[row_idx][col_idx]
            if (node == player):
                player_score += score
            elif (node == opponent):
                opponent_score += score

    weighted_score = player_score - opponent_score

    # Diferença de Peças: Diferença entre o número de peças do jogador e do oponente
    player_pieces = sum(1 for x in range(8) for y in range(8) if board[x][y] == player)
    opponent_pieces = sum(1 for x in range(8) for y in range(8) if board[x][y] == opponent)
    piece_difference_score = player_pieces - opponent_pieces

    # Mobilidade: Diferença entre o número de movimentos legais do jogador e do oponente
    player_legal_moves = len(state.board.legal_moves(player))
    opponent_legal_moves = len(state.board.legal_moves(opponent))
    mobility_score = player_legal_moves - opponent_legal_moves

    # Pesos: Ajuste esses valores conforme necessário
    piece_difference_weight = 0.3
    mobility_weight = 0.7
    weighted_score_weight = 1

    # Calculando a pontuação final
    evaluation = (piece_difference_weight * piece_difference_score +
                   mobility_weight * mobility_score +
                   weighted_score_weight * weighted_score)

    return evaluation

