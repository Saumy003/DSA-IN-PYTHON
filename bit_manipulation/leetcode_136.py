"""
Leetcode: 136 --> Find the number that appers single time.
"""

#brute force
nums = [1, 2, 2, 1, 4]
hash_map = {}

for num in nums:
    if num in hash_map:
        hash_map[num] += 1
    else:
        hash_map[num] = 1

for key in hash_map:
    if hash_map[key] == 1:
        print("Single Number is:",key)


#optimal solution
arr = [5, 1, 3, 3, 7, 1, 7]

def singleNumber(arr):
    ans = 0

    for num in arr:
        ans = num ^ ans
    return ans
print(singleNumber(arr))