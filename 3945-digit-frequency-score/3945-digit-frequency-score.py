class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solving using set
        uniq=set(str(n))
        ans=0
        for i in uniq:
            ans+=int(i)*(str(n).count(i))
        return ans