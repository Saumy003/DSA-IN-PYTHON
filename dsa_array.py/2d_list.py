"""
Learn about 2D List or matrix
"""

# how to represent in 2d list

nums = [[5, 20, 3], [7, -10, 9], [1, -52, 6]]       # a 3x3 matrix

print(nums)

# how to iterate 2d list or matrix

nums = [[5, 20, 3], [7, 10, 9], [1, 52, 6]]

rows = len(nums)
cols = len(nums[0])

for i in range(0, rows):
    for j in range(0, cols):
        print(nums[i][j])

    print()


# Print upper Tringle of a matrix

nums = [[5, 4, 3], [7, 1, 9], [1, 2, 6]] 

rows = len(nums)
cols = len(nums[0])

for i in range(0, rows):
    for j in range(0, cols):
        if j>=i:
            print(nums[i][j], end=" ")
        else:
            print("*", end=" ")

    print()

# Print digonals of matrix

nums = [[5, 4, 3], [7, 1, 9], [1, 2, 6]]

rows = len(nums)
cols = len(nums[0])

for i in range(0, rows):
    for j in range(0, cols):
        if i == j:
            print(nums[i][j], end=" ")
        else:
            print("*", end=" ")

    print()


# Print second digonals of matrix

nums = [[5, 4, 3], [7, 1, 9], [1, 2, 6]]

rows = len(nums)
cols = len(nums[0])

for i in range(0, rows):
    for j in range(0, cols):
        if i + j == 2:
            print(nums[i][j], end=" ")
        else:
            print("*", end=" ")

    print()

# Transpose of a matrix

nums = [[5, 9, 1], [2, 3, 7]]

rows = len(nums)
cols = len(nums[0])

result = [[0]*rows for _ in range(cols)]         # result = [[0, 0], [0, 0], [0, 0]]

for i in range(0, rows):
    for j in range(0, cols):
        result[j][i] = nums[i][j]

print("Transpose of given matrix is :",result)
