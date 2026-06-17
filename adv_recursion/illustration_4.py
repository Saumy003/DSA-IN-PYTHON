""" 4. Count all subsequences with sum = k. """

nums = [1, 1, 2, 3, 4, 5, 9]
target = 9

def solve(index, total):
    
    #base case
    if total == target:
        return 1
    elif total > target:
        return 0
    if index >= len(nums):
        return 0
    
    #take
    sum = total + nums[index]
    pick = solve(index + 1, sum)

    # backtrack
    sum = total

    # not pick
    not_pick = solve(index + 1, sum)
    return pick + not_pick

print(solve(0, 0))