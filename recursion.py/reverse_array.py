# Reverse an array using recursion #
nums = [5, 7, 3, 2, 6, 1, 5, 9]

def func(nums , left, right):
    if left >= right:
        return
    nums[left],nums[right] = nums[right], nums[left]
    func(nums, left +1,right-1)

func(nums , 0 ,7)
print(nums)

# Other approaches to "reverse an array" =>

# Approach 1 => using reverse()
arr1 = [1,2,3,4,5]

arr1.reverse()
print("Reversed Array:" , arr1)


# Approach 2 => Using slicing =>
arr2 = [9, 8, 7, 6, 5, 4]

reversed_arr2=arr2[::-1]
print("Reversed array:" , reversed_arr2)

# Approach 3 => using while loop
arr3 = [6, 7, 8, 9, 1, 2]

