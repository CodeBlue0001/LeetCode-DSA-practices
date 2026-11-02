class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        nums.sort()
        m=nums[len(nums)//2]
        for n in nums:
            ans+=abs(m-n)
        print(ans)
        return ans