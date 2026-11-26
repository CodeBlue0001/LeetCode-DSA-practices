class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn=10
        alice=False
        while n>=turn:
            n-=turn

            if alice==True:
                alice=False
            else:
                alice=True
            turn-=1
            
        return alice