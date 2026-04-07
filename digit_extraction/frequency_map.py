# Counting Frequency or Frequency map

#Approach 1 =>

nums = [5, 6, 7, 8,6, 7, 1, 3,3,4,2, 2,7, 3, 1]
freq_map = {}    # dictionary
for i in range(0 , len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map[7])

# Approach 2 =>by .get() method

num = [5, 6, 7, 8,6, 7, 1, 3,3,4,2, 2,7, 3, 1, 5]
hash_map = {}
n = len(num)

for i in range(0, n):
    hash_map[num[i]] = hash_map.get(num[i], 0) + 1

print(hash_map[5])
