""" Subset Sum -> 1 {GFG} """

nums = [5, 9, 3]
result = []
total = 0

def solve(index, total):

    #base case
    if index >= len(nums):
        result.append(total)
        return

    #backtrack
    sum = total + nums[index]
    solve(index + 1, sum)
    sum = total
    solve(index + 1, sum)

solve(0, 0)
print(result)