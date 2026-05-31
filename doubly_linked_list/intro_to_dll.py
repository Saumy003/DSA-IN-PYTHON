""" 1. Intro to Doubly Linked List """


# Creating New Node

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

n1 = Node(10)
n2 = Node(20)

n1.next = n2
n2.prev = n1

print(n1)                #<__main__.Node object at 0x0000028429706F90>  
print(n2.prev)           #<__main__.Node object at 0x0000028429706F90>


# Linking all the node
class DoublyLinkedList:
    def __init__(self):
        self.head = None