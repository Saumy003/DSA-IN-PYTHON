# Cheak if a string is palindrome or Not #

# Approach 1 => Using While loop

str1 = "anbcddcbna"
end = len(str1) -1
start = 0

while start < end:
    if str1[start] != str1[end]:
        print("Given String is Not a Palindrome")   # return False
    start += 1
    end -= 1

print("Given String is a Palindrome")

# Approach 2 => Using Recursion

str2 = "nitin"
def func(str2, left, right):
    if left >= right:
        return True
    if str2[left] != str2[right]:
        return False
    return func(str2, left +1, right-1)

func(str2, 0, len(str2)-1)
