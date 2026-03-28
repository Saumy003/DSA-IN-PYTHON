# Find the fibonacci number #
# Using recursion =>

def func(n):
    if n == 0 or n == 1:
        return n
    return func(n-1) + func(n-2)
    
fibonacci_number = func(int(input("Enter a number:")))
print("Fibonacci Number is:" , fibonacci_number)
