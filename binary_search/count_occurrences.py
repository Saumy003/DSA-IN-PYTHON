"""
Question: Count occurrences of a number in a sorted array with duplicates.
"""
# Brute Force -->  formula used=>(last index - first index +1) 

nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
target = 3
first = -1
last = -1

for i in range(0, len(nums)):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i

print("number of occurrance is:", last-first+1)

# Optimal solution -->   formula used => (upper_bound - lower_bound)

nums = [1, 2, 3, 3, 3, 3, 3, 5, 8, 9, 9, 10, 10, 10]
target = 10

# first occurrance is associated with lower bound
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
# last occurrance is associated with upper bound
upper_bound = len(nums)

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] > target:
        upper_bound = mid
        high = mid - 1
    else:
        low = mid +1

print("Number of occurance is :", upper_bound - lower_bound)
