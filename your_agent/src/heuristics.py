import your_agent.src.board_utils as board_utils
from board import Board


def score_heuristic(board: Board, color):
  return board.piece_count[color] / board_utils.board_size(board)


def mobility_heuristic(board: Board, color):
  legal_moves_count = len(board.legal_moves(color))
  opponent_legal_moves_count = len(board.legal_moves(board.opponent(color)))
  
  if legal_moves_count == 0 and opponent_legal_moves_count == 0:
    return 0
  
  denominator = max(legal_moves_count, opponent_legal_moves_count)
  
  return (legal_moves_count - opponent_legal_moves_count) / denominator

# Check if next moves enables to get a corner
def corner_heuristic(board: Board, color):
  value = 0
  corners = [(0,0), (0,7), (7,0), (7,7)]
  legal_moves = board.legal_moves(color)
  for corner in corners:
    if corner in legal_moves:
      value = 1

  legal_moves = board.legal_moves(board.opponent(color))
  for corner in corners:
    if corner in legal_moves:
      value = -1
  
  return value


def edges_heuristic(board: Board, color): 
  size = len(board.tiles)
  
  # Suppose it is a square board
  edges_score = 0
  for i in range(size):
    if board.tiles[0][i] == color:
      edges_score += 1
    if board.tiles[size-1][i] == color:
      edges_score += 1
    if board.tiles[i][0] == color:
      edges_score += 1
    if board.tiles[i][7] == color:
      edges_score += 1
      
  return edges_score / (4 * size)

