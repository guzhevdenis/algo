# Given the root of a binary tree,
# determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with
# keys less than the node's key.
# The right subtree of a node contains
# only nodes with keys greater than the node's key.
# Both the left and right subtrees must 
# also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


#Описание прохода Морриса:
# Ищем самого правого предшественника в левом поддереве текущего узла (изначально корня)
# Устанавливаем временную связь - этого правого предшественника на наш текущий узел 
# После чего переходим в это левое поддерево и продолжаем эту процедуру 

#Trying to use Morris traversal

def isValidBST(root):
    current = root
    prev_value = None

    while current:
        if current.left is None:
            # Проверка текущего узла
            if prev_value is not None and current.val <= prev_value:
                return False
            prev_value = current.val
            current = current.right
        else:
            # Найти предшественника (это и есть самый крайний правый элемент в левом поддереве текущего элемента)
            # Возможны две ситуации, мы либо уже его назначали, либо назначим первый раз 
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            # Установить временную связь
            if predecessor.right is None:
                predecessor.right = current
                current = current.left

            # Если этот предшественник уже был. Удаляем связь и идем направо
            else:
                # Восстановить структуру дерева
                predecessor.right = None
                # Проверка текущего узла
                if prev_value is not None and current.val <= prev_value:
                    return False
                prev_value = current.val
                current = current.right

    return True
    
    
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)

print(isValidBST(root))