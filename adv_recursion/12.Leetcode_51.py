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

n = 4
ans = []
board = ["." * n for _ in range(n)]
leftrow = [0] * n
upperDiagonal = [0] * (2 * n - 1)
lowerDiagonal = [0] * (2 * n - 1)

def solve(col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
    if col == n:
        ans.append(board[:])
        return

    for row in range(n):
        if (
            leftrow[row] == 0
            and lowerDiagonal[row + col] == 0
            and upperDiagonal[n - 1 + col - row] == 0
        ):
            board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
            leftrow[row] = 1
            lowerDiagonal[row + col] = 1
            upperDiagonal[n - 1 + col - row] = 1

            solve(col + 1, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)

            board[row] = board[row][:col] + "." + board[row][col + 1 :]
            leftrow[row] = 0
            lowerDiagonal[row + col] = 0
            upperDiagonal[n - 1 + col - row] = 0

    return ans

solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
print(ans)

# Output => [['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]