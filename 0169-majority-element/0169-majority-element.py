class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        max_=0
        for i , n in enumerate(nums):
            if n in freq:
                freq[n]+=1
                if freq[n]>len(nums)/2:
                    return n
            else:
                if len(nums)==1:
                    return n
                freq[n]=1
        # for n,f in freq.items():
        #     if f >len(nums)/2:
        #         return n