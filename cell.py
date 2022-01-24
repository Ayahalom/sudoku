import numpy as np


class Cell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.block = 1+3*(row/3) + col/3
        self.value = value
        self.markup = {}

    def __str__(self):
        if self.value == 0:
            return f"the cell located in row {self.row} and col {self.col} can contain {self.markup}"
        return f"the cell located in row {self.row} and col {self.col} contains {self.value}"

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_block(self):
        return self.block

    def get_value(self):
        return self.value

    def get_markup(self):
        return self.markup

    def set_value(self, value):
        self.value = value

    def set_markup(self, markup):
        self.markup = markup
