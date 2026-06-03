"""Basic Logic Built-Up Questions
    6. Toggle the i-th bit.
"""

n = 13
i = 1

def toggle_ith_bit():
    return n ^ (1 << i)

print(toggle_ith_bit())