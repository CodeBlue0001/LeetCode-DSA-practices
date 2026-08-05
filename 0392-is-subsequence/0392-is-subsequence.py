class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx=0
        cdx=len(s)
        for char in s:
            print(char)
            for i in range(idx,len(t)):
                if char==t[i]:
                    cdx-=1
                    idx=i+1
                    
                    print(t[idx:])
                    break
            # if condition==False:
            #     return False
        print(cdx)
        if cdx:
            return False
        return True
            
