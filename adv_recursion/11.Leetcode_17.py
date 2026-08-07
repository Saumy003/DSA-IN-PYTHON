""" Letter Combinatons of a Phone Number """

digits = "23"
char_map = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
result = []

def phoneNumber(index, subset):

    #base case
    if index >= len(digits):
        result.append("".join(subset))
        return
    for ch in char_map[digits[index]]:
        subset.append(ch)
        phoneNumber(index+ 1, subset)
        subset.pop()

phoneNumber(0, [])
print(result)