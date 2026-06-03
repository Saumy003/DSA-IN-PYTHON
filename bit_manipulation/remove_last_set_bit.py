"""Basic Logic Built-Up Questions
    7. Remove last set bit {right most}.
"""

n = 84

def remove_last_set_bit():
    return n & n-1

print(remove_last_set_bit())