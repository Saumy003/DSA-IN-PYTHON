"""Basic Logic Built-Up Questions
    4. Set the i-th bit.
"""
#using left shift and OR operator
n = 9
i = 2
def set_ith_bit():
    return (n | (1 << i))

print(set_ith_bit())