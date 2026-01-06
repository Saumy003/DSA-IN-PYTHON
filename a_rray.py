# Creating array using python array module (Method 1)
from array import *
a1 = array('i', [23,56,11])

print(a1)                    # array('i', [23, 56, 11])

for x in a1:
    print(x, end=" , ")                # 23 ,56 ,11

print("/n")

for i in range(3):
    print(a1[i] , end= " ")   # 23 56 11

# #functionality to find typecode of an array
    print(a1.typecode)

#  *ARRAY METHODS* 

#  to reverse the array
a1.reverse()
print(a1)

# to insert element in an array
a1.insert(1,42)                     #here 1 is index position and 42 is the number to be insert
for i in range(0,len(a1)):
    print(a1[i] , end=" ")

# # to overwrite an array index
a1[2] = 33                    #in place of 56, 33 is added
for i in range(0,len(a1)):
    print(a1[i] , end=" ")

# copy array to another variable 
val = array("i" , [1,2,3,4,5,6])

copyArray = array(val.typecode , (x for x in val))

for i in range(0, len(val)):
    print(copyArray[i] , end=" ")

# slicing of an arrray in python
val1 = array("i" , [9,8,7,6,5,4,3,2,1])

abc1 = val1[2:-3]            # ~ val1[2:6]

for i in range(0 , len(abc1)):
    print(abc1[i] , end=" ")

# #reverse array using slicing
val2 = array("i" , [9,8,7,6,5,4,3,2,1])

abc2 = val1[::-1]            # ~ val1[2:6]

for i in range(0 , len(abc2)):
    print(abc2[i] , end=" ")

# create an array by taking input from user
arr = array("i" , [])

n = int(input("Enter the number"))

for i in range(0,n):
    arr.append(int(input("Enter the next element")))
for x in arr:
    print(x, end=" ")

