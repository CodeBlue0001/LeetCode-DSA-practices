class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn=10
        alice=False
        while n>=turn:
            n-=turn

            alice=not alice
            turn-=1
            
        return alice