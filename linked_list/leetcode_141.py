""" Leetcode: 141 Linked List Cycle-1"""

#brute Force
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def cyclic_list(self):
        temp = self.head
        my_set = set()

        while temp is not None:
            if temp in my_set:
                return True
            
            my_set.add(temp)
            temp = temp.next

        return False
    
#optimal solution(Tortoise Hare Approach)

def cyclic_list(self):
        
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        
        return False