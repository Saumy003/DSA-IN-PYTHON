""" 7. Find Pairs with given sum in doubly linked list """

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #brute force --> [loop algo]
    def sum(self, target):
        temp1 = self.head
        result = []
        while temp1 is not None:
            temp2 = temp1.next
            while temp2 is not None:
                if temp1.val + temp2.val == target:
                    result.append([temp1.val, temp2.val])
                temp2 = temp2.next
            temp1 = temp1.next
        return result
    
    
    #better solution --> [hashing algo]
    def sum_(self, target):
        temp = self.head
        my_set = set()
        result = []
        while temp is not None:
            remaining = target - temp.val
            if remaining in my_set:
                result.append([remaining, temp.val])

            my_set.add(temp.val)
            temp = temp.next
        return result


    #optimal solution --> [two pointers algo]
    def _sum(self, target):
        left = self.head
        right = self.head
        result = []

        while right.next is not None:
            right = right.next
        
        while left is not None and right is not None and left.val < right.val:
            total = left.val + right.val
            if total == target:
                result.append([left.val, right.val])
                left = left.next
                right = right.prev
            
            elif total > target:
                right = right.prev
            
            else:
                left = left.next
        return result