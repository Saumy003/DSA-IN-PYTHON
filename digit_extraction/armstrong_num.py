# Check for Armstrong number

n = 1634
num = n
number_of_digit = len(str(n))
total = 0

while num > 0:
    ld = num % 10
    total = total + (ld**number_of_digit)
    num = num // 10

print(total)

if n == total:
    print("Given integer n is an armstrong number")
else:
    print("Given integer n is not an armstrong number")