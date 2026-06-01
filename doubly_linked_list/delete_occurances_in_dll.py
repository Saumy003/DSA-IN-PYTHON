""" 6. Delete all occurrences of a key in a doubly linked list """

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delete(self, key):

        # Empty list
        if self.head is None:
            return None

        temp = self.head

        while temp is not None:

            # Save next node before deleting current node
            next_node = temp.next

            if temp.val == key:

                # If node is head, move head forward
                if temp == self.head:
                    self.head = temp.next

                # Update previous node's next pointer
                if temp.prev is not None:
                    temp.prev.next = temp.next

                # Update next node's prev pointer
                if temp.next is not None:
                    temp.next.prev = temp.prev

            temp = next_node

        return self.head