from copy import deepcopy
from piece import ChessPiece
from king import King
from knight import Knight
from pawn import Pawn
from rook import Rook
from bishop import Bishop
from queen import Queen

row1 = ["x ", "o ", "x ", "o ", "x ", "o ", "x ", "o "]
row2 = ["o ", "x ", "o ", "x ", "o ", "x ", "o ", "x "]
row3 = ["x ", "o ", "x ", "o ", "x ", "o ", "x ", "o "]
row4 = ["o ", "x ", "o ", "x ", "o ", "x ", "o ", "x "]
row5 = ["x ", "o ", "x ", "o ", "x ", "o ", "x ", "o "]
row6 = ["o ", "x ", "o ", "x ", "o ", "x ", "o ", "x "]
row7 = ["x ", "o ", "x ", "o ", "x ", "o ", "x ", "o "]
row8 = ["o ", "x ", "o ", "x ", "o ", "x ", "o ", "x "]
BOARD_ORI = [row1, row2, row3, row4, row5, row6, row7, row8]


def get_board():
    return deepcopy(BOARD_ORI)


def get_elements():
    elements = ["a", "b", "c", "d", "e", "f", "g", "h"]
    return elements


def draw_board(board):

    for num, col in enumerate(board, 1):
        for num2, row in enumerate(col):
            if isinstance(row, ChessPiece):



                p = row.draw() if row.wasCaptured == False else BOARD_ORI[num - 1][num2 -1]

                # if row.wasCaptured == True:
                #     row = boardoOri[num][num2]
                # else:
                #     row = row.draw()

                print(p, end="| ")
            else:
                print(row, end="| ")

        print(num, end="\n")
    print("a ", " b ", " c ", " d ", " e ", " f ", " g ", " h ")


def board_setup(board):
    for i in range(8):
    #   board[x= row][y= col]
        board[1][i] = Pawn(color="black", row=1, col=i)
        board[6][i] = Pawn(color="white", row=6, col=i)


    # Knights
    board[0][1] = Knight(color="black", row=0, col=1)
    board[0][6] = Knight(color="black", row=0, col=6)

    board[7][1] = Knight(color="white", row=7, col=1)
    board[7][6] = Knight(color="white", row=7, col=6)

    # Bishops
    board[0][2] = Bishop(color="black", row=0, col=2)
    board[0][5] = Bishop(color="black", row=0, col=5)

    board[7][2] = Bishop(color="white", row=7, col=2)
    board[7][5] = Bishop(color="white", row=7, col=5)

    # Queens
    board[0][4] = Queen(color="black", row=0, col=4)
    board[7][3] = Queen(color="white", row=7, col=3)


    # Rooks
    board[0][0] = Rook(color="black", row=0, col=0)
    board[0][7] = Rook(color="black", row=0, col=7)

    board[7][0] = Rook(color="white", row=7, col=0)
    board[7][7] = Rook(color="white", row=7, col=7)

    # Kings
    board[0][3] = King(color="black", row=0, col=3)
    board[7][4] = King(color="black", row=7, col=4)

    return board