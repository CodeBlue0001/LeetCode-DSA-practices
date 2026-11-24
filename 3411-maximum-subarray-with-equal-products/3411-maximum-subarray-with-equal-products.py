class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # def prod(arr):
        #     n=1
        #     for i in arr:
        #         n*=i
        #     return n
        import math
        l=len(nums)
        ans=0
        if l<=1:
            return nums[0]

        for i in range(l):
            sub=[nums[i]]
            product=nums[i]
            for j in range(i+1,l):
                product*=nums[j]
                sub+=[nums[j]]
                lcm=math.lcm(*sub)
                gcd=math.gcd(*sub)
                if product==lcm*gcd:
                    if len(sub)>ans:
                        
                        ans=len(sub)
                else:
                    break
                if ans>l-i:
                    return ans 
        return ans