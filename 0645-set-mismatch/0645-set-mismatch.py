class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        l=len(nums)
        missing_number=(l*(l+1)/2)-sum(set(nums))
        print(int(missing_number))
        result=[]
        nums.sort()
        for i in range(1,l):
            if nums[i]==nums[i-1]:
                result+=[nums[i]]
        
        return result+[int(missing_number)]