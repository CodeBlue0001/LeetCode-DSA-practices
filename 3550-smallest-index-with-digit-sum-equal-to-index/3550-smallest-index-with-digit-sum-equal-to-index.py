class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(num:int)->int:
            sn=str(num)
            s=0
            for d in sn:
                s+=int(d)
            return s
        for i in range(len(nums)):
            s=digit_sum(nums[i])
            if i==s:
                return i
        return -1
            
