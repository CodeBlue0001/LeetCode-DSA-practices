class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=0
        r= [n:=n+i for i in nums]
        # print(r)
        return r