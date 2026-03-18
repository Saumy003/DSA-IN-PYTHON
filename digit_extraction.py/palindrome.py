# Check if a number is Palindrome or Not

n = 75257
num = n
result = 0

while num > 0:
    ld = num % 10
    result = (result*10) + ld
    num = num // 10

print(result)

if n == result:
    print("Given integer n is a palindrome")
else:
    print("Given integer n is not a palindrome")
