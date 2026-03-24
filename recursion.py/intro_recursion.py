# Introduction to Recursion #

# Tail Recursion #
count = 0

def func():
    global count  # Tell Python to use the 'count' from outside
    if count == 4:
        return
    print("Saumy Kumar") #print name 4 times
    count += 1
    func()

func() #function call

# Recurtion using Parameter in tail recursion
def func(i , n):
    if i > n:
        return
    print(i)   # 1 2 3 4
    func(i +1, n)
func(1,4)

# Head Recursion #

count = 0
def func():
    global count   # Tell Python to use the 'count' from outside
    if count == 4:
        return
    count += 1
    func()
    print("Anirudh") #print name 4 times

func()   #function call

# Recurtion using Parameter in head recursion
def func(i , n):
    if i > n:
        return
    func(i +1, n)
    print(i)    # 4 3 2 1
func(1,4)