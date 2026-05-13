"""
Lower Bound Implementation
"""

arr = [2, 3, 7, 10, 11, 11, 25]
target = 9

lower_bound = len(arr)       
low = 0
high = len(arr) - 1

while low<=high:

    mid = (low + high) // 2

    if arr[mid] >= target:            #key concept
        lower_bound = mid
        high = mid - 1
    
    else:
        low = mid + 1
print("Lower Bound:", lower_bound)