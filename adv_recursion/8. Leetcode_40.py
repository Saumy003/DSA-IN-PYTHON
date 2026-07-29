""" 8. Combination Sum 2 """

nums = [1, 1, 1, 2, 3]
result = []
total = 4
n = len(nums)

def backtrack(index, total, subset):

    #base case
    if total == 0:
        result.append(subset.copy())
        return

    if total <0:
        return

    #backtracking

    for i in range(index, n):
        if i> index and nums[i] == nums[i - 1]:
            continue

        subset.append(nums[i])
        sum = total - nums[i]
        backtrack(i + 1, sum, subset)
        subset.pop()

backtrack(0, 4, [])
print(result)