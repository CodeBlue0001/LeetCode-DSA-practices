class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ''' this code went time limit exceeded '''
        # for i in range(len(nums)):
        #     if max(nums[:i+1])-min(nums[i:])<=k:
        #         return i
        # return -1
        ''' using o(n) time and o(n) space approach'''
        l=len(nums)
        mx=[0]*l
        mn=[0]*l
        m=nums[0]
        n=nums[-1]

        for i in range(l):
            m=max(m,nums[i])
            mx[i]=m
        for i in range(l-1,-1,-1):
            n=min(n,nums[i])
            mn[i]=n

        

        for i in range(l):
            if mx[i]-mn[i]<=k:
                return i
        return -1