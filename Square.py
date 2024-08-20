
class Square:
    def __init__(self, side):
        self.piece = None

    def occupy(self, piece):
        self.piece = piece

    def realese(self):
        self.piece = None

    def occupied(self):
        return self.piece is not None

    def get_piece(self):
        return self.piece

