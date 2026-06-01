""" 5. To Reverse a Doubly Linked List """

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Brute force --> [Changing the position of the values]
    def reverse(self):
        temp = self.head
        stack = []

        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        
        temp = self.head

        while temp is not None:
            e = stack.pop()
            temp.val = e
            temp = temp.next
        return self.head
        

    #Optimal solution --> [By changing the link]
    def reverse_a_dll(self):
        curr = self.head
        prev = None

        #edge case
        if curr.next is None:
            return self.head
        
        #if there is no edge case
        while curr is not None:
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = front
        
        return prev