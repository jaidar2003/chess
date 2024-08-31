import unittest
from game.square import Square
from game.pieces import Rook


class TestSquare(unittest.TestCase):

    def test_occupy_and_release(self):
        square = Square()
        rook = Rook("white")

        # Verificar que la casilla está inicialmente vacía
        self.assertFalse(square.occupied())
        self.assertIsNone(square.get_piece())

        # Ocupa la casilla con una pieza
        square.occupy(rook)
        self.assertTrue(square.occupied())
        self.assertEqual(square.get_piece(), rook)

        # Libera la casilla
        square.release()
        self.assertFalse(square.occupied())
        self.assertIsNone(square.get_piece())


if __name__ == '__main__':
    unittest.main()
