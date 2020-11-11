import numpy as np
from sandbox8 import SudokuBoard
from aim.time import timeit
from time import sleep


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
        return False


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
