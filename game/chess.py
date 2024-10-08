from game.board import Board

class ChessGame:
    def __init__(self):
        self.board = Board()
        self.current_player = "white"


    def play(self, move_sequence=None):
        if move_sequence is None:
            move_sequence = []

        self.display_board()  # Mostrar el tablero solo una vez al comienzo

        while not self.is_game_over():
            origin, destination = self.get_move(move_sequence)
            if self.validate_move(origin, destination):
                self.move_piece(origin, destination)
                self.display_board()  # Mostrar el tablero después de mover una pieza
                self.switch_turn()
            else:
                print("Movimiento inválido. Inténtalo de nuevo.")


    def get_move(self, move_sequence=None):
        if move_sequence:
            return move_sequence.pop(0)
        try:
            origin = (int(input("Introduce fila de origen: ")), int(input("Introduce columna de origen: ")))
            destination = (int(input("Introduce fila de destino: ")), int(input("Introduce columna de destino: ")))
            return origin, destination
        except ValueError:
            print("Entrada inválida. Debes introducir números.")
            return self.get_move(move_sequence)


    def validate_move(self, origin, destination):
        return True


    def move_piece(self, origin, destination):
        piece = self.board.grid[origin[0]][origin[1]].get_piece()
        if piece:
            self.board.grid[origin[0]][origin[1]].release()
            self.board.grid[destination[0]][destination[1]].occupy(piece)


    def switch_turn(self):
        self.current_player = "black" if self.current_player == "white" else "white"


    def is_game_over(self):
        return False


    def display_board(self):
        self.board.show_board()