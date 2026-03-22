import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

CROWN = pygame.transform.scale(pygame.image.load('checkers/assets/Crown_icon-icons.com_52157.png'), (44, 25))