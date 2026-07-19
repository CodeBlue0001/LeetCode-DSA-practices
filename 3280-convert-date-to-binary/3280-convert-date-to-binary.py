class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def dec_to_binary(num):
            bi=''
            while(num):
                bit=num%2
                bi+=str(bit)
                num=num//2
            return bi[::-1]
        s=date.split('-')
        
        return dec_to_binary(int(s[0]))+"-"+dec_to_binary(int(s[1]))+"-"+dec_to_binary(int(s[2]))
        
        