from binary_search_matrix import T, T_sq


def row_column_search(matrix, value):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    # Start with the top right element
    top_right = matrix[0][-1]
    if top_right == value:
        # Found!
        row = 0
        column = len(matrix[0])-1
        return row, column
    elif top_right < value:
        # Eliminate first row
        sub_matrix = matrix[1:]
        found = row_column_search(sub_matrix, value)
        if found:
            row, column = found
            return row+1, column
    else:   # top_right > value
        # Eliminate last column
        sub_matrix = [row[:-1] for row in matrix]
        return row_column_search(sub_matrix, value)


def test_row_column_search():
    assert row_column_search(T, 13) == (3, 1)
    assert row_column_search(T_sq, 60) == (4, 5)
