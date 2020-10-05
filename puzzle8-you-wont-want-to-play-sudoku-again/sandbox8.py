
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
