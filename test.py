
from board import Board
from your_agent.agent  import make_move

board = Board()

board.tiles = [
    ['.','B','B','B','B','B','B','B'],
    ['W','B','B','B','B','B','B','B'],
    ['W','W','B','B','B','W','B','B'],
    ['W','B','W','B','W','B','W','B'],
    ['W','B','W','W','B','B','W','B'],
    ['W','W','B','W','B','B','B','B'],
    ['W','.','B','B','B','B','B','B'],
    ['.','B','B','B','B','B','B','.']
  ]

board.print_board()
print(board.legal_moves('B'))
print(make_move(board, 'B'))