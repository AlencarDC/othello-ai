from your_agent.src.minimax import MinimaxSolver
from board import Board

def make_move(the_board: Board, color):
  solver = MinimaxSolver()
  move = solver.minimax(the_board, color, 4)
  
  if move == None:
    return (-1, -1)
  return move

