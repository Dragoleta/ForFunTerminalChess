class ChessPiece:
    def __init__(self, color, row, col):
        self.color = color
        self.position = (row, col)
        self.intialPos = (row, col)
        self.wasCaptured = False

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
        
    def is_valid_move(self, row, col, board): ...

    def capture(self):
        self.wasCaptured = True

    def draw(self): ...
