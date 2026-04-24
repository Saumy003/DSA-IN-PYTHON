"""
Question:- Move zero to the end of the list
"""

# Brute Force 

nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
n = len(nums)
temp = []
for i in range(0, n):
    if nums[i] != 0:
        temp.append(nums[i])

nz = len(temp)
for i in range(0, nz):
    nums[i] = temp[i]
for i in range(nz, n):
    nums[i] = 0

print(nums)

# Optimal Solution(A trick one)

lst = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]

if len(lst)==1:
    print(lst)
if i == len(lst):
    print(lst)

i = 0
while i < len(lst):
    if lst[i]==0:
        break
    i += 1
    j = i + 1
    while j <len(lst):
        if lst[j]!= 0:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        j += 1

print(lst)