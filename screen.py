import pygame


def show_window():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Sudoku")
    screen.fill((255, 255, 255))
