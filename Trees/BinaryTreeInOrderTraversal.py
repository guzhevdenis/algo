#InOrder it is LNR
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rec_trav(node, list):
    if node is None:
        return 
    rec_trav(node.left, list)
    list.append(node.val)
    rec_trav(node.right,list)


def inorderTraversal(root):
    if root is None:
        return []

    answer = []

    #rec_trav(root, answer)
    stack = []
    stack.append(root)


    while curr is not None or len(stack) > 0:
        
        # Reach the left most Node of the curr Node
        while curr is not None:
            
            # Place pointer to a tree node on
            # the stack before traversing
            # the node's left subtree
            stack.append(curr)
            curr = curr.left

        # Current must be None at this point
        curr = stack.pop()
        answer.append(curr.val)

        # we have visited the node and its
        # left subtree. Now, it's right
        # subtree's turn
        curr = curr.right

    return answer 


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorderTraversal(root))
