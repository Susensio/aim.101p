def find_queens_apart(size=8):
    """Backtracking algorithm with recursive function."""

    def place_queen(queens_placed):
        column = len(queens_placed)

        if column == size:
            return queens_placed

        for row in range(size):
            queen = (column, row)
            if not in_range(queen, queens_placed):
                attemp = place_queen(queens_placed + [queen])
                if attemp is None:
                    continue  # next row
                else:
                    return attemp

            if row == size:
                return None

    result = place_queen([]) or []
    print(result)
    return result


def print_board(queens, size=8):
    horizontal = list(" ---"*size)
    vertical = list("|   "*size + "|")
    board = []
    for row in range(size):
        board.append(horizontal)
        board.append(vertical.copy())
    board.append(horizontal)

    for queen in queens:
        col, row = queen
        if col >= size or row >= size:
            raise ValueError('Queen out of board')
        board[row*2+1][col*4+2] = "Q"

    print('\n'.join(''.join(row) for row in board))


def in_range(queen, queens_placed):
    """
    1. No two queens can be on the same column.
    2. No two queens can be on the same row.
    3. No two queens can be on the same diagonal.

    >>> in_range((0,0), [(0,1)])
    True
    >>> in_range((0,0), [(2,1), (4,2)])
    False
    >>> in_range((0,0), [(1,1)])
    True
    >>> in_range((1,1), [(0,2)])
    True
    """

    queen_col, queen_row = queen
    for placed_col, placed_row in queens_placed:
        if placed_col == queen_col:
            return True
        if placed_row == queen_row:
            return True
        if placed_col-placed_row == queen_col-queen_row:
            return True
        if placed_col+placed_row == queen_col+queen_row:
            return True
    return False


if __name__ == "__main__":
    size = 4
    print_board(find_queens_apart(size), size)
