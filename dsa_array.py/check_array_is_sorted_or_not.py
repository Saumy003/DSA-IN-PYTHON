""" Check is given array is sorted or not =>
if sorted return True
if nt sorted return False
"""

nums = [3, 5, 6, 8, 9, 10, 20]
n = len(nums)

is_sorted = True
for i in range(0, n-1):
    if nums[i] > nums[i+1]:
        is_sorted = False

print(is_sorted)