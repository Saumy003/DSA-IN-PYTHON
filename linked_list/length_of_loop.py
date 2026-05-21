""" Find the Length of loop in Linked List """

#brute force

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def length_of_loop(self):
        temp = self.head
        my_dict = {}
        travel = 0

        while temp is not None:
            if temp in my_dict:
                return travel - my_dict[temp]

            my_dict[temp] = travel
            travel += 1
            temp = temp.next

        return 0                               #no loop involved
    
#optimal solution

    def length_of_loop_ll(self):  
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                slow = slow.next
                count = 1

                while slow is not fast:
                    slow = slow.next
                    count += 1
                return count
        
        return 0