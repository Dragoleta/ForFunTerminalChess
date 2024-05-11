from piece import ChessPiece

class Bishop(ChessPiece):

	def __init__(self, color, row, col):
		super().__init__(color, row, col)


	def move(self, row, col, board):


		if not self.is_valid_move(row, col, board):
			return False

		if isinstance(board[row][col], ChessPiece):
			if board[row][col].color == self.color:
				print("Can't move into a piece of the same color")
				return False
			board[row][col].capture()



		self.position = (row, col)
		return True


	
	def is_valid_move(self, row, col, board):
		a = self.position[0] - row
		b = self.position[1]  - col

		# TODO: Add colision detection
		if a - b != 0 and a + b != 0:
			return False


		return True



	def capture(self):
	    self.wasCaptured = True


	def draw(self): 
		return "wB" if self.color == "white" else "bB"

