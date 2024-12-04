# Given the roots of two binary trees p 
# and q, write a function to check if they are 
# the same or not.

# Two binary trees are considered the same 
# if they are structurally identical, and the nodes 
# have the same value.

# Definition for a binary tree node.
from collections import deque
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isSameTree(p, q):
    if p is None and q is None:
        return True


    queue = deque([p,q])

    while queue:
        t1 = queue.popleft()
        t2 = queue.popleft()
        if not t1 and not t2:
            continue
        if not t1 or not t2 or t1.val != t2.val:
            return False
        queue.append(t1.left)
        queue.append(t2.left)
        queue.append(t1.right)
        queue.append(t2.right)
    return True


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

qoot = TreeNode(5)
qoot.left = TreeNode(8)
qoot.right = TreeNode(4)

print(isSameTree(root, qoot))