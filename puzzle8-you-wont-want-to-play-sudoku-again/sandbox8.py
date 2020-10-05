class SudokuBoard(list):
    def __str__(self):
        SIDE = 9
        HORIZONTAL_LINE = "━━━"
        HORIZONTAL = "───"
        VERTICAL_LINE = "┃"
        VERTICAL = "|"
        POINT = "·"
        MISSING = "   "

        for row in range(SIDE):
            if (row % 3) == 0:
                print((POINT+HORIZONTAL_LINE)*SIDE + POINT)
            else:
                print((POINT+HORIZONTAL)*SIDE + POINT)

            line = []
            for col in range(SIDE):
                if (col % 3) == 0:
                    line.append(VERTICAL_LINE)
                else:
                    line.append(VERTICAL)

                value = self[row][col]
                if value == -1:
                    line.append(MISSING)
                else:
                    line.append(f" {value} ")

            line.append(VERTICAL_LINE)
            print("".join(line))

        print((POINT+HORIZONTAL_LINE)*SIDE + POINT)


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
    print(SudokuBoard(board))
