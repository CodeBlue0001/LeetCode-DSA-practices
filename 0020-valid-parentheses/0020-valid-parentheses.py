class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i =="(":
                stack+=[")"]
            elif i=="{":
                stack+=['}']
            elif i=="[":
                stack+=["]"]
            
                # return False
            else:
                if stack:
                    if stack[-1]==i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            # print(stack)
        if stack:
            return False
        return True