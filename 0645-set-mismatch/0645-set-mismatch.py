class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        l=len(nums)
        missing_number=(l*(l+1)/2)-sum(set(nums))
        print(int(missing_number))
        result=[]
        # nums.sort()
        # for i in range(1,l):
        #     if nums[i]==nums[i-1]:
        #         result+=[nums[i]]
        for i in range(1,l+1):
            try:
                nums.remove(i)
            except:
                pass
        print(result)
        return nums+[int(missing_number)]