""" Leetcode: 142 Linked List Cycle-2 """

#brute force
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def cyclic_lst(self):
        temp = self.head
        my_set = set()

        while temp is not None:
            if temp in my_set:
                return temp
            
            my_set.add(temp)
            temp = temp.next

        return None
    
#optimal solution
    def cyclic_list(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                slow = self.head

                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow

        return None