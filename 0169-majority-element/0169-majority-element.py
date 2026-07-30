class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i , n in enumerate(nums):
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        for n,f in freq.items():
            if f >len(nums)/2:
                return n