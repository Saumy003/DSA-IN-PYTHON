""" 3. Append [add at last] """

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Head
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        
        else:
            current = self.head
            while current.next:
                current = current.next
                
            current.next = new_node
            new_node.prev = current