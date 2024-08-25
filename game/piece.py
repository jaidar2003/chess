class Piece:
    def __init__(self, color):
        self.color = color

    def valid_move(self, origin, destination, board):
        raise NotImplementedError("Este método debe ser implementado en una subclase.")

    def __str__(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase.")

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return 'K' if self.color == 'white' else 'k'

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return 'Q' if self.color == 'white' else 'q'

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return 'B' if self.color == 'white' else 'b'

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return 'N' if self.color == 'white' else 'n'

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return 'R' if self.color == 'white' else 'r'

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return 'P' if self.color == 'white' else 'p'
