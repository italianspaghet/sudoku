from config import *
from sudoku.classes.sudoku import Sudoku


def show_window():
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    screen.fill(backgroundColor)


def draw_lines_sudoku():
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(window, lineColor, (25 + 50 * i, 25), (25 + 50 * i, 475), 4)
            pygame.draw.line(window, lineColor, (25, 25 + 50 * i), (475, 25 + 50 * i), 4)
        else:
            pygame.draw.line(window, lineColor, (25 + 50 * i, 25), (25 + 50 * i, 475), 2)
            pygame.draw.line(window, lineColor, (25, 25 + 50 * i), (475, 25 + 50 * i), 2)


def show_sudoku():
    sudoku = Sudoku()
    for i in range(9):
        for j in range(9):
            if sudoku.board[i][j] != 0:
                font = pygame.font.Font('resources/Minecraft.ttf', 30)
                text = font.render(str(sudoku.board[i][j]), True, numberColor)
                window.blit(text, (45 + 50 * j, 40 + 50 * i))
    for row in sudoku.board:
        print(' '.join(str(num) if num != 0 else '.' for num in row))
    pass
