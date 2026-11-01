class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # window=[]
        total=None
        S=0
        lng=0
        i=0
        ptr=0
        while i<len(nums):
            S+=nums[i]
            lng+=1
            while S>=target:
                if total:   
                    total=min(total,lng)
                else:
                    total=lng
                S-=nums[ptr]
                ptr+=1
                lng-=1
                
                # window.pop(0)
                # print("pop",window)          
            i+=1
       

        # print(total)
        if total:
            return total
        return 0
