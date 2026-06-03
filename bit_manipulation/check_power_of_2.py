"""Basic Logic Built-Up Questions
    8. Check if the number is power of 2.
"""

n = 16

def check_power_of_two():
    if n & n-1 == 0:
        print("True, n is power of 2")
    else:
        print("False, n is not a power of 2")

check_power_of_two()