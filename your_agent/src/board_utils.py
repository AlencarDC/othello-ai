import copy
from board import Board


def get_next_board(board: Board, move, color):
  new_board = copy.deepcopy(board)
  new_board.process_move(move, color)
  return new_board

def board_size(board: Board): 
  return len(board.tiles) * len(board.tiles[0])


# An Othello is divided into 3 phases:
# Opening/early game -> first 20 moves
# Mid-game -> next 20 moves
# End-game -> last 20 moves
# Source: https://www.ultraboardgames.com/othello/strategy.php
# For each move, 1 piece is added to the board, so we can
# define the game phase by the game number of pieces in the board
# (disregarding the 4 initial pieces)
EARLY_GAME = 'EARLY_GAME'
MID_GAME = 'MID_GAME'
END_GAME = 'END_GAME'
def game_phase(board: Board):
  pieces_count = board.piece_count[board.WHITE] + board.piece_count[board.BLACK]
  pieces_count -= 4 # removing the initial pieces
  
  if pieces_count <= 20:
    return EARLY_GAME
  elif pieces_count <= 40:
    return MID_GAME
  else:
    return END_GAME
  

def is_early_game(board: Board):
  return game_phase(board) == EARLY_GAME


def is_mid_game(board: Board):
  return game_phase(board) == MID_GAME


def is_end_game(board: Board):
  return game_phase(board) == END_GAME