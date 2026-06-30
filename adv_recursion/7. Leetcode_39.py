""" 7. Combination Sum: 1 """

nums = [2,3,6,7]
result = []
target = 7

def combinationSum(index, total, subset):

    # base case
    if total == target:
        result.append(subset.copy())
        return

    elif total > target:
        return

    if index >= len(nums):
        return

    # pick
    Sum = total + nums[index]
    subset.append(nums[index])
    combinationSum(index, Sum, subset)

    # backtrack
    subset.pop()

    # not pick
    combinationSum(index + 1, total, subset)


combinationSum(0,0,[])
print(result)