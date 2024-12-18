# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    node = None

    while head:
        temp = head.next
        head.next = node
        node = head
        head = temp        
    return node
