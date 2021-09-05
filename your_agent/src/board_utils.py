import copy
from board import Board


def get_next_board(board: Board, move, color):
  new_board = copy.deepcopy(board)
  new_board.process_move(move, color)
  return new_board

def board_size(board: Board): 
  return len(board.tiles) * len(board.tiles[0])
