class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window=0
        for i in range(len(s)):
            sub=""
            sub+=s[i]
            for j in range(i+1,len(s)):
                if sub.count(s[j])<2:
                    sub+=s[j]
                else:
                    break
            if window<len(sub):
                print(sub)
                window=len(sub)
        return window
            
