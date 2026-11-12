class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dcrs=1
        incrs=1
        ans=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                incrs+=1
                dcrs=1
            elif nums[i-1]>nums[i]:
                dcrs+=1
                incrs=1
            else:
                incrs=1
                dcrs=1
            ans=max(ans,dcrs,incrs)
        return ans
        