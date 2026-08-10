class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        
        k=len(height)-1
        
        c=0
        
        i=0
        while i<k:
            min_=min(height[i],height[k])
            if min_*abs(i-k) > c :
                c=min_*abs(i-k)
            if height[i]<=height[k]:
                i+=1
            else:
                k-=1

        return c

