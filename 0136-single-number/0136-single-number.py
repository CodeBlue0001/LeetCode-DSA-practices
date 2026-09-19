class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # solving o(n) and o(1)
        xor=nums[0]
        for i in range(1,len(nums)):
            xor=xor^nums[i]
        return xor