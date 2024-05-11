from piece import ChessPiece
from bishop import Bishop
from rook import Rook

class Queen(ChessPiece):
	def __init__(self, color, row, col):
		super().__init__(color, row, col)


	def is_valid_move(self, row, col, board):
		
		if not Rook.is_valid_move(self, row, col, board) and not Bishop.is_valid_move(self, row, col, board):	
			return False
		
		return True




	def draw(self):
		return "wQ" if self.color == "white" else "wQ"
