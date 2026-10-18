class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        numeric_pattern={}
        j=0
        for char in (pattern):
            if char not in numeric_pattern:
                numeric_pattern[char]=j
                j+=1
        print(numeric_pattern)
        numeric_string={}
        i=0
        st=s.split(" ")
        for word in st:
            # print(word)
            if word not in numeric_string:
                numeric_string[word]=i
                i+=1
        print(numeric_string)
        pts=""
        sts=""
        for char in pattern:
            pts+=str(numeric_pattern[char])
        print(pts)
        for word in st:
            sts+=str(numeric_string[word])
        print(sts)
        if pts==sts:
            return True 
        return False
        