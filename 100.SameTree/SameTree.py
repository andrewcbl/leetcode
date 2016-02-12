import sys
sys.path.append('/home/bilongc/projects/leetcode/utils')
from TreeNode import TreeNode
from TreeGen import TreeGen

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None or q is None:
            return p is None and q is None

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

tgen = TreeGen()
testTree0 = tgen.createBinaryTree("1,2,3,4,#,#,5")
testTree1 = tgen.createBinaryTree("1,2,3,4,#,#,5")

sol = Solution()
print sol.isSameTree(testTree0, testTree1)

