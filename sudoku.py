import numpy as np
from cell import Cell


class Sudoku:

    def __init__(self, grid):
        """
        Constructor for a Sudoku object.
        grid = nXn numpy array.
        """
        self.grid = grid
        self.markup = self.create_markup()

# FOR LATER USE
    # def __init__(self, grid):
    #     """
    #     Constructor for a Sudoku object.
    #     grid = nXn numpy array.
    #     """
    #     n, _ = grid.shape
    #     for i in range(n):
    #         for j in range(n):
    #             self.Cells[i][j] = Cell(row=i, col=j, value=grid[i][j])
    #     self.update_cell_value()

    def empty_cells_list(self):
        """
        This function recieves a 2d numpy array (currently assuming 9*9 array) of integers from 0 to 9
        This function returns the location of cells containing a 0
        """
        zeros_indx = np.argwhere(self.grid == 0)
        if len(zeros_indx[0]) > 0:
            return zeros_indx
        else:
            return [[-1, -1]]

    def first_empty_cell(self):
        """
        This function recieves a 2d numpy array (currently assuming 9*9 array) of integers from 0 to 9
        This function returns the location of the first cell containing a 0
        """
        return self.empty_cells_list()[0]

    def cell_markup_hat(self, index):
        """
        This function recieves an index of cell.
        This function returns the set of numbers not possible in that cell aka the markup hat
        """
        n, m = index
        row_set = set(self.grid[n, :])
        col_set = set(self.grid[:, m])
        block_set = set(self.grid[(3*(n//3)):(3*(n//3+1)),
                                  (3*(m//3)):(3*(m//3+1))].flatten())
        u = (row_set | col_set | block_set)
        u.discard(0)
        return u

    def cell_markup(self, index):
        # FILL
        # FILL
        markup_hat = self.cell_markup_hat(index)
        possibilities = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        return possibilities-markup_hat

    def create_markup(self):
        """
        This function returns a nXn initialized markup for the use of the constructor
        """
        n = self.get_size()
        return np.array([[self.cell_markup((i, j)) if self.grid[i][j] == 0 else set()
                          for j in range(n)] for i in range(n)])

    def update_cell(self, cell):
        self.update_cell_value(cell)
        self.update_markup_after_change(cell)

    def update_cell_value(self, cell):
        """
        This function updates the sudoku object value based on a passed cell.
        cell: a cell object describing the index of the desired update, and the value of that update 
        """
        self.grid[cell.get_row()][cell.get_col()] = cell.get_value()

    def update_markup_after_change(self, cell):
        """
        This function updates the sudoku object markup based on a passed cell which was changed.
        cell: a cell object describing the index of the desired update, and the value of that update 
        """
        row = cell.get_row()
        col = cell.get_col()
        val = cell.get_value()
        for horizontal, vertical, block in zip(self.markup[row, :], self.markup[:, col], self.markup[(3*(row//3)):(3*(row//3+1)),
                                                                                                     (3*(col//3)):(3*(col//3+1))].flatten()):
            horizontal.discard(val)
            vertical.discard(val)
            block.discard(val)

    def print_grid(self):
        print(self.grid)

    def print_markup(self):
        for row in self.get_markup():
            print(row)

    def get_grid(self):
        return self.grid

    def get_markup(self):
        return self.markup

    def get_size(self):
        return self.grid.shape[0]

    def slice_row(self, row_index):
        """
        This function returns the values and markup of a specified row
        row_index: an integer from 1 to n that specifies the desired row
        """
        return self.grid[row_index, :], self.markup[row_index, :]

    def slice_col(self, col_index):
        """
        This function returns the values and markup of a specified col
        col_index: an integer from 1 to n that specifies the desired col
        """
        return self.grid[:, col_index], self.markup[:, col_index]

    def slice_block(self, block_index):
        """
        This function returns the values and markup of a specified block
        block_number: an integer from 1 to n that specifies the desired block.
        blocks are indexed from left to right, top down.
        """
        first_row = (block_index//3)*3
        first_col = (block_index % 3)*3
        return self.grid[first_row:first_row+3, first_col:first_col+3].flatten(), self.markup[first_row:first_row+3, first_col:first_col+3].flatten()

    def slice_range(self, range_index, range_type):
        return {
            "row": self.slice_row(range_index),
            "col": self.slice_col(range_index),
            "block": self.slice_block(range_index)
        }[range_type]

    def check(self):
        required_vals = np.array(range(1, 10))
        for range_type in ["row", "col", "block"]:
            for i in range(9):
                values, _ = self.slice_range(i, range_type)
                b = np.copy(values)
                b.sort()
                if not np.array_equal(b, required_vals):
                    return False
        return True
