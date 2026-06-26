class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for s in words:
            f=0
            
            for i in s:
                
                if i not in allowed:
                    
                    f=1
                    break
            if f==0:
                c+=1
        return c