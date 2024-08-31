import unittest
from game.pieces import Rook, Pawn, Knight, Bishop, Queen, King

class MockBoard:
    def __init__(self, pieces=None):
        self.pieces = pieces if pieces else {}

    def get_piece(self, row, col):
        return self.pieces.get((row, col), "No piece")

class TestChessPieces(unittest.TestCase):
    def test_rook_moves(self):
        board = MockBoard()
        rook = Rook("white")
        self.assertTrue(rook.permited_move(0, 0, 0, 5, board))  # Movimiento horizontal válido
        self.assertTrue(rook.permited_move(0, 0, 5, 0, board))  # Movimiento vertical válido
        self.assertFalse(rook.permited_move(0, 0, 5, 5, board))  # Movimiento diagonal inválido

    def test_pawn_moves(self):
        board = MockBoard()
        white_pawn = Pawn("white")
        black_pawn = Pawn("black")

        self.assertTrue(white_pawn.permited_move(6, 0, 5, 0, board))  # Movimiento simple hacia adelante
        self.assertTrue(white_pawn.permited_move(6, 0, 4, 0, board))  # Movimiento doble desde posición inicial
        self.assertFalse(white_pawn.permited_move(6, 0, 3, 0, board))  # Movimiento inválido (demasiado lejos)
        self.assertTrue(black_pawn.permited_move(1, 0, 3, 0, board))  # Movimiento doble desde posición inicial
        self.assertFalse(black_pawn.permited_move(1, 0, 4, 0, board))  # Movimiento inválido

        # Test de captura
        board = MockBoard({(5, 1): "Piece_black"})
        self.assertTrue(white_pawn.permited_move(6, 0, 5, 1, board))  # Movimiento de captura válido

    def test_knight_moves(self):
        board = MockBoard()
        knight = Knight("white")
        self.assertTrue(knight.permited_move(0, 0, 2, 1, board))  # Movimiento en "L" válido
        self.assertTrue(knight.permited_move(0, 0, 1, 2, board))  # Otro movimiento en "L" válido
        self.assertFalse(knight.permited_move(0, 0, 2, 2, board))  # Movimiento diagonal inválido

    def test_bishop_moves(self):
        board = MockBoard()
        bishop = Bishop("white")
        self.assertTrue(bishop.permited_move(0, 0, 3, 3, board))  # Movimiento diagonal válido
        self.assertFalse(bishop.permited_move(0, 0, 3, 4, board))  # Movimiento no diagonal inválido

    def test_queen_moves(self):
        board = MockBoard()
        queen = Queen("white")
        self.assertTrue(queen.permited_move(0, 0, 0, 5, board))  # Movimiento horizontal válido
        self.assertTrue(queen.permited_move(0, 0, 5, 0, board))  # Movimiento vertical válido
        self.assertTrue(queen.permited_move(0, 0, 3, 3, board))  # Movimiento diagonal válido
        self.assertFalse(queen.permited_move(0, 0, 3, 4, board))  # Movimiento inválido

    def test_king_moves(self):
        board = MockBoard()
        king = King("white")
        self.assertTrue(king.permited_move(0, 0, 1, 1, board))  # Movimiento en una casilla válido
        self.assertFalse(king.permited_move(0, 0, 2, 2, board))  # Movimiento en más de una casilla inválido

if __name__ == "__main__":
    unittest.main()
