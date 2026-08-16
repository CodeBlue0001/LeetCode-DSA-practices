class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        # types={}
        # k=0
        # for i in candyType:
        #     if i not in types:
        #         types[k]=i
        #         k+=1
        ct=set(candyType)
        l=len(candyType)/2
        if len(ct)>=l:
            return l
        else:
            return len(ct)
        