class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l=len(nums)
    
        result=sum(nums[i]*nums[i] for i in range(l) if l%(i+1)==0)
        print(result)
        return result