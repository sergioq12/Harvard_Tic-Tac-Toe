"""
Tic Tac Toe Player
"""

import math
from pprint import pprint
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty_counts = 0
    for row in board:
        for col in row:
            if col == EMPTY:
                empty_counts += 1
    
    if empty_counts % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                action = (row, col)
                actions.add(action)

    return actions

def checkAction(board, action):
    """
    Returns if the action is possible.
    """
    row, col = action
    if row < 0 or row > len(board) or col < 0 or col > len(board[0]):
        return False
    elif board[row][col] != EMPTY:
        return False
    return True

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_to_play = player(board)
    new_board = deepcopy(board)
    if not checkAction(new_board, action):
        raise Exception("That action is not possible")
    row, col = action
    new_board[row][col] = player_to_play
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal Check
    if (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (board[1][0] == X and board[1][1] == X and board[1][2] == X) or (board[2][0] == X and board[2][1] == X and board[2][2] == X):
        return X
    elif (board[0][0] == O and board[0][1] == O and board[0][2] == O) or (board[1][0] == O and board[1][1] == O and board[1][2] == O) or (board[2][0] == O and board[2][1] == O and board[2][2] == O):
        return O

    # Vertical Check
    if (board[0][0] == X and board[1][0] == X and board[2][0] == X) or (board[0][1] == X and board[1][1] == X and board[2][1] == X) or (board[0][2] == X and board[1][2] == X and board[2][2] == X):
        return X
    elif (board[0][0] == O and board[1][0] == O and board[2][0] == O) or (board[0][1] == O and board[1][1] == O and board[2][1] == O) or (board[0][2] == O and board[1][2] == O and board[2][2] == O):
        return X

    # Diagonal Check
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return O
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O

    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    empty_counts = 0
    for row in board:
        for col in row:
            if col == EMPTY:
                empty_counts += 1
    if empty_counts == 0:
        return True

    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def Max(board):
    if terminal(board):
        return utility(board), None

    possible_actions = actions(board)
    max_value = float("-Inf")
    best_move = None
    for action in possible_actions:
        nextState = result(board, action)
        util, action_min = Min(nextState)
        if util > max_value:
            max_value = util
            best_move = action
            if max_value == 1:
                return max_value, best_move

    return max_value, best_move


def Min(board):
    if terminal(board):
        return utility(board), None

    possible_actions = actions(board)
    min_value = float("Inf")
    best_move = None
    for action in possible_actions:
        nextState = result(board, action)
        util, action_max = Max(nextState)
        if util < min_value:
            min_value = util     
            best_move = action
            if min_value == -1:
                return min_value, best_move

    return min_value, best_move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    if current_player == X:
        # as player is X we want to check the movements by the Min action
        value, action = Max(board)
        return action
    else:
        value, action = Min(board)
        return action