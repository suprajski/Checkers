import pygame
from checkers.constants import *
from checkers.game import Game 
from ai.algorithm import *
import sys

algorithm = "alphabeta"
if len(sys.argv) > 1:
    if len(sys.argv) > 1:
        algorithm = sys.argv[1]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')  

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(60)

        if game.turn == WHITE:
            value, new_board = choose_ai_move(game.board, 3, WHITE, game, algorithm)
            game.ai_move(new_board)
            

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update()
               

    pygame.quit()

main()