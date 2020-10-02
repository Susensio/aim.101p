from sandbox7 import split_into_quadrants

T = [[1, 4, 7, 11, 15],
     [2, 5, 8, 12, 19],
     [3, 6, 9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]]

T_sq = [[1, 4, 7, 11, 15, 35],
        [2, 5, 8, 12, 19, 38],
        [3, 6, 9, 16, 22, 42],
        [10, 13, 14, 17, 24, 55],
        [18, 21, 23, 26, 30, 60],
        [50, 60, 70, 80, 90, 100]]


def binary_search_2d(matrix, value):
    QUADRANT_PREFERENCE = 2

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    elif len(matrix) == 1 and len(matrix[0]) == 1:
        if center(matrix, QUADRANT_PREFERENCE) == value:
            # Value found!
            return (0, 0)
    else:
        quadrants = split_into_quadrants(matrix, QUADRANT_PREFERENCE)

        if center(matrix, QUADRANT_PREFERENCE) == value:
            return middle(matrix, QUADRANT_PREFERENCE)
        elif center(matrix, QUADRANT_PREFERENCE) < value:
            # Remove 2nd quadrant (index 1)
            quadrants.pop(2)
        else:
            # Only keep 2nd quadrant
            quadrants = {2: quadrants[2]}

        for i, quad in quadrants.items():
            found = binary_search_2d(quad, value)
            if found:
                row, col = found
                mid_row, mid_col = middle(matrix, QUADRANT_PREFERENCE)
                if i in (1, 4):
                    col = col + mid_col + 1
                if i in (3, 4):
                    row = row + mid_row + 1

                return row, col


def center(matrix, *args, **kwargs):
    middle_row, middle_col = middle(matrix, *args, **kwargs)
    return matrix[middle_row][middle_col]


def middle(matrix, quadrant_preference=4):
    middle_row = int(len(matrix) / 2 -
                     (0.5 if quadrant_preference in (1, 2) else 0)
                     )
    middle_col = int(len(matrix[0]) / 2 -
                     (0.5 if quadrant_preference in (2, 3) else 0)
                     )
    return middle_row, middle_col


def test_binary_search_2d_first_quad():
    assert binary_search_2d(T, 11) == (0, 3)


def test_binary_search_2d_second_quad():
    assert binary_search_2d(T, 1) == (0, 0)


def test_binary_search_2d_third_quad():
    assert binary_search_2d(T, 21) == (4, 1)


def test_binary_search_2d_fourth_quad():
    assert binary_search_2d(T, 30) == (4, 4)


def test_binary_search_2d_not_found():
    assert binary_search_2d(T, 100) is None


def test_binary_search_2d_square_center():
    assert binary_search_2d(T, 9) == (2, 2)


def test_binary_search_2d_square_first_quad():
    assert binary_search_2d(T_sq, 11) == (0, 3)


def test_binary_search_2d_square_second_quad():
    assert binary_search_2d(T_sq, 1) == (0, 0)


def test_binary_search_2d_square_third_quad():
    assert binary_search_2d(T_sq, 21) == (4, 1)


def test_binary_search_2d_square_fourth_quad():
    assert binary_search_2d(T_sq, 30) == (4, 4)


def test_binary_search_2d_square_not_found():
    assert binary_search_2d(T_sq, 1000) is None


def test_center_first_quad():
    m = [[2, 1], [3, 4]]
    assert center(m, 1) == 1


def test_center_second_quad():
    m = [[2, 1], [3, 4]]
    assert center(m, 2) == 2


def test_center_third_quad():
    m = [[2, 1], [3, 4]]
    assert center(m, 3) == 3


def test_center_fourth_quad():
    m = [[2, 1], [3, 4]]
    assert center(m, 4) == 4


if __name__ == "__main__":
    search = 21
    print(f"{search} is in {binary_search_2d(T, search)}")

    search = 17
    print(f"{search} is in {binary_search_2d(T, search)}")

    search = 1
    print(f"{search} is in {binary_search_2d(T, search)}")

    search = 35
    print(f"{search} is in {binary_search_2d(T, search)}")
