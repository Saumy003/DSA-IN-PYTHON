"""
Leetcode: 48  => Rotate Matrix by 90 degrees
"""
# Brute Force

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [3, 8, 5, 6], [7, 9, 4, 1]]

n = len(matrix)     # r = len(matrix)  # c =len(matrix[0])

result = [[0 for _ in range(n)] for _ in range(n)]       # list comprehension

for i in range(0, n):
    for j in range(0, n):
        result[j][(n-1)-i] = matrix[i][j]

print("Hence, the given matrix is rotated by 90 degree",result)

# Optimal solution(without taking any "result" matrix)

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

n = len(matrix)

for i in range(0, n-1):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # transpose of matrix

for i in range(0, n):
    matrix[i].reverse()

print("Hence, the given matrix is rotated by 90 degree",matrix)