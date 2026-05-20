""" Leetcode: 867 ->  Find the middle of a Linked list """

#brute Force
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    """ Count total number of nodes present"""

    def middle(self):
        n = 0
        temp = self.head
        while temp is not None:
            n += 1
            temp = temp.next
            

        """Apply loop in the half of total nodes"""

        temp = self.head
        for i in range(0, n // 2):
            temp = temp.next
        
        return temp


#Optimal Solution(Tortoise Hare Approach)

        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow