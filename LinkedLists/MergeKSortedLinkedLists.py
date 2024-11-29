# You are given an array of k linked-lists lists,
# each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted 
# linked-list and return it.

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def find_min(lists):
    if  not lists[0]:
        return None
    min = lists[0].val
    min_number = 0
    for i, node in enumerate(lists):
        if node.val <= min:
            min_number = i
            min = node.val
    return min_number

def mergeKLists(lists):


    filtered_list = [list for list in lists if list]

    if not filtered_list:
        return None
    
    dummy = ListNode()
    cur = dummy
    min_number = 0
    
    if filtered_list == None:
        return None
    
    while (filtered_list):
        min_number = find_min(filtered_list)
        cur.next = filtered_list[min_number]
        filtered_list[min_number] = filtered_list[min_number].next

        if(filtered_list[min_number] == None):
            filtered_list.pop(min_number)
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


lists = [[], [], three_three]
answer = mergeKLists(lists)
print('a')