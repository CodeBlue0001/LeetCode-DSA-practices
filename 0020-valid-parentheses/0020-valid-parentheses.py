class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for p in s:
            if p in "({[":
                stack+=[p]
            else:
                if stack:
                    top=stack[-1]
                    if top=='('and p==')':
                        stack.pop()
                    elif top=='{' and p=='}':
                        stack.pop()
                    elif top=='[' and p==']':
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return False if stack else True
