from piece import ChessPiece


class Rook(ChessPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)


    def is_valid_move(self, row, col, board):

        if self.position[0] != row and self.position[1] != col:
            print("Rook can only move vertically and horizontally")
            return False

    
        if self.position[0] == row:
            step = 1 if col > self.position[1] else -1
            for c in range(self.position[1] + step, col, step):
                if isinstance(board[row][c], ChessPiece):
                    print("There's an obstruction on the path")
                    return False
        else:  
            step = 1 if row > self.position[0] else -1
            for r in range(self.position[0] + step, row, step):
                if isinstance(board[r][col], ChessPiece):
                    print("There's an obstruction on the path")
                    return False

        return True

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

    def draw(self):
        return "wR" if self.color == "white" else "bR"
