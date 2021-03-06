from math import log2
from aim.arrays import Matrix

STATUE = object()


class Tile:
    pass


def tile_courtyard(side, missing):
    board = empty_board(side)
    board = place_all_tiles(board, missing)
    row_missing, col_missing = missing
    board[row_missing][col_missing] = STATUE
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


def place_all_tiles(board, missing):
    """This is where divide and conquer happens.

    Each branching divides the board into 4 quadrants.
    A tile is placed in covering the 3 quadrants that don't have any missing square.
    That way, subproblems are equivalent.
    """
    side = len(board)
    middle = side//2
    if side == 1:   # End condition
        pass
    else:           # Recursion
        missing_quadrant = find_quadrant(board, missing)

        sub_boards = split_into_quadrants(board)
        for q, sub_board in sub_boards.items():

            if q == missing_quadrant:
                row_missing, col_missing = missing
                if q == 1:
                    relative_missing = (row_missing, col_missing-middle)
                elif q == 2:
                    relative_missing = (row_missing, col_missing)
                elif q == 3:
                    relative_missing = (row_missing-middle, col_missing)
                else:  # q == 4
                    relative_missing = (row_missing-middle, col_missing-middle)
            else:
                if q == 1:
                    relative_missing = (middle-1, 0)
                elif q == 2:
                    relative_missing = (middle-1, middle-1)
                elif q == 3:
                    relative_missing = (0, middle-1)
                else:  # q == 4
                    relative_missing = (0, 0)

            sub_boards[q] = place_all_tiles(sub_board, relative_missing)

        board = merge_from_quadrants(sub_boards)

        place_center_tile(board, missing_quadrant)

    return board


def place_center_tile(board, skip_quadrant):
    """
    >>> board = empty_board(2)
    >>> place_center_tile(board, 3)
    >>> pretty_print(board)
    ·⎼⎼⎼·⎼⎼⎼·
    |       |
    ·⎼⎼⎼·   ·
    | N |   |
    ·⎼⎼⎼·⎼⎼⎼·
    """
    quadrants = [1, 2, 3, 4]
    quadrants.remove(skip_quadrant)
    tile = Tile()
    middle = len(board)//2
    for q in quadrants:
        if q == 1:
            board[middle-1][middle] = tile
        elif q == 2:
            board[middle-1][middle-1] = tile
        elif q == 3:
            board[middle][middle-1] = tile
        else:  # q == 4
            board[middle][middle] = tile


def find_quadrant(board, point):
    """Calculate quadrant in which point lies.

    >>> board = empty_board(8)
    >>> find_quadrant(board, (0, 0))
    2
    >>> find_quadrant(board, (0, 7))
    1
    >>> find_quadrant(board, (7, 0))
    3
    >>> find_quadrant(board, (7, 7))
    4
    """
    middle = len(board)//2
    row, column = point
    if row < middle:
        if column < middle:
            return 2
        else:
            return 1
    else:
        if column < middle:
            return 3
        else:
            return 4


def split_into_quadrants(board, quadrant_preference=4):
    """Divide into 4 boards middle side in quadrant order.
    ·⎼⎼⎼·⎼⎼⎼·
    | 2 | 1 |
    ·⎼⎼⎼·⎼⎼⎼·
    | 3 | 4 |
    ·⎼⎼⎼·⎼⎼⎼·

    >>> board = [[5, 6],
    ...          [7, 8]]
    >>> split_into_quadrants(board)
    {1: [[6]], 2: [[5]], 3: [[7]], 4: [[8]]}
    """
    if len(board) == 0 or len(board[0]) == 0:
        return [[]]
        raise ValueError("Empty array cannot be splited")

    middle_row = int(len(board) / 2 +
                     (0.5 if quadrant_preference in (1, 2) else 0)
                     )
    middle_col = int(len(board[0]) / 2 +
                     (0.5 if quadrant_preference in (2, 3) else 0)
                     )
    board = Matrix(board)

    q1 = board[:middle_row, middle_col:]
    q2 = board[:middle_row, :middle_col]
    q3 = board[middle_row:, :middle_col]
    q4 = board[middle_row:, middle_col:]
    return {1: q1, 2: q2, 3: q3, 4: q4}


def merge_from_quadrants(boards):
    """Join 4 boards in quadrant order.
    ·⎼⎼⎼·⎼⎼⎼·
    | 2 | 1 |
    ·⎼⎼⎼·⎼⎼⎼·
    | 3 | 4 |
    ·⎼⎼⎼·⎼⎼⎼·

    >>> merge_from_quadrants({1: [[1]], 2: [[2]], 3: [[3]], 4: [[4]]})
    [[2, 1], [3, 4]]
    """
    return ([row2+row1 for row1, row2 in zip(boards[1], boards[2])] +
            [row3+row4 for row3, row4 in zip(boards[3], boards[4])])


def place_tile(board, points):
    tile = Tile()
    (row1, col1), (row2, col2), (row3, col3) = points
    board[row1][col1] = tile
    board[row2][col2] = tile
    board[row3][col3] = tile


def place_statue(board, point):
    row, col = point
    board[row][col] = STATUE


def pretty_print(board):
    """
    >>> board = empty_board(4)
    >>> place_tile(board, ((0,0), (0,1), (1,0)))
    >>> place_tile(board, ((0,2), (0,3), (1,3)))
    >>> place_tile(board, ((2,0), (3,0), (3,1)))
    >>> place_tile(board, ((2,3), (3,3), (3,2)))
    >>> place_tile(board, ((1,1), (1,2), (2,1)))
    >>> place_statue(board, (2,2))
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
    NONE = " N "

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
            elif square is None:
                line.append(NONE)
            else:
                line.append(SQUARE)

        line.append(VERTICAL_SEPARATOR)
        print("".join(line))

    print((POINT+HORIZONTAL_SEPARATOR)*side + POINT)


TEST_MATRIX = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]


def test_split_into_quadrants_first():
    quadrants = split_into_quadrants(TEST_MATRIX, 1)
    assert quadrants[1] == [[2, 3], [5, 6]]
    assert quadrants[2] == [[1], [4]]
    assert quadrants[3] == [[7]]
    assert quadrants[4] == [[8, 9]]


def test_split_into_quadrants_second():
    quadrants = split_into_quadrants(TEST_MATRIX, 2)
    assert quadrants[1] == [[3], [6]]
    assert quadrants[2] == [[1, 2], [4, 5]]
    assert quadrants[3] == [[7, 8]]
    assert quadrants[4] == [[9]]


def test_split_into_quadrants_third():
    quadrants = split_into_quadrants(TEST_MATRIX, 3)
    assert quadrants[1] == [[3]]
    assert quadrants[2] == [[1, 2]]
    assert quadrants[3] == [[4, 5], [7, 8]]
    assert quadrants[4] == [[6], [9]]


def test_split_into_quadrants_fourth():
    quadrants = split_into_quadrants(TEST_MATRIX, 4)
    assert quadrants[1] == [[2, 3]]
    assert quadrants[2] == [[1]]
    assert quadrants[3] == [[4], [7]]
    assert quadrants[4] == [[5, 6], [8, 9]]


if __name__ == "__main__":
    tile_courtyard(8, (6, 5))
