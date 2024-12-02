#PostOrderIs LRN

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def postorderTraversal(root):
    result = []
    if root is None:
        return result

    # Create two stacks
    stk1 = []
    stk2 = []

    # Push root to first stack
    stk1.append(root)

    # Run while first stack is not empty
    while stk1:
      
        # Pop from stk1 and push it to stk2
        curr = stk1.pop()
        stk2.append(curr)

        # Push left and right children of 
        # the popped node
        if curr.left:
            stk1.append(curr.left)
        if curr.right:
            stk1.append(curr.right)

    # Collect all elements from second stack
    while stk2:
        curr = stk2.pop()
        result.append(curr.data)

    return result

        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(postorderTraversal(root))