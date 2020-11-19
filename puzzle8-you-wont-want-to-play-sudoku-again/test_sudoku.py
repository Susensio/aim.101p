from sandbox8 import SudokuBoard, solve_sudoku
from pytest import fixture


@fixture(scope='function')
def unsolved():
    return SudokuBoard([
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
    return SudokuBoard([
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


def test_solve(unsolved):
    assert solve_sudoku(unsolved).solved is True
