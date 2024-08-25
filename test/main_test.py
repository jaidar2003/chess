import unittest
from game.main import ChessGame

class TestMain(unittest.TestCase):

    def test_game_initialization(self):
        # Verificar que el juego se inicializa correctamente
        try:
            game = ChessGame()
            game.display_board()  # Mostrar el tablero al inicio
        except Exception as e:
            self.fail(f"Inicialización del juego falló con la excepción: {e}")

    def test_play_game(self):
        # Simular un turno de juego para asegurarse de que el flujo básico funciona
        try:
            game = ChessGame()
            game.play()  # Esto es difícil de probar completamente porque depende de la entrada del usuario
        except Exception as e:
            self.fail(f"Ejecutar el juego falló con la excepción: {e}")

if __name__ == '__main__':
    unittest.main()
