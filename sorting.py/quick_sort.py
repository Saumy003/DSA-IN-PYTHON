# QUICK SORT #
nums = [4, 1, 7, 6, 3, 2, 8]
n =len(nums)

# Code for Quick sort recursion part =>
def quick_sort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index +1, high)

# Code to place pivot at it correct position =>
def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i< j:
        while nums[i] <= pivot and i<= high - 1:
            i += 1
        while nums[j]> pivot and j>= low+1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[low], nums[j] = nums[j], nums[low]
    return j   # return the index of pivot

# Function call
quick_sort(nums, 0, n-1)
print("Sorted Array is:",nums)