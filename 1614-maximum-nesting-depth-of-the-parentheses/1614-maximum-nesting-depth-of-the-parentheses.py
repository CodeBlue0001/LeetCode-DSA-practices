class Solution:
    def maxDepth(self, s: str) -> int:
        result=0
        stack=[]
        for p in s:
            if p=='(':
                stack.append(p)
                if result<len(stack):
                    result=len(stack)
            elif p==')':
                stack.pop()
                
        print(result)
        return result