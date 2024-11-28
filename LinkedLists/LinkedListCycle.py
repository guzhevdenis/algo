# Fast and slow pointers initially points to the head\
#Алгоритм Флойда
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
def detect_loop(head):
    slow = head
    fast = head

    # Loop that runs while fast and slow pointer are not
    # None and not equal
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If fast and slow pointer points to the same node,
        # then the cycle is detected
        if slow == fast:
            return True
    return False