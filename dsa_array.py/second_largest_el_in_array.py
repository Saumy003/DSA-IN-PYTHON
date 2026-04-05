# Find the second largest element of the array #

# Approach => 1 => Brute Force
nums = [55, 32, 97, -55, 45, 32, 88, 21]

nums.sort()
n = len(nums)
print("Second largest element of the given array is:", nums[n-2])


# Approach => 2 => Better solution

arr = [55, 32, 97, -55, 45, 32, -98, 21]

largest = float("-inf")
second_largest = float("-inf")
n = len(nums)

for i in range(0, n):
    largest = max(largest, arr[i])

for i in range(0, n):
    if arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Second largest element in the given array is :", second_largest)

# Approach => 3 => Optimal solution

lst = [22, 34, 87, 67, -43, 45, -999, 0, 87]

largest = float("-inf")
second_largest = float("-inf")
n = len(lst)

for i in range(0, n):
    if lst[i] > largest:
        second_largest = largest
        largest = lst[i]
    elif lst[i]> second_largest and lst[i] != largest:
        second_largest = lst[i]

print("Second largest element in the given array is :", second_largest)
