class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from collections import deque

def isSymmetric(root):
     
    if not root:
        return True
    queue = deque([root.left, root.right])

    while queue:
        t1 = queue.popleft()
        t2 = queue.popleft()
        if not t1 and not t2:
            continue
        if not t1 or not t2 or t1.val != t2.val:
            return False
        queue.append(t1.left)
        queue.append(t2.right)
        queue.append(t1.right)
        queue.append(t2.left)
    return True
     
     