"""
Leetcode => 128
Largest Consecutive Sequence => Find the length(integer) of the longest consecutive sequence.
"""

# Brute Force

nums = [1, 99, 101, 98, 2, 5, 3, 99, 100, 1, 1]

n = len(nums)
max_count = 0
for i in range(0, n):
    num = nums[i]
    count = 1

    while num +1 in nums:
        count += 1
        num = num +1
    
    max_count = max(max_count, count)

print("Length of largest consecutive sequence is:", max_count)

# Better solution 

nums = [1, 99, 101, 98, 2, 5, 3, 99, 100, 1, 1]

nums.sort()
last_smaller = float("-inf")
count = 0
longest = 0

for i in range(0, len(nums)):
    num = nums[i]
    if num - 1 == last_smaller:
        count += 1
        last_smaller = num
    
    elif num != last_smaller:
        count = 1 
        last_smaller = num

    longest = max(longest, count)

print("Length of largest consecutive sequence is:", longest)

# Optimal Solution

nums = [1, 99, 101, 98, 2, 5, 3, 99, 100, 1, 1]

my_set = set()

for i in range(0 ,len(nums)):
    my_set.add(nums[i])

longest = 0

for num in my_set:
    if num - 1 not in my_set:
        x = num
        count = 1
        while x+1 in my_set:
            count += 1
            x += 1
        longest = max(longest, count)

print("Length of largest consecutive sequence is:", longest)