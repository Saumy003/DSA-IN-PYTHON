"""
Leetcode 33 --> Search in Roatated sorted array I
"""
# Brute Force 
nums = [11, 12, 23, 1, 4, 5, 6, 8, 9, 10]
target = 8

def search(arr, x):
    for i in range(0, len(nums)):
        if arr[i] == x:
            return i
    return -1   

required_index = search(nums, target)
print("index of given target is:", required_index)

# Optimal solution

nums = [11, 12, 23, 1, 4, 5, 6, 8, 9, 10]
target = 8

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print("Reqiured index is:",mid)

    if nums[mid] <= nums[high]:                  # if the sorted part is at left side of the mid
        if nums[mid] <= target <= nums[high]:
            low =mid +1
        else:
            high = mid - 1

    else:
        if nums[low] <= target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
