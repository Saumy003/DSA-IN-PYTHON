# Factorial recursion #

# Tail Recursion => =>
# without any parameter

count = 0
def func():
    global count
    if count == 4:
        return
    count += 1
    print(count)
    func()

func()

# with two parameter

def fun(i , n):
    if i >n :
        return
    print(i)
    fun(i+1,n)

fun(1,4)

# with one parameter

def func(n):
    if n > 4:
        return
    print(n)
    n += 1
    func(n)

func(1)

# factorial
