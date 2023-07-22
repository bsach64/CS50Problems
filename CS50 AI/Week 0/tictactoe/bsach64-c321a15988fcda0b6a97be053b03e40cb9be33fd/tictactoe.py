"""
Tic Tac Toe Player
"""
import copy
import math

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
    count_EMPTY = 0
    for row in board:
        for element in row:
            if element == EMPTY:        
                count_EMPTY += 1
    
    if count_EMPTY == 0:
        return None
    elif (count_EMPTY % 2) == 0:
        return O
    else:
        return X    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] == EMPTY:
        duplicate = copy.deepcopy(board)
        next_move = player(duplicate)
        duplicate[action[0]][action[1]] = next_move
        return duplicate
    else:
        raise Exception("Invalid Action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    players = [X, O]
    for player in players:
        for i in range(0, 3):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                return player
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                return player
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return player
            if board[0][2] == player and board[1][1] == player and board[2][0] == player:
                return player
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if player(board) == None:
        return True
    elif winner(board) != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1 
    elif winner(board) == None:
        return 0
    return 0

def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        value_actions = []
        for action in actions(board):
            value_actions.append([min_value(result(board, action)), action])
        optimal = max(value_actions, key=lambda x: x[0])
        return optimal[1]
    
    if player(board) == O:
        value_actions = []
        for action in actions(board):
            value_actions.append([max_value(result(board, action)), action])
        optimal = min(value_actions, key=lambda x: x[0])
        return optimal[1]


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v