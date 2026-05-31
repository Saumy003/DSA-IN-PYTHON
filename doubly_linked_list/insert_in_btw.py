""" 4. Insert In Between the DLL """

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert in Between the nodes
    def insert_in_between(self, val, position):
        new_node = Node(val)

        if position == 0:
            self.insert_at_head(val)
            return
        
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            print("Position out of Bounds")
            return
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node