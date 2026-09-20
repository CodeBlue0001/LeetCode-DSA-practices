class Solution:
    def reverseDegree(self, s: str) -> int:
        map_str={}
        v='a'
        for i in range(26,0,-1):
            map_str[v]=i
            v=chr(ord(v)+1)
        # print(map_str)
        result=0
        for i,n in enumerate(s):
            result+=((i+1)*map_str[n])
        return result

        