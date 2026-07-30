class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map=Counter(s)
        t_map=Counter(t)
        if len(s)!=len(t):
            return False
        print(s_map)
        for i in t:
            if i not in s:
                return False
            if s_map[i]!=t_map[i]:
                return False
        return True
