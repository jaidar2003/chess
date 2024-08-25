import pygame
import sys
from game.Board import Board
from game.Piece import King, Queen, Bishop, Knight, Rook, Pawn


pygame.init()
WIDTH, HEIGHT = 800, 800
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ajedrez")


SQUARE_SIZE = WIDTH // 8


def load_images():
    pieces = ['r', 'n', 'b', 'q', 'k', 'p', 'R', 'N', 'B', 'Q', 'K', 'P']
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE))
    return images


def draw_board(board, images):
    WINDOW.fill(BACKGROUND_COLOR)
    for row in range(8):
        for col in range(8):
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            color = GRID_COLOR if (row + col) % 2 == 0 else (200, 200, 200)
            pygame.draw.rect(WINDOW, color, rect)
            piece = board.grid[row][col].get_piece()
            if piece:
                piece_image = images.get(str(piece))
                if piece_image:
                    WINDOW.blit(piece_image, rect.topleft)
    pygame.display.flip()

def main():
    board = Board()
    images = load_images()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board(board, images)
        clock.tick(30)

if __name__ == "__main__":
    main()
