# Hashing in python

# Number hashing =>

# Approach - 1 => Brute Force

p = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
q = [10, 111, 1, 9, 5, 67, 2]

for i in q:
    count = 0
    for x in p:                           # T.C = O(n * m)
        if x == i:
            count += 1
    print(count , end=" ")

# Approach - 2 => Optimal solution

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

hash_list = [0] * 11
for num in n:
    hash_list[num] += 1
                                        
for num in m:
    if num<1 or num>10:                     # T.C = O(n + m)
        print(0)
    else:
        print(hash_list[num])

# Approach 3 => Using Dictionaries Instead


# Character hashing =>

s = "azyxyyzaaaa"
r = ["d", "a", "y", "x"]

freq_list = [0] * 26

for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    freq_list[index] += 1

for ch in r:
    ascii_value = ord(ch)
    index = ascii_value - 97
    print(freq_list[index])
