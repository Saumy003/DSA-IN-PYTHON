# BUBBLE SORT #

# Approach 1 => Average / Worst case
nums = [5, 1, 6, 8, 2, 4, 9]
n = len(nums)
for i in range(n-2, -1, -1):
    for j in range(0, i+1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1], nums[j]
print("Sorted list is:" ,nums)


# Approach 2 => Optimized Solution
lst = [1, 2, 3, 4, 5, 9, 10, 14, 12]
l = len(lst)
for i in range(l-2 , -1, -1):
    is_swap = False
    for j in range(0 , i+1):
        if lst[j] > lst[j+1]:
            lst[j] , lst[j+1] = lst[j+1] , lst[j]
            is_swap = True
    if is_swap == False:
        break

print("Sorted list is:" ,lst)
