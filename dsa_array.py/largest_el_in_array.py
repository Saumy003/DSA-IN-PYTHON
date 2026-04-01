# Find the largest element in the array. #

# method => 1
nums = [55, 32, -97, 99, 3, 67]

largest = nums[0]
n = len(nums)
for i in range (0, n):
    largest = max(largest, nums[i])
print("Largest element in the given array is:", largest)


# method => 2
arr = [55, 32, -97, 99, 333, 103]

largest = float("-inf")     # initially suppose -> largest = -infinity 
n = len(arr)
for i in range(0 , n):
    if arr[i]> largest:
        largest = arr[i]
print("Largest element in the given array is:", largest)