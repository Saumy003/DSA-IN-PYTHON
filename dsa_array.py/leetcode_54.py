"""
Leetcode: 54
Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output:  [1,2,3,4,8,12,11,10,9,5,6,7]
"""
matrix = [[1,2,3,7],[4,5,6,2],[7,8,9,5], [6,7,3,5]]

result = []
# Intialize pointers of traversal.
top, left = 0, 0
bottom, right = len(matrix) - 1, len(matrix[0]) - 1

# Traverse the matrix in a sprial order.
while top <= bottom and left <= right:
    # Move left to right across the top row.
    for i in range(left, right+1):
        result.append(matrix[top][i])
    top += 1

    # Move top to bottom along the right column
    for i in range(top, bottom +1):
        result.append(matrix[i][right])
    right -= 1

    # Move right to left across the bottom row (if still valid).
    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    # Move bottom to top along the left the left column(if applicable)
    if left <= right:
        for i in range(bottom, top-1, -1):
            result.append(matrix[i][left])
        left += 1

print("Required sprial order of the given matrix is:", result)
