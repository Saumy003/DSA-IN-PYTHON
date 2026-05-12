"""
Leetcode: 18 => 4Sum Problem
"""
# Brute Force  --> O(N4)

nums = [1, 0, -1, 0, -1, 2, 5, 9]
n = len(nums)
my_set = set()

if n< 4:                                   # base case
    print("Empty List",[])                
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if nums[i] + nums[j] + nums[k] + nums[l] == 0:
                    temp = [nums[i], nums[j], nums[k], nums[l]]         # list add kro do quadruplets ko
                    temp.sort()                                         # sort the list
                    my_set.add(tuple(temp))                             # convet list into tuple

result = []
for ans in my_set:
    result.append(list(ans))
print("quadruplets are:", result)

# Better Sulution  --> O(N3)

nums = [1, 0, -1, 0, -1, 2, 5, 9]
n = len(nums)
my_set = set()

if n< 4:                                   # edge case
    print("Empty List",[])   

for i in range(0, n):
    for j in range(i+1, n):
        hash_set = set()
        for k in range(j+1, n):
            fourth = 0 - (nums[i] + nums[j] + nums[k])
            if fourth in hash_set:
                temp = [nums[i], nums[j], nums[k], fourth]
                temp.sort()
                my_set.add(tuple(temp))
            hash_set.add(nums[k])

result = []
for ans in my_set:
    result.append(list(ans))
print("quadruplets are:", result)

# Optimal Solution --> O(N2)

nums = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5]
target = 8
n = len(nums)
answer = []

nums.sort()
for i in range(0, n):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    for j in range(i+1, n):
        if j > i + 1 and nums[j] == nums[j-1]:
            continue
        k = j+1
        l = n-1
        while k < l:
            total = nums[i] + nums[j] + nums[k] + nums[l]
            if total == target:
                answer.append([nums[i], nums[j], nums[k], nums[l]])
                k += 1
                l-= 1
                while k < l and nums[k] == nums[k-1]:
                    k += 1
                while l > k and nums[l] == nums[l-1]:
                    l -= 1
            elif total < target:
                k += 1
            else:
                l -= 1

print("quadruplets are:", answer)
