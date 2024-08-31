import unittest
from game.piece import *

class TestPiece(unittest.TestCase):
    def test_rook_white(self):
        piece = Piece("white")
        piece._Piece__type__ = "ROOK"
        self.assertEqual(piece.show(), "♖")


    def test_rook_black(self):
        piece = Piece("black")
        piece._Piece__type__ = "ROOK"
        self.assertEqual(piece.show(), "♜")


    def test_queen_white(self):
        piece = Piece("white")
        piece._Piece__type__ = "QUEEN"
        self.assertEqual(piece.show(), "♕")


    def test_queen_black(self):
        piece = Piece("black")
        piece._Piece__type__ = "QUEEN"
        self.assertEqual(piece.show(), "♛")

if __name__ == "__main__":
    unittest.main()
