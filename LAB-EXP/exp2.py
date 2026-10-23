def solve(board, row):
    if row == 8:
        for r in board:
            print(" ".join("Q" if x == 1 else "." for x in r))
        return True

    for col in range(8):
        safe = True

        for i in range(row):
            if board[i][col] == 1:
                safe = False

            if abs(board[i].index(1) - col) == abs(i - row):
                safe = False

        if safe:
            board[row][col] = 1

            if solve(board, row + 1):
                return True

            board[row][col] = 0

    return False


board = [[0 for i in range(8)] for j in range(8)]
solve(board, 0)
