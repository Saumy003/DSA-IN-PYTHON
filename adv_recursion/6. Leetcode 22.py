""" 6. Generate all the valid Paranthesis """

n = 3
brackets = [""] * (2 * n)
result = []


def solve(index, total, brackets, result):

    # base case
    if index >= len(brackets):
        if total == 0:
            result.append("".join(brackets))
        return
    
    # edge(invalid) case
    if total > len(brackets) // 2:
        return
    elif total < 0:
        return
    
    # put "("
    brackets[index] = "("
    total_sum = total + 1
    solve(index + 1 , total_sum, brackets, result)

    # put ")"
    brackets[index]= ")"
    total_sum = total - 1
    solve(index + 1, total_sum, brackets, result)

solve(0, 0, brackets, result)
print("Generated Parentheses are:",result)