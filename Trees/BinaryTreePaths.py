# Given the root of a binary tree, 
# return all root-to-leaf paths in any order.

# A leaf is a node with no children.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def binaryTreePaths(root):
    if root is None:
        return None
    
    node_map = {}
    level_nodes = []
    cur_nodes = []
    level_nodes.append(root)
    cur_nodes = []
    node_map[root] = str(root.val)

    result = []

    while(level_nodes): 

        cur_nodes = level_nodes
        level_nodes = []

        while (cur_nodes):

            node = cur_nodes[0]
            cur_nodes.pop(0)

            if(node.left):
                level_nodes.append(node.left)
                node_map[node.left] = node_map[node] + "->" + str(node.left.val) 
            if(node.right):
                level_nodes.append(node.right)
                node_map[node.right] = node_map[node] +"->" + str(node.right.val) 

            if(node.left is None and node.right is None):
                result.append(node_map[node])
    
     
    return result
     
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(binaryTreePaths(root))