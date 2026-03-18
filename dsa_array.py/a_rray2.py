# Creating array using python numpy module (Method 2)
from numpy import *
arr = array([1,2,3,4])
for x in arr:
    print(x , end=" ")

# storing hetrogenous array
val = array([1,4.5,"c","a",67])
for x in val:
    print(x , end=" ")

# to create multi-dimension array
zero_dim = array(10)
print(zero_dim)

one_dim = array([4,5,6,7,8])
print(one_dim)

two_dim = array([[1,2,3] ,[4,5,6] , [7,8,9]])
print(two_dim)

# creating array using arange function
val1 = arange(10,20,2)

for x in val1:
    print(x, end=" ")

# creating array using linspace function 
val2 = linspace(10,20,11)
for x in val2:
    print(x, end=" ")

# Create array using full functon
val3 = full(10 , 5)
for x in val3:
    print(x , end=" ")