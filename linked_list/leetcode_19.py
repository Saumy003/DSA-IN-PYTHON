""" Leetcode: 19 -> Remove Nth node from the end of the Linked List """

#brute force
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def remove_node(self):

        length = 0
        n = 2
        temp = self.head

        # Count total nodes
        while temp is not None:
            length += 1
            temp = temp.next

        # Edge case: remove head
        if length == n:
            new_head = self.head.next
            return new_head

        # Find previous node
        position_to_stop = length - n

        temp = self.head
        count = 1

        while count < position_to_stop:
            temp = temp.next
            count += 1

        # Remove node
        temp.next = temp.next.next

        return self.head
    
#optimal solution

   # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast n+1 steps ahead
        for i in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete node
        slow.next = slow.next.next

        return dummy.next