
def solve_sudoku(board):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == -1:
                # Try to place a number
                for number in range(1, 10):
                    new_board, allowed = place_sudoku_cell(
                        board, row, col, number)
                    if allowed:
                        # Branch down
                        attemp = solve_sudoku(new_board)
                        if attemp:
                            return attemp

                # When no number is valid, prune tree and backtrack
                return

    # All cells are filled
    return board


def place_sudoku_cell(board, row, col, number):
    new_board = [row.copy() for row in board]
    new_board[row][col] = number

    horizontal_unique = not (number in board[row])
    vertical_unique = not (number in [row[col] for row in board])

    box_row = row//3
    box_row_start = box_row*3
    box_row_end = (box_row+1)*3
    box_col = col//3
    box_col_start = box_col*3
    box_col_end = (box_col+1)*3
    box = [cell
           for row in board[box_row_start:box_row_end]
           for cell in row[box_col_start:box_col_end]]
    box_unique = not (number in box)

    allowed = horizontal_unique and vertical_unique and box_unique

    return new_board, allowed


def pretty_print_sudoku(board):
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
        for col, value in enumerate(board[row]):
            if col in (3, 6):
                substring.append(HEAVY_VERTICAL)
            elif col in (1, 2, 4, 5, 7, 8):
                substring.append(LIGHT_VERTICAL)
            substring.append(f" {value if value != -1 else ' '} ")
        substring.append(HEAVY_VERTICAL)
        string.append("".join(substring))

    string.append(HEAVY_BOTTOM)

    return "\n".join(string)


if __name__ == "__main__":
    board = [
        [-1, -1, -1, 1, 8, 4, -1, -1, -1],
        [-1, -1, 1, -1, -1, -1, 8, -1, -1],
        [-1, 8, -1, 7, -1, 3, -1, 6, -1],
        [9, -1, 7, -1, -1, -1, 1, -1, 6],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [3, -1, 4, -1, -1, -1, 5, -1, 8],
        [-1, 5, -1, 2, -1, 6, -1, 3, -1],
        [-1, -1, 9, -1, -1, -1, 6, -1, -1],
        [-1, -1, -1, 8, -1, 5, -1, -1, -1]
    ]
    print(pretty_print_sudoku(board))
    print(pretty_print_sudoku(solve_sudoku(board)))
