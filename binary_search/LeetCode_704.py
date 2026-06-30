"""
 Binary Search Algorithm 
 1. Real life example where binary works
 2. Problem Solving
 3. Iterative Solution
 4. Recursive Solution
 5. Time and Space Complexity
 """

# 3. Iterative Solution   --> O(log n) time and O(1) space

lst = [2, 4, 6, 7, 9, 11, 18, 19]
x = 6                                    #x = target = 6

def binary_search(nums, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            low = mid +1

        else:
            high = mid -1

    return -1

result = binary_search(lst, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in list")


# 4. Recursive Solution -> O(log n) time & O(log n) space

arr = [2, 3, 4, 10, 40]
x = 10                                # x = target

def binarySearch(nums, low, high, target):

    if low > high:                  # base case
        return -1
    
    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    
    elif nums[mid] < target:
        return binarySearch(nums, mid +1, high, target)

    else:
        return binarySearch(nums, low, mid - 1, target)

    
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index:", result)
else:
    print("Element is not present in list")

