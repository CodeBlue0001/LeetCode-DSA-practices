class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        stack=[]
        number="0123456789"
        s=s.split(" ")
        # print(s)
        for char in s:
            if char in number or char[0] in number:
                print(char)
                if stack:
                    if int(char)<=stack[-1]:
                        return False
                    else:
                        stack+=[int(char)]
                else:
                    stack+=[int(char)]
        print(stack)
        return True