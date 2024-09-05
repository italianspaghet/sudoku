import pygame
from resources.colors import *
#==============================================================================
# This is the configuration file for some parameters for the sudoku game.
# These parameters can be set by the player to customize the game or left
# for default values.
#==============================================================================
# Window size values can be set here. If, however, fullScreen is set to True,
# the program will just use the values of the screen resolution.
# ⚠️ CURRENTLY NOT WORKING, SCALING IS MISSING ⚠️
windowWidth = 500
windowHeight = 500
fullScreen = False
#==============================================================================
# Here you can choose the color of the background, the lines and the numbers.
# The default values are white for the background, black for the lines and
# the numbers.
backgroundColor = WHITE
lineColor = BLACK
numberColor = BLACK
#==============================================================================
# Here you can set the difficulty of the game which will determine how many
# numbers are shown at the beginning of the game. The default ist set to
# 'easy'. You can also put 'medium', 'hard', 'expert' or 'impossible'.
# ⚠️ CURRENTLY NOT WORKING, DIFFICULTY NOT YET IMPLEMENTED ⚠️
difficulty = 'easy'
#==============================================================================
# Here you can choose the type of sudoku you want to play. The default is the
# classic '9x9' sudoku. You can also choose '4x4' or '16x16'. There is also a
# 'star' mode and an extra 'crazy' mode.
# ⚠️ CURRENTLY NOT WORKING, SUDOKU TYPES NOT YET IMPLEMENTED ⚠️
sudokuType = '9x9'
crazyMode = False

# Setting the window variable
window = pygame.display.set_mode((windowWidth, windowHeight))