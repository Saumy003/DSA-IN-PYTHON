"""Traversal in Singly Linked List"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("Singly Linked List is Empty")
            
        else:
            curr = self
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next


# object creation
l1 = SinglyLinkedList()


"""append values
ll.append(20)
ll.append(30)
l1.append(40)
"""

#traversal
l1.traversal()           #20 30 40