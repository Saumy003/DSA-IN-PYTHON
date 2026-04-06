# Remove the duplicates from sorted array in place #

# Approach 1 => Brute Force
nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]

n = len(nums)
freq_map = {}

for i in range(0, n):
    freq_map[nums[i]] = 0

j = 0
for key in freq_map:
    nums[j] = key
    j += 1

print("Number of unique element is:", j)        # Output = 7

# Approach 2 => Optimal Solution

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]

n = len(nums)
if n == 1:
    print("Number of unique element is:", n)

i = 0
j = i + 1
while j < n:
    if nums[j] != nums[i]:
        i += 1
        nums[i], nums[j] = nums[j], nums[i]
    j += 1

print("Number of unique element is:", i+1)        # Output = 7