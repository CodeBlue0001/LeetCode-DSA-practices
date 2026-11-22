class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev=None
        number="0123456789"
        s=s.split(" ")
        # print(s)
        for char in s:
            if char in number or char[0] in number:
                
                if prev:
                    if int(char)<=prev:
                        return False
                    else:
                        prev=int(char)
                else:
                    prev=int(char)
        
        return True