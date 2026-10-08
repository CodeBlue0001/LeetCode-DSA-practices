class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        stack=[]
        flag=0
        for p in s:
            if flag==0 and p=="(":
                flag=1
            elif flag==1 and p=="(":
                ans+=p
                stack+=[p]
            elif flag==1 and stack and p==")":
                stack.pop()
                ans+=p
            elif len(stack)==0 and p==")":
                flag=0
                
            # print(ans,stack)
        return ans
