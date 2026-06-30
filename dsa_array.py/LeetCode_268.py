"""
LC - 268
Find the missing number in the array
"""

# BRUTE FORCE SOLUTION 

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(nums)

for i in range(0, n+1):
    if i in nums:
        continue
    else:
        print("Missing number in the array is:",i)

# BETTER SOLUTION

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(nums)

freq = {}
for i in range(0 , n+1):
    freq[i] = 0            # by default sb ki key staring me 0 hogi

for num in nums:
    freq[num] = 1

for k, v in freq.items():
    if v == 0:
        print("Missing number in the array is:", k)

# OPTIMAL SOLUTION

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

n =len(nums)

sum_of_natutal_numbres = n * (n+1) // 2
print("Missing number in the array is:", sum_of_natutal_numbres - sum(nums))
