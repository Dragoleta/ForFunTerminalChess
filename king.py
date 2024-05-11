from piece import ChessPiece


class King(ChessPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def is_valid_move(self, row, col):
        position = self.position
        valid_moves = [
            (-1, -1),
            (-1, 0),
            (-1, +1),
            (0, -1),
            (0, +1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
        ]

        if (row - position[0], col - position[1]) not in valid_moves:
            print("Invalid move: ", self.position, (row, col))
            return False

        return True

    def move(self, row, col, board):
        where_to = board[row][col]

        if not self.is_valid_move(row, col) :
            return False

        if isinstance(where_to, ChessPiece):
            if where_to.color == self.color:
                return False
            where_to.capture()
        self.position = (row, col)

        return True

    def draw(self):
        return "w$" if self.color == "white" else "b$"
