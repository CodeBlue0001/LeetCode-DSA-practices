class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst=[]
        for i in str(n):
            lst+=[int(i)]
        lst.sort(reverse=True)
        return lst[0]*lst[1]