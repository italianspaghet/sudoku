from resources.colors import *
import pygame
#==============================================================================
# This is the configuration file for some parameters for the sudoku game.
# These parameters can be set by the player to customize the game or left
# for default values.
#==============================================================================
# Window size values can be set here. If, however, fullScreen is set to True,
# the program will just use the values of the screen resolution.
windowWidth = 500
windowHeight = 500
fullScreen = False

# The color of the background can be set here. The default color is white.
backgroundColor = WHITE

window = pygame.display.set_mode((windowWidth, windowHeight))