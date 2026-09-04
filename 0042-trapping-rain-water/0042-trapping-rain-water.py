class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        n=len(height)
        l=[0]*n
        r=[0]*n
        
        lm=height[0]
        rm=height[-1]

        for i in range(n):
            l[i]=max(lm,height[i])
            lm=l[i]
        for i in range(n-1,-1,-1):
            r[i]=max(rm,height[i])
            rm=r[i]
        

        
        print(f"l:{l}\nr:{r}")        
        
        for i in range(len(height)):
            w=min(l[i],r[i])-height[i]
            print(f"{l[i]},{r[i]}-{height[i]}={w}")
            if w>0:
                water+=w
        return water
                    