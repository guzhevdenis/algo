class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxDepth(root):
     

    if root is None:
        return 0
    
    answer = []
    level_nodes = []
    cur_nodes = []

    level_nodes.append(root)
    
    
    while (level_nodes):

        answer.append([element.val for element in level_nodes])
        cur_nodes = level_nodes
        level_nodes = []

        while (cur_nodes):

            node = cur_nodes[0]
            cur_nodes.pop(0)

            if(node.left):
                level_nodes.append(node.left)
            if(node.right):
                level_nodes.append(node.right) 
        
    return len(answer)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(maxDepth(root))