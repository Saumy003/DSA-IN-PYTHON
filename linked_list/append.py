""" 1. Append in Singly Linked List """

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


# object creation
ll = SinglyLinkedList()

# append values
ll.append(20)
ll.append(30)

print(ll.head.val)          # 20
print(ll.head.next.val)     # 30