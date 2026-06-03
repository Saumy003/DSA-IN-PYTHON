"""Basic Logic Built-Up Questions
    5. Clear the i-th bit.
"""

#using left shift, NOT and AND operator

n = 13
i = 2
def clear_ith_bit():
    return n & (~(1 << i))

print(clear_ith_bit())