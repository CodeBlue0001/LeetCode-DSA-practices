class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        l=max(nums)
        for n in nums:
            ans+=abs(n-l)
        return ans