""" 2. Generate all the subsequences with sum = k using recursion """

nums = [5, 9, 4]
target = 9
result = []

def solve(index, total, subset):
    
    #base case
    if total == target:
        result.append(subset.copy())
        return
    elif total > target:
        return
    if index >= len(nums):
        return
    
    #take
    subset.append(nums[index])
    sum = total + nums[index]
    solve(index + 1, sum, subset)

    # backtrack
    e = subset.pop()
    sum = sum - e

    # not pick
    solve(index + 1, sum, subset)

solve(0, 0, [])

print(result)