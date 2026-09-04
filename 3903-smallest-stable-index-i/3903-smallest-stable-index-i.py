class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        for i in range(len(nums)):
            n=max(nums[0:i+1])-min(nums[i:])
            if n<=k:
                return i
        
        return -1