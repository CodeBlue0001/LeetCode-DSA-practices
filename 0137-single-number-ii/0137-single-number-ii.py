class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        has={}
        for num in nums:
            if num not in has:
                has[num]=1
            else:
                has[num]+=1
        for num,freq in has.items():
            if freq==1:
                return num