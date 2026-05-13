"""
Upper Bound Implementetion
"""

nums = [1, 1, 1, 2, 3, 3, 5, 6, 7, 7, 7, 9, 12, 12, 13]
target = 9

upper_bound = len(nums)        # keep this by default
low = 0 
high = len(nums) - 1

while low <= high:

    mid = (low + high) // 2

    if nums[mid] > target:     # key concept
        upper_bound = mid
        high = mid - 1
    
    else:
        low = mid + 1

print("Upper bound is: ",upper_bound)