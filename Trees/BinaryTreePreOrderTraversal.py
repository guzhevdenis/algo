#PreOrder it is NLR
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if root is None:
        return []
    
    answer = []
    stack = []
    stack.append(root)
    cur = root

    while stack:
        node = stack.pop()
        answer.append(node.val)

        # Push right child first so that left child is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return answer

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorderTraversal(root))