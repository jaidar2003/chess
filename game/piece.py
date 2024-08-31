
class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None


    def show(self):
        symbols = {
            "ROOK": {"WHITE": "♖", "BLACK": "♜"},
            "PAWN": {"WHITE": "♙", "BLACK": "♟"},
            "KNIGHT": {"WHITE": "♘", "BLACK": "♞"},
            "BISHOP": {"WHITE": "♗", "BLACK": "♝"},
            "QUEEN": {"WHITE": "♕", "BLACK": "♛"},
            "KING": {"WHITE": "♔", "BLACK": "♚"}
        }
        return symbols[self.__type__][self.__color__.upper()]



