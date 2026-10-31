class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans=0
        for i in range(1,n+1):
            if n%i==0 :
                ans=i
                k-=1
            if k==0:
                return ans
                
            
        return -1
