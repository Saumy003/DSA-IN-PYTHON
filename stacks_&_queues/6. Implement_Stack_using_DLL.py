""" Topic 6. Implement Stack using DLL """

class Node:
    # Constructor to initialize a new node
    def __init__(self, data):
        self.data = data
        self.next = None    # next is the link to the next node

class MyStack:
    def __init__(self):
        # Stack top pointer (None means stack is empty)
        self.top = None

    # Push operation: insert data at the top of the stack
    def push(self, data):
        new_node = Node(data)      # create a new node
        new_node.next = self.top   # next of new node points to old top
        self.top = new_node        # move top to new node

    # Pop operation: remove and return data from top of stack
    def pop(self):
        if self.top is None:
            return -1              # stack is empty
        popped = self.top.data     # get top data
        self.top = self.top.next   # move top to next node
        return popped