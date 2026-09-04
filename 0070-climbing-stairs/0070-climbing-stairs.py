class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        a,b=1,1
        c=0
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return c