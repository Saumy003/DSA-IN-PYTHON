# Rotate array by k place #

# Approach 1 => Brute Force
nums = [3, 9, 5, 6, 7, 2]
n = len(nums)
k = 3                        # number of rotations 
for _ in range(0, k):
    e = nums.pop()
    nums.insert(0, e)

# handling is k is grater than array length(n)
nums = [3, 9, 5, 6, 7, 2]
n = len(nums)
k= 22                        # k is the number of rotation (more than n)
rotations = k % n

for _ in range(0, rotations):
    e = nums.pop()
    nums.insert(0, e)

# Approach 2 => Better Solution(by slicing)

nums = [3, 9, 5, 6, 7, 2, 10, 9]

n = len(nums)
k = 5

nums[:] = nums[n-k:] + nums[ :n-k]

# Approach 3 => Optimal Solution(by reverse of array)
arr = [3, 9, 5, 6, 7, 2, 10, 9]
n = len(arr)
k = 5

start = 0
end = len(arr) - 1

def reverse(arr, atart, end):
    while start < end:
        arr[start], arr[end] = arr[end] , arr[start]
        start += 1
        end -=1

reverse(n-k, n-1)   # reverse last 'k' element
reverse(0, n-k-1)   # reverse remaining element
reverse(0, n-1)     # reverse whole array
