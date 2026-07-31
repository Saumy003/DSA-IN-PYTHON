""" Combination Sum 3 """

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
n = 9
k = 3

def solve(last, total, subset):

    #base case
    if total == n and len(subset) == k:
        result.append(subset.copy())
        return

    if total > n or len(subset) > k:
        return
    
    #backtrack
    for i in range(last, 10):
        sum = total + i
        subset.append(i)
        solve(i+ 1, sum, subset)
        subset.pop()

solve(1, 0, [])
print(result)