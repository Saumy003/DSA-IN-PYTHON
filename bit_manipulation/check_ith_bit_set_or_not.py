""" Basic Logic Built-Up Questions
3. Check if the i-th bit is set or not.
"""

#Method 1: using left shift
n = 13
i = 2

def check_ith_bit_set_or_not():
    if (n & (1 << i)) != 0:
        print("True")
    else:
        print("False")

check_ith_bit_set_or_not()


#Method 2: using right shift

n = 13
i = 1

def check_ith_bit_set_or_not_():
    if ((n >> i) & 1) != 0:
        print("True")
    else:
        print("False")

check_ith_bit_set_or_not_()