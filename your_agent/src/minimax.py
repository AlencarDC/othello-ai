import your_agent.src.board_utils as board_utils
from your_agent.src.heuristics import edges_heuristic, mobility_heuristic, score_heuristic, corner_heuristic
from board import Board


class MinimaxSolver(object):
  def __init__(self):
    pass

  def heuristic(self, board: Board, color):
    return 4*corner_heuristic(board, color) + 4*edges_heuristic(board, color) + 1*mobility_heuristic(board, color) + score_heuristic(board, color)
  
  def minimax(self, board, color, depth=0):
    _, max_move = self.maxvalue(board, color, depth)
    return max_move
  
  def maxvalue(self, board: Board, color, depth=0, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or board.is_terminal_state():
      return (self.heuristic(board, color), None)
    
    best_move_index = -1
    value = float('-inf')
    legal_moves = board.legal_moves(color)
    
    for index, move in enumerate(legal_moves):
      new_board = board_utils.get_next_board(board, move, color)
      min_value, _ = self.minvalue(new_board, color, depth - 1, alpha, beta)
      if min_value > value:
        value = min_value
        best_move_index = index
      
      alpha = max(alpha, value)
      if alpha >= beta:
        break
      
    if best_move_index < 0:
      return (self.heuristic(board, color), None)
    
    return (value, legal_moves[best_move_index])
    
      
  
  def minvalue(self, board: Board, color, depth=0, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or board.is_terminal_state():
      return (self.heuristic(board, color), None)
    
    best_move_index = -1
    value = float('inf')
    legal_moves = board.legal_moves(board.opponent(color))
    
    for index, move in enumerate(legal_moves):
      new_board = board_utils.get_next_board(board, move, board.opponent(color))
      max_value, _ = self.maxvalue(new_board, color, depth - 1, alpha, beta)
      if max_value < value:
        value = max_value
        best_move_index = index
      
      beta = min(beta, value)
      if beta <= alpha:
        break
      
    if best_move_index < 0:
      return (self.heuristic(board, color), None)
    
    return (value, legal_moves[best_move_index])