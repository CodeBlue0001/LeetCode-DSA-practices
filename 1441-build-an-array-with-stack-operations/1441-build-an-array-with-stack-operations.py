class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        
        s=[]
        for i in range(1,max(target)+1):
            s.append("Push")
            if i not in target:
                s.append("Pop")
            
        return s
