"""
Leetcode: 35  --> Search Insert Position
"""

# Brute Force
nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
target = 17 

for i in range(0, len(nums)):
    if nums[i] == target:
        print("Element found ,index is:",i)
        break

    if nums[i] > target:
        print("Element not found, but element will be at index:", i)
        break


# Optimal solution

arr = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
target = 2

lower_bound = len(arr)       
low = 0
high = len(arr) - 1

while low<=high:

    mid = (low + high) // 2

    if arr[mid] >= target:           
        lower_bound = mid
        high = mid - 1
    
    else:
        low = mid + 1
print("Reqired index is:", lower_bound)