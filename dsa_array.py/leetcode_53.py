"""
Leetcode-53
Kadane's Algorithm => Maximum subarray sum
"""

# brute force

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

n = len(nums)
maxi = float("-inf")

for i in range(0, n):
    total = 0
    for j in range(i, n):
        total = total + nums[j]
        maxi = max(maxi , total)

print("Maximum subarray sum:",maxi)        # Time Complexity is O(N**2)


# optimal solution (Kadane's Algo)

nums = [5, 4, -1, 7, 8]

sum = 0
maxi = float("-inf")

for i in range(0, len(nums)):
    sum = sum + nums[i]
    maxi = max(sum, maxi)

    if sum <0:
        sum = 0

print("Maximum subarray sum:",maxi)       # Time complexity is O(N)

