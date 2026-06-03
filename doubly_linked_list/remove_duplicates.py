""" 8. Remove duplicates from a sorted Doubly Linked List """

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def remove_duplicates(self):
        temp = self.head

        while temp is not None and temp.next is not None:

            # Duplicate found
            if temp.val == temp.next.val:

                duplicate = temp.next

                # Skip duplicate node
                temp.next = duplicate.next

                # Update prev pointer if next node exists
                if duplicate.next is not None:
                    duplicate.next.prev = temp

            else:
                temp = temp.next

        return self.head