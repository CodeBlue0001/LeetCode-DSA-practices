class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=0
        for i in range(len(nums)):
            nums[i]*=nums[i]
        nums.sort()
        l=len(nums)-1
        flag=1
        i=0
        while i<=l:
            if flag:
                r+=nums[l]
                l-=1
                flag=0
            else :
                r-=nums[i]
                i+=1
                flag=1
            
        return r
