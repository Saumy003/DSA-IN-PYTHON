"""
Leetcode 153 --> Find minimum in rotated sorted array
"""
# Btute sulotion

nums = [4, 5, 6, 7, 0, 1, 2]
mini = float("inf")

for i in range(0, len(nums)):
    if nums[i] < mini:
        mini = nums[i]

print("Minimum element in the given array is:",mini)

# Optimal Solution

nums = [7, 8, 9, 1, 2, 3, 4]
mini = float("inf")

low = 0
high = len(nums) - 1
while low <= high:
    mid = (low + high) // 2

    if nums[mid] <= nums[high]:
        mini = min(mini, nums[mid])
        high = mid - 1

    else:
        mini = min(mini, nums[low])
        low = mid + 1

print("Minimum element in the given array is:",mini)