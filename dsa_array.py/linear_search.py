# Program and concept of linear search

""" 
Question 1 :- nums = [5, 3, 9, 8, 1, 6, 4, -10, -100] and target = 4
"""

nums = [5, 3, 9, 8, 1, 6, 4, -10, -100]
target = 4
for i in range(0, len(nums)):
    if nums[i] == target:
        print(i)
        break