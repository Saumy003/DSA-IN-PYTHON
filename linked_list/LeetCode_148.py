""" Sort Linked List """

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head):

    # Base case
    if not head or not head.next:
        return head

    # Find middle of linked list
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves
    mid = slow.next
    slow.next = None

    # Recursively sort both halves
    left = sortList(head)
    right = sortList(mid)

    # Merge two sorted linked lists
    dummy = ListNode()
    tail = dummy

    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next

        tail = tail.next

    # Attach remaining nodes
    tail.next = left if left else right

    return dummy.next


# Function to print linked list
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# Creating linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

# Sort the linked list
head = sortList(head)

# Print sorted list
printList(head)