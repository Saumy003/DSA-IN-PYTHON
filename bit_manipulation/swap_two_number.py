""" Basic Logic Built-Up Questions
    2. Swapping of two numbers
"""

x = 5
y = 10
def swap(a, b):
    a = a^b
    b = a^b
    a = a^b
    return a , b
swap(x, y)
print("x, y=", swap(x, y))