"""
Leetcode 81. Search in Rotated Sorted Array II
"""

# Brute Force
nums = [10, 11, 11, 12, 12, 13, 13, 13, 1, 2, 3, 4]
target = 110

def search(arr, x):
    for i in range(0, len(nums)):
        if arr[i] == x:
            return True
    return False   

required_index = search(nums, target)
print(required_index)


# Optimal solution

nums = [7, 7, 7, 7, 7, 7, 7, 1, 2, 3, 4, 5, 7, 7]
target = 1

low = 0
high = len(nums) - 1

found = False

while low <= high:

    mid = (low + high) // 2

    if nums[mid] == target:
        found = True
        break

    # duplicates case
    if nums[low] == nums[mid] == nums[high]:
        low += 1
        high -= 1
        continue

    # right half sorted
    if nums[mid] <= nums[high]:

        if nums[mid] < target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1

    # left half sorted
    else:

        if nums[low] <= target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

print(found)