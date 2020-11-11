import numpy as np
from pytest import fixture
from sandbox8np import is_valid_cell, find_next_cell, is_solved


@fixture(scope='function')
def unsolved():
    return np.array([
        [0, 0, 0, 1, 8, 4, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 8, 0, 0],
        [0, 8, 0, 7, 0, 3, 0, 6, 0],
        [9, 0, 7, 0, 0, 0, 1, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 4, 0, 0, 0, 5, 0, 8],
        [0, 5, 0, 2, 0, 6, 0, 3, 0],
        [0, 0, 9, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 8, 0, 5, 0, 0, 0],
    ])


@fixture(scope='function')
def solved():
    return np.array([
        [5, 9, 6, 1, 8, 4, 2, 7, 3],
        [7, 3, 1, 6, 2, 9, 8, 5, 4],
        [4, 8, 2, 7, 5, 3, 9, 6, 1],
        [9, 2, 7, 5, 3, 8, 1, 4, 6],
        [8, 1, 5, 4, 6, 2, 3, 9, 7],
        [3, 6, 4, 9, 1, 7, 5, 2, 8],
        [1, 5, 8, 2, 4, 6, 7, 3, 9],
        [2, 4, 9, 3, 7, 1, 6, 8, 5],
        [6, 7, 3, 8, 9, 5, 4, 1, 2],
    ])


def test_find_next_cell(unsolved):
    assert find_next_cell(unsolved) == (0, 0)
    unsolved[0, 0] = 7
    assert find_next_cell(unsolved) == (0, 1)


def test_find_next_cell_not_found(solved):
    assert find_next_cell(solved) is None


def test_is_solved(solved):
    assert is_solved(solved) is True


def test_is_valid_cell(unsolved):
    cell = (5, 1)
    value = 1
    assert is_valid_cell(unsolved, cell, value) is True


def test_is_not_valid_cell_row(unsolved):
    cell = (2, 4)
    value = 6
    assert is_valid_cell(unsolved, cell, value) is False


def test_is_not_valid_cell_column(unsolved):
    cell = (6, 6)
    value = 8
    assert is_valid_cell(unsolved, cell, value) is False


def test_is_not_valid_cell_box(unsolved):
    cell = (1, 4)
    value = 7
    assert is_valid_cell(unsolved, cell, value) is False


def test_is_valid_cell_value_placed(unsolved):
    cell = (5, 1)
    value = 1
    unsolved[cell] = value
    assert is_valid_cell(unsolved, cell) is True


def test_is_not_valid_cell_row_value_placed(unsolved):
    cell = (2, 4)
    value = 6
    unsolved[cell] = value
    assert is_valid_cell(unsolved, cell) is False


def test_is_not_valid_cell_column_value_placed(unsolved):
    cell = (6, 6)
    value = 8
    unsolved[cell] = value
    assert is_valid_cell(unsolved, cell) is False


def test_is_not_valid_cell_box_value_placed(unsolved):
    cell = (1, 4)
    value = 7
    unsolved[cell] = value
    assert is_valid_cell(unsolved, cell) is False
