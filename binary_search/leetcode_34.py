"""
Leetcode: 34 --> Find the first or last occurance of a given number in a sorted array
"""

# Brute Force

nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 10]
target = 3

first = -1
last = -1

for i in range(0, len(nums)):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i

print(f"First occurance index:{first}, last occurance index:{last}")


# Optimal solution

nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 10]
target = 3

#first occurance corresponds to lower bound
lower_bound = -1

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] >= target:
        lower_bound = mid
        high = mid - 1
    else:
        low = mid +1
print("First occurance index is:", lower_bound)

#last Occurance corresponds to upper bound -1
upper_bound = -1

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] > target:
        upper_bound = mid
        high = mid - 1
    else:
        low = mid +1
print("Last occurance index is:", upper_bound -1)

