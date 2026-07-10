""" Fibbonaci Series Up to limit """

nums = int(input("Enter the limit:"))
a = 0
b = 1

while a <= nums:
    print(a, end=" ")
    c = a + b
    a = b
    b = c


""" Fibonacci Series of first n number """

nums = int(input("Enter the number of terms:"))
a = 0
b = 1

for i in range(nums):
    print(a, end=" ")
    c = a + b
    a = b
    b = c