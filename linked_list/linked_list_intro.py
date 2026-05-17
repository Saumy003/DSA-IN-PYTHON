"""How to create a Node Class"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = Node(5)          # objects --> node1, node2, node3...
node2 = Node(10)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1)           # <__main__.Node object at 0x000001F02F328A50>
print(node1.val)                      # node1 = 5
print(node1.next.val)                 # node2 = 10
print(node1.next.next.next.val)       # node4 = 8


"""Create Singly Linked List Class"""

class SinglyLinkedList:
    def __init__(self):
        self.head = None
