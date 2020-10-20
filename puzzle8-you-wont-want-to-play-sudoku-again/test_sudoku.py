from sandbox8 import SudokuBoard, solve_sudoku
from pytest import fixture


@fixture(scope='function')
def sudoku_board():
    return SudokuBoard([
        [-1, -1, -1, 1, 8, 4, -1, -1, -1],
        [-1, -1, 1, -1, -1, -1, 8, -1, -1],
        [-1, 8, -1, 7, -1, 3, -1, 6, -1],
        [9, -1, 7, -1, -1, -1, 1, -1, 6],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [3, -1, 4, -1, -1, -1, 5, -1, 8],
        [-1, 5, -1, 2, -1, 6, -1, 3, -1],
        [-1, -1, 9, -1, -1, -1, 6, -1, -1],
        [-1, -1, -1, 8, -1, 5, -1, -1, -1],
    ])


def test_solve(sudoku_board):
    solved = [
        [5, 9, 6, 1, 8, 4, 2, 7, 3],
        [7, 3, 1, 6, 2, 9, 8, 5, 4],
        [4, 8, 2, 7, 5, 3, 9, 6, 1],
        [9, 2, 7, 5, 3, 8, 1, 4, 6],
        [8, 1, 5, 4, 6, 2, 3, 9, 7],
        [3, 6, 4, 9, 1, 7, 5, 2, 8],
        [1, 5, 8, 2, 4, 6, 7, 3, 9],
        [2, 4, 9, 3, 7, 1, 6, 8, 5],
        [6, 7, 3, 8, 9, 5, 4, 1, 2],
    ]
    assert solve_sudoku(sudoku_board) == solved
