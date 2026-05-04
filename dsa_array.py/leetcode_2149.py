"""
Leetcode => 2149
Rearrange array elements by sign/symbols and return a new list.
"""

# Brute Force
nums = [5, 10, -3, -1, -10, 6]

positive = []
negative = []

for k in range(0, len(nums)):
    if nums[k] > 0:
        positive.append(nums[k])
    else:
        negative.append(nums[k])

for i in range(0, len(positive)):          # len(positive) = len(negative) --> always
    nums[2*i] = positive[i]
    nums[(2*i)+1] = negative[i]

print("My rearranged list is:", nums)


# Optimal Solution

nums = [5, 10, -3, -1, -10, 6]
n = len(nums)
result = [0] * n
pos_index = 0
neg_index = 1

for i in range(0, n):
    if nums[i]>= 0:
        result[pos_index] = nums[i]
        pos_index += 2

    else:
        result[neg_index] = nums[i]
        neg_index += 2

print("My rearranged list is :", result)