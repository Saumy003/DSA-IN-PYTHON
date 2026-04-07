# Print all factors of a given number.

# Approach 1 => Brute Force

number1 = 20
result1 = []
for i in range (1 , number1+1):
    if number1 % i == 0:
        result1.append(i)
print(result1)

# Approach 2 => Better Solution

number2 = 27
result2 = []

for i in range(1, number2 // 2):
    if number2 % i == 0:
        result2.append(i)
result2.append(number2)
print(result2)

# Approach 3 => Optimal Solution

from math import sqrt

number3 = 36
result3 = []
for i in range(1 , int(sqrt(number3))+1):
    if number3 % i == 0:
        result3.append(i)
        if number3 // i != i :
            result3.append(number3 // i)


result3.sort()
print(result3)

