import numpy as np
from sandbox8 import SudokuBoard
from aim.time import timeit


def print_sudoku(board): return print(SudokuBoard.__str__(board))


easy_board = np.array(
    [[5, 1, 7, 6, 0, 0, 0, 3, 4],
     [2, 8, 9, 0, 0, 4, 0, 0, 0],
     [3, 4, 6, 2, 0, 5, 0, 9, 0],
     [6, 0, 2, 0, 0, 0, 0, 1, 0],
     [0, 3, 8, 0, 0, 6, 0, 4, 7],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 9, 0, 0, 0, 0, 0, 7, 8],
     [7, 0, 3, 4, 0, 0, 5, 6, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
)

medium_board = np.array([
    [0, 0, 0, 1, 8, 4, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 8, 0, 0],
    [0, 8, 0, 7, 0, 3, 0, 6, 0],
    [9, 0, 7, 0, 0, 0, 1, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 4, 0, 0, 0, 5, 0, 8],
    [0, 5, 0, 2, 0, 6, 0, 3, 0],
    [0, 0, 9, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 8, 0, 5, 0, 0, 0]
])

backtracks = 0


def solve(board):
    """Allows initializing backtracks every solve and not every recursion."""
    global backtracks
    backtracks = 0
    return _solve(board)


def _solve(board):
    # Modify board inplace

    global backtracks

    implied_cells = []

    # Make multiple passes until nothing changes
    while True:
        implications_found = find_implications(board)
        if len(implications_found) == 0:
            # No more implications found, continue normal solving
            break
        for cell, value in implications_found:
            if is_valid_cell(board, cell, value):
                # Save implied cells
                row, col = cell
                board[row, col] = value
                implied_cells.append(cell)
            else:
                # Abort this solve
                erase_cells(board, implied_cells)
                return False

    cell_found = find_next_cell(board)
    if not cell_found:
        # Solved!
        print("SOLVED!")
        print_sudoku(board)
        print(f"{backtracks=}")
        return True
    else:
        while board[cell_found] < 9:
            board[cell_found] += 1

            if is_valid_cell(board, cell_found):
                if _solve(board):
                    return True
                else:
                    backtracks += 1

        board[cell_found] = 0
        # erase_cells(board, implied_cells)

        return False


def find_implications(board):
    implications = []
    ALL_NUMBERS = set(range(10))

    for row_num in range(9):
        row = board[row_num]
        if np.count_nonzero(row) == 8:
            value_missing = (ALL_NUMBERS-set(row)).pop()
            col_num = np.where(row == 0)[0][0]
            cell = row_num, col_num
            implications.append((cell, value_missing))

    for col_num in range(9):
        col = board[:, col_num]
        if np.count_nonzero(col) == 8:
            value_missing = (ALL_NUMBERS-set(col)).pop()
            row_num = np.where(col == 0)[0][0]
            cell = row_num, col_num
            implications.append((cell, value_missing))

    return implications


def erase_cells(board, cells):
    for cell in cells:
        board[cell] = 0


def is_valid_cell(board, cell, value=None):
    if value is None:
        # Value is already placed in cell
        value = board[cell]
        max_count = 1
    else:
        max_count = 0

    row, col = cell
    # Row
    if np.count_nonzero(board[row, :] == value) > max_count:
        return False

    # Column
    if np.count_nonzero(board[:, col] == value) > max_count:
        return False

    # Box
    box = board[box_slice(row, col)]
    if np.count_nonzero(box == value) > max_count:
        return False

    return True


def box_slice(row, col):
    box_row = row//3 * 3
    box_col = col//3 * 3
    return slice(box_row, box_row+3), slice(box_col, box_col+3)


def boxes_iterator(board):
    for row in (0, 3, 6):
        for col in (0, 3, 6):
            yield board[box_slice(row, col)]


def find_next_cell(board):
    empty_cells = np.argwhere(board == 0)
    if len(empty_cells) > 0:
        return tuple(empty_cells[0])
    else:
        return None


def is_solved(board):
    return all(is_valid_cell(board, (row, col))
               for row in range(0, 9)
               for col in range(0, 9))


if __name__ == "__main__":
    print_sudoku(easy_board)
    print(f"{is_solved(easy_board)=}\n")
    timeit(solve)(easy_board)
    print(f"{is_solved(easy_board)=}")

    # print("\n\n\n")

    # print_sudoku(medium_board)
    # print(f"{is_solved(medium_board)=}\n")
    # timeit(solve)(medium_board)
    # print(f"{is_solved(medium_board)=}")
