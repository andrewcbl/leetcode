import sys
sys.path.append('/home/bilongc/projects/leetcode/utils')
from TreeNode import TreeNode
from TreeGen import TreeGen

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numsDict = {}

        for i in xrange(0, len(nums)):
            elem = nums[i]
            if target - elem in numsDict.keys():
                return (numsDict[target-elem]+1, i+1)

            numsDict[elem] = i

        return (0, 0)

sol = Solution()
print sol.twoSum([2,7,11,15], 9)
