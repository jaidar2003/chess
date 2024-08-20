from Square import Square
from Piece import *

ROWS = 8
COLUMNS = 8

class Board:
    def __init__(self):
        self.rows = ROWS
        self.columns = COLUMNS
        self.grid = [[Square() for _ in range(self.columns)] for _ in range(self.rows)]
        self.initialize_pieces()

    def initialize_pieces(self):
        self.grid[7][4].occupy(King("white"))

    def show_board(self):
        for row in range(self.rows):
            for column in range(self.columns):
                piece = self.grid[row][column].get_piece()
                print(piece if piece else '.', end='')
            print()
