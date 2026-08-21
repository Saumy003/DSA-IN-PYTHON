""" Topic 3. Introduction to Deque Class """

from collections import deque

dq = deque([])
print(dq)

lst = deque([])

lst.append(100)
lst.append(200)
lst.append(300)
lst.appendleft(1)
lst.appendleft(9)

print(lst)

lst.popleft()
print(lst)