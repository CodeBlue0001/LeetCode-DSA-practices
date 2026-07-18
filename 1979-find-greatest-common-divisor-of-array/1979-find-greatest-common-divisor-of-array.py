class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            g=1
            for i in range(1,b+1):
                if a%i==0 and b%i==0:
                    g=i
            return g
        return gcd(min(nums),max(nums))