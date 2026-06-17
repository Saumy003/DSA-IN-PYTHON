""" 3. Check if there exists a subsequences with sum = k. """

nums = [1, 1, 2, 3, 4, 5]
target = 9
result = []

def solve(index, total, subset):
    
    #base case
    if total == target:
        result.append(subset.copy())
        return True
    elif total > target:
        return False
    if index >= len(nums):
        return False
    
    #take
    subset.append(nums[index])
    sum = total + nums[index]
    pick = solve(index + 1, sum, subset)
    if pick == True:
        return True

    # backtrack
    subset.pop()
    sum = total

    # not pick
    not_pick = solve(index + 1, sum, subset)
    return not_pick

print(solve(0, 0, []))