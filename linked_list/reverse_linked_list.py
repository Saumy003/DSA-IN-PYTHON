""" Reverse a Linked List """

#brute force(by changing the values)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        temp = self.head
        stack = []

        """ loop to append to stack"""

        while temp is not None:
            stack.append(temp.val)
            temp = temp.next

        """ loop to pop the value from stack"""

        temp = self.head
        while temp is not None:
            e = stack.pop()
            temp.val = e
            temp = temp.next

        return self.head

        
#optimal solution(change the link)
    def reverse_(self):

        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        
        return self.head