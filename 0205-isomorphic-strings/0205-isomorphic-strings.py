class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        spat={}
        for i,char in enumerate(s):
            # print(char,i)
            if char not in spat:
                spat[char]=i
        pat=""
        for char in s:
            pat+=str(spat[char])+" "
        
        print(f"spat{spat},pat{pat}")
        wpat={}
        for i,char in enumerate(t):
            # print(char,i)
            if char not in wpat:
                wpat[char]=i
        tpat=""
        for char in t:
            tpat+=str(wpat[char])+" "

        print(f"spat{wpat},pat{tpat}")
        return tpat==pat
        