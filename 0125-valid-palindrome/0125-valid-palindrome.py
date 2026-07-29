class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        lst="!@#$%^&*()_\"+-=\|{][}'?/;:.,<>*+ ~`"
        for i in lst:
            s=s.replace(i,"")
        s=s.lower()
        # print(cleaned)
        if s==s[::-1]:
            return True
        else:
            return False
