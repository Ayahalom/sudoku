import numpy as np
import stepSuggestion as suggest
from sudoku import Sudoku


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

    b = np.array([[0, 0, 7, 0, 0, 0, 3, 0, 1],
                  [4, 0, 0, 0, 0, 7, 0, 0, 0],
                  [0, 0, 2, 5, 8, 9, 0, 6, 0],
                  [0, 0, 5, 0, 2, 0, 0, 0, 7],
                  [0, 1, 0, 4, 9, 6, 5, 3, 0],
                  [0, 0, 0, 0, 0, 0, 9, 8, 0],
                  [8, 0, 0, 0, 5, 0, 0, 2, 0],
                  [0, 0, 4, 3, 0, 0, 0, 0, 0],
                  [0, 6, 9, 0, 0, 0, 1, 4, 0]])
    s = Sudoku(a)
    s2 = Sudoku(b)
    s2_sol = np.array([[9, 8, 7, 6, 4, 2, 3, 5, 1],
                       [4, 5, 6, 1, 3, 7, 2, 9, 8],
                       [1, 3, 2, 5, 8, 9, 7, 6, 4],
                       [6, 9, 5, 8, 2, 3, 4, 1, 7],
                       [7, 1, 8, 4, 9, 6, 5, 3, 2],
                       [2, 4, 3, 7, 1, 5, 9, 8, 6],
                       [8, 7, 1, 9, 5, 4, 6, 2, 3],
                       [5, 2, 4, 3, 6, 1, 8, 7, 9],
                       [3, 6, 9, 2, 7, 8, 1, 4, 5]])

    suggest.loop_singles(s2, "hidden")
    print(s2.check())


if __name__ == '__main__':
    main()
