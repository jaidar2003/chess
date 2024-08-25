import unittest
from game.chess import ChessGame
from game.piece import King

class TestChessGame(unittest.TestCase):

    def setUp(self):
        self.game = ChessGame()

    def test_initial_player(self):
        # Verificar que el jugador inicial es "white"
        self.assertEqual(self.game.current_player, "white")

    def test_switch_turn(self):
        # Cambiar de turno y verificar
        self.game.switch_turn()
        self.assertEqual(self.game.current_player, "black")
        self.game.switch_turn()
        self.assertEqual(self.game.current_player, "white")

    def test_move_piece(self):
        # Mover una pieza y verificar el movimiento
        self.game.board.move_piece((1, 0), (2, 0))
        self.assertTrue(self.game.board.grid[2][0].occupied())
        self.assertFalse(self.game.board.grid[1][0].occupied())

    def test_is_game_over(self):
        # Simular un juego no terminado
        self.assertFalse(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()
