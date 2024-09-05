from random import sample


class Sudoku:
    def __init__(self) -> None:
        self.base = 3
        self.side = self.base * self.base

        self.rangeBase = range(self.base)
        self.rows = [g * self.base + row for g in self.shuffle(self.rangeBase) for row in self.shuffle(self.rangeBase)]
        self.cols = [g * self.base + col for g in self.shuffle(self.rangeBase) for col in self.shuffle(self.rangeBase)]
        self.nums = self.shuffle(range(1, self.base * self.base + 1))

        self.board = [[self.nums[self.pattern(row, col)] for col in self.cols] for row in self.rows]
        self.squares = self.side * self.side
        self.empties = self.squares * 1 // 2

    def pattern(self, row, col):
        return (self.base * (row % self.base) + row // self.base + col) % self.side

    def shuffle(self, samp):
        return sample(samp, len(samp))

    def generate(self, squares, empties, board, side):
        for p in sample(range(squares), empties):
            board[p // side][p % side] = 0
        return board
