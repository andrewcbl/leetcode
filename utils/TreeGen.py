from TreeNode import TreeNode
from collections import deque

class TreeGen:
    def __init__(self):
        return

    def createBinaryTree(self, treeStr):
        vals = treeStr.split(',')
    
        # Empty Tree
        if len(vals) == 0:
            return None
    
        ptr = 1
        nodeStack = deque()
        root = TreeNode(int(vals[0]))
        nodeStack.append(root)
    
        while ptr < len(vals):
            parent = nodeStack.popleft()
    
            if vals[ptr] != '#':
                parent.left = TreeNode(int(vals[ptr]))
    
            if ptr+1 >= len(vals):
                return root
    
            if vals[ptr+1] != '#':
                parent.right = TreeNode(int(vals[ptr+1]))
    
            if not (parent.left is None):
                nodeStack.append(parent.left) 
    
            if not (parent.right is None):
                nodeStack.append(parent.right) 
    
            ptr += 2
        
        return root
    
