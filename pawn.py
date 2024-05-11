from piece import ChessPiece


class Pawn(ChessPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

        self.hasMoved = False

    def move(self, row, col, board):
        #   board[row= row][col= col]

        if self.is_valid_moves(row, col, board) == False:
            return False

        self.hasMoved = True
        self.position = (row, col)

        if isinstance(board[row][col], ChessPiece):
            board[row][col].capture()

        return True

    def is_valid_moves(self, row, col, board):

        step_size = 2 if self.hasMoved == False else 1
        step_direction = step_size if self.color == "black" else (step_size * -1)
        where_to = board[row][col]

        print(self.hasMoved, step_size, step_direction)
        if isinstance(where_to, ChessPiece):
            if where_to.color == self.color:
                return False

            row_dir = -1 if self.position[0] > row else 1

            if not self.position[0] + row_dir == row:
                print(
                    "Pawn can only move 1 step diagonally at a time when capturing an enemy piece"
                )
                return False

        else:
            if not self.position[1] == col:
                print("Pawn can only move diagonally when capturing an enemy piece")
                return False

        if self.color == "black":
            if not self.position[0] + step_direction >= row:
                print("Pawn can only move 1 step forward at a time ")
                return False
        else:
            if not self.position[0] + step_direction <= row:
                print("Pawn can only move 1 step forward at a time ")
                return False

        return True

    def capture(self):
        self.wasCaptured = True
        print("Captured")

    def draw(self):
        return "wP" if self.color == "white" else "bP"
