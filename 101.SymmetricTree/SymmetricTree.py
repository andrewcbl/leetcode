import sys
sys.path.append('/home/bilongc/projects/leetcode/utils')
from TreeNode import TreeNode
from TreeGen import TreeGen

class Solution(object):
    def helper(self, p, q):
        if p is None or q is None:
            return p is None and q is None

        return p.val == q.val and self.helper(p.left, q.right) and self.helper(p.right, q.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.helper(root.left, root.right) 
