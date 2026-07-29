class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        flag=0
        for i in s[::-1]:
            if i !=' ':
                l+=1
                flag=1
            elif flag==1 and i==' ':
                break
        return l
                
