# Print the individual digit from the end:-
num = 5873

while num > 0:
    last_digit = num % 10
    print(last_digit)

    num = num // 10        # float divison i.e. ignore decimal part only consider integer part

# Print individual digit from starting:-

number = "5873"   # why changed to string-> int object is not iterable

for i in number:
    print(i)