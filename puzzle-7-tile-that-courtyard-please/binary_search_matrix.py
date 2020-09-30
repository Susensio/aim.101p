from sandbox7 import split_into_quadrants
from pprint import pprint

T = [[1, 4, 7, 11, 15],
     [2, 5, 8, 12, 19],
     [3, 6, 9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]]

T_sq = [[1, 4, 7, 11, 15, 18],
        [2, 5, 8, 12, 19, 21],
        [3, 6, 9, 16, 22, 23],
        [10, 13, 14, 17, 24, 26],
        [18, 21, 23, 26, 30, 35],
        [50, 60, 70, 80, 90, 100]]


def binary_search_2d(matrix, value):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    elif len(matrix) == 1 and len(matrix[0]) == 1:
        if center(matrix) == value:
            # Value found!
            return (0, 0)
    else:
        quadrants = split_into_quadrants(matrix)

        if center(matrix) == value:
            return middle(matrix)
        elif center(matrix) < value:
            # Remove 2nd quadrant (index 1)
            quadrants.pop(1)
        else:
            # Only keep 2nd quadrant
            quadrants = [quadrants[1]]

        for q in quadrants:
            found = binary_search_2d(q, value)
            if found:
                row, col = found
                # BUG
                # Aqui no estoy sumando bien...
                return row+len(q), col+len(q[0])


def center(matrix):
    middle_row, middle_col = middle(matrix)
    return matrix[middle_row][middle_col]


def middle(matrix):
    middle_row = len(matrix) // 2
    middle_col = len(matrix[0]) // 2
    return middle_row, middle_col


if __name__ == "__main__":
    print(binary_search_2d(T, 21))
