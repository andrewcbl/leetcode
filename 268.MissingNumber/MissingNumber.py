class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        xor = 0

        for elem in nums:
            xor = xor ^ (elem)

        for i in xrange(0, n+1):
            xor = xor ^ i

        return xor

sol = Solution()
print sol.missingNumber([0,1,3])
print sol.missingNumber([0,1,2,3])
print sol.missingNumber([0])
print sol.missingNumber([1])
