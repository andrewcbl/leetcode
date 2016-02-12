# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printTreeLevelTraversal(self):
        result = []
        nodeStack = []
        if self is None:
            return result

        nodeStack.append(self)

        while len(nodeStack) > 0:
            curNode = nodeStack.pop()
            result.append(curNode.val)
            if curNode.right is not None:
                nodeStack.append(curNode.right)
            if curNode.left is not None:
                nodeStack.append(curNode.left)

        print result
