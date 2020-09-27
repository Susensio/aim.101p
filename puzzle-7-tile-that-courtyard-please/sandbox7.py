from math import log2

STATUE = object()


class Tile:
    pass


def tile_courtyard(side, missing):
    board = empty_board(side)
    place_tiles(board, missing)
    pretty_print(board)


def empty_board(side):
    """
    >>> empty_board(2)
    [[None, None], [None, None]]
    """
    if not log2(side).is_integer():
        raise ValueError("Side must be a power of 2")
    board = []
    for row in range(side):
        board.append([None] * side)
    return board


def place_tiles(board, missing):
    pass


def pretty_print(board):
    """
    >>> board = empty_board(4)
    >>> board[0][0] = board[0][1] = board[1][0] = 1
    >>> board[1][1] = board[2][1] = board[1][2] = 2
    >>> board[0][2] = board[0][3] = board[1][3] = 3
    >>> board[2][0] = board[3][0] = board[3][1] = 4
    >>> board[2][3] = board[3][3] = board[3][2] = 5
    >>> board[2][2] = STATUE
    >>> pretty_print(board)
    ·⎼⎼⎼·⎼⎼⎼·⎼⎼⎼·⎼⎼⎼·
    |       |       |
    ·   ·⎼⎼⎼·⎼⎼⎼·   ·
    |   |       |   |
    ·⎼⎼⎼·   ·⎼⎼⎼·⎼⎼⎼·
    |   |   | X |   |
    ·   ·⎼⎼⎼·⎼⎼⎼·   ·
    |       |       |
    ·⎼⎼⎼·⎼⎼⎼·⎼⎼⎼·⎼⎼⎼·
    """
    side = len(board)
    HORIZONTAL_SEPARATOR = "⎼⎼⎼"
    HORIZONTAL_JOINT = "   "
    VERTICAL_SEPARATOR = "|"
    VERTICAL_JOINT = " "
    POINT = "·"
    MISSING = " X "
    SQUARE = "   "

    for row in range(side):
        if row == 0:
            print((POINT+HORIZONTAL_SEPARATOR)*side + POINT)
        else:
            line = []
            line.append(POINT)
            for col in range(side):
                if board[row-1][col] == board[row][col]:
                    line.append(HORIZONTAL_JOINT)
                else:
                    line.append(HORIZONTAL_SEPARATOR)
                line.append(POINT)
            print("".join(line))

        line = []
        for col in range(side):
            if col == 0:
                line.append(VERTICAL_SEPARATOR)
            elif board[row][col-1] == board[row][col]:
                line.append(VERTICAL_JOINT)
            else:
                line.append(VERTICAL_SEPARATOR)

            square = board[row][col]
            if square is STATUE:
                line.append(MISSING)
            else:
                line.append(SQUARE)

        line.append(VERTICAL_SEPARATOR)
        print("".join(line))

    print((POINT+HORIZONTAL_SEPARATOR)*side + POINT)


if __name__ == "__main__":
    board = empty_board(4)
    board[0][0] = board[0][1] = board[1][0] = 1
    board[1][1] = board[2][1] = board[1][2] = 2
    board[0][2] = board[0][3] = board[1][3] = 3
    board[2][0] = board[3][0] = board[3][1] = 4
    board[2][3] = board[3][3] = board[3][2] = 5
    board[2][2] = STATUE
    pretty_print(board)
