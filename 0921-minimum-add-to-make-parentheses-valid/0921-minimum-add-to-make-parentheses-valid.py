class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        s2=[]
        c1,c2=0,0
        for p in s:
            if p=='(':
                c1+=1
                stack+=[p]
            elif stack and p==')':
                stack.pop()
                c2+=1
            elif s2 and p=='(':
                s2.pop()
            else:
                s2+=[p]
            print(stack,s2)
        print(stack,s2)
        return(len(stack)+len(s2))