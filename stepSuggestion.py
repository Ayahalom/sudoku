import numpy as np
from cell import Cell
from sudoku import Sudoku
from collections import Counter


def suggest_naked_single(sud):
    """
    This program Recieves a sudoku object.
    If a naked single exists in a sudoku, the program returns a cell object.
    Otherwise the program returns None
    """
    empties = sud.empty_cells_list()
    markup = sud.get_markup()
    for i, j in empties:
        if len(markup[i][j]) == 1:  # found a naked single
            (val,) = markup[i][j]
            return Cell(row=i, col=j, value=val)
    return None


def suggest_hidden_single(sud):
    """
    This program Recieves a sudoku object.
    If a hidden single exists in a sudoku, the program returns a cell object.
    Otherwise the program returns None
    """
    n = sud.get_size()
    for range_type in ["row", "col", "block"]:
        for i in range(n):
            values, markup = sud.slice_range(i, range_type)
            number_to_position = create_markup_to_value_dict(
                values, markup)
            for number, positions in number_to_position.items():
                if len(positions) == 1:
                    return Cell(row=i, col=positions[0], value=number)


def loop_singles(sud, singles_type):
    """
    This program recieves a suduko object.
    The program loops finds and updates all the naked/hidden singles in the sud.
    When the sud is out of naked/hidden singles the program prints how many iterations it took
    singles_type: "naked" or "hidden"
    """
    for i in range(len(sud.empty_cells_list())):
        suggestion = {"naked": suggest_naked_single(sud),
                      "hidden": suggest_naked_single(sud)}[singles_type]
        print(f"suggestion is {suggestion} of type {singles_type}")
        if(suggestion is None):
            print(f"breaking in {i} iteration")
            break
        sud.update_cell(suggestion)
    sud.print_grid()


def create_range_values_positions_counter(range_values, range_markup):
    """
    This program recieves a range of values and the markup of the different cells in it(assumed to be a slice of a sudoku object).
    The program returns a counter of the sort {value1:{position1,position2}}
    where value is a number option (1-9) and positions are the possible positions of that value

    range_values = numpy array of integers
    range_markup = numpy array of sets
    """
    value_positions_counts = Counter()
    for markup in range_markup[range_values == 0]:
        value_positions_counts.update(markup)
    return value_positions_counts


def create_markup_to_value_dict(range_values, range_markup):
    """
    """
    n = len(range_markup)
    position_to_options = {pos: range_markup[pos-1]
                           for pos in range(1, n+1) if range_values[pos-1] == 0}
    option_to_positions = {opt: set() for opt in range(1, n+1)}
    for position, options in position_to_options.items():
        for option in options:
            option_to_positions[option].add(position)
    return option_to_positions


def main():
    pass
    # arr = np.array([[1, 0], [0, 1], [0, 0]])


if __name__ == '__main__':
    main()
