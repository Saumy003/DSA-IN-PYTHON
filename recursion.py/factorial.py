# APPLICATION OF FUNCTIONAL RECURSION #

# Ques1. Find factorial of a given number

def fact(n):
    if n == 0 or n== 1:
        return 1
    return n * fact(n-1)
#calling function
result = fact(6)
print(result)