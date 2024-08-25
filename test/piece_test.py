import unittest
from game.piece import King, Rook, Pawn

class TestPiece(unittest.TestCase):

    def test_king(self):
        king = King("white")
        self.assertEqual(str(king), 'K')

    def test_rook(self):
        rook = Rook("black")
        self.assertEqual(str(rook), 'r')

    def test_pawn(self):
        pawn = Pawn("white")
        self.assertEqual(str(pawn), 'P')

if __name__ == '__main__':
    unittest.main()
