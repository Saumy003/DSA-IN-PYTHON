# Count the number of digits in ab integer.#


# Method 1 (Loop-Based approach)
n = 51
num = n
count = 0

while num >0:
    count += 1
    num = num // 10          # float divison i.e. ignore decimal part only consider integer part #

print(count)

# Method 2 (Logarithm approach)

from math import *

def count_digit(num):
    return int(log10(num)+1)

num_of_digit = count_digit(177715)
print(num_of_digit)