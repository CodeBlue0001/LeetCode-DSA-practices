class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        w=1
        # mem={}
        ans=len(set(nums))**2
        while w<len(nums):
            for i in range(len(nums)):
                if i+w>len(nums):
                    continue
                distinct=set(nums[i:i+w])
                           
                ans+=len(distinct)**2
                # print(ans,distinct) 
            w+=1
        # print(ans)
        return ans
    