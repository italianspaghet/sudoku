import pygame
from config import *


def show_window():
    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Sudoku")
    screen.fill(backgroundColor)
