from piece import ChessPiece


class Knight(ChessPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def is_valid_move(self, row, col):
        where_to = (row, col)
        position = self.position
        valid_moves = [
            (-1, -2),
            (+1, -2),
            (-2, -1),
            (-2, +1),
            (-1, +2),
            (+1 + 2),
            (+2, -1),
            (+2, +1),
        ]

        if (position[0] - row, position[1] - col) not in valid_moves:
            print("Invalid move: ", self.position, (row, col))
            return False

        return True

    def move(self, row, col, board):
        where_to = board[row][col]

        if self.is_valid_move(row, col) == False:
            return False

        if isinstance(where_to, ChessPiece):
            print("moving into piece")
            if where_to.color == self.color:
                print("moving into same color piece")
                return False
            where_to.capture()
        self.position = (row, col)

        return True

    def capture(self):
        self.wasCaptured = True

    def draw(self):
        return "wK" if self.color == "white" else "bK"
