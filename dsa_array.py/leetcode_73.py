"""
Leetcode => 73 => Set matrix to zero
"""

# Brute Force

matrix = [[7, 9, 2, 3], [20, 8, 0, 10], [29, 0, -10, 5], [4, 14, 6, 7]]

r = len(matrix)
c = len(matrix[0])

def mark_infinity(matrix, row, cols):
    for i in range(0, r):
        if matrix[i][cols] != 0:
            matrix[i][cols] = float("inf")

    for j in range(0, c):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")


def set_zero(matrix):
    global r
    global c

    for i in range(0, r):
        for j in range(0, c):
            if matrix[i][j] == 0:
                mark_infinity(matrix, i, j)

    for i in range(0, r):
        for j in range(0, c):
            if matrix[i][j] == float("inf"):
                matrix[i][j]=0

set_zero(matrix)
print("Required matrix is :", matrix)


# Optimal Approach
matrix = [[7, 9, 2, 3], [20, 8, 0, 10], [29, 0, -10, 5], [4, 14, 6, 7]]

r = len(matrix)
c = len(matrix[0])
row_track = [0 for _ in range(r)]
col_track = [0 for _ in range(c)]
for i in range(0, r):
    for j in range(0, c):
        if matrix[i][j] == 0:
            row_track[i] = -1
            col_track[j] = -1

for i in range(0, r):
    for j in range(0, c):
        if row_track[i] == -1 or col_track[j] == -1:
            matrix[i][j] = 0

print("Matrix is set to zero:", matrix)