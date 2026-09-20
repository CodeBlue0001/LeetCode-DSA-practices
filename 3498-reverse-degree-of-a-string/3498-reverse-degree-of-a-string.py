class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        for i,char in enumerate(s):
            result+=((123-(ord(char)))*(i+1))
        return result