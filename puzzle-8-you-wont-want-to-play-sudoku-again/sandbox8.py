from aim.time import timeit
from aim.arrays import Matrix


def solve_sudoku(board, current_row=0, current_col=0):
    # Find an empty cell
    for row in range(current_row, 9):
        for col in range(current_col if row == current_row else 0, 9):
            if board[row][col] == 0:
                # Try to place a number
                for number in range(1, 10):
                    allowed = is_allowed_sudoku_cell(board, row, col, number)
                    if allowed:
                        # Continue exploring this branch, i.e. move down the tree
                        board[row][col] = number
                        # cells_implied = make_implications(board)
                        attemp = solve_sudoku(board, row, col)
                        if attemp:
                            return attemp
                        else:
                            # Revert change and continue with next number
                            board[row][col] = 0
                            # for (row_implied, col_implied) in cells_implied:
                            #     board[row_implied][col_implied] = 0
                            board.backtracks += 1
                # When no number is valid, prune tree and backtrack
                return

    # All cells are traversed
    return board


def make_implications(board):
    cells_implied = []
    all_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # Only one empty slot in row/column/box
    for row_num, row in enumerate(board.rows):
        if 0 in row:
            missing = all_numbers - set(row)
            if len(missing) == 1:
                col_num = row.index(0)
                missing_value = missing.pop()
                if is_allowed_sudoku_cell(board, row_num, col_num, missing_value):
                    board[row_num][col_num] = missing_value
                    cells_implied.append((row_num, col_num))

    for col_num, col in enumerate(board.columns):
        if 0 in col:
            missing = all_numbers - set(col)
            if len(missing) == 1 and 0 in col:
                row_num = col.index(0)
                missing_value = missing.pop()
                if is_allowed_sudoku_cell(board, row_num, col_num, missing_value):
                    board[row_num][col_num] = missing_value
                    cells_implied.append((row_num, col_num))

    return cells_implied


def is_allowed_sudoku_cell(board, row, col, number):
    horizontal_unique = not (number in board.row(row))
    if not horizontal_unique:
        return False

    vertical_unique = not (number in board.col(col))
    if not vertical_unique:
        return False

    box_unique = not (number in board.box(row, col))
    if not box_unique:
        return False

    return True


class SudokuBoard(Matrix):
    __slots__ = ['backtracks']
    VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self, *args, **kwargs):
        self.backtracks = 0
        return super().__init__(*args, **kwargs)

    def _boxes_generator(self):
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                yield [cell
                       for row in self[box_row:box_row+3]
                       for cell in row[box_col:box_col+3]]

    def box(self, row, col):
        """
        0   1   2
        3   4   5
        6   7   8
        """
        box_num = row//3*3 + col//3
        return self.boxes[box_num]

    @property
    def boxes(self):
        return list(self._boxes_generator())

    @property
    def solved(self):
        for row in self.rows:
            if set(row) != self.VALUES:
                return False
        for col in self.columns:
            if set(col) != self.VALUES:
                return False
        for box in self.boxes:
            if set(box) != self.VALUES:
                return False
        return True

    def __str__(self):
        HEAVY_UPPER = "┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓"
        HEAVY_MIDDLE = "┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫"
        LIGHT_MIDDLE = "┠───┼───┼───╂───┼───┼───╂───┼───┼───┨"
        HEAVY_BOTTOM = "┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛"
        HEAVY_VERTICAL = "┃"
        LIGHT_VERTICAL = "│"
        SIDE = 9

        string = []

        string.append(HEAVY_UPPER)
        for row in range(SIDE):
            if row in (3, 6):
                string.append(HEAVY_MIDDLE)
            elif row in (1, 2, 4, 5, 7, 8):
                string.append(LIGHT_MIDDLE)

            substring = []

            substring.append(HEAVY_VERTICAL)
            for col, value in enumerate(self[row]):
                if col in (3, 6):
                    substring.append(HEAVY_VERTICAL)
                elif col in (1, 2, 4, 5, 7, 8):
                    substring.append(LIGHT_VERTICAL)
                substring.append(f" {value if value != 0 else ' '} ")
            substring.append(HEAVY_VERTICAL)
            string.append("".join(substring))

        string.append(HEAVY_BOTTOM)

        return "\n".join(string)


if __name__ == "__main__":
    board = SudokuBoard([
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
    print(board)

    timeit(solve_sudoku)(board)
    print(board)
    print(board.solved)
    print(board.backtracks)
