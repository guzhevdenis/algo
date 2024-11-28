# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if not head or not head.next:
            return True
    # Find the middle of the list    
    # it will be slow
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse the second half of it 
    # Compare the two halves
 # Reverse the second half of the list
    prev, curr = None, slow
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

        # Compare the two halves
    first, second = head, prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
        
three = ListNode(1)
two = ListNode(2,three)
head = ListNode(1,two)