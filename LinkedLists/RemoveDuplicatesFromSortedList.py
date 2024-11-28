# Given the head of a sorted linked list, delete all duplicates 
# such that each element appears only once. Return the linked list sorted as well.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def deleteDuplicates(head):
    cur = head
    while(cur):

        if (cur.val == cur.next.val):
            cur.next = cur.next.next
        else:
            cur = cur.next

         
    return head



three = ListNode(1)


two = ListNode(1, three)
head = ListNode(1, two)
new_head = deleteDuplicates(head)
print('f')