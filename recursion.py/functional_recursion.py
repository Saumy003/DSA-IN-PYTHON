# Parameterized and functional recursion ==>

# Ques1. Sum of 1 to n=4 by recursion(parametrized):--
def func(sum , i,n):
    if i >n:
        print(sum)      # sum = 10
        return
    func(sum+i , i+1,n)
#calling function
func(0, 1, 4)

#Ques2. Sum of 1 to n=4 by using functional recursion :--
def sum_recursive(x):
    if x == 1:  # base case
        return 1
    return x + sum_recursive(x-1)
#calling function
result = sum_recursive(10)
print(result)