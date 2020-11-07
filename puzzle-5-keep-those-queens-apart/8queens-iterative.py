# Programming for the Puzzled -- Srini Devadas
# Keep Those Queens Apart
# Given a 8 x 8 chess board, figure out how to place 8 Queens such that
# no Queen attacks another queen.
# This code uses a single-dimensional list to represent Queen positions


# This procedure checks that the most recently placed queen on the board on column
# current does not conflict with existing queens LEFT TO CURRENT.
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
def EightQueens(location=None, solutions=-1, n=8):

    if location is None:
        location = [-1] * n

    board = [-1] * n
    for i in range(n):
        board[0] = i if location[0] == -1 else location[0]
        for j in range(n):
            board[1] = j if location[1] == -1 else location[1]
            if not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k if location[2] == -1 else location[2]
                if not noConflicts(board, 2):
                    continue
                for L in range(n):
                    board[3] = L if location[3] == -1 else location[3]
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m if location[4] == -1 else location[4]
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o if location[5] == -1 else location[5]
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p if location[6] == - \
                                    1 else location[6]
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q if location[7] == - \
                                        1 else location[7]
                                    if noConflicts(board, 7):
                                        print(board)
                                        solutions -= 1
                                        if solutions == 0:
                                            return
                                    if not location[7] == -1:
                                        break
                                if not location[6] == -1:
                                    break
                            if not location[5] == -1:
                                break
                        if not location[4] == -1:
                            break
                    if not location[3] == -1:
                        break
                if not location[2] == -1:
                    break
            if not location[1] == -1:
                break
        if not location[0] == -1:
            break

    return


if __name__ == "__main__":
    EightQueens([-1, 4, -1, -1, -1, -1, -1, 0])
