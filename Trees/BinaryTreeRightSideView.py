# Given the root of a binary tree,
# imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def rightSideView(root):
    if root is None:
        return []
    
    result = []
    cur_nodes = []
    level_nodes = []

    level_nodes.append(root)
    

    while (level_nodes):

        cur_nodes = level_nodes
        result.append(level_nodes[-1].val)
        level_nodes = []

        while (cur_nodes):

            node = cur_nodes[0]
            cur_nodes.pop(0)

            if(node.left):
                level_nodes.append(node.left)
            if(node.right):
                level_nodes.append(node.right) 



    return result 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(rightSideView(root))