class Solution:
    def reverseBits(self, n: int) -> int:
        bits=""
        while n:
            bits+=str(n%2)
            n//=2
        if len(bits)<32:
            bits+="0"*(32-len(bits))
        bits=bits[::-1]
        num=0
        for i in range(len(bits)):
            if bits[i]=="1":
                num+=2**i
        return num