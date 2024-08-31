import unittest
from game.board import Board
from game.pieces import Rook, King, Pawn

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_setup(self):
        self.assertIsInstance(self.board.grid[0][0].get_piece(), Rook)
        self.assertIsInstance(self.board.grid[0][4].get_piece(), King)
        self.assertIsInstance(self.board.grid[1][0].get_piece(), Pawn)
        self.assertIsNone(self.board.grid[2][0].get_piece())

    def test_move_piece(self):
        self.board.move_piece((1, 0), (2, 0))
        self.assertIsInstance(self.board.grid[2][0].get_piece(), Pawn)
        self.assertIsNone(self.board.grid[1][0].get_piece())

if __name__ == '__main__':
    unittest.main()
