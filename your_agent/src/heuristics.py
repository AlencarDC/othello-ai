import your_agent.src.board_utils as board_utils
from board import Board


def score_heuristic(board: Board, color):
  return board.piece_count[color] / board_utils.board_size(board)


def score_difference_heuristic(board: Board, player_color):
  opponent_color = board.opponent(player_color)
  
  player_score = board.piece_count[player_color]
  opponent_score = board.piece_count[opponent_color]
  
  return (player_score - opponent_score) / (player_score + opponent_score)


def mobility_heuristic(board: Board, player_color):
  opponent_color = board.opponent(player_color)
  
  player_moves_count = len(board.legal_moves(player_color))
  opponent_moves_count = len(board.legal_moves(opponent_color))
  
  return (player_moves_count - opponent_moves_count) / (player_moves_count + opponent_moves_count + 1)


def corners_heuristic(board: Board, player_color):
  opponent_color = board.opponent(player_color)
  corners = [(0,0), (0,7), (7,0), (7,7)]
  
  player_corners = 0
  opponent_corners = 0
  for corner in corners:
    if board.tiles[corner[0]][corner[1]] == player_color:
      player_corners += 1
    elif board.tiles[corner[0]][corner[1]] == opponent_color:
      opponent_corners += 1
  
  return (player_corners - opponent_corners) / (player_corners + opponent_corners + 1)


def edges_heuristic(board: Board, player_color): 
  opponent_color = board.opponent(player_color)
  size = len(board.tiles)
  
  player_edges = 0
  opponent_edges = 0
  for i in range(size):
    if board.tiles[0][i] == player_color:
      player_edges += 1
    if board.tiles[size-1][i] == player_color:
      player_edges += 1
    if board.tiles[i][0] == player_color:
      player_edges += 1
    if board.tiles[i][7] == player_color:
      player_edges += 1
    
    if board.tiles[0][i] == opponent_color:
      opponent_edges += 1
    if board.tiles[size-1][i] == opponent_color:
      opponent_edges += 1
    if board.tiles[i][0] == opponent_color:
      opponent_edges += 1
    if board.tiles[i][7] == opponent_color:
      opponent_edges += 1
      
  return (player_edges - opponent_edges) / (player_edges + opponent_edges + 1)


def parity_heuristic(board: Board, color):
  score = board.piece_count[color]
  
  remaining_positions = board_utils.board_size(board) - score
  
  return -1 if remaining_positions % 2 == 0 else 1