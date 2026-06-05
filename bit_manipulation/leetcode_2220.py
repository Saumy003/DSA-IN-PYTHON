"""
Leetcode: 2220  --> Minimum Bit Flips to Convert Number
"""

def count_flips():
    start = 3
    goal = 4
    count = 0

    #applying xor operator
    xor = start ^ goal

    #count the number of ones in xor
    for i in range (0, 32):
        if xor & (1 << i) != 0:
            count += 1


    print("Minimum Bit Flips:", count)

count_flips()