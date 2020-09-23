# Programming for the Puzzled -- Srini Devadas
# Keep Those Queens Apart
# Given a 8 x 8 chess board, figure out how to place 8 Queens such that
# no Queen attacks another queen.
# This code uses a single-dimensional list to represent Queen positions


# This procedure checks that the most recently placed queen on the board on column
# current does not conflict with existing queens.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        # We have two diagonals hence need the abs()
        if (current - i == abs(board[current] - board[i])):
            return False
    return True


# This procedure places 8 Queens on a board so they don't conflict.
# It assumes n = 8 and won't work with other n!
def EightQueens(solutions=-1, location=None, n=8):

    board = [-1] * n
    for i in range(n):
        board[0] = i
        for j in range(n):
            board[1] = j
            if not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if not noConflicts(board, 2):
                    continue
                for L in range(n):
                    board[3] = L
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if noConflicts(board, 7):
                                        print(board)
                                        solutions -= 1
                                        if solutions == 0:
                                            return
    return


def eight_queens_constrained(location, n=8):

    if location is None:
        location = [-1] * n

    for column in range(n):
        if location[column] == -1:
            for row in range(n):
                location[column] = row
                # if (column == n-1) and noConflicts(location, column):
                #     print(location)


if __name__ == "__main__":

    # EightQueens()

    eight_queens_constrained([-1, 4, -1, -1, -1, -1, -1, 0])
