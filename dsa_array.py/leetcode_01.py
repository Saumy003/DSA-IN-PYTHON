"""
Leetcode - 01
Two Sum Problem
"""

# brute force
nums = [5, 9, 1, 2, 4, 15, 6, 3]    # target == 13
n = len(nums)
for i in range(0, n-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == 13:
            print(i,",", j)


# optimal solution

lst = [5, 9, 1, 2, 4, 15, 6, 3]    # target == 13
m = len(lst)

hash_map = {}
for i in range(0, m):
    remaining = 13 - lst[i]        # traget - lst[i]
    if remaining in hash_map:
        print(hash_map[remaining], i)

    hash_map[lst[i]] = i
