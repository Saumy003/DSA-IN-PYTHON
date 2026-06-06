""" 1. Generate all the subsequences using recursion """

nums = [5, 7, 9]
result = []

def solve(index, subset):

    # base case
    if index >= len(nums):
        result.append(subset.copy())
        return
    
    # take
    subset.append(nums[index])
    solve(index + 1, subset)

    # backtrack
    subset.pop()

    # not take
    solve(index + 1, subset)

solve(0, [])

print(result)


# T.C = O(2^n)
# S.C = O(n)