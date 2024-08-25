from game.square import Square
from game.piece import *

ROWS = 8
COLUMNS = 8

class Board:
    def __init__(self):
        self.rows = ROWS
        self.columns = COLUMNS
        self.grid = [[Square() for _ in range(self.columns)] for _ in range(self.rows)]
        self.initialize_pieces()

    def initialize_pieces(self):
        self.grid[0][0].occupy(Rook("black"))
        self.grid[0][1].occupy(Knight("black"))
        self.grid[0][2].occupy(Bishop("black"))
        self.grid[0][3].occupy(Queen("black"))
        self.grid[0][4].occupy(King("black"))
        self.grid[0][5].occupy(Bishop("black"))
        self.grid[0][6].occupy(Knight("black"))
        self.grid[0][7].occupy(Rook("black"))
        for i in range(COLUMNS):
            self.grid[1][i].occupy(Pawn("black"))

        self.grid[7][0].occupy(Rook("white"))
        self.grid[7][1].occupy(Knight("white"))
        self.grid[7][2].occupy(Bishop("white"))
        self.grid[7][3].occupy(Queen("white"))
        self.grid[7][4].occupy(King("white"))
        self.grid[7][5].occupy(Bishop("white"))
        self.grid[7][6].occupy(Knight("white"))
        self.grid[7][7].occupy(Rook("white"))
        for i in range(COLUMNS):
            self.grid[6][i].occupy(Pawn("white"))

    def show_board(self):
        for row in range(self.rows):
            for column in range(self.columns):
                piece = self.grid[row][column].get_piece()
                print(piece if piece else '.', end=' ')
            print()
