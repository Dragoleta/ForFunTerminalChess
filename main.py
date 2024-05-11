import subprocess
from board import draw_board, get_board, get_elements, board_setup
from player import Player


subprocess.run("clear")

empty_board = get_board()
elements = get_elements()
board = board_setup(empty_board)

turn = 0

playerW = Player("white")
playerB = Player("black")


while True:
    subprocess.run("clear")
    
    playing = playerW if turn % 2 == 0 else playerB

    print(playing.color)



    draw_board(board)

    try:
        pieceCol = str(input("Piece coluna: (|) "))
        pieceRow = int(input("Piece linha: (--) ")) - 1

        moveCol = str(input("Move coluna: (|) "))
        moveRow = int(input("Move Linha: (--) ")) - 1

        if pieceCol in elements and moveCol in elements:
            pieceCol = elements.index(pieceCol)
            moveCol = elements.index(moveCol)

    except ValueError:
        print("Invalid input")
        input("")
        continue

    if playing.color != board[pieceRow][pieceCol].color:
        print("can't move oponents pieces")
        input("")
        continue


    if board[pieceRow][pieceCol].move(moveRow, moveCol, board) == True:
        aux = board[moveRow][moveCol]
        board[moveRow][moveCol] = board[pieceRow][pieceCol]
        board[pieceRow][pieceCol] = aux



    turn += 1
    input("")
