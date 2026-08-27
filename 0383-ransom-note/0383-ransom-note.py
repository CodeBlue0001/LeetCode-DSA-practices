class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran=[]
        
        for r in ransomNote:
            
            if r not in ran:
                ran+=[r]
                if ransomNote.count(r)>magazine.count(r):
                    return False
        return True
