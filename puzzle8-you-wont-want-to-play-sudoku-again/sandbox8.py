class SudokuBoard(list):
    def __str__(self):
        HEAVY_UPPER = "┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓"
        HEAVY_MIDDLE = "┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫"
        LIGHT_MIDDLE = "┠───┼───┼───╂───┼───┼───╂───┼───┼───┨"
        HEAVY_BOTTOM = "┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛"
        HEAVY_VERTICAL = "┃"
        LIGHT_VERTICAL = "│"
        SIDE = 9

        string = []

        string.append(HEAVY_UPPER)
        for row in range(SIDE):
            if row in (3, 6):
                string.append(HEAVY_MIDDLE)
            elif row in (1, 2, 4, 5, 7, 8):
                string.append(LIGHT_MIDDLE)

            substring = []

            substring.append(HEAVY_VERTICAL)
            for col, value in enumerate(self[row]):
                if col in (3, 6):
                    substring.append(HEAVY_VERTICAL)
                elif col in (1, 2, 4, 5, 7, 8):
                    substring.append(LIGHT_VERTICAL)
                substring.append(f" {value if value != -1 else ' '} ")
            substring.append(HEAVY_VERTICAL)
            string.append("".join(substring))

        string.append(HEAVY_BOTTOM)

        return "\n".join(string)

        # HORIZONTAL_LINE = "━━━"
        # HORIZONTAL = "───"
        # VERTICAL_LINE = "┃"
        # VERTICAL = "|"
        # POINT = "·"
        # MISSING = "   "

        # for row in range(SIDE):
        #     if (row % 3) == 0:
        #         print((POINT+HORIZONTAL_LINE)*SIDE + POINT)
        #     else:
        #         print((POINT+HORIZONTAL)*SIDE + POINT)

        #     line = []
        #     for col in range(SIDE):
        #         if (col % 3) == 0:
        #             line.append(VERTICAL_LINE)
        #         else:
        #             line.append(VERTICAL)

        #         value = self[row][col]
        #         if value == -1:
        #             line.append(MISSING)
        #         else:
        #             line.append(f" {value} ")

        #     line.append(VERTICAL_LINE)
        #     print("".join(line))

        # print((POINT+HORIZONTAL_LINE)*SIDE + POINT)


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
