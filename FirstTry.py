# THIS PROGRAM WAS DONE ENTIRELY ALONE WITHOUT LOOKING AT ANY VIDEOS OR SOLUTIONS
# This is a program that solves sudokus
# The program does not recieve anything and it was a first try for me to see if I can implement a backtracking solution on my own

import numpy as np


def Solve(grid):
    # The function recieves a numpy array (it assumes the array has a single solution and the grid is of correct size) that reoresents a sudoku grid.
    # The function prints the filled sudoku
    empty_ind = firstEmptyCellIndex(grid)
    if empty_ind[0] == -1:
        print(grid)
        return True
    ints_opts = numbersPossbileInCellList(grid, empty_ind)
    if not ints_opts:
        return False
    for i in ints_opts:
        grid[empty_ind[0], empty_ind[1]] = i  # try an option
        if Solve(grid):
            return True
        else:
            grid[empty_ind[0], empty_ind[1]] = 0


def firstEmptyCellIndex(arr):
    # The function recieves an array and returens the first index containing a '0'
    indexes = np.where(arr == 0)
    if len(indexes[0]) > 0:
        return [indexes[0][0], indexes[1][0]]
    else:
        return [-1, -1]


def numbersNotPossibleInCellSet(arr, index):
    # The function recieves an array (it assumes the array has a single solution and the grid is of correct size) that reoresents a sudoku grid and an index
    # The function returns a number set of all the numbers that can't be put in that index based on sudoku's rules
    n, m = index
    row_set = set(arr[n, :])
    col_set = set(arr[:, m])
    block_set = set(arr[(3*(n//3)):(3*(n//3+1)),
                        (3*(m//3)):(3*(m//3+1))].flatten())
    u = (row_set | col_set | block_set)
    u.discard(0)
    return u


def numbersPossbileInCellList(arr, index):
    # The function recieves an array (it assumes the array has a single solution and the grid is of correct size) that reoresents a sudoku grid and an index
    # The function returns a number list of all the numbers that can be put in that index based on sudoku's rules
    not_allowed = numbersNotPossibleInCellSet(arr, index)
    allowed = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return sorted(allowed-not_allowed)


def main():
    a = np.array([[0, 4, 3, 0, 8, 0, 2, 5, 0],
                  [6, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 9, 4],
                  [9, 0, 0, 0, 0, 4, 0, 7, 0],
                  [0, 0, 0, 6, 0, 8, 0, 0, 0],
                  [0, 1, 0, 2, 0, 0, 0, 0, 3],
                  [8, 2, 0, 5, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 5],
                  [0, 3, 4, 0, 9, 0, 7, 1, 0]])
    print(a)
    print(Solve(a))

    b = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]])

    print(Solve(b))


if __name__ == '__main__':
    main()
