import numpy as np

from constants import *


class Board:
    grid = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

    def eval(self, player):
        return 0

    def copy(self):
        new_board = Board()
        new_board.grid = np.array(self.grid, copy=True)
        return new_board

    def reinit(self, canvas1):
        self.grid.fill(0)
        for i in range(7):
            for j in range(6):
                canvas1.itemconfig(disks[i][j], fill=disk_color[0])

    def get_possible_moves(self):
        possible_moves = list()
        if self.grid[3][5] == 0:
            possible_moves.append(3)
        for shift_from_center in range(1, 4):
            if self.grid[3 + shift_from_center][5] == 0:
                possible_moves.append(3 + shift_from_center)
            if self.grid[3 - shift_from_center][5] == 0:
                possible_moves.append(3 - shift_from_center)
        return possible_moves

    def add_disk(self, column, player, canvas1=None):
        for j in range(6):
            if self.grid[column][j] == 0:
                break
        self.grid[column][j] = player
        if canvas1 is not None:
            canvas1.itemconfig(disks[column][j], fill=disk_color[player])

    def column_filled(self, column):
        return self.grid[column][5] != 0

    def check_victory(self):
        # Horizontal alignment check
        for line in range(6):
            for horizontal_shift in range(4):
                if self.grid[horizontal_shift][line] == self.grid[horizontal_shift + 1][line] == \
                        self.grid[horizontal_shift + 2][line] == self.grid[horizontal_shift + 3][line] != 0:
                    return True
        # Vertical alignment check
        for column in range(7):
            for vertical_shift in range(3):
                if self.grid[column][vertical_shift] == self.grid[column][vertical_shift + 1] == \
                        self.grid[column][vertical_shift + 2] == self.grid[column][vertical_shift + 3] != 0:
                    return True
        # Diagonal alignment check
        for horizontal_shift in range(4):
            for vertical_shift in range(3):
                if self.grid[horizontal_shift][vertical_shift] == self.grid[horizontal_shift + 1][vertical_shift + 1] == \
                        self.grid[horizontal_shift + 2][vertical_shift + 2] == self.grid[horizontal_shift + 3][
                    vertical_shift + 3] != 0:
                    return True
                elif self.grid[horizontal_shift][5 - vertical_shift] == self.grid[horizontal_shift + 1][
                    4 - vertical_shift] == \
                        self.grid[horizontal_shift + 2][3 - vertical_shift] == self.grid[horizontal_shift + 3][
                    2 - vertical_shift] != 0:
                    return True
        return False
