class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        balence=[]
        for item in accounts:
            balence+=[sum(item)]
        return max(balence)
