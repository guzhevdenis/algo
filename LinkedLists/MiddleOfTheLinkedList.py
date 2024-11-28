# Given the head of a singly linked list, 
# return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
def size_of_linked_list(head):
    size = 1
    cur = head
    while(cur.next):
         cur = cur.next
         size += 1
    return size

def middleNode(head):
    size = size_of_linked_list(head)
    middle = (size + 1) // 2 + (size + 1) % 2
    n = 1 
    cur = head
    while (n != middle):
        cur = cur.next
        n += 1
    return cur

last = ListNode(5)
four = ListNode(4,last)
three = ListNode(3,four)
two = ListNode(2,three)
head = ListNode(1,two)

middle_node = middleNode(head)
print(middle_node.val)



