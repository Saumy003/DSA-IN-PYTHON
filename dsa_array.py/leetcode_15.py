"""
Leetcode: 15 => 3Sum problem 
"""

# Brute force ->(using 3 pointers)
lst = [-1, 0, 1, 2, -1, -4]
my_set = set()

n = len(lst)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if lst[i] + lst[j] + lst[k] == 0:
                temp_list = [lst[i], lst[j], lst[k]]
                temp_list.sort()
                my_set.add(tuple(temp_list))

print([list(result) for result in my_set])


# Better Solution
lst = [-1, 0, 1, 2, -1, -4]
n = len(lst)
result = set()
for i in range(0, n):
    my_set = set()
    for j in range(i+1, n):
        third = -(lst[i] + lst[j])
        if third in my_set:
            temp = [lst[i], lst[j], third]
            temp.sort()
            result.add(tuple(temp))

        my_set.add(lst[j])

print([list(answer) for answer in result])

# Optimal Solution(two pointer -> i is fix and j and k is moving from oppo sides)
nums = [-1, 0, 1, 2, -1, -4]
n = len(nums)
ans = []
nums.sort()         # T.C-> O(nlogn)
for i in range(n):
    if i != 0 and nums[i] == nums[i - 1]:
        continue

    # moving two pointers
    j = i +1
    k = n -1
    while j < k:
        total_sum = nums[i] + nums[j] + nums[k]
        if total_sum < 0:
            j += 1
        elif total_sum > 0:
            k -= 1
        else:
            temp = [nums[i], nums[j], nums[k]]
            ans.append(temp)
            j += 1
            k -= 1

            # skip the duplicates if occurred
            while j < k and nums[j] == nums[j - 1]:
                j += 1
            while j < k and nums[k] == nums[k + 1]:
                k -= 1

print(ans)
