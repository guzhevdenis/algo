# You are given an array of k linked-lists lists,
# each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted 
# linked-list and return it.

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def find_min(lists):
    min = lists[0].val
    min_number = 0
    for i, node in enumerate(lists):
        if node.val <= min:
            min_number = i
    return min_number

def mergeKLists(lists):
    dummy = ListNode()
    cur = dummy
    min_number = 0
    if lists == None:
        return None
    while (lists):
        min_number = find_min(lists)
        cur.next = lists[min_number]
        lists[min_number] = lists[min_number].next

        if(lists[min_number] == None):
            lists.pop(min_number)
        cur = cur.next
        
        
    return dummy.next


five = ListNode(5)
two = ListNode(2,five)
head = ListNode(1,two)

three_two = ListNode(4)
two_two = ListNode(3, three_two)    
head_two = ListNode(1,two_two)


three_three = ListNode(7)
two_three = ListNode(5, three_three)    
head_three = ListNode(2,two_three)


lists = [head, head_two, head_three]
answer = mergeKLists(lists)
print('a')