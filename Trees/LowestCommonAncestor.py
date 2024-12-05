# Given a binary tree, 
# find the lowest common ancestor (LCA) 
# of two given nodes in the tree.

# According to the definition of LCA on 
# Wikipedia: “The lowest common ancestor is defined between
# two nodes p and q as the lowest node in T that has both
# p and q as descendants (where we allow a node to be a descendant of itself).”

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def lowestCommonAncestor(root, p , q):
    if root is None or root == p or root == q:
            return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    return root.val if left and right else (left.val or right.val)


    

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode (4)

p = root.left
q = root.right

print(lowestCommonAncestor(root, p,q))