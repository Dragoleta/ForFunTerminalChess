import subprocess
from board import draw_board, get_board, get_elements, board_setup
from player import Player
import asyncio
from websockets.server import serve
import websockets
from websockets.sync.client import connect
import json
from typing import List

CHOICE:int

def get_player_input(playing, board):
	elements = get_elements()
	while True:
		try:
			pieceCol = str(input("Piece coluna: (|) "))
			pieceRow = int(input("Piece linha: (--) ")) - 1

			moveCol = str(input("Move coluna: (|) "))
			moveRow = int(input("Move Linha: (--) ")) - 1

			if pieceCol in elements and moveCol in elements:
				pieceCol = elements.index(pieceCol)
				moveCol = elements.index(moveCol)

			if playing.color != board[pieceRow][pieceCol].color:
				print("can't move oponents pieces")
				continue


			return pieceCol, pieceRow, moveCol, moveRow
			break


		except ValueError:
			print("Invalid input")
			input("")
			continue
		

def move_selected_pieces(board, pieceCol, pieceRow, moveCol, moveRow):

	if board[pieceRow][pieceCol].move(moveRow, moveCol, board) == True:
		aux = board[moveRow][moveCol]
		board[moveRow][moveCol] = board[pieceRow][pieceCol]
		board[pieceRow][pieceCol] = aux
		return board

	

async def runGame(websocket = None, whoAmI:str = None):
	subprocess.run("clear")

	empty_board = get_board()
	board = board_setup(empty_board)

	turn = 0

	if "host" == whoAmI:
		host = Player("white", whoAmI)
		client = Player("black", "client")
	elif "client" == whoAmI:
		host = Player("white", "host")
		client = Player("black", whoAmI)
	else:
		host = Player("white")
		client = Player("black")

	while True:
		try:
			subprocess.run("clear")
			
			playing = host if turn % 2 == 0 else client

			draw_board(board)
			if whoAmI != None:
				if playing.socket == whoAmI:
					pieceCol, pieceRow, moveCol, moveRow = get_player_input(playing, board)
					board = move_selected_pieces(board, pieceCol, pieceRow, moveCol, moveRow)
					await send_move(websocket, [pieceCol, pieceRow, moveCol, moveRow])
				else:
					pieceCol, pieceRow, moveCol, moveRow = await recieve_move(websocket)
					board = move_selected_pieces(board, pieceCol, pieceRow, moveCol, moveRow)
			else:
				pieceCol, pieceRow, moveCol, moveRow = get_player_input(playing, board)
				board = move_selected_pieces(board, pieceCol, pieceRow, moveCol, moveRow)


			turn += 1
			
			input("")

		except ValueError:
			input("Invalid input")
			continue


async def send_message(websocket, message):
	return await websocket.send(message)

async def recieve_message(websocket):
	message = await websocket.recv()
	print(message)
	return message


async def send_move(websocket, moves: List[str]):
	moves_json = json.dumps(moves)  # Serialize moves to JSON
	await websocket.send(moves_json.encode())

async def recieve_move(websocket):
    moves_json = await websocket.recv()  # Receive JSON-encoded moves
    moves = json.loads(moves_json)  # Deserialize moves from JSON
    print(moves)
    return moves


async def start_as_host():
	async with serve(handle_client, "0.0.0.0", 8765):        
		await asyncio.Future()  # run forever


async def start_as_client():
    try:
        host_ip = input("Host IP address: ")
        # Validate the IP address or hostname here if needed
        if not host_ip:
            raise ValueError("Invalid IP address or hostname")
        
        async with websockets.connect(f"ws://{host_ip}:8765") as client_socket:
            message = await receive_message(client_socket)
            if message == "Start game":
                ready_to_start = input("Are you ready to start the game? (yes/no): ")
                await send_message(client_socket, ready_to_start)
            host_conf = await receive_message(client_socket)
            if host_conf == "Starting":
                await runGame(client_socket, "client")

    except Exception as exc:
        print(f"Error connecting as client: {exc}", exc)


async def handle_client(websocket):
	await send_message(websocket, "Start game")
	client_conf = await recieve_message(websocket)
	if client_conf in "yesYesYy":
		await send_message(websocket, "Starting")
		await runGame(websocket, "host")


async def main():
	print("Welcome to the casual terminal chess")

	CHOICE = int(input("""What do you want to do?
		1 - Play localy
		2 - Host a game
		3 - Connect to a friend
		"""))

	match CHOICE:
		case 1:
			await runGame()
		case 2:
			while True:
				await start_as_host()
		case 3:
			while True:
				await start_as_client()


if __name__ == '__main__':
	 asyncio.run(main())