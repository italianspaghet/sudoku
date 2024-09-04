from pygame import *
from screen import *

#------------------------------------------------------------
# Initializing the game window
#------------------------------------------------------------
pygame.init()
show_window()

#------------------------------------------------------------
# Main loop
#------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    pygame.display.update()