class Piece:
    def __init__(self, color):
        self.color = color

    def valid_move(self, origin, destination, board):
        raise NotImplementedError("DEBERIA IMPLEMENTAR ESTO EN UNA SUBCLASE CREO?   ")


class King(Piece):
    def __init__(self,color):
        super().__init__(color)

    def valid_move(self, origin, destination, board):
        pass


class Queen(Piece):
    def __init__(self,color):
        super().__init__(color)

    def valid_move(self, origin, destination, board):
        pass


class Bishop(Piece):
    def __init__(self,color):
        super().__init__(color)

    def valid_move(self, origin, destination, board):
        pass


class Knight(Piece):
    def __init__(self,color):
        super().__init__(color)

    def valid_move(self, origin, destination, board):
        pass


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_move(self, origin, destination, board):
        pass


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_move(self, origin, destination, board):
        pass



