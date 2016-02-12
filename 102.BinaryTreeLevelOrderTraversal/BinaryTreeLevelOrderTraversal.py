import sys
sys.path.append('/home/bilongc/projects/leetcode/utils')
from TreeNode import TreeNode
from TreeGen import TreeGen

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        result = []

        if root is None:
            return result

        row = []
        curRowNodes = deque()
        nxtRowNodes = deque()
        curRowNodes.append(root)

        while len(curRowNodes) > 0:
            curNode = curRowNodes.popleft()
            row.append(curNode.val)

            if curNode.left is not None:
                nxtRowNodes.append(curNode.left)
            if curNode.right is not None:
                nxtRowNodes.append(curNode.right)

            if len(curRowNodes) == 0:
                curRowNodes = nxtRowNodes
                nxtRowNodes = deque()
                result.append(row)
                row = []
        return result

tgen = TreeGen()
#testTree0 = tgen.createBinaryTree("3,9,20,#,#,15,7")
testTree1 = tgen.createBinaryTree("1,2,3,4,#,#,5")

sol = Solution()
#print sol.levelOrder(testTree0)
print sol.levelOrder(testTree1)
