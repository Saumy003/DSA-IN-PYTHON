""" Leetcode:328 -> Segregate odd and even node in linked list """

#brute force
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:

    def segregate(self, head):

        if head is None or head.next is None:
            return head

        values = []

        # Store odd index values
        temp = head

        while temp:
            values.append(temp.val)
            if temp.next is None:
                break
            temp = temp.next.next

        # Store even index values
        temp = head.next

        while temp:
            values.append(temp.val)
            if temp.next is None:
                break
            temp = temp.next.next

        # Rewrite linked list
        temp = head
        index = 0

        while temp:
            temp.val = values[index]
            index += 1
            temp = temp.next

        return head


#optimal solution

class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head