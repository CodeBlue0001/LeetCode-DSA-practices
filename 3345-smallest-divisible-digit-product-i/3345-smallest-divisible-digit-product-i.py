class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def fn(num):
            mul = 1

            for i in str(num):
                mul *= int(i)
            return mul

        num=fn(10)
        
        for i in range(n,10+n):
            if fn(i)%t==0:
                return i