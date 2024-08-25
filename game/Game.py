from chess.Board import Board
from chess.Piece import Piece
from chess.Square import Square

class ChessGame:
    def __init__(self):
        self.board = Board()
        self.current_player = "white"

    def play(self):
        while not self.is_game_over():
            self.display_board()
            origin, destination = self.get_move
            if self.validate_move(origin, destination):
                self.move_piece(origin, destination)
                self.switch_turn()

    def validate_move(self, origin, destination):
        return True

    def move_piece(self, origin, destination):
        piece = self.board.grid[origin[0]][origin[1]].get_piece()
        self.board.grid[origin[0]][origin[1]].realese()
        self.board.grid[destination[0]][destination[1]].occupy(piece)

    def switch_turn(self):
        self.current_player = "black" if self.current_player == "white" else "white"

    def is_game_over(self):
        return False

    def display_board(self):
        self.board.show_board()

    def get_move(self, origin, destination):
        origin = (int(input("introduce fila de origen: ")), int(input("introduce columna de origen: ")))
        destination = (int(input("introduce fila de destino: ")), int(input("introduce columna de destino: ")))
        return origin, destination