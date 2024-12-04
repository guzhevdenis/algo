# Given the root of a binary tree and 
# an integer targetSum, return true if the tree 
# has a root-to-leaf path such that adding up all 
# the values along the path equals targetSum.

# A leaf is a node with no children.
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def hasPathSum(root, targetSum):
        
    if root is None:
        return []
    node_map = {}
    level_nodes = []
    cur_nodes = []
    level_nodes.append(root)
    cur_nodes = []
    node_map[root] = root.val

    while(level_nodes): 

        cur_nodes = level_nodes
        level_nodes = []

        while (cur_nodes):

            node = cur_nodes[0]
            cur_nodes.pop(0)

            if(node.left):
                level_nodes.append(node.left)
                node_map[node.left] = node.left.val + node_map[node]
            if(node.right):
                level_nodes.append(node.right)
                node_map[node.right] = node.right.val + node_map[node]
            if(node.left is None and node.right is None):
                if(node_map[node] == targetSum):
                    return True
        
    
     
    return False
    
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)


print(hasPathSum(root, 22))
