class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        r=len(s)-1
        flag=1
        def check(l,r,flag):
            while l<r:
                
                if s[l]==s[r]:
                    l+=1
                    r-=1
                    # return check(l,r,flag)
                else:
                    #
                    if flag==0: 
                        return False
                    return check(l+1,r,flag-1) or check(l,r-1,flag-1)
                    
                        
            # if l==r and s[l]==s[r]:
            return True
            
        return check(l,r,flag)