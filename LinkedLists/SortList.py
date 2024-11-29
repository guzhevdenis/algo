# Given the head of a linked list, return
# the list after sorting it in ascending order.
#MERGESORT
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def sortList(head):
    if not head or not head.next:
        return head

    mid = getMid(head)
    left = sortList(head)
    right = sortList(mid)

    return merge(left, right)

def getMid(head) :
    slow, fast = head, head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    return slow

def merge(left, right):
    dummy = ListNode(0)
    tail = dummy
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right
    return dummy.next
