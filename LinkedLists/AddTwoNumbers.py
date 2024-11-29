# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def addTwoNumbers(l1, l2):
    dummy = ListNode()
    res = dummy

    total = carry = 0

    while l1 or l2 or carry:
        total = carry

        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
            
        num = total % 10
        carry = total // 10
        dummy.next = ListNode(num)
        dummy = dummy.next
        
    return res.next
     



five = ListNode(5)
two = ListNode(2,five)
head = ListNode(1,two)

three_two = ListNode(4)
two_two = ListNode(3, three_two)    
head_two = ListNode(1,two_two)

answer = addTwoNumbers(head, head_two)

print('a')