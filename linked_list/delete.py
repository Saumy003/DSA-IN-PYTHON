"""4. Delete any Position of Singly Linked List"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def delete(self, val):
        current = self.head
        if current.next is not None:
            if current.val == val:
                self.head = current.next
                return
            
            else:
                found = False
                prev = None
                while current is not None:
                    if current.val == val:
                        found = True
                        break
                    prev = current
                    temp = current.next

                if found:
                    prev.next = current.next
                    return
                else:
                    print("Node not Found")


# object creation
l1 = SinglyLinkedList()

# delete any specific position
l1.delete(100)
