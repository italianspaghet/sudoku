from screen import *
import sys


#------------------------------------------------------------
# Initializing the game window
#------------------------------------------------------------
pygame.init()
show_window()
#------------------------------------------------------------
# Drawing the sudoku grid
#------------------------------------------------------------
draw_lines_sudoku()
show_sudoku()
#------------------------------------------------------------
# Main loop
#------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    pygame.display.update()
