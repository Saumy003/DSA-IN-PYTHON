""" 5. Generate all binary strings without consecutive one's """


def solve(index, flag, numbers, result):
    
    # base case
    if index >= len(numbers):
        result.append("".join(numbers))
        return
    
    # always place 0
    numbers[index] = "0"
    solve(index + 1, True, numbers, result)

    # place 1 only if previous character is not "1"
    if flag == True:
        numbers[index] = "1"
        solve(index + 1, False, numbers, result)
        numbers[index] = "0"



def generateBinaryStrings(n):
    numbers = ["0"]*n
    result = []
    solve(0, True, numbers, result)
    return result


n = 3
print(generateBinaryStrings(n))