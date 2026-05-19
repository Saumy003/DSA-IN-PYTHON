""" L -> 867"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None


    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        
        else:
            curr = self.head

            while curr.next is not None:
                curr = curr.next

            curr.next = new_node



    def traversal(self):
        if self.head is None:
            print("Singly Linked List is Empty")
            
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next



l1 = SinglyLinkedList()

l1.append(20)
l1.append(30)
l1.append(40)

l1.traversal()