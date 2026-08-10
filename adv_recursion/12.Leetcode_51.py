""" N-Queens """

# Brute Force

n = 4
board = ["." * n for _ in range(n)]
ans = []


def solve(col, board, ans, n):
    if col == n:
        ans.append(list(board))
        return

    for row in range(n):
        if isSafe(row, col, board, n):
            board[row] = board[row][:col] + "Q" + board[row][col + 1:]

            solve(col + 1, board, ans, n)

            board[row] = board[row][:col] + "." + board[row][col + 1:]


def isSafe(row, col, board, n):
    duprow = row
    dupcol = col

    # Check left
    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1

    # Check upper-left diagonal
    row = duprow
    col = dupcol

    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    # Check lower-left diagonal
    row = duprow
    col = dupcol

    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False
        row += 1
        col -= 1

    return True


solve(0, board, ans, n)

print(ans)

# Optimal Solution

