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
        else:
            assert True
        for cell, value in implications_found:
            if cell not in implied_cells:
                # Do not check double implications
                if is_valid_cell(board, cell, value):
                    # Save implied cells
                    board[cell] = value
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
        erase_cells(board, implied_cells)
        return False


def find_implications(board):
    implications = []
    ALL_NUMBERS = set(range(1, 10))

    for row_num in range(9):
        row = board[row_num]
        values_missing = (ALL_NUMBERS-set(row))
        if len(values_missing) == 1:
            col_num = np.where(row == 0)[0][0]
            cell = row_num, col_num
            implications.append((cell, values_missing.pop()))
        else:
            ...

    for col_num in range(9):
        col = board[:, col_num]
        values_missing = (ALL_NUMBERS-set(col))
        if len(values_missing) == 1:
            row_num = np.where(col == 0)[0][0]
            cell = row_num, col_num
            implications.append((cell, values_missing.pop()))
        else:
            ...

    for (row_offset, col_offset), box in boxes_iterator(board):
        values_missing = (ALL_NUMBERS-set(box.flatten()))
        if len(values_missing) == 1:
            row_num, col_num = [index[0] for index in np.where(box == 0)]
            cell = (row_num+row_offset, col_num+col_offset)
            implications.append((cell, values_missing.pop()))
        else:
            ...

    return implications


def erase_cells(board, cells):
    for cell in cells:
        board[cell] = 0


def is_valid_cell(board, cell, value=None):
    if value is None or value == board[cell]:
        # Value already placed in cell
        value = board[cell]
        max_count = 1
    else:
        max_count = 0

    if value == 0:
        return False

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
            offset = row, col
            yield offset, board[box_slice(row, col)]


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

    print("\n\n\n")

    # print_sudoku(medium_board)
    # print(f"{is_solved(medium_board)=}\n")
    # timeit(solve)(medium_board)
    # print(f"{is_solved(medium_board)=}")

    # almost = np.array([
    #     [5, 9, 6, 1, 8, 4, 2, 7, 3],
    #     [7, 3, 1, 6, 2, 9, 8, 5, 4],
    #     [4, 8, 2, 7, 5, 3, 9, 6, 1],
    #     [9, 2, 7, 5, 3, 8, 1, 4, 6],
    #     [8, 1, 5, 4, 0, 2, 3, 9, 7],
    #     [3, 6, 4, 9, 1, 7, 5, 2, 8],
    #     [1, 5, 8, 2, 4, 6, 7, 3, 9],
    #     [2, 4, 9, 3, 7, 1, 6, 8, 5],
    #     [6, 7, 3, 8, 9, 5, 4, 1, 2],
    # ])
    # print_sudoku(almost)
    # print(f"{is_solved(almost)=}\n")
    # timeit(solve)(almost)
    # print(f"{is_solved(almost)=}")
